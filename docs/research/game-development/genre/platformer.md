# Platformer

## Date
- 2026-03-29

## Summary
- Platformers fail first on movement feel, camera support, and restart cadence. The player should feel in control within seconds and be able to retry without friction.
- The dominant loop is:
  - read a hazard or route
  - execute a jump, dash, climb, or equivalent traversal verb
  - recover quickly from failure
  - learn the space through repetition
- The first systems that usually break are:
  - imprecise input or animation timing
  - cameras that fight the player
  - hazards that are hard to parse at speed
  - checkpoints or respawns that slow learning
- This genre needs explicit architecture for:
  - movement authority
  - camera framing and follow logic
  - hazard readability
  - checkpoint and retry loops
  - level blockout and timing rhythm

## Primary sources
- [Celeste on Steam](https://store.steampowered.com/app/504230/Celeste/)
- [Super Meat Boy on Steam](https://store.steampowered.com/app/40800/Super_Meat_Boy/)

## Why this matters to this repo
- Platformer tasks in this repo should not be treated like generic movement tuning. The core problem is learnable motion plus fast retry loops.
- Agents should explicitly name:
  - what owns input and movement truth
  - what the camera is allowed to do
  - how fast the player restarts after failure
  - what makes hazards readable at speed
- First slices should prove a teaching room, one hazard, and one quick recovery loop before adding more content.

## Decision impact
- Future presets and feature briefs should require:
  - movement authority and camera ownership
  - hazard readability
  - rapid retry or checkpoint behavior
  - a level rhythm that teaches by repetition
- When a project selects this genre, route output should surface movement, camera, and blockout notes together.
