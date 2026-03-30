# Release Hardening Example

## Scope
- A Unity 6 co-op demo is about to ship, and the team wants code protection, symbol policy, and a dedicated server split to stay reviewable.

## Baseline
- The current build path is reproducible.
- Multiplayer authority is not yet written down.
- Symbols are still bundled with the shipping artifact, which makes incident response easier now but riskier after launch.

## Decision order
1. Keep the build command deterministic.
2. Choose the smallest code-protection layer that still makes reverse engineering harder.
3. Write the multiplayer trust boundary before shipping.
4. Keep rollback and symbol policy explicit.

## Example hardening matrix

| Layer | Example choice | Why it matters |
| --- | --- | --- |
| Build integrity | Pinned CI command and deterministic output name | Makes release evidence and rollback easy to verify |
| Code protection | Unity managed stripping with explicit `link.xml` exceptions | Reduces dead code without breaking reflective systems |
| Multiplayer trust | Dedicated server with server-authoritative economy and inventory writes | Keeps client cheats from owning important state |
| Symbols | Separate symbol archive and crash dump path | Preserves triage without shipping debug detail to players |

## Good agent prompts
- "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split."
- "Review whether this Godot export should use PCK encryption and what rollback evidence should stay visible."
- "Set up an Unreal 5 shipping build with separate client and server targets and a clear trust boundary."

## Validation
- One build command is documented.
- One trust boundary is documented.
- One rollback owner is named.
- One smoke path proves the bundle still launches or connects.

## Related docs
- `docs/reference/release-hardening-guide.md`
- `docs/research/game-development/production/release-hardening.md`
- `docs/reference/ci-cd.md`
- `docs/reference/platform-guide.md`
- `docs/research/game-development/production/incident.md`
- `studio/docs/templates/release-hardening.md`
