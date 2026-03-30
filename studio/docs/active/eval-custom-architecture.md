# Eval Plan: Custom Architecture Routing

## Goal

Verify that custom architecture and custom rule-pack tasks surface the custom guide, example, and checklist layer before implementation starts.

## Scope

- project-specific architecture contracts
- custom rule packs and override points
- custom requests that need fixed versus overrideable rules

## Expected behavior

- The router should surface `docs/reference/custom-architecture.md` and `docs/examples/custom-architecture-example.md` for custom architecture or custom rule tasks.
- The checklist path should include `custom`, `architecture`, `quality`, and `research` layers so the owner, precedence, and proof path stay explicit.
- The custom lane should still reuse the standard architecture guide, not replace it.

## Validation

- run one route query for a custom-architecture prompt
- confirm the returned docs include the new custom guide and example
- confirm the checklist path includes the custom discipline
- confirm the custom guide explains fixed versus overrideable rules
- re-run the repo validation and local eval surface after routing changes

## Exit criteria

- custom architecture tasks are discoverable
- the examples index points to the new custom architecture example
- the router and checklist surface remain stable after the new context is added
