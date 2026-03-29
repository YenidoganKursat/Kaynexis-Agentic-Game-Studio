# Genre Design Pattern Catalog

## Date
- 2026-03-27

## Summary
- Different game genres fail for different reasons, so they need different architectural priorities from day one. A platformer fails first on feel and readability; a tactical RPG fails first on forecast clarity and decision load; a cozy sim fails first on routine texture and friction; an extraction game fails first on fairness, stakes, and economy trust.
- The safest way to use genre references is not to copy surface features. Instead, identify the dominant loop, the main player tension, the dominant source of content cost, and the first system most likely to break.
- In this repo, genre presets should be treated as architecture presets as much as creative prompts. Each genre points toward a different validation shape:
  - action-roguelite -> encounter readability and build variance
  - deckbuilder-roguelike -> state clarity, reward pool health, and route tension
  - co-op survival -> social coordination, resource pressure, and network resilience
  - auto-battler -> draft economy, board readability, and round resolution clarity
  - city-builder -> simulation legibility, demand curves, and bottleneck diagnosis
  - cozy sim -> routine legibility, low-friction progression, and environment attachment
  - extraction-lite -> raid fairness, secure economy, and extraction clarity
  - grand-strategy -> realm state, diplomacy, event pacing, and campaign trust
  - hero-shooter -> role clarity, objective pacing, and teamfight readability
  - life-sim -> routine texture, relationship state, and life-event content throughput
  - survivorlike -> density readability, scale-safe updates, and upgrade cadence
  - narrative adventure -> state tracking, content throughput, and choice legibility
  - platformer -> movement feel, camera support, and restart cadence
  - puzzle -> teach/test/twist sequencing and misunderstanding analysis
  - stealth -> detection fairness, patrol readability, and objective routing
  - colony-sim -> simulation legibility, agent priorities, and crisis recovery
  - factory-automation -> throughput clarity, composable systems, and scale tooling
  - metroidvania -> world-memory support, gate clarity, and return-path payoff
  - soulslike -> telegraph readability, recovery fairness, and shortcut-driven mastery
  - tactical RPG -> forecast readability, turn consequences, and complexity pacing

## Primary sources
- [Dead Cells official site](https://dead-cells.com/)
- [Risk of Rain 2 official site](https://riskofrain.2k.com/)
- [Slay the Spire on Steam](https://store.steampowered.com/app/646570/Slay_the_Spire/)
- [Balatro on Steam](https://store.steampowered.com/app/2379780/Balatro/)
- [Animal Crossing: New Horizons official site](https://animalcrossing.nintendo.com/new-horizons/create/)
- [Stardew Valley official site](https://www.stardewvalley.net/)
- [Don't Starve Together on Steam](https://store.steampowered.com/app/322330/Don_t_Starve_Together/)
- [Hunt: Showdown early access release notes](https://www.huntshowdown.com/news/hunt-showdown-early-access-release-notes)
- [Teamfight Tactics official site](https://teamfighttactics.leagueoflegends.com/)
- [Vampire Survivors on Steam](https://store.steampowered.com/app/1794680/Vampire_Survivors/)
- [Brotato on Steam](https://store.steampowered.com/app/1942280/Brotato/)
- [Life is Strange official site](https://lifeisstrange.square-enix-games.com/en-us)
- [Pentiment official site](https://pentiment.obsidian.net/)
- [Crusader Kings III official site](https://www.paradoxinteractive.com/games/crusader-kings-iii)
- [Stellaris official site](https://www.paradoxinteractive.com/games/stellaris)
- [HITMAN World of Assassination official site](https://www.hitman.com/)
- [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/)
- [RimWorld on Steam](https://store.steampowered.com/app/294100/RimWorld/)
- [Against the Storm on Steam](https://store.steampowered.com/app/1336490/Against_the_Storm/)
- [Factorio official site](https://www.factorio.com/)
- [Satisfactory on Steam](https://store.steampowered.com/app/526870/Satisfactory/)
- [Cities: Skylines II official site](https://www.paradoxinteractive.com/games/cities-skylines-ii/about)
- [The Sims 4 official site](https://www.ea.com/games/the-sims/the-sims-4)
- [Overwatch 2 official site](https://overwatch.blizzard.com/)
- [Metroid Dread official site](https://metroid.nintendo.com/dread/)
- [Hollow Knight official site](https://www.hollowknight.com/)
- [ELDEN RING official site](https://en.bandainamcoent.eu/elden-ring/elden-ring)
- [Fire Emblem Engage Ask the Developer](https://www.nintendo.com/en-gb/News/2023/January/Ask-the-Developer-Vol-8-Fire-Emblem-Engage-Chapter-3-2329633.html)

## Why this matters to this repo
- Genre choice should shape more than tone. It should change which docs, checklists, and validation loops matter first.
- Agents should stop giving the same first-slice advice to every genre. "Build one room and one enemy" makes sense for action-roguelites, but not for narrative adventure, cozy sim, or puzzle-first games.
- The repo's genre presets are already useful quick starts, but they need a deeper design layer so teams can reason from example loops instead of just genre labels.
- Once a first slice is chosen, the next step is not more examples; it is the advanced development framework that explains how the genre should scale.

## Decision impact
- Genre-specific research should become part of the default reading path for feature ideation and scoping.
- Future preset and wizard work should surface example games plus the first architecture risks for each preset.
- Task routing can stay discipline-driven, but genre docs should become the default contrast-set layer when a team is still deciding what kind of game it is building.

## Design patterns by genre

### Action roguelite
- Dominant loop:
  - enter encounter
  - survive readable pressure
  - choose build growth
  - reset into a stronger or more varied next run
- Architectural priority:
  - encounter readability
  - run-state vs meta-state separation
  - scalable enemy/content variation
- First system that breaks:
  - build variety collapses or permanent power trivializes skill expression
- Example inference:
  - `Dead Cells` emphasizes repeat attempts, no-checkpoint pressure, and combat mastery.
  - `Risk of Rain 2` emphasizes scaling enemies, item combinations, and co-op or solo run escalation.

### Co-op survival
- Dominant loop:
  - gather and coordinate
  - survive shared threats
  - recover from scarcity or mistakes
  - persist or rebuild together
- Architectural priority:
  - session authority
  - inventory/resource truth
  - co-op readability and recovery
- First system that breaks:
  - desync, griefing friction, or resource-state ambiguity
- Example inference:
  - `Don't Starve Together` foregrounds fight/farm/build/explore cooperation and survival style expression.

### Auto-battler
- Dominant loop:
  - draft or shop
  - place units on a small board
  - resolve the round automatically
  - adapt the roster or economy
- Architectural priority:
  - draft economy
  - board state clarity
  - resolution logs
- First system that breaks:
  - pool opacity or board rules become hard to read
- Example inference:
  - `Teamfight Tactics` foregrounds shop economy, board placement, and round-to-round adaptation.

### Cozy sim
- Dominant loop:
  - perform low-stress routine
  - improve home/farm/island
  - strengthen attachment to place and people
  - unlock more personal expression
- Architectural priority:
  - schedule/state legibility
  - low-friction traversal and UI
  - persistent environmental change
- First system that breaks:
  - chores become grind or interface friction overwhelms warmth
- Example inference:
  - `Stardew Valley` foregrounds farm building, community relationships, caves, and player-chosen routine breadth.
  - `Animal Crossing: New Horizons` foregrounds building an island paradise, crafting, customization, and persistent shared island state.

### Deckbuilder roguelike
- Dominant loop:
  - enter encounter
  - sequence a small hand of options
  - draft or route into a more specialized deck
  - survive long enough for synergies to matter
- Architectural priority:
  - deterministic combat state clarity
  - reward-pool health
  - card/data separation from runtime encounter state
- First system that breaks:
  - one archetype dominates or combat state becomes unreadable under stacked effects
- Example inference:
  - `Slay the Spire` foregrounds route planning, intent readability, and card additions or removals that keep deck shape meaningful.
  - `Balatro` foregrounds compact rules, score-combo escalation, and the thrill of strong synergies without losing immediate legibility.

### Extraction-lite
- Dominant loop:
  - kit up
  - enter high-risk space
  - decide how much more to risk
  - extract or lose the run's gains
- Architectural priority:
  - economy trust
  - loot authority
  - extraction fairness and information clarity
- First system that breaks:
  - unfair death, exploit economy, or unreadable extraction state
- Example inference:
  - `Hunt: Showdown` foregrounds sound cues, extraction pressure, and high-value objective escape timing.

### Grand strategy
- Dominant loop:
  - choose a long-horizon plan
  - react to events and diplomacy
  - expand or stabilize influence
  - preserve the campaign or run
- Architectural priority:
  - realm state
  - diplomacy and event systems
  - campaign-scale save trust
- First system that breaks:
  - UI or state becomes too dense to reason about
- Example inference:
  - `Crusader Kings III` foregrounds character-driven dynasties and long-horizon state.
  - `Stellaris` foregrounds empire-scale simulation and macro progression.

### Survivorlike
- Dominant loop:
  - survive movement pressure
  - gain frequent upgrades
  - become stronger while enemy density rises
  - hold on long enough for build identity to emerge
- Architectural priority:
  - scale-safe enemy and projectile representation
  - clutter control
  - short-loop reward cadence
- First system that breaks:
  - framerate or visual readability collapses before build expression becomes interesting
- Example inference:
  - `Vampire Survivors` foregrounds enemy density, automated or low-input attacks, and escalating choice cadence.
  - `Brotato` foregrounds short runs, arena compactness, and upgrade readability under heavy pressure.

### Narrative adventure
- Dominant loop:
  - advance scene
  - make character-defining choices
  - update relationships and state
  - pay off consequences later
- Architectural priority:
  - dialogue/state tracking
  - narrative content pipeline
  - consequence visibility without branch explosion
- First system that breaks:
  - content throughput or hidden state bugs
- Example inference:
  - `Life is Strange` foregrounds ordinary characters with extraordinary powers and choice-driven consequences.
  - `Pentiment` foregrounds authored historical setting, narrative investigation, and heavy content craft.

### Platformer
- Dominant loop:
  - read space
  - execute movement
  - fail quickly
  - retry with clearer mastery
- Architectural priority:
  - movement feel
  - camera support
  - checkpoint cadence
- First system that breaks:
  - latency, camera mismatch, or unclear landing affordances
- Example inference:
  - `Dead Cells` also shows the action-platformer side of this genre family, where movement and combat share the same readability budget.

### Puzzle
- Dominant loop:
  - observe rule
  - test hypothesis
  - learn the hidden constraint
  - recombine rules for a new twist
- Architectural priority:
  - rule clarity
  - teach/test/twist sequencing
  - misunderstanding instrumentation
- First system that breaks:
  - players solve by accident or fail to learn the intended rule
- Example inference:
  - `Portal 2` foregrounds puzzle elements, chambers, and a much larger sequence of authored test spaces; this supports the classic teach-and-escalate structure.

### Stealth
- Dominant loop:
  - scout a space
  - observe patrols and visibility
  - manipulate noise, timing, or line of sight
  - execute the objective
- Architectural priority:
  - AI perception
  - suspicion states
  - level geometry and route readability
- First system that breaks:
  - detection feels arbitrary instead of readable
- Example inference:
  - `HITMAN World of Assassination` foregrounds detection fairness, patrol logic, and sandbox objective solving.

### Colony sim
- Dominant loop:
  - set colony priorities
  - watch autonomous agents execute under pressure
  - absorb a crisis
  - stabilize into a more capable settlement
- Architectural priority:
  - agent/job priority visibility
  - simulation state trust across long sessions
  - crisis readability
- First system that breaks:
  - players stop understanding why agents act or why the colony is failing
- Example inference:
  - `RimWorld` foregrounds emergent stories through needs, incidents, and autonomous colonist behavior.
  - `Against the Storm` foregrounds repeated settlement cycles, pressure systems, and management clarity under varied conditions.

### City-builder
- Dominant loop:
  - zone or place a district
  - provide services and transport
  - inspect demand and bottlenecks
  - rebalance the city
- Architectural priority:
  - simulation legibility
  - transport/pathing clarity
  - overlays and inspection tools
- First system that breaks:
  - the city becomes unreadable before the simulation becomes interesting
- Example inference:
  - `Cities: Skylines II` foregrounds zoning, traffic, and city-scale simulation clarity.

### Life sim
- Dominant loop:
  - create or choose a character and home
  - follow a routine
  - personalize identity and relationships
  - unlock new life changes
- Architectural priority:
  - character and household state
  - calendar or schedule systems
  - relationship graphs and customization ownership
- First system that breaks:
  - routine turns into chores or state becomes opaque
- Example inference:
  - `The Sims 4` foregrounds character creation, household expression, and life-state progression.
  - `Animal Crossing: New Horizons` foregrounds place attachment, customization, and low-pressure social routines.

### Hero shooter
- Dominant loop:
  - choose a hero
  - contest an objective
  - coordinate with the team
  - swap or adapt to counterplay
- Architectural priority:
  - hero kit identity
  - objective and map rules
  - network authority and readability
- First system that breaks:
  - heroes blur together or the objective becomes unreadable at speed
- Example inference:
  - `Overwatch 2` foregrounds role clarity, teamfight readability, and objective pacing.

### Soulslike
- Dominant loop:
  - explore a dangerous space
  - read telegraphs
  - commit stamina
  - recover after risk
- Architectural priority:
  - telegraph windows and stamina
  - checkpoint/recovery rules
  - world gating and shortcut support
- First system that breaks:
  - punishment feels arbitrary instead of instructive
- Example inference:
  - `ELDEN RING` foregrounds stamina commitment, exploration pressure, and learning through repeated risk.

### Factory automation
- Dominant loop:
  - source inputs
  - transform them through a chain
  - diagnose bottlenecks
  - scale into more complex production
- Architectural priority:
  - throughput visibility
  - composable simulation units
  - build and debugging tooling
- First system that breaks:
  - scale turns the factory unreadable or too expensive to simulate
- Example inference:
  - `Factorio` foregrounds production chains, logistic clarity, and the satisfaction of solving bottlenecks at scale.
  - `Satisfactory` foregrounds the same throughput thinking in 3D, raising the cost of readability and placement ergonomics.

### Metroidvania
- Dominant loop:
  - explore until a gate stops progress
  - gain a traversal ability
  - return to old spaces with new access
  - deepen world understanding through new paths
- Architectural priority:
  - world graph and gate ownership
  - spatial memory support
  - meaningful backtracking reward
- First system that breaks:
  - gates feel arbitrary or the world stops being memorable enough to reward return play
- Example inference:
  - `Metroid Dread` foregrounds traversal gating, pursuit pressure, and directed return flow.
  - `Hollow Knight` foregrounds mood-driven exploration, world memory, and movement mastery that recontextualizes old paths.

### Tactical RPG
- Dominant loop:
  - forecast consequences
  - commit a turn plan
  - absorb the result
  - grow future options
- Architectural priority:
  - forecast readability
  - rules clarity
  - controlled complexity growth
- First system that breaks:
  - choice overload or rules opacity
- Example inference:
  - `Fire Emblem Engage` explicitly discusses balancing flashy new powers against square-grid tactics so the tactic itself does not break.
