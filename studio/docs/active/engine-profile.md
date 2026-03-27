# Engine Profile — kaynexisGame

## Engine
- Engine: Godot 4
- Version: 4.x
- Rendering path / pipeline: `forward_plus`

## Repository layout
- Expected runtime code: `src/`
- Expected content/assets: `assets/`
- Expected tests or manual validation artifacts: `tests/`
- Expected tools/import helpers: `tools/`

## Build targets
- Primary platforms: PC Premium
- Export/package notes: PC-first baseline, keyboard-first inputs now present, controller support still planned, artifact names stay deterministic
- CI/build assumptions: local checks via `make ci-local`, static Godot validation via `make godot-smoke`, optional container check via `make docker-verify`, GitHub workflows for validation and Docker smoke

## Core technical constraints
- Performance target: stable 60 FPS on target PC baseline
- Save/network assumptions: local save-safe behavior, no netcode in the first slice
- Native plugins / SDKs: none by default until explicitly added

## Validation workflow
- Fast local checks: `make validate`, `python3 scripts/run_local_evals.py`, `make test`
- Full validation path: `make ci-local`, then `make godot-smoke`, then `make export-linux` once `GODOT_BIN` or a local Godot install exists
- Release gating notes: do not tag demo or release branches until runtime smoke and at least one export preset have passed on a real machine or CI runner
