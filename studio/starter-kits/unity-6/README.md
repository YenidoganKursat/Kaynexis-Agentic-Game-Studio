# Unity 6 Starter Kit

Use this kit when the repo should target Unity 6 / 6000.x with a package-aware, asmdef-first structure.

Key assumptions:

- code is grouped by feature, not by giant shared folders
- `Packages/manifest.json` is committed and treated as a contract
- asmdef files create explicit runtime/editor/test boundaries
- the real editor binary can stay external while the repo still validates the intended commands
- the scaffold includes a sample combat-room runtime slice: player avatar, pulse enemy, health contract, enemy data asset, editor build entrypoint, and edit-mode tests

What "full repo support" means for Unity in this template:

- `Assets/Scripts/Runtime/` contains a concrete sample ownership model
- `Assets/Scripts/Editor/` contains the build execute-method entrypoint used by the adapter contract
- `Assets/Tests/EditMode/` contains deterministic test examples
- `Assets/Scenes/`, `Assets/Prefabs/`, and `Assets/ScriptableObjects/` document where authored assets belong
- `scripts/unity_adapter.py` exposes test and build command generation for real CLI use once `UNITY_CLI` is configured
