#!/usr/bin/env python3
"""Lightweight verification runner for AI_Development_System.

The runner loads a machine-readable verification registry, selects checks by
mode and budget, records executed and skipped checks as JSONL, and avoids slow
checks unless the selected mode and flags allow them.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = ROOT / "ai-system/spec/verification-checks.json"
DEFAULT_HISTORY = ROOT / "outputs/verification-history.jsonl"

MODE_DEFAULT_BUDGETS = {
    "NONE": 0,
    "SMOKE": 30,
    "FAST": 120,
    "STANDARD": 300,
}

MODE_SPEEDS = {
    "NONE": set(),
    "SMOKE": {"instant"},
    "FAST": {"instant", "fast"},
    "STANDARD": {"instant", "fast", "standard"},
    "FULL": {"instant", "fast", "standard", "slow", "expensive"},
    "RELEASE": {"instant", "fast", "standard", "slow", "expensive"},
    "MANUAL": {"instant", "fast", "standard", "slow", "expensive"},
    "NIGHTLY": {"instant", "fast", "standard", "slow", "expensive"},
}

LEGACY_MODE_ALIASES = {
    "CODE_ONLY_FAST": "FAST",
    "FAST_VALIDATION": "STANDARD",
}

VALUE_SCORES = {
    "critical": 100,
    "high": 50,
    "medium": 20,
    "low": 5,
}

SLOW_SPEEDS = {"slow", "expensive"}


@dataclass
class RunStats:
    executed: int = 0
    skipped: int = 0
    failed_blocking: int = 0
    incomplete_blocking: int = 0
    used_time: float = 0.0


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run bounded verification checks.")
    parser.add_argument("--mode", default="FAST", help="Verification mode, such as FAST or STANDARD.")
    parser.add_argument("--budget-sec", type=float, help="Total verification budget in seconds.")
    parser.add_argument("--dry-run", action="store_true", help="Select and report checks without executing commands.")
    parser.add_argument("--allow-slow", action="store_true", help="Allow slow/expensive checks when the mode also allows them.")
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY), help="Path to verification-checks.json.")
    parser.add_argument("--history-path", default=str(DEFAULT_HISTORY), help="Path for JSONL runtime history.")
    parser.add_argument("--task-id", help="Optional task ID to record in JSONL events.")
    parser.add_argument("--changed-files-count", type=int, help="Optional changed files count to record.")
    return parser.parse_args()


def normalize_mode(raw_mode: str) -> str:
    mode = raw_mode.strip().upper().replace("-", "_")
    mode = LEGACY_MODE_ALIASES.get(mode, mode)
    if mode not in MODE_SPEEDS:
        valid = ", ".join(sorted(MODE_SPEEDS))
        raise ValueError(f"Unsupported verification mode {raw_mode!r}. Valid modes: {valid}")
    return mode


def resolve_budget(mode: str, raw_budget: float | None) -> float:
    if raw_budget is not None:
        if raw_budget < 0:
            raise ValueError("--budget-sec must be non-negative")
        return raw_budget
    if mode in MODE_DEFAULT_BUDGETS:
        return float(MODE_DEFAULT_BUDGETS[mode])
    raise ValueError(f"{mode} requires an explicit --budget-sec")


def load_registry(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    items = data.get("items")
    if not isinstance(items, list):
        raise ValueError(f"{path}: expected top-level 'items' list")
    return items


def value_score(check: dict[str, Any]) -> int:
    return VALUE_SCORES.get(str(check.get("value_class", "")).lower(), 0)


def priority_score(check: dict[str, Any]) -> float:
    expected = float(check.get("expected_duration_sec") or 1)
    return value_score(check) / max(expected, 1.0)


def sort_checks(checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        checks,
        key=lambda check: (
            not bool(check.get("blocking_by_default")),
            -value_score(check),
            float(check.get("expected_duration_sec") or 0),
            -priority_score(check),
            str(check.get("id", "")),
        ),
    )


def mode_allows_slow(mode: str, allow_slow: bool) -> bool:
    if mode in {"RELEASE", "NIGHTLY"}:
        return True
    if mode in {"FULL", "MANUAL"}:
        return allow_slow
    return False


def command_args(command: Any) -> list[str] | None:
    if command is None:
        return None
    if isinstance(command, list) and all(isinstance(item, str) for item in command):
        return command
    return []


def make_event(
    *,
    run_id: str,
    task_id: str | None,
    check: dict[str, Any],
    mode: str,
    started_at: str,
    finished_at: str,
    duration_sec: float,
    result: str,
    exit_code: int | None,
    reason_for_run: str | None,
    reason_for_skip: str | None,
    changed_files_count: int | None,
    dry_run: bool,
) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "task_id": task_id,
        "check_id": check.get("id"),
        "verification_mode": mode,
        "started_at": started_at,
        "finished_at": finished_at,
        "duration_sec": round(duration_sec, 3),
        "result": result,
        "exit_code": exit_code,
        "timeout_sec": check.get("timeout_sec"),
        "blocking": bool(check.get("blocking_by_default")),
        "reason_for_run": reason_for_run,
        "reason_for_skip": reason_for_skip,
        "changed_files_count": changed_files_count,
        "dry_run": dry_run,
    }


def append_event(history_path: Path, event: dict[str, Any]) -> None:
    history_path.parent.mkdir(parents=True, exist_ok=True)
    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")


def skipped_event(
    *,
    run_id: str,
    task_id: str | None,
    check: dict[str, Any],
    mode: str,
    reason_for_skip: str,
    reason_for_run: str | None,
    changed_files_count: int | None,
    dry_run: bool,
) -> dict[str, Any]:
    now = utc_now()
    return make_event(
        run_id=run_id,
        task_id=task_id,
        check=check,
        mode=mode,
        started_at=now,
        finished_at=now,
        duration_sec=0.0,
        result="skipped",
        exit_code=None,
        reason_for_run=reason_for_run,
        reason_for_skip=reason_for_skip,
        changed_files_count=changed_files_count,
        dry_run=dry_run,
    )


def run_check(
    *,
    run_id: str,
    task_id: str | None,
    check: dict[str, Any],
    mode: str,
    args: list[str],
    changed_files_count: int | None,
) -> dict[str, Any]:
    started_at = utc_now()
    start = time.monotonic()
    timeout = float(check.get("timeout_sec") or 0)
    exit_code: int | None
    result: str

    try:
        completed = subprocess.run(
            args,
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout if timeout > 0 else None,
            check=False,
        )
        exit_code = completed.returncode
        result = "passed" if completed.returncode == 0 else "failed"
    except subprocess.TimeoutExpired:
        exit_code = None
        result = "timeout"

    duration_sec = time.monotonic() - start
    finished_at = utc_now()
    return make_event(
        run_id=run_id,
        task_id=task_id,
        check=check,
        mode=mode,
        started_at=started_at,
        finished_at=finished_at,
        duration_sec=duration_sec,
        result=result,
        exit_code=exit_code,
        reason_for_run=f"{check.get('value_class')} {check.get('speed_class')} check selected by {mode}",
        reason_for_skip=None,
        changed_files_count=changed_files_count,
        dry_run=False,
    )


def select_or_run(
    checks: list[dict[str, Any]],
    *,
    mode: str,
    budget_sec: float,
    dry_run: bool,
    allow_slow: bool,
    history_path: Path,
    task_id: str | None,
    changed_files_count: int | None,
) -> tuple[list[dict[str, Any]], list[str], RunStats]:
    run_id = str(uuid.uuid4())
    remaining = budget_sec
    events: list[dict[str, Any]] = []
    warnings: list[str] = []
    stats = RunStats()

    for check in sort_checks(checks):
        check_id = str(check.get("id"))
        speed_class = str(check.get("speed_class", "")).lower()
        expected = float(check.get("expected_duration_sec") or 0)
        default_modes = {str(item).upper() for item in check.get("default_modes", [])}
        command = command_args(check.get("command"))
        reason_for_run = f"{check.get('value_class')} {speed_class} check selected by {mode}"
        reason_for_skip: str | None = None

        if mode == "NONE":
            reason_for_skip = "mode NONE permits no command execution"
        elif mode not in default_modes:
            reason_for_skip = f"check is outside selected mode {mode}"
        elif speed_class not in MODE_SPEEDS[mode]:
            reason_for_skip = f"speed class {speed_class} is outside selected mode {mode}"
        elif speed_class in SLOW_SPEEDS and not mode_allows_slow(mode, allow_slow):
            reason_for_skip = "slow/expensive checks require an explicit mode and slow-check permission"
        elif expected > remaining:
            reason_for_skip = f"expected duration {expected:g}s exceeds remaining budget {remaining:g}s"
        elif command is None:
            reason_for_skip = "command is not implemented in the registry"
        elif command == []:
            reason_for_skip = "command format is unsupported; use a JSON array of strings"
        elif dry_run:
            reason_for_skip = "dry-run mode selected; command was not executed"
            remaining -= expected

        if reason_for_skip:
            event = skipped_event(
                run_id=run_id,
                task_id=task_id,
                check=check,
                mode=mode,
                reason_for_skip=reason_for_skip,
                reason_for_run=reason_for_run if mode in default_modes else None,
                changed_files_count=changed_files_count,
                dry_run=dry_run,
            )
            events.append(event)
            append_event(history_path, event)
            stats.skipped += 1
            if bool(check.get("blocking_by_default")) and mode in default_modes and reason_for_skip != "dry-run mode selected; command was not executed":
                stats.incomplete_blocking += 1
            continue

        event = run_check(
            run_id=run_id,
            task_id=task_id,
            check=check,
            mode=mode,
            args=command,
            changed_files_count=changed_files_count,
        )
        events.append(event)
        append_event(history_path, event)
        stats.executed += 1
        stats.used_time += float(event["duration_sec"])
        remaining = max(0.0, remaining - float(event["duration_sec"]))

        if event["result"] in {"failed", "timeout"} and event["blocking"]:
            stats.failed_blocking += 1
        if float(event["duration_sec"]) > expected:
            warnings.append(f"{check_id}: duration {event['duration_sec']}s exceeded expected {expected:g}s")
        if speed_class == "fast" and float(event["duration_sec"]) > 60:
            warnings.append(f"{check_id}: fast check exceeded 60s and should be optimized or reclassified")
        if speed_class == "standard" and float(event["duration_sec"]) > 300:
            warnings.append(f"{check_id}: standard check exceeded 5 minutes and should not be normal verification")

    return events, warnings, stats


def overall_result(dry_run: bool, stats: RunStats) -> str:
    if dry_run:
        return "dry_run"
    if stats.failed_blocking:
        return "failed"
    if stats.incomplete_blocking or stats.executed == 0:
        return "incomplete"
    return "passed"


def print_summary(
    *,
    mode: str,
    budget_sec: float,
    history_path: Path,
    dry_run: bool,
    events: list[dict[str, Any]],
    warnings: list[str],
    stats: RunStats,
) -> None:
    print("Verification Summary")
    print(f"Mode: {mode}")
    print(f"Budget: {budget_sec:g}s")
    print(f"Used time: {stats.used_time:.3f}s")
    print(f"Overall result: {overall_result(dry_run, stats)}")
    print(f"History: {history_path.relative_to(ROOT) if history_path.is_relative_to(ROOT) else history_path}")
    print()
    print("Checks:")
    for event in events:
        impact = "blocking" if event["blocking"] else "advisory"
        print(f"- {event['check_id']}: {event['result']}, {event['duration_sec']}s, {impact}")
    print()
    print("Skipped:")
    skipped = [event for event in events if event["result"] == "skipped"]
    if not skipped:
        print("- none")
    else:
        for event in skipped:
            print(f"- {event['check_id']}: {event['reason_for_skip']}")
    print()
    print("Runtime Warnings:")
    if not warnings:
        print("- none")
    else:
        for warning in warnings:
            print(f"- {warning}")


def main() -> int:
    try:
        args = parse_args()
        mode = normalize_mode(args.mode)
        budget_sec = resolve_budget(mode, args.budget_sec)
        registry_path = Path(args.registry)
        if not registry_path.is_absolute():
            registry_path = ROOT / registry_path
        history_path = Path(args.history_path)
        if not history_path.is_absolute():
            history_path = ROOT / history_path
        checks = load_registry(registry_path)
        events, warnings, stats = select_or_run(
            checks,
            mode=mode,
            budget_sec=budget_sec,
            dry_run=args.dry_run,
            allow_slow=args.allow_slow,
            history_path=history_path,
            task_id=args.task_id,
            changed_files_count=args.changed_files_count,
        )
        print_summary(
            mode=mode,
            budget_sec=budget_sec,
            history_path=history_path,
            dry_run=args.dry_run,
            events=events,
            warnings=warnings,
            stats=stats,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Verification runner failed: {exc}", file=sys.stderr)
        return 2

    result = overall_result(args.dry_run, stats)
    if result in {"failed", "incomplete"}:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
