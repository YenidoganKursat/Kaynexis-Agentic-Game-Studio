# Genre Planning Schema

## Date
- 2026-03-29

## Summary
- This note defines the planning schema the repo should use when turning a genre preset into a buildable game plan.
- It sits between genre selection and feature briefing: the plan names the player outcome, dominant tension, contrast set, loop ladder, ownership model, accessibility envelope, and validation ladder before implementation starts.
- The same schema works across supported genres, but each genre family emphasizes different risks, different first slices, and different scaling limits.

## Primary sources
- [Genre Guide](./genre-guide.md)
- [Genre Patterns](./genre-patterns.md)
- [Genre Examples](./genre-examples.md)
- [Genre Maturity](./genre-maturity.md)
- [MDA framework paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)
- [GameFlow paper](https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf)
- [PENS / SDT overview](https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/)
- [Microsoft Gaming Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines)
- [Accessible Games Initiative](https://accessiblegames.com/)

## Why this matters to this repo
- The repo already has strong support for genre presets, pattern catalogs, maturity guidance, and starter docs.
- What it still needs is a canonical planning schema that tells an agent how to turn a genre into a concrete plan without guessing the loop, the owner, the contrast set, or the first failure mode.
- Without this schema, the team can still drift into "genre label -> feature brief" with no shared model for the player outcome, accessibility envelope, performance envelope, or validation ladder.

## Decision impact
- Use this note after choosing a genre preset and before writing a feature brief.
- Use it whenever the request is "how do we plan this genre?" or "what should the plan for this genre include?"
- Keep the genre guide, genre plan, pattern catalog, example matrix, and starter note synchronized when the planning model changes.

## What each source contributes
- MDA: start from the desired player outcome and work downward toward the mechanics that produce it.
- GameFlow: keep the plan explicit about clear goals, immediate feedback, control, challenge-skill match, immersion, and social interaction when relevant.
- PENS: make room for competence, autonomy, and relatedness so the genre does not become only mechanically correct.
- Microsoft XAG and Accessible Games Initiative tags: declare the accessibility surface up front, including input, text, audio, motion, and timing constraints.

## Planning signals
- Player outcome: what the player should feel, learn, or accomplish.
- Dominant tension: the core tradeoff that keeps the loop interesting.
- Contrast set: the games or references that prove the plan is grounded.
- Loop ladder: the session loop, the run loop, or the campaign loop.
- Canonical owner: the system that owns truth, and the systems that only project it.
- Accessibility envelope: the controls, text, audio, motion, and timing limits that must remain legible.
- Performance envelope: the entity count, effect count, and scale lever that must stay within budget.
- Validation ladder: the smallest smoke, the first playtest, the first balance pass, and the first ship-readiness check.

## Genre family planning signals

| Genre family | Planning emphasis | First thing to prove | First thing not to overbuild |
|---|---|---|---|
| `action-roguelite` | encounter readability, build variety, reset value | one room with one dodge, one attack, one upgrade choice | meta systems before combat clarity |
| `deckbuilder-roguelike` | draw/discard state, route tension, reward pool health | tiny deck, one encounter, one draft reward | flashy card count before state readability |
| `co-op-survival` | shared scarcity, session authority, recovery | two-player join flow and one survive-the-night loop | content breadth before trust and sync |
| `auto-battler` | draft economy, board readability, round resolution | one shop or draft phase and one board | synergy complexity before board legibility |
| `cozy-sim` | routine texture, attachment, low-friction progression | one short daily routine with one visible improvement | grind and menu friction before warmth |
| `extraction-lite` | raid risk, stash safety, extraction clarity | one raid, one extraction point, one stash result | economy exploits and unclear death states |
| `grand-strategy` | campaign state, diplomacy, event pacing | one realm turn with one policy or diplomacy choice | UI density and unreadable state graphs |
| `survivorlike` | swarm readability, upgrade cadence, scale safety | one arena, one auto-attack, one level-up choice | visual clutter before perf budgets |
| `narrative-adventure` | scene cadence, branch clarity, content throughput | one short scene with one branching conversation | branching explosion before authored flow |
| `platformer` | movement feel, camera support, restart cadence | one teach-test-twist movement gauntlet | camera frustration and input ambiguity |
| `puzzle` | rule clarity, hinting, failure recovery | one rule taught, tested, then twisted | rule ambiguity and hint overuse |
| `stealth` | patrol readability, suspicion states, route planning | one patrol space with one readable detection rule | arbitrary detection and noisy sightlines |
| `colony-sim` | agent priorities, crisis recovery, layered simulation | one small colony with one need, one job source, one crisis | simulation opacity before readable diagnostics |
| `city-builder` | demand curves, transport bottlenecks, diagnosis | one district with one solvable bottleneck | unreadable city-scale systems before simple diagnostics |
| `factory-automation` | throughput, logistics, scale tools | one production chain with one solvable bottleneck | unreadable logistics before tool support |
| `life-sim` | routine, identity, relationships, long-horizon attachment | one character routine with one visible life change | chores and relationship opacity |
| `hero-shooter` | role kits, objective play, teamfight readability | one hero with one objective mode | heroes blurring together before role clarity |
| `metroidvania` | traversal gates, world memory, return loops | one mini-zone with one traversal unlock and one shortcut | arbitrary gating before map memory |
| `soulslike` | telegraph reading, stamina commitment, recovery mastery | one small duel with one checkpoint | punishment without readable recovery |
| `tactical-rpg` | forecast clarity, turn economy, build planning | one small skirmish with one meaningful build choice | decision paralysis before readable forecast |

## How to use the schema
1. Pick the genre preset and its contrast set.
2. Write the player outcome and dominant tension in plain language.
3. Name the loop ladder and the canonical owner before implementation.
4. Pick the first slice that proves the genre and the first system that will break if the genre is shallow.
5. Write the accessibility and performance envelope while the plan is still small.
6. Turn the plan into a feature brief, then into a test plan or QA matrix.

## Example prompts for the agent
- Write a genre plan for a tactical RPG that names the player outcome, loop ladder, state owner, accessibility envelope, and first broken system.
- Plan a city-builder by naming the bottleneck, the diagnostic overlays, and the first district that proves the genre.
- Write a genre plan for a co-op survival game that keeps session authority, shared scarcity, and recovery explicit.
- Turn this genre preset into a buildable plan before the first feature brief.

## Validation
- Name the player outcome, dominant tension, contrast set, and first slice.
- Name the canonical owner and the projection or feedback path if one exists.
- Name the accessibility envelope and the performance envelope.
- Name the first failure mode and the smallest validation loop that proves the plan.

## Related docs
- `docs/reference/genre-plan.md`
- `docs/examples/genre-plan-example.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `studio/docs/templates/genre-plan.md`
- `studio/docs/active/genre-starter.md`
