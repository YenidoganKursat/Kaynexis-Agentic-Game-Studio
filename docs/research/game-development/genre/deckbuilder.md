# Deckbuilder

## Date
- 2026-03-28

## Summary
- Deckbuilder roguelikes fail first on economy and choice quality, not animation polish. The architecture must protect card definition data, encounter pacing, draw/discard state, reward tables, and long-term unlock rules from becoming one tangled blob.
- The dominant loop is:
  - enter an encounter or event
  - spend limited cards and resources
  - survive or optimize the combat outcome
  - draft or modify the deck
  - repeat with a stronger but more fragile build identity
- The first systems that usually break are:
  - deck bloat that erodes identity
  - relic or modifier synergy explosions that trivialize risk
  - unclear draw/discard/exhaust visibility
  - reward pools that stop creating meaningful tension
- This genre wants durable data boundaries:
  - authored card definitions
  - runtime deck state
  - combat resolution state
  - run modifiers and relics
  - durable unlocks or meta content

## Primary sources
- [Slay the Spire on Steam](https://store.steampowered.com/app/646570/Slay_the_Spire/)
- [Balatro on Steam](https://store.steampowered.com/app/2379780/Balatro/)

## Why this matters to this repo
- Deckbuilder tasks in this repo should stop being routed as generic gameplay or generic economy only. They are a blend of data architecture, reward structure, UI clarity, and progression boundaries.
- Agents should explicitly name:
  - what lives in authored card or relic data
  - what lives in current-combat state
  - what lives in current-run state
  - what persists between runs
  - how the player reads the deck, discard pile, hand state, and rewards
- First-slice recommendations should prioritize a small but meaningful draft loop over a huge card list.

## Decision impact
- Future genre presets and feature briefs should call out:
  - deck growth rules
  - card-state visibility
  - modifier stacking rules
  - meta unlock boundaries
- When a project selects this genre, route output should favor combat, economy, save, and UI architecture notes together instead of one discipline alone.
