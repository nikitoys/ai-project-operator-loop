# Agent Tasks — {{PROJECT_NAME}}

Status: Draft

## Purpose

This file is the project-local Agent Work Package registry.

Agent Work Packages are bounded planning artifacts. They do not authorize execution, parallel execution, automatic execution, automatic merge or automatic acceptance.

Human Owner remains the final decision maker.

## Safety Boundaries

- Sequential execution remains the default.
- Agent Work Packages must stay inside their parent task scope.
- Candidate parallel groups are informational until explicitly approved by the Human Owner.
- A package can be executed only through an approved task or prompt package.
- This registry must not be used to bypass review, QA or Human Owner acceptance.

## Agent Work Package Registry

| ID | Status | SOP | Role | Parent Task | Verification Mode | Notes |
|---|---|---|---|---|---|---|
| AWP-001 | proposed | TBD | TBD | TBD | {{DEFAULT_VERIFICATION_MODE}} | Define after parent task approval. |

## Required Package Fields

Each Agent Work Package should define:

```text
id:
parent_task:
status:
sop:
role:
action:
context:
input_artifacts:
output_artifacts:
scope:
out_of_scope:
allowed_files:
locked_files:
forbidden_actions:
dependencies:
acceptance_criteria:
verification_mode:
expected_output:
review_instructions:
risks:
questions_or_blockers:
```

## Status Values

```text
proposed
draft
ready
approved
blocked
in_progress
result_submitted
in_review
rework_required
accepted
rejected
deferred
archived
```

## Notes

Use `AI_PROJECT/AGENT_LOCKS.md` for file-scope and locked-file planning.

Use `AI_PROJECT/AGENT_RESULTS.md` after a package result is submitted.

