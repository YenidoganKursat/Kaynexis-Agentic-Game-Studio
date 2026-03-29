# Metroidvania Architecture

## Date
- 2026-03-28

## Summary
- Metroidvanias fail first on traversal memory and gating clarity. The genre lives or dies on whether the player can understand where abilities matter, what changed in the world, and why returning to older spaces feels rewarding rather than tedious.
- The dominant loop is:
  - explore and read the space
  - hit a gate
  - earn a mobility or combat unlock
  - re-interpret older spaces with new capabilities
  - push into deeper territory
- The first systems that usually break are:
  - unclear traversal ability affordances
  - map or gating ambiguity
  - save/checkpoint friction
  - backtracking that feels like dead travel instead of meaningful recontextualization
- This genre needs deliberate architecture for:
  - traversal ability state
  - room or world gating metadata
  - checkpoint/save rhythm
  - map discovery state
  - combat/traversal overlap
  - content reuse across re-visits

## Primary sources
- [Metroid Dread - Nintendo Official Site](https://metroid.nintendo.com/dread/)
- [Metroid Dread on Nintendo Store](https://www.nintendo.com/us/store/products/metroid-dread/)
- [Hollow Knight official site](https://www.hollowknight.com/)

## Why this matters to this repo
- Metroidvania tasks should not be treated like ordinary platformer tasks. The key problem is usually gating architecture plus traversal-state readability, not just jump feel.
- Agents should explicitly state:
  - what new capability unlocks
  - what world metadata tracks the gate
  - how the player learns that old paths changed
  - where the save/checkpoint loop resets pressure
  - how combat and traversal share readability budget
- First slices should prove one meaningful recontextualized return path, not just one standalone obstacle room.

## Decision impact
- Future presets and docs should require:
  - one gating vocabulary
  - one traversal-state save model
  - one map/readability plan
  - one backtracking value test
- When a project selects this genre, route output should surface mechanic, level, save, and UI/map research together.
