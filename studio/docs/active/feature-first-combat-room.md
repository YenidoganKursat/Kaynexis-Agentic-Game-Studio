# Feature Brief — First Combat Room

## Player outcome
- Learn the room rhythm in seconds: move, read a telegraph, commit to a dash, then claim a reward
- Feel a clear action-roguelite promise where aggression and timing are rewarded immediately

## Scope
- Must-have: top-down movement, one pulse-based enemy, three-hit fail state, one upgrade choice after the clear
- Nice-to-have: stronger screen feedback and a second wave once the room feels stable
- Explicit non-goals: inventory, save/load, controller rebinding, metaprogression, content variety

## Acceptance criteria
- The player can move with keyboard input and dash with `ui_accept`
- The Pulse Warden telegraphs, pulses, and can be defeated only by dashing through the pulse radius
- Taking a pulse without dashing resets the player and costs health
- Clearing the room presents a one-of-two upgrade choice that changes player stats immediately

## Touched systems
- `project.godot`
- `export_presets.cfg`
- `src/main.tscn`
- `src/main.gd`
- `src/player.gd`
- `src/pulse_warden.gd`
- `scripts/godot_smoke.py`
- `scripts/godot_export.py`
- `tests/test_godot_surface.py`

## Risks & dependencies
- Risks: feedback could still feel too light; built-in `ui_accept` dash input may need a custom action later
- External dependencies: optional local Godot 4.x install or `GODOT_BIN` for runtime smoke and export
- Test focus: telegraph readability, dash timing, loss/reset flow, reward choice persistence
