# Unity

## Date
- 2026-03-27

## Summary
- Unity’s docs treat package layout and assembly definition boundaries as core organizational tools, with the test framework and batchmode test execution forming the baseline automation surface.
- The repo implication is to document package and asmdef boundaries even before the real editor binary is wired in CI, so structure and intended commands remain deterministic.

## Primary sources
- [Unity custom package layout](https://docs.unity3d.com/Manual/cus-layout.html)
- [Unity Test Framework command line](https://docs.unity3d.com/Packages/com.unity.test-framework%402.0/manual/reference-command-line.html)

## Why this matters to this repo
- The Unity starter kit should ship with `Packages/manifest.json`, a project version file, and a documented code root.
- Validation should focus on structural contracts first: packages, asmdef boundaries, and test/build commands.
- Build-pipeline docs should record the intended Unity batchmode commands even if the editor remains external.

## Decision impact
- Keep the Unity starter kit package-aware and asmdef-first.
- Add Unity-specific checklist items for package drift and CLI command documentation.
- Treat Unity CLI paths as config in `studio.toml`, not scattered shell snippets.
