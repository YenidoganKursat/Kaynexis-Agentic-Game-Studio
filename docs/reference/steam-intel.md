# Steam Intel Guide

## Summary

Steam intel in this repo means a source-backed watch on Steam store traffic, wishlists, forum/community signals, hardware mix, and current market context.
Use it when the task asks what Steam is saying now, what players are reacting to, or which graph should drive the next decision.

## Primary sources

- [Steamworks documentation home](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Store and Platform Traffic Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: UTM Analytics](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Wishlist Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Visibility on Steam](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Steam Community](https://partner.steamgames.com/doc/home)
- [Steam Community discussions](https://steamcommunity.com/discussions/%2A)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [GDC 2026 State of the Game Industry Report](https://reg.gdconf.com/2026-SOTI)
- [GDC 2025 State of the Game Industry report](https://reg.gdconf.com/state-of-game-industry-2025)
- [IGDA Developer Satisfaction Survey](https://igda.org/dss/)
- [ESA Essential Facts 2025](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2025-data/)

## Why this matters to this repo

- The repo already has sector, marketing, storefront, and community templates.
- Steam intel adds the narrower layer that decides what Steam is actually telling us right now before we guess about wishlists, forums, or hardware mix.
- It is especially useful when the task affects:
  - Steam store page changes
  - wishlist pacing
  - forum/discussion themes
  - hardware and compatibility assumptions
  - market appetite for a Steam-first game

## Decision impact

- Use Steam intel before revising a Steam page, planning a demo beat, changing support assumptions, or deciding whether a community complaint is a one-off or a trend.
- Keep facts and inference separate:
  - facts from the source pages
  - implication for this repo
  - confidence or uncertainty
- Prefer first-party Steamworks and official survey sources before secondary trackers.

## Signal map

| Signal family | What it answers | Best chart | How the agent should use it |
| --- | --- | --- | --- |
| Store traffic | Which page/view sources are moving interest | line chart or funnel | Decide whether a page push, trailer refresh, or tag cleanup is needed |
| Wishlists | Whether the store page is converting attention into intent | time-series and funnel chart | Decide whether the next beat should be metadata, trailer, demo, or community work |
| Community / forum signals | What players are confused, asking, or repeating | topic table or stacked bar | Separate one-off posts from recurring themes and production blockers |
| Hardware baseline | What PC/Steam users are likely to run | stacked bar or heat map | Set performance, compatibility, and minimum-spec assumptions |
| Market context | What the current industry and audience picture looks like | summary card plus comparison table | Keep scope, launch, and support assumptions current |

## Visualization pack

Use a simple, user-friendly pack first:

1. Summary card: traffic, wishlists, forum themes, hardware risk, and one recommendation.
2. Trend line: store traffic and wishlist movement over time.
3. Funnel: impressions -> store visits -> wishlists -> demo installs -> return visits.
4. Topic table: forum and discussion themes with frequency and severity.
5. Hardware mix chart: OS, GPU, or resolution slices only when they matter to the decision.
6. Decision box: one sentence on what should happen next.

```mermaid
flowchart LR
    ["Steamworks traffic and wishlist data"] --> ["Normalize the time window"]
    ["Steam Community discussions"] --> ["Group recurring themes"]
    ["Steam Hardware Survey"] --> ["Read hardware mix"]
    ["GDC / IGDA / ESA surveys"] --> ["Add market context"]
    ["Normalize the time window"] --> ["Chart pack"]
    ["Group recurring themes"] --> ["Chart pack"]
    ["Read hardware mix"] --> ["Chart pack"]
    ["Add market context"] --> ["Chart pack"]
    ["Chart pack"] --> ["Simple recommendation"]
```

## Monitoring cadence

- Daily during an active launch, demo, or festival beat.
- Weekly during store-page preparation or community review cycles.
- Monthly for a Steam-first product strategy review.
- Immediately after a forum spike, wishlist spike, or store-page revision.

## Example prompts for the agent

- "Track Steam store traffic, wishlist movement, forum themes, and hardware mix for a Steam-first survival game."
- "Summarize what the latest Steam hardware and community signals mean for our next store-page update."
- "Turn the current Steam signals into a simple chart pack and one recommendation."

## Validation

- Name the source family and the time window before summarizing.
- Separate facts, qualitative forum themes, and repo implications.
- Give the user one short summary plus one chart recommendation.

## Related docs

- `docs/examples/steam-intel-example.md`
- `docs/reference/platform-guide.md`
- `docs/research/game-development/production/steam-intel.md`
- `docs/research/game-development/production/platform-compatibility.md`
- `docs/reference/sector-intel.md`
- `docs/reference/marketing-guide.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/mastermind-guide.md`
