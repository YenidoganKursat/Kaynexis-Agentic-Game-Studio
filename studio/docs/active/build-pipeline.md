# Build Pipeline — Kaynexis Agentic Game Studio

## Build graph
- Source -> route/checklist/research alignment -> repo validation -> starter-kit validation -> local evals -> engine-native smoke -> package -> artifact -> distribution

## Environments
- Local: `make ci-local`
- Front door: `python3 scripts/codex_studio.py`
- CI: `.github/workflows/repo-validate.yml`
- Starter-kit matrix: `.github/workflows/starter-kit-contracts.yml`
- Release gate bundle: `.github/workflows/release-readiness.yml`
- Nightly audit: `.github/workflows/nightly-audit.yml`
- Container check: `.github/workflows/docker-smoke.yml` and `make docker-verify`
- Adapter contract smoke: repo-local Unity/Unreal tool stubs keep dry-run checks honest in CI
- Release: real editor/export jobs only count as complete once engine binaries are present on the runner

## Engine contracts
- Godot 4: `python3 scripts/godot_smoke.py --static-only`, optional runtime smoke, then `python3 scripts/godot_export.py --preset "..."`
- Unity 6: the adapter auto-detects standard macOS Unity Hub installs when available; otherwise use `tools/engine-stubs/unity/Unity` for contract smoke only, or set a real `UNITY_CLI` path for editor-backed tests/builds
- Unreal 5: use `tools/engine-stubs/unreal/RunUAT.sh` for command-contract smoke; switch to a real `UNREAL_UAT` or `UNREAL_EDITOR` path for packaging work

## Artifacts & versioning
- Keep artifact names deterministic
- Store release notes, validation commands, and build provenance alongside artifacts
- Emit `build/ci/*` report bundles so CI failures have portable evidence instead of only console logs
- Add symbols or crash artifacts once the engine-specific build pipeline exists

## Failure / rollback
- If validation or evals regress, stop before merge
- If Docker or workflow changes break, revert the smallest change first
- Record release or infra regressions in `studio/docs/active/risk-register.md` and an eval plan when shared behavior changed
