# Genre Example Matrix

## Date
- 2026-03-27

## Summary
- This matrix maps the repo's genre presets to example games that illustrate the core loop and the most important early design risk.
- The examples below are inferences from official game pages, store pages, and first-party developer materials. They are meant as contrast sets, not cloning targets.

## Primary sources
- [Dead Cells official site](https://dead-cells.com/)
- [Risk of Rain 2 official site](https://riskofrain.2k.com/)
- [Stardew Valley official site](https://www.stardewvalley.net/)
- [Animal Crossing: New Horizons official site](https://animalcrossing.nintendo.com/new-horizons/create/)
- [Don't Starve Together on Steam](https://store.steampowered.com/app/322330/Don_t_Starve_Together/)
- [Hunt: Showdown early access release notes](https://www.huntshowdown.com/news/hunt-showdown-early-access-release-notes)
- [Life is Strange official site](https://lifeisstrange.square-enix-games.com/en-us)
- [Pentiment official site](https://pentiment.obsidian.net/)
- [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/)
- [Fire Emblem Engage Ask the Developer](https://www.nintendo.com/en-gb/News/2023/January/Ask-the-Developer-Vol-8-Fire-Emblem-Engage-Chapter-3-2329633.html)

## Why this matters to this repo
- When choosing a genre preset, teams should also choose a contrast set.
- A contrast set gives Codex and the project team a shared vocabulary for what "good" looks like and what usually fails first.

## Decision impact
- Genre presets and first-slice docs should cite one or two example references from this matrix.
- Future onboarding can surface this matrix directly in the setup wizard or `codex_studio.py init` help.

## Matrix

| Preset | Example games | What to study first | First risk to watch |
|---|---|---|---|
| `action-roguelite` | `Dead Cells`, `Risk of Rain 2` | repetition loop, build variety, scaling pressure | run variety collapse |
| `co-op-survival` | `Don't Starve Together` | shared resource truth, social recovery, session stakes | desync and inventory ambiguity |
| `cozy-sim` | `Stardew Valley`, `Animal Crossing: New Horizons` | routine texture, attachment to place, low-friction progression | grind and UI sprawl |
| `extraction-lite` | `Hunt: Showdown` | extraction clarity, sound/information play, economy trust | unfair loss and exploit pressure |
| `narrative-adventure` | `Life is Strange`, `Pentiment` | scene flow, choice visibility, content throughput | branch/state bugs |
| `platformer` | `Dead Cells` as action-platformer contrast | movement feel, retry cadence, hazard readability | input/camera frustration |
| `puzzle` | `Portal 2` | teach/test/twist sequencing, chamber escalation | rule ambiguity |
| `tactical-rpg` | `Fire Emblem Engage` | forecast clarity, mobility vs tactics balance, choice density | decision paralysis or broken mobility |

## Quick application notes

### If the project is genre-uncertain
- Start by picking the column that describes the strongest player tension:
  - readable pressure -> action-roguelite
  - shared scarcity -> co-op-survival
  - low-stress routine -> cozy-sim
  - high-risk extraction -> extraction-lite
  - authored choice and consequence -> narrative-adventure
  - movement mastery -> platformer
  - insight and rule discovery -> puzzle
  - forecastable consequence planning -> tactical-rpg

### If the project blends two presets
- Decide which preset owns:
  - the first 10 minutes
  - the dominant failure loop
  - the most expensive content pipeline
- Use the secondary preset only after the primary one is validated.
