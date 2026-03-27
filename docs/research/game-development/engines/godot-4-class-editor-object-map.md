# Godot 4 Class, Editor, and Object Map

## Date
- 2026-03-27

## Summary
- Godot's runtime model is tree-first: `Object` is the base type, `Node` is the main runtime building block, `SceneTree` manages the active hierarchy and game loop, and `PackedScene` stores reusable scene hierarchies on disk.
- Godot's editor model is property-first: the Inspector edits `Object` and `Resource` properties, while editor-time automation should be deliberate through `@tool` or editor plugins rather than mixed into ordinary runtime scripts.
- The repo implication is to keep scene ownership explicit, keep reusable data in `Resource` types when appropriate, and treat editor-time scripts as a separate risk surface.

## Primary sources
- [Godot Object class architecture](https://docs.godotengine.org/en/stable/engine_details/architecture/object_class.html)
- [Godot Node class reference](https://docs.godotengine.org/en/stable/classes/class_node.html)
- [Godot SceneTree class reference](https://docs.godotengine.org/en/stable/classes/class_scenetree.html)
- [Godot PackedScene class reference](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [Running code in the editor](https://docs.godotengine.org/en/stable/tutorials/plugins/running_code_in_the_editor.html)
- [EditorDock class reference](https://docs.godotengine.org/en/stable/classes/class_editordock.html)

## Why this matters to this repo
- Godot work in this repo should start by inspecting the current scene tree and node ownership, not by assuming a flat script-only model.
- Agent recommendations need a stable answer to "should this be a node, a scene, a resource, or an editor plugin?" because that decision affects file layout, validation, and long-term iteration speed.
- Editor-time behaviors need stronger caution than runtime behaviors because tool scripts can permanently modify scenes and resources while the editor is open.

## Decision impact
- Godot tasks should link both the architecture baseline and this class/editor/object map before large runtime or editor refactors.
- The Godot checklist should guard scene ownership, resource boundaries, and editor-script safety.
- Godot-specialized agents should explicitly state whether a change belongs in a scene, a script, a `Resource`, or an editor plugin before implementing it.

## Canonical classes and objects

### `Object`
- Base type for Godot objects.
- Use it as the conceptual root when reasoning about notifications, properties, signals, and inspector exposure.
- Agent rule: if a task is about property editing, serialization, or editor inspection, start from the object's property model before changing runtime hierarchy.

### `Node`
- Main runtime building block.
- Nodes become powerful when placed in a tree, and Godot's docs treat a scene as a tree of nodes that can be saved and instantiated.
- Agent rule: use `Node` or a node-derived type for things that need lifecycle callbacks, scene membership, input/processing hooks, or parent-child ownership.

### `SceneTree`
- Owns the active hierarchy and the game loop.
- Also manages current scene switching, pausing, and group operations.
- Agent rule: when a task touches spawning, scene swaps, pause state, or group-wide calls, inspect `get_tree()` usage and `SceneTree` assumptions before changing local node code.

### `PackedScene`
- Serialized reusable scene resource for saving and instantiating scene hierarchies.
- Agent rule: if the same hierarchy should be spawned or reused, prefer a separate scene resource over rebuilding the tree procedurally in multiple places.

### `Resource`
- Use for shared serializable data, authored configuration, and reusable asset-backed state.
- Agent rule: if data must be shared by many scene instances or edited independently of a node tree, consider `Resource` before duplicating exported node fields.

## Editor surfaces

### Inspector and property editing
- Godot's editor inspects object and resource properties, and exported script variables appear there as part of the editing workflow.
- Agent rule: if a task is "make this tunable by designers," first decide whether the value belongs as an exported node property, a `Resource` field, or a custom inspector/editor plugin.

### Dock-based editor extensions
- Godot's editor can host dockable UI through editor plugins.
- Agent rule: if the user wants a workflow panel, importer UI, or editor-only tool surface, use editor plugin patterns instead of runtime scene nodes.

### `@tool` / `[Tool]`
- Godot's docs are explicit that editor-time code is opt-in and that dependent scripts usually also need tool mode.
- Tool scripts can make permanent modifications in the editor.
- Agent rule: use tool scripts only when live editor feedback is the actual requirement; otherwise keep the code runtime-only.

## Agent operating rules
- Inspect the real scene tree and node names before editing script references such as `$Child`, `get_node()`, groups, or signal connections.
- State whether a proposed feature lives in a scene, a node script, a `Resource`, or an editor plugin before implementation.
- Prefer separate `.tscn` scenes for reusable runtime hierarchies and `Resource` assets for shared authored data.
- For editor tooling, verify whether `@tool`, `EditorPlugin`, `EditorInspectorPlugin`, or a dock is actually needed; avoid mixing editor code into runtime scripts by default.
- When touching inspector-facing values, mention how the property will appear to a designer and whether it remains safe to duplicate or instance.

## Common mistakes to avoid
- Treating a reusable subtree like a hard-coded script concern instead of a separate scene.
- Storing shared authored data only on node instances instead of a reusable `Resource`.
- Adding `@tool` without considering permanent editor-side mutations, dependency requirements, or version control recovery.
- Changing node names or hierarchy without checking script paths, group calls, or signal hookups.
