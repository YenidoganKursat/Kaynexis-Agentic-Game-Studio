---
name: engine-setup
description: Audit or frame engine-specific project setup, folder conventions, packages/plugins, and build assumptions. Use for Godot, Unity, or Unreal setup and repo structure decisions.
---

# Engine Setup

## When to use
Audit or frame engine-specific project setup, folder conventions, packages/plugins, and build assumptions. Use for Godot, Unity, or Unreal setup and repo structure decisions.

## Inputs to gather
- engine and version
- repo structure
- target platforms

## Recommended roles
- `technical_director`
- `engine_programmer`
- `docs_researcher`

## Primary docs / outputs
- `studio/docs/active/engine-profile.md`
- `studio/docs/active/build-pipeline.md`
- `docs/research/game-development/engines/*-architecture.md`
- `docs/research/game-development/engines/*-class-editor-object-map.md`
- `docs/research/game-development/engines/*-2d-3d-navigation-damage-performance.md`
- `docs/reference/engine-agent-guidelines.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Read the matching engine architecture note, class/editor/object map, and 2D/3D-navigation-damage-performance note before making structural recommendations.
3. Choose the smallest useful output that moves the project forward.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Inspect the repo, existing docs, and engine clues before asking for more information.
- Use minimal clarifying questions only when a missing fact blocks a good recommendation.
- Write or update durable docs when the output should survive chat history.

## Deliverables
- engine setup checklist
- repo/layout notes
- class/editor/object ownership model
- world-stack, pathfinding, damage, and scale model
- version-sensitive cautions
- next implementation slice

## Validation bar
- updated active docs
- recommended next skill
- critical unknowns listed
