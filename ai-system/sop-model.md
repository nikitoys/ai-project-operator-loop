# SOP Model

Status: Draft
Version: v0.1.0

## Purpose

This document defines the SOP Model for AI_Development_System.

The SOP Model describes how a repeatable Standard Operating Procedure is represented, selected and used inside the existing governance-first workflow.

It does not implement runtime behavior.

It does not authorize automatic execution, automatic acceptance, parallel execution or agent work decomposition by itself.

## Governed Entity

The governed entity is a managed SOP.

A managed SOP is a documented, repeatable operating procedure that guides how Human Owner intent moves through roles, artifacts, gates, review and QA for a specific class of work.

Managed SOPs can describe product work, rework, documentation work, QA work, Codex execution preparation or AI Development System evolution.

Managed SOPs are planning and governance artifacts. They are not executable programs.

## Source-of-Truth Documents

The SOP Model depends on the following source-of-truth documents:

- `workflow.md` for the standard development workflow.
- `roles.md` and `system-structure.md` for role boundaries.
- `task-format.md` and `task-lifecycle.md` for task readiness, execution and closure.
- `prompt-lifecycle.md` for prompt drafting, review and approval.
- `codex-lifecycle.md` for scoped Codex execution and result intake.
- `review-process.md` and `review-lifecycle.md` for review requirements.
- `qa-lifecycle.md` for QA planning, checks, defects and approval recommendations.
- `lifecycle-governance.md` for shared managed-entity governance.
- `security-policy.md` and `privacy-data-handling-policy.md` for safety, sandbox and external LLM boundaries.
- `evolution/sop-multi-agent-implementation-plan.md` for the controlled SOP and optional multi-agent initiative.
- `evolution/evolution-backlog.md` for bounded future evolution tasks.
- `system-changelog.md` for applied system change history.
- `../spec/README.md` for the current Markdown-to-spec relationship.

If an SOP conflicts with these documents, the source document wins until an approved AI System Change Proposal or bounded evolution task changes the source of truth.

## SOP Definition

A SOP is a structured procedure that answers:

- which class of work is being handled;
- which roles participate;
- which artifacts are required before work starts;
- which stages and gates must be followed;
- where Human Owner approval is required;
- what review and QA must check;
- what outputs and learning records should be produced.

An SOP should reduce ambiguity in repeated work. It must not expand task scope, override approval gates or replace source-of-truth lifecycle documents.

## Required SOP Fields

Every managed SOP should define these fields:

- `SOP ID` - stable identifier, for example `SOP-FEATURE-001`.
- `Name` - short human-readable name.
- `Purpose` - why the SOP exists and what class of work it governs.
- `Trigger` - condition that starts SOP selection.
- `Applicable scope` - work types, repository areas or situations where the SOP applies.
- `Participating roles` - roles involved and their responsibilities in this SOP.
- `Stages/actions` - ordered procedure steps.
- `Input artifacts` - documents, tasks, prompts, decisions or files required before execution.
- `Output artifacts` - documents, tasks, prompts, review reports, QA reports, changelog entries or decisions produced by the SOP.
- `Handoff rules` - how work moves between Human Owner, ChatGPT Orchestrator, AI roles and Codex Executor.
- `Gates` - required checks before moving to the next stage.
- `Review and QA requirements` - review types, QA checks and evidence expected before acceptance.
- `Human Owner approval points` - decisions that require explicit Human Owner approval.
- `Relationship to task/prompt/Codex lifecycle` - how the SOP uses existing task, prompt and Codex execution lifecycles.
- `Metrics or learning outputs` - lessons, defects, rework causes, cycle notes or improvement candidates produced by the SOP.

## Relationship to Existing Workflow

SOPs sit above the standard workflow as selection and routing guidance.

The standard workflow remains:

```text
Product Discovery
-> Requirements
-> Architecture
-> UX Design
-> Planning
-> Implementation
-> Review
-> QA
-> Deployment
-> Documentation Update
```

An SOP may skip stages only when the source documents and task scope already make the skipped stage unnecessary. The reason should be explicit in the task or prompt package.

An SOP must not start implementation without Definition of Ready, scope, acceptance criteria and approval requirements being clear.

## Relationship to Roles and Role Boundaries

SOPs route work to existing roles. They do not create new role authority.

Role boundaries remain governed by `roles.md` and `system-structure.md`.

Examples:

- Product Owner AI owns product value and MVP scope, not implementation.
- System Architect AI owns architecture decisions, not code execution.
- Project Manager AI owns task decomposition and ordering, not product scope expansion.
- Code Reviewer AI and QA Engineer AI recommend acceptance or rework, but do not replace Human Owner acceptance.
- AI System Maintainer owns AI Development System evolution through controlled change.
- Codex Executor changes repository files only within approved prompt or task boundaries.

If an SOP requires a role to act outside its documented responsibility, the SOP must stop and request a documented decision or future role change.

## Relationship to Task Lifecycle

SOPs use the task lifecycle to convert intent into bounded work.

The SOP should ensure that managed tasks have:

- clear description;
- owner role;
- source documents;
- scope and out of scope;
- expected files or allowed files;
- acceptance criteria;
- checks or test cases;
- result format;
- known risks and blockers.

SOPs must preserve one bounded task at a time unless a future approved parallel execution policy allows otherwise.

## Relationship to Prompt Lifecycle and Codex Lifecycle

SOPs can guide prompt preparation, but prompts remain governed by `prompt-lifecycle.md`.

Codex execution remains governed by `codex-lifecycle.md`.

An SOP may recommend a Codex Prompt Package only after:

- task scope is bounded;
- source documents are listed;
- allowed files and forbidden actions are explicit;
- acceptance criteria are testable;
- Human Owner approval requirement is assessed;
- verification mode is defined.

Codex must report changed files, summary, checks, errors, questions and diff or key changes. SOPs must not bypass result intake or review.

## Relationship to Review and QA

Each SOP must define review and QA expectations before work starts.

Review should follow `review-process.md` and `review-lifecycle.md`.

QA should follow `qa-lifecycle.md`.

At minimum, an SOP should state:

- whether code review, documentation review, security/privacy review or QA review is required;
- which acceptance criteria are checked;
- whether regression checks are needed;
- what evidence is expected;
- who recommends approval or rework;
- where Human Owner acceptance is required.

Review approval and QA approval are recommendations or gates. They do not replace final Human Owner acceptance.

## Relationship to Future Agent Work Packages

Future Agent Work Packages may use SOPs as planning input.

This document does not define the Agent Work Package standard. That is reserved for `EVOL-010`.

Until that standard exists and is approved, SOPs may describe future decomposition conceptually, but must not require or generate agent work packages as an active execution mechanism.

## Relationship to Future Optional Parallel Execution

Sequential execution remains the default.

Parallel execution is future opt-in behavior only.

This document does not define the full Parallel Execution Policy. That is reserved for a later bounded evolution task.

Any future parallel execution must remain planned, Human Owner-approved, conflict-checked, reviewed and QA-gated. SOPs must not authorize parallel execution on their own.

## Default Rule

Sequential execution remains the default operating mode for AI_Development_System.

The safe one-task Codex workflow remains valid.

## Boundary Rule

An SOP does not authorize:

- automatic execution;
- automatic Codex invocation;
- automatic branch or merge operations;
- automatic result acceptance;
- bypassing review or QA;
- bypassing Human Owner approval;
- expanding allowed files;
- changing role boundaries;
- changing lifecycle states.

Any behavior-changing system update must go through controlled evolution and, when required, an AI System Change Proposal.

## Initial SOPs

The following initial SOPs are documented as governance models only.

They are intentionally lightweight. They provide selection guidance and lifecycle relationships without introducing agent work package standards, scripts, specs or runtime behavior.

## SOP-FEATURE-001 - Feature Delivery SOP

Purpose:

Guide a new product feature from Human Owner intent to bounded implementation, review, QA and acceptance.

Trigger:

The Human Owner requests a new product capability, user-facing behavior or MVP feature.

Applicable scope:

Product feature work in a concrete project repository.

Participating roles:

- Human Owner defines direction and accepts final result.
- Product Owner AI clarifies product value and MVP boundary.
- Business Analyst AI defines requirements and acceptance criteria.
- System Architect AI defines technical approach when architecture is affected.
- UX/UI Designer AI defines UX states when user-facing UI is affected.
- Project Manager AI decomposes work into bounded tasks.
- Codex Executor implements approved repository changes.
- Code Reviewer AI reviews implementation quality and compliance.
- QA Engineer AI verifies acceptance criteria and regressions.
- Technical Writer AI updates documentation when needed.

Stages/actions:

```text
Human Owner intent
-> product and requirements clarification
-> architecture and UX clarification when needed
-> bounded task creation
-> prompt package preparation
-> Human Owner approval
-> sequential Codex execution
-> result intake
-> review
-> QA
-> Human Owner acceptance
-> documentation and changelog update when required
-> lessons or improvement notes when useful
```

Input artifacts:

- Human Owner request or `AI_PROJECT/OWNER_PLAN.md`.
- Product vision, PRD, architecture and UX docs where applicable.
- Bounded task or prompt package.
- Acceptance criteria and verification mode.

Output artifacts:

- Updated task record.
- Codex result report.
- Review report.
- QA report or documented checks.
- Documentation or changelog updates when required.
- Improvement notes when repeated friction appears.

Human Owner approval points:

- feature scope approval;
- implementation prompt approval when repository files will change;
- acceptance of final result;
- explicit risk acceptance when review or QA leaves residual risk.

Review and QA requirements:

Feature work usually requires code review and QA. Documentation review is required when docs or onboarding guidance change. Security/privacy review is required when sensitive data, external services, auth, secrets or sandbox boundaries are affected.

## SOP-BUGFIX-001 - Bugfix / Rework SOP

Purpose:

Guide defect fixes, review findings or QA findings into targeted rework without expanding scope.

Trigger:

A bug report, review finding, QA defect, failed check or Human Owner rework request is accepted for correction.

Applicable scope:

Bugfixes, task rework, documentation corrections and regression fixes.

Participating roles:

- Human Owner decides whether the issue must be fixed, deferred, rejected or accepted as risk.
- ChatGPT Orchestrator routes the finding and prepares a narrow rework prompt when needed.
- Relevant domain role clarifies intended behavior.
- Codex Executor applies the approved fix inside explicit scope.
- Code Reviewer AI and QA Engineer AI re-check the affected area.
- Technical Writer AI updates documentation if the fix changes documented behavior.

Stages/actions:

```text
finding or defect
-> severity and scope classification
-> Human Owner or reviewer decision
-> targeted rework task or prompt
-> Human Owner approval when repository changes are needed
-> sequential Codex execution
-> re-review
-> regression check when needed
-> Human Owner acceptance or further rework
```

Input artifacts:

- Review report, QA defect, bug report or Human Owner rework request.
- Original task or prompt package.
- Affected acceptance criteria.
- Allowed files and forbidden actions for the rework.

Output artifacts:

- Narrow rework task or prompt.
- Codex result report.
- Re-review result.
- Regression check notes when applicable.
- Updated task status.

Human Owner approval points:

- acceptance of risk when a finding is not fixed;
- approval before repository-changing rework;
- final acceptance after re-review or QA.

Review and QA requirements:

Rework must focus on approved findings only. Re-review should check the finding and affected files. Regression checks are required when the fix touches shared behavior, lifecycle rules, user-facing behavior or previously failed areas.

## SOP-SYSTEM-001 - AI System Evolution SOP

Purpose:

Guide AI_Development_System changes through controlled evolution while preserving Human Owner authority and changelog discipline.

Trigger:

The Human Owner requests AI Development System evolution, an improvement is accepted, a roadmap item becomes active or an evolution backlog item is selected.

Applicable scope:

Changes to AI system documentation, governance, roles, workflow, lifecycle documents, prompts, specs, templates, helper scripts or system version.

Participating roles:

- Human Owner approves behavior-changing system changes and accepts final result.
- AI System Maintainer owns system evolution handling.
- System Architect AI helps with model and governance consistency.
- Technical Writer AI maintains documentation clarity and indexes.
- Code Reviewer AI and QA Engineer AI review and verify as needed.
- Codex Executor applies approved local repository changes inside allowed files.

Stages/actions:

```text
Human Owner request or roadmap/backlog item
-> classify as EVOLUTION or SYSTEM
-> read source documents
-> confirm scope, out of scope and allowed files
-> assess AICP and approval requirement
-> execute one bounded evolution task
-> update indexes, backlog and changelog when required
-> run required checks or report skipped checks
-> review for scope control and governance consistency
-> Human Owner acceptance
-> recommend next bounded phase
```

Input artifacts:

- Evolution roadmap, backlog item, owner plan, AICP or Human Owner request.
- Relevant source-of-truth system documents.
- Allowed files, forbidden actions, acceptance criteria and verification mode.

Output artifacts:

- Updated system document or bounded documentation set.
- Updated evolution backlog status.
- Changelog entry and README version mirrors when version changes.
- Check results or documented verification limitations.
- Next recommended bounded task.

Human Owner approval points:

- approval before behavior-changing system changes;
- approval before role, lifecycle, prompt, review, QA, security or source-of-truth changes;
- final acceptance of the completed evolution task.

Review and QA requirements:

AI system evolution must be reviewed for scope control, source-of-truth consistency, Human Owner approval preservation, changelog/index consistency and absence of unrelated product code changes.

## SOP Change and Evolution Rules

SOP changes are AI Development System changes.

SOP changes must follow controlled evolution when they affect:

- workflow behavior;
- role boundaries;
- lifecycle rules;
- prompt requirements;
- review or QA requirements;
- Human Owner approval points;
- Codex execution boundaries;
- system version;
- future agent or parallel execution behavior.

Small wording corrections may be handled as documentation changes, but changelog impact should be assessed when source-of-truth documents are affected.

Adding, changing, deprecating or removing a managed SOP should record:

- reason for change;
- affected SOP ID;
- affected source documents;
- expected benefit;
- risk of not changing;
- approval requirement;
- version impact;
- changelog entry when applied.

## Metrics and Learning Outputs

SOP use should produce lightweight learning signals when useful:

- repeated blockers;
- unclear source documents;
- missing acceptance criteria;
- review finding patterns;
- QA defect patterns;
- rework causes;
- verification gaps;
- prompt quality issues;
- candidate improvement-log or evolution-backlog items.

Metrics are learning inputs, not automatic triggers for execution.

## Open Questions / Future Work

- Define the Agent Work Package standard in `EVOL-010`.
- Define the planning-only multi-agent workflow in `EVOL-011`.
- Define the full parallel execution policy in `EVOL-012`.
- Define result intake and integration review for agent outputs in `EVOL-013`.
- Add machine-checkable SOP and Agent Work Package specs in `EVOL-014`.
- Decide whether SOP IDs should later be mirrored into `spec/sops.json`.
- Decide whether concrete projects should maintain local SOP selections in `AI_PROJECT/` after templates exist.

