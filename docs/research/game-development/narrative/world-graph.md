# World Graph

## Date
- 2026-03-29

## Summary
- Complex story-heavy games often need a world graph: a canonical graph of characters, factions, organizations, locations, items, events, and the relationships between them.
- The stable split is: authored content describes nodes and edges, runtime systems own state changes, and presentation layers render filtered slices of the graph for UI, dialogue, quests, and lore.
- A production-safe world graph can explain who knows whom, which faction owns what, which event happened when, and how that history should survive save/load, localization, and large-scale content growth.

## Primary sources
- [Neo4j graph data modeling concepts](https://neo4j.com/developer/graph-database/)
- [Neo4j graph data science / performance guidance](https://neo4j.com/product/graph-data-science/)
- [Yarn Spinner Variable Storage](https://docs.yarnspinner.dev/components/variable-storage/variable-storage)
- [Twine Cookbook Macros](https://twinery.org/cookbook/terms/terms_macros.html)
- [Twine Cookbook Style Guide](https://twinery.org/cookbook/style_guide.html)

## Why this matters to this repo
- The repo already has dialogue, lorebook, quest, party, and genre guidance. The world graph fills the missing structural layer that connects those systems into a single canonical relationship map.
- This matters for faction-based RPGs, investigative stories, relationship sims, grand strategy games, colony sims, and any game where history and social context are mechanically meaningful.
- Without this layer, teams tend to store relationships in dialogue flags, event scripts, or item descriptions that become impossible to audit at scale.

## Decision impact
- Use this note when the game needs a relationship graph, faction network, lineage map, organization chart, history log, event chronology, or social-web system.
- Tasks mentioning world graph, relationship graph, faction network, chronology, timeline, lineage, biography, organization, social graph, or history should surface this note.
- Feature briefs should say which nodes exist, which edges exist, which system owns each type of truth, and what the read path needs to be fast at runtime.

## Architecture guidance

### Model the world as nodes, edges, and events
- Use distinct node types for characters, factions, organizations, locations, items, and story events.
- Use explicit edge types for relationships such as allied_with, rival_of, member_of, located_in, owns, witnessed, created, inherited, or caused.
- Treat major history beats as events, not just text notes, so the graph can explain causality and chronology.

### Keep canon and runtime truth separate
- Canon should describe the relationship structure.
- Runtime should store changes such as approvals, betrayals, unlocked knowledge, or dynamic ownership.
- Presentation should render a filtered view of the graph, not become the source of truth.

### Use stable ids and type-safe edges
- Every node should have a stable id that survives rewrites and localization.
- Every edge should have a direction, a type, and a reason or timestamp when relevant.
- Avoid free-form relationships that cannot be queried later.

### Make history append-only where possible
- Histories are easier to audit when events are appended rather than overwritten.
- If a state must be summarized, keep a snapshot plus the underlying event trail.
- That gives the repo a recovery path after rewrites, retcons, or save migration.

### Optimize for fast lookup, not just expressive authoring
- Runtime should read the smallest useful slice of the graph for the current scene, quest, location, or faction view.
- Cache denormalized views for common queries such as:
  - current faction stance
  - party relationship changes
  - local location history
  - known connections for a codex screen
- Do not traverse the entire graph every frame if a narrow adjacency list or indexed projection will do.

### Keep authoring and review practical
- Authors should be able to add a node or edge without editing unrelated canon.
- Reviewers should be able to inspect one historical beat without loading the whole world bible.
- The content pipeline should validate ids, edge types, and missing references before the graph is considered usable.

## What to watch out for
- Relationship logic duplicated in dialogue, quest, and lorebook scripts
- A world graph that stores everything as one giant blob
- Chronology that can be rewritten without a revision trail
- Expensive traversal during gameplay when a cached view would be cheaper
- “History” living only in prose and never in queryable data

## Validation expectations
- A mature world graph support surface should be able to answer:
  - Which nodes are authoritative?
  - Which edges are allowed?
  - Which history events are append-only?
  - Which system owns runtime changes versus canon?
  - What is the fast path for the most common query?
- If those questions cannot be answered clearly, the graph is still only a concept sketch.

## Related references
- `docs/reference/world-graph-methodology.md`
- `docs/reference/lorebook-methodology.md`
- `docs/research/game-development/narrative/lorebook.md`
- `docs/research/game-development/systems/dialogue.md`
- `docs/research/game-development/systems/party.md`
- `docs/research/game-development/foundations/frameworks.md`
