# UI Guide

## Summary
- UI work is about screen ownership, projected state, input focus, and readability, not only about layout.
- The most common stacks in this repo are:
  - Godot 4: `Control`, `Container`, `CanvasLayer`, `Theme`, and custom GUI controls for scene-tree-first HUDs and menus.
  - Unity 6: UI Toolkit (`UIDocument`, UXML, USS, UI Builder, runtime event system) for data-heavy or tool-like UI, with uGUI reserved for simpler runtime overlays or legacy paths.
  - Unreal 5: UMG / Widget Blueprints plus CommonUI and Enhanced Input for gameplay-framework-first screens and controller-heavy navigation.
- The right UI path usually depends on three things:
  - what owns the screen state
  - what owns the gameplay truth
  - where the template or starter source comes from
- This repo prefers built-in and official UI paths first, then official samples or templates, then marketplace or asset-store UI packs if the built-in path is not enough.

## Primary sources
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Godot custom GUI controls](https://docs.godotengine.org/en/stable/tutorials/ui/custom_gui_controls.html)
- [Godot keyboard/controller navigation and focus](https://docs.godotengine.org/en/stable/tutorials/ui/gui_navigation.html)
- [Godot pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)
- [Godot theme type variations](https://docs.godotengine.org/en/stable/tutorials/ui/gui_theme_type_variations.html)
- [Unity UI Toolkit manual](https://docs.unity3d.com/2023.2/Documentation/Manual/UIElements.html)
- [Unity UI Builder](https://docs.unity3d.com/ja/current/Manual/best-practice-guides/ui-toolkit-for-advanced-unity-developers/ui-builder.html)
- [Unity runtime UI event system](https://docs.unity3d.com/ja/6000.0/Manual/UIE-Runtime-Event-System.html)
- [Unity UI Toolkit FAQ for input and event systems](https://docs.unity3d.com/ja/6000.0/Manual/UIE-faq-event-and-input-system.html)
- [Unreal UMG UI Designer Quick Start Guide](https://dev.epicgames.com/documentation/de-de/unreal-engine/umg-ui-designer-quick-start-guide?application_version=4.27)
- [Input Fundamentals for CommonUI in Unreal Engine](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/input-fundamentals-for-commonui-in-unreal-engine)
- [Using CommonUI With Enhanced Input in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- UI tasks in this repo should always separate:
  - durable screen state
  - transient widget state
  - projected gameplay data
  - input and focus rules
  - accessibility and readability
  - template or starter source
- HUD, menu, pause, settings, inventory, upgrade, and onboarding work gets fragile when the UI owns gameplay authority or when the template source is not named.
- Agents should decide the smallest viable UI slice before implementation and should name the template or starter source up front.

## Decision impact
- Use this guide when a task mentions HUD, menu, settings, pause, onboarding, inventory UI, upgrade UI, controller navigation, or UI template selection.
- The agent should explicitly state:
  - screen owner
  - data projection owner
  - input/focus owner
  - template or starter source
  - validation path

## Simple-to-advanced ladder
1. Simple runtime HUD or menu with one or two states.
2. State-driven screen with projected data and explicit focus rules.
3. Controller-friendly flow with pause behavior, navigation, and accessibility constraints.
4. Template-driven reusable screen architecture with shared styles, viewmodels, or widget/presenter boundaries.

## Where ready-made templates live
- Repo starter kits and example slices first.
- Official engine docs and sample projects next.
- Official packages, plugins, and template systems next.
- Asset libraries, asset stores, or marketplaces only after the built-in and official sample paths are not enough.

## Engine-specific notes

### Godot 4
- Most used stack: `Control` tree, `CanvasLayer`, `Theme`, and custom GUI controls.
- Ready-made sources: the Godot UI tutorials, custom GUI control examples, theme skinning docs, and asset-library UI packs or demo projects.
- Best when: the screen can stay scene-tree-first and the UI needs explicit focus and pause behavior.

### Unity 6
- Most used stack: UI Toolkit, `UIDocument`, UXML, USS, and UI Builder.
- Ready-made sources: UI Toolkit samples, UI Builder templates, package samples, and Asset Store UI packs.
- Best when: the screen is data-heavy, tool-like, or wants reusable layout/style assets.

### Unreal 5
- Most used stack: UMG / Widget Blueprints, CommonUI, and Enhanced Input.
- Ready-made sources: the UMG quick start, CommonUI docs, widget blueprint templates, Fab samples, and gameplay-framework templates like Lyra-style project examples.
- Best when: controller-first navigation, larger gameplay-framework ownership, or editor-native screen assembly matters.

## Example prompts for the agent
- "Design a controller-first pause menu in Godot using Control, CanvasLayer, and a Theme source."
- "Use Unity UI Toolkit and UI Builder to build an inventory screen with UXML templates and USS styles."
- "Choose UMG, CommonUI, and Enhanced Input for an Unreal settings menu and name the widget template source."

## Validation
- List the screen states and the owner of each state.
- Confirm the gameplay truth stays outside the widget when the screen only projects data.
- Check keyboard, gamepad, and pointer paths.
- Check pause behavior, focus behavior, and blocked gameplay behavior.
- State the template or starter source explicitly.

## Related docs
- `docs/research/game-development/systems/ui.md`
- `docs/research/game-development/systems/input.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-examples.md`
- `docs/examples/ui-example.md`
