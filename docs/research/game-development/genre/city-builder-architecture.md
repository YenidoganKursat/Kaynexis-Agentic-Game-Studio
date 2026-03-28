# City-Builder Architecture

## Date
- 2026-03-28

## Summary
- City-builders fail first on simulation opacity, not on graphics polish. The player must be able to see why a district is failing, what demand is changing, and which system is responsible before the city-scale simulation becomes satisfying.
- The dominant loop is:
  - zone or place a district
  - provide services and transport
  - observe demand, bottlenecks, and traffic
  - rebalance the city
  - expand into more complex planning
- The first systems that usually break are:
  - unreadable traffic or logistics
  - demand curves that the player cannot explain
  - expensive simulation that fights scale
  - overlays or UI that hide the real bottleneck
- This genre needs explicit architecture for:
  - city state and zoning data
  - service coverage and demand simulation
  - transport/pathing and bottleneck detection
  - overlays and inspection UI
  - save stability for long sessions

## Primary sources
- [Cities: Skylines II official site](https://www.paradoxinteractive.com/games/cities-skylines-ii/about)
- [Cities: Skylines II on Steam](https://store.steampowered.com/app/949230/Cities_Skylines_II/)

## Why this matters to this repo
- City-builder tasks in this repo should not be routed like generic level work. They are primarily simulation, UI, and scale-management problems.
- Agents should explicitly name:
  - what is authored city data versus runtime city state
  - how demand, services, and transport are represented
  - what overlay or inspector lets the player debug the city
  - how save/load preserves long-running simulation trust
- First-slice recommendations should prefer one readable district and one solvable bottleneck over a broad but shallow map.

## Decision impact
- Future presets and feature briefs should require:
  - zoning or placement rules
  - demand or service categories
  - transport or pathing visibility
  - a clear overlay for bottleneck diagnosis
- When a project selects this genre, route output should surface UI, simulation, pathing, save, and performance notes together.
