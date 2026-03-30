# Inventory

## Date
- 2026-03-27

## Summary
- Inventory systems stay manageable when they separate four layers that often get collapsed into one:
  - immutable item definition data
  - runtime inventory state such as counts, durability, roll values, or ownership
  - equipment or loadout state that changes gameplay rules
  - UI projection of those states for grids, lists, quick bars, and drag-and-drop
- Godot, Unity, and Unreal all encourage a split between authored data and live mutable state, even though they expose different authoring surfaces. Godot favors `Resource` for reusable data and `Control`-based UI trees for projection. Unity favors `ScriptableObject` for authored definitions and serialized runtime wrappers or plain C# state for mutable inventory contents. Unreal favors Data Assets or `UPrimaryDataAsset` plus an inventory-owning component, subsystem, or gameplay framework object, with UMG presenting the result.
- Inventory design becomes brittle when the UI widget tree is treated as the source of truth. UI should reflect slot state, selection state, and equipment rules; it should not silently become the inventory model.
- Equipment systems should define their rule boundary early:
  - cosmetic slot only
  - stat modifier
  - ability unlock
  - animation or socket binding
  - persistence requirement
- High-risk inventory mistakes repeat across engines:
  - mutating shared authored data instead of per-instance state
  - coupling drag-and-drop directly to save format
  - using world actors or scene nodes as the long-term source of truth for owned items
  - failing to define stackability, uniqueness, and equip-slot rules before content count grows

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Godot ItemList](https://docs.godotengine.org/en/stable/classes/class_itemlist.html)
- [Godot saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity script serialization](https://docs.unity3d.com/kr/6000.0/Manual/script-serialization.html)
- [Unity runtime binding example with ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding-list-view.html)
- [Unity custom inventory property drawer example](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/example-create-custom-inventory-property-drawer.html)
- [Unreal UPrimaryDataAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/UPrimaryDataAsset)
- [Asset Management in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)
- [UMG UI Designer Quick Start Guide in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-quick-start-guide-in-unreal-engine)
- [Saving and Loading Your Game in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine)

## Why this matters to this repo
- Inventory tasks in this repo should explicitly name the data split:
  - item definition
  - runtime owned-item state
  - equipment/loadout state
  - UI representation
  - persistence projection
- Agents should stop recommending "store the whole inventory directly in the UI list" or "save the current actor/node graph exactly as owned item state." Those shortcuts are fast early and expensive later.
- Character and enemy work in this repo will often depend on equipment rules, consumables, loot tables, or ability-granting items. Inventory architecture therefore affects combat, save systems, and UI at the same time.
- This repo wants repeatable task routing and durable design decisions. Inventory tasks should therefore document stack rules, ownership rules, and save boundaries before content count scales.

## Decision impact
- Future feature briefs and save plans should classify every inventory-related field as one of:
  - authored item definition
  - runtime slot or stack state
  - equipment binding
  - durable save/profile state
- Inventory recommendations should specify the engine-native ownership model:
  - Godot: `Resource` definitions, script-backed runtime state, `Control` UI, explicit save projection
  - Unity: `ScriptableObject` definitions, runtime container state, UI Toolkit or prefab/UI layer projection, explicit persistence boundary
  - Unreal: Data Asset definitions, component/subsystem or gameplay-framework-owned runtime state, UMG projection, `USaveGame` or equivalent persistence boundary
- Route and checklist output for inventory tasks should surface both gameplay and persistence research when the task involves equipment, loot persistence, or loadout carryover.
