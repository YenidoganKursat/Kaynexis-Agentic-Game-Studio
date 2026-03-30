# Combat ADR

## Status
- Accepted

## Context
- The repo had Godot wiring but no actual gameplay loop.
- The first slice needed to prove combat readability, failure, and reward without overbuilding systems.
- Local validation also needed to work even when Godot is not installed on every contributor machine.

## Decision
- Build the first room as a single self-contained Godot scene in `src/main.tscn`.
- Use a simple pulse enemy instead of a full AI stack so the first slice proves timing and telegraph clarity first.
- Pair the gameplay slice with static smoke automation, pytest coverage, and export presets so the repo becomes build-aware immediately.

## Consequences
- Benefits: the repo now has a real playable loop, a deterministic export surface, and automation that does not depend entirely on chat memory
- Costs: combat depth is intentionally shallow and controller-first input polish is deferred
- Follow-up work: add a second enemy or second wave, introduce a dedicated `dash` input action, and bring runtime smoke into CI with a Godot-capable runner

## Rejected options
- Add a second feature system such as loot or save/load before the combat loop existed
- Build the first slice purely as docs without engine-native gameplay files
