# Project Control Connectivity

Status: Draft
Version: v0.1.0

## Purpose

This document defines how AI and Codex sessions discover project-local control documents without loading every document into context by default.

Project control connectivity is the read-order and visibility layer for concrete repositories that use AI_Development_System. It tells an agent which project control files exist, which files must be read for the current task and which files should remain known but unloaded until relevant.

## Problem

Project repositories can gain new local control files over time. If an existing root `AGENTS.md` does not mention the new files, an agent may never discover them.

That is project-control drift: the local control layer contains a document, but the read order does not reliably lead the agent to it.

## Project Control Index

Concrete projects should include:

```text
AI_PROJECT/PROJECT_CONTROL_INDEX.md
```

For Root Control Mode, the equivalent file is:

```text
PROJECT_CONTROL_INDEX.md
```

The index is a compact manifest. It is not product documentation and does not authorize implementation. Its job is to make the project control layer visible and to classify local files by importance and read policy.

## Standard Read Order

Foldered Control Mode sessions should start with:

```text
1. AGENTS.md
2. AI_PROJECT/AGENTS.md
3. AI_PROJECT/PROJECT_CONTROL_INDEX.md
4. AI_PROJECT/PROJECT_OPERATION_PROFILE.md
5. Task-relevant project control files from the index
6. Relevant AI_Development_System source documents when needed
```

Root Control Mode sessions should start with:

```text
1. AGENTS.md
2. PROJECT_CONTROL_INDEX.md
3. PROJECT_OPERATION_PROFILE.md
4. Task-relevant project control files from the index
5. Relevant AI_Development_System source documents when needed
```

## Importance Levels

| Level | Meaning |
|---|---|
| `critical` | Needed to avoid acting outside project authority, scope or current task state. |
| `high` | Usually needed for planning, execution, review or verification decisions. |
| `medium` | Needed for specific workflows such as plan intake, continuation or multi-agent planning. |
| `reference` | Useful to know about, but loaded only when the task calls for it. |

## Read Policies

| Policy | Meaning |
|---|---|
| `always_full` | Read the full document before repository-affecting work in its declared context. |
| `conditional_full` | Read the full document when the current task type, scope or acceptance criteria need it. |
| `known_only` | Keep the document visible in the index, but do not load it unless it becomes relevant. |
| `on_demand` | Load only when explicitly requested or when another loaded document points to it. |

## Required Behavior

Agents should read the index early, then decide which documents to load based on importance, read policy and current task.

Agents should not load every project-control file by default when the index marks a file as `known_only` or `on_demand`.

Agents should include a short `Control Context` section in repository-affecting reports:

```text
Control Context:
- Loaded Control Docs:
- Known But Not Loaded:
- Missing or Drift:
```

## Drift Rules

Report project-control drift when:

- root `AGENTS.md` does not point to the local project control index;
- local `AGENTS.md` does not point to the project control index;
- the project control index omits a standard local control file that exists or should exist;
- `CODEX_WORKFLOW.md` does not require reporting `Control Context`;
- `PROJECT_OPERATION_PROFILE.md` conflicts with specialized local control files.

Drift is a warning by default. It should be reported clearly, but it does not by itself authorize automatic rewrites of local project files.

## Conflict Rules

Local project control files may restrict global defaults.

Local project control files must not weaken:

- Human Owner approval rules;
- lifecycle governance;
- safety and privacy rules;
- explicit forbidden actions;
- sandbox or external-tool boundaries.

If a local control file conflicts with a global system rule, report the conflict and stop unless the global rule explicitly allows local override.

If local project control files conflict with each other, report project-control drift and identify which files need synchronization.
