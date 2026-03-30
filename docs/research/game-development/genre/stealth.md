# Stealth

## Date
- 2026-03-28

## Summary
- Stealth games fail first on detection readability and patrol fairness. The player needs to understand what causes suspicion, where visibility comes from, and how to recover after a near-miss.
- The dominant loop is:
  - scout a space
  - observe patrols and visibility
  - manipulate noise, timing, or line of sight
  - execute the objective
  - exit without over-triggering the alarm state
- The first systems that usually break are:
  - detection rules that are too subtle to learn
  - patrol or alert states that feel arbitrary
  - level geometry that makes ghosting impossible to read
  - failure recovery that punishes experimentation too hard
- This genre needs explicit architecture for:
  - AI perception and suspicion states
  - patrol routes and visibility rules
  - sound/noise and light/shadow readability
  - objective routing and escape logic
  - safe fail/retry loops for experimentation

## Primary sources
- [HITMAN World of Assassination official site](https://www.hitman.com/)

## Why this matters to this repo
- Stealth tasks in this repo should not be routed like ordinary action tasks. They are primarily perception, routing, and failure-recovery problems.
- Agents should explicitly name:
  - how guards perceive the player
  - how suspicion escalates and cools down
  - what geometry or props support stealth readability
  - how the game lets the player recover after detection
- First-slice recommendations should favor one patrol space and one readable detection rule over a broad sandbox.

## Decision impact
- Future presets and feature briefs should require:
  - detection and suspicion ownership
  - patrol or route readability
  - sound/light visibility assumptions
  - objective escape or recovery rules
- When a project selects this genre, route output should surface AI, level, audio, UI, and failure-state notes together.
