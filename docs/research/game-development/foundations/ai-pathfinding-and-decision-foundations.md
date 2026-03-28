# AI, Pathfinding, and Decision Foundations

## Date
- 2026-03-28

## Summary
- Pathfinding and decision architectures should be chosen for the representation they need, the debugging story they allow, and the entity scale they can sustain, not because a technique is fashionable.
- Classical heuristic search such as A* remains the baseline for many game navigation problems because it is understandable, tunable, and predictable.
- Hierarchical approaches become valuable when map scale, repeated routing, or large numbers of agents make flat search too expensive.
- Behavior Trees remain useful because they are debuggable and author-friendly. GOAP or planner-style approaches become useful when the design space is about flexible goal pursuit and combinatorial action selection rather than fixed encounter scripts.

## Primary sources
- Hart, Nilsson, and Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths" — https://ieeexplore.ieee.org/document/4082128/
- Botea, Muller, and Schaeffer, "Near Optimal Hierarchical Path-Finding" — https://citeseerx.ist.psu.edu/document?doi=33e4258aef9ededfffd811aae5bc72c195460204&repid=rep1&type=pdf
- Iovino et al., "A Survey of Behavior Trees in Robotics and AI" — https://arxiv.org/abs/2005.05842
- Orkin, "Agent Architecture Considerations for Real-Time Planning in Games" — https://static.hlt.bme.hu/semantics/external/pages/GOAP/alumni.media.mit.edu/_jorkin/aiide05OrkinJ.pdf
- Orkin, "Goal-Oriented Action Planning: Ten Years Old and No Fear" — https://www.gdcvault.com/play/1022019/Goal-Oriented-Action-Planning-Ten

## Why this matters to this repo
- The repo already supports multiple engines and multiple genres, so AI decisions need to travel across engines without collapsing into "just use NavMesh plus a behavior tree" every time.
- A durable studio system needs reasoning that survives implementation details. This note gives that reasoning a neutral layer above Godot nodes, Unity components, or Unreal actors.
- It also keeps Codex from recommending heavyweight AI stacks where a deterministic scripted behavior or small heuristic controller would be faster, cheaper, and easier to debug.

## Decision impact
- Tasks involving navigation, pursuit, patrols, planners, formations, or encounter AI should surface both engine-specific notes and this foundational note.
- Feature briefs should state the scale assumption explicitly: number of agents, navigation graph complexity, update rate, and debugging needs.
- Performance and gameplay checklists should ask whether the chosen representation is overbuilt relative to the problem.

## Practical framing
- Use heuristic search when:
  - the navigation problem is spatial, explicit, and reasonably bounded
  - designers need predictable route behavior
  - debugging path quality matters more than dynamic plan expressiveness
- Use hierarchical pathfinding when:
  - the world is large or repeatedly traversed
  - many agents need approximate but good-enough routes
  - routing cost dominates encounter scale
- Use Behavior Trees when:
  - designers need readable and inspectable decision logic
  - encounter scripting and stateful reactions matter
  - the team benefits from strong debugging and authoring structure
- Use GOAP or planner-style systems when:
  - the design depends on flexible goal pursuit and action recombination
  - authored branching logic would otherwise explode combinatorially
  - world state and action preconditions are central to the fantasy

## What to watch out for
- Do not adopt planner-style systems if the action space is tiny or fixed. The overhead and debugging burden often outweigh the gain.
- Do not treat pathfinding and decision-making as one problem. A strong path system does not solve tactical choice, and a strong decision system does not solve navigation scale.
- Many AI failures come from stale world state, update frequency mismatches, or bad debugging tools rather than from the core algorithm.
- If the team cannot inspect the reason an agent chose an action or route, the system is probably too opaque for production use.
