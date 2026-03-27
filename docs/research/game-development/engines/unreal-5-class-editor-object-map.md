# Unreal 5 Class, Editor, and Object Map

## Date
- 2026-03-27

## Summary
- Unreal's object model is class-first: `UObject` is the base of the reflection, serialization, and garbage collection system; `AActor` is the base class for objects that can be placed or spawned in a level; and Components provide reusable behavior and spatial hierarchy within actors.
- Unreal's authoring model is editor-first: exposed properties surface in the Details panel, gameplay classes can be extended in Blueprints, and the Blueprint Editor plus Play/Simulate loops are core to iteration.
- The repo implication is to decide early whether a feature belongs in a `UObject`, an `AActor`, a `UActorComponent`, or a Blueprint-facing class, because that choice shapes module layout, editor affordances, and packaging behavior.

## Primary sources
- [Unreal Engine Terminology](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-terminology)
- [Unreal Engine Actors Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actors-reference)
- [Quick Start Guide to Components and Collision in Unreal Engine C++](https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-guide-to-components-and-collision-in-unreal-engine-cpp)
- [Exposing Gameplay Elements to Blueprints Visual Scripting in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/exposing-gameplay-elements-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.6)
- [Toolbar in the Blueprints Visual Scripting Editor for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine)
- [Level Editor Details Panel in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine)
- [In-Editor Testing (Play & Simulate) in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/ineditor-testing-play-and-simulate-in-unreal-engine)

## Why this matters to this repo
- Unreal changes are expensive to unwind if Actor, Component, Blueprint, and editor exposure decisions are made casually.
- Agent guidance needs to be precise about what is level-placeable, what is reusable behavior, what is pure data/supporting object state, and what must remain editor-facing for designers.
- Packaging and build docs are stronger when they are informed by the actual object and module model rather than only by command lines.

## Decision impact
- Unreal tasks should link both the architecture baseline and this class/editor/object map before introducing new gameplay classes, modules, or editor-facing property surfaces.
- Unreal checklist items should guard Actor vs Component ownership, Blueprint exposure boundaries, and designer-editable property safety.
- Unreal-specialized agents should name whether a change belongs in `UObject`, `AActor`, `UActorComponent`, Blueprint, or editor-only code before implementation.

## Canonical classes and objects

### `UObject`
- Base class of all Unreal objects, with garbage collection, metadata, editor exposure, and serialization support.
- Agent rule: if something needs reflection, serialized properties, editor exposure, or Blueprint access but does not need to exist in the world as a placeable entity, consider `UObject` first.

### `AActor`
- Base class for objects that can be placed or spawned in a level.
- Agent rule: use an Actor for world presence, spatial identity, level placement, or spawning; do not use Actors as the default shape for every helper system.

### Components
- Components are attached to Actors and commonly arranged in a hierarchy under a root component.
- Unreal's own component quick start demonstrates using a root collision component, visual mesh component, particle system component, spring arm, and camera as a single Actor hierarchy.
- Agent rule: if the feature is reusable behavior or a sub-part of an Actor rather than an independent world entity, prefer a Component.

### Pawn / Character / Controller
- Unreal's terminology docs treat Pawn and Character as gameplay-facing Actor roles, with Controllers possessing Pawns.
- Agent rule: if the task changes player embodiment, AI possession, or input authority, state clearly whether the change belongs to a Pawn/Character, the Controller, or a shared component.

### Blueprints
- Blueprint is the designer-facing extension layer for classes and exposed gameplay elements.
- Agent rule: if a system needs designer iteration on properties or graph-level composition, prefer a Blueprint-facing API over hard-coded values hidden in C++.

## Editor surfaces

### Details panel
- The Details panel is the main property editing surface for selected actors and assets.
- Agent rule: when proposing `UPROPERTY` exposure, think about the exact Details-panel experience and whether the property is safe, understandable, and stable enough for non-programmers to edit.

### Blueprint Editor
- The Blueprint editor toolbar exposes compile, search, class defaults, and play/simulate/debug workflows.
- Agent rule: if the task affects Blueprint-authored iteration, describe how the class will compile, where defaults will be edited, and how the change will be debugged in-editor.

### Play In Editor / Simulate In Editor
- Unreal's editor supports immediate in-editor play and simulate loops from the Level Editor and Blueprint Editor.
- Agent rule: every Unreal gameplay or Blueprint task should include a narrow PIE/SIE validation path, not only a packaging command.

## Agent operating rules
- Inspect `.uproject`, `Config/`, `Source/`, and `Content/` before proposing new files or moving responsibilities.
- Decide first whether the feature is a `UObject`, an `AActor`, or a Component concern; make that ownership decision explicit in the recommendation.
- Prefer designer-owned asset references and editor-exposed defaults over hard-coded asset paths in C++ when the feature is meant to be tuned in Unreal Editor.
- Use Blueprint exposure deliberately: expose what designers need, but avoid turning low-level implementation details into editable defaults without guardrails.
- Always include an editor validation loop, such as Details-panel edit + Blueprint compile + PIE/SIE check, before discussing packaging.

## Common mistakes to avoid
- Creating Actors for every piece of reusable behavior that should really be a Component or a simpler reflected object.
- Hard-coding asset paths in C++ for designer-facing content that should be assigned in editor defaults or Blueprints.
- Exposing too much internal state to the Details panel or Blueprints without a stable ownership model.
- Treating packaging as the only proof path while skipping Blueprint compile and Play In Editor validation.
