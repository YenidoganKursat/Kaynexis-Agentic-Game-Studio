# Engine Installation

Use this guide when you need a real engine install, a durable team default, or a clear contract-smoke fallback for Godot 4, Unity 6, or Unreal 5.

If you only need repo structure validation, the stub commands in `docs/setup/quick-access.md` are enough. If you want editor-backed validation or release-grade packaging, install the real engine and wire the matching path into the repo.

## What counts as installed here

| Engine | Minimum install | Team default path | Contract smoke | Editor-backed validation |
| --- | --- | --- | --- | --- |
| Godot 4 | Official stable 4.x binary or package-manager install | `GODOT_BIN` | `python3 scripts/godot_smoke.py --static-only` | `python3 scripts/godot_smoke.py` and `python3 scripts/godot_export.py --preset "<preset>"` |
| Unity 6 | Unity Hub plus a stable 6000.x editor | `UNITY_CLI` | `python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --unity-path tools/engine-stubs/unity/Unity --dry-run --json` | `python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --unity-path "$UNITY_CLI" --dry-run --json` |
| Unreal 5 | Epic Games Launcher plus a stable 5.x editor or source build | `UNREAL_EDITOR` / `UNREAL_UAT` | `python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path tools/engine-stubs/unreal/RunUAT.sh --dry-run --json` | `python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path "$UNREAL_UAT" --platform Win64 --dry-run --json` |

## Godot 4

- Install the current stable 4.x build from the official Godot download page.
- Use the package manager only if it still gives you a stable binary that matches the current project contract.
- Set `GODOT_BIN` when the binary is not already on `PATH`.
- Keep runtime/export validation separate from static repo validation.

Good default checks:

```bash
python3 scripts/godot_smoke.py --static-only
python3 scripts/godot_smoke.py
python3 scripts/godot_export.py --preset "Linux/X11"
```

## Unity 6

- Install Unity Hub first, then install a stable 6000.x editor through Hub.
- Add only the modules you actually need for the target platforms.
- Set `UNITY_CLI` if you want the repo to point at a specific editor binary.
- Treat the stub path as contract smoke only.

Good default checks:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --unity-path tools/engine-stubs/unity/Unity \
  --dry-run --json
```

For editor-backed validation, replace the stub path with `"$UNITY_CLI"`.

## Unreal 5

- Install Epic Games Launcher, then add a stable Unreal 5.x editor or a source build.
- Install the platform SDKs needed for the target family before expecting packaging to work.
- Set `UNREAL_EDITOR` or `UNREAL_UAT` when you want the repo to point at a real local install.
- Treat the stub path as contract smoke only.

Good default checks:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

For engine-backed packaging, replace the stub path with `"$UNREAL_UAT"` and use the target platform you actually ship.

## Installation rules

1. Match the engine family to `studio.toml` and the active docs.
2. Prefer stable editor installs for release-bound validation.
3. Use contract smoke only when the real engine is intentionally unavailable.
4. Keep engine paths in `.env` for local overrides or `studio.toml` for durable team defaults.
5. Do not assume every contributor has every engine installed.
6. Keep the current project layout, starter kit, and build pipeline aligned with the actual install.

## Environment variables

- `GODOT_BIN`
- `UNITY_CLI`
- `UNREAL_EDITOR`
- `UNREAL_UAT`

These are optional local tool paths, not secrets.

## Validation

Run these after a new install or a path change:

```bash
python3 scripts/doctor.py
python3 scripts/validate_engine_kits.py
make validate
python3 scripts/run_local_evals.py
```

If you are switching engines or changing the setup contract, also re-check `studio/docs/active/engine-profile.md` and `studio/docs/active/build-pipeline.md`.

## Primary sources

- [Godot download page](https://godotengine.org/download/)
- [Unity download and Hub entry point](https://unity.com/download)
- [Unreal install docs](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine)
- [Engine selection guide](../reference/engine-selection-guide.md)
- [Engine map](../reference/engine-map.md)
- [Engine fit](../reference/engine-fit.md)

## Related docs

- [Getting Started](getting-started.md)
- [Quick Access](quick-access.md)
- [First Hour Walkthrough](first-hour-walkthrough.md)
- [Troubleshooting](troubleshooting.md)
- [Engine Selection Guide](../reference/engine-selection-guide.md)
- [Engine Map](../reference/engine-map.md)
- [Engine Fit](../reference/engine-fit.md)
