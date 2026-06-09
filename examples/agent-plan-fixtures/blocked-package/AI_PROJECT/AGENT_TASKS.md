# Agent Tasks — Blocked Package Fixture

Status: Draft

## Purpose

Fixture for blocked package exclusion.

## Agent Work Package Registry

| ID | Status | SOP | Role | Parent Task | Verification Mode | Notes |
|---|---|---|---|---|---|---|
| AWP-REQ-001 | accepted | SOP-FEATURE-001 | Business Analyst AI | T-020 | FAST_VALIDATION | Requirements are complete. |
| AWP-BE-001 | blocked | SOP-FEATURE-001 | Backend Developer AI | T-020 | FAST_VALIDATION | Blocked package must not enter ready groups. |
| AWP-FE-001 | ready | SOP-FEATURE-001 | Frontend Developer AI | T-020 | FAST_VALIDATION | Frontend planning can start after requirements. |

## AWP-REQ-001

```text
dependencies: none
```

## AWP-BE-001

```text
dependencies: AWP-REQ-001
```

## AWP-FE-001

```text
dependencies: AWP-REQ-001
```
