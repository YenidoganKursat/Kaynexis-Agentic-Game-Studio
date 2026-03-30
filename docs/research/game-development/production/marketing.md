# Marketing

## Date

2026-03-29

## Summary

Game marketing works best in this repo when the agent treats it as a strategy and measurement problem, not just a copywriting or posting problem.
The useful question is: which audience, channel, asset, and metric combination is most likely to move the next milestone?

## Primary sources

- [Steamworks Documentation: Discounting](https://partner.steamgames.com/doc/marketing/discounts)
- [Steam Branding Guidelines](https://partner.steamgames.com/public/marketing/Steam_Guidelines_01042017.pdf)
- [App Store Connect Analytics](https://developer.apple.com/app-store-connect/analytics/)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Google Play: Publish your app](https://developer.android.com/studio/publish/)
- [Google Play Quality](https://developer.android.com/quality)
- [Google Play Games on PC: Development readiness](https://developer.android.com/games/playgames/development-readiness)
- [Google Play Inline Install Brand Guidelines](https://developer.android.com/distribute/marketing-tools/brand-guidelines/inline-installs.pdf)
- [Accessible Games Initiative accessibility tags](https://accessiblegames.com/accessibility-tags/)

## Why this matters to this repo

- The repo already has storefront, community, sector, and launch-beat tooling.
- Marketing strategy adds the missing layer that decides which of those tools should matter first.
- It also gives the agent a durable way to separate channel fit from raw enthusiasm.

## Decision impact

- Whether the next move should be a store-page push, a demo beat, a creator beat, or a community beat.
- Whether the current message is strong enough for the audience.
- Whether the assets are ready for the chosen channel.
- Whether the measurement path is real or just hopeful.

## Signal map

| Source family | What it answers | Marketing use |
|---|---|---|
| Steamworks discounting and branding docs | What Steam allows, how sales/events work, and how brand usage should look | Steam-first messaging, sale timing, store asset shape |
| App Store Connect analytics and review guidance | How Apple-facing campaigns and metadata should be measured and constrained | product page strategy, campaign links, compliance-aware messaging |
| Google Play publish / quality / PC readiness docs | How Android or PC-on-Android surfaces are read, shipped, and measured | mobile or PC storefront readiness and asset planning |
| Accessible Games tags | How to phrase accessibility support in store metadata and marketing copy | discoverability and trust signaling |
| Sector intel | What changed recently in the market or policy environment | current-window adjustments to scope, launch, or support planning |

## Measurement stack

- First-party analytics from the storefront or platform.
- Store page impressions, clicks, and conversion.
- Wishlist growth, demo installs, or sign-up growth.
- Return visits after a beat or demo.
- Creator coverage quality and referral traffic.
- Review sentiment and comment themes after launch or beta beats.
- Cost-per-result if paid channels are used.

## What to watch out for

- Treating a single beat as a full strategy.
- Optimizing for vanity metrics without a baseline.
- Releasing assets before the message is testable.
- Ignoring store or policy constraints.
- Mixing implementation work with campaign decisions.

## Repo impact

- The marketing guide and example should be read before any launch or campaign planning work.
- If the task is about current campaign status, chart packs, or metric movement, use `docs/reference/marketing-intel.md` and `docs/examples/marketing-intel-example.md` instead of the strategy pack.
- The storefront and community templates remain the beat-level companions.
- The sector-intel note remains the current-window companion when the market or platform changes.
