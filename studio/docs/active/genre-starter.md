# Genre Starter — Action Roguelite

## Selected preset

- Preset slug: `action-roguelite`
- Summary: Short runs, compounding build variety, readable combat, meaningful risk/reward, and strong reset value.

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

## Recommended first skills

- $studio-start
- $combat-loop
- $metaprogression-loop
- $qa-matrix

## Next commands

- `python3 scripts/codex_studio.py next "Implement the first combat room with one upgrade choice"`
- `python3 scripts/codex_studio.py checklist --task "Implement the first combat room with one upgrade choice"`
- `python3 scripts/scaffold_feature.py "First Combat Room" --with-adr --with-test-plan`
- `python3 scripts/generate_qa_matrix.py "First Combat Room"`
