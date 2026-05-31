# Knowledge Lifecycle

Status: Draft
Version: v0.1.0

## Purpose

This document defines how knowledge is observed, captured, classified, validated, promoted, maintained, deprecated, removed and archived inside the AI Development System.

It enables the system to learn from reviews, improvements, repeated issues and decisions without turning every observation into an immediate rule.

## Governed Entity

A managed knowledge item is any reusable learning, concept, pattern, decision insight, recurring issue, terminology clarification or lesson learned that may improve future work inside the AI Development System.

Managed knowledge items may become glossary entries, rules, prompts, templates, review checks, lifecycle improvements or archived lessons.

Informal thoughts are not managed knowledge items unless they are captured in an approved source-of-truth location or explicitly linked to a task, review, improvement, decision, AICP or changelog entry.

## What Counts as Knowledge

Knowledge may include:

- repeated review findings;
- recurring QA defects or regression risks;
- clarified terminology;
- stable lessons learned from completed tasks;
- decisions that should guide future work;
- common prompt patterns that improve execution quality;
- recurring failure modes in Codex execution;
- process improvements discovered during system evolution;
- documented assumptions that became stable enough to reuse;
- examples that help apply a lifecycle, rule, template or process.

Knowledge should be reusable, explainable and connected to evidence or source context.

## What Does Not Count as Knowledge

The following do not count as managed knowledge by default:

- one-off opinions without supporting evidence;
- unresolved assumptions;
- temporary task notes with no future reuse value;
- speculative ideas not yet validated or approved;
- implementation details that belong only in product documentation;
- secrets, credentials or sensitive operational data;
- personal preferences unless the Human Owner explicitly approves them as system rules;
- raw discussion transcripts without classification or summary.

Non-knowledge observations may still be stored in an improvement log or task notes if useful, but they must not be promoted automatically.

## Source of Truth

Default source-of-truth documents for knowledge are:

- `/ai-system/glossary.md` and related glossary files for approved terminology;
- `/ai-system/rules.md` for approved system rules;
- `/ai-system/system-prompt.md` and prompt documents for approved prompt behavior;
- `/ai-system/document-templates.md` for approved reusable templates;
- `/ai-system/improvement-log.md` for observations, recurring problems and candidate improvements;
- `/ai-system/system-changelog.md` for applied system changes and historical context;
- `/ai-system/decision-process.md` and decision records for approved Human Owner decisions;
- `/ai-system/review-lifecycle.md` and review reports for review-derived lessons;
- `/ai-system/change-lifecycle.md` and AICPs for approved system changes;
- `/ai-system/lifecycle-governance.md` for shared lifecycle governance rules.

If a knowledge item cannot be linked to a source, it must remain a candidate or be rejected.

## Knowledge Lifecycle States

Managed knowledge items should use these states where applicable:

- `Observed` - a possible knowledge item was noticed but not yet written in a managed form.
- `Captured` - the item was recorded with enough context to review later.
- `Candidate` - the item is classified as potentially reusable knowledge.
- `Validated` - the item was checked against evidence, source documents and Human Owner intent.
- `Promoted` - the item was converted into a glossary term, rule, prompt, template or other source-of-truth update.
- `Active` - the promoted knowledge is currently usable by the AI Development System.
- `Deprecated` - the item is no longer recommended but retained for context or transition.
- `Archived` - the item is retained for history and audit only.
- `Rejected` - the item was reviewed and not accepted as reusable knowledge.
- `Removed` - the item was intentionally deleted from active source-of-truth locations.

Specific tools or task records may use shorter labels, but they should map back to these states.

## Allowed Operations

## Observe Knowledge

Goal: notice a possible reusable lesson, pattern, problem or term.

Observation can happen during task execution, review, QA, Codex result intake, improvement triage, decision handling or system evolution.

Observed knowledge must not affect future behavior until captured and validated.

## Capture Knowledge

Goal: record the observation in a managed location.

Captured knowledge should include:

- short title;
- source context;
- date or related task/change;
- evidence or examples;
- why it may matter;
- suggested future use;
- owner or reviewer when known.

The default capture location is `/ai-system/improvement-log.md` unless the item clearly belongs directly in a glossary, decision record, review report or changelog entry.

## Classify Knowledge

Goal: decide what type of knowledge the item may become.

Common classifications:

- glossary term;
- system rule;
- prompt instruction;
- document template;
- review checklist item;
- QA or regression lesson;
- process improvement;
- decision guidance;
- archived lesson learned.

Classification does not approve the item; it only routes validation and promotion.

## Validate Knowledge

Goal: check whether the item is accurate, reusable and consistent with source-of-truth documents.

Validation should check:

- evidence quality;
- whether the issue repeated or has strong enough impact;
- consistency with glossary, rules, roles, workflow and lifecycle documents;
- conflict with Human Owner decisions;
- whether the item belongs in `/ai-system` or product `/docs`;
- whether promotion requires AICP or Human Owner approval;
- whether the item is too narrow, temporary or speculative.

## Promote to Glossary

Goal: convert validated terminology into glossary documentation.

A knowledge item may be promoted to glossary when it defines a term, removes ambiguity or improves shared understanding.

Glossary promotion should preserve the term, definition, scope and cross-links to relevant lifecycle documents.

## Promote to Rule

Goal: convert validated operational knowledge into an approved rule.

A knowledge item may be promoted to a rule only when it must constrain future behavior.

Rule promotion usually requires Human Owner approval and may require AICP when it changes AI Development System behavior.

## Promote to Template

Goal: convert validated reusable structure into a template.

A knowledge item may be promoted to a template when it improves repeatability without creating a mandatory rule.

Template promotion should define when to use the template and which fields are required or optional.

## Promote to Prompt

Goal: convert validated prompt behavior into prompt documentation or a prompt package update.

Prompt promotion must follow prompt lifecycle rules and must not silently change authority, scope, approval rules or role responsibilities.

## Link to Source

Goal: connect knowledge to evidence and affected documents.

Knowledge items should link to source documents, reviews, tasks, decisions, AICPs, changelog entries or commits where possible.

Knowledge without source links should not be promoted unless the Human Owner explicitly approves it.

## Deprecate Knowledge

Goal: mark knowledge as no longer recommended while retaining context.

Deprecation is appropriate when a rule, term, template or lesson is outdated, replaced or no longer safe to use.

Deprecated knowledge should point to the replacement when one exists.

## Remove Knowledge

Goal: delete knowledge from active source-of-truth locations when retention would be misleading, unsafe or unnecessary.

Removal requires stronger justification than deprecation and must preserve audit history when the item affected prior system behavior.

## Archive Knowledge

Goal: retain knowledge history after rejection, replacement, deprecation or closure.

Archived knowledge is not active guidance. It may be used for audit, lessons learned and future analysis.

## Audit Knowledge

Goal: periodically check whether active knowledge remains accurate and useful.

Audit should identify stale, duplicated, conflicting, unsupported or over-promoted knowledge.

## Ownership Model

Default ownership:

- Human Owner approves knowledge that changes system behavior, rules, prompts, authority or risk acceptance.
- ChatGPT Orchestrator captures, classifies and routes knowledge items.
- AI System Maintainer owns knowledge governance and consistency with lifecycle documents.
- Technical Writer AI owns glossary, template and documentation clarity.
- Code Reviewer AI owns code-review-derived knowledge.
- QA Engineer AI owns QA, defect and regression lessons.
- Relevant domain roles own domain-specific knowledge accuracy.
- Codex Executor may apply approved knowledge updates only through explicit task scope.

No AI role may convert an observation into a binding rule without required approval.

## Knowledge Capture Rules

Knowledge should be captured when:

- the same issue appears repeatedly;
- a review or QA finding reveals a reusable lesson;
- a Human Owner decision should guide future work;
- a term causes ambiguity;
- a prompt pattern improves or harms execution quality;
- a process gap appears during system evolution;
- a completed task reveals a stable lesson learned.

Capture should be concise and evidence-based. Raw conversation should be summarized before becoming managed knowledge.

## Validation Rules

Before promotion, knowledge must be validated for:

- correctness;
- source traceability;
- reuse value;
- consistency with existing documents;
- risk of overgeneralization;
- required Human Owner approval;
- required AICP or version impact;
- correct destination document.

Unvalidated knowledge may inform discussion, but must not be treated as an active rule or source of truth.

## Promotion Rules

Promotion converts validated knowledge into an active source-of-truth artifact.

Promotion must identify one destination:

- glossary term;
- rule;
- prompt instruction;
- template;
- review or QA checklist item;
- lifecycle/process update;
- changelog or decision reference;
- archived lesson learned.

A single knowledge item may be split into multiple promoted artifacts only when each destination has clear scope and approval.

## Relationship to Glossary

Glossary files store approved terminology, not every observation.

Knowledge should become a glossary entry when it defines a stable term, clarifies scope, prevents repeated misunderstanding or supports lifecycle consistency.

Glossary updates should include cross-links to lifecycle documents when terminology is lifecycle-specific.

## Relationship to Rules and Prompts

Rules constrain future behavior. Prompts guide role behavior and execution.

Knowledge may become a rule or prompt instruction only after validation and approval.

Prompt updates must not create hidden policy changes, new authority or expanded scope without Human Owner approval.

Rules and prompts should reference the knowledge source when the reason is not obvious.

## Relationship to Improvement Lifecycle

`/ai-system/improvement-log.md` is the default intake location for many knowledge candidates.

Improvement entries may produce knowledge when they reveal reusable lessons, repeated issues or stable process changes.

Knowledge Lifecycle does not replace Improvement Lifecycle. Improvement Lifecycle governs triage, conversion and closure of improvements once that lifecycle is implemented.

## Relationship to Change Lifecycle

Promoting knowledge into rules, prompts, lifecycle documents, process documents or templates may be a managed system change.

When knowledge promotion changes AI Development System behavior, it must follow `/ai-system/change-lifecycle.md` and may require an AICP.

Knowledge that only records a lesson learned without behavior change may not require a system change.

## Relationship to Review Lifecycle

Reviews are a major source of knowledge.

Review findings may become knowledge when they reveal recurring issues, unclear rules, missing templates, ambiguous terms or stable lessons learned.

Review approval does not automatically promote review findings into active knowledge. Promotion requires validation and the appropriate destination document update.

## Stale Knowledge Detection

Knowledge may be stale when:

- it conflicts with newer lifecycle documents;
- it references deprecated rules, prompts or roles;
- it no longer matches current workflow;
- repeated reviews show it is misleading;
- a Human Owner decision supersedes it;
- product or system architecture changes make it obsolete;
- it lacks source traceability and cannot be validated.

Stale knowledge should be deprecated, updated, archived or removed.

## Deprecation and Removal Rules

Deprecate knowledge when it is outdated but still useful for history or transition.

Remove knowledge when keeping it would be misleading, unsafe, duplicated or contrary to approved source-of-truth documents.

Removal should preserve audit context in changelog, decision records, AICP history or git history when the removed item previously affected behavior.

Human Owner approval is required when deprecation or removal changes active system behavior.

## Lesson Learned Storage Rules

Lessons learned should be stored at the lowest durable level that preserves future value:

- glossary for terminology lessons;
- rules for mandatory behavior lessons;
- prompts for role or execution guidance;
- templates for repeatable structure;
- improvement log for candidate or unresolved lessons;
- changelog for applied system evolution history;
- review reports for task-specific lessons;
- archived notes for historical context without active guidance.

Lessons learned should include source context and should avoid turning one-off events into broad rules.

## Human Owner Approval Rules

Human Owner approval is required for:

- promoting knowledge into binding rules;
- changing prompt behavior or role authority;
- changing lifecycle, workflow or approval rules;
- accepting knowledge with meaningful uncertainty or risk;
- deprecating or removing active knowledge that affects system behavior;
- resolving conflicts between knowledge sources;
- deciding whether repeated observations justify a system change.

AI roles may recommend promotion, deprecation or removal, but Human Owner decides when system behavior or risk changes.

## AICP Relationship

An AICP is required when knowledge promotion, deprecation or removal affects:

- AI Development System behavior;
- role definitions or responsibilities;
- lifecycle governance;
- workflow or approval process;
- prompt requirements;
- review, QA or Codex execution rules;
- system version;
- permanent adoption of an experiment;
- rollback of an applied system change.

An AICP is not required for ordinary glossary clarification, archived lessons or task-local notes unless they change the AI Development System itself.

## Version Impact Rules

Use `MAJOR.MINOR.PATCH` for AI Development System knowledge changes.

- Patch: wording, formatting, link correction, glossary clarification or archived lesson without behavior change.
- Minor: new knowledge lifecycle document, new knowledge state, new knowledge operation, new promotion path or meaningful knowledge governance addition.
- Major: significant change to approval model, source-of-truth hierarchy, role authority, workflow or lifecycle governance.

When uncertain, choose the higher impact and ask the Human Owner to confirm.

## Audit and History Rules

Knowledge history should preserve:

- knowledge item title or identifier;
- source context;
- classification;
- validation result;
- promotion destination;
- Human Owner decision when required;
- related review, QA flow, improvement, decision, AICP, changelog entry or commit;
- deprecation, removal or archival reason;
- replacement knowledge when applicable.

Audit should make it possible to understand why knowledge became active and why it later changed.

## Relationship to Lifecycle Governance

This document specializes `/ai-system/lifecycle-governance.md` for managed knowledge items.

If this document and lifecycle governance conflict, report the conflict and require Human Owner approval before changing behavior.

Future knowledge lifecycle changes must follow lifecycle governance, document lifecycle and process lifecycle rules.

## Boundary Rules

Knowledge lifecycle must not be used to bypass Human Owner approval.

Knowledge lifecycle must not silently turn observations into binding rules.

Knowledge lifecycle must not store secrets, credentials or sensitive operational data.

Knowledge lifecycle must not replace product documentation, task acceptance, review approval, QA execution or change governance.

Knowledge lifecycle must not promote speculative, one-off or unsupported observations into active source of truth.
