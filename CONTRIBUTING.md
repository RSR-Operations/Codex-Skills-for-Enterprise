# Contributing

Contributions should make enterprise workflows more repeatable, valuable, and trustworthy. Prefer fewer, higher-quality skills over a large catalog of shallow prompt wrappers.

## Before Creating A Skill

Use [templates/enterprise-workflow-map.md](templates/enterprise-workflow-map.md) to define the workflow, audience, inputs, outputs, quality risks, and acceptance criteria.

A good candidate skill has:

- a specific enterprise workflow;
- repeated use across teams or operating rhythms;
- clear input and output artifacts;
- quality standards that can be encoded;
- measurable productivity, speed, quality, or risk-reduction value.

## Skill Requirements

Follow [docs/skill-quality-standard.md](docs/skill-quality-standard.md). At minimum, every skill must include:

- `SKILL.md` with only `name` and `description` frontmatter;
- explicit trigger language in the description;
- concise workflow instructions;
- `agents/openai.yaml` with a default prompt that mentions `$skill-name`;
- only necessary `references/`, `scripts/`, or `assets/`.

Do not place README files, changelogs, install guides, or process notes inside skill folders.

## Review Workflow

1. Map the workflow using the enterprise workflow template.
2. Draft or update the skill.
3. Add repo-level examples in `docs/examples.md` if the use case is new.
4. Review the work with [templates/skill-review-checklist.md](templates/skill-review-checklist.md).
5. Run validation.

```bash
python3 scripts/validate_skills.py
```

6. Test at least one realistic enterprise prompt before submitting.

## Pull Request Standard

In the pull request summary, include:

- workflow improved;
- skill added or changed;
- validation command and result;
- realistic prompt used for manual testing;
- known limitations or human-review requirements.
