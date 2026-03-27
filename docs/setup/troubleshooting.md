# Troubleshooting

## `python3 scripts/codex_studio.py init` fails immediately

Check:

- Python is installed and is `3.11+`
- you are running the command from the repo root
- the repo was copied completely, including hidden folders such as `.codex/` and `.agents/`

Run:

```bash
python3 scripts/doctor.py
```

## Git hooks were not installed

The hook installer only works when `.git/` exists.

If the repo has not been initialized yet:

```bash
git init
./scripts/install_git_hooks.sh
```

Or run:

```bash
python3 scripts/setup_repo.py --init-git
```

## `project_radar.py` says the engine is unknown

That means the repo does not yet contain common engine clues such as:

- `project.godot`
- `Assets/` and `ProjectSettings/`
- `*.uproject`

Fix:

- update `studio/docs/active/engine-profile.md`
- add the real engine-native repo files when they exist

## Active docs still contain placeholders

Run setup again with the right metadata or edit the docs directly:

```bash
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --overwrite
```

If you only want to inspect the issue:

```bash
python3 scripts/studio_status.py
python3 scripts/doctor.py
```

## Docker commands fail

Check:

- Docker is installed
- Docker Desktop or the Docker daemon is running

Then retry:

```bash
docker compose build
docker compose run --rm app
```

## `python3 scripts/godot_smoke.py` says no Godot binary was found

Static validation still works without Godot:

```bash
python3 scripts/godot_smoke.py --static-only
```

If you want runtime smoke or exports, install Godot 4.x locally or point the repo to a binary:

```bash
export GODOT_BIN="/absolute/path/to/godot"
python3 scripts/godot_smoke.py
python3 scripts/godot_export.py --preset "Linux/X11"
```

## I only want the docs and scripts, not the Docker helper

That is fine. Docker is optional.

Use the native commands instead:

```bash
python3 scripts/codex_studio.py init --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite --yes
make validate
```

## `make` is not available

Use the Python script commands directly.
Everything exposed in the `Makefile` also has a direct `python3 scripts/...` equivalent.
