# Test Runtime Tracking

Status: Draft
Version: v0.1.0

## Purpose

This document defines lightweight runtime tracking for verification checks.

The goal is to keep verification useful and bounded. The system should learn which checks are fast, slow, flaky or no longer appropriate for normal task verification.

## Captured Runtime Data

Every executed or skipped check should produce one JSONL event with these fields:

- `run_id`
- `task_id`, if available
- `check_id`
- `verification_mode`
- `started_at`
- `finished_at`
- `duration_sec`
- `result`
- `exit_code`
- `timeout_sec`
- `blocking`
- `reason_for_run`
- `reason_for_skip`
- `changed_files_count`, if available

Allowed `result` values are defined in `/ai-system/verification-cost-model.md`:

- `passed`
- `failed`
- `skipped`
- `timeout`
- `not_applicable`

## Local Runtime History

Local runtime history should remain local by default.

Recommended local paths:

```text
.verification-history.jsonl
outputs/verification-history.jsonl
AI_PROJECT/verification-history.local.jsonl
```

The default lightweight runner stores local events in:

```text
outputs/verification-history.jsonl
```

## What Must Be Committed

Commit:

- verification policy documents;
- machine-readable check registry;
- verification runner source code;
- reusable example history files;
- documentation explaining the fields and rules.

Do not commit:

- real local runtime history from a developer machine;
- environment-specific command output;
- logs that include private paths, secrets, credentials or private project data;
- generated local history files.

## Aggregate Metrics

Runtime history may be summarized into these aggregate metrics:

- `last_duration_sec`
- `avg_duration_sec`
- `median_duration_sec`
- `p95_duration_sec`
- `failure_rate`
- `timeout_rate`
- `last_10_results`

Aggregates may be calculated locally from JSONL history. They should be treated as advisory unless a future approved task defines a committed metrics format.

## Runtime Degradation Rules

If a check is classified as `fast` but `p95_duration_sec` becomes greater than 60 seconds, the system must warn that the check should be optimized or reclassified.

If a check is classified as `standard` but `p95_duration_sec` becomes greater than 5 minutes, the system must warn that the check should not be part of normal task verification.

Timeouts and repeated failures should be reported separately from duration drift. A slow passing check and a flaky fast check are different problems.

## Skip Tracking

Skipped checks are useful evidence.

Record `reason_for_skip` when a check is skipped because:

- the selected mode does not include it;
- it does not fit the remaining budget;
- slow checks are not allowed;
- the command is not implemented;
- the check is not applicable to changed files;
- the execution is a dry run.

Skipped checks must not be counted as passed.

## Privacy and Safety

Runtime history should not include secrets, credentials or sensitive data.

When command output is needed for debugging, summarize the failure separately instead of storing full logs in runtime history.

## Source Files

Related documents and artifacts:

- `/ai-system/verification-cost-model.md`
- `/ai-system/verification-modes.md`
- `/ai-system/spec/verification-checks.json`
- `/scripts/verification/run_checks.py`
