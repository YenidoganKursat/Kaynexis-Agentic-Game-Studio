# Golden Example — Feature Brief

## Player outcome
- The player can survive a short combat room by reading one clear enemy pulse, timing one dash, and choosing one meaningful upgrade afterward.

## Scope
- Must-have:
  - one room
  - one enemy role
  - one dash verb
  - one upgrade choice
- Nice-to-have:
  - stronger room reset feedback
- Explicit non-goals:
  - full run structure
  - meta progression
  - additional enemy archetypes

## Acceptance criteria
- A first-time tester understands when the pulse is dangerous.
- Dashing changes success rate in a readable way.
- The upgrade choice changes the next attempt enough to be noticeable.

## Touched systems
- combat readability
- player state
- enemy telegraph
- upgrade UI

## Risks & dependencies
- Pulse timing may feel unfair without clear anticipation frames.
- Upgrade impact may be too small to justify the choice screen.
- Needs one repeatable smoke path after any combat timing change.
