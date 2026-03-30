# Release Hardening Guide

## Summary
- Release hardening keeps build integrity, code protection, multiplayer trust, and rollback evidence explicit before a build ships.
- Treat stripping, encryption, and obfuscation as cost-raising layers, not as a substitute for server authority or secret hygiene.
- Use this guide when a release asks for code hiding, symbol policy, protected builds, or a dedicated server split.

## Primary sources
- [Godot Engine export and encryption docs](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)
- [Godot Engine script encryption key docs](https://docs.godotengine.org/ja/3.5/development/compiling/compiling_with_script_encryption_key.html)
- [Unity manual: Assembly Definition importer](https://docs.unity3d.com/es/2019.4/Manual/class-AssemblyDefinitionImporter.html)
- [Epic Developer Community: Unreal dedicated server docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/dedicated-servers-in-unreal-engine)
- [Epic Developer Community: Unreal build configurations](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)

## Why this matters to this repo
- The repo already treats CI, versioning, platform fit, and multiplayer as separate durable lanes.
- Release hardening keeps those lanes from drifting apart when the build needs protection, signing, or server/client splits.
- It also keeps the team honest about what code protection can and cannot claim.

## Decision impact
- Prefer the smallest protection layer that still preserves debugging and rollback.
- Keep symbol, crash, and debug artifact policy explicit rather than hidden inside the build step.
- If the game is online or co-op, define the trust boundary before code protection is finalized.

## Hardening layers
- Build integrity: deterministic command, pinned environment, artifact hash or signature policy.
- Code protection: stripping, encryption, obfuscation, or no extra protection, chosen deliberately.
- Multiplayer trust: server authority, client prediction, validation, and reconnect assumptions.
- Symbols and crash evidence: what stays with the build, what stays in a symbol store, and who can read it.
- Recovery: rollback owner, known-good artifact, and abort condition.

## Engine-specific notes

### Godot 4
- Prefer export preset hardening and, when needed, PCK encryption or script encryption as a cost-raising layer.
- Keep the encryption key and any protected export template contract in the repo docs, not in chat.
- Do not treat export encryption as a security boundary; server authority still matters for multiplayer.

### Unity 6
- Use managed code stripping consciously and record any `link.xml` or `[Preserve]` exceptions.
- If multiplayer trust matters, keep authoritative server state out of client-only code paths.
- Separate release symbols from the shipping artifact so crash triage remains possible after publish.

### Unreal 5
- Prefer Shipping configuration for real release builds and keep separate client/server targets when multiplayer trust needs it.
- Keep symbols and debug artifacts in a separate lane from the shipping build.
- If dedicated servers are part of the release, document the server package and the trust boundary together.

## Multiplayer trust
- Name the authoritative side before the release hardening pass begins.
- State what the client may predict and what the server must validate.
- If the game is co-op or online, describe the dedicated server split or the exact fallback trust model.
- Keep desync and reconnect checks in the same review bundle as the build-hardening decision.

## Example prompts for the agent
- "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split."
- "Review whether our Godot export should use PCK encryption and what rollback evidence must remain visible."
- "Set up an Unreal 5 shipping build with separate client/server targets and a clear trust boundary."

## Validation
- Name the build-integrity plan, code-protection choice, and trust boundary before implementation.
- Keep one smoke path for packaging or launch.
- Keep rollback ownership and symbol policy explicit.
- Sync the guide with the example, research note, checklist, and eval plan.

## Related docs
- `docs/examples/release-hardening-example.md`
- `docs/research/game-development/production/release-hardening.md`
- `docs/reference/ci-cd.md`
- `docs/reference/platform-guide.md`
- `docs/research/game-development/production/platform.md`
- `docs/research/game-development/production/incident.md`
- `studio/docs/templates/release-checklist.md`
- `studio/docs/templates/release-hardening.md`
- `studio/checklists/discipline/release_hardening.toml`
- `studio/docs/active/eval-release-hardening.md`
