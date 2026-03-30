# Asset Alternatives

## Summary
Asset alternatives are about choosing the smallest engine-native option that still keeps source files, shared data, reusable hierarchies, and runtime load boundaries separate.

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot PackedScene](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [Godot ResourceLoader](https://docs.godotengine.org/en/stable/classes/class_resourceloader.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity Sprite Atlas](https://docs.unity3d.com/6000.1/Documentation/Manual/class-SpriteAtlas.html)
- [Unity Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest)
- [Unity AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)
- [Unreal Data Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine)
- [Unreal Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)
- [Unreal Referencing Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/referencing-assets-in-unreal-engine)

## Why this matters to this repo
- Asset-heavy work in this repo should not force one answer for every use case.
- The agent needs a shortlist of engine-native alternatives so it can choose the smallest safe path first.
- The repo benefits from source-backed decisions instead of hidden import or packaging habits.

## Decision impact
- Prefer `Resource`, `ScriptableObject`, or Data Asset for shared authored data.
- Prefer `PackedScene`, `Prefab`, or Blueprint actor templates for reusable hierarchies.
- Prefer `SpriteAtlas`, Addressables, AssetBundles, or Asset Manager only when the library size or load boundary justifies them.
- Prefer proxy art or graybox assets until the loop is proven.

## Shared data
- Godot: `Resource`
- Unity: `ScriptableObject`
- Unreal: Data Asset or `PrimaryDataAsset`
- Alternative: tiny hard-coded constants for throwaway prototypes
- Watch out for: mutable runtime state in a shared asset

## Reusable hierarchies
- Godot: `PackedScene`
- Unity: `Prefab`
- Unreal: Blueprint actor or reusable actor setup
- Alternative: scripted spawn templates
- Watch out for: copying the same hierarchy by hand

## Presentation
- 2D art: `Sprite2D`, `SpriteRenderer`, Paper2D
- UI imagery: `TextureRect`, `Image`, `UUserWidget`
- Animation: `AnimationPlayer`, `Animator`, Animation Blueprint
- VFX: `GPUParticles2D` / `GPUParticles3D`, `ParticleSystem`, Niagara
- Alternative: mesh-driven or shader-driven presentation when the project needs it
- Watch out for: letting the visual node own gameplay truth

## Streaming and packaging
- Godot: deterministic resource loading and import paths
- Unity: Addressables or AssetBundles for larger libraries
- Unreal: Asset Manager and soft references for streamable content
- Alternative: hard references for small slices
- Watch out for: loading rules that only work in one scene

## Placeholder versus final assets
- modular proxy art
- graybox or blockout
- generated draft assets
- final authored assets
- Watch out for: hero-art investment before the loop is proven

## Validation
- Decide which asset is authoritative.
- Decide what can be regenerated.
- Decide which asset may be streamed or shared.
- Decide what must stay local to a scene, prefab, or actor.
