# Getting Started

This guide is for the person setting up the repository for the first time.

## Prerequisites

Required:

- Python `3.11+`

Recommended:

- Git
- Node.js
- Codex CLI: `npm i -g @openai/codex`
- Docker if you want the optional container workflow

## Quick Setup

Simplest path:

```bash
python3 scripts/start_game_studio.py
```

Direct setup from the repo root:

```bash
python3 scripts/setup_repo.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite
```

What it does:

- bootstraps the active studio docs
- installs git hooks when `.git/` exists
- validates repo layout, docs, and assets
- runs a local doctor pass

## Make-Based Setup

If you prefer a shorter command surface:

```bash
make setup PROJECT_NAME="Your Game" ENGINE=godot-4 PLATFORM=pc-premium GENRE=action-roguelite
```

## After Setup

Read these in order:

1. `studio/docs/active/game-brief.md`
2. `studio/docs/active/genre-starter.md`
3. `studio/docs/active/engine-profile.md`
4. `studio/docs/active/current-sprint.md`
5. `docs/reference/repo-tour.md`
6. `docs/reference/code-review.md`
7. `docs/reference/eval-strategy.md`
8. `docs/reference/command-cheatsheet.md`

Then run:

```bash
python3 scripts/project_radar.py --warn-only
python3 scripts/route_task.py "describe your next task"
python3 scripts/run_local_evals.py
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite
```

## Recommended First Feature Flow

1. Bootstrap the repo.
2. Confirm engine, platform, genre, and current scope in active docs.
3. Route the first task.
4. Create a feature brief:

```bash
python3 scripts/scaffold_feature.py "Core Movement" --with-adr --with-test-plan
```

5. Generate a QA matrix before calling the slice done:

```bash
python3 scripts/generate_qa_matrix.py "Core Movement"
```

If `genre-starter.md` suggests a tighter first slice for your chosen genre, prefer that over a broader generic first task.

## If You Change Codex Behavior

Create an eval plan when the change affects shared instructions, agents, or routing logic:

```bash
python3 scripts/scaffold_eval_plan.py "Route Task Refresh"
```

Use this for changes to:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.agents/skills/**`
- shared scripts such as `route_task.py`, `setup_repo.py`, or `doctor.py`

## Optional Docker Workflow

The repo includes an optional Ubuntu 24.04 helper container.

Build it:

```bash
docker compose build
```

Open a shell inside it:

```bash
docker compose run --rm app
```

Inside the container the repo is mounted at `/app`.

## Readiness Check

You are in a good state when all of these are true:

- `python3 scripts/doctor.py` reports no failures
- `make validate` passes
- `python3 scripts/run_local_evals.py` passes
- `studio/docs/active/game-brief.md` reflects the real project
- `studio/docs/active/engine-profile.md` reflects the real engine and version
- `python3 scripts/project_radar.py --warn-only` produces only acceptable warnings
