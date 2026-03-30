# Custom Packs

## Date

2026-03-30

## Summary

Custom packs give the repo a reusable way to group project-specific rules, optional hooks, and fallback behavior into a named bundle that can be reviewed later.

## Primary sources

- https://martinfowler.com/articles/scaling-architecture-conversationally.html
- https://platform.openai.com/docs/guides/agents-sdk
- [Godot EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html)
- [Unity custom package layout](https://docs.unity3d.com/Manual/cus-layout.html)
- [Unreal plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)
- `docs/reference/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/architecture-guide.md`
- `studio/docs/templates/custom-packs.md`

## Why this matters to this repo

- The repo already distinguishes canonical architecture from custom rule packs and extension packs.
- Some tasks need a higher-level registry for custom feature bundles rather than a single rule override or a single plugin.
- A pack registry makes custom capability surfaces easier to route, review, and validate.
- The pack registry should stay narrower than a general extension system.

## Decision impact

- Treat a custom pack as a durable contract.
- Keep the canonical architecture, the custom rule contract, and the optional hook pack separate.
- Name the fixed rules, overrideable rules, hook points, fallback, and validation path before implementation.
- Keep the pack registry small enough to review.

## Pack shape

- pack id
- pack type
- owner
- dependencies
- fixed rules
- override rules
- hook points
- override points
- fallback
- proof path

## Repo impact

- The routing layer can surface a dedicated custom pack lane.
- The checklist layer can require pack type, owner, fallback, and proof path before implementation.
- The examples index can show how to combine rule packs and hook packs into one reviewable bundle.

## Related docs

- `docs/reference/custom-packs.md`
- `docs/examples/custom-packs-example.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `studio/docs/templates/custom-packs.md`
- `studio/checklists/discipline/custom_packs.toml`
- `studio/docs/active/custom-packs-adr.md`
