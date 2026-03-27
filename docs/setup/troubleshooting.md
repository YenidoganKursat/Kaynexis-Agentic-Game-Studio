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

## `python3 scripts/unity_adapter.py ...` says no Unity binary was found

Contract smoke still works with the repo-local stub:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --unity-path tools/engine-stubs/unity/Unity \
  --dry-run --json
```

If you want editor-backed Unity validation or builds, point the repo to a real Unity executable:

```bash
export UNITY_CLI="/absolute/path/to/Unity"
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --unity-path "$UNITY_CLI" \
  --dry-run --json
```

## `python3 scripts/unreal_adapter.py ...` says no Unreal tool path was found

Contract smoke still works with the repo-local stub:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

If you want engine-backed packaging, point the repo to a real Unreal path:

```bash
export UNREAL_UAT="/absolute/path/to/RunUAT.sh"
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path "$UNREAL_UAT" \
  --platform Win64 \
  --dry-run --json
```

## I only want the docs and scripts, not the Docker helper

That is fine. Docker is optional.

Use the native commands instead:

```bash
python3 scripts/codex_studio.py init --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite --yes
make validate
```

You can swap `--engine godot-4` for `unity-6` or `unreal-5`.

## `make` is not available

Use the Python script commands directly.
Everything exposed in the `Makefile` also has a direct `python3 scripts/...` equivalent.
