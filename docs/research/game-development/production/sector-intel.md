# Sector Intel

## Date

- 2026-03-29

## Summary

- Sector intel in this repo means a current, source-backed watch on the game industry, platform policy, and market signals that can influence planning.
- It is useful when the team wants to know what changed recently, what the official source actually says, and what that might mean for scope, launch, accessibility, or platform support.

## Primary sources

- [GDC 2026 State of the Game Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- [GDC 2025 State of the Game Industry report](https://reg.gdconf.com/state-of-game-industry-2025)
- [GDC State of the Game Industry hub](https://gdconf.com/state-game-industry/)
- [IGDA Developer Satisfaction Survey (DSS)](https://igda.org/dss/)
- [IGDA 2023 DSS press release](https://igda.org/news-archive/press-release-the-igda-and-western-university-release-2023-developer-satisfaction-survey/)
- [ESA Essential Facts 2025](https://www.theesa.com/resources/essential-facts-about-the-us-video-game-industry/2025-data/)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Store support hub](https://developer.apple.com/support/app-store/)
- [Google Play app quality](https://developer.android.com/quality)
- [Google Play Games on PC readiness](https://developer.android.com/games/playgames/development-readiness)
- [Accessible Games Initiative](https://accessiblegames.com/)
- [Accessible Games Initiative tags](https://accessiblegames.com/accessibility-tags/)

## Why this matters to this repo

- This repo already has strong routing for genre, engines, performance, release, and architecture.
- Sector intel adds the external "what is changing now" layer that helps the agent avoid stale assumptions.
- It is especially useful when the task affects:
  - platform priority
  - release planning
  - accessibility disclosures
  - hardware and performance expectations
  - genre bets that depend on current market appetite

## Decision impact

- Use sector intel before locking scope for a launch, port, platform strategy, or live-ops bet.
- Keep facts and inference separate:
  - facts from official sources
  - implication for this repo
  - confidence or uncertainty
- Prefer official report hubs, policy pages, and platform documentation before blogs or social posts.

## Signal map

### Developer sentiment and labor

- GDC and IGDA are the default sources for developer sentiment, layoffs, work conditions, and career satisfaction.
- Use them when scope or staffing assumptions need to reflect current industry pressure.

### Market and player base

- ESA Essential Facts is the default source for audience scale and player behavior.
- Use it when platform reach, demographic assumptions, or market language matters.

### PC hardware baseline

- Steam Hardware & Software Survey is the default source for current Steam/PC hardware baselines.
- Use it when performance, compatibility, or GPU assumptions should be grounded in current PC usage.

### Platform policy and distribution

- Steamworks, Apple App Review, and Google Play quality/policy docs are the default sources for distribution constraints.
- Use them when launch timing, store listing, content, monetization, or review risk matters.

### Accessibility discovery

- Accessible Games Initiative tags and guidance help the agent phrase accessibility features in storefront and metadata language.
- Use them when accessibility disclosure or feature labeling is part of the decision.

## Monitoring cadence

- Monthly: Steam Hardware & Software Survey, major platform policy pages, store guidance updates
- Quarterly: platform policy changes, storefront feature changes, accessibility tag updates
- Annual: GDC State of the Game Industry, IGDA DSS, ESA Essential Facts

## What to watch out for

- Do not treat a press summary as the same thing as the underlying survey or policy page.
- Do not cite old currentness without a date window.
- Do not blur a fact into an interpretation.
- Do not mix sector intel with engine implementation guidance unless the task truly needs both.

## Repo impact

- Add `sector-intel.md` and `sector-intel-example.md` to the user-facing docs and routing surface.
- Keep the sector note, example, template, checklist, and eval plan in sync.
- Surface sector signals when a task needs current industry, platform, or policy context before implementation.
