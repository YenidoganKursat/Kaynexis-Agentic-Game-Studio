# ADR Example

## Status
- Accepted

## Context
- The prototype needs upgrade choices between encounters, but permanent progression would distort short-loop combat tuning.

## Decision
- Keep run-state upgrades separate from durable progression.
- Upgrades earned inside a run reset at run end.
- Durable unlocks may expand future choice pools but cannot directly alter current combat math yet.

## Consequences
- Benefits:
  - combat tuning stays legible
  - reset value stays high
- Costs:
  - less long-term retention pressure in early slices
  - future migration work when durable unlocks arrive

## Rejected options
- Permanent stat upgrades from the first slice
- Mixing run rewards and profile rewards into one inventory table
