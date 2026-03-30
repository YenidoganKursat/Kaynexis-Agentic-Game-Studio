# Eval Plan — Versioning Metadata

## Change under test
- Canonical version source of truth, changelog sync, and release tag policy.

## Goal
- Make sure the repo can tell the difference between a prerelease working tree and a release-ready tag.
- Keep the `VERSION` file, `CHANGELOG.md`, and build artifacts aligned.

## Benchmark cases
1. `VERSION` exists and matches the semantic version pattern.
2. A prerelease version keeps `## Unreleased` in `CHANGELOG.md`.
3. A release version requires a matching changelog heading.
4. CI artifact reports surface the current version.
5. Versioning commits include a subject and body that say what changed.

## Rubric
- `pass` when the version guard reports a valid status and no failures.
- `warn` when the changelog exists but the repo is still in prerelease mode.
- `fail` when the version string is malformed or the changelog does not match the version state.
- `warn` when versioning docs do not mention commit notes or the same commit-note contract as the changelog.

## Run notes
- `python3 scripts/version_guard.py --json`
- `python3 scripts/ci_artifact_report.py --output-dir build/ci/version --label version-check --json`
- `make version`
