# Review Lifecycle

Status: Draft
Version: v0.1.0

## Purpose

This document defines how managed reviews are opened, assigned, executed, reported, reworked, re-reviewed, approved, rejected, closed and archived inside the AI Development System.

It applies the shared governance model from `/ai-system/lifecycle-governance.md` to review work and closes the review governance gap left by `/ai-system/review-process.md`.

## Governed Entity

A managed review is any structured review activity that evaluates whether a task result, Codex result, document, process, system change or other source-of-truth change satisfies approved scope, acceptance criteria and system rules.

Managed reviews include:

- code reviews;
- QA reviews;
- documentation reviews;
- prompt and Codex result reviews;
- lifecycle and governance reviews;
- re-reviews after rework;
- final review recommendations before Human Owner acceptance.

Informal comments are not managed reviews unless they affect task acceptance, rework, rejection, closure or source-of-truth decisions.

## Source of Truth

Default source-of-truth documents for review are:

- `/ai-system/review-process.md` for review types, severity levels and review report format;
- `/ai-system/task-format.md` for task scope, acceptance criteria and expected output;
- `/ai-system/task-lifecycle.md` for task review states, rework and closure boundaries;
- `/ai-system/codex-lifecycle.md` for Codex result intake, review and rework flow;
- `/ai-system/qa-lifecycle.md` for QA review, defect handling and regression checks;
- `/ai-system/lifecycle-governance.md` for shared lifecycle governance rules;
- `/ai-system/roles.md` for reviewer role responsibilities;
- approved task documents, prompt packages, AICPs, review reports and changelog entries for task-specific scope.

If review scope conflicts with source documents, acceptance criteria or allowed files, the conflict must be reported before approval or rejection.

## Review Lifecycle States

Managed reviews should use these states where applicable:

- `Not Required` - review is explicitly not needed for the task or change.
- `Planned` - review scope, type and reviewer are identified.
- `Ready for Review` - output is available and review can start.
- `In Review` - reviewer is actively checking the result.
- `Changes Requested` - review found issues requiring rework.
- `Re-review Required` - rework was submitted and must be checked again.
- `Approved` - review passed within approved scope.
- `Approved with Notes` - review passed, but non-blocking notes or risks remain.
- `Rejected` - output is not acceptable in current form.
- `Blocked` - review cannot continue because required input, authority, environment or decision is missing.
- `Closed` - review is complete and no active review action remains.
- `Archived` - review record is retained for history and audit.

Specific tools or task records may use shorter status labels, but they should map back to these states.

## Allowed Operations

## Assess Review Need

Goal: decide whether a managed review is required and what type is appropriate.

Review is usually required when a task changes code, behavior, user-facing flows, data handling, architecture, process rules, lifecycle rules, prompt behavior or source-of-truth documentation.

A review may be marked `Not Required` only when the reason is documented and the Human Owner or approved task scope accepts that risk.

## Plan Review

Goal: define review type, scope, reviewer and expected output.

Review planning should identify:

- reviewed entity;
- source-of-truth documents;
- review type;
- reviewer role;
- acceptance criteria or review checklist;
- severity expectations;
- known risks;
- required evidence or files;
- blocking assumptions.

## Open Review

Goal: move a review to `Ready for Review`.

Before opening review:

- the reviewed output must exist;
- scope and allowed files must be known;
- acceptance criteria or expected output must be available;
- reviewer role must be clear;
- unresolved blockers must be documented.

## Assign Reviewer

Goal: make reviewer ownership explicit.

The reviewer should match the review type and risk area. If multiple review types are required, the ChatGPT Orchestrator coordinates sequencing and prevents duplicate or conflicting findings.

## Execute Review

Goal: evaluate the output against approved scope and system rules.

Review execution should check:

- compliance with the task or change request;
- compliance with source-of-truth documents;
- missing or unrelated changes;
- quality, maintainability and clarity;
- security, performance or reliability risks where applicable;
- documentation consistency;
- QA and regression implications;
- boundary rule violations.

## Report Findings

Goal: produce a review report in the format defined by `/ai-system/review-process.md`.

Review findings must include severity, evidence or rationale, affected scope and recommended next state.

Findings should distinguish between blocking issues, non-blocking issues and optional suggestions.

## Request Rework

Goal: route review findings into targeted correction.

Rework must address approved review findings only and must not silently expand product, implementation or system scope.

Codex may perform review rework only through an explicit rework task or prompt with allowed files, forbidden actions and acceptance criteria.

## Submit Rework for Re-review

Goal: move the review to `Re-review Required` after rework is available.

The rework submission should identify:

- findings addressed;
- files or documents changed;
- findings intentionally not addressed;
- remaining risks;
- whether QA or regression is required.

## Re-review

Goal: verify that requested rework resolved the review findings without introducing unacceptable new issues.

Re-review should focus on:

- previously reported critical and major findings;
- changed files or documents;
- regression risk caused by the fix;
- new issues introduced by rework;
- unresolved notes requiring Human Owner decision.

Re-review may produce `Approved`, `Approved with Notes`, `Changes Requested`, `Rejected` or `Blocked`.

## Approve

Goal: mark review output as acceptable within approved scope.

Review approval means the reviewer found no blocking issues or remaining risks were explicitly accepted by the Human Owner.

Review approval does not replace final Human Owner acceptance of task results.

## Reject

Goal: mark reviewed output as unacceptable in current form.

Rejection should record the reason, blocking findings and whether rework, rollback, deferral or a new task is needed.

## Block

Goal: pause review when it cannot continue safely.

Review should be blocked when:

- acceptance criteria are missing or conflicting;
- source-of-truth documents conflict;
- reviewed output is incomplete or unavailable;
- required files or evidence are unavailable;
- Human Owner decision is required;
- review would exceed approved scope.

## Unblock

Goal: resume review after a blocker is resolved.

Unblock should record what changed, which blocker was resolved and whether review scope changed.

## Close Review

Goal: end active review handling.

A review may be closed when:

- it is approved and required task, QA or Human Owner decisions are recorded;
- it is rejected and the next action is recorded;
- it is superseded by a new review or task;
- it is explicitly deferred by the Human Owner;
- it is marked not required with documented rationale.

## Archive

Goal: retain review history after closure.

Archived review records may be used for audit, regression planning, lessons learned and future lifecycle improvements.

## Ownership Model

Default ownership:

- Human Owner approves final task result, accepts risk and decides disputed review outcomes.
- ChatGPT Orchestrator routes review flow, coordinates reviewers, summarizes findings and prepares rework prompts.
- Code Reviewer AI owns code review findings and code-level risk analysis.
- QA Engineer AI owns QA review findings, defect handling and regression recommendations.
- Technical Writer AI owns documentation review findings and source-of-truth consistency.
- AI System Maintainer owns lifecycle, governance and system consistency reviews.
- Relevant domain roles own domain-specific correctness checks.
- Codex Executor fixes review findings only through an approved task or prompt with explicit scope.

Reviewer roles may recommend approval, rejection or rework, but Human Owner remains final acceptance authority where task closure, risk acceptance or source-of-truth decisions are involved.

## Review Types Relationship

`/ai-system/review-process.md` defines the base review types:

- Code Review checks implementation quality, compliance, security, performance and unnecessary scope expansion.
- QA Review checks acceptance criteria, scenarios, edge cases, user-facing errors and regression risks.
- Documentation Review checks README, API, changelog and consistency between implementation and documentation.

Review Lifecycle governs the state model and transitions for those review types.

Multiple review types may be required for one task. Their findings should be consolidated before Human Owner acceptance to avoid contradictory closure decisions.

## Severity Relationship

Severity levels from `/ai-system/review-process.md` determine transition pressure:

- `Critical` findings block approval and normally move review to `Changes Requested`, `Rejected` or `Blocked`.
- `Major` findings require rework or explicit Human Owner risk acceptance before approval.
- `Minor` findings may allow `Approved with Notes` when they do not violate acceptance criteria or source-of-truth rules.
- `Suggestion` findings are optional and must not block closure unless the Human Owner changes scope.

Severity must not be downgraded to avoid rework or accelerate closure.

## Re-review Process

Re-review is required when critical or major findings were fixed, when requested documentation changes were made, when QA defects were corrected or when Human Owner asks for confirmation after rework.

Re-review flow:

```text
Review finding
→ Changes Requested
→ targeted rework task or prompt
→ rework result
→ Re-review Required
→ focused re-review
→ approval, notes, further rework, rejection or blocker
```

Re-review should be narrower than the original review unless rework changed additional scope or introduced new risk.

## Closure Rules

A review can close as `Approved` only when:

- required review types were completed or explicitly scoped out;
- critical findings are resolved;
- major findings are resolved or accepted by the Human Owner;
- re-review is complete when required;
- QA or regression implications are recorded;
- remaining risks are documented;
- final Human Owner decision is recorded when required.

A review can close as `Rejected` only when rejection reason, blocking findings and next action are recorded.

A review must not close with unresolved critical findings unless the Human Owner explicitly decides to reject, defer or roll back the reviewed output.

## Relationship to Task Lifecycle

Review is part of task completion.

`/ai-system/task-lifecycle.md` requires review before a task can be considered done. Review outcomes may move a task to:

- `In Review` when review starts;
- `Rework Required` when critical or major findings require correction;
- `Blocked` when review cannot continue safely;
- `Rejected` when output is unacceptable;
- `Done` only after review, QA if required and Human Owner approval are complete.

Task closure must reference review status or review report when review is required.

## Relationship to Codex Execution Lifecycle

Codex result review must follow `/ai-system/codex-lifecycle.md`.

Codex execution may produce a result report, but that report does not approve the result by itself.

Review findings from Codex output may trigger a rework prompt. The rework prompt must preserve task scope, allowed files, forbidden actions and acceptance criteria.

Codex must not self-approve review findings it created unless the Human Owner explicitly allows that review model for low-risk work.

## Relationship to QA Lifecycle

QA findings and review findings are related but not identical.

Review Lifecycle governs review states, reviewer ownership and closure. QA Lifecycle governs QA planning, execution, defect reporting and regression checks.

When QA defects require implementation or documentation changes, review should verify the rework and QA should run regression where required.

Critical QA failures block review closure unless the Human Owner rejects, defers, rolls back or explicitly accepts the risk.

## Relationship to Lifecycle Governance

This document specializes `/ai-system/lifecycle-governance.md` for managed reviews.

If this document and lifecycle governance conflict, report the conflict and require Human Owner approval before changing behavior.

Future review lifecycle changes must follow lifecycle governance, document lifecycle and process lifecycle rules.

## Human Owner Approval Rules

Human Owner approval is required for:

- final task acceptance;
- accepting unresolved major or critical review risk;
- marking review as not required when risk is meaningful;
- rejecting task output based on review findings when the decision affects source of truth;
- expanding review scope into product, implementation or system changes;
- approving Codex rework tasks that change repository files;
- closing disputed reviews;
- accepting rollback, deferral or production use after review failure.

Reviewer roles recommend; Human Owner decides.

## AICP Relationship

An AICP is required when review findings or review process changes affect:

- AI Development System behavior;
- role definitions or responsibilities;
- lifecycle governance;
- workflow or approval process;
- prompt requirements;
- review, QA or Codex execution rules;
- system version;
- permanent adoption of an experiment;
- rollback of an applied system change.

An AICP is not required for ordinary task-level review findings unless they change the AI Development System itself.

## Version Impact Rules

Use `MAJOR.MINOR.PATCH` for AI Development System review changes.

- Patch: wording, formatting, link correction or review clarification without behavior change.
- Minor: new review lifecycle document, new review state, new review operation, new approval rule or meaningful review process addition.
- Major: significant change to approval model, reviewer ownership, workflow, role hierarchy or governance model.

When uncertain, choose the higher impact and ask the Human Owner to confirm.

## Audit and History Rules

Review history should preserve:

- reviewed entity;
- review type;
- reviewer role;
- source documents checked;
- findings by severity;
- review verdict;
- rework requested;
- re-review result when applicable;
- unresolved risks;
- Human Owner decisions;
- related task, Codex execution, QA flow or AICP;
- affected files or documents when applicable.

Review reports, changelog entries and git commits together form the audit trail for review-governed repository changes.

## Boundary Rules

Review lifecycle must not be used to bypass Human Owner approval.

Review lifecycle must not silently expand product scope, implementation scope or system behavior.

Review lifecycle must not allow Codex to fix review findings without explicit task scope or approval.

Review lifecycle must not merge unrelated review, QA, implementation or system evolution work unless explicitly approved.

Review lifecycle must not replace QA execution, Codex result intake, task closure or lifecycle governance; it coordinates with them through explicit states and records.
