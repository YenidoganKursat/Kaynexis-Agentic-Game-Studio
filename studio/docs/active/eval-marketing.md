# Eval Plan — Marketing Strategy Surface

## Change under test

- New marketing strategy guide, example, research note, checklist, template, and routing surface.
- Updated docs and task guidance for campaign strategy, measurement, and evaluation.

## Goal

- The agent should be able to distinguish campaign strategy from beat copy.
- The agent should name the objective, audience, channel fit, asset readiness, and measurement path before recommending a plan.
- Current market signals should be separated from evergreen marketing structure.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Build a marketing strategy for a Steam-first indie survival game" | Common strategy request | The router may fall back to launch phrasing | The marketing route surfaces the strategy guide, example, research note, and checklist |
| "Compare creator outreach versus a Steam demo beat for a small co-op game" | Channel-fit decision | The agent may answer as a release checklist | The agent names the objective, audience, assets, and metrics that decide between channels |
| "Evaluate whether our current page can support the next beat" | Readiness and evidence | The answer may ignore measurement | The answer states the baseline, proof points, and first metric |

## Rubric

- Correctness
- Evidence quality
- Channel fit
- Measurement clarity
- Instruction compliance

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, analytics, or artifacts

## Regression watchlist

- Do not collapse strategy into beat copy.
- Do not choose channels without naming the audience.
- Do not recommend metrics without a baseline.
- Do not ignore store or platform constraints.

## Exit criteria

- The guide, example, research note, checklist, and eval plan all stay synchronized.
- The router can identify marketing strategy tasks reliably.
- The checklist bundle surfaces the marketing discipline and supporting launch/community layers.
