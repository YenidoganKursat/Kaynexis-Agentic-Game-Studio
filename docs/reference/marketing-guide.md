# Marketing Guide

## Summary

Game marketing in this repo means choosing the right audience, promise, channel mix, asset stack, and measurement path before the work turns into random posting.
Use this guide when the question is "what should we do and why?" rather than "what should we post this week?"
If the task is specifically about Steam store traffic, wishlists, forum signals, or hardware context, start with `docs/reference/steam-intel.md` and keep this guide as the strategy companion.
If the task is specifically about current campaign status, dashboard output, chart packs, or latest metric movement, start with `docs/reference/marketing-intel.md` and keep this guide as the strategy companion.
If the task is specifically about platform-family compatibility or readiness across Windows, macOS, Linux/Steam Deck, web, Android/iOS, or TV/webOS, start with `docs/reference/platform-guide.md` and keep the platform matrix separate from the campaign strategy.

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

- The repo already has strong launch, community, sector, and storefront templates.
- This guide adds a durable strategy layer so the agent can decide where to spend effort before it writes beat copy or launch checklists.
- It also keeps strategy work aligned with current sector signals when the market, platform policy, or launch window changes.

## Decision impact

- Which audience is primary.
- Which channel owns the first beat.
- Which assets are required before promotion starts.
- Which metric proves the strategy is working.
- Which policy or platform rule could block the plan.

## Strategy model

Choose one objective first:

- awareness
- wishlist growth
- demo installs
- launch conversion
- retention or return visits
- creator reach
- community growth

Then answer these in order:

1. Who is the audience?
2. What promise do we want them to remember?
3. Which channel best reaches that audience?
4. Which proof points can the game already support?
5. Which asset formats are needed for that channel?
6. What baseline and target will prove the plan?
7. What policy, metadata, or platform constraint could block the plan?

## Channel families

| Channel | Best when | First metric | Common failure mode |
|---|---|---|---|
| Steam page and store events | PC-first games with a playable hook | store page CTR, wishlist growth, conversion from page visit | message does not match the trailer or screenshots |
| Demo / festival beat | The gameplay loop is easier to feel than explain | demo installs, retention, return visits, wishlists after demo | the demo is not representative or is too rough |
| Creator outreach | The game is readable in short clips or live play | mentions, clip reach, referral traffic, wishlists | outreach happens before the build is watchable |
| Community / newsletter / Discord | The game needs repeated trust and feedback loops | open rate, join rate, reply rate, active members | the channel becomes noise without a moderation plan |
| App Store / Google Play pages | Mobile or web distribution matters | page views, installs, conversion, retention | the store page lacks proof or policy-compliant metadata |
| Paid acquisition | The funnel is measurable and the budget is bounded | cost per install / wishlist / sign-up | money is spent before the funnel is understood |
| Live ops / patch beats | The game already has recurring players | return visits, patch engagement, response sentiment | the beat is treated like a launch instead of a retention loop |

## Evaluation criteria

- The objective is single and measurable.
- The audience and promise are explicit.
- The channel fits the audience and the asset strength.
- The proof points are real gameplay or real content.
- The measurement path exists before the beat ships.
- The policy and platform constraints are named.
- The expected upside justifies the cost and timing.

## Measurement methods

- First-party platform analytics for page views, conversion, and campaign tracking.
- UTM or campaign links when the channel is external.
- Wishlist or install growth over a fixed window.
- Demo playthrough retention or return visits.
- Trailer or clip watch-through when the asset is the main proof.
- Review sentiment and comment themes after launch beats.
- Creator coverage quality, not just raw mention count.
- Comparison against a baseline from the previous beat or the previous campaign window.

## Status and chart pack

Use `docs/reference/marketing-intel.md` when the user wants the latest marketing readout instead of the strategy itself.

The most useful current-status pack is usually:

1. Summary card: current window, top movement, and top risk.
2. Trend line: traffic, wishlists, installs, or replies over time.
3. Funnel: impressions -> visits -> wishlists -> demo installs -> return visits.
4. Channel mix chart: which channel carries the current weight.
5. Theme table: recurring creator or community themes.
6. Efficiency table: spend versus result, if paid support is active.

## Monitoring cadence

- Daily during a live beat or launch window.
- Weekly during campaign preparation.
- Monthly for strategy review and channel rebalancing.
- Immediately after a demo, festival, or major store change.

## Example prompts for the agent

- "Evaluate whether our current Steam page should lead the next beat or whether we need a demo-first campaign."
- "Compare creator outreach versus festival participation for a small indie survival game and name the metrics that decide."
- "Build a source-backed marketing strategy for a Steam-first indie game and show the baseline, target, and proof path."

## Validation

- Name the objective, audience, channel, and measurement path before recommending a strategy.
- Separate facts, assumptions, and implications.
- Cite the official source family and the current date window if market conditions matter.

## Related docs

- `docs/examples/marketing-example.md`
- `docs/examples/marketing-intel-example.md`
- `docs/reference/sector-intel.md`
- `docs/reference/steam-intel.md`
- `docs/reference/marketing-intel.md`
- `docs/reference/platform-guide.md`
- `docs/examples/platform-example.md`
- `docs/research/game-development/production/platform-compatibility.md`
- `docs/research/game-development/production/marketing.md`
- `docs/research/game-development/production/marketing-intel.md`
- `studio/docs/templates/marketing-plan.md`
- `studio/docs/templates/marketing-brief.md`
- `studio/docs/templates/marketing-intel.md`
- `studio/docs/templates/storefront-checklist.md`
- `docs/reference/mastermind-guide.md`
- `studio/docs/templates/community-ops.md`
- `docs/reference/task-prompt-examples.md`
