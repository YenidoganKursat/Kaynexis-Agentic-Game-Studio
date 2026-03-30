# Eval Plan — Genre Plan Schema

## Change under test

- Added a canonical genre planning schema, example, template, and routing guidance for turning a genre preset into a buildable plan.
- Updated the genre starter and genre guidance surfaces so the plan schema appears before feature briefs.

## Atlas references

- Primary system atlas: `docs/reference/system-atlas.md`
- Core class atlas: `docs/reference/engine-atlas.md`
- Fast owner map: `docs/reference/engine-map.md`

## Goal

- The agent should ask for or surface the player outcome, dominant tension, contrast set, loop ladder, state owner, accessibility envelope, performance envelope, and validation ladder before implementation starts.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Write a genre plan schema for a tactical RPG" | Tests the new plan-centered routing and docs | The repo only surfaces the genre guide and pattern catalog | The plan guide, example, and research note are surfaced together |
| "Plan a city-builder before implementation" | Tests genre-specific planning advice | The agent may jump straight to feature brief language | The agent should name the bottleneck, contrast set, and first slice first |
| "Create a genre plan for co-op survival" | Tests whether the plan remains genre-shaped | The agent may under-specify authority and recovery | The plan should mention session authority, shared scarcity, and recovery |

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Delegation restraint
- Validation honesty
- Genre adaptation quality

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- The user-facing answer should stay simple.
- Single specialist mode should remain available.
- The plan schema should not replace the genre guide, the pattern catalog, or the example matrix.

## Exit criteria

- `codex_studio next` and `codex_studio checklist` surface the genre plan docs for plan-shaped genre tasks.
- The repo docs explain how the plan differs from the feature brief.
- The new schema is visible in the starter and prompt examples.
