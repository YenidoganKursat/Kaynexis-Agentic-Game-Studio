# Eval Plan: Architecture Routing

## Goal

Verify that architecture-heavy tasks surface the new architecture guide, example, and checklist layer before implementation starts.

## Scope

- state ownership, authority, event flow, and projection tasks
- architecture decisions that affect save, UI, AI, combat, or engine structure
- agent examples for architecture-first planning

## Expected behavior

- The router should surface `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` for architecture-heavy tasks, and the guide diagrams should be visible in the review path.
- The checklist path should include `architecture`, `quality`, and `research` layers so the owner, boundary, and proof path stay explicit.
- Generic research tasks should still be able to land on the existing research path when the prompt is not architecture-heavy.

## Validation

- run one route query for an architecture-heavy prompt
- confirm the returned docs include the new architecture guide and example
- confirm the returned guide exposes the new diagrams
- confirm the checklist path includes the architecture discipline
- re-run the repo validation and local eval surface after routing changes

## Exit criteria

- architecture tasks are discoverable
- the examples index points to the new architecture example
- the router and checklist surface remain stable after the new context is added
