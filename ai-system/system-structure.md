# AI Development System Structure

Status: Draft  
Version: v0.1.0

## Purpose

This document explains the structure of the AI Development System from the Human Owner's point of view.

It shows:

- who participates in the system;
- how roles are grouped;
- who makes decisions;
- who prepares work;
- who executes work;
- who reviews results;
- how the system evolves.

## High-Level Structure

```text
Human Owner
│
├── ChatGPT Orchestrator
│   │
│   ├── Product Layer
│   │   ├── Product Owner AI
│   │   └── Business Analyst AI
│   │
│   ├── Design Layer
│   │   ├── System Architect AI
│   │   └── UX/UI Designer AI
│   │
│   ├── Management Layer
│   │   └── Project Manager AI
│   │
│   ├── Implementation Layer
│   │   ├── Backend Developer AI
│   │   ├── Frontend Developer AI
│   │   └── DevOps Engineer AI
│   │
│   ├── Quality Layer
│   │   ├── Code Reviewer AI
│   │   └── QA Engineer AI
│   │
│   ├── Documentation Layer
│   │   └── Technical Writer AI
│   │
│   └── System Evolution Layer
│       └── AI System Maintainer
│
└── Codex Executor
```

## Human Owner

The Human Owner is the top-level decision maker.

The Human Owner:

- defines direction;
- approves or rejects decisions;
- approves MVP scope;
- sends prepared prompts to Codex;
- reviews Codex output with ChatGPT;
- approves changes to the AI Development System.

Main rule:

```text
AI recommends. Human decides.
```

## ChatGPT Orchestrator

ChatGPT Orchestrator coordinates the system.

It decides which role should be active, which workflow stage is current, which document is used and what result should be produced.

ChatGPT Orchestrator:

- prepares documents;
- prepares Codex prompts;
- reviews Codex output;
- detects contradictions;
- recommends next steps;
- invokes AI roles when needed.

## Codex Executor

Codex Executor is the repository executor.

Codex:

- creates files;
- changes files;
- implements tasks;
- updates documentation when explicitly instructed;
- returns changed files, summaries, diffs, tests and questions.

Codex does not own product decisions and must not change scope or system rules without approval.

## Product Layer

The Product Layer answers:

```text
What are we building and why?
```

### Product Owner AI

Solves:

- product idea;
- target audience;
- user problem;
- product value;
- MVP scope;
- out-of-MVP scope;
- success criteria.

Outputs:

- Product Vision;
- MVP definition;
- product priorities.

### Business Analyst AI

Solves:

- user roles;
- user scenarios;
- user stories;
- acceptance criteria;
- functional requirements;
- non-functional requirements;
- constraints and open questions.

Outputs:

- PRD;
- User Stories;
- Acceptance Criteria.

## Design Layer

The Design Layer answers:

```text
How should the product work technically and for the user?
```

### System Architect AI

Solves:

- technical stack;
- architecture approach;
- modules;
- project structure;
- database design;
- API contracts;
- authorization;
- security;
- technical risks.

Outputs:

- Architecture Document;
- API Documentation;
- Database Schema;
- technical decisions.

### UX/UI Designer AI

Solves:

- screens;
- user flows;
- UI elements;
- forms;
- empty/loading/success/error states;
- validation messages.

Outputs:

- UX Specification;
- screen map;
- UI states;
- user-facing messages.

## Management Layer

The Management Layer answers:

```text
In what order should we work?
```

### Project Manager AI

Solves:

- current stage detection;
- backlog creation;
- task decomposition;
- dependency tracking;
- next minimal step;
- risk detection;
- MVP focus;
- scope creep prevention.

Outputs:

- Backlog;
- task plan;
- next step;
- risk list;
- progress status.

## Implementation Layer

The Implementation Layer answers:

```text
How do we turn tasks into files, code and infrastructure?
```

### Backend Developer AI

Solves:

- API implementation;
- business logic;
- database logic;
- authorization;
- validation;
- backend errors;
- backend tests.

### Frontend Developer AI

Solves:

- screens;
- components;
- forms;
- API integration;
- navigation;
- frontend validation;
- UI states.

### DevOps Engineer AI

Solves:

- local/dev/staging/production environments;
- Docker;
- docker-compose;
- environment variables;
- CI/CD;
- logs;
- backup;
- deployment instructions.

## Quality Layer

The Quality Layer answers:

```text
Can this result be accepted?
```

### Code Reviewer AI

Solves:

- task compliance;
- architecture compliance;
- code quality;
- security issues;
- performance risks;
- error handling;
- scope creep detection.

Outputs:

- Review Report;
- Critical Issues;
- Major Issues;
- Minor Issues;
- Suggestions;
- Final Verdict.

### QA Engineer AI

Solves:

- acceptance criteria verification;
- positive scenarios;
- negative scenarios;
- edge cases;
- regression checks;
- user-facing behavior.

Outputs:

- QA Report;
- Test Cases;
- Regression Checklist.

## Documentation Layer

The Documentation Layer answers:

```text
Is everything important recorded?
```

### Technical Writer AI

Solves:

- README updates;
- setup instructions;
- project structure documentation;
- changelog updates;
- onboarding documentation;
- consistency between code and documentation.

## System Evolution Layer

The System Evolution Layer answers:

```text
Does the AI Development System itself need to change?
```

### AI System Maintainer

Solves:

- process problems;
- role conflicts;
- workflow weaknesses;
- unclear prompts;
- missing rules;
- excessive process complexity;
- system versioning;
- change proposals.

Outputs:

- Improvement Log entry;
- AI System Change Proposal;
- Experiment proposal;
- System Changelog update;
- system version update.

## Main Operating Loop

```text
Human Owner sets goal
→ ChatGPT Orchestrator selects role and stage
→ AI role prepares document, task or review
→ Human Owner approves direction
→ ChatGPT prepares Codex prompt if repository changes are needed
→ Codex Executor changes files
→ ChatGPT reviews result
→ Human Owner approves, rejects or requests rework
→ Documentation is updated
```

## Main Rule

```text
Human Owner controls.
ChatGPT organizes.
AI roles specialize.
Codex executes.
Documentation records.
AI System Maintainer evolves the system.
```
