# Godot

## Date
- 2026-03-27

## Summary
- Godot’s own docs emphasize flexible filesystem organization, scene-centric composition, and a tree structure where a stable main scene can wire smaller reusable scenes together.
- The practical repo implication is to keep the bootstrap scene explicit, keep script ownership local to the node tree that owns behavior, and avoid spreading state through hidden global couplings too early.

## Primary sources
- [Godot project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)
- [Godot scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html)

## Why this matters to this repo
- The Godot starter kit should keep `project.godot` and a deterministic main scene path.
- Godot validation should focus on scene/script/export integrity before advanced engine automation.
- Checklist rules should push reusable scene boundaries and readable signal ownership.

## Decision impact
- Keep the root Godot slice and starter kit centered on `src/main.tscn`.
- Require static smoke coverage for scene nodes, scripts, and export presets.
- Use Godot checklist items to guard scene ownership, smoke coverage, and runtime smoke when a binary exists.
