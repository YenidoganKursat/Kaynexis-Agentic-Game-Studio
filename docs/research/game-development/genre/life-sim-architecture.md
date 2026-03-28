# Life-Sim Architecture

## Date
- 2026-03-28

## Summary
- Life-sims fail first on relationship-state legibility and routine texture. The player needs to understand who they are, what their daily rhythm is, and how small recurring actions change the life of the character or household over time.
- The dominant loop is:
  - create or choose a character and home
  - follow a daily routine
  - customize identity, relationships, and environment
  - unlock new life options
  - repeat with deeper attachment
- The first systems that usually break are:
  - UI sprawl that hides meaningful life changes
  - relationship or calendar state that is hard to explain
  - content throughput that cannot keep up with routine variety
  - save files that drift as the simulation grows
- This genre needs explicit architecture for:
  - character state and household state
  - time, calendar, and schedule systems
  - relationship graphs and social events
  - customization and cosmetic ownership
  - save/load stability across long play sessions

## Primary sources
- [The Sims 4 official site](https://www.ea.com/games/the-sims/the-sims-4)
- [Animal Crossing: New Horizons official site](https://animalcrossing.nintendo.com/new-horizons/)
- [Stardew Valley official site](https://www.stardewvalley.net/)

## Why this matters to this repo
- Life-sim tasks in this repo should not be handled like action or combat tasks. They are primarily about state continuity, routine pacing, relationship readability, and content throughput.
- Agents should explicitly name:
  - what lives in character state, household state, and world state
  - how time advances and how routines are represented
  - how social or relationship changes are surfaced to the player
  - what persistence guarantees the save system must uphold
- First-slice recommendations should favor one routine plus one visible life change instead of a large open-ended sandbox.

## Decision impact
- Future presets and feature briefs should require:
  - calendar or time ownership
  - relationship-state visibility
  - customization or home/wardrobe ownership
  - content pipeline assumptions for routine variety
- When a project selects this genre, route output should surface UI, narrative, content pipeline, save, and localization notes together.
