# Extensions Guide

Use this guide when the task needs opt-in custom modules, plugin-like add-ons, or hook packs that sit beside the canonical architecture families.
If the task is really about a reusable custom feature registry or broader pack bundle, start with `docs/reference/custom-packs.md` first.

## Summary

Extensions are for optional capability surfaces that should be enabled deliberately, validated separately, and documented with a small manifest.

Use them when the repo needs:

- a feature hook that should not live in the core architecture family
- a project-specific add-on with a clear enable or disable point
- a pack that combines editor hooks, UI hooks, data hooks, or tool hooks
- a reusable optional module that should stay reviewable instead of becoming chat-only tribal knowledge

## Primary sources

- `docs/reference/custom-architecture.md`
- `docs/reference/custom-packs.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/library-guide.md`
- `docs/research/game-development/foundations/extensions.md`
- [Godot EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html)
- [Unity custom package layout](https://docs.unity3d.com/Manual/cus-layout.html)
- [Unreal plugins](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)

## Why this matters to this repo

- The repo already has canonical architecture, custom request contracts, and engine starter kits.
- The repo also has a broader registry layer for reusable custom feature bundles.
- Some changes are not rule overrides; they are opt-in feature packs or tooling add-ons.
- A dedicated extensions lane keeps those packs explicit, reviewable, and easy to disable if they drift.

## Decision impact

- Keep the canonical architecture, the custom request contract, and the extension pack separate.
- Treat the extension pack as a manifest-driven add-on with explicit hook points.
- Name the fallback when the extension is disabled or not present.
- Do not let an extension silently replace the core rule set.

## Extension pack model

- `manifest` records the pack id, owner, scope, dependencies, hook points, and fallback.
- `hook points` name where the pack attaches: runtime, editor, data, UI, telemetry, or release.
- `override points` name what the pack may replace or augment.
- `pack layers` stay explicit: canonical core, shared extension, project-specific override.

## Pack layout

- `studio/extensions/README.md`
- `studio/extensions/custom/README.md`
- `studio/extensions/custom/manifest.example.toml`

## Example prompts for the agent

- "Design an extension pack for inventory filter hooks and editor panels."
- "Define a plugin-like add-on that exposes a debug overlay without changing the canonical combat state."
- "Build an extension manifest for a UI hook pack that can be disabled cleanly if it misbehaves."

## Validation

- Name the pack owner and the fallback before implementation.
- Write down the manifest fields and the hook points.
- Run one narrow smoke, test, or review pass that proves the pack attaches and detaches cleanly.

## Related docs

- `docs/examples/extensions-example.md`
- `docs/examples/custom-packs-example.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/custom-packs.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/library-guide.md`
- `docs/research/game-development/foundations/extensions.md`
- `studio/extensions/custom/eval-plan.md`
- `studio/checklists/discipline/extensions.toml`
- `studio/extensions/README.md`
- `studio/extensions/custom/README.md`
- `studio/docs/active/eval-extensions.md`
