# Language and Localization Policy

Status: Draft  
Version: v0.1.0

## Purpose

This document defines how language and localization work inside the AI Development System.

The goal is to make Human Owner-facing output predictable while keeping system control structures stable for AI roles and Codex execution.

## Core Principle

Separate language into layers:

- system language;
- Human Owner-facing language;
- generated prompt package language;
- repository documentation language;
- fixed control terms.

User-facing text may be localized. Control structures must remain stable.

## Default Language Model

```text
System Language: English
Repository Documentation Language: English
Human Owner Language: inferred from the Human Owner's latest message
Chat Response Language: Human Owner Language
Prompt Package Language: English or Hybrid
Decision Keywords: English fixed
Mode Markers: English fixed
```

The Human Owner may override the output language explicitly.

## System Language

English is the default language for:

- system documents in `/ai-system`;
- source-of-truth section names and field names;
- role names;
- lifecycle state names;
- prompt package structure;
- Codex execution controls.

This keeps the AI Development System consistent across roles, prompts and repository history.

## Human Owner-Facing Language

ChatGPT Orchestrator should answer the Human Owner in the Human Owner's language by default.

If the Human Owner writes in Russian, the answer should be in Russian unless the Human Owner asks otherwise.

If the Human Owner switches language, the answer may follow the latest clear language signal.

## Generated Prompt Package Language

Generated prompt packages should preserve stable English structure.

The following elements should remain in English:

- mode markers such as `[SYSTEM]`, `[CODEX]`, `[REVIEW]`, `[EVOLUTION]`, `[DRY-RUN]`;
- header fields such as `Active Role`, `Active Stage`, `Active Document`, `Expected Result`;
- required prompt fields such as `Repository`, `Source Documents`, `Task`, `Scope`, `Out of Scope`, `Allowed Files`, `Forbidden Actions`, `Acceptance Criteria`, `Expected Output`, `Review Instructions`;
- decision keywords such as `APPROVED`, `REWORK`, `REJECTED`, `DEFERRED`, `EXPERIMENT`;
- file paths, branch names, task IDs and command names.

Explanatory text inside prompt packages may be written in:

- English, when the prompt is intended mainly for Codex execution;
- the Human Owner's language, when the prompt is intended for Human Owner review;
- hybrid format, when both review clarity and Codex stability matter.

## Repository Documentation Language

Repository source-of-truth documents in `/ai-system` should remain in English by default.

Changing the documentation language is a system change and requires Human Owner approval.

Project documents in `/docs` may define their own language policy if needed.

## Fixed Terms

Do not translate control terms when they are used as system commands, state names, field names or decision words.

Examples:

- `APPROVED`;
- `REWORK`;
- `Scope`;
- `Out of Scope`;
- `Acceptance Criteria`;
- `Forbidden Actions`;
- `[CODEX]`.

These terms may be explained in the Human Owner's language, but the control term itself should remain stable.

## Override Rules

The Human Owner may explicitly request:

- a specific answer language;
- a fully English prompt package;
- a hybrid prompt package;
- a localized explanation of an English prompt package.

Explicit Human Owner language instructions override default inference for that response or artifact.

## Boundary Rules

Localization must not change scope, acceptance criteria, forbidden actions, approval status or repository paths.

Translation must not rename system files, task IDs, mode markers, decision keywords or role names unless an approved system change explicitly requires it.

When translation may reduce execution clarity, prefer stable English structure with localized explanations.
