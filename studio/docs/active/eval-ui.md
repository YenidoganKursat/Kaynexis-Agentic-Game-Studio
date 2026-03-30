# Eval Plan: UI Routing and Template Guidance

## Goal

Verify that UI-heavy tasks surface the UI guide, UI example, and engine-specific UI notes, while keeping template-source and projection-boundary guidance visible.

## Scope

- HUD, menu, settings, pause, inventory, onboarding, and template-selection prompts
- controller-first navigation and focus-heavy UI tasks
- agent examples for stack choice, template source, and screen ownership

## Expected behavior

- The router should surface `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` for UI-heavy prompts.
- The router should also surface the matching engine UI note for Godot, Unity, or Unreal when the engine is explicit.
- The checklist path should require the agent to name the screen owner, projection boundary, focus model, and template source before implementation.
- The examples index should point to the UI example as a concrete template-selection and screen-ownership reference.

## Validation

- run one route query for a UI-heavy prompt
- confirm the returned docs include the UI guide, UI example, and matching engine UI note
- confirm the checklist path includes the `ui-ux` discipline and the UI-specific required items
- re-run the repo validation and local eval surface after routing changes

## Exit criteria

- UI-heavy tasks are discoverable
- the examples index points to the UI example
- the router and checklist surface remain stable after the new context is added
