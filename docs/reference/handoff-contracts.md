# Handoff Contracts

Use this page when work needs to move between people, agents, or disciplines without becoming vague.

The goal is simple: every handoff should preserve scope, evidence, risks, validation, ownership, blockers, and next step.

## Use the template

Start from:

- `studio/docs/templates/handoff-contract.md`
- `docs/examples/handoff-example.md`
- `docs/examples/traceability-example.md`
- `docs/examples/test-example.md`
- `docs/examples/eval-example.md`
- `studio/docs/templates/genre-starter.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `studio/docs/templates/lorebook-brief.md`
- `docs/reference/lorebook-methodology.md`
- `studio/docs/templates/world-graph-brief.md`
- `docs/reference/world-graph-methodology.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/agent-execution.md`
- `docs/examples/mastermind-example.md`
- `docs/examples/prompt-journal-example.md`
- `docs/examples/agent-transcript-example.md`
- `docs/examples/agent-execution-example.md`

When a new template lands, update this page too so the handoff format stays aligned with the repo's current planning surface.

## Required fields

Every handoff should include:

- scope
- evidence
- risk
- validation
- owner
- blockers
- next step
- where the execution packet lives

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

For system-heavy work, the handoff should also say:

- which system atlas entry the work maps to
- which engine class or object family owns the runtime behavior
- which shared data asset or editor surface owns the reusable state
- if the task is advanced performance work, which algorithm family or first lever the receiver should keep if the current pass still leaves a bottleneck

The default feature scaffold now writes the atlas references into new handoff docs, so keep this page synchronized with the scaffolded contract rather than treating atlas lookup as ad hoc.

The default feature scaffold also places optional test-plan and eval-plan docs beside the handoff, so the contract should describe the validation bundle as one package, not as scattered follow-up notes.

The bugfix scaffold and eval-plan scaffold now do the same for triage and validation work, so handoff guidance should stay aligned when the task is a bug, crash, or eval-plan change instead of a feature brief.

The examples index at `docs/examples/README.md` now covers the atlas-aware bugfix flow too, so handoff guidance should stay aligned with that example surface as well.

The same examples index also covers the atlas-aware feature scaffold flow, so handoff guidance should stay aligned with feature brief, test plan, and eval plan examples as a single package.

The same examples index also covers the master mind orchestration flow, so handoff guidance should stay aligned with the controller summary, handoff map, and validation path as a single package.

The same examples index also covers the agent transcript flow, so handoff guidance should stay aligned with assignment history, conversation turns, and review path as a single package.

Those example pages now use the short canonical names only, so handoff guidance should point at `feature-example.md`, `lorebook-example.md`, and `world-graph-example.md` instead of legacy golden-style filenames.

The examples index now also groups examples into structure packs, so handoff guidance should preserve that grouping when a handoff spans:

- engine and gameplay
- agent operating model
- production and market
- customability and theory

If the receiving person needs to reopen the work later, keep the pack label visible in the handoff, the execution packet, and the validation bundle so the next move is obvious.

If the handoff is architecture-heavy, include `docs/reference/architecture-guide.md` (with diagrams) and `docs/examples/architecture-example.md` in the same bundle so the owner, boundary, and proof path stay visible.

If the work needs a durable execution contract, include `docs/reference/agent-execution.md` and `docs/examples/agent-execution-example.md` so the owner, mode, proof path, custom rules, and stop conditions stay visible.

For lorebook-heavy work, the handoff should also say:

- which canon source of truth is being extended
- what unlocks a new lore entry
- which system owns persistence of unlocked lore
- whether the work changes canon or only presentation

For world graph or history-heavy work, the handoff should also say:

- which node and edge types are authoritative
- whether history is append-only or snapshot-backed
- which system owns fast reads for the common graph query

For tasks that should be easy to reopen later, the handoff should also say:

- where the prompt history entry lives
- where the agent journal note lives
- where the agent transcript entry lives
- where the execution packet lives
- what the short evaluation was
