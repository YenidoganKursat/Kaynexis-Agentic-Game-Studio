# Genre Guide

## Date
- 2026-03-28

## Summary
- This playbook explains how to develop the repo's supported genre families in practice.
- It is not a clone guide. It is a build guide: what to research first, what to prototype first, what usually breaks first, and how to validate the first real slice.
- Treat each genre as a different production system, not a different skin over the same starting plan.

## Primary sources
- [Genre Patterns](./genre-patterns.md)
- [Genre Examples](./genre-examples.md)
- [Dead Cells official site](https://dead-cells.com/)
- [Slay the Spire on Steam](https://store.steampowered.com/app/646570/Slay_the_Spire/)
- [Teamfight Tactics official site](https://teamfighttactics.leagueoflegends.com/)
- [Stardew Valley official site](https://www.stardewvalley.net/)
- [Crusader Kings III official site](https://www.paradoxinteractive.com/games/crusader-kings-iii)
- [HITMAN World of Assassination official site](https://www.hitman.com/)

## Why this matters to this repo
- Genre choice in this repository is not just a label. It changes the first slice, the checklist bundle, the active starter, the validation path, and the research notes that should be read before implementation.
- Without a genre development guide, the repo can still drift into "pick a preset and guess the rest" behavior, which is exactly what the studio OS is trying to prevent.

## Decision impact
- Use this playbook before you write a feature brief for a genre-specific project.
- Update the matching preset, example matrix row, and active genre starter whenever the guidance here changes.
- When a genre becomes a real project, route the first task through the playbook, then through the matching architecture note, and only then into implementation.

## How to use this playbook
- Start with `genre-plan.md` when you need the planning scaffold before the feature brief.
- Then start with the matching architecture note in this folder.
- Read the example matrix to pick one or two contrast sets.
- If you need more than one contrast set, use `docs/examples/genre-gallery-example.md` alongside the matrix.
- Read `genre-patterns.md` when you need to choose the software pattern that should own the dominant tension.
- Use the genre preset to seed active docs.
- Then use the guidance below to choose the first slice, the first risky system, and the first validation path.

## Software pattern selection
- If the genre is about state visibility or consequence, start from `state projection` and `dialogue / branch projection`.
- If the genre is about many repeated things, start from `spawn / pool / instance`.
- If the genre is about round or turn resolution, start from `deterministic resolver` and `board / lane resolution`.
- If the genre is about routing, memory, or campaign history, start from `graph / route model`.
- If the genre is about simulation pressure, start from `scheduler / job queue` and `overlay / diagnostic view`.
- If the genre is about stealth or detection, start from `perception / suspicion FSM`.
- If the chosen software pattern is still unclear after this pass, use the example matrix plus the maturity framework before implementation.

## Shared development sequence for every genre
1. Name the dominant tension.
2. Choose the first player loop that exposes that tension.
3. Define the state ownership boundary.
4. Pick the first system that will break if the genre is shallow.
5. Build the smallest slice that proves the loop.
6. Validate readability, pacing, and failure recovery before adding breadth.
7. Only add adjacent systems after the first slice has a clear win and a clear failure mode.

## Advanced development path
- Once the first slice is stable, move from "does the loop work?" to "what does this genre need at scale?"
- Use [Genre Maturity](./genre-maturity.md) to deepen state ownership, content throughput, performance, accessibility, and validation shape.
- If the main problem becomes genre-shaped performance rather than loop shape, read `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` before reaching for engine micro-optimizations.
- The advanced path should answer whether the genre can survive a larger project without collapsing into generic systems or unreadable state.

## Genre-by-genre guidance

### Action roguelite
- Build around encounter readability, dodge timing, and build variety.
- First slice: one room, one dodge, one attack, one enemy role, one upgrade choice.
- Research first: run structure, invulnerability timing, reward pacing, and difficulty ramps.
- Watch first: if the build can be solved too early or if enemy pressure is visually noisy.
- Validate: a room should be readable at first glance, and losing should teach rather than confuse.

### Deckbuilder roguelike
- Build around sequencing, route choice, and reward-pool health.
- First slice: a tiny deck, one enemy encounter, one draft choice, one map step.
- Research first: card flow, draw/discard state, effect stacking, and route tension.
- Watch first: state unreadability and one dominant deck archetype.
- Validate: the player should always know why a turn won or failed.

### Co-op survival
- Build around shared scarcity, coordination, and recovery.
- First slice: two players, one resource loop, one threat loop, one rebuild action.
- Research first: session authority, inventory truth, revive/recovery, and grief-resistance.
- Watch first: desync, unclear ownership, and too many items before cooperation matters.
- Validate: the team should understand who owns what and how a failed session recovers.

### Auto-battler
- Build around draft economy, board placement, and round resolution.
- First slice: one shop or draft, one board, one round log, one upgrade path.
- Research first: pool health, positional rules, combat resolution, and economy curve.
- Watch first: board opacity and under-explained synergy spikes.
- Validate: the player should understand why the board won before the next draft starts.

### Cozy sim
- Build around routine, attachment, and low-friction progression.
- First slice: one daily routine, one place improvement, one relationship beat.
- Research first: schedule clarity, interaction warmth, and environmental persistence.
- Watch first: grind, menu friction, and chores that feel like chores.
- Validate: the player should feel calmer and more attached after a short session, not more exhausted.

### Extraction-lite
- Build around risk, stash value, and escape pressure.
- First slice: one raid, one extraction, one stash result, one meaningful loss state.
- Research first: economy trust, loot authority, visibility, and escape rules.
- Watch first: unfair deaths, exploit loops, or unclear extraction timing.
- Validate: the player should be able to explain the stakes before taking the raid.

### Grand strategy
- Build around long-horizon plans, diplomacy, and campaign trust.
- First slice: one realm turn, one policy choice, one diplomatic event, one readable consequence.
- Research first: campaign state, interface density, event pacing, and meta-history.
- Watch first: unreadable state and too many systems before the campaign proves itself.
- Validate: a player should be able to describe the current strategic problem in one sentence.

### Survivorlike
- Build around movement pressure, upgrade cadence, and scale-safe performance.
- First slice: one arena, one auto-attack or light input loop, one level-up choice.
- Research first: entity density, projectile clutter, readability, and performance ceilings.
- Watch first: visual chaos and frame drops before the build feels interesting.
- Validate: pressure should rise while readability remains intact.

### Narrative adventure
- Build around scene flow, choice clarity, and authored consequence.
- First slice: one scene, one meaningful choice, one follow-up consequence.
- Research first: dialogue ownership, branching shape, and content throughput.
- Watch first: branch explosion or hidden-state bugs.
- Validate: the player should understand what changed and why it matters later.

### Platformer
- Build around movement feel, camera support, and retry cadence.
- First slice: one movement teaching room, one hazard, one recovery loop.
- Research first: input responsiveness, camera framing, and restart speed.
- Watch first: camera frustration and imprecise movement.
- Validate: failure should feel fast, fair, and informative.

### Puzzle
- Build around one clear rule, one test, and one twist.
- First slice: a puzzle that teaches a rule, applies it, and then changes the condition.
- Research first: affordances, hinting, and misunderstanding recovery.
- Watch first: vague rules and hidden solutions.
- Validate: players should be able to explain the rule in their own words.

### Stealth
- Build around patrol readability, suspicion states, and route planning.
- First slice: one patrol room, one detection rule, one hiding or escape option.
- Research first: visibility, sound, guard logic, and fail-state recovery.
- Watch first: detection that feels arbitrary or noisy.
- Validate: the player should understand why they were seen.

### Colony sim
- Build around job priorities, simulation legibility, and crisis recovery.
- First slice: one small colony, one need, one job source, one incident.
- Research first: agent priorities, simulation update cost, and crisis readability.
- Watch first: opaque simulation and cascading losses the player cannot explain.
- Validate: the player should know why the colony is unstable.

### City-builder
- Build around zoning, transport, and demand curves.
- First slice: one district, one bottleneck, one fix, one visible outcome.
- Research first: demand, traffic, service coverage, and scale tooling.
- Watch first: city-scale opacity and bottlenecks the player cannot diagnose.
- Validate: the player should see cause and effect on the map.

### Factory-automation
- Build around throughput, logistics, and scale tooling.
- First slice: one production chain, one bottleneck, one throughput improvement.
- Research first: conveyor flow, machine graph, resource ratios, and build tools.
- Watch first: unreadable logistics or expensive simulation.
- Validate: the player should be able to trace where the throughput is lost.

### Life sim
- Build around routine, identity, relationships, and long-horizon attachment.
- First slice: one character routine, one relationship beat, one visible life change.
- Research first: social state, time loops, and meaningful daily variation.
- Watch first: chores that do not feel expressive and relationships that lack state.
- Validate: the player should feel their schedule and relationships matter.

### Hero shooter
- Build around role kits, objective play, and teamfight readability.
- First slice: one hero kit, one objective mode, one readable teamfight.
- Research first: role clarity, cooldown pacing, map objective structure, and counterplay.
- Watch first: heroes that blur together or objectives that disappear under combat noise.
- Validate: a player should know what that hero is good at in one line.

### Metroidvania
- Build around traversal unlocks, world memory, and return-path payoff.
- First slice: one mini-zone, one new traversal tool, one shortcut back to a prior door.
- Research first: gate placement, backtracking payoff, and map legibility.
- Watch first: arbitrary gates and dead backtracking.
- Validate: each new traversal tool should meaningfully change map interpretation.

### Soulslike
- Build around telegraph reading, stamina commitment, and recovery fairness.
- First slice: one duel, one checkpoint, one clear shortcut or recovery loop.
- Research first: animation timing, punish windows, respawn loop, and shortcut economy.
- Watch first: punishment that feels arbitrary or hidden.
- Validate: the player should lose because they misread, not because the rules were unclear.

### Tactical RPG
- Build around forecast clarity, positioning, and consequence planning.
- First slice: one skirmish, one meaningful build choice, one forecast UI.
- Research first: turn forecast, mobility budget, damage prediction, and encounter pacing.
- Watch first: decision paralysis or strategy that collapses into one dominant move.
- Validate: players should understand the consequences before they commit.

## How to turn this into work
- If the genre is not yet chosen, pick the genre that best fits the strongest tension.
- If the genre is chosen, write a feature brief for the first slice using the loop above.
- If you are still comparing two genres, use the example matrix plus this playbook to compare the first 10 minutes, the first broken system, and the first validation path.

## Related references
- `genre-patterns.md`
- `genre-examples.md`
- `docs/reference/genre-presets.md`
- `studio/docs/active/genre-starter.md`
- the matching `*-architecture.md` note for the chosen genre
