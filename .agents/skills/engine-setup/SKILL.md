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
- `docs/research/game-development/engines/*-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/*-2d-3d-navigation-damage-performance.md`
- `docs/research/game-development/systems/inventory.md`
- `docs/research/game-development/systems/character.md`
- `docs/research/game-development/systems/enemy.md`
- `docs/reference/agent-guide.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Read the matching engine architecture note, class/editor/object map, 2D/3D class-and-mechanic guide, and 2D/3D-navigation-damage-performance note before making structural recommendations.
3. If the task touches inventory, character state, or enemy behavior, read the matching systems note before suggesting ownership or data boundaries.
4. Choose the smallest useful output that moves the project forward.
5. Update or create durable docs when the result should persist.
6. Recommend the next best role or skill if more work remains.

## Category rules
- Inspect the repo, existing docs, and engine clues before asking for more information.
- Use minimal clarifying questions only when a missing fact blocks a good recommendation.
- Write or update durable docs when the output should survive chat history.

## Deliverables
- engine setup checklist
- repo/layout notes
- class/editor/object ownership model
- common 2D/3D class and mechanic primitives
- inventory, character, and enemy ownership boundaries when relevant
- world-stack, pathfinding, damage, and scale model
- version-sensitive cautions
- next implementation slice

## Validation bar
- updated active docs
- recommended next skill
- critical unknowns listed
