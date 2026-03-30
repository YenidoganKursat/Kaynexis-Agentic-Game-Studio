# Soulslike

## Date
- 2026-03-28

## Summary
- Soulslike-inspired action RPGs fail first on telegraph clarity and punishment fairness. The player must be able to read enemy commitment, understand stamina cost, and recover from mistakes without feeling that the system is arbitrary.
- The dominant loop is:
  - explore a dangerous space
  - read telegraphs and commit stamina
  - survive a difficult encounter
  - recover, learn, and return
  - unlock safer traversal through mastery and shortcuts
- The first systems that usually break are:
  - attack windows that are too vague to read
  - checkpoints or death recovery that feel punitive instead of meaningful
  - world gates that do not teach or reward return paths
  - enemy AI that lacks rhythm or consistency
- This genre needs explicit architecture for:
  - stamina and commitment timing
  - animation telegraphs and hit windows
  - checkpoint, respawn, and corpse-recovery rules
  - world gating and shortcut design
  - combat tuning with strong recovery rules

## Primary sources
- [ELDEN RING official site](https://en.bandainamcoent.eu/elden-ring/elden-ring)
- [ELDEN RING starter guide](https://media-center.bandainamcoent.eu/games/elden-ring-nightreign/ERN_FuturePress_StarterGuide.pdf)

## Why this matters to this repo
- Soulslike tasks in this repo should not be treated like ordinary action tasks. The core problem is usually fairness through readability, not just difficulty.
- Agents should explicitly name:
  - how stamina, animation, and recovery rules interact
  - what checkpoints or gates protect the player from repeat frustration
  - what makes the enemy readable before the hit lands
  - how the level structure supports safe return after failure
- First-slice recommendations should prioritize a single duel or miniboss space with clear recovery and shortcut rules.

## Decision impact
- Future presets and feature briefs should require:
  - telegraph windows and recovery rules
  - checkpoint or corpse-recovery ownership
  - shortcut or return-path design
  - clarity on how punishment teaches rather than punishes blindly
- When a project selects this genre, route output should surface combat, level design, accessibility, save, and tuning notes together.
