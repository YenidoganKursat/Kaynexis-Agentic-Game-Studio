# Genre Presets

Use this page when you want to choose a genre quickly without reading every preset file.

The easiest path is:

```bash
python3 scripts/codex_studio.py init
```

That guided setup shows the same options in a simple menu and then creates `studio/docs/active/genre-starter.md` for the chosen genre.

For deeper design references, also read:

- `docs/research/game-development/genre/genre-design-pattern-catalog.md`
- `docs/research/game-development/genre/genre-example-matrix.md`

## Quick chooser

| Genre slug | Best fit | Suggested first slice | Watch first |
|---|---|---|---|
| `action-roguelite` | Repeatable combat runs with build variety | One combat room, two enemy roles, one upgrade choice | Run variety collapse |
| `deckbuilder-roguelike` | Run-based drafting, sequencing, and route-planning tension | One combat run with a tiny deck and one draft reward | Solved decks and unreadable combat states |
| `co-op-survival` | Shared pressure and resource scarcity | Two-player join flow plus one survive-the-night loop | Desync pain |
| `auto-battler` | Draft economy, small-board placement, and round resolution | One draft or shop phase plus one board | Roster opacity |
| `cozy-sim` | Low-stress routine and attachment loops | One short daily routine with a visible improvement | Excessive grind |
| `extraction-lite` | High-risk session stakes and stash economy | One raid, one extraction point, one stash outcome | Economy exploits |
| `grand-strategy` | Long-horizon realm planning, diplomacy, and campaign state | One realm turn with one policy or diplomacy choice | UI density |
| `survivorlike` | Movement-first survival against dense enemy waves | One arena, one auto-attack, one level-up choice | Visual clutter and perf collapse |
| `narrative-adventure` | Story-first pacing and stateful progression | One short scene with one branching conversation | Branching explosion |
| `platformer` | Movement mastery and cadence | One teach-test-twist movement gauntlet | Camera frustration |
| `puzzle` | Rule clarity and satisfying player insight | One rule taught, tested, then twisted | Rule ambiguity |
| `stealth` | Patrol readability, suspicion states, and objective routing | One patrol space with one readable detection rule | Detection feels arbitrary |
| `colony-sim` | Agent priorities, crisis recovery, and layered simulation | One small colony with one need, one job source, one crisis | Simulation opacity |
| `city-builder` | City-scale planning, demand curves, and transport bottlenecks | One district with one solvable bottleneck | Unreadable city-scale bottlenecks |
| `factory-automation` | Throughput, logistics, and scale through player-built systems | One production chain with one solvable bottleneck | Unreadable logistics |
| `life-sim` | Routine, identity, relationships, and long-horizon attachment | One character routine with one visible life change | Chores and relationship opacity |
| `hero-shooter` | Role kits, objective play, and teamfight readability | One hero with one objective mode | Heroes blur together |
| `metroidvania` | Exploration, traversal gates, and return loops | One mini-zone with one traversal unlock and one shortcut | Arbitrary gating |
| `soulslike` | Telegraph reading, stamina commitment, and recovery mastery | One small duel with one checkpoint | Punishment feels arbitrary |
| `tactical-rpg` | Forecastable combat and build depth | One small skirmish with one meaningful build choice | Decision paralysis |

## Good defaults

- If you care most about feel and replayable combat, start with `action-roguelite`.
- If you care most about route planning, card sequencing, and compact state clarity, start with `deckbuilder-roguelike`.
- If you care most about routine, readability, and calm progression, start with `cozy-sim`.
- If you care most about teaching a single idea well, start with `puzzle`.
- If you care most about precision movement, start with `platformer`.
- If you care most about authored story flow, start with `narrative-adventure`.
- If you care most about teamwork and survival pressure, start with `co-op-survival`.
- If you care most about draft economy and board resolution, start with `auto-battler`.
- If you care most about risk economy and session stakes, start with `extraction-lite`.
- If you care most about long-horizon realm planning, start with `grand-strategy`.
- If you care most about swarm pressure, build escalation, and short-run intensity, start with `survivorlike`.
- If you care most about systemic management, agent priorities, and recoverable disasters, start with `colony-sim`.
- If you care most about city-scale planning and transport bottlenecks, start with `city-builder`.
- If you care most about throughput puzzles, logistics, and scale, start with `factory-automation`.
- If you care most about routine, identity, and relationship state, start with `life-sim`.
- If you care most about role kits and objective matches, start with `hero-shooter`.
- If you care most about world memory, traversal gating, and exploration payoff, start with `metroidvania`.
- If you care most about patrol readability and route control, start with `stealth`.
- If you care most about stamina mastery and telegraph readability, start with `soulslike`.
- If you care most about tactical clarity and build planning, start with `tactical-rpg`.
