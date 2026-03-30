# Cozy Sim

## Date
- 2026-03-29

## Summary
- Cozy sims fail first when routine becomes grind, when UI friction breaks the mood, or when the world does not visibly respond to the player's care.
- The dominant loop is:
  - perform a gentle daily routine
  - improve a place, home, or island
  - strengthen attachment to people or spaces
  - unlock new comforts or personalization
  - repeat with higher expressive payoff and less friction
- The first systems that usually break are:
  - chores feeling like chores instead of expression
  - menus and item flows becoming heavy
  - environmental changes not persisting clearly
  - relationship beats lacking visible state
- This genre needs explicit architecture for:
  - schedule clarity
  - low-friction interaction loops
  - world-state persistence
  - relationship or attachment state
  - comfort-first UI and pacing

## Primary sources
- [Stardew Valley official site](https://www.stardewvalley.net/)
- [Animal Crossing: New Horizons – Official site](https://animalcrossing.nintendo.com/new-horizons/)
- [Create your getaway — Animal Crossing: New Horizons](https://animalcrossing.nintendo.com/new-horizons/create/)

## Why this matters to this repo
- Cozy sim tasks in this repo should not be routed like ordinary farming or building tasks. The core challenge is low-friction routine plus durable attachment.
- Agents should explicitly name:
  - what the daily routine is
  - what visibly persists in the world
  - what relationship or comfort state the player is building
  - where UI or inventory friction would ruin the mood
- First slices should prove one routine, one place improvement, and one visible response from the world.

## Decision impact
- Future presets and feature briefs should require:
  - routine clarity
  - persistence and decoration state
  - relationship or comfort projection
  - low-friction menus and interactions
- When a project selects this genre, route output should surface UI, persistence, and warm interaction notes together.
