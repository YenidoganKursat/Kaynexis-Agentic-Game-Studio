# Engine Examples

This page shows concrete examples for Godot 4, Unity 6, and Unreal 5.

Use it when you want to move from "which engine?" to "what does this look like in practice?"

## Example slices by engine

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
- `docs/reference/task-prompt-examples.md`
- `docs/reference/workflow-recipes.md`
