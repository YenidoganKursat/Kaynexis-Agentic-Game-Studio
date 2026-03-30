# Release Validation Baseline

## Date
- 2026-03-27

## Summary
- Release readiness should be driven by deterministic commands, explicit artifact expectations, and known-issue visibility, even before full engine automation exists for every engine.
- That means the repo should unify local validation, evals, and workflow behavior before promising external build confidence.

## Primary sources
- [Godot project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)
- [Unity Test Framework command line](https://docs.unity3d.com/Packages/com.unity.test-framework%402.0/manual/reference-command-line.html)
- [Sharing and Releasing Projects for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine)

## Why this matters to this repo
- The same validations should run locally and in CI.
- Every engine starter kit should declare smoke/export expectations even if runtime binaries are external.
- Release docs should show known blockers and artifact locations clearly.

## Decision impact
- Keep `make validate` and GitHub Actions aligned.
- Add starter-kit validation to local CI.
- Extend route/checklist output to include validation steps and engine actions.
- Keep the versioning contract in sync with `docs/research/game-development/production/versioning.md`, `CHANGELOG.md`, and `VERSION` before calling a release bundle complete.
