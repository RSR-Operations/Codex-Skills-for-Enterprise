# Skill Quality Standard

This repository uses a strict v1 quality bar. A skill should encode a valuable enterprise workflow that Codex can execute more consistently with the skill than without it.

## Required Structure

Each skill folder must contain:

- `SKILL.md`
- `agents/openai.yaml`
- optional `references/`, `scripts/`, or `assets/` only when they directly support the skill

Do not add `README.md`, changelogs, install guides, or process notes inside a skill folder. Put repo-level documentation in `docs/` or `templates/`.

## Frontmatter

`SKILL.md` must include only:

```yaml
---
name: lowercase-hyphen-name
description: Clear explanation of what the skill does and when Codex should use it.
---
```

The description is the trigger surface. It must include concrete contexts such as artifact types, business workflows, or user intents.

## Instruction Quality

Good skill instructions are:

- concise enough to load quickly;
- procedural enough to guide repeatable execution;
- specific about outputs and quality rules;
- honest about uncertainty, missing data, privacy, and human review;
- supported by references only when extra detail is useful.

Avoid generic productivity advice, broad AI strategy language, or content Codex already knows.

## Progressive Disclosure

Use `references/` when a workflow has variants, rubrics, templates, or examples that are not always needed. Keep references one level deep and link them directly from `SKILL.md`.

Use `scripts/` only for deterministic work that would otherwise be rewritten repeatedly.

Use `assets/` only for templates, icons, example files, or resources used in outputs.

## Enterprise Readiness

Every skill should support:

- measurable workflow value;
- clear business audience;
- privacy-aware handling of sensitive details;
- actionable outputs with owners, dates, risks, and next steps when applicable;
- validation through realistic enterprise prompts.
