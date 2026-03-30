# Hero Shooter

## Date
- 2026-03-28

## Summary
- Hero shooters fail first on role clarity and objective readability, not on raw combat flash. The player must understand what their hero can do, why their team composition matters, and how the map or objective mode is being contested.
- The dominant loop is:
  - choose a hero with a defined role
  - contest an objective or map control point
  - swap or coordinate to answer the situation
  - win through teamwork and readable pressure
  - repeat across short, high-energy matches
- The first systems that usually break are:
  - hero kits that blur together
  - objective modes that are not readable at speed
  - network or perf problems that degrade combat trust
  - VFX/UI clutter that hides team and enemy intent
- This genre needs explicit architecture for:
  - hero data and cooldown/state ownership
  - objective and map-mode rules
  - network authority and replication assumptions
  - telemetry for hero and role balance
  - presentation rules for killfeed, UI, and effects

## Primary sources
- [Overwatch 2 official site](https://overwatch.blizzard.com/)
- [Overwatch 2 patch notes and updates](https://overwatch.blizzard.com/en-us/news/patch-notes/live/)

## Why this matters to this repo
- Hero-shooter tasks in this repo should not be routed like generic combat tasks. They are a blend of combat loop design, objective flow, netcode assumptions, and readability under pressure.
- Agents should explicitly name:
  - what is hero-owned versus match-owned state
  - how objectives are represented and scored
  - what replication or authority model keeps combat fair
  - how VFX and UI preserve combat readability
- First-slice recommendations should focus on one hero, one objective, and one teamfight readability pass rather than a huge roster.

## Decision impact
- Future presets and feature briefs should require:
  - hero kit identity and role definition
  - objective mode or map control rules
  - network or multiplayer authority assumptions
  - telemetry for balance and killfeed readability
- When a project selects this genre, route output should surface combat, multiplayer, UI, performance, and telemetry notes together.
