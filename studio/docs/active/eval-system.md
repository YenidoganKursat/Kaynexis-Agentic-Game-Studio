# System Eval

## Change under test

- `scripts/studio_core.py` now includes the engine quick map, engine class atlas, and game systems atlas in the default research refs surfaced by `route_task.py`.
- The feature brief and handoff templates now ask for system atlas references.
- The feature traceability and handoff contracts now describe system-heavy ownership more explicitly.

## Goal

- Make the agent land on the right reference docs faster.
- Keep system-heavy requests tied to the engine class atlas and the game systems atlas.
- Reduce vague handoffs and briefs that omit ownership surfaces.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Design a combat slice with damage, loot, and UI feedback" | Common gameplay path | Routes to gameplay docs only | Includes engine quick map, engine class atlas, and game systems atlas in research refs |
| "Write a handoff for inventory UI and save migration" | Checks template guidance | Handoff text may skip atlas references | Handoff explicitly names the relevant system atlas and ownership surface |
| "Create a feature brief for dialogue and quest flow" | Tests planning surface | Brief may stay vague on ownership | Brief includes system atlas lookup and engine mini atlas guidance |
| "Update routing for a world graph feature" | Shared-script change with narrative scope | Could miss atlas references in eval reasoning | Eval notes describe the atlas references used to validate the change |

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

- Routing should not become noisy or overbroad.
- Existing route_task cases should still pass.
- Handoff and feature templates should remain concise.

## Exit criteria

- `route_task.py` surfaces the atlas refs on the representative prompts.
- Feature brief and handoff docs mention atlas references without adding clutter.
- Repo validation and local evals stay green.
