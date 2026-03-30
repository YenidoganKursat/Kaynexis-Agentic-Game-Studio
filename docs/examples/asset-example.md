# Asset Example

## Scope
A small combat-room slice needs item icons, a pickup object, one shared tuning bundle, and one effect asset.

## Baseline
- one reusable source icon
- one runtime pickup object
- one shared tuning asset
- one deterministic import or load rule

## Decision order
1. Identify the source asset.
2. Choose the runtime owner.
3. Choose the shared data owner.
4. Decide the import or load path.
5. Decide the compression, atlas, or packaging rule.
6. Decide the validation path.

## Engine-shaped examples

| Engine | Preferred split | Good alternative | Common mistake |
| --- | --- | --- | --- |
| Godot 4 | `TextureRect` or `Sprite2D`, `Resource`, `PackedScene` | `ResourceLoader`-driven import flow | putting mutable state into `Resource` |
| Unity 6 | `Image` / `SpriteRenderer`, `ScriptableObject`, `Prefab`, `Sprite Atlas`, Addressables | AssetBundles for larger libraries | storing live run state in `ScriptableObject` |
| Unreal 5 | `UUserWidget`, Data Asset / `PrimaryDataAsset`, `AActor` / Blueprint, `Asset Manager`, soft references | Data Tables for flat tuning | hard-coded asset paths or mutable state in Data Assets |

## Good agent prompts
- Compare `Resource`, `PackedScene`, and imported texture ownership for a Godot HUD.
- Decide whether Unity should use `ScriptableObject`, `Sprite Atlas`, or Addressables for an inventory screen.
- Decide whether Unreal should use Data Assets or soft references for shop items and their loading path.
- Plan a low-risk placeholder-art path that preserves runtime ownership.

## Validation
- Name the source file and the runtime consumer.
- Show where import settings live.
- Show where shared tuning lives.
- Show where the first smoke test or manual validation happens.
