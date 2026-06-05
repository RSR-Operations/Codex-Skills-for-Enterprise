---
name: meeting-intelligence
description: Turn raw meeting notes, transcripts, agendas, or recap drafts into executive-ready decisions, action items, risks, follow-ups, and unresolved questions. Use when Codex needs to synthesize meetings, extract accountability, prepare leadership summaries, or convert discussion into operational next steps.
---

# Meeting Intelligence

## Workflow

1. Identify meeting purpose, participants, context, and intended audience from the provided material.
2. Separate confirmed decisions from discussion, suggestions, assumptions, and unresolved questions.
3. Extract action items with owner, due date, dependency, and success signal when available.
4. Surface risks, blockers, escalations, and alignment gaps that require leadership attention.
5. Produce a concise output that can be pasted into an executive recap, project tracker, or follow-up message.

## Output Standard

Use this structure unless the user requests another format:

- **Executive Summary**: 3-5 bullets capturing the business-relevant outcome.
- **Decisions**: decision, rationale, owner, and downstream impact.
- **Action Items**: owner, task, deadline, dependency, and status.
- **Risks And Escalations**: issue, impact, urgency, and proposed next step.
- **Open Questions**: unresolved item, decision needed, and recommended owner.
- **Follow-Up Draft**: short message suitable for stakeholders.

## Rules

- Do not invent owners, dates, decisions, or commitments. Mark missing fields as `Not stated`.
- Treat ambiguous statements as discussion unless the notes clearly indicate a decision.
- Preserve sensitive details only when they are necessary for accountability or risk clarity.
- Prefer direct, neutral language over meeting-style narrative.

## References

Read `references/output-patterns.md` when the user asks for a specific recap style, board-facing summary, or action register.
