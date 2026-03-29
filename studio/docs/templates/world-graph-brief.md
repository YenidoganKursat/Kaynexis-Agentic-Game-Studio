# World Graph Brief — {WORLD_GRAPH_NAME}

## Canon scope
- Which world entities belong in this graph?
- Which relationships are in scope?
- Which history events must be queryable?

## Node types
- Characters
- Factions
- Organizations
- Locations
- Items
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
- What is append-only?
- What may be revised?
- What needs a snapshot?

## Query needs
- What must be fast at runtime?
- What should be precomputed?
- What should be cached?

## Ownership
- Which system owns canon?
- Which system owns runtime changes?
- Which system owns presentation?

## Implementation notes
- Save/load implications
- Localization concerns
- UI / quest / lorebook integration
