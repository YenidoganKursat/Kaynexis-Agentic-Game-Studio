# Genre Presets

Use this page when you want to choose a genre quickly without reading every preset file.

The easiest path is:

```bash
python3 scripts/start_game_studio.py
```

That guided setup shows the same options in a simple menu and then creates `studio/docs/active/genre-starter.md` for the chosen genre.

## Quick chooser

| Genre slug | Best fit | Suggested first slice | Watch first |
|---|---|---|---|
| `action-roguelite` | Repeatable combat runs with build variety | One combat room, two enemy roles, one upgrade choice | Run variety collapse |
| `co-op-survival` | Shared pressure and resource scarcity | Two-player join flow plus one survive-the-night loop | Desync pain |
| `cozy-sim` | Low-stress routine and attachment loops | One short daily routine with a visible improvement | Excessive grind |
| `extraction-lite` | High-risk session stakes and stash economy | One raid, one extraction point, one stash outcome | Economy exploits |
| `narrative-adventure` | Story-first pacing and stateful progression | One short scene with one branching conversation | Branching explosion |
| `platformer` | Movement mastery and cadence | One teach-test-twist movement gauntlet | Camera frustration |
| `puzzle` | Rule clarity and satisfying player insight | One rule taught, tested, then twisted | Rule ambiguity |
| `tactical-rpg` | Forecastable combat and build depth | One small skirmish with one meaningful build choice | Decision paralysis |

## Good defaults

- If you care most about feel and replayable combat, start with `action-roguelite`.
- If you care most about routine, readability, and calm progression, start with `cozy-sim`.
- If you care most about teaching a single idea well, start with `puzzle`.
- If you care most about precision movement, start with `platformer`.
- If you care most about authored story flow, start with `narrative-adventure`.
- If you care most about teamwork and survival pressure, start with `co-op-survival`.
- If you care most about risk economy and session stakes, start with `extraction-lite`.
- If you care most about tactical clarity and build planning, start with `tactical-rpg`.
