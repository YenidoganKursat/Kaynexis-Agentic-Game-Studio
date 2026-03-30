# Assets Research

## Summary
This folder records asset ownership choices, import rules, and alternative stacks for source art, shared tuning, reusable hierarchies, and streamable libraries.

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot PackedScene](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [Godot ResourceLoader](https://docs.godotengine.org/en/stable/classes/class_resourceloader.html)
- [Godot import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity AssetDatabase](https://docs.unity3d.com/6000.1/Documentation/Manual/AssetDatabase.html)
- [Unity Sprite Atlas](https://docs.unity3d.com/6000.1/Documentation/Manual/class-SpriteAtlas.html)
- [Unity Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
- [Unreal Data Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine)
- [Unreal Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)
- [Unreal Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine)

## Structure
- `alternatives.md`
- `ownership.md`
- `import.md`

## How to use this
- Read `alternatives.md` when deciding between runtime objects, shared assets, and streaming strategies.
- Read `ownership.md` when runtime state, authored data, and editor ownership are getting mixed together.
- Read `import.md` when folder layout, naming, compression, or load paths are changing.
- Pair this folder with `docs/reference/asset-guide.md` and `docs/examples/asset-example.md`.

## Validation rule
- If a task changes asset ownership, import behavior, or packaging assumptions, it must name the source asset, runtime owner, and validation path.
