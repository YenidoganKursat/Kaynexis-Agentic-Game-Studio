# Feature Traceability

Use this page when a feature needs to stay linked across planning, implementation, testing, and release.

The minimum chain is:

1. feature brief
2. architecture decision if the change is structural
3. touched code or content paths
4. test plan or QA matrix
5. release note or release gate evidence

## Use the template

Start from:

- `studio/docs/templates/feature-traceability.md`
- `docs/examples/feature-example.md`
- `docs/examples/traceability-example.md`
- `docs/examples/adr-example.md`
- `docs/examples/qa-example.md`
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

If you introduce a new template or a new narrative support surface, add it to this chain so the trace from brief to build to QA stays obvious.

## Why this matters

Without traceability, teams forget:

- why the feature exists
- which tradeoff was accepted
- what was supposed to be tested
- what should be mentioned at release time

## Good traceability

- one stable feature name or slug
- explicit links between docs
- concrete code/content paths instead of "misc gameplay changes"
- clear release impact
- if the work affects shipping identity, the target version or tag family should be visible in the same chain
- if the work should be reopened later, the prompt history, execution packet, agent journal entry, and agent transcript should point at the same review path

For genre support work, traceability should also show:

- which genre family the change strengthens
- whether the change affects first-slice guidance or mature support guidance
- whether a preset, playbook, example matrix, or advanced framework changed
- which software pattern the genre change is trying to own
- which example games proved that the pattern is real

For system support work, traceability should also show:

- which system atlas entry was consulted
- which engine class or object family example informed the change
- whether the work changes runtime ownership, shared data ownership, or editor ownership
- if the work is an advanced optimization pass, which algorithm family was chosen and which advanced perf note or example justified it

For quality-control work, traceability should also show:

- which quality-control process step was used
- which evidence artifact proves the decision
- which go/no-go gate was applied

The default feature scaffold now includes these atlas references in generated traceability docs, so keep this page aligned with the scaffold output instead of treating atlas lookup as optional extra context.

The default feature scaffold also writes optional test-plan and eval-plan docs into the same package, so feature traceability should treat validation docs as part of the same chain rather than separate afterthoughts.

The bugfix scaffold and eval-plan scaffold now use the same atlas references, so traceability should also stay aligned when the work is about crashes, triage, or validation behavior rather than a new feature slice.

The examples index at `docs/examples/README.md` now points readers at the atlas-aware bugfix and eval scaffold flow as well, so traceability should keep that example page synchronized too.

The examples index also points readers at the atlas-aware feature scaffold flow, so feature traceability should treat the brief, handoff, test plan, and eval plan as one package when examples are updated.

The examples index also points readers at the master mind orchestration flow, so traceability should keep the controller summary, handoffs, and validation path aligned with the example bundle.

The examples index also points readers at the prompt journal flow, so traceability should keep the later-review trail aligned with the same bundle when the work needs to be reopened later.

The same examples index also points readers at the agent transcript flow, so traceability should keep task assignments and conversation turns aligned with the same bundle when the work needs to be reopened later.

The same examples index also points readers at the execution packet flow, so traceability should keep the owner, mode, proof path, and custom rules aligned with the same bundle when the work needs to be reopened later.

Those example references now use the short canonical names only, so traceability should point at `feature-example.md`, `lorebook-example.md`, and `world-graph-example.md` instead of legacy golden-style filenames.

The examples index now also groups examples into structure packs, so traceability should preserve that grouping when work spans:

- engine and gameplay
- agent operating model
- production and market
- customability and theory

If a trace path crosses one of those packs, keep the pack label visible in the feature brief, handoff, test plan, and eval plan so the reopen path stays obvious.

If the feature is architecture-heavy, include `docs/reference/architecture-guide.md` (with diagrams) and `docs/examples/architecture-example.md` in the same chain so the owner, boundary, and proof path stay visible.

For lorebook support work, traceability should also show:

- which canon scope changed
- whether the lorebook affected gameplay unlocks or only authored prose
- which systems own the lorebook data, unlock logic, and save/load persistence

For world graph or history work, traceability should also show:

- which node and edge types were added or changed
- whether the history model is append-only or snapshot-backed
- which system owns canonical relationship truth and which systems only render it

## Bad traceability

- the feature brief exists but nothing references it
- tests exist but are not tied to a feature goal
- release notes mention behavior no doc ever described
- ADRs exist without any linked feature or follow-up work
