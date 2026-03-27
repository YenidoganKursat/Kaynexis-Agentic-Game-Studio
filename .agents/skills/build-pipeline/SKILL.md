---
name: build-pipeline
description: Design or harden CI/build/package flows, environment assumptions, versioning, and artifacts. Use for reproducible builds and release engineering.
---

# Build Pipeline

## When to use
Design or harden CI/build/package flows, environment assumptions, versioning, and artifacts. Use for reproducible builds and release engineering.

## Inputs to gather
- target platforms
- current build path
- artifact needs
- branch/release flow

## Recommended roles
- `build_release_engineer`
- `technical_director`
- `qa_lead`

## Primary docs / outputs
- `studio/docs/templates/build-pipeline.md`
- `studio/docs/templates/release-checklist.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. If code changes are involved, keep the patch tight and validate the changed behavior.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Map the actual files/systems first, then choose the smallest viable implementation slice.
- Prefer reversible, reviewable patches over broad speculative refactors.
- Report commands, tests, and manual checks honestly.

## Deliverables
- pipeline plan
- artifact map
- automation steps
- failure recovery

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
