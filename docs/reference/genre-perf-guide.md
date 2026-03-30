# Genre Perf Guide

Use this guide when the bottleneck is shaped more by the genre than by the engine.

The rule is simple: name the genre family, decide the dominant pressure, choose the first genre lever, and only then pick the engine-specific tuning path.

## Summary

- This guide turns genre research into a performance order of operations.
- It exists because city-builders, survivorlikes, factories, strategy games, stealth games, and narrative-heavy games all fail first for different reasons.
- The repo should not give the same first optimization advice to every genre.

## Primary sources

- [Genre Guide](../research/game-development/genre/genre-guide.md)
- [Genre Maturity](../research/game-development/genre/genre-maturity.md)
- [Genre Patterns](../research/game-development/genre/genre-patterns.md)
- [Genre Examples](../research/game-development/genre/genre-examples.md)
- [Perf Guide](./perf-guide.md)
- [Godot performance note](../research/game-development/engines/godot-performance.md)
- [Unity performance note](../research/game-development/engines/unity-performance.md)
- [Unreal performance note](../research/game-development/engines/unreal-performance.md)

## Why this matters to this repo

- Genre-specific performance problems are often structural, not accidental.
- If the agent optimizes the wrong layer first, we get faster wrongness instead of a better slice.
- The repo needs a guide that tells the agent whether the real issue is entity density, simulation tick cost, state compression, UI virtualization, replication pressure, or traversal/perception overhead.

## Decision impact

- Performance tasks should name the genre family before implementation.
- The first lever should come from the genre bottleneck, not from a generic engine habit.
- Engine-level optimizations still matter, but only after the genre-shaped bottleneck is identified.

## How to use this guide

1. Identify the genre family.
2. State the dominant pressure in that genre.
3. Pick the smallest lever that can prove or disprove the bottleneck.
4. Keep readability, fairness, and recovery intact while tuning.
5. Escalate to engine-specific batching, pooling, instancing, or data-oriented paths only if the measurement proves it.

## Genre families

### Swarm / pressure loops

Examples: action roguelite, survivorlike, hero-shooter

- First lever: cap active entities and pool repeated objects.
- Second lever: separate visuals from simulation and cull off-screen work.
- Watch first: projectile churn, hit/contact cost, and clutter before combat logic.
- Avoid: jumping to ECS, Mass, or a data-oriented rewrite before entity density is proven to be the bottleneck.

### Simulation / management

Examples: city-builder, colony-sim, factory-automation, grand-strategy

- First lever: chunk simulation, batch events, and update dirty regions only.
- Second lever: virtualize or compress UI state that grows with the simulation.
- Watch first: sim tick cost, pathing cost, and full-world redraws before visuals.
- Avoid: simulating inactive regions at full fidelity or recomputing the whole campaign every frame.

### Route / state / narrative

Examples: deckbuilder-roguelike, tactical-rpg, narrative-adventure, cozy-sim, life-sim

- First lever: diff runtime state instead of rebuilding it.
- Second lever: compress branch state, save projections, and derived UI state.
- Watch first: state bloat, branch explosion, and UI recomputation before content breadth.
- Avoid: letting authored text or dialog scripts own runtime authority.

### Traversal / stealth / puzzle

Examples: stealth, metroidvania, platformer, puzzle

- First lever: cache perception, visibility, room state, and gate state.
- Second lever: simplify collision, nav, and restart cadence before scale work.
- Watch first: global simulation when the player only touches a local slice.
- Avoid: making every room or guard process the whole world every frame.

### Networked sessions

Examples: co-op-survival, extraction-lite, hero-shooter

- First lever: clarify authority, replication frequency, and interest management.
- Second lever: pool repeated net events and keep prediction budgets explicit.
- Watch first: replication overhead and ownership ambiguity before combat scale.
- Avoid: actor-per-entity replication without a clear contract.

## What to decide first

Before touching implementation, an agent should state:

1. the genre family
2. the dominant pressure
3. the baseline measurement or reproducible spike
4. the likely bottleneck class
5. the first genre lever to try
6. the fallback lever if the first one does not move the needle

## Preferred order of operations

When the task is "make the genre faster," prefer this order:

1. protect readability, fairness, and recovery first
2. reduce the genre's dominant scale cost
3. batch, pool, cache, or chunk repeated work
4. virtualize state or UI if the surface outgrows the screen
5. move to engine-specific large-scale systems only when measurement proves the need

If the genre lever still leaves the bottleneck in spatial partitioning, culling, batching, instancing, job systems, or state compression, escalate to `docs/reference/advanced-perf-guide.md` before reaching for a larger architecture rewrite.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Run a performance pass on a survivorlike and cap active enemies before changing combat logic"
python3 scripts/codex_studio.py next "Run a performance pass on a city-builder and chunk simulation before adding more AI detail"
python3 scripts/codex_studio.py next "Run a performance pass on a factory-automation game and trace throughput bottlenecks before increasing machine count"
python3 scripts/codex_studio.py next "Run a performance pass on a grand-strategy game and batch campaign state before adding more diplomacy"
python3 scripts/codex_studio.py next "Run a performance pass on a co-op survival game and tighten replication ownership before changing combat"
python3 scripts/codex_studio.py next "Run a performance pass on a stealth game and cache visibility before adding patrol complexity"
```

## Validation

When the agent is done, it should report:

- the genre family
- the baseline
- the first genre lever tried
- the before and after measurement
- the reason the chosen path beat the alternatives

## Related docs

- `docs/reference/perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/examples/perf-example.md`
- `docs/examples/advanced-perf-example.md`
- `docs/examples/genre-perf-example.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`
- `docs/research/game-development/engines/godot-performance.md`
- `docs/research/game-development/engines/unity-performance.md`
- `docs/research/game-development/engines/unreal-performance.md`
