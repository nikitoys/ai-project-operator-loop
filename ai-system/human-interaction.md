# Human Interaction Model

Status: Draft

## Purpose

This document defines how the Human Owner interacts with ChatGPT, Codex and the repository.

## Core Model

```text
Human Owner controls direction
ChatGPT Orchestrator prepares prompts, documents and reviews
Codex Executor changes repository files
Repository stores code and documentation
Human Owner approves or rejects results
```

## Human Owner Responsibilities

The Human Owner:

- defines goals;
- chooses priorities;
- approves MVP scope;
- approves documents;
- sends prepared prompts to Codex;
- returns Codex output to ChatGPT for review;
- accepts, rejects or requests rework;
- approves changes to the AI Development System.

## ChatGPT Responsibilities

ChatGPT:

- identifies active role and active stage;
- prepares documents;
- prepares Codex prompt packages;
- reviews Codex output;
- identifies risks and contradictions;
- recommends next steps.

## Codex Responsibilities

Codex:

- executes concrete repository tasks;
- changes only allowed files;
- follows scope and out of scope;
- reports changed files, diff, tests and issues.

## Standard Loop

```text
1. Human asks ChatGPT for the next step or prompt.
2. ChatGPT prepares a structured prompt package.
3. Human sends the prompt to Codex.
4. Codex changes repository files.
5. Human returns Codex output to ChatGPT.
6. ChatGPT reviews the result.
7. Human decides APPROVED, REWORK, REJECTED or DEFERRED.
8. Documentation is updated if needed.
```

## Recommended Codex Result Format

```text
Task:
Changed files:
Summary:
Tests:
Errors:
Questions:
Diff:
```

## Decision Statuses

- `APPROVED` — result accepted.
- `REWORK` — result needs changes.
- `REJECTED` — result rejected.
- `DEFERRED` — decision postponed.
- `EXPERIMENT` — accepted temporarily for testing.

## Main Rule

AI recommends. Human decides.
