# Genre Plan Example

## Scope
- A tactical RPG with one skirmish encounter, one readable forecast, and one small build choice.

## Baseline
- The current design idea is still a genre label, not a buildable plan.
- The team knows it wants tactical depth, but it has not yet named the player outcome, the owner of truth, or the first thing that will break if the plan is shallow.

## Decision order
1. Name the player outcome.
2. Name the genre family and contrast set.
3. Name the dominant tension and loop ladder.
4. Name the canonical owner and projection path.
5. Name the accessibility and performance envelope.
6. Name the first slice and first failure mode.

## Example plan

### Player outcome
- The player should feel clever because each turn is a forecast puzzle, not a reaction test.

### Genre family
- `tactical-rpg`

### Dominant tension
- Safe repositioning versus committing to a damaging action.

### Contrast set
- `Fire Emblem Engage`
- `Into the Breach`
- `Triangle Strategy`

### Loop ladder
- Move into range -> preview outcomes -> commit a turn -> resolve -> recover -> upgrade -> repeat.

### Canonical owner
- The combat state owns turn order, action legality, range, and damage truth.
- The UI only projects the forecast and the consequences.
- The save system only projects durable campaign state, not temporary combat truth.

### Mechanics / dynamics / aesthetics
- Mechanics: turn order, movement, damage, status effects, and build choices.
- Dynamics: forecasted commitment, tradeoffs in positioning, and long-term party composition.
- Aesthetics: tension, mastery, readable consequence, and tactical satisfaction.

### Accessibility envelope
- Forecasts must be readable at a glance.
- Turn prompts must be keyboard and controller friendly.
- Color should never be the only way to distinguish threat, range, or status.

### Performance envelope
- The first scale lever is grid and unit count, not fancy visuals.
- Keep the combat log, threat display, and forecast projection cheap to update.

### First slice
- One small skirmish on a compact grid.
- One player unit with one meaningful ability.
- Two enemy archetypes with readable turns.
- One objective that ends the fight cleanly.

### Risks
- Decision paralysis if the forecast is too dense.
- UI clutter if every combat detail owns its own display.
- Slow turns if the plan adds too many status systems before the baseline is fun.

### Validation
- The player can explain why a move worked or failed.
- The player can name the owner of combat truth.
- The player can tell what will happen before pressing confirm.
- The player can recover from a loss without confusion.

## Genre adaptation notes

| Genre | What changes in the plan |
|---|---|
| `co-op-survival` | plan around shared scarcity, session authority, and recovery rules |
| `city-builder` | plan around demand curves, bottlenecks, and diagnostic overlays |
| `puzzle` | plan around teach/test/twist sequencing and hinting rules |
| `stealth` | plan around patrol readability, suspicion states, and route planning |

## Good agent prompts
- Write a genre plan for a tactical RPG that names the player outcome, loop ladder, state owner, accessibility envelope, and first broken system.
- Turn this genre preset into a buildable plan before the first feature brief.
- Design a genre plan that makes the first slice prove the core fantasy instead of the whole game.

## Validation
- The plan names the outcome, contrast set, loop ladder, owner, envelope, and first failure mode.
- The plan can be read without needing the implementation code.
- The plan can be turned into a feature brief and a QA matrix without inventing missing details.

## Related docs
- `docs/reference/genre-plan.md`
- `docs/research/game-development/genre/genre-plan.md`
