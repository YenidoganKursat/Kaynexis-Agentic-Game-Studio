# World Graph Example

## Canon scope
- The world graph covers the Vale frontiers, their factions, the guild network, key landmarks, and the major history beats that explain why the frontier is politically unstable.
- It does not store short-lived quest flags or conversation-local state.

## Node types
- Characters
- Factions
- Organizations
- Locations
- Artifacts
- Events

## Edge types
- Member of
- Allied with
- Rival of
- Located in
- Owns
- Witnessed
- Created
- Inherited

## History rules
- The fall of Red Forge is append-only.
- Minor tone rewrites are allowed for prose, but the causal event id stays stable.
- The world state snapshot for the current chapter is derived from the event trail.

## Query needs
- Current faction allegiance must be fast to read during dialogue.
- Nearby relationship context must be fast to read for a codex screen.
- The map overlay should not traverse the full graph every frame.

## Ownership
- Canon is owned by the narrative director.
- Runtime relationship changes are owned by quest and event systems.
- Presentation is owned by UI and codex screens.

## Implementation notes
- Save/load persists discovered graph nodes and any runtime relationship deltas.
- Localization changes prose only.
- Dialogue and quest logic read the graph, but do not redefine canonical edges.
