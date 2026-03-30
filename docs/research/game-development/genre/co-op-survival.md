# Co-op Survival

## Date
- 2026-03-29

## Summary
- Co-op survival fails first on shared resource truth, session authority, and recovery fairness. The player should be able to explain who owns what, why the team is still alive, and how the next collapse can be recovered from.
- The dominant loop is:
  - gather or craft together
  - survive environmental or creature pressure
  - recover from scarcity
  - rebuild the shared base or loadout
  - repeat with higher coordination demands
- The first systems that usually break are:
  - inventory ownership becoming unclear
  - revive or recovery rules feeling arbitrary
  - griefing or loot theft creating social friction
  - too many tasks arriving before cooperation matters
- This genre needs explicit architecture for:
  - session authority
  - shared inventory and resource truth
  - revive/recovery rules
  - threat pacing and night-pressure loops
  - anti-grief or trust-preserving recovery logic

## Primary sources
- [Don't Starve Together on Steam](https://store.steampowered.com/app/322330/Don_t_Starve_Together/)
- [Klei support: Does Don't Starve Together have caves or ruins content?](https://support.klei.com/hc/en-us/articles/360029557132-Does-Don-t-Starve-Together-have-caves-or-ruins-content)
- [Klei support: Hide Don't Starve Together items from Steam Inventory](https://support.klei.com/hc/en-us/articles/25338712573460-How-to-hide-Dont-Starve-Together-items-from-your-Steam-Inventory)

## Why this matters to this repo
- Co-op survival tasks in this repo should not be treated like single-player combat or crafting tasks. They are session-truth, recovery, and shared-pressure problems first.
- Agents should explicitly name:
  - who owns the session truth
  - how the team shares or loses resources
  - how the game recovers after a wipe or rescue failure
  - what stops the cooperation loop from becoming grief-heavy
- First slices should prove one shared resource loop and one recovery loop before the game grows into many systems.

## Decision impact
- Future presets and feature briefs should require:
  - session authority
  - shared inventory or stash ownership
  - revive and recovery rules
  - anti-grief boundaries
  - a readable team-failure recovery loop
- When a project selects this genre, route output should surface authority, inventory, recovery, and level-pressure notes together.
