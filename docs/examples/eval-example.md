# Eval Example

## Change under test

- `scripts/scaffold_feature.py` should generate a review bundle with feature brief, handoff, traceability, test plan, and eval plan when requested.
- The generated docs should include atlas references so the agent starts from the same ownership map every time.

## Atlas references

- Primary system atlas: `docs/reference/system-atlas.md`
- Core class atlas: `docs/reference/engine-atlas.md`
- Fast owner map: `docs/reference/engine-map.md`

## Goal

- Make the scaffold output more reviewable and easier to continue without hunting for missing context.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| Scaffold a feature brief for Core Movement | Common feature path | Feature brief only, with missing validation context | Brief, handoff, traceability, test plan, and eval plan are created together |
| Scaffold a bugfix for save corruption | Common triage path | Bug and crash docs without validation bundle | Bug, crash triage, test plan, and eval plan are created together |

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Validation honesty

## Run notes

- Date / operator / model / config
- Commands used
- Links to generated docs or artifacts

## Regression watchlist

- Missing atlas refs in generated docs
- Validation docs omitted when flags are requested
- Output paths or filenames drifting from the scaffold contract

## Exit criteria

- Generated docs match the expected bundle shape
- Atlas references are present in the output package
