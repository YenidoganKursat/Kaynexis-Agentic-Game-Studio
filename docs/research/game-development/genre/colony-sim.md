# Colony Sim

## Date
- 2026-03-28

## Summary
- Colony sims fail first on simulation ownership and information overload. The genre becomes fragile when needs, jobs, schedules, events, production chains, and UI warnings all compete without a strong priority model.
- The dominant loop is:
  - assign or enable production and survival behaviors
  - respond to environmental or social pressure
  - grow the settlement's capability
  - absorb setbacks and emergent stories
  - re-prioritize the colony
- The first systems that usually break are:
  - unclear job priority or AI assignment rules
  - unreadable need or mood state
  - content sprawl in build/craft trees
  - event systems that overwhelm recovery
- This genre wants explicit architecture for:
  - colonist or citizen state
  - job or task assignment
  - settlement-wide resources
  - event or storyteller pressure
  - UI summaries and alerts
  - save and simulation persistence

## Primary sources
- [RimWorld on Steam](https://store.steampowered.com/app/294100/RimWorld/)
- [Against the Storm on Steam](https://store.steampowered.com/app/1336490/Against_the_Storm/)

## Why this matters to this repo
- Colony-sim tasks should not be treated like simple crafting or UI work. The real problem is usually simulation ownership plus player-facing prioritization.
- Agents should explicitly state:
  - who owns actor needs and schedules
  - who owns task arbitration
  - who owns settlement resource truth
  - how events escalate pressure
  - how the UI helps the player recover
- First slices should prove one short settlement loop with one clear crisis and one recovery path.

## Decision impact
- Future genre presets and docs should require:
  - one simulation priority model
  - one colony resource truth model
  - one alert/readability model
  - one event escalation model
- When a project selects this genre, route output should surface save, UI, economy, and AI/state architecture together.
