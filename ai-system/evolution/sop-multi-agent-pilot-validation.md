# SOP / Multi-Agent Pilot Validation

Status: Draft  
Version: v0.2.0

## Purpose

This document records pilot validation findings for the SOP-guided and optional multi-agent layer.

The goal is to test whether the current documents, templates, golden project example and dry-run planning helper provide enough evidence to support the next runtime decision step.

This document does not approve runtime implementation.

## Scope

In scope:

- validate the filled `examples/golden-project/` multi-agent planning example;
- run dry-run agent planning commands;
- run documentation integrity validation;
- manually review SOP, Agent Work Package, dependency, lock, result, review, QA and metric coverage;
- manually review safety boundaries;
- record findings, limitations and recommended follow-ups.

Out of scope:

- no runtime implementation;
- no Codex execution;
- no branch, worktree, merge or acceptance automation;
- no script fixes;
- no spec changes;
- no template changes;
- no product or application code changes.

## Source Documents and Artifacts

- `ai-system/evolution/sop-multi-agent-implementation-plan.md`
- `ai-system/sop-model.md`
- `ai-system/agent-work-package.md`
- `ai-system/multi-agent-planning.md`
- `ai-system/parallel-execution-policy.md`
- `ai-system/agent-result-intake.md`
- `ai-system/integration-review.md`
- `spec/sops.json`
- `spec/agent-work-package.schema.json`
- `spec/agent-result.schema.json`
- `spec/parallel-policy.json`
- `ai-system/templates/foldered/AI_PROJECT/AGENT_PLAN.md`
- `ai-system/templates/foldered/AI_PROJECT/AGENT_TASKS.md`
- `ai-system/templates/foldered/AI_PROJECT/AGENT_LOCKS.md`
- `ai-system/templates/foldered/AI_PROJECT/AGENT_RESULTS.md`
- `ai-system/templates/foldered/AI_PROJECT/AGENT_METRICS.md`
- `examples/golden-project/`
- `scripts/agent-plan-mvp.py`
- `scripts/check-docs-integrity.py`
- `scripts/validate-agent-plan-fixtures.py`
- `scripts/validate-system.py`

## Pilot Scenarios

### 1. Golden Project Dry-Run Validation

Commands:

```bash
python3 scripts/agent-plan-mvp.py validate --project-root examples/golden-project
python3 scripts/agent-plan-mvp.py check-locks --project-root examples/golden-project
python3 scripts/agent-plan-mvp.py list-parallel-groups --project-root examples/golden-project
python3 scripts/agent-plan-mvp.py generate-prompts --project-root examples/golden-project
```

Observed results:

- `validate` found all five `AI_PROJECT/AGENT_*` files.
- `validate` recognized four Agent Work Packages: `AWP-REQ-001`, `AWP-BE-001`, `AWP-FE-001` and `AWP-QA-001`.
- Each package was reported as ready and complete enough for planning.
- `check-locks` read `AI_PROJECT/AGENT_LOCKS.md` and detected no lock conflicts from available data.
- `list-parallel-groups` listed one informational candidate group containing all four packages.
- `generate-prompts` printed four bounded prompt drafts for review only and did not execute them.

### 2. Documentation Integrity Validation

Command:

```bash
python3 scripts/check-docs-integrity.py
```

Observed result:

- Documentation integrity check passed before recording this EVOL-018 document and passed again after documentation updates.

### 3. Manual Golden Example Review

The golden example demonstrates:

- selected SOP: `SOP-FEATURE-001`;
- Agent Work Package decomposition;
- dependencies between requirements, backend, frontend and QA packages;
- `allowed_files` and `locked_files`;
- candidate parallel group `CPG-001` as informational only;
- Human Owner approval boundary;
- result intake placeholders;
- integration review placeholder/status;
- QA handoff placeholder/status;
- metrics placeholder/status;
- dry-run helper usage.

### 4. Manual Safety Boundary Review

The current SOP / optional multi-agent layer preserves these boundaries:

- no automatic execution;
- no automatic merge;
- no automatic acceptance;
- Human Owner approval remains required;
- candidate parallel groups are informational until approved under the Parallel Execution Policy;
- sequential execution remains the default.

### 5. Historical Tool Limitation Review

At the time of EVOL-018, `scripts/agent-plan-mvp.py` performed useful Markdown-oriented dry-run reporting but did not deeply parse dependency graphs from the planning files.

As a result, `list-parallel-groups` could list all non-blocked packages as one informational candidate group. In the golden example, the intended candidate group was narrower: `CPG-001` is `AWP-BE-001 + AWP-FE-001` only after `AWP-REQ-001` has been accepted.

This limitation was routed to `EVOL-020` and later closed by dependency-aware dry-run planning. EVOL-026 evidence below reflects the current dependency-aware behavior.

## EVOL-026 Expanded Pilot Evidence

This section expands pilot evidence beyond the original golden example.

Validation categories:

- Validated dry-run behavior: behavior confirmed by repository files and read-only validation commands.
- Manually simulated orchestration behavior: lifecycle and review behavior represented as documented manual process, not automated execution.
- Future runtime behavior: not validated and not approved.

### PILOT-DOC-001: Documentation-Only Evolution Change

- Pilot id: `PILOT-DOC-001`
- Pilot type: Documentation-only change
- Purpose: Validate that a bounded AI Development System documentation change can be planned, recorded, checked and routed without runtime execution.
- Input/task summary: Close a documentation evolution item by updating source-of-truth Markdown, roadmap, backlog, changelog and README version mirrors.
- SOP/workflow used: Controlled system evolution flow from `change-process.md`, documentation review rules from `review-process.md`, and Human Owner decision boundaries from `human-interaction.md`.
- AWP created or expected: Expected single documentation AWP such as `AWP-DOC-001` for source document updates and `AWP-REVIEW-001` for review/verification if represented in Agent Work Package form.
- Dependency graph shape: Linear; `AWP-DOC-001 -> AWP-REVIEW-001`.
- Candidate parallel groups: None. Documentation update and review are sequential because review depends on completed documentation changes.
- Agent Result Intake usage: Manually simulated. A hardened Agent Result record would capture `awp_id`, changed documents, claims, verification, risks, followups, scope compliance and safety boundary compliance.
- Integration Review usage: Manually simulated. Integration Review checks changelog/version consistency, roadmap/backlog consistency, README mirrors and absence of runtime authorization.
- Human Owner approval point: Human Owner approval remains required before accepting the documentation change as done.
- Verification commands:

```bash
python3 scripts/check-docs-integrity.py
python3 scripts/validate-system.py
```

- Observed result: Read-only validation can verify documentation integrity and broader system checks without modifying files.
- Limitations: This pilot validates documentation governance and repository consistency only; it does not validate product code execution or real agent runtime.
- Follow-up improvements: Continue using the hardened Agent Result schema for documentation tasks when L3 manual orchestration pilots are recorded.

### PILOT-CODE-001: Small Tooling Change

- Pilot id: `PILOT-CODE-001`
- Pilot type: Small code/tooling change
- Purpose: Validate that a small bounded repository script change can be planned and verified while preserving dry-run boundaries.
- Input/task summary: Improve or validate a local planning helper without enabling execution, branch/worktree automation, merge automation or acceptance automation.
- SOP/workflow used: Agent planning and dry-run validation workflow from `multi-agent-planning.md`, safety boundaries from `parallel-execution-policy.md`, result handoff from `agent-result-intake.md`, and integration checks from `integration-review.md`.
- AWP created or expected: Expected `AWP-TOOL-001` for the script change and `AWP-QA-001` for validation/review.
- Dependency graph shape: Linear; `AWP-TOOL-001 -> AWP-QA-001`.
- Candidate parallel groups: None. QA/review remains blocked until the script change is complete.
- Agent Result Intake usage: Manually simulated. A result record must list changed script files, claims about dry-run behavior, commands run, limitations, risks and followups.
- Integration Review usage: Manually simulated. Integration Review must inspect whether the change stayed within tooling scope and preserved forbidden automation boundaries.
- Human Owner approval point: Human Owner approval remains required before accepting the tooling change.
- Verification commands:

```bash
python3 -m py_compile scripts/agent-plan-mvp.py scripts/validate-agent-plan-fixtures.py scripts/validate-system.py
python3 scripts/validate-agent-plan-fixtures.py
python3 scripts/validate-system.py
```

- Observed result: Current validation covers Python compile checks, dependency-aware planning fixtures and the full read-only system validation path.
- Limitations: This pilot validates local tooling behavior only. It does not execute Codex, launch agents, create worktrees, merge branches or accept work.
- Follow-up improvements: Add narrower fixture cases when new planning edge cases are discovered.

### PILOT-MA-001: Multi-Agent Parallel Planning Case

- Pilot id: `PILOT-MA-001`
- Pilot type: Multi-agent parallel planning case
- Purpose: Validate dependency-aware dry-run planning for a requirements-first, backend/frontend-parallel, QA-after-integration pattern.
- Input/task summary: Plan a Task Tracker due-date filter enhancement using requirements, backend, frontend and QA/integration Agent Work Packages.
- SOP/workflow used: `SOP-FEATURE-001`, Multi-Agent Planning workflow, Parallel Execution Policy, Agent Result Intake and Integration Review.
- AWP created or expected:
  - `AWP-REQ-001` for requirements clarification.
  - `AWP-BE-001` for backend changes after requirements are complete.
  - `AWP-FE-001` for frontend changes after requirements are complete.
  - `AWP-QA-001` for QA/integration after backend and frontend are complete.
- Dependency graph shape: Diamond; `AWP-REQ-001 -> AWP-BE-001 + AWP-FE-001 -> AWP-QA-001`.
- Candidate parallel groups:
  - In `examples/golden-project`, with no completed prerequisites, ready layer is `AWP-REQ-001` and there is no candidate parallel group.
  - In `examples/agent-plan-fixtures/accepted-prerequisite`, after `AWP-REQ-001` is accepted, the valid candidate group is `AWP-BE-001, AWP-FE-001`.
  - `AWP-QA-001` is excluded until both `AWP-BE-001` and `AWP-FE-001` are complete.
- Agent Result Intake usage: Manually simulated. Each logical agent result must use the hardened Agent Result schema and record changed files, claims, verification, risks, blockers, followups, scope compliance and safety boundary compliance.
- Integration Review usage: Manually simulated. Integration Review must inspect backend/frontend compatibility, unresolved risks, QA readiness, result claims, verification evidence and Human Owner approval requirements.
- Human Owner approval point: Human Owner must approve any parallel execution decision, result acceptance and final closure. Candidate groups are informational only.
- Verification commands:

```bash
python3 scripts/agent-plan-mvp.py list-parallel-groups --project-root examples/golden-project
python3 scripts/agent-plan-mvp.py list-parallel-groups --project-root examples/agent-plan-fixtures/accepted-prerequisite
python3 scripts/validate-agent-plan-fixtures.py
python3 scripts/validate-system.py
```

- Observed result: Dependency-aware dry-run planning reports `AWP-REQ-001` as the first ready layer in the golden project. After an accepted prerequisite fixture, it reports `AWP-BE-001, AWP-FE-001` as the valid informational candidate group and excludes `AWP-QA-001` until backend and frontend prerequisites are complete.
- Limitations: This is validated dry-run planning and manually simulated orchestration only. It does not validate automatic execution, runtime scheduling, branch/worktree lifecycle, automatic merge or automatic acceptance.
- Follow-up improvements: Record at least one full L3 manual orchestration pilot before reconsidering assisted execution.

### EVOL-026 Safety Boundary Review

No pilot scenario approves runtime execution.

Validated dry-run behavior:

- documentation integrity and system validation commands run locally;
- dependency-aware planning fixtures pass;
- golden project dry-run validation passes;
- candidate parallel groups remain informational.

Manually simulated orchestration behavior:

- Agent Result Intake is represented as a required manual record;
- Integration Review is represented as a required manual review step;
- Human Owner approval remains the decision gate.

Future/not-yet-validated runtime behavior:

- automatic Codex execution;
- automatic multi-agent execution;
- branch/worktree lifecycle automation;
- automatic merge;
- automatic acceptance;
- automatic QA/review closure.

## Findings

### FINDING-001: Golden Project Planning Files Are Discoverable

- Finding ID: `FINDING-001`
- Type: Success
- Severity: Minor
- Evidence: `validate` reported all five `AI_PROJECT/AGENT_*` files as present.
- Impact: The foldered example is usable as a pilot artifact for agent planning validation.
- Recommended follow-up: Keep the golden project as the primary non-runtime example for future pilot checks.
- Suggested target EVOL or future backlog item: Covered by `EVOL-017`; no new backlog item required.

### FINDING-002: Agent Work Packages Are Recognized

- Finding ID: `FINDING-002`
- Type: Success
- Severity: Minor
- Evidence: `validate` recognized `AWP-REQ-001`, `AWP-BE-001`, `AWP-FE-001` and `AWP-QA-001`.
- Impact: The current template and example format is sufficient for simple package discovery.
- Recommended follow-up: Preserve table-based package entries unless future parser work introduces a stricter format.
- Suggested target EVOL or future backlog item: No new backlog item required.

### FINDING-003: Lock Conflict Check Works for Available Data

- Finding ID: `FINDING-003`
- Type: Success
- Severity: Minor
- Evidence: `check-locks` read `AI_PROJECT/AGENT_LOCKS.md` and reported no detected lock conflicts.
- Impact: The helper can support early file-scope conflict review when lock data is present.
- Recommended follow-up: Continue using `AGENT_LOCKS.md` as the explicit lock registry for pilot examples.
- Suggested target EVOL or future backlog item: No new backlog item required.

### FINDING-004: Candidate Parallel Group Reporting Was Over-Broad

- Finding ID: `FINDING-004`
- Type: Historical Limitation
- Severity: Major
- Evidence: `list-parallel-groups` reported `candidate_group_1: AWP-REQ-001, AWP-BE-001, AWP-FE-001, AWP-QA-001`, while the golden example records intended `CPG-001` as `AWP-BE-001 + AWP-FE-001` only after `AWP-REQ-001`.
- Impact: The dry-run helper is useful for visibility, but it should not be treated as a reliable dependency-aware parallel planner yet.
- Recommended follow-up: Completed by `EVOL-020`; continue validating dependency-aware behavior through fixtures and CI.
- Suggested target EVOL or future backlog item: Closed by `EVOL-020`; original observation recorded as `IMP-002`.

### FINDING-005: Prompt Draft Generation Preserves Execution Boundaries

- Finding ID: `FINDING-005`
- Type: Success
- Severity: Minor
- Evidence: `generate-prompts` printed four prompt drafts and explicitly stated they were generated for review only and not sent to Codex.
- Impact: The helper can prepare bounded prompt drafts without becoming an execution runtime.
- Recommended follow-up: Keep prompt generation dry-run only unless a future approved evolution task changes the boundary.
- Suggested target EVOL or future backlog item: No new backlog item required.

### FINDING-006: Documentation Integrity Passed

- Finding ID: `FINDING-006`
- Type: Success
- Severity: Minor
- Evidence: `python3 scripts/check-docs-integrity.py` passed before EVOL-018 documentation was recorded and passed again after documentation updates.
- Impact: The current documentation baseline is coherent enough for pilot recording and updated index/version references remain consistent.
- Recommended follow-up: Continue running the integrity check after each bounded evolution task.
- Suggested target EVOL or future backlog item: No new backlog item required.

### FINDING-007: Runtime Integration Is Not Justified Yet

- Finding ID: `FINDING-007`
- Type: Risk
- Severity: Major
- Evidence: The governance layer, templates, specs and dry-run helper work as documentation and reporting artifacts, but dependency-aware planning remains limited and no live execution pilot has been approved.
- Impact: Starting runtime automation now would exceed the evidence gathered by this pilot and could weaken the one-task, approval-gated workflow.
- Recommended follow-up: Use `EVOL-019` to record a runtime decision. Current evidence supports deferring runtime integration and continuing with bounded dry-run improvements.
- Suggested target EVOL or future backlog item: `EVOL-019`; possible follow-up `EVOL-020`.

## Follow-Up Routing

| Finding | Route | Notes |
| --- | --- | --- |
| `FINDING-001` | No new item | Success covered by `EVOL-017`. |
| `FINDING-002` | No new item | Current examples are parseable enough for simple discovery. |
| `FINDING-003` | No new item | Lock checks work with available data. |
| `FINDING-004` | Closed follow-up | Routed to `EVOL-020` and `IMP-002`; dependency-aware dry-run planning is now implemented. |
| `FINDING-005` | No new item | Prompt drafts remain dry-run only. |
| `FINDING-006` | No new item | Re-run after documentation updates. |
| `FINDING-007` | EVOL-019 decision input | Recommendation is to defer runtime integration. |

No AICP, spec change or template change is required by this pilot record.

## Recommendation for EVOL-019 Runtime Decision

Recommended EVOL-019 decision: `DEFERRED`.

Reasoning:

- the governance-first SOP / optional multi-agent layer is coherent as documentation, templates, specs and dry-run reporting;
- the golden project can demonstrate bounded planning without product runtime code;
- the dry-run helper preserves safety boundaries;
- dependency-aware parallel group calculation is not mature enough to justify runtime execution;
- Human Owner approval, review, QA and final acceptance must remain manual gates.

EVOL-019 should record the Human Owner runtime decision. It should not start runtime implementation unless the Human Owner explicitly approves a new bounded runtime experiment.

## Remaining Risks

- Markdown-oriented parsing may miss malformed dependencies, ambiguous package relationships or hidden lock conflicts.
- Candidate parallel groups require manual review until dependency parsing improves.
- Future runtime proposals could accidentally weaken the one-task loop unless EVOL-019 keeps the governance-first boundary explicit.
- Golden project coverage is useful but still a single example, not broad validation across multiple project types.

## Next-Step Recommendation

Next bounded phase: `EVOL-019 — Decide whether runtime integration is justified`.

Recommended outcome for EVOL-019: record a `DEFERRED` runtime decision and allow only bounded dry-run improvements unless the Human Owner explicitly approves a separate experiment.

Recommended follow-up after EVOL-019: consider `EVOL-020 — Improve dry-run agent planner dependency parsing`.
