# Asset Guide

## Summary
Asset decisions are about ownership, lifecycle, and reuse: source file, imported artifact, shared tuning asset, reusable scene/object, or streamable bundle.

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot PackedScene](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [Godot ResourceLoader](https://docs.godotengine.org/en/stable/classes/class_resourceloader.html)
- [Godot project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)
- [Godot import process](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity AssetDatabase](https://docs.unity3d.com/6000.1/Documentation/Manual/AssetDatabase.html)
- [Unity Sprite Atlas](https://docs.unity3d.com/6000.1/Documentation/Manual/class-SpriteAtlas.html)
- [Unity Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
- [Unity AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)
- [Unreal Data Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine)
- [Unreal Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)
- [Unreal Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine)

## Why this matters to this repo
- Asset-heavy tasks fail when source art, imported assets, shared tuning, and live runtime state are mixed together.
- The agent needs a stable answer to "what owns the truth" before it recommends content work.
- The repo should prefer deterministic naming and a small set of official asset alternatives over ad hoc import hacks.

## Decision impact
- Prefer a clear source-to-runtime path.
- Keep shared tuning out of mutable runtime state.
- Prefer the smallest engine-native alternative that can survive scale and validation.
- Use streamable or soft-referenced libraries only when the content set truly needs it.

## Asset families and alternatives

| Need | Prefer | Alternatives | Watch out |
| --- | --- | --- | --- |
| Shared tuning | `Resource`, `ScriptableObject`, Data Asset / `PrimaryDataAsset` | tiny hard-coded constants for throwaway prototypes | mutable runtime state in a shared asset |
| Reusable world chunk | `PackedScene`, `Prefab`, `Blueprint` actor template | scripted spawn templates | copying the same hierarchy by hand |
| 2D art presentation | `Sprite2D`, `SpriteRenderer`, Paper2D sprite/flipbook | mesh impostors or generated art when the project needs them | letting the visual node own gameplay truth |
| UI imagery | `TextureRect`, `Image`, `UUserWidget` image layer | vector-like or text-based UI where appropriate | hiding state inside the widget tree |
| Animation playback | `AnimationPlayer`, `Animator`, Animation Blueprint | sprite-sheet playback or code-driven state when the animation graph is not needed | collapsing state and presentation into one graph |
| VFX and particles | `GPUParticles2D` / `GPUParticles3D`, `ParticleSystem`, Niagara | shader-driven effects or animation if particles are overkill | using VFX as the only proof that gameplay happened |
| Large asset libraries | deterministic scene/resource layout, Addressables, Asset Bundles, Asset Manager soft refs | hard references for small slices | loading rules that only work in one scene |
| Placeholder art | modular proxy art, graybox, generated drafts | final authored art later | investing in hero assets before the loop is proven |

## Engine anchors

### Godot 4
- Use `Resource` for shared authored data and `PackedScene` for reusable runtime hierarchies.
- Use `ResourceLoader` and the import pipeline when a task depends on deterministic source-to-runtime loading.
- Prefer editor plugins or import plugins when the content rule itself needs tooling support.

### Unity 6
- Use `ScriptableObject` for shared authored data and `Prefab` for reusable hierarchies.
- Use `AssetDatabase` for editor import and validation tasks.
- Use `Sprite Atlas`, `Addressables`, or `AssetBundles` only when the content set needs the extra packaging boundary.

### Unreal 5
- Use Data Assets or `PrimaryDataAsset` for shared authored data.
- Use `Asset Manager` and soft references when loading boundaries matter.
- Prefer explicit references in editor defaults or Blueprints for designer-facing content.

## Example prompts for the agent
- Compare Godot `Resource`, `PackedScene`, and imported texture ownership for a HUD icon set.
- Decide whether Unity should use `ScriptableObject`, `Sprite Atlas`, or Addressables for inventory art.
- Decide whether Unreal should use Data Assets or soft references for a shop item library.
- Plan a placeholder-art path that can be swapped without changing runtime ownership.

## Validation
- Name the source asset.
- Name the runtime owner.
- Name the shared data owner.
- Name the import or load boundary.
- Name the first validation path before the asset set grows.
