# Command Cheatsheet

## One-Time Setup

Guided setup:

```bash
python3 scripts/start_game_studio.py
```

Direct setup:

```bash
python3 scripts/setup_repo.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite
```

Seed a concrete active-doc baseline:

```bash
python3 scripts/seed_project_baseline.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite
```

Install git hooks manually:

```bash
./scripts/install_git_hooks.sh
```

## Health and Validation

Run the health check:

```bash
python3 scripts/doctor.py
```

Run the local eval corpus:

```bash
python3 scripts/run_local_evals.py
```

Validate the repo:

```bash
python3 scripts/validate_repo_layout.py
python3 scripts/validate_docs.py
python3 scripts/validate_assets.py
```

Or:

```bash
make validate
make ci-local
```

Godot slice validation:

```bash
python3 scripts/godot_smoke.py --static-only
python3 scripts/godot_smoke.py
python3 -m pytest -q tests/test_godot_surface.py
```

Godot export:

```bash
python3 scripts/godot_export.py --preset "Linux/X11"
python3 scripts/godot_export.py --preset "Windows Desktop"
```

Print studio status:

```bash
python3 scripts/studio_status.py
```

## Docs and Presets

Bootstrap active docs:

```bash
python3 scripts/bootstrap_studio.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite
```

Replace the preset pack:

```bash
python3 scripts/apply_preset.py --engine godot-4 --platform pc-premium --genre action-roguelite --replace
```

## Routing and Planning

Find the likely workflow for a task:

```bash
python3 scripts/route_task.py "Add aim assist tuning for controller combat"
```

Scan for top gaps:

```bash
python3 scripts/project_radar.py --warn-only
```

## Scaffolding

Feature brief + ADR + test plan:

```bash
python3 scripts/scaffold_feature.py "Core Combat" --with-adr --with-test-plan
```

Bug triage docs:

```bash
python3 scripts/scaffold_bugfix.py "Save Corruption After Alt-F4"
```

QA matrix:

```bash
python3 scripts/generate_qa_matrix.py "Vertical Slice"
```

Eval plan:

```bash
python3 scripts/scaffold_eval_plan.py "Reviewer Prompt Refresh"
```

## Make Targets

Show the target list:

```bash
make help
```

Common targets:

- `make setup`
- `make start`
- `make baseline`
- `make doctor`
- `make evals`
- `make validate`
- `make ci-local`
- `make test`
- `make godot-smoke`
- `make godot-smoke-strict`
- `make export-linux`
- `make export-windows`
- `make status`
- `make radar`
- `make route TASK="..."`
- `make feature FEATURE="..."`
- `make bug BUG="..."`
- `make qa QA_TITLE="..."`
- `make eval EVAL_TITLE="..."`
- `make hooks-enable`
- `make hooks-disable`
- `make docker-verify`

## Optional Docker Commands

Build the helper container:

```bash
docker compose build
```

Open a shell in the helper container:

```bash
docker compose run --rm app
```
