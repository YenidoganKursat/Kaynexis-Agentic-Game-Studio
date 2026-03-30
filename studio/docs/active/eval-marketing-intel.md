# Eval Plan: Marketing Intel

## Change under test

- Add a current-status marketing intel lane with chart-pack guidance and source-backed snapshot structure.

## Goal

- Make marketing status requests return a compact set of numbers, chart families, and one implication instead of strategy-only advice.

## Risks

- The new lane could blur into the strategy guide if the source hierarchy is not explicit.
- The task router could over-match generic marketing requests if the keyword split is too loose.
- The chart pack could become too large to read quickly.

## Validation

- Route a marketing status request and confirm the marketing-intel docs appear first.
- Confirm the checklist surfaces source family, window, baseline, chart pack, and implication.
- Confirm the example shows one current-window table and one chart-pack summary.
- Confirm the research note and template stay aligned with the guide.

## Success criteria

- A user can ask for current marketing status and get a chart pack instead of a strategy memo.
- The repo keeps marketing strategy and marketing intel as separate but linked lanes.
- The validation path stays small enough to reopen later without reading the whole chat.
