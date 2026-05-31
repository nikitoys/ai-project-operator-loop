# Improvement Log

Status: Draft

This file records observed process problems and improvement ideas.

Entries here do not change the AI Development System directly.

System changes must go through `change-process.md` and an AI System Change Proposal.

## Template

```md
## IMP-000: Title

### Status
Observed / Proposed / Converted to AICP / Closed

### Problem
What happened?

### Evidence
Where did it happen?

### Impact
What was affected?

### Possible Cause
Why might it have happened?

### Next Step
Observe / Create AICP / Close
```

## Entries

## IMP-001: Unstable Response and Prompt Language

### Status
Converted to AICP

### Problem
AI Development System responses and generated prompts may appear in English when the Human Owner expects Russian output.

### Evidence
The Human Owner reported periodic English answers and prompt artifacts during repository work.

### Impact
Human-facing output becomes less predictable, and generated prompt artifacts may mix review language with execution language without a clear rule.

### Possible Cause
The system did not define a separate language policy for Human Owner-facing responses, prompt package structure and repository documentation.

### Next Step
Converted to `/ai-system/aicp-language-policy.md` and addressed by `/ai-system/language-policy.md`.
