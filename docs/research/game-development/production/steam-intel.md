# Steam Intel

## Date

- 2026-03-30

## Summary

- Steam intel in this repo means a current, source-backed watch on Steam store traffic, wishlists, forum and community themes, hardware mix, and the market context that shapes Steam-first planning.
- It is useful when the team wants to know what Steam is saying now, what players are reacting to, and which chart should drive the next decision.

## Primary sources

- [Steamworks documentation home](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Store and Platform Traffic Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: UTM Analytics](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Wishlist Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Visibility on Steam](https://partner.steamgames.com/doc/home)
- [Steam Community discussions](https://steamcommunity.com/discussions/%2A)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [GDC 2026 State of the Game Industry Report](https://reg.gdconf.com/2026-SOTI)
- [GDC 2025 State of the Game Industry report](https://reg.gdconf.com/state-of-game-industry-2025)
- [IGDA Developer Satisfaction Survey (DSS)](https://igda.org/dss/)
- [ESA Essential Facts 2025](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2025-data/)

## Why this matters to this repo

- The repo already has launch, community, sector, marketing, and storefront tools.
- Steam intel adds the narrower layer that decides what Steam is actually telling us right now before we guess about wishlists, forums, or hardware mix.
- It helps the agent answer questions like:
  - which Steam metric is changing
  - whether forum chatter is a one-off or a pattern
  - which hardware or compatibility assumption has gone stale
  - whether the next move should be a store refresh, demo beat, or support note

## Decision impact

- Use Steam intel before revising a Steam page, planning a demo beat, changing support assumptions, or deciding whether a community complaint is a one-off or a trend.
- Keep facts and inference separate:
  - fact: what the source page says
  - inference: what that might mean for this repo
  - confidence: how strong the signal is
- Prefer first-party Steamworks and official survey sources before secondary trackers.

## Signal map

### Store traffic and conversion

- Read Steamworks traffic reporting, UTM analytics, visibility pages, and wishlist reporting together.
- Use them when the question is whether attention is turning into wishlists or whether the store page is leaking interest.

### Community and forum signals

- Steam Community discussions are the default source for repeated questions, bug reports, feedback themes, and support pressure.
- Use them when the question is whether one complaint is isolated or part of a broader pattern.

### Hardware and compatibility baseline

- Steam Hardware & Software Survey is the default source for current PC/Steam hardware mix.
- Use it when performance, compatibility, resolution, or GPU assumptions should be grounded in current usage.

### Market context and surveys

- GDC, IGDA, and ESA reports are the default context sources for developer sentiment, industry pressure, and audience behavior.
- Use them when launch, scope, or support planning needs current market context instead of stale memory.

## Monitoring cadence

- Daily during an active launch, demo, or festival beat.
- Weekly during store-page preparation or community review cycles.
- Monthly for a Steam-first product strategy review.
- Immediately after a forum spike, wishlist spike, or store-page revision.

## What to watch out for

- Do not treat forum noise as the same thing as a store conversion signal.
- Do not treat a press summary as the same thing as the underlying survey or policy page.
- Do not cite old currentness without a date window.
- Do not blur a fact into an interpretation.

## Repo impact

- Add `steam-intel.md` and `steam-intel-example.md` to the user-facing docs and routing surface.
- Keep the Steam note, example, checklist, and eval plan in sync.
- Surface Steam signals when a task needs current store, forum, wishlist, or hardware context before implementation.

## Related docs

- `docs/reference/steam-intel.md`
- `docs/examples/steam-intel-example.md`
- `docs/reference/sector-intel.md`
- `docs/reference/marketing-guide.md`
- `docs/research/game-development/production/README.md`
