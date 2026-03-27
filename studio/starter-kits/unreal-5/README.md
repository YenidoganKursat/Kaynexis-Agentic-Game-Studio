# Unreal 5 Starter Kit

Use this kit when the repo should target Unreal Engine 5.x with explicit module, config, and packaging boundaries.

Key assumptions:

- runtime modules live under `Source/`
- project config stays under `Config/`
- content stays under `Content/`
- cook/package commands are documented even before automation is attached
- the scaffold includes a sample gameplay framework surface: character, enemy actor, health component, data asset, project config, and packaging contract

What "full repo support" means for Unreal in this template:

- `Source/StarterKit/` contains a real ownership split between gameplay framework classes and data assets
- `Config/` contains startup-map and input assumptions instead of leaving the project config blank
- `Content/Blueprints/` and `Content/Maps/` explain where Blueprint assembly and level content should live
- `scripts/unreal_adapter.py` exposes package command generation for real `UNREAL_UAT` / `UNREAL_EDITOR` use once configured
