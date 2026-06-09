# Agent Tasks — Cycle Fixture

Status: Draft

## Purpose

Fixture for dependency cycle detection.

## Agent Work Package Registry

| ID | Status | SOP | Role | Parent Task | Verification Mode | Notes |
|---|---|---|---|---|---|---|
| AWP-REQ-001 | ready | SOP-FEATURE-001 | Business Analyst AI | T-020 | FAST_VALIDATION | Depends on QA in this cycle fixture. |
| AWP-QA-001 | ready | SOP-FEATURE-001 | QA Engineer AI | T-020 | FAST_VALIDATION | Depends on requirements in this cycle fixture. |

## AWP-REQ-001

```text
dependencies: AWP-QA-001
```

## AWP-QA-001

```text
dependencies: AWP-REQ-001
```
