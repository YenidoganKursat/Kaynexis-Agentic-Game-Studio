# ADR — Custom Packs as a Registry Layer

## Status
- Accepted

## Context
- The repo already has separate lanes for custom architecture and extension packs.
- Some work needs a higher-level registry for reusable feature bundles that can combine rules, hooks, manifests, and fallbacks.
- Without a registry layer, custom work tends to splinter into one-off notes.

## Decision
- Add a dedicated custom packs layer above the narrower custom architecture and extension pack lanes.
- Keep the pack contract explicit: pack id, pack type, owner, dependencies, fixed rules, override rules, hook points, override points, fallback, and validation path.
- Route broad custom feature bundle work to the custom packs lane first.

## Consequences
- Benefits
  - More reusable custom feature bundles
  - Clearer pack registry and fallback behavior
  - Easier routing and review for future custom features
- Costs
  - One more concept to maintain
  - A small amount of documentation and routing duplication
- Follow-up work
  - Keep the custom packs guide, example, checklist, and eval plan synchronized
  - Keep the narrower custom architecture and extension pack lanes distinct

## Rejected options
- Fold everything into the custom architecture lane
- Fold everything into the extension pack lane
- Keep custom feature bundles as chat-only notes
