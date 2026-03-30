# Genre Maturity

## Date
- 2026-03-29

## Summary
- This framework explains how to take the repo's supported genre families from a first validated slice to a deeper, production-ready support model.
- It is not a clone guide. It is a maturity guide: what to instrument, what to scale, what to keep readable, and what to prove before the genre is considered truly supported.
- The intent is to raise every supported genre family from "starter preset" to "architecturally strong enough to survive a real project".

## Primary sources
- [Genre Guide](./genre-guide.md)
- [Genre Patterns](./genre-patterns.md)
- [Genre Examples](./genre-examples.md)
- [MDA framework paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)
- [GameFlow paper](https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf)
- [PENS / SDT overview](https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/)
- [Microsoft Gaming Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines)
- [Accessible Games Initiative](https://accessiblegames.com/)

## Why this matters to this repo
- The repo already has genre presets, architecture notes, and first-slice guidance. What it still needs is a stronger answer to "what does mature support for this genre actually look like?"
- Without a deeper layer, the system can still drift into "good starter, weak long-term support". That is fine for a prototype template, but not for a studio OS that claims multi-genre depth.
- This framework gives Codex a higher-resolution target: not just the first room, but the information budget, state model, performance envelope, economy shape, accessibility surface, and content pipeline that a real project needs.

## Decision impact
- Use this framework after the genre preset, genre plan, and development playbook, but before a feature brief becomes implementation work.
- Use it when you want to compare two genres, mature one genre into a larger project, or decide whether a hybrid genre has a real ownership model.
- Keep the matching preset, example matrix, playbook, and architecture note synchronized whenever this framework changes.

## How to use this framework
1. Read the genre preset and the matching architecture note.
2. Read the development playbook for the first slice shape.
3. Read this framework to understand what "good at scale" looks like.
4. Write a feature brief that states the first slice, the scale target, and the first thing that will break if the genre is shallow.
5. Build a small slice, then add the minimum system needed to prove the deeper genre promise.

## Theoretical pillars for mature genre support
- `Dominant loop`: what the player repeats, and why the repetition stays interesting.
- `Information budget`: how much state the player can read before the genre becomes noisy.
- `State ownership`: which systems own persistent truth, session truth, and presentation truth.
- `Reward cadence`: how often the genre rewards the player, and whether that cadence matches the loop.
- `Failure recovery`: how the genre teaches, punishes, or resets without feeling arbitrary.
- `Content throughput`: how much authored content the genre demands to stay fresh.
- `Performance envelope`: how many entities, effects, or simulations the genre can support without collapsing readability.
- `Accessibility envelope`: what must stay legible for players with different input, timing, or sensory needs.
- `Validation ladder`: what must be proven in a smoke test, a playtest, a balancing pass, and a ship-readiness pass.

## Software pattern portfolio
- Mature genre support also needs a named software pattern portfolio, not just a genre loop.
- The portfolio should say whether the genre is primarily owned by state projection, deterministic resolution, authority split, graph routing, scheduler/queue, spawn/pool/instance, or perception/suspicion logic.
- If the genre cannot name its software pattern family, it usually cannot explain its scaling risks or its first brittle system.

## Maturity ladder
### Level 1: first slice
- One loop, one failure mode, one recovery path.
- Enough to prove that the genre label is real, not just decorative.

### Level 2: genre support
- Multiple systems start to talk to each other.
- The player can explain why they won, lost, or changed strategy.

### Level 3: genre maturity
- The genre has clear state ownership, tuning surfaces, and content rules.
- The support surface includes UI, save, balance, telemetry, and performance considerations.

### Level 4: multi-engine parity
- The genre can be represented in Godot, Unity, and Unreal without collapsing into the least common denominator.
- Each engine uses its own best-fit architecture while preserving the same design promise.

## Genre family support map

### Action roguelite
- Mature support means encounter grammar, enemy taxonomy, build telemetry, and meta-progression are all intentional.
- The advanced support target is not just "one room and one enemy". It is "run variety, pressure readability, and build variance all stay healthy over many runs."

### Deckbuilder roguelike
- Mature support means card/effect state is deterministic, reward pools stay healthy, and route choice remains meaningful.
- The advanced support target is a clear deck identity model, explicit stack rules, and logs that explain why a turn succeeded or failed.

### Co-op survival
- Mature support means session authority, shared inventory truth, revive/recovery, and grief resistance are designed together.
- The advanced support target is a system where co-op coordination feels natural, not like a netcode patch on a solo game.

### Auto-battler
- Mature support means economy balance, draft pool health, board readability, and round resolution logs are all aligned.
- The advanced support target is a board state that stays explainable even when the underlying simulation becomes complex.

### Cozy sim
- Mature support means routine variation, place attachment, relationship state, and friction-light UI all support warmth.
- The advanced support target is a game that feels lived in, not merely scheduled.

### Extraction-lite
- Mature support means loot authority, raid fairness, extraction clarity, and anti-exploit economy rules are explicit.
- The advanced support target is a risk economy players can trust even when they lose.

### Grand strategy
- Mature support means campaign memory, diplomacy, event pacing, and state compression stay readable at scale.
- The advanced support target is a strategic UI that keeps the campaign comprehensible while the simulation remains deep.

### Survivorlike
- Mature support means entity density, projectile clutter, upgrade cadence, and performance-safe representation stay in balance.
- The advanced support target is a pressure loop that can scale up without turning into unreadable noise.

### Narrative adventure
- Mature support means branch containment, dialogue ownership, consequence visibility, and content throughput are controlled.
- The advanced support target is authored consequence that feels meaningful without exploding into unmaintainable state.

### Platformer
- Mature support means movement grammar, camera support, hazard rhythm, and restart cadence are tuned together.
- The advanced support target is a movement language the player can feel immediately and master over time.

### Puzzle
- Mature support means rule teaching, hinting, twist design, and misunderstanding recovery are explicit.
- The advanced support target is a puzzle system that teaches itself without spoiling itself.

### Stealth
- Mature support means perception models, suspicion states, patrol grammar, and route planning are readable.
- The advanced support target is stealth that rewards observation and manipulation instead of guesswork.

### Colony sim
- Mature support means job priorities, event visibility, crisis recovery, and save trust all survive long sessions.
- The advanced support target is a colony where players can diagnose why the simulation failed.

### City-builder
- Mature support means zoning, demand curves, transport/pathing, overlays, and diagnostics are all first-class.
- The advanced support target is a city the player can troubleshoot from the map, not just admire from afar.

### Factory-automation
- Mature support means throughput tracing, logistics visualization, scale tooling, and simulation budgets are explicit.
- The advanced support target is a factory the player can debug like a system, not just place like a decoration.

### Life sim
- Mature support means routine variation, relationship graphs, calendar state, and personalization keep evolving.
- The advanced support target is an identity-driven simulation that supports long-term attachment.

### Hero shooter
- Mature support means role kits, objective pacing, map readability, telemetry, and counterplay all stay visible.
- The advanced support target is a hero identity system that is easy to learn and hard to master without confusion.

### Metroidvania
- Mature support means world graph ownership, gate clarity, shortcut rewards, and traversal memory are deliberate.
- The advanced support target is a map that changes meaning after each ability unlock.

### Soulslike
- Mature support means telegraph windows, stamina economy, checkpoint fairness, and shortcut economy are tuned together.
- The advanced support target is difficulty that feels earned because the rules are readable.

### Tactical RPG
- Mature support means forecast UI, terrain value, turn consequence, and build density are balanced together.
- The advanced support target is strategy where commitment is informed rather than hidden.

## Hybrid genre guidance
- Pick one genre to own the first 10 minutes, the loss loop, and the core tuning model.
- Let the secondary genre modify texture, not replace the primary loop.
- If two genres compete for the same first-slice budget, the project is not ready to be hybrid yet.

## Validation expectations
- A mature genre support surface should be able to answer:
  - What is the dominant loop?
  - What is the first system that breaks when the genre is shallow?
  - What must stay readable under scale?
  - What is the failure recovery model?
  - What does the player need to understand before the second session?
- If those questions cannot be answered clearly, the genre is still in concept or first-slice territory.

## Related references
- `docs/reference/genre-presets.md`
- `genre-guide.md`
- `genre-patterns.md`
- `genre-examples.md`
- `studio/docs/active/genre-starter.md`
