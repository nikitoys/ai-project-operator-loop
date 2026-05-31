# Glossary — Execution Terms

Status: Draft

## Task Lifecycle

The lifecycle for managed tasks, from creation and approval through execution, review, acceptance, rejection, deferral or archival.

Defined in `/ai-system/task-lifecycle.md`.

## Codex Execution Lifecycle

The lifecycle for controlled Codex repository work, including prompt preparation, approval, execution, result intake, review, rework, acceptance, rollback and archival.

Defined in `/ai-system/codex-lifecycle.md`.

## Review Lifecycle

The lifecycle for managed reviews, including review planning, reviewer assignment, findings, rework, re-review, approval, rejection, closure and archival.

Defined in `/ai-system/review-lifecycle.md`.

## QA Lifecycle

The lifecycle for managed QA work, including QA planning, checks, defect reporting, rework, regression, approval, rejection and archival.

Defined in `/ai-system/qa-lifecycle.md`.

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

## Re-review

A repeated review after rework has been submitted.

Re-review checks whether previous findings were resolved and whether the rework created new issues.

## Review Closure

The point where a review is formally finished because findings are approved, rejected, deferred, converted to follow-up work or closed by the Human Owner.

## Rework

Changes requested after review, QA, result intake or Human Owner decision.

Rework should address specific findings and then return for review or re-review when required.

## Result Intake

The step where ChatGPT Orchestrator reads and assesses Codex Executor output before review, acceptance, rework or rejection.

Result intake checks changed files, summary, tests, errors, unresolved issues and scope compliance.

## Acceptance Gate

A control point that must pass before work is accepted.

An acceptance gate may require acceptance criteria, review, QA, documentation consistency and Human Owner approval.

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
