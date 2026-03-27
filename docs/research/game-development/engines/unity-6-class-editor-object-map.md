# Unity 6 Class, Editor, and Object Map

## Date
- 2026-03-27

## Summary
- Unity's runtime model is container-first: `GameObject` is the scene unit, functionality comes from attached Components, and reusable authored hierarchies are usually stored as Prefabs.
- Unity's data model is asset-first: `ScriptableObject` is for shared authored data and tooling state, while `MonoBehaviour` remains attached behavior on scene objects and prefabs.
- Unity's editor model is split from runtime code: custom windows derive from `EditorWindow`, custom inspectors derive from `Editor`, and editor editing should prefer `SerializedObject` and `SerializedProperty` so undo, multi-object editing, and prefab overrides keep working.

## Primary sources
- [Unity Manual: The GameObject class](https://docs.unity3d.com/6000.1/Documentation/Manual/class-GameObject.html)
- [Unity Manual: Use components](https://docs.unity3d.com/6000.1/Documentation/Manual/UsingComponents.html)
- [Unity Manual: ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity Manual: Introduction to prefabs](https://docs.unity3d.com/6000.1/Documentation/Manual/prefabs-introduction.html)
- [Unity Scripting API: EditorWindow](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/EditorWindow.html)
- [Unity Scripting API: Editor](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Editor.html)

## Why this matters to this repo
- Unity work in this repo needs a consistent answer to "is this scene state, prefab state, or shared asset data?" because those choices affect memory, authoring, and how safely Codex can refactor behavior.
- Agent output for Unity should be explicit about runtime vs editor-only code, because `UnityEditor` dependencies belong in editor assemblies and should not leak into runtime code paths.
- Checklists and starter kits become stronger when they talk about actual object ownership instead of only folder names.

## Decision impact
- Unity tasks should link both the architecture baseline and this class/editor/object map when new runtime patterns or editor tooling are proposed.
- Unity checklist items should guard the GameObject/Component split, ScriptableObject usage, and editor/runtime separation.
- Unity-specialized agents should explicitly name whether a change belongs in a scene, prefab, component, ScriptableObject asset, custom inspector, or custom window.

## Canonical classes and objects

### `GameObject`
- Fundamental scene object and container for Components.
- Agent rule: treat `GameObject` as the identity and composition container, not as the place where logic "lives" by itself.

### Components and `MonoBehaviour`
- Components add functionality and editable properties to GameObjects.
- Agent rule: if behavior belongs to a placed object or prefab instance, it usually belongs in a Component or `MonoBehaviour`, not in a global singleton by default.

### Prefabs
- Reusable asset templates for GameObject hierarchies.
- Prefab instances stay linked to the source asset, and Unity supports overrides, nested prefabs, and prefab variants.
- Agent rule: when the same hierarchy recurs across scenes or should be spawned at runtime, prefer a prefab over duplicated scene setup.

### `ScriptableObject`
- Shared asset-backed data container derived from `UnityEngine.Object`.
- Not attachable to a GameObject; it is saved as an asset and is well-suited to shared configuration or editor-authored data.
- Agent rule: if data should be shared across many prefab or scene instances without duplication, move it into a `ScriptableObject` instead of repeating it on `MonoBehaviour` fields.

## Editor surfaces

### Inspector
- Components and asset data are edited through the Inspector.
- Agent rule: when making something designer-tunable, explain whether the value should live on a component instance, a prefab asset, or a ScriptableObject asset.

### `EditorWindow`
- Custom dockable or floating editor windows derive from `EditorWindow`.
- Agent rule: use `EditorWindow` for multi-step workflows, content browsers, reports, or tooling panels that are broader than a single inspected object.

### `Editor`
- Custom inspectors derive from `Editor`.
- Unity's docs recommend `SerializedObject` and `SerializedProperty` for custom editing so undo, multi-object editing, and prefab overrides keep working correctly.
- Agent rule: if the task is to improve editing of one asset or component type in the Inspector, prefer a custom `Editor` over a separate window.

## Agent operating rules
- Inspect whether the task belongs to a scene object, prefab, or asset before proposing new code.
- Prefer Components for object-bound behavior, Prefabs for reusable hierarchies, and ScriptableObjects for shared authored data.
- Keep `UnityEditor` APIs inside editor-only code paths and assemblies; runtime code should not depend on editor namespaces.
- When proposing editor extensions, choose `Editor` for object-specific inspector changes and `EditorWindow` for broader workflows.
- If a design requires shared configuration plus per-instance overrides, describe the split explicitly: ScriptableObject for defaults, prefab or component fields for local overrides.

## Common mistakes to avoid
- Packing shared data into every prefab instance instead of a ScriptableObject asset.
- Treating GameObjects as logic containers while leaving the actual ownership of behavior unclear.
- Writing custom inspectors that bypass `SerializedObject` and break undo, multi-editing, or prefab override workflows.
- Mixing `UnityEditor` dependencies into runtime assemblies or gameplay scripts.
