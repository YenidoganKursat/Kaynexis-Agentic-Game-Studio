# Content Pipeline Baseline

## Date
- 2026-03-27

## Summary
- A small team or solo repo gets more value from deterministic import/naming rules than from elaborate tooling too early.
- The repo should therefore treat content handoff paths, naming rules, and import assumptions as first-class docs and checklist items before building heavier asset automation.

## Primary sources
- [Godot project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)
- [Unity custom package layout](https://docs.unity3d.com/Manual/cus-layout.html)
- [Working with Plugins in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)

## Why this matters to this repo
- Content-pipeline docs should say where authored assets begin and where runtime-ready assets live.
- Starter kits should reserve deterministic roots for content even before the first real asset lands.
- Checklist items should focus on authoring path and naming determinism.

## Decision impact
- Keep `studio/docs/active/content-pipeline.md` in the default doc set.
- Add a discipline checklist for content pipeline.
- Prefer small, explicit content rules before larger import automation.
