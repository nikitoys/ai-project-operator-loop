# AICP-001: Language and Localization Policy

## Status

Applied

## Problem

AI Development System responses and generated prompts may switch between English and the Human Owner's language without an explicit rule.

## Evidence

The Human Owner observed that answers and prompt artifacts periodically appear in English when Russian output is expected.

## Root Cause

The system defines interaction modes, prompt structure and decision keywords, but it does not define separate language rules for:

- internal system reasoning;
- Human Owner-facing output;
- generated Codex prompt packages;
- repository documentation;
- stable control keywords and field names.

## Proposed Change

Add a language and localization policy that separates system language from user-facing language.

The policy should define:

- English as the default system and repository documentation language;
- the Human Owner's language as the default response language;
- stable English markers and structural prompt fields;
- English or hybrid language for Codex prompt packages;
- non-translation rules for decision keywords, file paths, mode markers and task control fields.

## Affected Files

- `/ai-system/language-policy.md`
- `/ai-system/README.md`
- `/ai-system/owner-guide.md`
- `/ai-system/prompt-lifecycle.md`
- `/ai-system/rules.md`
- `/ai-system/operating-model.md`
- `/ai-system/improvement-log.md`
- `/ai-system/system-changelog.md`

## Expected Benefit

- Human-facing responses become more predictable.
- Codex prompts remain stable and less likely to lose structure through translation.
- Repository documentation keeps one source-of-truth language unless explicitly changed.
- Future prompt and role documents have a shared localization rule.

## Risks

- Hybrid prompt language may feel inconsistent if not explained.
- Adding a language policy increases system documentation surface area.
- Fully localized prompt packages may become harder for Codex to execute reliably.

## Decision

APPROVED by Human Owner.

## Version Impact

Minor
