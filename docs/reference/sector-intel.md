# Sector Intel Guide

## Summary

Sector intel in this repo means a source-backed snapshot of current game-industry, platform, policy, and market signals that can affect planning.
Use it when the task asks what is changing now, what the latest reports say, or which current constraints should shape the next decision.
If the work is specifically about Steam store traffic, wishlists, forum themes, or hardware mix, switch to `docs/reference/steam-intel.md` and keep this note as the wider current-signals companion.
If the work is specifically about platform-family compatibility or readiness across Windows, macOS, Linux/Steam Deck, web, Android/iOS, or TV/webOS, switch to `docs/reference/platform-guide.md` and keep this note as the wider current-signals companion.

## Primary sources

- [GDC 2026 State of the Game Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- [GDC 2025 State of the Game Industry report](https://reg.gdconf.com/state-of-game-industry-2025)
- [GDC State of the Game Industry hub](https://gdconf.com/state-game-industry/)
- [IGDA Developer Satisfaction Survey](https://igda.org/dss/)
- [IGDA 2023 Developer Satisfaction Survey press release](https://igda.org/news-archive/press-release-the-igda-and-western-university-release-2023-developer-satisfaction-survey/)
- [ESA Essential Facts 2025](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2025-data/)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Store support and review hub](https://developer.apple.com/support/app-store/)
- [Google Play app quality](https://developer.android.com/quality)
- [Google Play Games on PC readiness](https://developer.android.com/games/playgames/development-readiness)
- [Accessible Games Initiative](https://accessiblegames.com/)
- [Accessible Games Initiative tags](https://accessiblegames.com/accessibility-tags/)

## Why this matters to this repo

- This repo already treats genre, engine, performance, platform, and release work as separate decisions.
- Sector intel keeps those decisions grounded in current external reality instead of stale memory or generic advice.
- It helps the agent answer questions like:
  - what is changing in the industry right now
  - which platform constraints matter most this quarter
  - what current market or policy signals should shape scope, launch, or support planning

## Decision impact

- Use sector intel before changing platform targets, release assumptions, accessibility disclosure, store strategy, or live-ops scope.
- Separate facts from inference:
  - fact: what the official report or policy says
  - inference: what that might mean for this repo
- Prefer official or primary sources first, then add secondary coverage only if the task explicitly needs broader context.

## Source hierarchy

1. Official report or policy page
2. Official platform documentation or survey hub
3. Trade-association summary or press release
4. Secondary commentary only if the question still needs context

## Monitoring cadence

- Monthly: Steam Hardware & Software Survey, platform policy updates, storefront guidance changes
- Quarterly: platform news, policy changes, store requirements, accessibility tag updates
- Annual: GDC State of the Game Industry, IGDA DSS, ESA Essential Facts

## Example prompts for the agent

- "Summarize the current game-industry signals that matter for a Steam-first indie survival game."
- "Track the latest platform-policy and accessibility changes that could affect a mobile release plan."
- "Give me a source-backed current snapshot of the game sector, with the main implications for our scope."

## Validation

- Name the source family and the time window before summarizing.
- Report the signal, the implication, and the confidence separately.
- Do not present inference as fact.

## Related docs

- `docs/examples/sector-intel-example.md`
- `docs/research/game-development/production/sector-intel.md`
- `docs/reference/steam-intel.md`
- `docs/reference/platform-guide.md`
- `docs/examples/platform-example.md`
- `docs/research/game-development/production/platform-compatibility.md`
- `docs/reference/agent-guide.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
