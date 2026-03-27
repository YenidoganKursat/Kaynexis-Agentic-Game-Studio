---
name: ui-flow
description: Design or implement one UI flow with screen states, transitions, copy needs, and validation. Use for menus, HUD flows, settings, or onboarding screens.
---

# UI Flow

## When to use
Design or implement one UI flow with screen states, transitions, copy needs, and validation. Use for menus, HUD flows, settings, or onboarding screens.

## Inputs to gather
- flow goal
- screen list
- input methods
- data/state requirements

## Recommended roles
- `ux_designer`
- `ui_artist`
- `ui_programmer`

## Primary docs / outputs
- `studio/docs/templates/feature-brief.md`
- `studio/docs/templates/accessibility-pass.md`

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
- flow map
- UI implementation plan
- copy/accessibility notes
- test checklist

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
