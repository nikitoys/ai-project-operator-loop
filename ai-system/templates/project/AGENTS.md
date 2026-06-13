# AGENTS.md — {{PROJECT_NAME}}

Status: Draft

## Start Here

Before working in this repository, read:

1. `PROJECT_CONTROL_INDEX.md`
2. `PROJECT_OPERATION_PROFILE.md`
3. `PROJECT_GOAL.md`
4. `CODEX_CURRENT.md` before starting or resuming Codex work
5. `CODEX_TASKS.md` before selecting, creating or executing tasks
6. `docs/verification-policy.md` when checks, QA, browser or visual validation are relevant
7. `CODEX_WORKFLOW.md` before Codex execution, project-control updates or system updates
8. `OWNER_PLAN.md` when doing plan intake or backlog refresh
9. `CODEX_PLAN.md` during planning or backlog refresh
10. `CODEX_SESSION_LOG.md` when continuing prior work
11. AI_Development_System security/privacy policies when relevant and available

## Project Context

Project: `{{PROJECT_NAME}}`
Target App Directory: `{{TARGET_APP_DIRECTORY}}`
Human Owner Language: `{{HUMAN_OWNER_LANGUAGE}}`
Default Verification Mode: `{{DEFAULT_VERIFICATION_MODE}}`
Control Index: `PROJECT_CONTROL_INDEX.md`
Operation Profile: `PROJECT_OPERATION_PROFILE.md`

## Core Rules

- Human Owner makes final decisions.
- Codex is an executor, not a product decision maker.
- `OWNER_PLAN.md` is planning input, not executable scope.
- Do not implement without an approved task and acceptance criteria.
- Do not touch files outside approved scope.
- Use `PROJECT_CONTROL_INDEX.md` to decide which control files to load instead of loading every local document by default.
- Follow `PROJECT_OPERATION_PROFILE.md` for project-local operating defaults.
- Follow `docs/verification-policy.md` before running checks.
- Inherit AI_Development_System security and privacy baselines when the project embeds or references them.
- Browser, Playwright, screenshots, console checks and visual QA are on-demand only.
