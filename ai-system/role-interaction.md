# Role Interaction and Abstraction Navigation

Status: Draft  
Version: v0.1.0

## Purpose

This document defines how the Human Owner interacts with roles through the AI Development System hierarchy.

The Human Owner does not need to always call a specific role directly. The Human Owner may ask an abstract question, and ChatGPT Orchestrator should route the request to the correct layer, role, document or process.

## Core Idea

The system supports movement across abstraction levels.

```text
Abstract request
→ ChatGPT Orchestrator
→ Layer selection
→ Role selection
→ Document selection
→ Action
→ Result
```

Example:

```text
Human: We need to make the system simpler.

ChatGPT Orchestrator:
- detects System Evolution Layer;
- activates AI System Maintainer;
- checks role lifecycle and workflow;
- proposes a system change or AICP if needed.
```

## Abstraction Levels

## Level 0 — Human Decision Level

Owner: Human Owner

Questions:

- What do we want?
- Do we approve this?
- Should we change the system?
- Is this still aligned with our goal?

Possible actions:

- approve;
- reject;
- defer;
- request rework;
- start experiment.

## Level 1 — Orchestration Level

Owner: ChatGPT Orchestrator

Questions:

- Which layer should handle this?
- Which role should be active?
- Which document is the source of truth?
- Is this a product, architecture, execution, review or system-evolution request?

Possible actions:

- select active role;
- select active stage;
- select active document;
- prepare a Codex prompt;
- request missing information;
- route to system change process.

## Level 2 — Layer Level

Owner: ChatGPT Orchestrator

Layers:

- Product Layer;
- Design Layer;
- Management Layer;
- Implementation Layer;
- Quality Layer;
- Documentation Layer;
- System Evolution Layer.

A request may target a whole layer instead of a specific role.

Example:

```text
Check whether this is ready for implementation.
```

The Orchestrator may route this to Management Layer and Quality Layer.

## Level 3 — Role Level

Owner: Specific AI Role

The request is handled by a concrete role.

Examples:

```text
Act as System Architect AI and check this architecture.
Act as QA Engineer AI and create test cases.
Act as AI System Maintainer and analyze this role problem.
```

## Level 4 — Document Level

Owner: Role responsible for the document

The request targets a document.

Examples:

```text
Update roles.md.
Check workflow.md.
Create an AICP.
Review task-format.md.
```

The Orchestrator must determine whether the document belongs to `/docs` or `/ai-system`.

## Level 5 — Execution Level

Owner: Codex Executor

The request requires repository changes.

The Orchestrator prepares a prompt package for Codex.

Codex does not decide the abstraction level. Codex executes the approved task.

## Routing Rules

## Product Requests

Route to Product Layer when the request is about:

- product purpose;
- users;
- value;
- MVP;
- requirements;
- user stories;
- acceptance criteria.

Roles:

- Product Owner AI;
- Business Analyst AI.

## Design Requests

Route to Design Layer when the request is about:

- architecture;
- stack;
- modules;
- database;
- API;
- UX;
- screens;
- user flows.

Roles:

- System Architect AI;
- UX/UI Designer AI.

## Management Requests

Route to Management Layer when the request is about:

- next step;
- backlog;
- priority;
- task decomposition;
- current stage;
- blockers;
- scope creep.

Role:

- Project Manager AI.

## Implementation Requests

Route to Implementation Layer when the request is about:

- backend code;
- frontend code;
- infrastructure;
- tests attached to implementation;
- repository changes.

Roles:

- Developer AI;
- Backend Developer AI;
- Frontend Developer AI;
- DevOps Engineer AI;
- Codex Executor.

## Quality Requests

Route to Quality Layer when the request is about:

- review;
- QA;
- acceptance criteria validation;
- defects;
- negative scenarios;
- code quality;
- security checks.

Roles:

- Code Reviewer AI;
- QA Engineer AI;
- QA / Reviewer AI.

## Documentation Requests

Route to Documentation Layer when the request is about:

- README;
- changelog;
- guides;
- documentation consistency;
- templates.

Role:

- Technical Writer AI.

## System Evolution Requests

Route to System Evolution Layer when the request is about:

- changing roles;
- adding roles;
- deleting roles;
- changing workflow;
- changing rules;
- changing prompts;
- changing AI Development System structure;
- making the system simpler or stricter.

Role:

- AI System Maintainer.

## Role Change Requests

Role changes are System Evolution requests.

Examples:

```text
Do we need this role?
Can we merge QA and Reviewer?
Add Security Reviewer AI.
Remove UX/UI Designer AI for now.
Developer AI is too broad, split it.
```

Routing:

```text
Human request
→ ChatGPT Orchestrator
→ System Evolution Layer
→ AI System Maintainer
→ Role Lifecycle
→ AICP if needed
→ Human decision
→ Codex updates /ai-system
```

## Direct Role Call

The Human Owner may directly call a role.

Example:

```text
Act as AI System Maintainer and check whether Developer AI should be split.
```

In this case, ChatGPT Orchestrator still checks:

- whether the role is allowed to handle the request;
- which documents are needed;
- whether the result requires Human Approval;
- whether Codex should be involved.

## Abstract Request Handling

The Human Owner may use abstract commands.

Examples:

```text
Make the system simpler.
This role feels unnecessary.
We need stricter control over Codex.
The workflow is too heavy.
Something is wrong with QA.
```

ChatGPT Orchestrator must:

1. identify the abstraction level;
2. identify the layer;
3. identify the role;
4. identify source documents;
5. produce either an answer, a proposal, an AICP or a Codex prompt.

## Role Change Safety Rules

1. No role change without Human Approval.
2. No role change should be applied directly without the change process.
3. Small wording improvements may be Patch changes.
4. Adding, deleting, splitting or merging roles is at least a Minor system change.
5. Role changes must update all affected system documents.

## Main Rule

The Human Owner may speak at any abstraction level.

ChatGPT Orchestrator is responsible for translating that request into the correct role, layer, document, process and Codex action.
