# AGENTS.md — {{PROJECT_NAME}} AI Bootstrap

This project uses AI Development System in Foldered Control Mode.

## Directory Model

```text
/AI_Development_System   # reusable upstream AI Development System
/AI_PROJECT              # local project control files and project state
{{TARGET_APP_DIRECTORY}} # target application/product code
```

## Mandatory First Read

Before repository-affecting work, read:

```text
/AI_PROJECT/AGENTS.md
/AI_PROJECT/PROJECT_GOAL.md
/AI_PROJECT/docs/verification-policy.md
/AI_PROJECT/CODEX_WORKFLOW.md
/AI_PROJECT/CODEX_CURRENT.md
/AI_PROJECT/CODEX_TASKS.md
/AI_Development_System/AGENTS.md
/AI_Development_System/ai-system/rules.md
```

When doing AI system bootstrap, update or evolution, also read:

```text
/AI_Development_System/ai-system/project-integration-model.md
/AI_Development_System/ai-system/project-control-files.md
/AI_Development_System/ai-system/project-bootstrap.md
/AI_Development_System/ai-system/project-system-update.md
```

## Boundaries

- Application code lives in `{{TARGET_APP_DIRECTORY}}`.
- Local project control files live in `/AI_PROJECT`.
- Reusable AI system files live in `/AI_Development_System`.
- Do not modify `/AI_Development_System` unless the task explicitly targets AI system update, synchronization or evolution.
- Do not modify application code during AI system bootstrap or system update.
- Do not treat `AI_PROJECT/OWNER_PLAN.md` as executable scope.

## Default Verification Mode

```text
{{DEFAULT_VERIFICATION_MODE}}
```

Browser automation, Playwright/MCP browser sessions, screenshots, browser console checks and manual visual QA are on-demand only.
