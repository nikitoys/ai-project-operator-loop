# Project Control Index — {{PROJECT_NAME}}

Status: Draft

## Purpose

This file is the compact read-order map for root-local AI control documents.

Read it after root `AGENTS.md`. Use it to decide which project control files must be loaded for the current task and which files should remain known but unloaded until relevant.

## Reading Rules

- `critical` documents protect project authority, scope and current task state.
- `high` documents guide planning, execution, review and verification.
- `medium` documents support specific workflows such as plan intake, continuation or multi-agent planning.
- `reference` documents are loaded on demand.
- `always_full` means read the full document before repository-affecting work in its declared context.
- `conditional_full` means read the full document when the current task needs it.
- `known_only` means keep the file visible without loading it by default.
- `on_demand` means load only when explicitly requested or referenced by loaded context.

## Project Control Documents

| Path | Importance | Read Policy | Read When |
|---|---|---|---|
| `PROJECT_OPERATION_PROFILE.md` | critical | always_full | Before repository-affecting work. |
| `PROJECT_GOAL.md` | critical | always_full | Before planning, implementation, review or scope decisions. |
| `CODEX_CURRENT.md` | critical | always_full | Before starting or resuming Codex work. |
| `CODEX_TASKS.md` | high | conditional_full | Before selecting, creating or executing tasks. |
| `docs/verification-policy.md` | high | conditional_full | Before running checks, QA, browser sessions or visual validation. |
| `CODEX_WORKFLOW.md` | high | conditional_full | Before Codex execution, project-control updates or system updates. |
| `OWNER_PLAN.md` | medium | conditional_full | During plan intake, backlog refresh or owner-roadmap review. |
| `CODEX_PLAN.md` | medium | conditional_full | During planning, sequencing or backlog grooming. |
| `CODEX_SESSION_LOG.md` | medium | conditional_full | During continuation, result review, audit or handoff. |
| `CODEX_COMMANDS.md` | reference | on_demand | When interpreting short operator commands. |
| `PROMPTS.md` | reference | on_demand | When preparing reusable prompt packages. |
| `AI_DEV_SYSTEM_VERSION.md` | reference | conditional_full | During system update, synchronization or audit. |

## Inherited System Documents

| Path | Importance | Read Policy | Read When |
|---|---|---|---|
| `AI_Development_System/AGENTS.md` | high | conditional_full | When global AI Development System rules are needed. |
| `AI_Development_System/ai-system/rules.md` | high | conditional_full | When global rules or conflicts are involved. |
| `AI_Development_System/ai-system/security-policy.md` | high | conditional_full | Before secrets, credentials, sensitive code, sandbox or security work. |
| `AI_Development_System/ai-system/privacy-data-handling-policy.md` | high | conditional_full | Before private data, personal data, external LLM or data-sharing work. |

## Control Context Reporting

Repository-affecting results should include:

```text
Control Context:
- Loaded Control Docs:
- Known But Not Loaded:
- Missing or Drift:
```

## Drift Rules

- If root `AGENTS.md` does not mention `PROJECT_CONTROL_INDEX.md`, report project-control drift.
- If this index omits a standard project control file, report project-control drift.
- If `PROJECT_OPERATION_PROFILE.md` conflicts with specialized local control files, report project-control drift.
- Drift does not authorize rewriting local files without an approved project-control task.
