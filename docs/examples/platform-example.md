# Platform Example

## Scope
- A Steam-first survival game wants a clear compatibility plan for Windows, macOS, Linux/Steam Deck, web demo, Android/iOS, and webOS/TV.
- The team wants a one-page matrix that tells them what to prioritize now, what to research next, and what can stay deferred.
- If the task also needs support tiers or release sequencing, use `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md`, and `docs/research/game-development/production/cross-platform.md` alongside this matrix.

## Baseline
- One shared codebase is allowed, but one shared release assumption is not.
- The primary family should be the one the first slice is optimized for.
- The next family should be the one that most stresses the same core loop.

## Decision order
1. Name the primary platform family.
2. Name the next family and the biggest delta between them.
3. Separate input, performance, store/policy, and distribution risks.
4. Pick the first validation that proves the family is viable.

## Example signal scan
- Windows PC: installer path, driver variance, controller parity, and graphics options
- macOS: App Sandbox, signing, Apple Silicon, and controller support
- Linux / Steam Deck: Steamworks, Proton / SteamOS, and verification requirements
- Web: startup latency, asset size, focus loss, and browser persistence
- Android / iOS: touch layout, battery, thermal, suspend/resume, and store review
- webOS / TV: remote navigation, 10-foot UI, focus, and TV store rules

## Dashboard schema
- Header cards: family, next family, current blocker, confidence
- Matrix: family, input model, perf envelope, policy risk, distribution path
- Heatmap: readiness by family
- Recommendation card: go/no-go, first lever, fallback lever, owner

## Good agent prompts
- "Turn this into a platform readiness matrix with one scorecard row for each family and one first validation per family."
- "Tell me which platform differences are launch blockers versus future research for a Steam-first build."
- "Summarize the biggest compatibility risks for webOS TV and Steam Deck using official docs first."

## Validation
- The family split is explicit.
- The first lever is named before tuning.
- The output includes one chart or matrix and one repo implication.

## Related docs
- [docs/reference/cross-platform-guide.md](../reference/cross-platform-guide.md)
- [docs/examples/cross-platform-example.md](cross-platform-example.md)
- [docs/reference/platform-guide.md](../reference/platform-guide.md)
- [docs/research/game-development/production/platform-compatibility.md](../research/game-development/production/platform-compatibility.md)
- [docs/reference/sector-intel.md](../reference/sector-intel.md)
- [docs/examples/steam-intel-example.md](steam-intel-example.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
- [studio/checklists/discipline/platform_compatibility.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/platform_compatibility.toml)
- [studio/docs/active/eval-platform-compatibility.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-platform-compatibility.md)
