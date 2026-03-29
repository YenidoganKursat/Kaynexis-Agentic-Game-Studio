# Unreal 5 Gameplay Systems Playbook

## Date
- 2026-03-28

## Summary
- Unreal is strongest when world entities, reusable behavior, authored data, and designer-facing UI each have a clearly named owner.
- For this repo, the practical default is: use Enhanced Input for player verbs, `AActor`/`UActorComponent`/`UObject` boundaries for gameplay ownership, UMG or Viewmodel-driven UI for screen state, `UPrimaryDataAsset`/Data Assets for shared authored data, and GAS, StateTree, EQS, or Mass only when the problem scope justifies them.
- The repo should not let damage, ability, UI, and save logic collapse into one Blueprint just because that is the fastest early prototype path.

## Primary sources
- [Enhanced Input API and platform settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/EnhancedInput/UEnhancedInputPlatformSettings)
- [Using Gameplay Abilities in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-abilities-in-unreal-engine)
- [Gameplay Tags API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/GameplayTags)
- [UUserWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/UUserWidget)
- [Widget Blueprints in UMG](https://dev.epicgames.com/documentation/es-es/unreal-engine/widget-blueprints-in-umg-for-unreal-engine)
- [UMG Viewmodel](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-viewmodel-for-unreal-engine)
- [Save Game Blueprint API](https://dev.epicgames.com/documentation/es-es/unreal-engine/BlueprintAPI/SaveGame)
- [AActor::TakeDamage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/TakeDamage)
- [Gameplay Framework in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine)
- [Paper 2D overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine)

## Why this matters to this repo
- Unreal tasks should not start from "make a Blueprint and wire everything into it." They should start from ownership boundaries.
- The repo needs a stable answer to "what is an Actor, what is a Component, what is data, what is UI, and what is save state" because Unreal exposes all of those cleanly and it is easy to overexpose them.
- Enhanced Input, UMG, SaveGame, gameplay tags, and GAS all imply different responsibilities; the repo should name the contract before implementation.

## Decision impact
- Use this playbook when designing controls, widgets, inventory, ability systems, enemy AI, save flows, or performance-sensitive content.
- Prefer explicit boundaries:
  - input intent -> Enhanced Input
  - world presence -> `AActor`
  - reusable sub-behavior -> `UActorComponent`
  - shared authored data -> `UObject`-based data asset
  - UI -> `UUserWidget` / Widget Blueprint / Viewmodel workflow
  - persistence -> SaveGame projection layer

## Input and controls
- Default owner: Enhanced Input.
- Define actions and mappings for verbs such as `Move`, `Dash`, `Interact`, `Pause`, `MenuAccept`, and `MenuBack`.
- Keep player-mappable settings and remapping persistence separate from combat or world logic.
- Watch out for: using raw key polling when a data-driven input action path would keep the project easier to maintain.

## UI, HUD, and menu flow
- Default owner: UMG widgets backed by `UUserWidget`.
- Use Widget Blueprints for designer-editable screens and the Viewmodel workflow when UI should be data-driven and less destructive.
- Keep HUD and menu state distinct from gameplay state so UI can observe and present without becoming the source of truth.
- Watch out for: letting the widget own combat or progression decisions just because it can call back into the world.

## Inventory, equipment, and authored data
- Default owner: `UPrimaryDataAsset`, Data Asset, or other reflected data object for item definitions and shared tuning.
- Runtime slot state should live in a dedicated gameplay object, component, or subsystem, not in the shared asset.
- Use Gameplay Tags where categorization or effect gating needs to stay queryable and designer-friendly.
- Watch out for: hard-coding item data in Blueprint graphs or leaking mutable runtime state into data assets.

## Abilities, upgrades, and build variety
- Default owner: GAS when abilities, costs, cooldowns, and effect flow are part of the real game contract.
- Use Gameplay Tags to describe state, gates, and interaction rules.
- Keep durable unlocks, current-run state, and presentation state separate.
- Watch out for: building a parallel ability framework beside GAS without a strong reason.

## Enemy behavior and encounter design
- Default owner: Actor or Character plus reusable Components, then StateTree/EQS or other explicit AI orchestration when needed.
- Use the Gameplay Framework to decide whether the behavior belongs to Pawn, Character, Controller, or a helper component.
- For large enemy counts, evaluate instancing or Mass earlier than you would in a classic Actor-only design.
- Watch out for: shoving sensing, decision, combat, and UI signaling into one Blueprint class.

## Save and progression
- Default owner: SaveGame projection layer.
- Save durable state, then reconstruct world and UI state from the saved projection.
- Keep save data independent from the live object graph so migration and recovery are manageable.
- Watch out for: serializing the whole live world as if that were a reliable persistence format.

## Performance and scale
- Use Instanced Static Meshes for many repeated visuals.
- Use Mass when the simulation problem is large enough to justify a data-oriented path.
- Use EQS for query-heavy spatial reasoning and StateTree for explicit decision flow before inventing a custom graph.
- Watch out for: assuming Actor-per-entity remains the right answer once counts grow.

## Editor workflow
- Use Details panel exposure intentionally.
- Use Blueprint compile plus PIE/SIE as the first validation loop for gameplay/editor changes.
- Keep C++ ownership, Blueprint exposure, and designer editing surface explicit.
- Watch out for: exposing every internal field as editable just because it is technically possible.

## Best-fit first slice
- For a compact action slice, start with:
  - Enhanced Input actions and rebinding
  - a UMG HUD or menu stack
  - a Data Asset-backed item or ability definition
  - a simple `TakeDamage` contact model before GAS
  - explicit Blueprint/Actor/Component ownership lines

## Common mistakes to avoid
- Using Blueprint as a dumping ground for every responsibility.
- Making UI the authority for gameplay state.
- Hard-coding asset references when a data asset or exposed default would be clearer.
- Choosing GAS before the project actually needs it.
- Letting Actor counts scale uncontrolled when instancing or Mass would be the honest fit.
