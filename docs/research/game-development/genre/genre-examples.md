# Genre Examples

## Date
- 2026-03-27

## Summary
- This matrix maps the repo's genre presets to example games that illustrate the core loop and the most important early design risk.
- The examples below are inferences from official game pages, store pages, and first-party developer materials. They are meant as contrast sets, not cloning targets.
- The gallery now also includes a small adjacent-genre set for cases where the project needs stronger contrast than the preset list alone can provide.

## Primary sources
- [Dead Cells official site](https://dead-cells.com/)
- [Risk of Rain 2 official site](https://riskofrain.2k.com/)
- [Slay the Spire on Steam](https://store.steampowered.com/app/646570/Slay_the_Spire/)
- [Balatro on Steam](https://store.steampowered.com/app/2379780/Balatro/)
- [Stardew Valley official site](https://www.stardewvalley.net/)
- [Animal Crossing: New Horizons official site](https://animalcrossing.nintendo.com/new-horizons/create/)
- [Don't Starve Together on Steam](https://store.steampowered.com/app/322330/Don_t_Starve_Together/)
- [Hunt: Showdown early access release notes](https://www.huntshowdown.com/news/hunt-showdown-early-access-release-notes)
- [Vampire Survivors on Steam](https://store.steampowered.com/app/1794680/Vampire_Survivors/)
- [Brotato on Steam](https://store.steampowered.com/app/1942280/Brotato/)
- [Life is Strange official site](https://lifeisstrange.square-enix-games.com/en-us)
- [Pentiment official site](https://pentiment.obsidian.net/)
- [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/)
- [RimWorld on Steam](https://store.steampowered.com/app/294100/RimWorld/)
- [Against the Storm on Steam](https://store.steampowered.com/app/1336490/Against_the_Storm/)
- [Factorio official site](https://www.factorio.com/)
- [Satisfactory on Steam](https://store.steampowered.com/app/526870/Satisfactory/)
- [Metroid Dread official site](https://metroid.nintendo.com/dread/)
- [Hollow Knight official site](https://www.hollowknight.com/)
- [Fire Emblem Engage Ask the Developer](https://www.nintendo.com/en-gb/News/2023/January/Ask-the-Developer-Vol-8-Fire-Emblem-Engage-Chapter-3-2329633.html)
- [Civilization VII support and news](https://support.civilization.com/hc/en-us)
- [Hi-Fi RUSH official page](https://bethesda.net/en/game/hifi-rush)
- [Minecraft official site](https://www.minecraft.net/)
- [Valheim official site](https://www.valheim.com/)
- [Bloons TD 6 on Steam](https://store.steampowered.com/app/960090/Bloons_TD_6/)
- [Two Point Campus official site](https://www.twopointstudios.com/games/two-point-campus/)
- [Prey support page](https://help.bethesda.net/app/answers/detail/a_id/39395/)
- [Deus Ex: Mankind Divided official site](https://www.deusex.com/)

## Why this matters to this repo
- When choosing a genre preset, teams should also choose a contrast set.
- A contrast set gives Codex and the project team a shared vocabulary for what "good" looks like and what usually fails first.

## Software pattern contrast sets

Use these when the team already knows the genre family but still needs a concrete software shape to build against.

| Pattern | Example games | What to study first |
|---|---|---|
| State projection | `Life is Strange`, `Pentiment`, `The Sims 4` | how authored or simulation state becomes readable to the player without the UI owning truth |
| Deterministic resolver | `Slay the Spire`, `Balatro`, `Teamfight Tactics` | why a turn or round resolved the way it did, and how logs keep the system explainable |
| Authority split | `Don't Starve Together`, `Hunt: Showdown`, `Overwatch 2` | where session truth lives and how presentation stays separate from authority |
| Graph / route model | `Metroid Dread`, `Hollow Knight`, `Crusader Kings III` | world memory, gates, routes, and campaign-scale history |
| Spawn / pool / instance | `Vampire Survivors`, `Brotato`, `Risk of Rain 2` | why density stayed readable and how repeated objects avoided churn |
| Overlay / diagnostic view | `RimWorld`, `Against the Storm`, `Factorio`, `Cities: Skylines II` | the overlays or diagnostics that let the player find bottlenecks |
| Scheduler / job queue | `RimWorld`, `Factorio`, `The Sims 4` | priority, throughput, and recovery behavior in simulation-heavy systems |
| Board / lane resolution | `Teamfight Tactics`, `Fire Emblem Engage` | how a small state space stays legible across round resolution |
| Perception / suspicion FSM | `HITMAN World of Assassination`, stealth and patrol games | how detection and suspicion stay fair and readable |

## Decision impact
- Genre presets and first-slice docs should cite one or two example references from this matrix.
- Future onboarding can surface this matrix directly in the setup wizard or `codex_studio.py init` help.
- Teams that already know their contrast set should graduate from this matrix into the advanced genre framework before they start a real production backlog.

## Matrix

| Preset | Example games | What to study first | First risk to watch |
|---|---|---|---|
| `action-roguelite` | `Dead Cells`, `Risk of Rain 2` | repetition loop, build variety, scaling pressure | run variety collapse |
| `deckbuilder-roguelike` | `Slay the Spire`, `Balatro` | reward pool health, state readability, route planning | solved decks or unreadable card states |
| `co-op-survival` | `Don't Starve Together` | shared resource truth, social recovery, session stakes | desync and inventory ambiguity |
| `auto-battler` | `Teamfight Tactics` | draft economy, board positioning, round pacing | roster opacity or board confusion |
| `cozy-sim` | `Stardew Valley`, `Animal Crossing: New Horizons` | routine texture, attachment to place, low-friction progression | grind and UI sprawl |
| `extraction-lite` | `Hunt: Showdown` | extraction clarity, sound/information play, economy trust | unfair loss and exploit pressure |
| `grand-strategy` | `Crusader Kings III`, `Stellaris` | realm state, diplomacy, event pacing | UI density or state overload |
| `survivorlike` | `Vampire Survivors`, `Brotato` | density readability, upgrade cadence, performance ceilings | clutter and spawn/perf collapse |
| `narrative-adventure` | `Life is Strange`, `Pentiment` | scene flow, choice visibility, content throughput | branch/state bugs |
| `platformer` | `Dead Cells` as action-platformer contrast | movement feel, retry cadence, hazard readability | input/camera frustration |
| `puzzle` | `Portal 2` | teach/test/twist sequencing, chamber escalation | rule ambiguity |
| `stealth` | `HITMAN World of Assassination` | detection fairness, patrol readability, objective routing | detection feeling arbitrary |
| `colony-sim` | `RimWorld`, `Against the Storm` | job priorities, crisis readability, long-session state | simulation opacity |
| `city-builder` | `Cities: Skylines II` | zoning, demand curves, transport clarity | unreadable city-scale bottlenecks |
| `factory-automation` | `Factorio`, `Satisfactory` | throughput visibility, bottleneck debugging, scale tooling | unreadable logistics or expensive simulation |
| `life-sim` | `The Sims 4`, `Animal Crossing: New Horizons` | routine texture, relationships, long-session identity | chores and relationship opacity |
| `hero-shooter` | `Overwatch 2` | hero role clarity, objective pacing, teamfight readability | heroes blur together or objective confusion |
| `metroidvania` | `Metroid Dread`, `Hollow Knight` | world memory, traversal gating, return-loop reward | arbitrary gates or dead backtracking |
| `soulslike` | `ELDEN RING` | telegraph clarity, stamina commitment, recovery fairness | punishment feels arbitrary |
| `tactical-rpg` | `Fire Emblem Engage` | forecast clarity, mobility vs tactics balance, choice density | decision paralysis or broken mobility |

## Additional design cards

Use these when the project sits between presets or when a feature brief needs a stronger contrast set.

| Card | Example games | What to study first | First design question | First risk |
|---|---|---|---|---|
| `sandbox-survival` | `Minecraft`, `Valheim` | emergent goals, crafting progression, world persistence | what keeps the player self-directing after the first shelter? | aimless wandering or goal dilution |
| `tower-defense` | `Bloons TD 6` | lane clarity, path pressure, upgrade economy | what makes each wave legible and each upgrade meaningful? | path opacity or trivial stall strategies |
| `4X` | `Civilization VII` | empire-phase transitions, macro pacing, map readability | how does the game compress huge state into a readable turn? | state overload or late-game drag |
| `rhythm-action` | `Hi-Fi RUSH` | beat sync, audiovisual timing, readable combo windows | what owns timing truth: music, animation, or combat state? | sync drift or inaccessible timing |
| `management-sim` | `Two Point Campus` | staff/student simulation, layout tools, service diagnostics | which problems can the player solve from one map view? | hidden service failures or tool sprawl |
| `immersive-sim` | `Prey`, `Deus Ex: Mankind Divided` | affordance density, multiple solutions, reactive spaces | how many valid answers can one room support? | arbitrary gating or noisy options |

## Quick application notes

### If the project is genre-uncertain
- Start by picking the column that describes the strongest player tension:
  - readable pressure -> action-roguelite
  - compact sequencing and route planning -> deckbuilder-roguelike
  - shared scarcity -> co-op-survival
  - draft and board resolution -> auto-battler
  - low-stress routine -> cozy-sim
  - high-risk extraction -> extraction-lite
  - long-horizon empire state -> grand-strategy
  - high-density survival pressure -> survivorlike
  - authored choice and consequence -> narrative-adventure
  - movement mastery -> platformer
  - insight and rule discovery -> puzzle
  - detection and route control -> stealth
  - emergent colony management -> colony-sim
  - city-scale planning -> city-builder
  - logistics and throughput scaling -> factory-automation
  - life routine and identity -> life-sim
  - hero kit and objective matches -> hero-shooter
  - exploration through gated traversal -> metroidvania
  - stamina challenge and recovery mastery -> soulslike
  - forecastable consequence planning -> tactical-rpg

### If the project blends two presets
- Decide which preset owns:
  - the first 10 minutes
  - the dominant failure loop
  - the most expensive content pipeline
- Use the secondary preset only after the primary one is validated.
