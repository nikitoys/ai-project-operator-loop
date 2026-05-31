# Codex Execution Lifecycle

Status: Draft
Version: v0.1.0

## Purpose

This document defines how Codex executions are prepared, approved, run, reported, reviewed, reworked, accepted, rejected, rolled back and archived inside the AI Development System.

It applies the shared governance model from `/ai-system/lifecycle-governance.md` to repository execution through Codex.

## Governed Entity

A Codex execution is an approved attempt by Codex Executor to change, inspect, verify or report on repository state within explicit task or prompt boundaries.

Codex executions include:

- documentation changes;
- implementation changes;
- test or verification runs;
- repository inspections;
- rework tasks;
- rollback tasks;
- AI Development System updates.

Codex is an executor. Codex does not own product decisions, system decisions, role changes, approval decisions or scope expansion.

## Source of Truth

Default source-of-truth documents for Codex execution are:

- `/ai-system/human-interaction.md` for the Human Owner, ChatGPT and Codex loop;
- `/ai-system/prompt-lifecycle.md` for prompt drafting, review, approval and result review;
- `/ai-system/task-format.md` for task structure, Definition of Ready and Definition of Done;
- `/ai-system/review-process.md` for result review and severity rules;
- `/ai-system/rules.md` for Codex rules and implementation constraints;
- `/ai-system/change-process.md` for AI Development System evolution;
- approved task or prompt packages for execution-specific scope.

If an execution prompt conflicts with source documents, Codex should stop or report the conflict instead of guessing.

## Codex Execution Lifecycle States

Codex executions should use these states where applicable:

- `Proposed` - execution is suggested but not yet shaped into a prompt package.
- `Prompt Drafted` - prompt package exists but is not yet reviewed or approved.
- `Prompt Reviewed` - prompt package was checked for scope, safety and completeness.
- `Approved for Execution` - Human Owner approved sending the prompt to Codex.
- `Sent to Codex` - approved prompt was handed to Codex Executor.
- `In Progress` - Codex is executing the task.
- `Completed` - Codex finished execution and has output to report.
- `Failed` - execution could not complete successfully.
- `Result Submitted` - Codex returned changed files, summary, checks, errors, questions and diff or key changes.
- `In Review` - ChatGPT Orchestrator, reviewer role or QA is checking the result.
- `Rework Required` - review found approved issues that need targeted correction.
- `Accepted` - Human Owner accepted the result.
- `Rejected` - Human Owner rejected the result.
- `Rolled Back` - applied changes were reverted through an approved rollback action.
- `Archived` - execution record is retained for history, not active handling.

State names may be shortened in task tools or external systems, but they should map back to these states.

## Codex Execution Operations

## Prepare Prompt

Goal: create a bounded prompt package for Codex.

A prompt package should include:

- mode marker;
- active role;
- active stage;
- active document;
- expected result;
- repository path;
- source documents;
- task;
- scope;
- out of scope;
- allowed files;
- forbidden actions;
- acceptance criteria;
- expected output;
- review instructions.

Prompt packages should follow `/ai-system/prompt-lifecycle.md` and `/ai-system/task-format.md`.

## Review Prompt

Goal: check the prompt before execution.

Prompt review should verify:

- clear source documents;
- narrow scope;
- explicit allowed files;
- explicit forbidden actions;
- testable acceptance criteria;
- stable expected output;
- no hidden product or system decisions;
- Human Owner approval requirement when repository state can change.

## Approve Prompt

Goal: authorize Codex execution.

Human Owner approval is required before Codex changes repository files, applies system changes, runs risky commands or performs rollback.

AI roles may recommend approval, but they do not approve execution.

## Execute

Goal: perform the approved repository task.

Codex must:

- stay inside scope;
- use only allowed files unless the Human Owner approves a scope change;
- avoid forbidden actions;
- preserve unrelated user changes;
- report blockers instead of guessing when scope, state or approval is unclear.

## Report Result

Goal: return execution output for intake and review.

Codex must report:

- changed files;
- summary;
- checks or tests;
- errors;
- questions;
- diff or key changes.

If no files changed, Codex should say so explicitly.

## Intake Result

Goal: receive Codex output and determine the next state.

Result intake should check:

- whether changed files are within allowed files;
- whether forbidden actions occurred;
- whether checks or tests ran;
- whether errors or questions block review;
- whether output is complete enough for review;
- whether repository state conflicts with the task.

Incomplete result reports should be returned for clarification or rework before acceptance.

## Review Result

Goal: evaluate whether Codex output satisfies the task.

Review should follow `/ai-system/review-process.md` and check:

- task compliance;
- scope control;
- architecture or process compliance;
- security and safety risks;
- readability and maintainability when code is involved;
- acceptance criteria;
- negative scenarios and regression risks;
- documentation consistency;
- changelog or index updates when needed.

## Request Rework

Goal: create a targeted follow-up prompt for approved review findings.

A rework prompt must be narrower than the original prompt.

It should include:

- review findings being addressed;
- severity;
- allowed files;
- forbidden actions;
- acceptance criteria for the rework;
- expected output.

Rework must not add unrelated scope.

## Accept Result

Goal: close execution as accepted.

Only the Human Owner accepts final Codex results.

Acceptance may happen when acceptance criteria are satisfied, review passed and required documentation is updated, or when the Human Owner explicitly accepts documented risk.

## Reject Result

Goal: close execution as not accepted.

Rejected results should record:

- why the result was rejected;
- whether changes must be reverted;
- whether a new task or prompt is needed;
- whether an improvement-log entry or AICP is needed.

## Roll Back

Goal: revert applied changes after an accepted or partially applied execution causes problems.

Rollback requires Human Owner approval when it affects repository files, source-of-truth documentation, product behavior, system behavior or history.

Rollback should be handled as its own bounded task or prompt package.

Rollback output should report:

- files reverted;
- reason for rollback;
- original execution or commit being reverted;
- checks performed;
- remaining risks or follow-up work.

## Archive

Goal: retain execution history after completion, rejection, rollback or deferral.

Archived execution records may be used for audit, lessons learned, prompt improvement or future rework.

## Prompt Package Requirements

Every Codex execution prompt should define:

- role;
- context;
- source documents;
- task ID or task title;
- scope;
- out of scope;
- allowed files or expected files;
- forbidden actions;
- acceptance criteria;
- checks or tests expected;
- result format;
- review instructions.

For repository-changing tasks, allowed files and forbidden actions must be explicit.

## Result Intake Requirements

A Codex result is ready for review when it includes:

- changed files or explicit statement that no files changed;
- summary of work performed;
- checks or tests performed, or reason they were not run;
- errors encountered;
- questions or blockers;
- diff or key changes.

If the result is incomplete, ChatGPT Orchestrator should request clarification or rework before review or acceptance.

## Required Codex Report Format

Codex should report:

```text
Changed files:
Summary:
Checks / tests:
Errors:
Questions:
Diff or key changes:
```

This extends the recommended result format from `/ai-system/human-interaction.md` without changing that document.

## Failure Handling

## Sandbox Failure

If a command fails because of sandboxing or permissions, Codex should report the failure and request approval only when the command is necessary and within scope.

Codex must not work around sandbox restrictions by changing task scope.

## Dependency Failure

If dependencies are missing or cannot be installed, Codex should report:

- dependency name;
- command attempted;
- error summary;
- whether escalation or Human Owner action is needed;
- possible lower-risk alternative if one exists.

## Test Failure

If tests fail, Codex should report failing command, relevant failure summary and whether the failure appears caused by current changes, existing repository state or environment.

Test failure usually blocks acceptance unless the Human Owner explicitly accepts the risk.

## Scope Ambiguity

If scope, allowed files, acceptance criteria or source documents are unclear, Codex should stop and ask a question instead of guessing.

## Partial Implementation

If Codex completes only part of the task, it should report what is done, what remains, why it stopped and whether rework or a new task is needed.

Partial implementation must not be accepted as done unless the Human Owner explicitly changes acceptance criteria.

## Conflicting Repository State

If the repository has unrelated changes, stale references, merge conflicts or files that differ from prompt assumptions, Codex should preserve unrelated work and report the conflict.

Codex must not revert unrelated changes unless explicitly instructed by the Human Owner.

## Rework Prompt Flow

Rework flow:

```text
Review finding
→ Human Owner decision
→ Narrow rework prompt
→ Codex execution
→ Result submitted
→ Re-review
→ Human Owner acceptance or further decision
```

Rework prompts must address approved findings only.

If review reveals a broader process problem, record an improvement idea or prepare an AICP instead of expanding the rework prompt silently.

## Rollback Handling

Rollback is appropriate when:

- accepted changes caused a regression;
- system behavior changed incorrectly;
- documentation became misleading;
- partial implementation cannot be safely completed;
- Human Owner rejects applied changes and wants them reverted.

Rollback requires Human Owner approval when active repository state or source-of-truth documentation changes.

Rollback should not be mixed with unrelated fixes unless explicitly approved.

## Ownership Model

Default ownership:

- Human Owner approves execution, accepts results, rejects results and approves rollback.
- ChatGPT Orchestrator prepares prompts, intakes results and routes review.
- Codex Executor executes approved tasks and reports results.
- Relevant domain role owns task content and domain correctness.
- Code Reviewer AI reviews code quality, architecture compliance, safety and maintainability.
- QA Engineer AI checks acceptance criteria, negative scenarios and regression risks.
- AI System Maintainer owns Codex executions that change the AI Development System.

Codex may report recommendations, but it does not approve scope, product decisions or system decisions.

## Relationship to Task Format

Codex execution should be tied to a task or prompt package that satisfies the relevant parts of `/ai-system/task-format.md`.

Definition of Ready applies before execution. Definition of Done applies before acceptance.

## Relationship to Prompt Lifecycle

Codex execution begins after a prompt package is drafted, reviewed and approved under `/ai-system/prompt-lifecycle.md`.

Prompt improvement after failed or unclear execution should feed back into prompt lifecycle rather than being handled as an untracked chat message.

## Relationship to Review Process

Codex results must be reviewed before a task is considered done.

Review severity from `/ai-system/review-process.md` controls acceptance:

- Critical issues block acceptance.
- Major issues require fix or explicit Human Owner decision.
- Minor issues and suggestions may be accepted or deferred by the Human Owner.

## Relationship to Lifecycle Governance

This document specializes `/ai-system/lifecycle-governance.md` for Codex executions.

If this document and lifecycle governance conflict, report the conflict and require Human Owner approval before changing behavior.

## Relationship to Document Lifecycle

Codex executions that create, update, deprecate, archive, remove or roll back source-of-truth documents must respect `/ai-system/document-lifecycle.md`.

## Relationship to Process Lifecycle

Codex Execution Lifecycle is a managed process and must respect `/ai-system/process-lifecycle.md`.

Changes to execution states, operations, ownership, prompt requirements, result intake or rollback rules are process changes and may require Human Owner approval and AICP.

## Boundary Rules

Codex execution lifecycle must not be used to bypass Human Owner control.

Codex execution lifecycle must not allow Codex to make product or system decisions.

Codex execution lifecycle must not weaken task scope, allowed files, forbidden actions, review or acceptance rules.

Codex execution lifecycle must not combine unrelated implementation, documentation, system evolution or rollback work unless explicitly approved.
