# Test Plan — First Combat Room

## Scope
- The first playable room: movement, pulse timing, failure/reset, upgrade choice, and export-ready project surfaces

## Smoke tests
| Test | Steps | Expected |
|---|---|---|
| Static surface | Run `python3 scripts/godot_smoke.py --static-only` | Scene, scripts, and export presets validate cleanly |
| Automated test | Run `python3 -m pytest -q tests/test_godot_surface.py` | Test passes |
| Runtime launch | Run `python3 scripts/godot_smoke.py` on a machine with Godot 4.x | Project starts headless without runtime errors |
| Manual room clear | Open the project in Godot 4.x and clear the room | Player defeats the Pulse Warden and sees the upgrade choice |

## Risk-based cases
- Edge case: stand inside the pulse without dashing and confirm only one health loss per pulse window
- Reset case: lose all health and confirm the room resets cleanly
- Input case: confirm both arrow keys and WASD move the player
- Platform case: export with `Linux/X11` or `Windows Desktop` once a Godot binary is available

## Exit criteria
- Static smoke, pytest, and manual room clear all pass
- At least one export preset succeeds on a real machine or CI runner before external sharing
