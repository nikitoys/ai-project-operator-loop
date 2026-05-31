# Prompt Lifecycle and Codex Prompt Factory

Status: Draft  
Version: v0.1.0

## Purpose

This document defines how prompts are created, reviewed, approved, executed and improved inside the AI Development System.

Prompts are managed artifacts. They should not be treated as random chat messages when they affect repository work, Codex execution or the AI Development System itself.

## Core Idea

The Human Owner should not manually write detailed Codex prompts every time.

Instead:

```text
Human Intent
→ ChatGPT Orchestrator
→ Prompt Draft
→ Human Review
→ Approved Prompt Package
→ Codex Execution
→ Result Review
→ Prompt Improvement if needed
```

## Codex Prompt Factory

Codex Prompt Factory is the mechanism that turns a Human Owner intent into a structured prompt package for Codex.

It is operated by ChatGPT Orchestrator.

## Prompt Types

## 1. System Prompt

Defines the behavior of the whole AI Development System.

Source document:

```text
/ai-system/system-prompt.md
```

## 2. Role Prompt

Defines behavior of a specific AI role.

Source document:

```text
/ai-system/roles.md
```

## 3. Codex Prompt Package

A structured prompt prepared for Codex to change repository files.

Used when the Human Owner asks to create, update, review or apply repository changes.

## 4. Review Prompt

A prompt used to review Codex output.

Usually activates Code Reviewer AI, QA Engineer AI or AI System Maintainer.

## 5. Rework Prompt

A prompt used to correct issues found during review.

It must be narrower than the original task and must only address approved review findings.

## 6. Evolution Prompt

A prompt used to analyze or change the AI Development System itself.

It usually routes to AI System Maintainer and may require AICP before any repository changes.

## Prompt Lifecycle States

```text
Intent
→ Draft
→ Reviewed
→ Approved
→ Sent to Codex
→ Executed
→ Result Reviewed
→ Closed
```

Optional states:

```text
Rejected
Rework Required
Archived
Improved
```

## State Definitions

## Intent

The Human Owner describes what they want in natural language.

Example:

```text
We need to create document-lifecycle.md.
```

## Draft

ChatGPT Orchestrator creates a structured prompt.

The draft is not yet approved for Codex execution.

## Reviewed

The Human Owner or ChatGPT checks whether the prompt is safe, scoped and complete.

## Approved

The Human Owner approves the prompt for Codex.

## Sent to Codex

The approved prompt is pasted into Codex or sent through an automation.

## Executed

Codex performs repository changes and returns output.

## Result Reviewed

ChatGPT reviews the Codex result using Review Mode.

## Closed

The execution result is accepted or the task is intentionally stopped.

## Required Structure of a Codex Prompt Package

Every Codex Prompt Package should include:

```text
Mode:
Role:
Repository:
Context:
Source Documents:
Task:
Scope:
Out of Scope:
Allowed Files:
Forbidden Actions:
Acceptance Criteria:
Expected Output:
Review Instructions:
```

## Prompt Marker

Use this marker when the Human Owner wants ChatGPT to create a prompt but not execute anything directly:

```text
[PROMPT]
```

Alias:

```text
/prompt
```

Example:

```text
[PROMPT]
Create a Codex prompt to add /ai-system/document-lifecycle.md.
```

Expected behavior:

- ChatGPT creates a prompt package;
- no repository changes are made unless explicitly requested;
- the prompt should include allowed files and forbidden actions;
- the prompt waits for Human Owner approval.

## Difference Between [PROMPT] and [CODEX]

`[PROMPT]` means:

```text
Generate a prompt artifact for review.
Do not assume immediate execution.
```

`[CODEX]` means:

```text
Prepare a Codex-ready prompt package for execution.
The Human Owner may send it to Codex after review.
```

Both modes should keep Human Owner approval in the loop.

## Prompt Storage

Prompts may be stored when they are reusable, important or part of system evolution.

Recommended location:

```text
/ai-system/prompts/
```

Recommended files:

```text
/ai-system/prompts/README.md
/ai-system/prompts/codex-prompt-template.md
/ai-system/prompts/review-prompt-template.md
/ai-system/prompts/rework-prompt-template.md
/ai-system/prompts/evolution-prompt-template.md
```

Generated one-off prompts do not need to be committed unless they represent a reusable pattern.

## Automation Boundary

The system may later automate prompt execution, but only with explicit safeguards.

Safe automation sequence:

```text
Human Intent
→ ChatGPT generates prompt
→ Human approves prompt
→ Automation sends prompt to Codex
→ Codex returns result
→ ChatGPT reviews result
→ Human approves repository changes
```

Unsafe automation:

```text
ChatGPT generates prompt
→ Codex executes automatically
→ changes are accepted automatically
```

This is not allowed by default.

## Self-Feeding Automation

Self-feeding means a system generates a prompt and feeds it into Codex or another executor automatically.

This may be allowed only for low-risk operations after explicit Human Owner approval and clear constraints.

Allowed only if:

- operation scope is narrow;
- allowed files are explicit;
- forbidden actions are explicit;
- rollback is possible;
- review is mandatory;
- Human Owner approval is required before final acceptance.

Not allowed for:

- deleting roles;
- changing workflow structure;
- changing system rules;
- changing architecture;
- changing security-related behavior;
- applying major version changes;
- accepting Codex output without review.

## Prompt Improvement

If Codex repeatedly makes the same mistake, the issue may indicate a weak prompt.

Process:

```text
Review issue
→ Identify prompt weakness
→ Record improvement if recurring
→ Update prompt template if needed
→ Update system changelog if system behavior changes
```

## Main Rule

Prompts that affect repository state are controlled artifacts.

They may be generated by AI, but they should be reviewed by the Human Owner before execution and reviewed again after Codex produces a result.
