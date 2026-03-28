# Factory Automation Architecture

## Date
- 2026-03-28

## Summary
- Factory automation games fail first on throughput visibility and simulation scalability. The genre depends on the player's ability to reason about production flow, bottlenecks, spatial planning, and logistics chains over time.
- The dominant loop is:
  - gather or unlock production capability
  - automate one bottleneck
  - expand throughput or complexity
  - notice the next bottleneck
  - refactor or scale the system
- The first systems that usually break are:
  - unclear production state and bottleneck visibility
  - logistics representation cost at scale
  - world interaction friction for building, replacing, and routing
  - save/load complexity once the factory becomes large
- This genre wants explicit architecture for:
  - machine definitions
  - recipe and throughput data
  - logistics links and transport representation
  - world placement and editing tools
  - production telemetry and debugging UI
  - long-save stability

## Primary sources
- [Factorio official site](https://www.factorio.com/)
- [Factorio on Steam](https://store.steampowered.com/app/427520/Factorio/)
- [Satisfactory on Steam](https://store.steampowered.com/app/526870/Satisfactory/)

## Why this matters to this repo
- Factory-automation tasks should route to tools, UI, performance, and save architecture much earlier than a typical action prototype would.
- Agents should explicitly state:
  - throughput truth
  - logistics representation choice
  - placement/edit tooling expectations
  - bottleneck visibility path
  - save/load expectations for large factories
- First slices should prove one production chain with visible debugability, not a huge map with shallow automation.

## Decision impact
- Future presets and first-slice docs should require:
  - one throughput debugging path
  - one representation strategy for logistics
  - one save/load risk note
  - one building/edit interaction model
- When a project selects this genre, route output should surface tools-pipeline, performance, UI, and save notes alongside gameplay.
