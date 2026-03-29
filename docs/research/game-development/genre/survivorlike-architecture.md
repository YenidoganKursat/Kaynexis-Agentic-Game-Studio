# Survivorlike Architecture

## Date
- 2026-03-28

## Summary
- Survivorlikes fail first on scale readability and build tempo. The genre looks visually simple, but it quickly becomes a performance, progression, and clarity problem once enemy counts, passive synergies, and drop density increase.
- The dominant loop is:
  - survive escalating waves
  - gather XP or drops under movement pressure
  - choose upgrades at high frequency
  - build toward a late-run power spike
  - cash out permanent progress and restart
- The first systems that usually break are:
  - uncontrolled screen noise
  - unclear hitboxes and unfair crowd pressure
  - passive upgrade menus that flatten into obvious choices
  - representation and allocation cost under swarm scale
- This genre needs deliberate decisions on:
  - auto-fire versus aimed control
  - enemy density representation
  - drop pickup rules
  - temporary upgrade cadence
  - meta progression pacing

## Primary sources
- [Vampire Survivors on Steam](https://store.steampowered.com/app/1794680/Vampire_Survivors/)
- [Brotato on Steam](https://store.steampowered.com/app/1942280/Brotato/)

## Why this matters to this repo
- Survivorlike work in this repo should surface performance and readability immediately, not after content scale already exists.
- Agents should explicitly state:
  - enemy-count strategy
  - pickup and XP magnet rules
  - upgrade cadence
  - readability budget for effects and drops
  - meta unlock boundaries
- First-slice advice should prove one escalation curve and one upgrade cadence, not just "spawn more enemies."

## Decision impact
- When a project selects this genre, route and checklist output should bias toward:
  - performance
  - combat readability
  - upgrade/build architecture
  - meta progression boundaries
- Future presets should include a required note on late-run readability and scale risk.
