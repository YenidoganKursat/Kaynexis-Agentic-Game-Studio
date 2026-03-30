# Marketing Intel

## Date

- 2026-03-30

## Summary

- Marketing intel in this repo means a source-backed current-window snapshot of campaign health, channel movement, and content performance.
- It is useful when the team wants numbers and chart families before it changes the next marketing decision.
- This note is the companion to `docs/reference/marketing-guide.md`, which stays focused on strategy and planning.

## Primary sources

- [Steamworks documentation home](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Store and Platform Traffic Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: UTM Analytics](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Wishlist Reporting](https://partner.steamgames.com/doc/home)
- [Steam Community discussions](https://steamcommunity.com/discussions/%2A)
- [App Store Connect Analytics](https://developer.apple.com/app-store-connect/analytics/)
- [Google Play app quality](https://developer.android.com/quality)
- [Google Play Games on PC readiness](https://developer.android.com/games/playgames/development-readiness)
- [GDC State of the Game Industry hub](https://gdconf.com/state-game-industry/)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)

## Why this matters to this repo

- The repo already has launch, community, sector, and storefront tools.
- Marketing intel adds the current-status layer that decides what the next beat should react to.
- It keeps current-window reporting separate from evergreen marketing strategy.

## Decision impact

- Use marketing intel before changing budget, creative, channel priority, or beat timing.
- Keep facts and implication separate:
  - fact: what the platform or analytics view says
  - implication: what that might mean for this repo
  - confidence: how strong the signal is
- Prefer official platform reporting and first-party analytics before secondary trackers.

## Signal families

| Signal family | What it answers | Best chart | Repo use |
| --- | --- | --- | --- |
| Store traffic | Which channels are moving attention | trend line or funnel | Decide whether metadata, trailer, or channel mix should change |
| Wishlist or install movement | Whether the page or funnel is converting | funnel and trend chart | Decide whether the next beat should be store, demo, or follow-up work |
| Community response | What players keep asking or repeating | topic table | Separate one-off noise from recurring blockers |
| Creator coverage | Whether outside coverage is amplifying the message | mention table or trend chart | Judge outreach quality instead of raw count only |
| Spend efficiency | Whether paid support is doing its job | cost-per-result table | Decide whether to keep, cut, or reshape paid support |
| Market context | Whether the current window changed the meaning of the metrics | summary card | Keep the signal read honest about the date window |

## Monitoring cadence

- Daily during a live campaign, demo, or launch window.
- Weekly during a campaign-prep cycle.
- Monthly for a health review and channel rebalancing.
- Immediately after a spike, drop, or beat.

## What to watch out for

- Do not treat a single beat as the whole marketing picture.
- Do not optimize for vanity metrics without a baseline.
- Do not show a chart without the source family and date window.
- Do not blur a fact into an interpretation.

## Repo impact

- Add `marketing-intel.md` and `marketing-intel-example.md` to the user-facing docs and routing surface.
- Keep the marketing guide, chart pack, checklist, and eval plan synchronized.
- Surface marketing intel when a task needs current campaign, channel, or funnel context before implementation.

## Related docs

- `docs/reference/marketing-intel.md`
- `docs/reference/marketing-guide.md`
- `docs/examples/marketing-intel-example.md`
- `docs/reference/steam-intel.md`
- `docs/reference/sector-intel.md`
