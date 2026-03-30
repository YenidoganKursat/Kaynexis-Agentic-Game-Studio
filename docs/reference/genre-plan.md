# Genre Plan Guide

## Summary
- Use this guide when a genre preset needs to become a buildable game plan instead of just a label or a feature brief stub.
- The plan sits between genre selection and feature briefing: it names the player outcome, dominant tension, contrast set, loop ladder, ownership model, accessibility envelope, and validation ladder before implementation starts.
- Treat each genre as a different planning shape. The same fields stay present, but the emphasis changes by genre family.

## Primary sources
- `docs/research/game-development/genre/genre-plan.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`
- `docs/research/game-development/genre/genre-maturity.md`
- [MDA framework paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)
- [GameFlow paper](https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf)
- [PENS / SDT overview](https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/)
- [Microsoft Gaming Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines)
- [Accessible Games Initiative](https://accessiblegames.com/)

## Why this matters to this repo
- The repo already has genre presets, pattern catalogs, maturity guidance, and starter docs.
- What it still needs is a canonical planning schema that tells an agent how to turn a genre into a concrete plan without guessing the loop, the owner, the contrast set, or the first failure mode.
- Without this schema, the team can still drift into "genre label -> feature brief" with no shared model for the player outcome, accessibility envelope, performance envelope, or validation ladder.

## Decision impact
- Use this guide after choosing a genre preset and before writing a feature brief.
- Use it whenever the request is "how do we plan this genre?" or "what should the plan for this genre include?"
- Keep the genre guide, genre plan, pattern catalog, example matrix, and starter note synchronized when the planning model changes.

## Planning flow

```mermaid
flowchart LR
  P["Genre preset"] --> C["Contrast set"]
  C --> S["Genre plan schema"]
  S --> F["Feature brief"]
  F --> T["Test / QA matrix"]
  T --> I["Implementation"]
```

## Plan schema

1. Player outcome and fantasy
2. Genre family and contrast set
3. Dominant tension and loop ladder
4. Mechanics / dynamics / aesthetics mapping
5. Canonical owner and projection boundary
6. Accessibility envelope
7. Performance envelope
8. Content throughput and economy shape
9. Validation ladder
10. Risks and fallback plan

### 1. Player outcome and fantasy
- State the experience the player should leave with.
- Use outcome language the player would understand, not engine language.
- If the outcome is unclear, the rest of the plan will be vague too.

### 2. Genre family and contrast set
- Name the genre family and one or two contrast games.
- The contrast set keeps the plan grounded in a real shape instead of a vague mood.
- If you cannot name the contrast set, the genre is probably not ready for planning yet.

### 3. Dominant tension and loop ladder
- Name the one tension the player repeats.
- Write the session loop, then the run loop, then the campaign or meta loop if one exists.
- The plan should show how the loop grows without losing readability.

### 4. Mechanics / dynamics / aesthetics mapping
- Start from the player feeling and work backward to the rules that produce it.
- Use the MDA chain to keep the plan from becoming implementation-first.
- A good plan can explain why the player should care before it lists systems.

### 5. Canonical owner and projection boundary
- Name the system that owns truth.
- Name the systems that only project, mirror, or summarize that truth.
- If UI, save, or telemetry starts owning gameplay truth, the plan needs to be corrected.

### 6. Accessibility envelope
- Note the controls, text, audio, motion, and timing expectations that must remain legible.
- Use the XAG and Accessible Games tags as a scoping tool, not as a late add-on.
- If the genre depends on rapid inputs, hidden state, or dense presentation, call that out here.

### 7. Performance envelope
- State the first scale lever before the first content burst.
- Mention the likely pressure point: entities, effects, UI density, simulation, network sync, or animation.
- If the plan cannot name the first lever, it is not ready to scale.

### 8. Content throughput and economy shape
- Say how much authored content the genre needs to stay fresh.
- Note whether the content cost is in encounters, dialogue, routes, maps, items, or simulation events.
- If the genre has an economy, state the trusted sinks and sources.

### 9. Validation ladder
- Write the smallest smoke that proves the genre is real.
- Write the first playtest question.
- Write the first balance or tuning pass.
- Write the first ship-readiness check.

### 10. Risks and fallback plan
- Name the first thing that will break if the genre is shallow.
- Name the fallback path if the first slice does not prove the fantasy.
- Keep one explicit cut path so the plan can shrink without losing its core.

## Genre adapters

| Genre family | Plan emphasis | First slice proof | First thing not to overbuild |
|---|---|---|---|
| `action-roguelite` | encounter readability, build variety, reset value | one room with one dodge, one attack, one upgrade choice | meta systems before combat clarity |
| `deckbuilder-roguelike` | draw/discard state, route tension, reward pool health | tiny deck, one encounter, one draft reward | card count before state readability |
| `co-op-survival` | shared scarcity, session authority, recovery | two-player join flow and one survive-the-night loop | content breadth before sync trust |
| `auto-battler` | draft economy, board readability, round resolution | one shop or draft phase and one board | synergy complexity before board legibility |
| `cozy-sim` | routine texture, attachment, low-friction progression | one short daily routine with one visible improvement | grind before warmth |
| `extraction-lite` | raid risk, stash safety, extraction clarity | one raid, one extraction point, one stash result | exploits before trust |
| `grand-strategy` | campaign state, diplomacy, event pacing | one realm turn with one policy or diplomacy choice | UI density before readable state |
| `survivorlike` | swarm readability, upgrade cadence, scale safety | one arena, one auto-attack, one level-up choice | visual clutter before perf budget |
| `narrative-adventure` | scene cadence, branch clarity, content throughput | one short scene with one branching conversation | branching explosion before authored flow |
| `platformer` | movement feel, camera support, restart cadence | one teach-test-twist movement gauntlet | camera frustration before input clarity |
| `puzzle` | rule clarity, hinting, failure recovery | one rule taught, tested, then twisted | rule ambiguity and hint overuse |
| `stealth` | patrol readability, suspicion states, route planning | one patrol space with one readable detection rule | arbitrary detection before fairness |
| `colony-sim` | agent priorities, crisis recovery, layered simulation | one small colony with one need, one job source, one crisis | simulation opacity before diagnostics |
| `city-builder` | demand curves, transport bottlenecks, diagnosis | one district with one solvable bottleneck | unreadable city-scale systems before overlays |
| `factory-automation` | throughput, logistics, scale tools | one production chain with one solvable bottleneck | unreadable logistics before tool support |
| `life-sim` | routine, identity, relationships, long-horizon attachment | one character routine with one visible life change | chores before attachment |
| `hero-shooter` | role kits, objective play, teamfight readability | one hero with one objective mode | heroes blurring together before role clarity |
| `metroidvania` | traversal gates, world memory, return loops | one mini-zone with one traversal unlock and one shortcut | arbitrary gating before map memory |
| `soulslike` | telegraph reading, stamina commitment, recovery mastery | one small duel with one checkpoint | punishment before readable recovery |
| `tactical-rpg` | forecast clarity, turn economy, build planning | one small skirmish with one meaningful build choice | decision paralysis before forecast |

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
- `docs/research/game-development/genre/genre-plan.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `docs/examples/genre-plan-example.md`
- `studio/docs/templates/genre-plan.md`
- `studio/docs/active/genre-starter.md`
