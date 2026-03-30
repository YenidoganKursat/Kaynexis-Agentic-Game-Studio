# Steam Intel Example

## Scope

- A source-backed Steam intelligence bundle for a Steam-first indie survival game.
- The goal is not to predict the whole market. The goal is to explain what Steam is saying now, then turn that into a store, community, or support decision.

## Baseline

- Official sources first.
- Currentness is explicit.
- Forum themes stay separate from hard metrics.
- The user gets one short summary plus a chart pack recommendation.

## Decision order

1. Pick the time window.
2. Read Steamworks traffic, wishlist, and visibility docs first.
3. Read the current Steam hardware survey.
4. Scan Steam discussions for recurring themes.
5. Add GDC, IGDA, or ESA context only if the market picture matters.
6. Turn the result into a dashboard schema and one decision.

## Example signal scan

| Signal | Source family | What to watch | How the agent should use it |
| --- | --- | --- | --- |
| Steam traffic | Steamworks traffic / UTM / visibility | visit spikes, campaign sources, seasonal drops | Decide whether page copy, trailer, or tags need attention |
| Wishlists | Steamworks wishlist reporting | conversion from visits to wishlists, movement after beats | Decide whether to push the store page, demo, or community next |
| Forum themes | Steam Community discussions | repeated questions, complaints, compatibility reports | Decide whether a FAQ, patch note, or support note is needed |
| Hardware mix | Steam Hardware & Software Survey | OS, GPU, and display mix | Decide whether the minimum spec or performance note needs adjusting |
| Market context | GDC / IGDA / ESA | developer sentiment, audience signals, current market pressure | Decide whether the launch plan or support scope needs a change |

## Dashboard schema

- Header cards: traffic, wishlist delta, discussion volume, hardware risk, and the current recommendation.
- Trend line: store visits and wishlists over 7, 14, and 30 days.
- Funnel chart: impressions -> visits -> wishlists -> demo installs -> return visits.
- Topic table: forum themes grouped by frequency and severity.
- Hardware chart: platform or GPU mix only when it changes the decision.
- Decision card: one clear next action with one sentence of evidence.

```mermaid
flowchart LR
    ["Steamworks metrics"] --> ["Normalize"]
    ["Forum threads"] --> ["Theme cluster"]
    ["Hardware survey"] --> ["Device mix"]
    ["External surveys"] --> ["Market context"]
    ["Normalize"] --> ["Dashboard"]
    ["Theme cluster"] --> ["Dashboard"]
    ["Device mix"] --> ["Dashboard"]
    ["Market context"] --> ["Dashboard"]
    ["Dashboard"] --> ["One decision"]
```

## Good agent prompts

- "Build a Steam intel pack for our survival game and show the store, wishlist, forum, and hardware signals separately."
- "Decide whether the next Steam move should be a store-page refresh, a demo beat, or a forum FAQ update."
- "Turn the current Steam signals into a chart pack that a producer can read in one minute."

## Validation

- The agent names the source family and the date window.
- The agent separates metrics from forum themes.
- The agent includes one chart recommendation and one next step.

## Related docs

- `docs/reference/steam-intel.md`
- `docs/research/game-development/production/steam-intel.md`
- `docs/examples/sector-intel-example.md`
- `docs/examples/marketing-example.md`
