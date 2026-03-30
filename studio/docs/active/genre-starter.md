# Genre Starter — Action Roguelite

## Selected preset

- Preset slug: `action-roguelite`
- Summary: Short runs, compounding build variety, readable combat, meaningful risk/reward, and strong reset value.

## How this starter is used

- This file is the active, generated starter for the currently selected genre.
- It should mirror the public preset catalog and the matching architecture note instead of acting like a standalone one-off brief.
- When a new genre family is added, update the preset, the example matrix, and the research note together so the starter stays trustworthy.
- Treat the preset catalog as expandable, not fixed; the current support set now also includes auto-battler, grand-strategy, stealth, city-builder, life-sim, hero-shooter, and soulslike families.
- Use `docs/research/game-development/genre/genre-guide.md` when you want to know how to turn the preset into a real first slice instead of just a label.

## Default assumptions

- 20–45 minute runs
- High encounter readability
- Meta progression without invalidating mastery

## Must-watch risks

- Run variety collapse
- Snowball balance
- Too much permanent power
- Content fatigue

## Suggested first slice

- One combat room with one dodge or signature ability
- Two enemy roles with readable telegraphs
- One upgrade choice between encounters

## Reference games

- `Dead Cells` -> study repeat-run mastery, failure cadence, and readable combat pressure
- `Risk of Rain 2` -> study scaling chaos, item-build variance, and escalation pacing

## Design focus

- Dominant loop: survive encounter -> choose build growth -> repeat
- Architecture watch: separate run state from meta progression early
- First risk: variety collapse or permanent power trivializing mastery

## Planning schema

- Use `docs/reference/genre-plan.md` to turn this preset into a buildable plan before the first feature brief.
- Player outcome: survive a short run and feel mastery through readable combat.
- Dominant tension: survive now versus build for later.
- Contrast set: `Dead Cells`, `Risk of Rain 2`.
- Loop ladder: encounter -> reward -> upgrade -> reset.
- State owner: run state in the combat loop; meta progression elsewhere.
- Accessibility envelope: clear telegraphs, readable damage, controller-safe dodge timing.
- Validation ladder: one room should tell the player why they won or lost.

## Advanced genre guidance

- Deeper theory and maturity path: `docs/research/game-development/genre/genre-maturity.md`
- The short maturity filename is the canonical one; the older verbose framework name is retired, so keep this starter, the preset catalog, and the example matrix on the short name.
- Use this once the first combat room is stable and you want to scale the action-roguelite support model into something a larger project can trust.

## Recommended first skills

- $studio-start
- $combat-loop
- $metaprogression-loop
- $qa-matrix

## Next commands

- `python3 scripts/codex_studio.py next "Implement the first combat room with one upgrade choice"`
- `python3 scripts/codex_studio.py checklist --task "Implement the first combat room with one upgrade choice"`
- `python3 scripts/scaffold_feature.py "First Combat Room" --with-adr --with-test-plan --with-eval-plan`
- `python3 scripts/generate_qa_matrix.py "First Combat Room"`
