# Unreal Visuals

## Date
- 2026-03-28

## Summary
- Unreal's visual layer works best when Paper2D, animation blueprints, UMG, and Niagara each keep a clear ownership boundary instead of being blended into one Blueprint graph.
- For this repo, the practical default is: use Paper2D for 2D sprite presentation, Animation Blueprints for skeletal animation state, UMG for UI imagery and screen flow, and Niagara for particle-driven effects.
- The repo should decide explicitly whether a visual is 2D sprite art, 3D skeletal animation, UI presentation, or a VFX system before implementation starts.

## Primary sources
- [Content Examples Sample Project](https://dev.epicgames.com/documentation/de-de/unreal-engine/content-examples-sample-project-for-unreal-engine)
- [Paper 2D Sprite Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-sprite-material-in-unreal-engine?application_version=5.6)
- [Control Animation Blueprint Parameters from Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-animation-blueprint-parameters-from-sequencer-in-unreal-engine?application_version=5.6)
- [Displaying Your UMG UI in the Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/displaying-your-umg-ui-in-the-viewport-in-unreal-engine%3Fapplication_version%3D5.2%3Fapplication_version%3D5.2%3Fapplication_version%3D5.2?application_version=5.2)
- [Particle effects](https://dev.epicgames.com/documentation/es-es/unreal-engine/6-16-particle-effects)

## Why this matters to this repo
- Unreal tasks in this repo should not collapse sprite work, animation work, UI work, and VFX work into one Blueprint because it is convenient in the short term.
- Agents need a stable answer to "is this Paper2D, animation, UI, or Niagara?" because that choice affects authoring, debugging, and packaging.
- Visual decisions should stay compatible with the repo's broader rule that gameplay authority, editor exposure, and presentation do not belong to the same layer by default.

## Decision impact
- Use this playbook when a task involves sprites, flipbooks, animation blueprints, UI widgets, or particle effects.
- Prefer explicit boundaries:
  - 2D sprite presentation -> Paper2D
  - skeletal animation state -> Animation Blueprint / animation-driven editor workflow
  - UI imagery and menu screens -> UMG / Widget Blueprints
  - particle-driven VFX -> Niagara
  - shared tuning and reusable materials -> asset-backed data rather than hard-coded Blueprint graphs

## 2D visuals
- Paper2D is the right home for 2D sprite presentation in Unreal when the project wants a sprite/flipbook-style workflow.
- Keep the sprite presentation surface separate from collision, combat, and progression state.
- Watch out for: assuming 2D presentation means the whole feature should be structured like a generic Blueprint dump.

## 3D visuals
- For 3D presentation, keep the visual hierarchy attached to the gameplay entity rather than mixing render concerns into a world controller.
- Use component and asset ownership deliberately so the same gameplay actor can swap materials, meshes, or presentation layers without changing the rules of the mechanic.
- Watch out for: letting visual complexity hide the actual gameplay owner.

## Animation and presentation
- Animation Blueprints are the main stateful presentation layer for animated characters and other skeletal motion systems.
- Use animation state to reflect gameplay state and timing, not as the only authority for gameplay truth.
- Keep blend/transition logic readable so designers can reason about what will happen in the editor.
- Watch out for: burying combat or persistence truth only in animation graphs or Sequencer timelines.

## UI image ownership
- UMG and Widget Blueprints own the UI presentation layer.
- Keep the widget's screen state separate from gameplay state, then project runtime data into the widget.
- When the UI needs data flow rather than raw graph logic, prefer a viewmodel-style approach or a clear projection layer.
- Watch out for: making widgets decide gameplay outcomes because they are easiest to edit.

## VFX and particles
- Niagara is the default owner for modern particle-driven effects.
- Keep VFX as presentation, and keep the trigger and gameplay consequence in the gameplay layer.
- Watch out for: particle systems being the only proof that the effect happened when the gameplay layer has no confirmation path.

## Common mistakes
- Collapsing Paper2D, animation, UI, and VFX into one Blueprint graph.
- Hard-coding the image or animation authority so designers cannot swap presentation safely.
- Letting UMG or Niagara own gameplay state instead of observing it.
- Using particles to hide a lack of clear animation or gameplay timing.
