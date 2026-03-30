# Prompt Journal

## Date
- 2026-03-29

## Summary
- Append-only prompt history and agent journal entries keep broad tasks reviewable after chat moves on.
- The journal records what the user asked, what the agent expected, what it found, what improved, and the short evaluation.

## Primary sources
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/quality-process.md`
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html)

## Why this matters to this repo
- Broad repo changes are easier to trust when the user can reopen a dated trail later.
- Short step notes make it easier to understand why a route, checklist, or validation path changed.
- Prompt history and agent journal entries give the repo one durable review trail instead of many scattered comments.

## Decision impact
- Keep the journal append-only.
- Keep user prompts and agent step notes in the same active file but in separate sections.
- Keep entries timestamped, short, and linked to the docs or validation used.

## Repo impact
- Add a prompt-journal guide and example.
- Add an active prompt journal file.
- Add a journal command for prompt history and step notes.
- Keep routing, checklist, and validation behavior aligned with the journal trail when those systems change.
