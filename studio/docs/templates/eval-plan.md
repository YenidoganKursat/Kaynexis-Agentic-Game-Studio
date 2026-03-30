# Eval Plan — {EVAL_NAME}

## Change under test

- What changed
- Which files, agents, prompts, or scripts are affected

## Atlas references

- Primary system atlas: `{SYSTEM_ATLAS_REF}`
- Core class atlas: `{ENGINE_ATLAS_REF}`
- Fast owner map: `{ENGINE_MAP_REF}`

## Goal

- What better behavior should look like

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| Example task | Common path | Capture the current behavior before changing routing or validation | Show the improved behavior with the same command and a clearer output shape |

Add at least one scenario that matches the exact feature, instruction, or routing change you are making.

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Delegation restraint
- Validation honesty

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- What must not get worse

## Exit criteria

- What must pass before merge or adoption
