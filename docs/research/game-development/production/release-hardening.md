# Release Hardening

## Date
- 2026-03-30

## Summary
- Release hardening is the production layer that sits between "the build works" and "the build is safe to ship."
- It covers build integrity, code protection, multiplayer trust boundaries, symbol policy, and rollback evidence.
- Protection layers can raise the cost of inspection, but they do not replace server authority or proper secret handling.

## Primary sources
- [Godot Engine export and encryption docs](https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html)
- [Godot Engine script encryption key docs](https://docs.godotengine.org/ja/3.5/development/compiling/compiling_with_script_encryption_key.html)
- [Unity manual: Assembly Definition importer](https://docs.unity3d.com/es/2019.4/Manual/class-AssemblyDefinitionImporter.html)
- [Epic Developer Community: Unreal dedicated server docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/dedicated-servers-in-unreal-engine)
- [Epic Developer Community: Unreal build configurations](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)

## Why this matters to this repo
- The repo already treats CI/CD, versioning, platform fit, and incident response as durable production concerns.
- Release hardening makes the code-protection and multiplayer-trust decisions reviewable in the same place as build and rollout decisions.
- Without it, build trust, server trust, and rollback evidence drift into separate conversations.

## Decision impact
- Choose the smallest protection layer that still preserves debugging and recovery.
- Write the server/client trust boundary before the build is considered release-ready.
- Keep symbol and crash artifact policy explicit so incident response remains possible after ship.
- Use release hardening alongside build-release and release, not instead of them.

## Hardening matrix

| Concern | What to decide | Repo effect |
| --- | --- | --- |
| Build integrity | deterministic command, pinned toolchain, artifact naming | CI can reproduce the exact build that shipped |
| Code protection | stripping, encryption, obfuscation, or no extra layer | reverse engineering becomes harder without pretending to be security |
| Multiplayer trust | server authority, client prediction, validation, reconnect behavior | co-op and online state stay owned by the right side |
| Symbols | what stays in the shipping build and what goes to symbol storage | crash triage stays possible without exposing debug detail |
| Recovery | rollback owner, known-good artifact, abort condition | incidents can stop quickly instead of improvising |

## Trust boundary rules
- If a build has online or co-op features, the release hardening note must say what the client can trust.
- If the build is offline-only, the note should still say whether the protection layer is only cost-raising.
- If the build uses dedicated servers, the server package and the client package should be named separately.
- If stripping or encryption could break reflection or mod hooks, that risk must be stated before merge.

## Repo impact
- Release hardening tasks now route through a dedicated lane and checklist bundle.
- Build and release docs should point at the hardening note when code hiding or multiplayer trust changes.
- Incident response should inherit the symbol policy and rollback path from this note.

## Related docs
- `docs/reference/release-hardening-guide.md`
- `docs/examples/release-hardening-example.md`
- `docs/reference/ci-cd.md`
- `docs/research/game-development/production/README.md`
- `docs/research/game-development/production/platform.md`
- `docs/research/game-development/production/incident.md`
- `studio/checklists/discipline/release_hardening.toml`
- `studio/docs/active/eval-release-hardening.md`
- `studio/docs/templates/release-checklist.md`
- `studio/docs/templates/release-hardening.md`
