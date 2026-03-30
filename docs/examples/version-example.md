# Version Example

Compare this example with `docs/reference/version-guide.md` and `docs/research/game-development/production/versioning.md` before you cut or bump a release version.

## Scope
- Keep the repo version, changelog, and tag policy aligned before a release cut.

## Baseline
- `VERSION` currently holds the canonical working-tree version.
- `CHANGELOG.md` keeps `Unreleased` at the top during active development.
- Release tags should stay in the `vX.Y.Z` family.

## Decision order
1. Decide whether the work is still prerelease or ready for a release tag.
2. Update `VERSION` first.
3. Update `CHANGELOG.md` so the new state is obvious to humans.
4. Run the version guard and keep any release notes or build artifacts in sync.
5. Only tag once the release checklist and build evidence agree.

## Ready-made version bundles
- Dev bump: `2.1.0-dev` plus an `Unreleased` changelog section.
- Release cut: `2.1.0` plus a matching changelog heading and release note.
- Hotfix cut: a patch bump with the same changelog and tag policy.

## Commit notes
- Subject: `feat(versioning): record release-note summary for 2.1.0-dev`
- Body:

```text
What changed:
- updated VERSION to 2.1.0-dev
- added changelog bullets for the new agent-role checklist packs
- kept tag policy and release notes aligned
```

## Good agent prompts
- "Bump the repo to 2.1.0-dev and keep the release metadata aligned."
- "Prepare the first release tag policy and show how the changelog should change."
- "Write commit notes that describe what changed in the version bump."
- "Check whether VERSION, CHANGELOG.md, and the release checklist are consistent."

## Validation
- `python3 scripts/version_guard.py --json`
- `make version`
- `python3 scripts/ci_artifact_report.py --output-dir build/ci/version --label version-check --json`
