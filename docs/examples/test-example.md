# Test Example

## Scope
- Core combat room with one dash verb, one enemy pulse, and one upgrade choice

## Smoke tests
| Test | Steps | Expected |
|---|---|---|
| Launch | Start the build and enter the room | Room opens without errors |
| Dash timing | Wait for telegraph, dash once | Player avoids the hit window |
| Upgrade flow | Clear the room and choose an upgrade | Next attempt changes visibly |

## Risk-based cases
- Edge case: pause during telegraph and resume
- Save/load case: restart the room after failure
- Input case: spam dash at the exact telegraph boundary
- Platform case: keyboard/mouse and controller both map the dash
- State ownership case: upgrade state is reset between room attempts
- Damage/contact case: contact damage only fires once per intended overlap
- AI/navigation case: enemy positioning still makes the telegraph readable

## Atlas references
- Primary system atlas: `docs/reference/system-atlas.md`
- Core class atlas: `docs/reference/engine-atlas.md`
- Fast owner map: `docs/reference/engine-map.md`

## Exit criteria
- No stale room state after retry
- Dash and upgrade behavior remain readable to a first-time tester
