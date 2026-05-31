# Process Lifecycle

Status: Draft
Version: v0.1.0

## Purpose

This document defines how managed processes are read, created, updated, reviewed, approved, rejected, split, merged, deprecated, archived, removed, rolled back and audited inside the AI Development System.

It applies the shared governance model from `/ai-system/lifecycle-governance.md` to process documentation and process evolution.

## Governed Entity

A managed process is any repeatable workflow, procedure, lifecycle, review path, prompt flow, approval flow or execution flow that affects how the AI Development System operates.

Managed processes include:

- development workflow;
- review process;
- change process;
- prompt lifecycle;
- document lifecycle;
- role lifecycle;
- lifecycle governance;
- Human Owner interaction flow;
- future task, Codex, QA, decision, improvement, knowledge and experiment lifecycles.

One-time task instructions, temporary notes and informal recommendations are not managed processes unless they are accepted as source-of-truth process documentation.

## Source of Truth

Default source-of-truth locations for managed processes are:

- `/ai-system/workflow.md` for the standard development workflow;
- `/ai-system/change-process.md` for AI Development System evolution flow;
- `/ai-system/review-process.md` for review and QA review rules;
- `/ai-system/prompt-lifecycle.md` for prompt creation, approval, execution and review flow;
- `/ai-system/*-lifecycle.md` for specific managed entity lifecycles;
- `/ai-system/human-interaction.md` for Human Owner, ChatGPT and Codex interaction flow.

If process documents conflict, report the conflict before applying the process. Higher-level governance documents should guide resolution, but Human Owner approval is required when behavior changes.

## Process Lifecycle States

Managed processes should use these states where applicable:

- `Proposed` - suggested but not yet drafted or approved.
- `Draft` - written for review, not yet accepted as active process truth.
- `In Review` - being checked for consistency, scope and governance impact.
- `Active` - accepted and currently used.
- `Experimental` - approved temporarily with success criteria and review date.
- `Deprecated` - retained but no longer recommended for new work.
- `Archived` - retained for history, not used for active work.
- `Rejected` - reviewed and not accepted.
- `Removed` - deleted from active documentation after approval and reference cleanup.
- `Rolled Back` - reverted to an earlier approved state after an applied change caused problems.

A process document should expose its status when it is part of `/ai-system` source-of-truth documentation.

## Process Operations

## Read

Goal: understand the current process before using or changing it.

Rules:

- Read the source process document and relevant governance documents.
- Check whether the process is active, draft, experimental or deprecated.
- Report conflicts with lifecycle governance, document lifecycle, rules or Human Owner instructions.

## Create

Goal: add a new managed process when existing processes cannot safely cover recurring work.

Create a process when:

- the work repeats often;
- the path needs clear states, gates or ownership;
- unclear process behavior causes scope creep, quality loss or review friction;
- the Human Owner approves the new process or an approved task requires it.

A new process should define purpose, governed activity, source of truth, states, operations, owner, approval rules, AICP relationship, version impact and audit rules.

## Update

Goal: adjust an existing managed process while preserving continuity.

Updates must stay within the approved scope.

If an update changes behavior, gates, approval rules, responsibilities, lifecycle states, prompt requirements, review criteria or version impact, it requires Human Owner approval and may require AICP.

## Review

Goal: verify that a process is clear, consistent and safe to use.

Process review should check:

- consistency with `/ai-system/lifecycle-governance.md`;
- consistency with `/ai-system/document-lifecycle.md`;
- compatibility with existing roles and responsibilities;
- whether Human Owner control is preserved;
- whether the process adds useful control without unnecessary overhead;
- whether related indexes, status summaries or changelog entries need updates.

## Approve

Goal: accept a process as active source of truth.

Only the Human Owner approves system-level process changes.

AI roles may recommend a decision using `APPROVED`, `REWORK`, `REJECTED`, `DEFERRED` or `EXPERIMENT`, but they do not make the final decision.

## Reject

Goal: mark a proposed or draft process as not accepted.

Rejected process drafts should be removed or retained only when useful for history. The rejection reason should be clear.

## Split

Goal: divide one broad process into narrower processes when one document or workflow becomes too complex.

Use split when:

- one process covers unrelated responsibilities;
- different roles own different parts;
- review or execution quality suffers because the process is too broad;
- narrower lifecycles would reduce ambiguity.

Splitting a process requires reference cleanup and Human Owner approval when active behavior changes.

## Merge

Goal: combine overlapping processes when separation creates unnecessary overhead.

Use merge when:

- processes duplicate states, gates or approval rules;
- users cannot tell which process applies;
- separate process documents slow work without improving control;
- one unified process would be clearer.

Merging active processes requires Human Owner approval and reference cleanup.

## Deprecate

Goal: mark an active process as no longer recommended while preserving history.

Deprecation requires Human Owner approval when the process is active.

A deprecation note should include:

- reason;
- replacement process;
- date or version;
- removal condition.

## Archive

Goal: retain an inactive process for historical reference.

Archived processes must not be used for new work unless restored or explicitly referenced as history.

Archive actions should update indexes and references that could route users to inactive guidance.

## Remove

Goal: delete a managed process after it is no longer needed.

Removal requires Human Owner approval when the process was active or referenced.

Before removal:

- references must be found and updated;
- replacement process must be identified if needed;
- changelog or audit history must preserve the reason.

## Roll Back

Goal: restore a previous approved process state after an applied change causes problems.

Rollback requires Human Owner approval for system-level processes.

Rollback should record:

- what changed back;
- why rollback was needed;
- which version or commit was restored;
- whether follow-up rework is needed.

## Audit

Goal: check whether a process still works and still matches the rest of the AI Development System.

Audit should check:

- whether the process is used;
- whether it conflicts with newer governance or lifecycle documents;
- whether it creates unnecessary overhead;
- whether it misses states, owners, review rules or closure criteria;
- whether repeated improvement-log entries suggest process failure.

Audit may result in no change, clarification, AICP, deprecation, split, merge, rollback or removal.

## Ownership Model

Default ownership:

- Human Owner approves system-level process changes.
- ChatGPT Orchestrator routes process requests and prepares prompts, reviews or AICP drafts.
- AI System Maintainer owns AI Development System process evolution.
- Technical Writer AI owns clarity, structure, consistency and index updates.
- Domain roles may contribute to process content for their area.
- Codex Executor applies approved process documentation edits only within explicit scope.

Each process document may define more precise ownership.

## Approval Rules

Human Owner approval is required for process changes that:

- create or remove managed processes;
- change lifecycle states or allowed operations;
- change workflow gates or approval requirements;
- change role responsibilities or process ownership;
- change prompt, review, QA or Codex execution behavior;
- split or merge active processes;
- deprecate or archive active processes;
- roll back an applied process change;
- permanently adopt an experimental process.

Small wording, formatting, link or index updates may be handled as patch-level documentation updates when they do not change behavior.

## AICP Relationship

An AICP is required when a process change affects:

- AI Development System behavior;
- workflow or lifecycle states;
- role responsibilities;
- approval rules;
- prompt requirements;
- review, QA or Codex execution rules;
- system version;
- permanent adoption of an experiment;
- rollback of an applied process change.

An AICP is not required for narrow wording corrections, index updates or clarifications that do not change behavior.

## Version Impact Rules

Use `MAJOR.MINOR.PATCH`.

- Patch: wording, formatting, link correction or clarification without process behavior change.
- Minor: new process document, new lifecycle process, new process state, new process operation or meaningful process addition.
- Major: significant change to the operating model, approval model, role hierarchy, workflow sequence or system governance.

When uncertain, choose the higher impact and ask the Human Owner to confirm.

## Audit and History Rules

Process changes should leave enough history to understand:

- what changed;
- why it changed;
- who approved it;
- which process documents were affected;
- whether the change was proposed, applied, rejected, experimental, deprecated, archived, removed or rolled back.

Use:

- `system-changelog.md` for applied AI Development System process changes;
- `improvement-log.md` for observed process problems and improvement ideas;
- AICP documents for proposed process behavior changes;
- git history for exact diffs and commits.

## Relationship to Lifecycle Governance

This document specializes `/ai-system/lifecycle-governance.md` for managed processes.

It should not redefine common governance unless process-specific detail is required.

If this document and lifecycle governance conflict, report the conflict and require Human Owner approval before changing behavior.

## Relationship to Document Lifecycle

Most managed processes are stored as managed documents.

Therefore, process changes must also respect `/ai-system/document-lifecycle.md` for documentation status, source-of-truth rules, index updates, deprecation, archival, removal and rollback.

A process may be behaviorally unchanged but still require document lifecycle handling when its source document is created, updated, archived or removed.

## Boundary Rules

Process lifecycle must not be used to bypass Human Owner control.

Process lifecycle must not redesign existing workflow, review process, change process or prompt lifecycle unless that redesign is explicitly approved.

Process lifecycle must not combine unrelated system evolution, product, implementation or infrastructure changes.

Process lifecycle should add only the amount of process needed to improve control, quality or speed.
