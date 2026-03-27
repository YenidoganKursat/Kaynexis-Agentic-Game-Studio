# Codex Game Studio Pro Max

A Codex-first multi-engine studio operating system for building games iteratively with durable repo state.

This repository is the planning, routing, checklist, research, validation, and starter-kit layer around a real game project. The sample Godot slice is only a reference proof, not the primary product. The primary product is the system that lets Codex and a human operator keep designing, validating, and shipping work across Godot, Unity, and Unreal without falling back to ad-hoc chat memory.

## What it includes

- One root config surface in `studio.toml`
- A front-door CLI in `python3 scripts/codex_studio.py`
- Codex-local agents in `.codex/agents/`
- Reusable skills in `.agents/skills/`
- Layered starter kits for `godot-4`, `unity-6`, and `unreal-5`
- Layered checklist manifests for base, engine, discipline, milestone, and custom rules
- Live project truth in `studio/docs/active/`
- Research-backed engine and production notes in `docs/research/game-development/`
- Engine-specific class/editor/object maps and agent guidance for Godot, Unity, and Unreal
- Validation, eval, CI, Docker, and GitHub governance surfaces

## Fastest start

Guided setup:

```bash
python3 scripts/codex_studio.py init
```

That flow lets you pick engine, platform, and genre, writes `studio.toml`, seeds active docs, and runs the shared validation path.

Direct setup:

```bash
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes
```

## Front-door workflow

Use the repo through these six modes first:

- `python3 scripts/codex_studio.py init`
- `python3 scripts/codex_studio.py next "Describe the next task"`
- `python3 scripts/codex_studio.py checklist --task "Describe the next task"`
- `python3 scripts/codex_studio.py research --category systems --title "Save loop architecture"`
- `python3 scripts/codex_studio.py doctor`
- `python3 scripts/codex_studio.py engine --list`

The legacy entry points still work:

- `scripts/start_game_studio.py` -> `init`
- `scripts/setup_repo.py` -> setup backend
- `scripts/route_task.py` -> `next`

## First 15 minutes

1. Run `python3 scripts/codex_studio.py init`
2. Open `studio.toml`
3. Open `studio/docs/active/game-brief.md`
4. Open `studio/docs/active/engine-profile.md`
5. Open `studio/docs/active/current-sprint.md`
6. Run `python3 scripts/codex_studio.py next "Describe the next gameplay or pipeline task"`
7. Run `python3 scripts/codex_studio.py checklist --task "Describe the same task"`
8. Run `python3 scripts/run_local_evals.py`

## Multi-engine support model

This repo uses starter-kit parity, not fake feature parity:

- Godot 4 starter kit: scene/script/export baseline plus smoke helpers
- Unity 6 starter kit: package/asmdef/test-command baseline
- Unreal 5 starter kit: project/module/package-command baseline

Inspect them with:

```bash
python3 scripts/codex_studio.py engine --list
python3 scripts/validate_engine_kits.py
```

## Checklist system

Checklist resolution is layered and deterministic:

1. `base`
2. `engine`
3. `discipline`
4. `milestone`
5. `custom`

Example:

```bash
python3 scripts/codex_studio.py checklist --task "Implement the first combat room"
```

Custom overrides live in `studio/checklists/custom/`.

## Research system

Research is now a durable part of the workflow instead of a side note.

- Engine notes: `docs/research/game-development/engines/`
- Agent guide: `docs/reference/engine-agent-guidelines.md`
- Production notes: `docs/research/game-development/production/`
- Policy: `docs/research/game-development/policy.md`
- Template: `docs/research/game-development/templates/research-note.md`

Scaffold a new note with:

```bash
python3 scripts/codex_studio.py research --category systems --title "Combat readability baseline"
```

## Validation surface

Common commands:

- `python3 scripts/codex_studio.py doctor`
- `python3 scripts/validate_engine_kits.py`
- `python3 scripts/run_local_evals.py`
- `make validate`
- `make ci-local`

Godot reference-slice validation:

- `python3 scripts/godot_smoke.py --static-only`
- `python3 scripts/godot_smoke.py`
- `python3 -m pytest -q tests/test_godot_surface.py`
- `python3 scripts/godot_export.py --preset "Linux/X11"`

Unity and Unreal adapter command generation:

- `python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --dry-run --json`
- `python3 scripts/unity_adapter.py build --project-path studio/starter-kits/unity-6/scaffold --dry-run --json`
- `python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --dry-run --json`

When local engine paths are configured, the same adapter entry points can run the real editor or packaging commands instead of only printing them.

## Repo map

```text
studio.toml
scripts/codex_studio.py
studio/starter-kits/
studio/checklists/
studio/docs/active/
docs/research/game-development/
.codex/agents/
.agents/skills/
```

## GitHub and ops

The repo includes `CODEOWNERS`, issue forms, PR template, CI workflows, contribution and security docs, eval fixtures, and Docker-based helper validation.

For maintainer setup, branch protection, and rulesets, use `docs/setup/github-maintainer-setup.md`.

## Environment

Start from `.env.example` if you need local tool paths or API keys.

An optional `.env.example` is included for local tooling and integrations. Start with `docs/setup/secrets-and-env.md` before creating a real `.env`.

## Optional Codex Hooks

Repo-local hooks are scaffolded but disabled by default because the Codex hooks feature is still experimental.

Enable them with:

```bash
make hooks-enable
```

Disable them with:

```bash
make hooks-disable
```

## Recommended Skill Entry Points

Use these first when the next move is unclear:

- `$studio-start`
- `$intake-router`
- `$project-radar`
- `$feature-brief`

## Optional Docker Helper Environment

This repo includes a lightweight Ubuntu 24.04 + Python container for users who want an isolated helper shell for the scripts and docs workflow.

Build and enter it with:

```bash
docker compose build
docker compose run --rm app
```

Inside the container, the repository is mounted at `/app`.

## Further Reading

- `codex-game-studio-v3-roadmap.md`
- `CHANGELOG.md`

## Notes

- This template is intentionally opinionated: broad coverage, but narrow execution slices.
- The nested `AGENTS.md` files let Codex behave differently in `src/`, `tests/`, `assets/`, `studio/docs/`, `prototypes/`, and `tools/`.
- The git hooks are optional, but recommended for teams using this repo seriously.
- Adapt the agent roster and skill set once your actual engine, platform, and production constraints become concrete.
