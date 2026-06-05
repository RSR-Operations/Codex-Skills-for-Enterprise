# Skill Review Checklist

Use this checklist before adding or updating a skill.

## Trigger And Scope

- [ ] Skill name is lowercase hyphen-case and under 64 characters.
- [ ] Frontmatter includes only `name` and `description`.
- [ ] Description clearly says what the skill does and when to use it.
- [ ] Scope is specific enough to trigger reliably.

## Instruction Quality

- [ ] `SKILL.md` is concise, procedural, and free of placeholder text.
- [ ] Output format is explicit.
- [ ] Missing information and uncertainty are handled honestly.
- [ ] Privacy, sensitivity, or human-review needs are addressed where relevant.

## Resources

- [ ] `references/`, `scripts/`, and `assets/` exist only if needed.
- [ ] References are one level deep and linked from `SKILL.md`.
- [ ] No README, changelog, install guide, or unrelated docs are inside the skill folder.
- [ ] `agents/openai.yaml` has clear UI metadata.

## Validation

- [ ] `python3 scripts/validate_skills.py` passes.
- [ ] At least one realistic enterprise prompt has been tested.
- [ ] Output quality was reviewed against the intended audience and workflow.
