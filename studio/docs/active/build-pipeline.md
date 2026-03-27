# Build Pipeline — kaynexisGame

## Build graph
- Source -> repo validation -> local evals -> Godot static smoke -> pytest -> optional runtime smoke -> export -> artifact -> distribution

## Environments
- Local: `make ci-local`
- Local engine smoke: `make godot-smoke`
- Local automated tests: `make test`
- Local exports: `make export-linux` and `make export-windows`
- CI: `.github/workflows/repo-validate.yml`
- Container check: `.github/workflows/docker-smoke.yml` and `make docker-verify`
- Release: use `scripts/godot_export.py` once a Godot 4.x binary is available on the machine or runner

## Artifacts & versioning
- Keep artifact names deterministic
- Linux export path: `build/linux/kaynexisGame.x86_64`
- Windows export path: `build/windows/kaynexisGame.exe`
- Store release notes, validation commands, and build provenance alongside artifacts
- Add symbols or crash artifacts once the engine-specific build pipeline exists

## Failure / rollback
- If validation or evals regress, stop before merge
- If Godot export fails, rerun `python3 scripts/godot_smoke.py --json --static-only` before changing scene logic
- If Docker or workflow changes break, revert the smallest change first
- Record release or infra regressions in `studio/docs/active/risk-register.md` and an eval plan when shared behavior changed
