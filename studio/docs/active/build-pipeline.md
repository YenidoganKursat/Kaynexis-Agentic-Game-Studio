# Build Pipeline — kaynexisGame

## Build graph
- Source -> route/checklist/research alignment -> repo validation -> starter-kit validation -> local evals -> engine-native smoke -> package -> artifact -> distribution

## Environments
- Local: `make ci-local`
- Front door: `python3 scripts/codex_studio.py`
- CI: `.github/workflows/repo-validate.yml`
- Container check: `.github/workflows/docker-smoke.yml` and `make docker-verify`
- Release: add engine-native export jobs once the real project is wired

## Engine contracts
- Godot 4: `python3 scripts/godot_smoke.py --static-only`, optional runtime smoke, then `python3 scripts/godot_export.py --preset "..."`
- Unity 6: starter-kit structure plus documented batchmode test/build commands in active docs
- Unreal 5: starter-kit structure plus documented build/package commands in active docs

## Artifacts & versioning
- Keep artifact names deterministic
- Store release notes, validation commands, and build provenance alongside artifacts
- Add symbols or crash artifacts once the engine-specific build pipeline exists

## Failure / rollback
- If validation or evals regress, stop before merge
- If Docker or workflow changes break, revert the smallest change first
- Record release or infra regressions in `studio/docs/active/risk-register.md` and an eval plan when shared behavior changed
