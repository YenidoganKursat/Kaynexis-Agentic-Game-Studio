# Sector Intel Example

## Scope

- A compact source-backed snapshot of current game-sector signals for a Steam-first indie project.
- The goal is not to predict the whole industry. The goal is to surface the most relevant current signals, then turn them into planning implications.

## Baseline

- Source hierarchy is explicit.
- Currentness is explicit.
- Facts are separated from inference.
- The user gets one short summary plus the validation path.

## Decision order

1. Pick the source window.
2. Gather official report or policy sources first.
3. Summarize the facts.
4. Add a short implication for the repo.
5. Flag any uncertainty or missing data.

## Example sector scan

| Signal | Source family | What to watch | How the agent should use it |
| --- | --- | --- | --- |
| Developer sentiment | GDC State of the Game Industry, IGDA DSS | layoffs, AI, working conditions, studio health, career satisfaction | Use to judge whether scope, staffing assumptions, or messaging should change |
| Market / audience | ESA Essential Facts | player demographics, platform reach, play behavior | Use to shape platform priority, store messaging, and audience assumptions |
| PC baseline | Steam Hardware & Software Survey | current hardware distribution and API/OS mix | Use to set practical performance, compatibility, and GPU assumptions |
| Store / policy | Apple App Review, Google Play quality, Steamworks docs | review risk, content rules, listing constraints, feature requirements | Use to guard release planning and avoid platform surprises |
| Accessibility discovery | Accessible Games Initiative | tags, storefront disclosure, feature clarity | Use to shape accessibility planning and metadata wording |

## Good agent prompts

- "Summarize the current game-sector signals for our genre and platform target, using official sources first."
- "What should we know about the current industry picture before we lock scope for a Steam-first release?"
- "Track policy and platform signals that could change our launch plan next quarter."

## Validation

- The agent names the source family and date window.
- The agent states facts and inference separately.
- The agent ends with one clear repo implication and one next step.

## Related docs

- `docs/reference/sector-intel.md`
- `docs/research/game-development/production/sector-intel.md`
- `docs/reference/agent-guide.md`
