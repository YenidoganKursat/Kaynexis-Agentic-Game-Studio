# Handoff Contracts

Use this page when work needs to move between people, agents, or disciplines without becoming vague.

The goal is simple: every handoff should preserve scope, evidence, risks, validation, ownership, blockers, and next step.

## Use the template

Start from:

- `studio/docs/templates/handoff-contract.md`
- `docs/examples/handoff-contract-golden-example.md`
- `studio/docs/templates/genre-starter.md`
- `docs/research/game-development/genre/genre-advanced-development-framework.md`
- `studio/docs/templates/lorebook-brief.md`
- `docs/reference/lorebook-methodology.md`

## Required fields

Every handoff should include:

- scope
- evidence
- risk
- validation
- owner
- blockers
- next step

## Good handoff behavior

- name the exact feature or slice, not a vague area
- link the docs or code paths already touched
- state what is already proven and what is still assumed
- make blockers explicit instead of hiding them in prose
- say what the receiver should do next, not just what happened so far

## Bad handoff behavior

- "combat mostly done"
- "UI needs polish"
- "someone should test this"
- "it should work now"

## Minimum contract

If time is tight, one good paragraph per field beats a long fuzzy summary.

The receiving person should be able to answer:

- what is the task
- what is already true
- what is risky
- what should be validated next
- who owns the next move

For genre-heavy work, the handoff should also say:

- which genre family is being supported
- which loop or system is being matured
- what the first failure mode is likely to be
- whether the task is still first-slice work or already moving into maturity work

For lorebook-heavy work, the handoff should also say:

- which canon source of truth is being extended
- what unlocks a new lore entry
- which system owns persistence of unlocked lore
- whether the work changes canon or only presentation
