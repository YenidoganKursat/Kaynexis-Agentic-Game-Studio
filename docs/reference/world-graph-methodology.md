# World Graph Methodology

Use this when a game needs a durable relationship and history layer for characters, factions, organizations, locations, items, events, timelines, lineage, social graphs, or map-linked world state.

## What a world graph is in this repo
- A world graph is a canonical relationship map, not a story dump.
- It connects authored facts, runtime deltas, and presentation projections.
- It should stay narrower than the full lorebook and more structured than a one-off quest brief.

## Core rule
- The world graph defines durable relationship truth.
- Runtime systems own live changes such as alignment shifts, discoveries, temporary control, and player-specific knowledge.
- UI, dialogue, quest, and codex layers render projections of the graph; they do not become the authority for canon.

## Recommended workflow
1. Define the canon scope.
2. List the node types.
3. List the edge types and ownership rules.
4. Decide which history is append-only and which is snapshot-backed.
5. Define the common read path and cache or projection strategy.
6. Specify save/load and localization rules.
7. Write the brief, checklist, and validation path before implementation.

## Good world graph entry shape
- stable id
- node type
- title
- summary
- canonical attributes
- incoming and outgoing edges
- history events
- runtime projection
- revision
- owner

## Node and edge guidance
- Nodes should usually include characters, factions, organizations, locations, items, and events.
- Edges should be typed and directional when ownership or causality matters.
- Prefer explicit relationships such as member_of, allied_with, rival_of, located_in, owns, witnessed, caused, or inherited.

## History rules
- Keep major history beats append-only when possible.
- If a state must be summarized, keep a snapshot plus the underlying event trail.
- Store revisions when a canon fact changes so retcons stay auditable.

## Performance guidance
- Index by id and type first.
- Precompute common adjacency lists or filtered projections for gameplay and codex use.
- Cache common reads such as current faction stance, nearby relationship context, and local history windows.
- Avoid full-graph traversal every frame if a narrow projection or lookup table will do.

## What to avoid
- prose-only history that is never queryable
- relationship truth hidden only in dialogue or item text
- one giant graph blob with no typed edges
- full traversal on the hot path when a cached read would be cheaper
- mutable canon without a revision trail

## Validation questions
- Can the system answer who knows whom, who owns what, and what happened when?
- Can the common query run through a fast path?
- Can save/load restore both graph canon and runtime deltas?
- Can localization rewrite prose without breaking stable ids or edge types?

## Related docs
- `docs/reference/lorebook-methodology.md`
- `docs/research/game-development/narrative/world-graph.md`
- `docs/research/game-development/narrative/lorebook.md`
- `docs/examples/world-graph-example.md`
- `studio/docs/templates/world-graph-brief.md`
- `docs/research/game-development/systems/dialogue.md`
- `docs/research/game-development/systems/party.md`
