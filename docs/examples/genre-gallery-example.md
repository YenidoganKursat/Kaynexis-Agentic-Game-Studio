# Genre Gallery Example

## Purpose
- Use this when a request needs more than one genre contrast set before a feature brief or starter doc is written.
- The goal is not to copy games. The goal is to pick the best design lesson, the first slice, and the first failure mode.

## Selected project shape
- Primary preset: `sandbox-survival`
- Secondary contrasts: `tower-defense`, `4X`, `rhythm-action`

## How to use this gallery
1. Pick one primary card that owns the first 10 minutes.
2. Pick one contrast card that stresses the weakest system.
3. Pick one anti-example that would push the project away from its intended promise.
4. Write the feature brief only after the first slice is clear in plain language.

## Example cards

| Card | Example games | What to study first | First design question | First risk |
|---|---|---|---|---|
| `sandbox-survival` | `Minecraft`, `Valheim` | emergent goals, crafting progression, world persistence | what keeps the player self-directing after the first shelter? | aimless wandering or goal dilution |
| `tower-defense` | `Bloons TD 6` | lane clarity, path pressure, upgrade economy | what makes each wave legible and each upgrade meaningful? | path opacity or trivial stall strategies |
| `4X` | `Civilization VII` | empire-phase transitions, macro pacing, map readability | how does the game compress huge state into a readable turn? | state overload or late-game drag |
| `rhythm-action` | `Hi-Fi RUSH` | beat sync, audiovisual timing, readable combo windows | what owns timing truth: music, animation, or combat state? | sync drift or inaccessible timing |
| `management-sim` | `Two Point Campus` | staff/student simulation, layout tools, service diagnostics | which problems can the player solve from one map view? | hidden service failures or tool sprawl |
| `immersive-sim` | `Prey`, `Deus Ex: Mankind Divided` | affordance density, multiple solutions, reactive spaces | how many valid answers can one room support? | arbitrary gating or noisy options |

## Agent note
- If the project blends two cards, choose the one that owns failure recovery, not the one that merely sounds closer to the theme.
- For implementation, pair this gallery with `docs/research/game-development/genre/genre-examples.md` and the matching genre guide before writing the feature brief.

## Related docs

- [`docs/reference/genre-presets.md`](../reference/genre-presets.md)
- [`docs/reference/genre-plan.md`](../reference/genre-plan.md)
- [`docs/research/game-development/genre/genre-guide.md`](../research/game-development/genre/genre-guide.md)
- [`docs/research/game-development/genre/genre-examples.md`](../research/game-development/genre/genre-examples.md)
