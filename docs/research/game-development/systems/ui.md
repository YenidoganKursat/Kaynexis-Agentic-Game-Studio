# UI

## Date
- 2026-03-27

## Summary
- UI architecture is healthier when it separates:
  - durable screen or flow state
  - transient widget state
  - gameplay data projection
  - input and focus behavior
  - copy and accessibility concerns
  - transition or modal rules
- Godot's `Control` tree and focus system reward explicit hierarchy and pause-aware process modes. Unity's runtime UI work is cleaner when UXML, USS, `UIDocument`, and event-system assumptions are named instead of buried in scripts. Unreal's UMG and CommonUI layers work better when activatable screens, input routing, and widget ownership are defined deliberately.
- HUD and menu work becomes fragile when the HUD owns gameplay rules or when every screen reads game state directly from runtime objects without a clear presenter or projection boundary.
- Good UI flow docs should state:
  - screen list
  - entry and exit conditions
  - focus or navigation model
  - controller and mouse parity assumptions
  - blocked gameplay states
  - validation path
- Pause, upgrade, inventory, and settings screens are not interchangeable. They often need different input modes, different layering, and different persistence expectations.

## Primary sources
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Godot keyboard/controller navigation and focus](https://docs.godotengine.org/en/stable/tutorials/ui/gui_navigation.html)
- [Godot pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)
- [Godot HUD example using CanvasLayer](https://docs.godotengine.org/es/stable/getting_started/first_2d_game/06.heads_up_display.html)
- [Unity UI Toolkit manual](https://docs.unity3d.com/2023.2/Documentation/Manual/UIElements.html)
- [Unity get started with runtime UI](https://docs.unity3d.com/cn/2023.2/Manual/UIE-get-started-with-runtime-ui.html)
- [Unity runtime UI event system](https://docs.unity3d.com/ja/6000.0/Manual/UIE-Runtime-Event-System.html)
- [Unity UI Toolkit FAQ for input and event systems](https://docs.unity3d.com/ja/6000.0/Manual/UIE-faq-event-and-input-system.html)
- [Unreal UMG UI Designer Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-quick-start-guide-in-unreal-engine?application_version=5.6)
- [Input Fundamentals for CommonUI in Unreal Engine](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/input-fundamentals-for-commonui-in-unreal-engine)
- [Using CommonUI With Enhanced Input in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- Tasks mentioning HUD, menus, settings, pause, onboarding, tooltip, inventory UI, or upgrade UI should surface screen-flow architecture, not just widget cosmetics.
- Agents should explicitly say:
  - which screen or HUD state is durable
  - which data is only projected into UI
  - what input mode is active
  - what focus rules apply
  - what gameplay is paused, blocked, or still live
- This repo wants practical operator-friendly guidance. UI tasks should therefore include both authoring surface and runtime behavior, rather than pretending layout and state ownership are separate problems.

## Decision impact
- Route and checklist output should surface this note for tasks mentioning HUD, pause, menu, settings, screen flow, upgrade choice, inventory UI, controller navigation, or onboarding flow.
- Future UI and accessibility templates should require:
  - screen states
  - input/focus states
  - blocked gameplay states
  - copy and readability notes
  - validation steps for keyboard, controller, and pointer paths

## Related docs
- `docs/reference/ui-guide.md`
- `docs/examples/ui-example.md`
