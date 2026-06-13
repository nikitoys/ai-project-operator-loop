# Verification Modes

Status: Draft
Version: v0.2.0

## Purpose

This document defines explicit verification modes for Codex execution, review and QA inside projects managed by the AI Development System.

Verification mode is part of scope control. It defines which checks are allowed, which checks are optional, which checks are forbidden unless explicitly requested, and how much time may be spent on verification.

## Core Rule

Do not run all tests by default.

Run the minimum sufficient verification set for the current task, within an explicit verification budget.

Codex Executor must not silently upgrade the verification mode. If a stronger mode is needed, report the recommendation instead of running it.

Do not say "all tests passed" unless all relevant tests for the selected mode actually ran. Prefer mode-specific wording such as:

```text
FAST verification passed.
STANDARD verification passed.
```

## Browser and Visual QA Boundary

Browser automation, Playwright/MCP browser sessions, screenshots, manual visual inspections and browser console checks are on-demand QA only.

Do not run them unless the Human Owner explicitly requests them or the current task explicitly lists them in acceptance criteria.

Do not mark a task `PARTIAL` only because browser checks, screenshots, visual inspection or console checks were skipped, unless those checks were explicitly required for that task.

## Verification Budget Fields

Codex tasks and prompt packages should include:

```text
Verification Mode:
Verification Budget:
Allowed Slow Checks: true/false
Runtime Tracking: enabled/disabled
```

When a budget is not specified, use the mode default below and report that default in the final result.

## Mode: NONE

Budget: 0 sec.

No command execution.

Use when the task is analysis-only, prompt-only, or when execution is unsafe or not approved.

Required output:

- explain verification risk;
- list checks that were not run;
- recommend the smallest next verification mode if needed.

## Mode: SMOKE

Budget: 30 sec.

Run only instant critical checks.

Use for very small documentation or metadata changes where a minimal scope/safety signal is enough.

Allowed:

- instant checks;
- critical checks that fit the budget;
- dry-run checks that do not execute project work.

Forbidden unless explicitly requested:

- fast/standard/slow/expensive checks;
- full repository checks;
- browser or visual QA.

## Mode: FAST

Budget: 120 sec.

Run instant and fast checks relevant to changed files.

Use for ordinary code-only changes, documentation changes and fast bugfixes.

Allowed:

- instant checks;
- fast checks relevant to changed files;
- local syntax, parse or metadata checks when they fit the budget;
- typecheck or focused tests only when they are known to be fast for the repository.

Forbidden unless explicitly requested:

- slow checks;
- full repository exhaustive checks;
- release/golden checks;
- browser or visual QA.

## Mode: STANDARD

Budget: 300 sec.

Run `FAST` plus selected standard checks if they fit the budget.

Use when the task explicitly asks for standard validation or when the change touches shared workflow, lifecycle, policy or tooling behavior.

Allowed:

- all checks allowed by `FAST`;
- selected standard checks that fit the remaining budget;
- dry-run or smoke verification for new tooling.

Forbidden unless explicitly requested:

- slow checks;
- expensive checks;
- release/golden checks;
- browser or visual QA.

## Mode: FULL

Requires explicit request, release context, CI/nightly context, or a task that explicitly selects `FULL`.

No default local budget. The task must declare a budget.

May run slow checks when slow checks are explicitly allowed and they fit the declared budget.

Required output:

- total runtime;
- checks run;
- checks skipped;
- slow checks run or skipped;
- remaining risks.

`FULL` must never be selected silently.

## Mode: RELEASE

Requires explicit Human Owner request or release task.

No default local budget. The task must declare a budget.

Runs release-critical checks, including slow or golden checks when available and when they fit the declared budget.

Required output:

- total runtime;
- release-critical checks;
- slow/golden checks run or skipped;
- explicit risk statement.

`RELEASE` must never be selected silently.

## Mode: MANUAL

Human Owner explicitly chooses checks.

Budget and slow-check permission must be declared by the Human Owner or the task.

Use when the Human Owner wants a custom verification set rather than a standard mode.

## Nightly Context

`NIGHTLY` may appear in machine-readable check registries as an automation context, not as a default Codex mode.

Nightly execution requires separate approval and must not be inferred from ordinary local work.

## Legacy Compatibility

Older project templates may still use these names:

| Legacy Name | Current Meaning |
| --- | --- |
| `CODE_ONLY_FAST` | Use `FAST` unless the task explicitly chooses `NONE` or `SMOKE`. |
| `FAST_VALIDATION` | Use `STANDARD` unless the task declares a smaller budget. |
| `BROWSER_SMOKE` | On-demand browser QA overlay; requires explicit Human Owner request or acceptance criteria. |
| `VISUAL_QA` | On-demand visual QA overlay; requires explicit Human Owner request or acceptance criteria. |

These aliases exist for compatibility. New prompt packages should prefer `NONE`, `SMOKE`, `FAST`, `STANDARD`, `FULL`, `RELEASE` or `MANUAL`.

## Mode Selection Rules

- If no verification mode is specified, use `FAST` for ordinary code-only changes, documentation changes and fast bugfixes.
- If the task specifies `STANDARD`, use `STANDARD` and its declared or default 300 sec budget.
- If the task specifies `FULL`, `RELEASE` or `MANUAL`, require explicit budget and slow-check permission before running slow checks.
- Do not infer browser or visual QA from the word `check` alone.
- Do not run slower checks because they are available.
- Do not silently upgrade from `FAST` to `STANDARD`, `FULL` or `RELEASE`.
- If a stronger mode is recommended, report the recommendation instead of running it.

## Registry Relationship

Machine-readable check metadata is stored in:

```text
/ai-system/spec/verification-checks.json
```

The registry defines check IDs, value classes, speed classes, expected durations, timeouts, default modes and whether a check is blocking by default.

Markdown remains the source of truth for policy. The registry is a machine-readable inventory used by lightweight tooling.

## Runtime Tracking Relationship

Runtime tracking is defined in:

```text
/ai-system/test-runtime-tracking.md
```

Every executed check should record measured wall-clock duration. Every skipped check should record an explicit reason.

A check without measured runtime must not be reported as fully verified.

## Prompt Package Relationship

Codex prompt packages should include:

```text
Verification Mode:
Verification Budget:
Allowed Slow Checks:
Runtime Tracking:
```

The verification mode must align with allowed checks and forbidden actions.

If a task needs stronger checks, the prompt must explicitly say so.

## Review Relationship

Reviewers must evaluate whether Codex obeyed the declared verification mode and budget.

Skipping browser, visual, slow, release or full checks is not a review failure when the declared mode does not allow or require those checks.

Running browser, Playwright, screenshots, console inspection, manual visual QA, slow checks, full checks or release checks outside the declared mode is a scope violation unless explicitly approved by the Human Owner.
