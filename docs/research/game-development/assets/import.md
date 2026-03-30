# Asset Import

## Summary
Asset import is about source files, imported artifacts, compression, naming, and reload behavior.

## Primary sources
- [Godot ResourceLoader](https://docs.godotengine.org/en/stable/classes/class_resourceloader.html)
- [Godot import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html)
- [Unity AssetDatabase](https://docs.unity3d.com/6000.1/Documentation/Manual/AssetDatabase.html)
- [Unity Sprite Atlas](https://docs.unity3d.com/6000.1/Documentation/Manual/class-SpriteAtlas.html)
- [Unity Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
- [Unreal Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)
- [Unreal Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine)

## Why this matters to this repo
- Import behavior changes build determinism, memory, and runtime load paths.
- Asset decisions in this repo should say where source ends and runtime-ready data begins.
- The agent should pick the smallest boundary that can survive validation.

## Decision impact
- Use deterministic source roots and import roots.
- Compress only after the read path is stable.
- Choose atlases, Addressables, AssetBundles, or soft references only when scale needs them.
- Keep the load boundary explicit so tasks remain testable.

## Source versus imported files
- Source art lives in authoring space.
- Imported assets live in runtime-ready space.
- The build should know which is which.

## Naming and folder rules
- Use deterministic names.
- Keep source roots stable.
- Keep import roots predictable.

## Compression and residency
- Compress only after the read path is stable.
- Pack atlases when reuse matters.
- Stream large libraries only when scale justifies the complexity.

## Engine notes

### Godot 4
- `ResourceLoader` and import plugins own the import boundary.
- Imported assets are not the same as source files.

### Unity 6
- `AssetDatabase` owns editor import and asset queries.
- Use `Sprite Atlas`, Addressables, or AssetBundles deliberately rather than by habit.

### Unreal 5
- `Asset Manager` and soft references help shape what loads when.
- Keep designer-facing references explicit in editor defaults or data assets.

## Validation
- Validate naming.
- Validate the import root.
- Validate the load path.
- Validate the compression choice.
