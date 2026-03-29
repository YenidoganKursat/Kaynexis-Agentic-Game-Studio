# Engine Profile — Kaynexis Agentic Game Studio

## Engine
- Engine: Godot 4
- Version: 4.x
- Rendering path / pipeline: confirm once real engine-native project files land
- Repo support contract: multi-engine starter-kit parity for Godot 4, Unity 6, and Unreal 5

## Repository layout
- Shared studio config: `studio.toml`
- Front-door workflow: `scripts/codex_studio.py`
- Expected runtime code: `src/`
- Expected content/assets: `assets/`
- Expected tests or manual validation artifacts: `tests/`
- Expected tools/import helpers: `tools/`

## Build targets
- Primary platforms: PC Premium
- Export/package notes: PC-first baseline, controller support expected, artifact names should stay deterministic
- CI/build assumptions: local checks via `make ci-local`, starter-kit validation via `python3 scripts/validate_engine_kits.py`, optional container check via `make docker-verify`, GitHub workflows for validation and Docker smoke

## Starter-kit parity
- Supported engine families: Godot 4, Unity 6, Unreal 5
- Primary engine for this project: Godot 4
- Current runtime reference slice: Godot 4 in `src/`
- Unity starter-kit support includes runtime, editor, prefab, ScriptableObject, and edit-mode test surfaces
- Unreal starter-kit support includes gameplay framework, health/component, data asset, config, and packaging surfaces
- Unity and Unreal support live through starter kits, adapters, checklists, research notes, and CI contract smoke
- Engine-specific caveats and research should be linked from `docs/research/game-development/engines/`

## Core technical constraints
- Performance target: stable 60 FPS on target PC baseline
- Save/network assumptions: local save-safe behavior, no netcode in the first slice
- Native plugins / SDKs: none by default until explicitly added

## Validation workflow
- Fast local checks: `make validate`, `python3 scripts/run_local_evals.py`
- Full validation path: `make ci-local` plus engine-native smoke once the actual project exists
- Release gating notes: add engine-native build/export validation before external demos or shipping branches
