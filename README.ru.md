# AI Development System

Языки: [English](README.md) | [Русский](README.ru.md)

Статус: Draft
Версия: v0.3.0

Этот репозиторий содержит AI Development System: операционную модель для разработки проектов через AI-роли, документацию, lifecycle governance, генерацию промптов, выполнение задач через Codex, review и контролируемую эволюцию системы.

Это не обычный application repository. Основной источник истины находится в `/ai-system`.

## Назначение

Система помогает Human Owner работать с ChatGPT и Codex через явные роли, режимы, промпты, правила review и change governance.

Основная идея:

```text
Human Owner controls.
ChatGPT Orchestrator routes.
AI roles specialize.
Codex executes scoped repository changes.
Documentation records decisions.
```

## Текущие возможности

- Режимы взаимодействия: Free, System, Prompt, Codex, Review, Evolution и Dry Run.
- Ролевая модель для product, design, management, implementation, quality, documentation и system evolution.
- Формат Codex prompt package со scope, allowed files, forbidden actions и acceptance criteria.
- Review process с уровнями severity и decision keywords Human Owner.
- Lifecycle governance для управляемых сущностей системы.
- Language and localization policy для пользовательских ответов и generated prompts.
- Контролируемая эволюция системы через improvement log, AICP и changelog.

## Основные документы

- `/ai-system/README.md` - индекс AI Development System.
- `/ai-system/owner-guide.md` - как Human Owner взаимодействует с системой.
- `/ai-system/interaction-modes.md` - поддерживаемые режимы и routing rules.
- `/ai-system/operating-model.md` - реализованные, частичные и отсутствующие области системы.
- `/ai-system/system-structure.md` - структура ролей и слоев системы.
- `/ai-system/roles.md` - реестр AI-ролей.
- `/ai-system/rules.md` - глобальные правила системы.
- `/ai-system/prompt-lifecycle.md` - lifecycle создания, review и выполнения промптов.
- `/ai-system/task-format.md` - стандартный формат задач.
- `/ai-system/review-process.md` - процесс review и QA.
- `/ai-system/change-process.md` - процесс контролируемой эволюции.
- `/ai-system/lifecycle-governance.md` - общие lifecycle rules.
- `/ai-system/language-policy.md` - правила языка и локализации.
- `/ai-system/system-changelog.md` - история версий системы.
- `/ai-system/improvement-log.md` - замеченные process problems и improvement ideas.

## Режимы взаимодействия

Используй явные маркеры, когда нужна точность:

```text
[FREE]       ordinary explanation or discussion
[SYSTEM]     process through AI Development System
[PROMPT]     generate a prompt artifact for review
[CODEX]      prepare a Codex-ready prompt package
[REVIEW]     review Codex output
[EVOLUTION]  analyze or change the AI Development System
[DRY-RUN]    simulate without applying
```

Если маркер не указан, ChatGPT Orchestrator определяет режим по запросу.

Работа, влияющая на репозиторий, должна проходить через AI Development System process и указывать:

```text
Active Role:
Active Stage:
Active Document:
Expected Result:
```

## Language Policy

Ответы для Human Owner по умолчанию должны быть на языке Human Owner.

Системные документы и control structures по умолчанию остаются на английском:

- mode markers, например `[SYSTEM]` и `[CODEX]`;
- prompt fields, например `Scope`, `Out of Scope` и `Acceptance Criteria`;
- decision keywords, например `APPROVED`, `REWORK`, `REJECTED`, `DEFERRED` и `EXPERIMENT`;
- file paths, task IDs, branch names и command names.

Generated Codex prompts обычно должны быть English или Hybrid: стабильная английская структура с локализованными пояснениями, когда это полезно.

## Standard Workflow

```text
Human intent
-> ChatGPT Orchestrator classifies mode
-> active role and source documents are selected
-> prompt, task, review or system change is prepared
-> Human Owner approves or requests rework
-> Codex applies approved repository changes when needed
-> result is reviewed
-> changelog or documentation is updated when required
```

## Решения Human Owner

Используй эти decision words:

```text
APPROVED   accept result
REWORK     request changes
REJECTED   reject result
DEFERRED   postpone decision
EXPERIMENT test temporarily
```

AI может рекомендовать решение, но решение принимает Human Owner.

## Модель репозитория

```text
/ai-system   # AI Development System rules, roles, workflow and governance
/docs        # product documentation when a product project exists
README.md    # repository entrypoint in English
README.ru.md # Russian repository entrypoint
AGENTS.md    # instructions for future AI sessions
```

Legacy operator-loop files may exist, но `/ai-system` является текущим primary source of truth.

## Минимальные правила безопасности

- Не менять файлы репозитория, если Human Owner явно не попросил repository change или Codex execution task.
- Не рассматривать AI Development System evolution как обычный разговор.
- Не генерировать Codex prompts без mode markers и execution boundaries.
- Не принимать Codex output автоматически без review.
- Не смешивать unrelated system, product, implementation и documentation changes без явного approval.
