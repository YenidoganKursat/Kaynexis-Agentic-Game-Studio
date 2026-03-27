# Codex Compatibility

This repository is intentionally shaped around official Codex repo conventions.

## Codex-native surfaces in this repo

- `AGENTS.md` at the repo root, plus nested `AGENTS.md` files
- `.codex/config.toml` for shared project defaults
- `.codex/agents/` for focused custom agents
- `.agents/skills/` for reusable workflows
- `.codex/hooks.json` for optional experimental hooks
- local evals under `evals/`
- GitHub validation workflows that mirror the local checks

## Supported operating model

- root instructions stay concise
- review policy lives in dedicated docs
- evals guard shared behavior changes
- hooks are opt-in
- Docker is optional, not mandatory

## What to customize first

1. `.github/CODEOWNERS`
2. `studio/docs/active/engine-profile.md`
3. `studio/docs/active/game-brief.md`
4. `studio/docs/active/current-sprint.md`
5. `.env` if you actually need integrations

## Helpful local commands

```bash
make ci-local
python3 scripts/run_local_evals.py
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite
python3 scripts/toggle_codex_hooks.py --status
```

## Related docs

- `docs/reference/code-review.md`
- `docs/reference/eval-strategy.md`
- `docs/setup/optional-codex-hooks.md`
- `docs/setup/github-maintainer-setup.md`
