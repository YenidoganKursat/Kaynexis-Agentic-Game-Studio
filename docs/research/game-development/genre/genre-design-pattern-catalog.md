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
  - cozy sim -> routine legibility, low-friction progression, and environment attachment
  - extraction-lite -> raid fairness, secure economy, and extraction clarity
  - survivorlike -> density readability, scale-safe updates, and upgrade cadence
  - narrative adventure -> state tracking, content throughput, and choice legibility
  - platformer -> movement feel, camera support, and restart cadence
  - puzzle -> teach/test/twist sequencing and misunderstanding analysis
  - colony-sim -> simulation legibility, agent priorities, and crisis recovery
  - factory-automation -> throughput clarity, composable systems, and scale tooling
  - metroidvania -> world-memory support, gate clarity, and return-path payoff
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

## Why this matters to this repo
- Genre choice should shape more than tone. It should change which docs, checklists, and validation loops matter first.
- Agents should stop giving the same first-slice advice to every genre. "Build one room and one enemy" makes sense for action-roguelites, but not for narrative adventure, cozy sim, or puzzle-first games.
- The repo's genre presets are already useful quick starts, but they need a deeper design layer so teams can reason from example loops instead of just genre labels.

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
