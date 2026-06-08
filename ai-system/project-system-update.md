# Project System Update

Status: Draft
Version: v0.1.0

## Purpose

This document defines how to update AI_Development_System inside a project that already adopted it.

Project system update is a controlled migration of the local project control layer. It is not application implementation.

## Core Principle

Update upstream system files separately from local project control files.

```text
AI_Development_System/  -> upstream system copy, may be refreshed
AI_PROJECT/             -> local project control layer, must be merged
application code        -> out of scope
```

## Trigger Commands

Recommended Human Owner commands:

```text
Обновить AI-систему
Обновить систему
Проверить обновление AI-системы
```

These commands must not start application implementation.

## Standard Update Flow

```text
Human Owner asks to update AI system
-> classify as Project System Update
-> read local control files
-> read current AI_Development_System standard and templates
-> compare local project state with current standard
-> produce migration report
-> Human Owner approves or requests rework
-> update control files only
-> update AI_DEV_SYSTEM_VERSION.md
-> run CODE_ONLY_FAST checks only
-> stop
```

## Merge Rules

Do not overwrite local files blindly.

When updating an existing project:

- preserve local project mission, constraints, target app directory and owner plan;
- preserve local command aliases unless they conflict with system safety;
- add missing required files;
- add missing sections where useful;
- update verification mode and browser or visual QA boundaries when missing;
- record conflicts instead of silently resolving them;
- ask Human Owner before replacing any local control file.

## Files That May Be Updated

In Foldered Control Mode:

```text
AGENTS.md
AI_PROJECT/AGENTS.md
AI_PROJECT/PROJECT_GOAL.md
AI_PROJECT/OWNER_PLAN.md
AI_PROJECT/CODEX_COMMANDS.md
AI_PROJECT/CODEX_WORKFLOW.md
AI_PROJECT/CODEX_PLAN.md
AI_PROJECT/CODEX_CURRENT.md
AI_PROJECT/CODEX_TASKS.md
AI_PROJECT/CODEX_SESSION_LOG.md
AI_PROJECT/PROMPTS.md
AI_PROJECT/AI_DEV_SYSTEM_VERSION.md
AI_PROJECT/docs/verification-policy.md
```

In Root Control Mode, equivalent root control files may be updated.

## Files That Must Not Be Updated

Do not modify application or product code during project system update.

Exceptions require a separate approved implementation task.

## Migration Report Format

Project system update should report:

```text
Status:
Current Integration Mode:
Target Integration Mode:
Current AI Development System Version:
Target AI Development System Version:
Already Compatible:
Missing Files:
Files to Merge:
Conflicts:
Application Code Modified: yes/no
Recommended Action:
Required Human Owner Decision:
```

## Version Record

Projects should store local adoption metadata in:

```text
AI_PROJECT/AI_DEV_SYSTEM_VERSION.md
```

## Verification

Default verification mode for project system update is:

```text
CODE_ONLY_FAST
```

Allowed checks:

```bash
git diff --check
git status --short
```

Do not run browser, Playwright, screenshots, application builds or app tests unless the Human Owner explicitly requests them for this update.
