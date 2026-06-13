# AI_PROJECT/AGENTS.md — Task Tracker

Status: Draft

## Purpose

This file defines local AI/Codex instructions for the Task Tracker example repository.

## Project Context

Project: `Task Tracker`
Target App Directory: `task-tracker-app`
Human Owner Language: `English`
Default Verification Mode: `FAST_VALIDATION`
Control Index: `AI_PROJECT/PROJECT_CONTROL_INDEX.md`
Operation Profile: `AI_PROJECT/PROJECT_OPERATION_PROFILE.md`

## Start Here

Read in order:

1. `AI_PROJECT/PROJECT_CONTROL_INDEX.md`
2. `AI_PROJECT/PROJECT_OPERATION_PROFILE.md`
3. `AI_PROJECT/PROJECT_GOAL.md`
4. `AI_PROJECT/CODEX_CURRENT.md` before starting or resuming Codex work
5. `AI_PROJECT/CODEX_TASKS.md` before selecting, creating or executing tasks
6. `AI_PROJECT/docs/verification-policy.md` when checks, QA, browser or visual validation are relevant
7. `AI_PROJECT/CODEX_WORKFLOW.md` before Codex execution, project-control updates or system updates
8. `AI_PROJECT/OWNER_PLAN.md` when doing plan intake
9. `AI_PROJECT/CODEX_PLAN.md` during planning or backlog refresh
10. `AI_PROJECT/AGENT_ASSIGNMENTS.md` when doing L3 manual orchestration
11. `AI_PROJECT/CODEX_SESSION_LOG.md` when continuing prior work
12. `AI_Development_System/AGENTS.md` when system-level rules are needed

## Core Rules

- Human Owner makes final decisions.
- Codex is an executor, not a product decision maker.
- `OWNER_PLAN.md` is planning input, not executable scope.
- Do not implement without an approved task and acceptance criteria.
- Do not touch files outside approved scope.
- Use `PROJECT_CONTROL_INDEX.md` to decide which control files to load instead of loading every local document by default.
- Follow `PROJECT_OPERATION_PROFILE.md` for project-local operating defaults.
- Follow `docs/verification-policy.md` before running checks.
- Follow inherited AI_Development_System security and privacy baselines.
- Browser, Playwright, screenshots, console checks and visual QA are on-demand only.
