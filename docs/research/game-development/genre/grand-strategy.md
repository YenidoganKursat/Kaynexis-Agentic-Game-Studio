# Grand Strategy

## Date
- 2026-03-28

## Summary
- Grand-strategy games fail first on state-model readability and long-horizon pacing. The player must be able to reason about realms, diplomacy, events, and long-term consequences without the UI becoming a wall of numbers.
- The dominant loop is:
  - choose a long-horizon plan
  - react to events and diplomacy
  - expand or stabilize influence
  - preserve the campaign or run
  - repeat over a very long session
- The first systems that usually break are:
  - dense UI or map state hiding causality
  - diplomacy/event pacing that feels arbitrary
  - AI layers that are too opaque to trust
  - save systems that drift across long campaigns
- This genre needs explicit architecture for:
  - realm, faction, or empire state
  - diplomacy and event systems
  - long-session save trust and history
  - layered map/UI hierarchy
  - AI/campaign pacing rules

## Primary sources
- [Crusader Kings III official site](https://www.paradoxinteractive.com/games/crusader-kings-iii)
- [Stellaris official site](https://www.paradoxinteractive.com/games/stellaris)

## Why this matters to this repo
- Grand-strategy tasks in this repo should not be routed like ordinary tactics or colony tasks. They are primarily macro-simulation, diplomacy, and state readability problems.
- Agents should explicitly name:
  - what realm or faction state is authoritative
  - how diplomacy, policies, and events are modeled
  - what the player can read at the map level versus the detail level
  - how long-session saves preserve trust
- First-slice recommendations should prefer one realm turn or one policy decision over a full-scale empire sandbox.

## Decision impact
- Future presets and feature briefs should require:
  - campaign-level state ownership
  - diplomacy or event pacing
  - layered UI or map readability
  - long-session save trust
- When a project selects this genre, route output should surface UI, save, AI, event, and simulation notes together.
