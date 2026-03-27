# Codex Compatibility

This repository is intentionally shaped around official Codex repo conventions.

It is also intentionally multi-engine. The repo-level contract covers `godot-4`, `unity-6`, and `unreal-5`; the current Godot slice is only the reference implementation that proves the studio OS can drive a real runtime surface.

## Codex-native surfaces in this repo

- `AGENTS.md` at the repo root, plus nested `AGENTS.md` files
- `.codex/config.toml` for shared project defaults
- `.codex/agents/` for focused custom agents
- `.agents/skills/` for reusable workflows
- `.codex/hooks.json` for optional experimental hooks
- local evals under `evals/`
- GitHub validation workflows that mirror the local checks
- starter-kit adapters and command contracts for Godot, Unity, and Unreal

## Supported operating model

- root instructions stay concise
- review policy lives in dedicated docs
- evals guard shared behavior changes
- hooks are opt-in
- Docker is optional, not mandatory
- engine parity is defined at starter-kit and adapter level, not by pretending all three engines share the same runtime files

## What to customize first

1. `.github/CODEOWNERS`
2. `studio/docs/active/engine-profile.md`
3. `studio/docs/active/game-brief.md`
4. `studio/docs/active/current-sprint.md`
5. `.env` if you actually need integrations

## Helpful local commands

```bash
make ci-local
python3 scripts/codex_studio.py engine --list --json
python3 scripts/run_local_evals.py
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine unity-6 --platform pc-premium --genre tactical-rpg
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine unreal-5 --platform console-premium --genre co-op-survival
python3 scripts/starter_kit_contract_smoke.py --engine godot-4 --json
python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --unity-path tools/engine-stubs/unity/Unity --dry-run --json
python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path tools/engine-stubs/unreal/RunUAT.sh --dry-run --json
python3 scripts/toggle_codex_hooks.py --status
```

## Related docs

- `docs/reference/code-review.md`
- `docs/reference/eval-strategy.md`
- `docs/setup/optional-codex-hooks.md`
- `docs/setup/github-maintainer-setup.md`
