# Agent Locks — {{PROJECT_NAME}}

Status: Draft

## Purpose

This file records project-local file-scope and locked-file planning for Agent Work Packages.

Locks are planning records only. They do not grant write permission.

This file does not authorize execution, parallel execution, automatic execution, automatic merge or automatic acceptance.

Human Owner remains the final decision maker.

## Safety Boundaries

- Sequential execution remains the default.
- `allowed_files` define maximum file surface for a package if later approved.
- `locked_files` define planned file ownership for conflict reasoning only.
- Overlapping `locked_files` block parallel execution unless re-scoped and explicitly approved.
- Candidate parallel groups are informational until approved under the Parallel Execution Policy.

## File-Scope Registry

| Package ID | allowed_files | locked_files | Conflict Status | Notes |
|---|---|---|---|---|
| AWP-001 | TBD | TBD | not checked | Define before execution approval. |

## Conflict Checklist

Before execution approval, check:

- no package modifies files outside `allowed_files`;
- no parallel candidate has overlapping `locked_files`;
- shared files are isolated or sequenced;
- broad globs are justified;
- security/privacy-sensitive files are explicitly approved and isolated;
- rollback or rework path is clear.

## Parallel Group Notes

```text
Parallel group approved: no
Dependency check passed: no
Locked-file check passed: no
Integration review planned: no
QA decision recorded: no
```

