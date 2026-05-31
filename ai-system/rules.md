# Rules

Status: Draft

## Core Rules

1. Documentation is the source of truth.
2. The Human Owner makes final decisions.
3. AI roles work only inside their responsibility area.
4. Codex is an executor, not a product decision maker.
5. MVP focus has priority over unnecessary completeness.

## Documentation Rules

1. Product decisions must be reflected in `/docs`.
2. System decisions must be reflected in `/ai-system`.
3. If implementation changes behavior, relevant documentation must be updated.
4. If documentation and code conflict, the conflict must be reported.

## Implementation Rules

1. Do not implement without a backlog task.
2. Do not implement without acceptance criteria.
3. Do not add functionality outside task scope.
4. Do not change architecture without approval.
5. Do not change API contracts without updating API Documentation.
6. Do not mix unrelated backend, frontend, infrastructure and documentation work unless the task explicitly allows it.

## Review Rules

1. Every implementation task must pass review.
2. Review must check task scope, architecture, security, readability and error handling.
3. QA must check acceptance criteria and negative scenarios.
4. Critical issues block acceptance.
5. Major issues require fix or explicit human decision.

## Evolution Rules

1. AI Development System cannot be changed directly.
2. Every system change requires an AI System Change Proposal.
3. System changes must be recorded in `system-changelog.md`.
4. System changes should not be mixed with application implementation tasks.
5. Experiments must have success criteria and a final decision.

## Codex Rules

Every Codex prompt should include:

- role;
- context;
- input documents;
- task ID;
- scope;
- out of scope;
- expected files;
- acceptance criteria;
- result format.

Codex must report:

- changed files;
- summary;
- tests;
- errors;
- questions;
- diff or key changes.
