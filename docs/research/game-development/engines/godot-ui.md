# Godot UI

## Date
- 2026-03-29

## Summary
- Godot UI is healthiest when the `Control` tree owns the screen, `CanvasLayer` owns overlay stacking, `Theme` owns shared skinning, and gameplay truth stays elsewhere.
- The most used stack in practice is `Control` + `Container` + `CanvasLayer` + `Theme`, with custom GUI controls when the built-in controls are not enough.
- Use `Control` for layout, focus, and interaction; use custom controls for reusable, authored widgets; use a `Theme` resource for shared style instead of hand-styling every node.
- This is a good engine for scene-tree-first HUDs, menus, settings pages, and compact controller-friendly flows.

## Primary sources
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Godot custom GUI controls](https://docs.godotengine.org/en/stable/tutorials/ui/custom_gui_controls.html)
- [Godot keyboard/controller navigation and focus](https://docs.godotengine.org/en/stable/tutorials/ui/gui_navigation.html)
- [Godot pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)
- [Godot theme type variations](https://docs.godotengine.org/en/stable/tutorials/ui/gui_theme_type_variations.html)

## Why this matters to this repo
- UI tasks in Godot should be written as scene ownership and projection problems, not just styling problems.
- Agents should name whether the flow is screen-space or world-space, whether pause blocks gameplay, and whether the UI only projects state.
- Godot is often the fastest path for a first playable UI slice, but it can become messy if gameplay state and layout state are mixed in the same scene.

## Decision impact
- Prefer `Control`-based scenes for UI-only work.
- Prefer `CanvasLayer` for HUD or overlay screens that should stay above the world.
- Prefer custom GUI controls for reusable widgets with explicit minimum size and theme behavior.
- Prefer `Theme` resources or type variations when a family of screens should stay visually consistent.

## Simple-to-advanced ladder
1. A basic `Control` scene with labels, buttons, and one state change.
2. A `CanvasLayer` HUD with projected gameplay data and explicit focus behavior.
3. A reusable custom control or scene template with a shared `Theme`.
4. A multi-screen menu or HUD stack with pause behavior, controller navigation, and reusable style variants.

## Ready-made template sources
- Godot UI tutorials and examples in the official docs.
- Godot custom GUI control examples.
- Godot theme and skinning docs.
- Godot Asset Library UI packs, demo projects, or control templates.
- This repo's starter kits and UI examples.

## Common mistakes
- Letting the HUD own gameplay rules.
- Mixing pause behavior and gameplay authority in the same `Control` tree.
- Styling each widget independently instead of using a shared theme.
- Forgetting that focus order and controller navigation are part of the UI contract.

## Repo impact
- UI brief, route, and checklist docs should state the template source, the durable screen owner, and the projected data owner before implementation.

