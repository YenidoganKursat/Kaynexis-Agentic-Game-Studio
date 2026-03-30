# Tactical RPG

## Date
- 2026-03-29

## Summary
- Tactical RPGs fail first on forecast clarity, mobility budget, and decision load. The player should be able to read the battlefield, predict consequences, and understand why a commitment was good or bad.
- The dominant loop is:
  - read a grid or tactical space
  - forecast an attack or move
  - commit to positioning and action choice
  - resolve the turn
  - adapt the roster or formation
- The first systems that usually break are:
  - cover, hit, or range rules becoming opaque
  - turn forecast UI being too weak or too noisy
  - mobility values or terrain rules feeling arbitrary
  - complexity spiraling before the player learns the basic tactical language
- This genre needs explicit architecture for:
  - turn forecast and combat preview
  - mobility and terrain ownership
  - encounter pacing and unit roster depth
  - support, status, and build synergy readability
  - recovery from a bad position without hiding the stakes

## Primary sources
- [Fire Emblem™ Engage for Nintendo Switch - Nintendo Official Site](https://www.nintendo.com/us/store/products/fire-emblem-engage-switch/)
- [Fire Emblem Engage: Divine Edition - Nintendo Official Site](https://www.nintendo.com/us/store/products/fire-emblem-engage-divine-edition-117513/)
- [Fire Emblem Engage Ask the Developer](https://www.nintendo.com/en-gb/News/2023/January/Ask-the-Developer-Vol-8-Fire-Emblem-Engage-Chapter-3-2329633.html)

## Why this matters to this repo
- Tactical RPG tasks in this repo should not be routed like generic RPG or turn-based combat tasks. They are forecast, mobility, and turn-consequence problems first.
- Agents should explicitly name:
  - the forecast model and what it shows
  - how movement and terrain cost are owned
  - how the player reads risk before committing
  - how build depth stays understandable under pressure
- First slices should prove one skirmish, one meaningful build choice, and one forecast UI before the tactics layer grows.

## Decision impact
- Future presets and feature briefs should require:
  - turn forecast clarity
  - terrain and mobility ownership
  - readable status and synergy effects
  - a small encounter that teaches tactical language before the roster grows
- When a project selects this genre, route output should surface forecast, positioning, and combat-preview notes together.
