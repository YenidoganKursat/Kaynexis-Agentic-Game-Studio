# Eval Plan — Custom Packs

## Change under test

Add a dedicated custom pack lane for reusable project-specific feature bundles, manifests, and fallback behavior.

## Goal

Prove that the repo can route custom pack requests to a single registry-oriented structure without confusing them with the narrower custom architecture or extension pack lanes.

## Risks

- The pack lane could become a duplicate of custom architecture or extensions.
- The registry could become too broad if pack types are not kept narrow.
- Validation could drift if the guide, example, checklist, and active note do not stay synchronized.

## Validation

1. Route a custom pack request and confirm the custom pack docs appear first.
2. Render the custom packs checklist and confirm pack type, owner, fallback, and proof path are explicit.
3. Check that the example manifest demonstrates a durable registry row.

## Success criteria

- The custom pack lane is discoverable and distinct from the narrower lanes.
- The pack contract names fixed rules, override rules, hook points, and fallback behavior.
- The docs, checklist, and active note stay synchronized.
