# Current Sprint — kaynexisGame

## Sprint goal
- Prove the first playable slice around `First Combat Room`

## In scope
- Confirm engine and repo layout decisions
- Build the first core gameplay slice
- Establish one repeatable validation path
- Land export and smoke surfaces for the Godot baseline
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Local or CI Godot runtime is not installed yet | Owner: technical_director | Mitigation: install Godot 4.x or set `GODOT_BIN` so runtime smoke and exports can run
- GitHub remote and rulesets are not configured yet | Owner: producer | Mitigation: create remote and apply maintainer setup doc

## Definition of done
- Implementation done for the first slice with one readable pulse enemy and one upgrade choice
- Validation done locally and documented through `scripts/godot_smoke.py`, `pytest`, and manual smoke notes
- Docs updated to reflect real project state instead of template assumptions
