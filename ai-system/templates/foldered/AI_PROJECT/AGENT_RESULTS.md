# Agent Results — {{PROJECT_NAME}}

Status: Draft

## Purpose

This file records project-local Agent Result intake and integration review status references.

Agent Result Intake does not accept final task results.

Integration Review does not replace QA or Human Owner final acceptance.

This file does not authorize execution, automatic merge or automatic acceptance.

## Safety Boundaries

- Sequential execution remains the default unless a Human Owner-approved parallel group exists.
- Results must be checked against scope, `allowed_files`, `locked_files`, `forbidden_actions`, dependencies and verification mode.
- Integration Review is required before acceptance for approved parallel execution groups.
- QA or documented QA decision is required before final acceptance when applicable.
- Human Owner remains the final decision maker.

## Result Intake Log

| Result ID | Package ID | Status | Changed Files Checked | Verification Mode | Next Review Step |
|---|---|---|---|---|---|
| RES-001 | AWP-001 | not submitted | no | {{DEFAULT_VERIFICATION_MODE}} | Not ready. |

## Required Result Fields

Each result should include:

```text
result_id:
agent_work_package:
parent_task:
sop:
role:
status:
changed_files:
summary:
scope_statement:
checks_performed:
verification_mode:
errors:
questions:
blockers:
diff_or_key_changes:
dependency_notes:
review_notes:
qa_notes:
security_privacy_notes:
recommended_next_state:
```

## Integration Review References

| Parent Task | Result Set | Integration Review Status | QA Handoff Status | Human Owner Acceptance |
|---|---|---|---|---|
| TBD | TBD | not started | not ready | not reached |

