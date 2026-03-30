# Auto-Battler

## Date
- 2026-03-28

## Summary
- Auto-battlers fail first on roster/economy readability, not on combat spectacle. The player must be able to understand what was drafted, how a board is resolving, and why a round was won or lost.
- The dominant loop is:
  - draft or shop
  - place units on a small board
  - resolve the round automatically
  - adapt the roster or economy
  - repeat with more constrained but stronger decisions
- The first systems that usually break are:
  - shop pools or roll economies becoming opaque
  - board positioning rules being hard to explain
  - combat resolution logs being too noisy or too thin
  - synergy stacks that are powerful but unreadable
- This genre needs explicit architecture for:
  - shop and draft economy
  - board state and placement rules
  - round resolution and combat logs
  - item/unit pool health
  - readable match UI for adaptation

## Primary sources
- [Teamfight Tactics official site](https://teamfighttactics.leagueoflegends.com/)

## Why this matters to this repo
- Auto-battler tasks in this repo should not be routed like ordinary combat tasks. They are primarily economy, board-state, and resolution-clarity problems.
- Agents should explicitly name:
  - what is in the roster pool versus the active board
  - how rounds resolve and how the player reads the outcome
  - how the shop or draft economy is protected from degeneracy
  - what UI surfaces the current build identity and next decision
- First-slice recommendations should favor one board and one draft cycle over a huge unit list.

## Decision impact
- Future presets and feature briefs should require:
  - shop or draft economy ownership
  - board placement rules
  - round-resolution logging
  - pool-health or synergy-stacking constraints
- When a project selects this genre, route output should surface economy, UI, combat resolution, and balance notes together.
