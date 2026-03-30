# Version Guide

## Summary
- `VERSION` is the canonical repo version file.
- `CHANGELOG.md` is the human-readable history.
- Release tags should use `vX.Y.Z`.
- Prerelease builds stay explicit with a suffix such as `-dev` until a tag is cut.

## Primary sources
- [Semantic Versioning 2.0.0](https://semver.org/)
- [GitHub Releases documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Git tags reference](https://git-scm.com/docs/git-tag)

## Why this matters to this repo
- Version drift makes build provenance, release notes, and rollback steps harder to trust.
- The studio OS already keeps docs, workflows, and artifacts close together; versioning should do the same.
- Agents need one obvious place to read before changing release metadata.

## Decision impact
- Root `VERSION` is the source of truth for the current working-tree version.
- `CHANGELOG.md` should keep the release story readable for humans.
- Release bundles should read the same version string that the repo exposes.
- Release tags should stay short, canonical, and aligned with the root version.

## Commit messages
- Versioning and release-scoped commits should say what changed in the subject and, when more than one surface moves, a short body with `What changed:` bullets.
- Use an action-first subject with a scope, for example `feat(versioning): record the release-note summary for 2.1.0-dev`.
- Keep the commit note aligned with the changelog entry so the version file, changelog, and git history tell the same story.
- If the commit only bumps metadata, say so explicitly and name the target version or tag family.

## Version states
- `X.Y.Z-dev` or similar prerelease suffix: active development, not a final tag.
- `vX.Y.Z`: release tag form for shipped or demoed artifacts.
- If the repo is in prerelease mode, `CHANGELOG.md` should keep `## Unreleased` at the top.
- If the repo is in release mode, the changelog should include the matching `## vX.Y.Z` heading.

## Example prompts for the agent
- "Bump the repo to the next dev version and keep VERSION and CHANGELOG in sync."
- "Prepare the version tag policy for the first external demo."
- "Write commit notes that say what changed for the version bump and keep the changelog aligned."
- "Check whether the current changelog and version file disagree."

## Validation
- `python3 scripts/version_guard.py --json`
- `make version`
- `make ci-local`
- `.githooks/commit-msg` should reject versioning or release commits that do not describe what changed.

## Related docs
- `docs/examples/version-example.md`
- `docs/research/game-development/production/versioning.md`
- `docs/research/game-development/production/release-validation.md`
- `studio/checklists/discipline/versioning.toml`
- `studio/docs/active/eval-versioning.md`
- `docs/reference/ci-cd.md`
- `docs/reference/feature-traceability.md`
- `studio/docs/templates/release-checklist.md`
