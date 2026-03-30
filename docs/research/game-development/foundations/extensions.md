# Extensions

## Date

2026-03-30

## Summary

Project-specific extension packs should be treated as opt-in add-ons with explicit manifests, hook points, and a clean fallback path.
If the task needs a reusable custom feature registry or broader pack bundle first, start with `docs/reference/custom-packs.md`.

## Primary sources

- `docs/reference/extensions-guide.md`
- `docs/reference/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/library-guide.md`
- `docs/reference/architecture-guide.md`
- `studio/extensions/README.md`
- `studio/extensions/custom/eval-plan.md`
- [Godot EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html)
- [Unity custom package layout](https://docs.unity3d.com/Manual/cus-layout.html)
- [Unreal plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)

## Why this matters to this repo

- Some tasks need optional capability surfaces rather than a rewrite of the canonical architecture.
- Extension packs keep those surfaces explicit, reversible, and reviewable.
- The broader custom packs registry keeps reusable bundles reviewable before they become optional add-ons.
- The repo already uses manifest-style contracts elsewhere, so the extension layer should follow the same discipline.

## Decision impact

- Keep the core behavior and the extension behavior separate.
- Name the manifest, the owner, the hook points, and the fallback.
- Validate the pack with one narrow attach/detach or enable/disable path.
- Prefer the smallest viable extension surface before adding new folders or hook layers.

## Extension pack model

- manifest
- hook points
- override points
- dependency list
- fallback behavior
- validation path

## Repo impact

- Add a dedicated extensions folder for opt-in packs and project-specific manifests.
- Keep custom architecture focused on rule contracts while extension packs handle optional capability surfaces.

## Related docs

- `docs/reference/extensions-guide.md`
- `docs/examples/extensions-example.md`
- `docs/examples/custom-packs-example.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/custom-packs.md`
- `studio/checklists/discipline/extensions.toml`
- `studio/extensions/README.md`
- `studio/extensions/custom/README.md`
- `studio/docs/active/eval-extensions.md`
