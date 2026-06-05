# Light Adapter Patterns

Adapters should make skills easier to use with real artifacts while keeping the core skills tool-agnostic.

## Principles

- Keep `SKILL.md` independent of specific vendors.
- Prefer exported artifacts, logs, CSVs, diffs, and markdown over direct tool coupling at first.
- Add scripts only when they perform deterministic extraction, filtering, or validation.
- Keep credentials, tokens, customer data, and private system details out of the repo.

## Engineering Ops

Useful adapter inputs:

- CI log excerpts;
- failed job summaries;
- PR descriptions and changed-file lists;
- commit ranges and ticket summaries.

Possible future scripts:

- extract the first meaningful CI failure from a long log;
- summarize changed files by extension and directory;
- normalize commit messages into release-note buckets.

## Revenue Ops

Useful adapter inputs:

- CRM CSV exports;
- opportunity notes;
- account research excerpts;
- discovery notes and proposal constraints.

Possible future scripts:

- detect missing required CRM fields in a CSV;
- flag stale next steps by date;
- normalize account research sources into evidence labels.

## Knowledge Ops

Useful adapter inputs:

- document exports;
- meeting notes;
- support threads;
- policy text;
- source excerpts with dates and authors.

Possible future scripts:

- split source bundles into cited excerpts;
- check KB article metadata completeness;
- detect stale review dates.

## Adapter Readiness Checklist

- Artifact input is clear and repeatable.
- Script output can be reviewed by a human.
- Failure modes are explicit.
- Sensitive data handling is documented.
- Core skill remains useful without the adapter.
