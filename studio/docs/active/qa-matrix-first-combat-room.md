# QA Matrix — First Combat Room

## Test cases

| Case | Type | Expected | Notes |
|---|---|---|---|
| 1. Player can move and dash around the arena | Smoke / Regression | Pass | TBD |
| 2. Dash during the pulse defeats the Pulse Warden | Smoke / Regression | Pass | TBD |
| 3. Taking a pulse without dashing resets the player and costs health | Smoke / Regression | Pass | TBD |
| 4. Upgrade choice 1 or 2 resolves the room and updates the player stats | Smoke / Regression | Pass | TBD |

## Environment notes
- Baseline: Godot 4.x project on PC
- Static fallback: `scripts/godot_smoke.py --static-only`
- Runtime/export path: requires local Godot 4.x or `GODOT_BIN`

## Exit criteria
- All critical cases pass or accepted risks are documented
