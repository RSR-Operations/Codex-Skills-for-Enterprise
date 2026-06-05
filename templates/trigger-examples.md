# Trigger Examples

Use these examples when designing skill descriptions and testing invocation.

## Strong Trigger Language

```yaml
description: Turn raw meeting notes, transcripts, agendas, or recap drafts into executive-ready decisions, action items, risks, follow-ups, and unresolved questions. Use when Codex needs to synthesize meetings, extract accountability, prepare leadership summaries, or convert discussion into operational next steps.
```

Why it works:

- names the artifacts;
- names the business workflow;
- names the expected output;
- includes explicit "Use when" contexts.

## Weak Trigger Language

```yaml
description: Helps with meetings and productivity.
```

Why it fails:

- too broad;
- no artifact type;
- no output expectation;
- no reliable usage context.

## Prompt Examples

```text
Use $meeting-intelligence to extract decisions, owners, and follow-ups from these notes.
```

```text
Use $decision-memo to compare these options and recommend a path for executive approval.
```

```text
Use $automation-opportunity-map to identify repeatable steps and rank automation candidates.
```
