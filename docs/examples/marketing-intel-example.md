# Marketing Intel Example

## Scope

Steam-first indie survival game.
Goal: turn the current campaign and community signals into one readable chart pack before the next marketing decision.

## Baseline

- Steam page exists and is tracked.
- Community and creator signals are coming in from more than one channel.
- The team has some raw numbers, but not yet one consistent view of the current window.
- No one has named the one chart that should drive the next move.

## Decision order

1. Pick the time window.
2. Name the source family.
3. Record the baseline.
4. Summarize the current movement.
5. Choose the chart pack.
6. Write one repo implication.

## Example status pack

| Signal | Source family | Window | Baseline | Current | Chart | What it suggests |
|---|---|---|---|---|---|---|
| Store visits | Steamworks traffic reporting | Last 14 days | 1,000 visits / 14d | 1,340 visits / 14d | Trend line | The page is gaining attention |
| Wishlist adds | Steamworks wishlist reporting | Last 14 days | 32 / 14d | 46 / 14d | Funnel chart | The page still converts, but the message may need sharpening |
| Creator mentions | Creator coverage / platform analytics | Last 14 days | 3 mentions / 14d | 5 mentions / 14d | Theme table | Creator hooks are readable enough to travel |
| Community questions | Steam Community / Discord | Last 14 days | 6 repeated questions | 11 repeated questions | Topic table | The next beat should answer a recurring confusion |
| Paid efficiency | UTM or campaign analytics | Last 14 days | no baseline | $2.80 per wishlist | Efficiency table | Paid support is measurable, but the creative may need a refresh |

## Visualization pack

1. Summary card: `up / flat / down`, current window, and the main callout.
2. Trend line: visits, wishlists, or installs over time.
3. Funnel: impressions -> visits -> wishlists -> demo installs.
4. Topic table: recurring creator or community themes.
5. Channel mix chart: which channel currently carries the weight.
6. Decision box: whether to keep the beat, change the message, or pause.

```mermaid
flowchart LR
    ["Steamworks analytics"] --> ["Normalize the window"]
    ["Creator and community notes"] --> ["Group repeated themes"]
    ["Campaign tracking"] --> ["Read efficiency"]
    ["Normalize the window"] --> ["Chart pack"]
    ["Group repeated themes"] --> ["Chart pack"]
    ["Read efficiency"] --> ["Chart pack"]
    ["Chart pack"] --> ["One recommendation"]
```

## Good agent prompts

- "Turn the latest marketing signals into a chart pack and tell me what changed."
- "Compare our current wishlist trend, creator mentions, and community themes, then choose one next move."
- "Summarize the current marketing status and point at the one chart that matters most."

## Validation

- The report names the time window and source family.
- The report shows a baseline, the current movement, and one implication.
- The report includes one chart recommendation the user could reopen later.

## Related docs

- `docs/reference/marketing-intel.md`
- `docs/reference/marketing-guide.md`
- `docs/reference/steam-intel.md`
- `docs/research/game-development/production/marketing-intel.md`
- `docs/examples/steam-intel-example.md`
- `studio/docs/templates/marketing-intel.md`
