# UI Example

## Summary
- This example shows the level of specificity expected for UI tasks in this repo.
- The goal is to name the screen owner, the projection boundary, the input model, and the template source before implementation starts.

## Example prompts
- "Design a Godot pause menu using Control, CanvasLayer, and a reusable Theme source."
- "Compare Unity UI Toolkit and uGUI for an inventory screen and say which template source should be used first."
- "Plan an Unreal settings menu with UMG, CommonUI, and Enhanced Input, and keep the widget from owning gameplay truth."

## Common decision set
- Godot: scene-tree-first `Control` flow with `CanvasLayer` for overlay and `Theme` for shared style.
- Unity: UI Toolkit for data-heavy or reusable screens, uGUI for quick overlays or legacy paths.
- Unreal: UMG / Widget Blueprints plus CommonUI for controller-first screen flow.

## Template sources
- Repo starter kits and current examples.
- Official engine tutorials and sample projects.
- Official package templates and samples.
- Asset libraries, stores, or marketplaces only after the built-in path is exhausted.

## Validation
- State which screen is durable and which data is only projected.
- Name the keyboard, gamepad, and pointer behavior.
- Name the template source before writing the screen.
- Confirm the screen does not own combat, save, or other gameplay authority.

## Related docs
- `docs/reference/ui-guide.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-examples.md`
- `docs/reference/task-prompt-examples.md`
