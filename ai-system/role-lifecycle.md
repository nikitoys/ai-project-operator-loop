# Role Lifecycle

Status: Draft  
Version: v0.1.0

## Purpose

This document defines how AI roles are read, added, changed, deprecated and removed.

Roles are not fixed forever. The AI Development System may evolve by creating new roles, merging existing roles, editing role responsibilities or removing roles that are no longer useful.

## Core Principle

Roles are part of the AI Development System.

Therefore, role changes must follow the system change process and must not be done randomly.

## Role Registry

The current role registry is stored in:

```text
/ai-system/roles.md
```

The human-readable hierarchy is stored in:

```text
/ai-system/system-structure.md
```

If a role is added, edited or removed, both files may need to be updated.

## Minimal Role Set

The minimal useful role set is:

```text
Human Owner
ChatGPT Orchestrator
Project Manager AI
Product Owner AI
Business Analyst AI
System Architect AI
Developer AI
QA / Reviewer AI
Technical Writer AI
AI System Maintainer
Codex Executor
```

For very small projects, `Developer AI` may combine Backend, Frontend and DevOps responsibilities.

For larger projects, `Developer AI` may be split into:

- Backend Developer AI;
- Frontend Developer AI;
- Mobile Developer AI;
- DevOps Engineer AI;
- Database Engineer AI.

## Role Operations

## 1. Read Role

Goal: understand what a role does.

Input:

- role name.

Read from:

- `/ai-system/roles.md`;
- `/ai-system/system-structure.md`;
- `/ai-system/glossary-core.md` if term clarification is needed.

Output:

- role purpose;
- responsibilities;
- forbidden actions;
- input documents;
- output documents;
- related workflow stages.

Command example:

```text
Read role: System Architect AI
```

## 2. Add Role

Goal: create a new role when existing roles cannot cover a recurring responsibility.

A new role may be added when:

- the responsibility repeats often;
- the responsibility does not clearly belong to an existing role;
- mixing it with an existing role reduces quality;
- the benefit is greater than the added complexity.

A new role should not be added when:

- the need happened once;
- a task clarification is enough;
- an existing role can handle it with a small prompt update;
- the new role creates unclear ownership.

Required process:

```text
Problem
→ Improvement Log entry
→ AICP
→ Human approval
→ Update roles.md
→ Update system-structure.md
→ Update workflow.md if needed
→ Update system-changelog.md
```

## 3. Edit Role

Goal: change responsibilities, boundaries or prompt behavior of an existing role.

A role may be edited when:

- it frequently acts outside its responsibility;
- its responsibilities overlap with another role;
- its output format is unclear;
- it misses important checks;
- project needs changed.

Required process:

```text
Observed issue
→ Root cause analysis
→ AICP
→ Human approval
→ Update roles.md
→ Update related documents
→ Update system-changelog.md
```

## 4. Split Role

Goal: divide one broad role into multiple specialized roles.

Example:

```text
Developer AI
→ Backend Developer AI
→ Frontend Developer AI
→ DevOps Engineer AI
```

Use when one role becomes too broad and quality decreases.

## 5. Merge Roles

Goal: combine roles when the system is too heavy.

Example:

```text
QA Engineer AI + Code Reviewer AI
→ QA / Reviewer AI
```

Use when separate roles create overhead without improving quality.

## 6. Deprecate Role

Goal: mark a role as no longer recommended but keep it documented temporarily.

Use when:

- a role may still be referenced by old tasks;
- removal would confuse history;
- the role is being replaced.

Deprecation entry should include:

- reason;
- replacement role;
- date;
- removal condition.

## 7. Delete Role

Goal: remove a role from the active system.

Allowed only when:

- role is unused;
- responsibilities moved to another role;
- documentation references are updated;
- Human Owner approved removal.

Required updates:

- `/ai-system/roles.md`;
- `/ai-system/system-structure.md`;
- `/ai-system/workflow.md` if the role owned a stage;
- `/ai-system/system-prompt.md` if the role is listed there;
- `/ai-system/glossary-core.md` if the role has a glossary entry;
- `/ai-system/system-changelog.md`.

## Role Change Proposal Template

```md
# AICP-000: Add/Edit/Delete Role

## Status
Proposed / Accepted / Rejected / Experimental / Applied

## Change Type
Add Role / Edit Role / Split Role / Merge Roles / Deprecate Role / Delete Role

## Role Name
Name of the role.

## Problem
Why is this change needed?

## Evidence
Where did the problem appear?

## Proposed Change
What changes in the role registry?

## Responsibilities
What the role will do.

## Forbidden Actions
What the role must not do.

## Input Documents
Which documents the role uses.

## Output Documents
Which documents or artifacts the role creates.

## Affected Files
- /ai-system/roles.md
- /ai-system/system-structure.md
- /ai-system/workflow.md
- /ai-system/system-prompt.md
- /ai-system/glossary-core.md
- /ai-system/system-changelog.md

## Risks
What can become worse?

## Decision
Human Owner decision.

## Version Impact
Patch / Minor / Major
```

## Version Impact Rules

- Patch: small wording change in a role description.
- Minor: add, delete, split or merge a role.
- Major: change the role hierarchy or operating model.

## Main Rule

Do not create roles for beauty.

Create, edit or delete roles only when it improves control, quality or speed of the AI Development System.
