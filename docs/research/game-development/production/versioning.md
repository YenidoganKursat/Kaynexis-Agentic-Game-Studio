# Versioning Contract

## Date
- 2026-03-29

## Summary
- Versioning is not just a label; it is the contract that ties together the current repo state, changelog history, release tags, and build provenance.
- This repo should treat the root `VERSION` file as the canonical working-tree version and keep `CHANGELOG.md` readable for humans.
- The simplest useful policy is `X.Y.Z-dev` for active development and `vX.Y.Z` for release tags.

## Primary sources
- [Semantic Versioning 2.0.0](https://semver.org/)
- [GitHub Releases documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Git tags reference](https://git-scm.com/docs/git-tag)

## Why this matters to this repo
- The studio OS already keeps docs, validations, and artifacts close together.
- Version drift makes release notes, rollback notes, and artifact provenance harder to trust.
- Versioning gives the agent a concrete thing to update before release readiness work lands.

## Decision impact
- Keep the root `VERSION` file as the source of truth for the working-tree version.
- Keep `CHANGELOG.md` aligned with that version state.
- Treat release tags as short canonical artifacts that should match the version family.
- Keep version data visible in the build pipeline and CI artifact report.
- Use the version guard before declaring a release-ready bundle complete.

## Commit notes
- Versioning commits should capture the version state and the exact surfaces changed.
- Prefer a subject that names the action and scope, plus a body that lists the version, changelog heading, tag policy, and release-note summary when several files move together.
- The commit note, changelog entry, and version file should tell the same story.

## Repo impact
- Version-aware release workflows can now read a single version source instead of guessing from branch names or release notes.
- The release checklist should point at the same version contract as CI and the changelog.
- The agent can now route version bumps, tag prep, and changelog sync to a dedicated checklist bundle.
- The versioning checklist and eval plan should stay in sync with the same commit-note contract so release history stays readable later.
- The commit-msg hook should mirror the same rule so versioning or release commits describe what changed before they land.
