# AI Development System

Status: Draft  
Version: v0.18.0

## Purpose

`/ai-system` describes how this repository is developed through an AI-assisted development process.

This folder does not describe the product itself. It describes the development mechanism: roles, rules, workflow, human interaction, task format, review process and controlled evolution of the system.

## Core Principle

Documentation is the source of truth.

AI roles do not work from inspiration. They work from approved documents, explicit tasks and defined acceptance criteria.

## Version Source

The current AI_Development_System version is the top version entry in `system-changelog.md`.

Primary README files mirror that changelog version and must be updated whenever the top changelog version changes.

## Documentation Integrity Checks

Run the repository documentation integrity checks with:

```bash
python3 scripts/check-docs-integrity.py
```

The check covers internal Markdown links, unresolved placeholders outside reusable templates, index completeness for system documents and visible status/version consistency.

## Security and Privacy Baseline

AI-assisted work must follow:

- `security-policy.md` for secrets, sandbox boundaries, sensitive code and security review;
- `privacy-data-handling-policy.md` for private data, external LLM sharing and data minimization.

## System Layers

```text
AI Development System
├── Human Owner
├── ChatGPT Orchestrator
├── Codex Executor
├── AI Roles
├── Documentation
├── Workflow
├── Rules
├── Review Process
├── Evolution Process
└── System Evolution Module
```

## Repository Model

```text
/project
  /ai-system   # rules, roles, prompts, workflow, evolution of the AI system
  /docs        # product documentation: vision, PRD, architecture, backlog, API, UX
  /backend     # backend implementation
  /frontend    # frontend implementation
  /infra       # deployment and infrastructure
  README.md
```

## Files

- `glossary.md` — all terms used by the system.
- `system-prompt.md` — main controlling prompt for the AI Development System.
- `roles.md` — AI roles and their responsibilities.
- `human-interaction.md` — how the human works with ChatGPT and Codex.
- `language-policy.md` — language and localization rules for responses, prompts and documentation.
- `workflow.md` — development stages and gates.
- `rules.md` — global rules and restrictions.
- `system-schemes.md` — compact text schemes for roles, documents and process flow.
- `task-format.md` — standard task format for Codex and AI roles.
- `decision-process.md` — decision statuses and ownership.
- `decision-lifecycle.md` — lifecycle rules for Human Owner decisions.
- `review-process.md` — review and QA rules.
- `review-lifecycle.md` — lifecycle rules for managed reviews and re-review flow.
- `qa-lifecycle.md` — lifecycle rules for QA work and regression checks.
- `knowledge-lifecycle.md` — lifecycle rules for managed knowledge and lessons learned.
- `experiment-lifecycle.md` — lifecycle rules for managed experiments and rollback.
- `improvement-lifecycle.md` — lifecycle rules for managed improvements and conversion paths.
- `change-process.md` — controlled evolution of the AI Development System.
- `change-lifecycle.md` — lifecycle rules for managed system changes.
- `lifecycle-governance.md` — shared governance model for managed lifecycle documents.
- `document-lifecycle.md` — lifecycle rules for source-of-truth documents.
- `process-lifecycle.md` — lifecycle rules for managed processes.
- `task-lifecycle.md` — lifecycle rules for managed tasks.
- `codex-lifecycle.md` — lifecycle rules for Codex execution.
- `prompt-lifecycle.md` — lifecycle rules for prompts and prompt packages.
- `project-integration-model.md` — foldered and root integration modes for concrete projects.
- `foldered-integration.md` — recommended foldered architecture for embedding AI_Development_System into concrete projects.
- `project-control-files.md` — standard project-level control files for concrete repositories.
- `project-bootstrap.md` — workflow for initializing new and existing project repositories.
- `project-system-update.md` — workflow for updating already integrated project control layers.
- `verification-modes.md` — explicit check modes and on-demand browser/visual QA rules.
- `security-policy.md` — security baseline for secrets, sandbox boundaries, sensitive code and automation.
- `privacy-data-handling-policy.md` — privacy and data-handling rules for private data, external LLMs and generated artifacts.
- `aicp-language-policy.md` — approved change proposal for language and localization policy.
- `aicp-security-privacy-policy.md` — approved change proposal for security, privacy and data-handling policy.
- `document-templates.md` — templates for project documents.
- `system-changelog.md` — history of changes to the AI Development System.
- `improvement-log.md` — observations and problems in the system.
- `../scripts/check-docs-integrity.py` — documentation integrity check for links, placeholders, indexes and version/status fields.

## Evolution Module

The `evolution/` directory defines roadmap-driven self-evolution of AI_Development_System.

- `evolution/README.md` — index and operating principle for the system evolution module.
- `evolution/roadmap.md` — strategic and tactical roadmap for AI_Development_System.
- `evolution/evolution-loop.md` — observe → diagnose → propose → plan → execute → verify → review → approve → release → learn loop.
- `evolution/evolution-policy.md` — permissions, boundaries and anti-runaway rules for self-evolution.
- `evolution/owner-evolution-plan.md` — Human Owner-authored intake place for broad system evolution plans.
- `evolution/owner-plan-intake.md` — workflow for mapping owner plans to roadmap, backlog and one bounded next task.
- `evolution/system-health-check.md` — repeatable system health-check checklist.
- `evolution/evolution-backlog.md` — managed backlog of system evolution items.
- `evolution/analysis-report-baseline.md` — baseline findings from the analytical repository report.
- `evolution/templates/system-change-proposal.md` — AI System Change Proposal template.
- `evolution/templates/evolution-task.md` — bounded system evolution task template.
- `evolution/templates/owner-evolution-plan.md` — reusable owner plan intake template.

## Templates

- `templates/foldered/` — recommended templates for `AGENTS.md`, `AI_Development_System/` and `AI_PROJECT/` integration.
- `templates/project/` — root-mode templates for simple or legacy projects.

## Operating Model

```text
Human Owner sets direction
ChatGPT Orchestrator prepares documents, prompts and reviews
Codex Executor changes repository files
Documentation records decisions
AI Development System controls the process
System Evolution Module controls roadmap-driven self-improvement
```

## Minimal Rule

No implementation task should start without:

- a task from the backlog;
- required source documents;
- clear scope and out of scope;
- acceptance criteria;
- expected output;
- review step.

No system evolution task should start without:

- a roadmap item, backlog item, health-check finding, analytical report finding or Human Owner request;
- owner plan intake and mapping when the source is a broad Human Owner evolution plan;
- explicit allowed files;
- verification mode;
- review requirements;
- Human Owner approval requirement assessment;
- changelog impact assessment.
