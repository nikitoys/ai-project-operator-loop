# Verification Policy — {{PROJECT_NAME}}

Status: Draft

## Default Verification Mode

```text
{{DEFAULT_VERIFICATION_MODE}}
```

## Modes

- `NONE` — no command execution; explain verification risk.
- `SMOKE` — 30 sec budget; instant critical checks only.
- `FAST` — 120 sec budget; instant and fast checks relevant to changed files.
- `STANDARD` — 300 sec budget; `FAST` plus selected standard checks that fit the budget.
- `FULL` — explicit full verification; may run slow checks only when allowed and budgeted.
- `RELEASE` — explicit release verification; may include release/golden checks when available.
- `MANUAL` — Human Owner chooses checks, budget and slow-check permission.

Legacy aliases:

- `CODE_ONLY_FAST` maps to `FAST`.
- `FAST_VALIDATION` maps to `STANDARD`.
- `BROWSER_SMOKE` is an on-demand browser QA overlay.
- `VISUAL_QA` is an on-demand visual QA overlay.

## Runtime Tracking Fields

Tasks should declare:

```text
Verification Mode:
Verification Budget:
Allowed Slow Checks: true/false
Runtime Tracking: enabled/disabled
```

## On-Demand Browser and Visual QA Rule

Browser automation, Playwright/MCP browser sessions, screenshots, manual visual inspections and browser console checks are on-demand only.

Do not run them unless the Human Owner explicitly requests them or the current task explicitly lists them in acceptance criteria.

Do not mark a task `PARTIAL` only because browser checks, screenshots, visual inspection or console checks were skipped, unless those checks were explicitly required.

## System Update Checks

For AI system bootstrap or update, use `FAST` unless explicitly instructed otherwise.

Slow, full, release, browser, visual and golden-scenario checks are not default.
