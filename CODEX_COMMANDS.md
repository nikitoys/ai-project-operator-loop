# Codex Operator Commands

Short operator commands must be interpreted through `CODEX_WORKFLOW.md`.

## `Старт`

Reads the core project memory and reports readiness, current state, and next
suggested operator action. Does not change files. Use at the start of a fresh
session.

## `Статус`

Reports current status, approved task, phase, changed files, checks, blockers,
and next action. Does not change files. Use to inspect the loop state.

## `Советник`

Assesses project direction, stalled work, and possible drift, then recommends
one next operator step. Does not change files. Use for strategic review.

## `Аудит`

Checks consistency across state and workflow docs and reports stale or
contradictory state. Does not change files. Use before relying on project
memory.

## `Разобрать план`

Reads `OWNER_PLAN.md`, compares it with current project state, identifies what is already done, partially done, missing, unclear or out of scope, proposes updates to `CODEX_PLAN.md` and `CODEX_TASKS.md`, and stops. Does not implement anything.

## `План`

Reads project state and proposes 3-5 next tasks ranked by value. Does not
change files. Use when choosing the next task.

## `План подробнее N`

Expands task `N` into scope, checks, done criteria, and commit message. Does
not change files. Use before approving a task.

## `Утверждаю задачу N`

Records the selected task in `CODEX_CURRENT.md` with `status: approved`.
Changes state files only. Use when selecting a planned task.

## `Выполняй`

Runs the approved task through the One-Task Loop, checks it, commits once, and
stops. Changes only files allowed by the approved task. Use after approval.

## `Выполняй без коммита`

Runs the approved task and checks, then stops before commit. Changes allowed
task files. Use when you want to review the diff first.

## `Коммить`

Commits approved scoped changes only after checks passed or skipped checks are
explained. Changes git history only. Use after review or `Выполняй без коммита`.

## `Стоп`

Stops current work and marks `CODEX_CURRENT.md` as `stopped`. Changes state
files only. Use when pausing unfinished work.

## `Продолжай текущую`

Reads `CODEX_CURRENT.md` and continues only the approved or stopped task.
Changes allowed task files. Use to resume a paused loop.

## `Отмени текущую`

Marks `CODEX_CURRENT.md` as `cancelled` without deleting changes unless told.
Changes state files only. Use to abandon the current task.

## Verification Mode Commands

## `Код быстро`

Selects `CODE_ONLY_FAST` for ordinary code-only changes, documentation changes and fast bugfixes. Allows only fast checks such as `git diff --check` and `git status --short`; optional typecheck only when source files changed and practical.

## `Проверка быстро`

Selects `FAST_VALIDATION`. Allows standard validation such as typecheck, tests and build when available. Does not allow browser, Playwright, screenshots, console inspection or manual visual QA unless explicitly requested.

## `Браузер проверить`

Selects `BROWSER_SMOKE`. Allows a limited browser/runtime check. Use only when the Human Owner explicitly requests browser verification.

## `Визуально проверить`

Selects `VISUAL_QA`. Allows screenshots, visual inspection, Playwright visual checks or browser snapshots only when explicitly requested or required by task acceptance criteria.
