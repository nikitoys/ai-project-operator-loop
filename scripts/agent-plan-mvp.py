#!/usr/bin/env python3
"""Dry-run helper for AI_PROJECT agent planning files.

This helper reads project-local AI_PROJECT/AGENT_* files and prints planning
reports. It never executes Codex, creates branches, merges changes, accepts
results or modifies application code.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path


AGENT_FILES = [
    Path("AGENT_PLAN.md"),
    Path("AGENT_TASKS.md"),
    Path("AGENT_LOCKS.md"),
    Path("AGENT_RESULTS.md"),
    Path("AGENT_METRICS.md"),
]

AWP_RE = re.compile(r"^AWP-[A-Za-z0-9_-]+$")
AWP_ID_RE = re.compile(r"\bAWP-[A-Za-z0-9_-]+\b")
EMPTY_VALUES = {"", "tbd", "none", "not checked", "not proposed", "n/a", "-"}
BLOCKED_STATUSES = {"blocked", "rejected", "archived", "deferred"}
COMPLETED_STATUSES = {"accepted", "complete", "completed", "done"}


@dataclass
class AgentPackage:
    id: str
    status: str = ""
    sop: str = ""
    role: str = ""
    parent_task: str = ""
    verification_mode: str = ""
    notes: str = ""
    allowed_files: list[str] = field(default_factory=list)
    locked_files: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)


def project_dir(project_root: Path) -> Path:
    return project_root.resolve() / "AI_PROJECT"


def read_agent_files(project_root: Path) -> tuple[dict[Path, str], list[Path]]:
    base = project_dir(project_root)
    present: dict[Path, str] = {}
    missing: list[Path] = []

    for relative in AGENT_FILES:
        path = base / relative
        if path.exists():
            present[relative] = path.read_text(encoding="utf-8")
        else:
            missing.append(relative)

    return present, missing


def table_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or all(set(cell) <= {"-", " "} for cell in cells):
            continue
        rows.append(cells)
    return rows


def split_files(value: str) -> list[str]:
    if value.strip().lower() in EMPTY_VALUES:
        return []
    parts = re.split(r"[,;]", value)
    return [part.strip() for part in parts if part.strip() and part.strip().lower() not in EMPTY_VALUES]


def unique_preserve_order(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result


def split_dependencies(value: str) -> list[str]:
    if value.strip().lower() in EMPTY_VALUES:
        return []
    return unique_preserve_order(AWP_ID_RE.findall(value))


def header_indexes(cells: list[str]) -> dict[str, int]:
    return {cell.strip().lower().replace("_", " "): index for index, cell in enumerate(cells)}


def parse_agent_tasks(text: str) -> dict[str, AgentPackage]:
    packages: dict[str, AgentPackage] = {}
    indexes: dict[str, int] = {}

    for cells in table_rows(text):
        if cells and not AWP_RE.match(cells[0]):
            possible_indexes = header_indexes(cells)
            if "id" in possible_indexes and (
                "dependencies" in possible_indexes or "depends on" in possible_indexes
            ):
                indexes = possible_indexes
            continue

        if len(cells) < 2 or not AWP_RE.match(cells[0]):
            continue

        dependency_index = indexes.get("dependencies", indexes.get("depends on"))
        package = AgentPackage(
            id=cells[0],
            status=cells[1] if len(cells) > 1 else "",
            sop=cells[2] if len(cells) > 2 else "",
            role=cells[3] if len(cells) > 3 else "",
            parent_task=cells[4] if len(cells) > 4 else "",
            verification_mode=cells[5] if len(cells) > 5 else "",
            notes=cells[6] if len(cells) > 6 else "",
            dependencies=split_dependencies(cells[dependency_index])
            if dependency_index is not None and dependency_index < len(cells)
            else [],
        )
        packages[package.id] = package

    detail_dependencies = parse_agent_task_detail_dependencies(text)
    for package_id, dependencies in detail_dependencies.items():
        if package_id in packages:
            packages[package_id].dependencies = unique_preserve_order(
                packages[package_id].dependencies + dependencies
            )

    return packages


def parse_agent_task_detail_dependencies(text: str) -> dict[str, list[str]]:
    dependencies: dict[str, list[str]] = {}
    current_package_id: str | None = None

    for line in text.splitlines():
        stripped = line.strip()
        header_match = re.match(r"^#+\s+(AWP-[A-Za-z0-9_-]+)\b", stripped)
        if header_match:
            current_package_id = header_match.group(1)
            continue

        if current_package_id is None:
            continue

        field_match = re.match(r"^(dependencies|depends_on|depends on)\s*:\s*(.+)$", stripped, re.IGNORECASE)
        if not field_match:
            continue

        dependencies[current_package_id] = unique_preserve_order(
            dependencies.get(current_package_id, []) + split_dependencies(field_match.group(2))
        )

    return dependencies


def parse_agent_plan_dependencies(text: str) -> dict[str, list[str]]:
    dependencies: dict[str, list[str]] = {}
    indexes: dict[str, int] = {}

    for cells in table_rows(text):
        lower_cells = [cell.strip().lower().replace("_", " ") for cell in cells]
        if "depends on" in lower_cells and ("package" in lower_cells or "agent work package" in lower_cells):
            indexes = header_indexes(cells)
            continue

        package_index = indexes.get("package", indexes.get("agent work package"))
        dependency_index = indexes.get("depends on")
        if package_index is None or dependency_index is None:
            continue
        if package_index >= len(cells) or dependency_index >= len(cells):
            continue

        package_ids = split_dependencies(cells[package_index])
        if len(package_ids) != 1:
            continue

        package_id = package_ids[0]
        dependencies[package_id] = unique_preserve_order(
            dependencies.get(package_id, []) + split_dependencies(cells[dependency_index])
        )

    return dependencies


def parse_agent_locks(text: str) -> dict[str, tuple[list[str], list[str]]]:
    locks: dict[str, tuple[list[str], list[str]]] = {}

    for cells in table_rows(text):
        if len(cells) < 3 or not AWP_RE.match(cells[0]):
            continue
        locks[cells[0]] = (split_files(cells[1]), split_files(cells[2]))

    return locks


def load_packages(project_root: Path) -> tuple[dict[str, AgentPackage], dict[Path, str], list[Path]]:
    present, missing = read_agent_files(project_root)
    packages = parse_agent_tasks(present.get(Path("AGENT_TASKS.md"), ""))
    plan_dependencies = parse_agent_plan_dependencies(present.get(Path("AGENT_PLAN.md"), ""))
    locks = parse_agent_locks(present.get(Path("AGENT_LOCKS.md"), ""))

    for package_id, dependencies in plan_dependencies.items():
        if package_id in packages:
            packages[package_id].dependencies = unique_preserve_order(
                packages[package_id].dependencies + dependencies
            )

    for package_id, (allowed_files, locked_files) in locks.items():
        package = packages.setdefault(package_id, AgentPackage(id=package_id))
        package.allowed_files = allowed_files
        package.locked_files = locked_files

    return packages, present, missing


def normalized_status(package: AgentPackage) -> str:
    return package.status.strip().lower()


def is_blocked(package: AgentPackage) -> bool:
    return normalized_status(package) in BLOCKED_STATUSES


def is_complete(package: AgentPackage) -> bool:
    return normalized_status(package) in COMPLETED_STATUSES


def missing_dependency_errors(packages: dict[str, AgentPackage]) -> list[str]:
    errors: list[str] = []
    package_ids = set(packages)

    for package in packages.values():
        missing = [dependency for dependency in package.dependencies if dependency not in package_ids]
        if missing:
            errors.append(f"missing dependency for {package.id}: {', '.join(missing)}")

    return errors


def cycle_errors(packages: dict[str, AgentPackage]) -> list[str]:
    errors: list[str] = []
    state: dict[str, str] = {}
    path: list[str] = []

    def visit(package_id: str) -> None:
        if state.get(package_id) == "done":
            return
        if state.get(package_id) == "visiting":
            start = path.index(package_id)
            errors.append("dependency cycle: " + " -> ".join(path[start:] + [package_id]))
            return

        state[package_id] = "visiting"
        path.append(package_id)
        for dependency in packages[package_id].dependencies:
            if dependency in packages:
                visit(dependency)
        path.pop()
        state[package_id] = "done"

    for package_id in packages:
        if state.get(package_id) is None:
            visit(package_id)

    return unique_preserve_order(errors)


def dependency_validation_errors(packages: dict[str, AgentPackage]) -> list[str]:
    return missing_dependency_errors(packages) + cycle_errors(packages)


def completed_package_ids(packages: dict[str, AgentPackage]) -> set[str]:
    return {package.id for package in packages.values() if is_complete(package)}


def incomplete_prerequisites(package: AgentPackage, completed: set[str]) -> list[str]:
    return [dependency for dependency in package.dependencies if dependency not in completed]


def ready_packages(packages: dict[str, AgentPackage]) -> list[AgentPackage]:
    completed = completed_package_ids(packages)
    ready: list[AgentPackage] = []

    for package in packages.values():
        if is_complete(package) or is_blocked(package):
            continue
        if not incomplete_prerequisites(package, completed):
            ready.append(package)

    return ready


def topological_layers(packages: dict[str, AgentPackage]) -> list[list[str]]:
    satisfied = completed_package_ids(packages)
    remaining = {
        package.id
        for package in packages.values()
        if not is_complete(package) and not is_blocked(package)
    }
    layers: list[list[str]] = []

    while remaining:
        layer = [
            package_id
            for package_id in packages
            if package_id in remaining and not incomplete_prerequisites(packages[package_id], satisfied)
        ]
        if not layer:
            break
        layers.append(layer)
        remaining.difference_update(layer)
        satisfied.update(layer)

    return layers


def dependency_exclusions(packages: dict[str, AgentPackage], ready_ids: set[str]) -> list[str]:
    completed = completed_package_ids(packages)
    exclusions: list[str] = []

    for package in packages.values():
        if package.id in ready_ids or is_complete(package):
            continue
        if is_blocked(package):
            exclusions.append(f"{package.id}: excluded because status is {package.status or 'unknown'}")
            continue

        incomplete = incomplete_prerequisites(package, completed)
        if incomplete:
            exclusions.append(f"{package.id}: waiting for incomplete prerequisites: {', '.join(incomplete)}")

    return exclusions


def lock_conflicts(packages: dict[str, AgentPackage]) -> dict[str, list[str]]:
    by_file: dict[str, list[str]] = {}
    for package in packages.values():
        for locked_file in package.locked_files:
            by_file.setdefault(locked_file, []).append(package.id)
    return {path: ids for path, ids in by_file.items() if len(ids) > 1}


def print_boundary() -> None:
    print("Boundary:")
    print("- dry-run/reporting only")
    print("- does not execute Codex")
    print("- does not create branches, worktrees, commits or merges")
    print("- does not modify AI_PROJECT files or application code")
    print("- does not accept results")
    print("- candidate parallel groups are informational only")


def command_validate(args: argparse.Namespace) -> int:
    packages, present, missing = load_packages(args.project_root)

    print_boundary()
    print("Project Root:", args.project_root.resolve())
    print("AI_PROJECT:", project_dir(args.project_root))
    print("Agent Planning Files:")
    for relative in AGENT_FILES:
        status = "present" if relative in present else "missing"
        print(f"- {status}: AI_PROJECT/{relative.as_posix()}")

    print("Agent Work Packages:")
    if not packages:
        print("- none recognized in AI_PROJECT/AGENT_TASKS.md")
    else:
        for package in packages.values():
            incomplete = [
                name
                for name, value in [
                    ("status", package.status),
                    ("sop", package.sop),
                    ("role", package.role),
                    ("parent_task", package.parent_task),
                    ("verification_mode", package.verification_mode),
                ]
                if value.strip().lower() in EMPTY_VALUES
            ]
            suffix = f" incomplete: {', '.join(incomplete)}" if incomplete else " complete enough for planning"
            dependencies = ", ".join(package.dependencies) if package.dependencies else "none"
            print(f"- {package.id}: {package.status or 'unknown'};{suffix}; dependencies=[{dependencies}]")

    errors = dependency_validation_errors(packages)
    if errors:
        print("Dependency Validation: failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Dependency Validation: passed")
    return 0


def command_check_locks(args: argparse.Namespace) -> int:
    packages, _, missing = load_packages(args.project_root)
    print_boundary()

    if Path("AGENT_LOCKS.md") in missing:
        print("Lock Source: missing AI_PROJECT/AGENT_LOCKS.md")
    else:
        print("Lock Source: AI_PROJECT/AGENT_LOCKS.md")

    if not packages:
        print("Lock Check: no Agent Work Packages recognized")
        return 0

    for package in packages.values():
        allowed = ", ".join(package.allowed_files) if package.allowed_files else "none recorded"
        locked = ", ".join(package.locked_files) if package.locked_files else "none recorded"
        print(f"- {package.id}: allowed_files=[{allowed}] locked_files=[{locked}]")

    conflicts = lock_conflicts(packages)
    if not conflicts:
        print("Lock Conflicts: none detected from available data")
        return 0

    print("Lock Conflicts:")
    for locked_file, package_ids in conflicts.items():
        print(f"- {locked_file}: {', '.join(package_ids)}")
    return 0


def command_list_parallel_groups(args: argparse.Namespace) -> int:
    packages, _, _ = load_packages(args.project_root)
    print_boundary()
    print("Parallel Group Policy: informational only; not executable until Human Owner approval")

    conflicts = lock_conflicts(packages)
    if conflicts:
        print("Candidate Parallel Groups: none; locked-file conflicts must be resolved first")
        for locked_file, package_ids in conflicts.items():
            print(f"- conflict {locked_file}: {', '.join(package_ids)}")
        return 0

    errors = dependency_validation_errors(packages)
    if errors:
        print("Dependency Validation: failed")
        for error in errors:
            print(f"- {error}")
        return 1

    if len(packages) < 2:
        print("Candidate Parallel Groups: none; fewer than two Agent Work Packages recognized")
        return 0

    completed = completed_package_ids(packages)
    ready = ready_packages(packages)
    ready_ids = {package.id for package in ready}
    ready_labels = [package.id for package in ready]

    print("Dependency Validation: passed")
    print("Completed/Satisfied Prerequisites:", ", ".join(sorted(completed)) if completed else "none")
    print("Ready Dependency Layer:")
    if ready_labels:
        print(f"- ready_layer_1: {', '.join(ready_labels)}")
        print("  reason: all listed packages are unblocked and all AWP prerequisites are complete/satisfied")
    else:
        print("- none")

    layers = topological_layers(packages)
    if layers:
        print("Topological Dependency Layers:")
        for index, layer in enumerate(layers, 1):
            marker = "current_ready" if index == 1 else "future_after_prior_layers_complete"
            print(f"- layer_{index}: {', '.join(layer)}")
            print(f"  status: {marker}")

    exclusions = dependency_exclusions(packages, ready_ids)
    if exclusions:
        print("Excluded Packages:")
        for exclusion in exclusions:
            print(f"- {exclusion}")

    if len(ready) < 2:
        print("Candidate Parallel Groups: none; ready dependency layer has fewer than two packages")
        return 0

    print("Candidate Parallel Groups:")
    print(f"- candidate_group_1: {', '.join(ready_labels)}")
    print("  status: informational_only")
    print("  execution_authorized: no")
    print("  human_owner_approval_required: yes")
    print("  validity: all listed packages are unblocked and have only complete/satisfied AWP prerequisites")
    return 0


def prompt_ready(package: AgentPackage) -> bool:
    required = [package.id, package.status, package.sop, package.role, package.parent_task, package.verification_mode]
    return all(value.strip().lower() not in EMPTY_VALUES for value in required)


def command_generate_prompts(args: argparse.Namespace) -> int:
    packages, _, _ = load_packages(args.project_root)
    print_boundary()
    print("Prompt Drafts: generated for review only; not sent to Codex")

    if not packages:
        print("- none; no Agent Work Packages recognized")
        return 0

    generated = 0
    for package in packages.values():
        if not prompt_ready(package):
            print(f"- skipped {package.id}: insufficient package data for bounded prompt draft")
            continue

        generated += 1
        allowed = ", ".join(package.allowed_files) if package.allowed_files else "Use parent task allowed files; confirm before execution."
        locked = ", ".join(package.locked_files) if package.locked_files else "No locked files recorded; confirm before execution."
        print()
        print(f"## Prompt Draft: {package.id}")
        print("[CODEX]")
        print(f"Active Role: {package.role}")
        print("Active Stage: Agent Work Package Execution")
        print("Active Document: AI_PROJECT/AGENT_TASKS.md")
        print(f"Expected Result: bounded result for {package.id}; no automatic acceptance")
        print()
        print("Task:")
        print(f"- Parent task: {package.parent_task}")
        print(f"- SOP: {package.sop}")
        print(f"- Agent Work Package: {package.id}")
        print(f"- Verification Mode: {package.verification_mode}")
        print()
        print("Allowed Files:")
        print(f"- {allowed}")
        print()
        print("Locked Files:")
        print(f"- {locked}")
        print()
        print("Forbidden Actions:")
        print("- Do not execute unrelated work.")
        print("- Do not modify files outside allowed_files.")
        print("- Do not create branches, worktrees, commits or merges.")
        print("- Do not accept results automatically.")
        print()
        print("Expected Output:")
        print("- Changed files")
        print("- Summary")
        print("- Checks performed")
        print("- Errors or blockers")
        print("- Questions")
        print("- Diff or key changes")

    if generated == 0:
        print("No prompt drafts generated.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dry-run agent planning helper for AI_PROJECT files.")
    parser.add_argument(
        "command",
        choices=["validate", "check-locks", "list-parallel-groups", "generate-prompts"],
    )
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "validate":
        return command_validate(args)
    if args.command == "check-locks":
        return command_check_locks(args)
    if args.command == "list-parallel-groups":
        return command_list_parallel_groups(args)
    if args.command == "generate-prompts":
        return command_generate_prompts(args)

    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
