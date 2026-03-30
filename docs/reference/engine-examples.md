# Engine Examples

This page shows concrete examples for Godot 4, Unity 6, and Unreal 5.

Use it when you want to move from "which engine?" to "what does this look like in practice?"

If you only need the fastest possible owner/stack answer, start with `docs/reference/engine-map.md` first and then come back here for examples.
If the real decision is which engine fits a specific developer profile or team shape, read `docs/reference/engine-fit.md` and `docs/examples/engine-fit-example.md` first, then use this page to translate that fit into a concrete slice.
If the real decision is whether one engine family has a better build, test, performance, or toolchain scorecard, read `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` first, then use this page to translate that decision into a concrete slice.
If you need the class-family breakdown behind those examples, read `docs/reference/engine-atlas.md` next, then the matching engine mini atlas.
If the task is about source art, imported assets, shared tuning, or load boundaries, read `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` before implementation.
If the task is about HUDs, menus, settings, onboarding, or template selection, read `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` before implementation.
If the task is about audio playback, animation timing, or presentation sync, read `docs/reference/audio-animation-guide.md` and `docs/examples/audio-animation-example.md` before implementation.

## Example slices by engine

The examples below are intentionally small. They show the ownership pattern and validation path, not the final content scale.

### Godot 4

Best for:

- a fast first playable slice
- scene-driven iteration
- compact 2D or lightweight 3D prototypes

Example slice:

- a single combat room with a player, one enemy type, one upgrade choice, and one clear win state

Typical ownership:

- runtime behavior in `.gd`
- authored scene structure in `.tscn`
- reusable data in `.tres`
- simple visual state in `AnimationTree`, `Sprite2D`, or `AnimatedSprite2D`

Good prompts:

```bash
python3 scripts/codex_studio.py next "Implement a readable dash and damage window for the first Godot combat room"
python3 scripts/codex_studio.py next "Add a compact upgrade choice screen after room clear in Godot"
python3 scripts/codex_studio.py next "Tune Godot sprite animation ownership for a small boss windup"
```

What to watch:

- keep player state and scene state separate
- do not let visual rings lie about hit logic
- keep collision and camera boundaries explicit

### Unity 6

Best for:

- editor-heavy workflows
- package and assembly boundaries
- content pipelines with tools, prefabs, and ScriptableObject data

Example slice:

- a room-based action prototype with a runtime controller, prefab-based enemies, ScriptableObject upgrades, and edit-mode validation

Typical ownership:

- runtime behavior in `MonoBehaviour`
- authored data in `ScriptableObject`
- reusable scene setup in `Prefab`
- editor tooling in `EditorWindow` or editor scripts

Good prompts:

```bash
python3 scripts/codex_studio.py next "Design a Unity upgrade screen that reads from ScriptableObject data and controller navigation"
python3 scripts/codex_studio.py next "Implement pooled projectiles and clear damage feedback for a Unity combat slice"
python3 scripts/codex_studio.py next "Plan a Unity editor tool for tagging combat VFX assets by gameplay event"
```

What to watch:

- keep runtime logic out of editor-only scripts
- keep prefabs small and data-driven
- avoid making ScriptableObjects hold transient per-run state

### Unreal 5

Best for:

- gameplay-framework-first projects
- larger 3D systems
- teams that want strong packaging and engine-native architecture

Example slice:

- a gameplay framework-based encounter with a Character, Component, Data Asset, HUD widget, and packaging validation

Typical ownership:

- runtime behavior in `Actor`, `Character`, `Pawn`, or `Component`
- authored data in `Data Asset` / `Primary Data Asset`
- visual scripting in `Blueprint`
- presentation in `UMG`

Good prompts:

```bash
python3 scripts/codex_studio.py next "Design an Unreal combat slice with character movement, enemy aggro, and UI health feedback"
python3 scripts/codex_studio.py next "Plan a Blueprint-friendly upgrade selection screen for Unreal 5"
python3 scripts/codex_studio.py next "Prepare Unreal packaging validation for a Win64 demo build"
```

What to watch:

- keep gameplay state in gameplay classes, not widgets
- keep content ownership clear between Blueprint and C++
- do not assume packaging is healthy unless the packaging path actually runs

## Same mechanic, three engine examples

Use this section when the same feature must make sense in Godot, Unity, and Unreal without collapsing into a one-engine assumption.

### A short dodge mechanic

- Godot 4: `CharacterBody2D` or `CharacterBody3D` owns movement, with animation and invulnerability frames separated into dedicated logic.
- Unity 6: `CharacterController` or `Rigidbody` movement plus a small state machine and animation parameters.
- Unreal 5: `Character` plus movement component, with animation state and ability timing kept separate.

### A combat upgrade choice

- Godot 4: scene node for the upgrade UI, `Resource`-backed upgrade data, and a small runtime selection system.
- Unity 6: `ScriptableObject` upgrade definitions, prefab UI, and controller-safe menu navigation.
- Unreal 5: `Primary Data Asset` or data table for upgrade definitions, `UMG` for presentation, and gameplay class ownership for the state change.

### A persistent inventory

- Godot 4: data objects for item definitions, runtime inventory container in script, and save conversion that avoids direct scene coupling.
- Unity 6: `ScriptableObject` item definitions, runtime inventory state in a plain C# model or service, and explicit save migration boundaries.
- Unreal 5: data asset definitions, runtime inventory on gameplay classes or components, and save-game serialization with clear ownership.

## UI and template examples

Use this section when the question is about HUDs, menus, settings, onboarding, or template choice rather than only styling.

### A controller-first pause menu

- Godot 4: `Control` owns the flow, `CanvasLayer` owns the overlay, and `Theme` owns the shared style. Start from the Godot UI tutorials or an Asset Library UI pack when you need a ready-made template.
- Unity 6: UI Toolkit owns the reusable layout, `UIDocument` binds the runtime screen, and UI Builder or package samples provide the starting template. Use uGUI only if the screen is intentionally simple or legacy-bound.
- Unreal 5: `UMG` / Widget Blueprints own the visible screen, CommonUI owns controller-first activation, and a widget blueprint template or sample project is the closest ready-made starter.

### A settings screen

- Godot 4: a `Control` scene with explicit focus order and pause behavior.
- Unity 6: UI Toolkit if the screen is reusable or data-heavy, uGUI if the screen is a small runtime overlay.
- Unreal 5: UMG + CommonUI when the screen must respect controller focus and input routing.

Good prompts:

```bash
python3 scripts/codex_studio.py next "Design a controller-first pause menu in Godot using Control, CanvasLayer, and a Theme source"
python3 scripts/codex_studio.py next "Use Unity UI Toolkit and UI Builder to build an inventory screen with UXML templates and USS styles"
python3 scripts/codex_studio.py next "Choose UMG, CommonUI, and Enhanced Input for an Unreal settings menu and name the widget template source"
```

## Audio and animation examples

Use this section when sound cues and visible motion must stay aligned without making presentation the gameplay owner.

### A short boss windup

- Godot 4: `AudioStreamPlayer` plays the cue while `AnimationPlayer` or `AnimationTree` handles the visible windup and reaction.
- Unity 6: `AudioSource` plays the cue while `Animator` owns the animation state and `AudioMixer` handles the mix split if needed.
- Unreal 5: `Audio Components` or `MetaSounds` play the cue while `Animation Blueprints` own the visible windup and `Quartz` or Sequencer only enters when sync needs proof.

### A UI confirm and close

- Godot 4: `AudioStreamPlayer` handles the confirm sound while `Control` and `AnimationPlayer` own the menu motion.
- Unity 6: `AudioSource` handles the confirm sound while `Animator` and the UI flow own the visible transition.
- Unreal 5: `Audio Components` handle the confirm cue while UMG and `Animation Blueprints` own the visible state change.

## GPU and render scale examples

Use this section when the question is not just "can the game render this?" but "where should repeated visuals, buffer data, and GPU work live?"

### Godot 4

- `RenderingServer` for render-side ownership when the scene tree is the wrong scale boundary.
- `RenderingDevice` for compute or buffer-driven work when a real GPU contract is required.
- `MultiMesh` / `MultiMeshInstance3D` for repeated visuals before inventing a per-node swarm.

### Unity 6

- `GraphicsBuffer` for structured render data that should stay buffer-shaped.
- `ComputeShader` for uniform, parallel GPU work.
- Instanced indirect drawing for dense repeated visuals before a DOTS rewrite.

### Unreal 5

- Instanced Static Meshes for repeated geometry before increasing Actor count.
- Nanite when the problem is virtualized detail and geometry scale.
- HLOD when the problem is world-scale visibility reduction.

Good prompts:

```bash
python3 scripts/codex_studio.py next "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever"
python3 scripts/codex_studio.py next "Compare Unity GraphicsBuffer, ComputeShader, and indirect instancing for a dense projectile field before changing gameplay code"
python3 scripts/codex_studio.py next "Choose between Unreal Instanced Static Meshes, Nanite, and HLOD for repeated world objects before scaling Actor count"
```

## Example validation paths

Godot:

```bash
python3 scripts/godot_smoke.py --static-only
python3 scripts/godot_export.py --preset "Linux/X11"
```

Unity:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --dry-run --json
```

Unreal:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

## When to use this page

Use this page when:

- the same mechanic needs to make sense in all three engines
- a contributor needs concrete examples instead of abstract engine advice
- you want to avoid accidentally designing a Godot-only solution for a Unity or Unreal task
- you are comparing runtime ownership, editor ownership, and authored data across engines

## Related references

- `docs/reference/engine-selection-guide.md`
- `docs/research/game-development/engines/README.md`
- `docs/research/game-development/engines/*-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/*-systems-playbook.md`
- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/ui-guide.md`
- `docs/examples/ui-example.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/asset-guide.md`
- `docs/reference/engine-fit.md`
- `docs/examples/engine-fit-example.md`
- `docs/reference/engine-eval.md`
- `docs/examples/engine-eval-example.md`
- `docs/reference/workflow-recipes.md`
