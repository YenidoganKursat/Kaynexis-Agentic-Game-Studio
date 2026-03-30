# Unreal Classes

## Date
- 2026-03-27

## Summary
- Unreal's most-used gameplay primitives revolve around the gameplay framework, reflected object model, Components, and designer-facing assets. The practical starting question is usually whether a feature belongs in an `AActor`, `APawn`/`ACharacter`, `UActorComponent`, Blueprint, or a data asset.
- Unreal supports both 3D gameplay framework work and Paper2D work, but most production problems are solved by being explicit about which world stack owns the feature instead of mixing them ad hoc.
- The fastest iteration path in Unreal usually combines C++ or Blueprint class ownership with an editor validation loop: Details-panel edit, Blueprint compile if relevant, then PIE/SIE.

## Primary sources
- [Unreal Engine Terminology](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-terminology)
- [Gameplay Framework in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine)
- [Unreal Engine Actors Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actors-reference)
- [Quick Start Guide to Components and Collision in Unreal Engine C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-guide-to-components-and-collision-in-unreal-engine-cpp)
- [Paper 2D overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine)
- [Data Assets in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine)
- [Exposing Gameplay Elements to Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-gameplay-elements-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.6)
- [Blueprint Editor toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine)
- [Details panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine)
- [Play and Simulate in editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine)
- [Epic C++ Coding Standard for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine)

## Why this matters to this repo
- Unreal tasks in this repo need a durable reference for which class family usually owns a mechanic and which parts should stay Blueprint- or data-driven.
- Repo users need a practical 2D and 3D mechanic map that sits between the broad architecture note and the heavier AI/damage/performance note.
- Agent outputs should be able to say, concretely, whether a mechanic belongs in gameplay framework classes, reusable Components, Paper2D objects, or designer-authored data assets.

## Decision impact
- Unreal recommendations should cite this guide when choosing between `Actor`, `Character`, `Component`, Blueprint exposure, and data-asset ownership.
- Feature briefs should explicitly name the gameplay-framework owner, the reusable behavior layer, and the data-asset layer.
- Checklist and route outputs should treat 2D-vs-3D gameplay framework choice as a first-class design decision.

## 2D building blocks

### Paper2D sprites and flipbooks
- Purpose: authored 2D rendering and animation surfaces inside Unreal.
- Use them for: 2D characters, props, and simple sprite-driven gameplay presentation.
- Watch out for: assuming a full 2D-specific gameplay framework will replace all ordinary Actor/Component decisions; Paper2D still benefits from clear gameplay ownership.

### `AActor`
- Purpose: spawnable or placeable world entity.
- Use it for: pickups, hazards, triggers, interactables, and simple enemies or world objects in 2D or 3D.
- Watch out for: using plain actors for everything when a shared component or data asset would reduce duplication.

### collision components
- Purpose: overlap and blocking ownership.
- Use them for: trigger zones, pickups, melee contact, hazard rings, and proximity checks.
- Watch out for: vague collision channel rules or too many unrelated concerns on one collision primitive.

## 3D building blocks

### `ACharacter`
- Purpose: gameplay-framework character with movement support, common controller integration, and capsule-oriented character assumptions.
- Use it for: player avatars, humanoid enemies, and movement-heavy gameplay entities in 3D.
- Watch out for: forcing non-character simulation problems into `ACharacter` just because it is convenient.

### `APawn` and Controllers
- Purpose: possession-based gameplay entity and its controlling logic.
- Use them for: custom embodied units, vehicles, or scenarios where you want a pawn that is not a standard character.
- Watch out for: mixing control authority across Pawn, Controller, and Components without a clean ownership split.

### `UActorComponent`
- Purpose: reusable sub-behavior attached to actors.
- Use it for: health, interaction, targeting, ability gateways, status effects, and other reusable gameplay capabilities.
- Watch out for: turning a component into a hidden god-system with too many unrelated responsibilities.

### camera rig components
- Purpose: common 3D camera composition through spring arm and camera components.
- Use them for: follow cameras, shoulder cameras, orbit rigs, and authored framing.
- Watch out for: hard-coding camera assumptions into the character when the rig should remain swappable or designer-tunable.

## Shared authored-data building blocks

### Blueprints
- Purpose: designer-facing class extension and composition surface.
- Use them for: defaults, composition, event graphs, and designer iteration on gameplay classes that already have a stable core API.
- Watch out for: exposing unstable internals just because Blueprint makes it easy.

### Data Assets
- Purpose: shared authored data.
- Use them for: enemy archetypes, item definitions, encounter tuning, progression tables, and other reusable configuration.
- Watch out for: putting transient runtime state into data assets instead of keeping them as authored templates.

## Common mechanic patterns

### Player movement
- 2D default: keep Paper2D presentation separate from gameplay ownership; decide whether the unit is still best expressed as an `Actor`, `Pawn`, or `Character`.
- 3D default: use `ACharacter` when standard character movement and possession are the mechanic baseline.
- Watch out for: spreading input, locomotion, and camera authority across Character, Controller, and Blueprint without naming the source of truth.

### Contact and damage
- Use collision and overlap components for readable authored contact.
- Use `TakeDamage`-style simple damage flow for straightforward combat systems.
- Escalate to the Gameplay Ability System when attributes, effects, replication, and reusable ability logic become core architecture concerns.
- Watch out for: mixing simple damage and GAS concepts in the same feature without a declared owner.

### Camera and framing
- Use spring-arm plus camera composition for many third-person cases.
- Keep combat target logic, lock-on state, and camera lag ownership explicit instead of burying them across multiple Blueprints.

### Spawn and reuse
- Use Actors for world presence.
- Use Components for reusable behavior.
- Use Data Assets for reusable tuning.
- Use Blueprints to expose stable defaults and assembly surfaces.
- Watch out for: hard-coded asset paths or C++-only defaults when designers need to iterate in-editor.

### Animation and state
- Use animation blueprints and gameplay state together, not as substitutes for each other.
- Keep hit confirmation, invulnerability, and state transitions understandable outside the animation graph.

## Writing style and naming

### Engine-native style
- Follow Unreal's reflection-aware C++ patterns and coding standard.
- Practical repo rule:
  - keep Unreal type prefixes meaningful: `U`, `A`, `F`, `E`, `I`, `T`
  - use clear `UPROPERTY` and `UFUNCTION` exposure only where designers or Blueprints actually need them
  - keep header ownership and module boundaries explicit

### Runtime vs editor style
- Keep editor-facing exposure deliberate:
  - C++ for stable core behavior
  - Blueprint for assembly and tuned defaults
  - Details panel for safe authored parameters
- Prefer data assets and Blueprint defaults over hard-coded references when the feature is meant to be tuned by content authors.

## What to watch out for
- Using `AActor` for every concern instead of splitting reusable logic into components.
- Letting Blueprint exposure sprawl until internal invariants can be broken in the editor.
- Treating Paper2D as a total architecture replacement instead of a presentation and content layer that still needs gameplay ownership clarity.
- Building gameplay state only in animation or Blueprint graphs without documenting the system contract.
- Hard-coding asset ownership in C++ when the mechanic should be designer-driven.

## Additional structural families

### `UPrimitiveComponent`, `UStaticMeshComponent`, `USkeletalMeshComponent`, and `UCharacterMovementComponent`
- Purpose: collision, visible bodies, and movement support.
- Use them for: blocking surfaces, visible world props, animated characters, and authored locomotion bodies.
- Watch out for: hiding unrelated gameplay state inside the mesh or movement component just because it is convenient.

### `UCameraComponent` and `USpringArmComponent`
- Purpose: camera framing and follow composition.
- Use them for: third-person rigs, shoulder cameras, orbit setups, and adjustable camera offsets.
- Watch out for: mixing camera authority with input or combat logic.

### `UWidgetComponent`
- Purpose: world-space UI projection.
- Use it for: diegetic labels, status billboards, and interactable overlays.
- Watch out for: using world widgets to own the real HUD state.

### `UEnhancedInputComponent`, `UInputAction`, `UInputMappingContext`, and `UEnhancedInputLocalPlayerSubsystem`
- Purpose: modern input mapping and possession-aware input flow.
- Use them for: explicit input maps, action bindings, and player-specific routing.
- Watch out for: hard-coding input assumptions into the pawn when the mapping should live in the input layer.

### `UGameInstanceSubsystem`, `UWorldSubsystem`, and `ULocalPlayerSubsystem`
- Purpose: scoped service ownership.
- Use them for: session services, world services, and local-player services.
- Watch out for: dumping every shared service into one global singleton shape.

### `UDataTable` and `UTimelineComponent`
- Purpose: authored tabular data and time-based sequencing.
- Use them for: balance tables, content lookups, and scripted timing.
- Watch out for: using tables as live state stores or timelines as hidden game rules.

### `UBehaviorTree`, `UBlackboardComponent`, and `UNiagaraComponent`
- Purpose: AI structure and scalable VFX.
- Use them for: readable AI behavior, tactical sensing, and visual feedback.
- Watch out for: turning AI helpers or VFX components into the real gameplay owner.
