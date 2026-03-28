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
| `cozy-sim` | Low-stress routine and attachment loops | One short daily routine with a visible improvement | Excessive grind |
| `extraction-lite` | High-risk session stakes and stash economy | One raid, one extraction point, one stash outcome | Economy exploits |
| `survivorlike` | Movement-first survival against dense enemy waves | One arena, one auto-attack, one level-up choice | Visual clutter and perf collapse |
| `narrative-adventure` | Story-first pacing and stateful progression | One short scene with one branching conversation | Branching explosion |
| `platformer` | Movement mastery and cadence | One teach-test-twist movement gauntlet | Camera frustration |
| `puzzle` | Rule clarity and satisfying player insight | One rule taught, tested, then twisted | Rule ambiguity |
| `colony-sim` | Agent priorities, crisis recovery, and layered simulation | One small colony with one need, one job source, one crisis | Simulation opacity |
| `factory-automation` | Throughput, logistics, and scale through player-built systems | One production chain with one solvable bottleneck | Unreadable logistics |
| `metroidvania` | Exploration, traversal gates, and return loops | One mini-zone with one traversal unlock and one shortcut | Arbitrary gating |
| `tactical-rpg` | Forecastable combat and build depth | One small skirmish with one meaningful build choice | Decision paralysis |

## Good defaults

- If you care most about feel and replayable combat, start with `action-roguelite`.
- If you care most about route planning, card sequencing, and compact state clarity, start with `deckbuilder-roguelike`.
- If you care most about routine, readability, and calm progression, start with `cozy-sim`.
- If you care most about teaching a single idea well, start with `puzzle`.
- If you care most about precision movement, start with `platformer`.
- If you care most about authored story flow, start with `narrative-adventure`.
- If you care most about teamwork and survival pressure, start with `co-op-survival`.
- If you care most about risk economy and session stakes, start with `extraction-lite`.
- If you care most about swarm pressure, build escalation, and short-run intensity, start with `survivorlike`.
- If you care most about systemic management, agent priorities, and recoverable disasters, start with `colony-sim`.
- If you care most about throughput puzzles, logistics, and scale, start with `factory-automation`.
- If you care most about world memory, traversal gating, and exploration payoff, start with `metroidvania`.
- If you care most about tactical clarity and build planning, start with `tactical-rpg`.
