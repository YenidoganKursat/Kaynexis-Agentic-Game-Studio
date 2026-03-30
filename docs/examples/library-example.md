# Library Example

## Scope

- Unity 6 inventory HUD with controller remap
- Godot 4 stealth slice with navigation and save
- Unreal 5 co-op combat slice with input, UI, and VFX

## Baseline

| Case | Current pain | Minimal official stack |
| --- | --- | --- |
| Unity 6 inventory HUD | Legacy input polling and too much UI rebuild work | Input System package, UI Toolkit or uGUI/TMP, Cinemachine if camera framing is part of the same slice |
| Godot 4 stealth slice | Custom input plumbing and ad hoc path code | `InputMap`, `Control` / `CanvasLayer`, `NavigationServer2D/3D` or `AStarGrid2D/3D`, `ConfigFile` or `Resource` for persistence |
| Unreal 5 co-op combat | Controller remap, HUD state, and VFX ownership are unclear | Enhanced Input, UMG, CommonUI when the menu flow is controller-first, Niagara for effects |

## Decision order

- Start with the case, not the package name.
- Ask whether the built-in engine API already covers the need.
- If not, use the smallest official package or plugin that covers the gap.
- Only then consider a third-party dependency.
- Keep the validation path tied to the same slice.

## Likely library choices by case

- Input: Godot `InputMap`, Unity Input System package, Unreal Enhanced Input
- UI: Godot `Control` / `CanvasLayer`, Unity UI Toolkit or uGUI/TMP, Unreal UMG and optionally CommonUI
- Navigation: Godot `NavigationServer`, Unity AI Navigation, Unreal Navigation System and EQS or StateTree if needed
- Save: Godot `ConfigFile` / `Resource`, Unity serialization helpers, Unreal `SaveGame`
- Networking: Godot `MultiplayerAPI`, Unity Netcode for GameObjects, Unreal replication and OnlineSubsystem
- VFX: Godot particles, Unity Particle System or VFX Graph, Unreal Niagara

## Smallest high-impact fixes

- stop adding libraries until the built-in option is disproven
- keep one owner for input, UI, save, and navigation
- do not add DOTS, Mass, or GAS unless scale or authority clearly demands it
- document the fallback if a package proves unnecessary

## Good agent prompts

- "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow."
- "For a Godot 4 stealth prototype, tell me whether the built-in APIs already cover input, navigation, and save."
- "For an Unreal 5 co-op combat slice, name the minimum official stack for input, UI, networking, and effects."
- "For a city-builder, recommend the smallest navigation and UI package set before any third-party dependency."

## Validation

- re-run the same gameplay slice or editor workflow with the chosen stack
- confirm the built-in option was either enough or intentionally rejected
- verify the dependency list is still the smallest thing that solves the case
- record the ownership boundary in the durable docs if the choice sticks
