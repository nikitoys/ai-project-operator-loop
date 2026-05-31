# Glossary — Core Terms

Status: Draft

## AI Development System

A controlled system for developing an application through AI roles, documentation, workflow, review and human decisions.

It is not a single prompt. It is a documented operating model for software development with AI.

## Human Owner

The human who owns the project and makes final decisions.

Responsibilities:

- sets product direction;
- approves or rejects documents;
- approves or rejects implementation results;
- sends prepared prompts to Codex;
- decides whether the AI Development System should change.

## ChatGPT Orchestrator

ChatGPT acting as process organizer.

Responsibilities:

- prepares prompts for Codex;
- helps create and update documents;
- acts as Project Manager, Architect, Reviewer or QA when needed;
- analyzes Codex output;
- proposes next steps;
- helps evolve the AI Development System.

## Codex Executor

Codex acting as repository executor.

Responsibilities:

- changes files in the repository;
- implements tasks;
- updates documentation when explicitly instructed;
- returns changed files, diffs, test results and issues.

Codex should not invent product scope or change system rules without approval.

## AI Role

A specific AI personality responsible for one area of work.

Examples:

- Project Manager AI;
- Product Owner AI;
- Business Analyst AI;
- System Architect AI;
- UX/UI Designer AI;
- Backend Developer AI;
- Frontend Developer AI;
- QA Engineer AI;
- Code Reviewer AI;
- DevOps Engineer AI;
- Technical Writer AI;
- AI System Maintainer.

## Role Prompt

A prompt defining an AI role.

It describes role identity, responsibilities, forbidden actions, input documents, output documents and response format.

## System Prompt

The main controlling prompt of the AI Development System.

It defines global rules, roles, workflow, restrictions and documentation discipline.

## Source of Truth

The approved documentation that has priority over AI suggestions.

If AI output contradicts approved documentation, either the output is rejected or documentation is explicitly updated through the proper process.

## Workflow

The ordered development process.

Default workflow:

```text
Product Discovery → Requirements → Architecture → UX Design → Planning → Implementation → Review → QA → Deployment → Documentation Update
```

## Gate

A control point between stages.

Examples:

- implementation cannot start without PRD and Architecture Document;
- a task cannot be accepted without acceptance criteria;
- AI Development System cannot change without a change proposal.

## Repository

The project storage location.

It contains AI system documentation, project documentation, code, infrastructure and top-level README.

## Active Role

The AI role currently responsible for the work.

## Active Stage

The current workflow stage.

## Active Document

The main document currently being created, updated or used.

## Human Approval

Explicit human confirmation that a result, decision or change is accepted.
