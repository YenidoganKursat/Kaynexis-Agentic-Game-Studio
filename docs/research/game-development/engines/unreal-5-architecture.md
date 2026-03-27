# Unreal 5 Architecture Baseline

## Date
- 2026-03-27

## Summary
- Unreal’s official guidance centers on explicit project structure, plugin/module boundaries, and deliberate packaging/release planning.
- The repo implication is to keep `Config/`, `Content/`, and `Source/` boundaries obvious, document package commands before scale, and treat module/plugin sprawl as an architecture issue rather than a cleanup task.

## Primary sources
- [Working with Plugins in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)
- [Sharing and Releasing Projects for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine)

## Why this matters to this repo
- The Unreal starter kit should be a text-first scaffold with a `.uproject`, config root, content root, and module skeleton.
- Validation should check boundary markers and documented package commands before pretending to offer full editor automation.
- Release docs should capture cook/package assumptions explicitly.

## Decision impact
- Keep the Unreal starter kit focused on module and packaging contracts.
- Add Unreal-specific checklist items for boundary clarity and package-command documentation.
- Document Unreal editor/build paths via `studio.toml` instead of embedding machine-specific commands in multiple docs.
