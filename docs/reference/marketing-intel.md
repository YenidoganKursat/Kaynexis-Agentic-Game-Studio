# Marketing Intel Guide

## Summary

Marketing intel in this repo means a source-backed current-window snapshot of campaign health, channel movement, audience response, and asset performance.
Use this guide when the task asks what is changing now, which chart should drive the next decision, or whether the current marketing motion is healthy.
If the task is about campaign strategy, audience fit, channel mix, or beat planning, use `docs/reference/marketing-guide.md` instead and keep this page as the current-status companion.
If the task is Steam-specific, keep `docs/reference/steam-intel.md` nearby so the Steam snapshot and the broader marketing snapshot do not get mixed together.

## Primary sources

- [Steamworks documentation home](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Store and Platform Traffic Reporting](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: UTM Analytics](https://partner.steamgames.com/doc/home)
- [Steamworks documentation: Wishlist Reporting](https://partner.steamgames.com/doc/home)
- [Steam Community discussions](https://steamcommunity.com/discussions/%2A)
- [App Store Connect Analytics](https://developer.apple.com/app-store-connect/analytics/)
- [Google Play app quality](https://developer.android.com/quality)
- [Google Play Games on PC readiness](https://developer.android.com/games/playgames/development-readiness)
- [Sector Intel Guide](docs/reference/sector-intel.md)

## Why this matters to this repo

- The repo already has strategy, storefront, community, and sector guidance.
- This guide adds the missing current-status layer so the agent can answer with numbers and chart families before it opines.
- It keeps campaign evaluation aligned with current-window signals when the market, platform policy, or store motion changes.

## Decision impact

- Which channel is moving interest right now.
- Which funnel step is leaking.
- Which asset or message is gaining or losing traction.
- Which campaign deserves more budget, more creative work, or a pause.
- Which chart family should be shown to a user or reviewer.

## Status model

Choose one status question first:

- traffic trend
- wishlist trend
- store conversion
- creator coverage
- community response
- spend efficiency
- content throughput
- campaign health

Then answer these in order:

1. What is the source window?
2. Which source family owns the signal?
3. What is the baseline?
4. What is the current movement?
5. Which chart family shows the movement clearly?
6. What repo implication should follow?

## Signal map

| Signal family | What it answers | Best chart | How the agent should use it |
| --- | --- | --- | --- |
| Traffic and discovery | Which channels are still bringing attention | line chart or area chart | Decide whether the next move is metadata, reach, or creative refresh |
| Wishlist and install movement | Whether attention is turning into intent or activation | funnel or trend chart | Decide whether the next beat should be store-page, demo, or follow-up work |
| Community response | What players are confused about or excited by | theme table or stacked bar | Separate one-off noise from recurring patterns |
| Creator / press coverage | Whether outside coverage is helping the message travel | mention table or trend chart | Judge outreach quality instead of raw mention count only |
| Spend efficiency | Whether paid work is moving the expected outcome | cost-per-result table or scatter plot | Decide whether to keep, cut, or reshape paid support |
| Content throughput | Whether the team is shipping enough usable assets | status table or mini gantt | Decide whether the bottleneck is production, approval, or distribution |

## Visualization pack

Use a simple pack first:

1. Summary card: current window, top movement, top risk, and one recommendation.
2. Trend line: the main signal over time, usually traffic, wishlists, or installs.
3. Funnel: impressions -> visits -> conversions -> follow-on actions.
4. Channel mix chart: where interest is coming from and where it leaks.
5. Theme table: recurring community or creator themes with frequency and severity.
6. Efficiency table: spend versus result, if paid work is active.
7. Decision box: one sentence on what should happen next.

```mermaid
flowchart LR
    ["Campaign and platform analytics"] --> ["Normalize the time window"]
    ["Community and creator signals"] --> ["Group recurring themes"]
    ["Spending and output logs"] --> ["Read efficiency"]
    ["Normalize the time window"] --> ["Chart pack"]
    ["Group recurring themes"] --> ["Chart pack"]
    ["Read efficiency"] --> ["Chart pack"]
    ["Chart pack"] --> ["One recommendation"]
```

## Monitoring cadence

- Daily during an active campaign, demo, or launch window.
- Weekly during campaign preparation or review cycles.
- Monthly for a marketing health review and channel rebalancing.
- Immediately after a spike, a drop, or a major beat.

## Example prompts for the agent

- "Turn the current marketing signals into a simple chart pack and one recommendation."
- "Summarize the latest campaign status for our Steam-first launch and name the chart that matters most."
- "Evaluate whether the next beat should be more budget, a creative refresh, or a pause."

## Validation

- Name the source family and date window before charting.
- Separate facts, charted metrics, and repo implications.
- Give the user one short summary plus one chart recommendation.

## Related docs

- `docs/examples/marketing-intel-example.md`
- `docs/reference/marketing-guide.md`
- `docs/reference/steam-intel.md`
- `docs/reference/sector-intel.md`
- `docs/research/game-development/production/marketing-intel.md`
- `docs/research/game-development/production/marketing.md`
- `studio/docs/templates/marketing-intel.md`
- `studio/checklists/discipline/marketing_intel.toml`
- `studio/docs/active/eval-marketing-intel.md`
