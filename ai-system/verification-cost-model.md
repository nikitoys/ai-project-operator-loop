# Verification Cost Model

Status: Draft
Version: v0.1.0

## Purpose

This document defines how the AI Development System chooses verification checks by cost, value, risk coverage and available time budget.

Verification is not "run everything by default". Verification should be sufficient for the current task, bounded by the declared verification mode and budget, and explicit about what was skipped.

## Core Principle

Run the minimum sufficient verification set for the current task.

Do not run slow, full, release, browser, visual or golden-scenario checks unless the Human Owner explicitly requested them or the selected verification mode requires them.

## Speed Classes

| Speed Class | Expected Runtime |
| --- | --- |
| `instant` | expected <= 10 sec |
| `fast` | expected <= 60 sec |
| `standard` | expected <= 5 min |
| `slow` | expected <= 20 min |
| `expensive` | expected > 20 min |

Speed class is an estimate until measured runtime history exists. When runtime history shows consistent drift, the check should be optimized or reclassified.

## Value Classes

| Value Class | Meaning |
| --- | --- |
| `critical` | Protects correctness, scope, safety or release integrity. |
| `high` | Catches likely regressions or important documentation/spec drift. |
| `medium` | Useful confidence signal, but not always required for every task. |
| `low` | Informational or narrow confidence signal. |

## Check Result Types

| Result | Meaning |
| --- | --- |
| `passed` | The check ran and returned success inside its timeout. |
| `failed` | The check ran and returned failure. |
| `skipped` | The check did not run and must include `reason_for_skip`. |
| `timeout` | The check exceeded its timeout. |
| `not_applicable` | The check does not apply to the task or changed files. |

## Check Impact

Checks have one of two impact levels:

| Impact | Meaning |
| --- | --- |
| `blocking` | Failure blocks acceptance unless the Human Owner explicitly accepts the risk. |
| `advisory` | Failure or skip must be reported, but does not automatically block acceptance. |

`blocking=true` should be reserved for fast or high-confidence checks that protect correctness, scope, safety or release integrity.

Slow and expensive checks should be advisory by default unless the current mode is `FULL` or `RELEASE`, or the Human Owner explicitly allows them.

## Selection Rules

Check selection should consider:

- declared verification mode;
- explicit verification budget;
- changed files and task scope;
- check value class;
- expected runtime;
- measured runtime history;
- blocking/advisory impact;
- whether slow checks are allowed.

When the budget is limited, prefer checks in this order:

1. blocking checks before advisory checks;
2. higher value before lower value;
3. lower expected duration before higher expected duration;
4. higher `priority_score = value_score / max(expected_duration_sec, 1)`.

Do not run a check when its expected duration does not fit the remaining budget.

## Runtime Measurement Rule

Every executed check must record wall-clock duration.

A check without measured runtime must not be reported as fully verified. It may be reported as skipped, not implemented, not applicable, dry-run only or manually reviewed, but not as passed.

## Reporting Rules

Codex final reports must state the selected verification mode and budget.

Use mode-specific language:

```text
FAST verification passed.
STANDARD verification passed.
```

Do not say:

```text
All tests passed.
```

unless all relevant tests for the selected mode actually ran.

Skipped checks must be listed with explicit reasons such as:

- outside selected mode;
- expected duration exceeds remaining budget;
- slow checks not allowed;
- command not implemented;
- not applicable to changed files;
- dry-run only;
- Human Owner did not request the stronger mode.

## Source Files

Related documents and artifacts:

- `/ai-system/verification-modes.md`
- `/ai-system/test-runtime-tracking.md`
- `/ai-system/spec/verification-checks.json`
- `/scripts/verification/run_checks.py`
