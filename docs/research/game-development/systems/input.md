# Input

## Date
- 2026-03-27

## Summary
- Control architecture is healthier when it separates:
  - physical device input
  - action mapping
  - gameplay interpretation
  - UI navigation input
  - camera response and presentation
  - runtime rebinding or remapping persistence
- Godot favors named actions in the `InputMap`, input events, and explicit UI focus navigation for `Control` trees. Unity's recommended path is the Input System package with action assets, `PlayerInput`, `InputSystemUIInputModule`, and optional interactive rebinding flows. Unreal's standard complex-input path is Enhanced Input, often paired with UMG or CommonUI when UI input and gameplay input must coordinate.
- Control schemes become brittle when gameplay code reads raw device state everywhere. The system should define actions such as move, aim, interact, confirm, cancel, pause, and skill slots once, then project them into gameplay and UI separately.
- Camera behavior should be treated as its own design surface. It is downstream from movement and targeting, but it should not quietly own combat rules, input arbitration, or pause/menu state.
- Runtime rebinding and remapping should explicitly define:
  - what can be remapped
  - what stays reserved
  - how device families differ
  - where the mapping is stored
  - how UI and gameplay stay in sync after a remap

## Primary sources
- [Godot input examples](https://docs.godotengine.org/en/stable/tutorials/inputs/input_examples.html)
- [Godot controller features](https://docs.godotengine.org/en/stable/tutorials/inputs/controller_features.html)
- [Godot keyboard/controller navigation and focus](https://docs.godotengine.org/en/stable/tutorials/ui/gui_navigation.html)
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Godot pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)
- [Unity Input manual](https://docs.unity3d.com/kr/6000.0/Manual/Input.html)
- [Unity Input System package](https://docs.unity3d.com/kr/6000.0/Manual/com.unity.inputsystem.html)
- [Unity PlayerInput component](https://docs.unity3d.com/ja/Packages/com.unity.inputsystem%401.4/manual/Components.html)
- [Unity interactive rebinding and bindings](https://docs.unity3d.com/ja/Packages/com.unity.inputsystem%401.4/manual/ActionBindings.html)
- [Unity runtime UI event system](https://docs.unity3d.com/ja/6000.0/Manual/UIE-Runtime-Event-System.html)
- [Unreal systems and workflows overview for Unity developers](https://dev.epicgames.com/documentation/pl-pl/unreal-engine/unreal-engines-systems-and-workflows-overview-for-unity-developers)
- [Module 2: Create a Flashlight with Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/module-2-create-a-flashlight-with-enhanced-input)
- [Input Fundamentals for CommonUI in Unreal Engine](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/input-fundamentals-for-commonui-in-unreal-engine)
- [Using CommonUI With Enhanced Input in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.6)
- [UMG UI Designer Quick Start Guide in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-quick-start-guide-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- Tasks mentioning controls, controller support, keyboard/gamepad parity, rebinding, pause menus, HUD navigation, or camera behavior should stop treating those as small glue problems. They are system boundaries that affect gameplay, UI, accessibility, and save state together.
- Agents should explicitly say:
  - what the action map is
  - what gameplay layer consumes it
  - what UI layer consumes it
  - what camera reacts to it
  - what remap data is persisted
- This repo wants engine-aware recommendations. Input should therefore use engine-native action systems instead of direct key polling scattered across gameplay scripts or Blueprints.
- Control and remap tasks often cross into accessibility. The repo should keep those dependencies visible rather than letting a menu task quietly become a control-architecture rewrite.

## Decision impact
- Future mechanic, UI, and accessibility tasks should document:
  - action names
  - input consumers
  - UI focus/nav rules
  - remap persistence boundary
  - camera ownership
- Route and checklist output should surface this note for tasks mentioning input, controls, controller, keyboard/gamepad parity, remap, rebind, camera follow, pause, or UI navigation.
