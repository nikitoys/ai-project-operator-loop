# Glossary — Execution Terms

Status: Draft

## Definition of Ready

Conditions required before a task can be started:

- clear description;
- input documents;
- scope;
- out of scope;
- acceptance criteria;
- no blocking ambiguity.

## Definition of Done

Conditions required before a task is considered complete:

- acceptance criteria satisfied;
- review passed;
- QA passed or test cases documented;
- documentation updated if needed;
- Human Owner approved the result.

## Review

A structured check of the result.

Can include code review, architecture review, QA review and documentation review.

## Code Review

A check of code quality, architecture, security, maintainability, performance and compliance with the task.

## QA

Quality Assurance.

Checks whether implementation satisfies requirements and user scenarios.

## Critical Issue

A blocking issue that prevents acceptance.

Examples:

- security vulnerability;
- data loss risk;
- broken architecture;
- failed acceptance criteria.

## Major Issue

A serious issue that should be fixed before acceptance.

## Minor Issue

A non-blocking issue that can be fixed later or in the same iteration.

## Suggestion

Optional improvement.

## Decision

A human-approved status for a document, task, review or system change.

## APPROVED

The result is accepted.

## REWORK

The result needs changes.

## REJECTED

The result is not accepted.

## DEFERRED

The decision is postponed.

## EXPERIMENT

The change is accepted temporarily for testing.

## Prompt Package

A complete prompt prepared for Codex.

Usually includes:

- role;
- context;
- input documents;
- task;
- scope;
- out of scope;
- expected files;
- acceptance criteria;
- result format.

## Executor Output

The result returned by Codex.

Should include:

- changed files;
- summary;
- diff;
- test output;
- unresolved issues;
- questions.

## Environment

A runtime context such as local, dev, staging or production.

## Deployment

Process of running the application in an environment.

## Rollback

Reverting a code, documentation or system change.
