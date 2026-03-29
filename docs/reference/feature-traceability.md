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
- `docs/examples/feature-brief-golden-example.md`
- `docs/examples/adr-golden-example.md`
- `docs/examples/qa-matrix-golden-example.md`
- `studio/docs/templates/genre-starter.md`
- `docs/research/game-development/genre/genre-advanced-development-framework.md`
- `studio/docs/templates/lorebook-brief.md`
- `docs/reference/lorebook-methodology.md`

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

For genre support work, traceability should also show:

- which genre family the change strengthens
- whether the change affects first-slice guidance or mature support guidance
- whether a preset, playbook, example matrix, or advanced framework changed

For lorebook support work, traceability should also show:

- which canon scope changed
- whether the lorebook affected gameplay unlocks or only authored prose
- which systems own the lorebook data, unlock logic, and save/load persistence

## Bad traceability

- the feature brief exists but nothing references it
- tests exist but are not tied to a feature goal
- release notes mention behavior no doc ever described
- ADRs exist without any linked feature or follow-up work
