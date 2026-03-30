# Cross-Platform

## Date
- 2026-03-30

## Summary
- Cross-platform planning is a support-strategy problem before it is a porting problem.
- The repo should be able to answer which platform families are core, supported, demo-only, research-only, or deferred, and why.
- In practice, the family splits that matter most are input model, session length, save and suspend behavior, packaging and policy, UI scale, and performance envelope.

## Primary sources
- [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Sandbox](https://developer.apple.com/documentation/security/app_sandbox)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [Android quality guidelines](https://developer.android.com/quality)
- [Google Play Games on PC development readiness](https://developer.android.com/games/playgames/development-readiness)
- [Android TV documentation](https://developer.android.com/tv)
- [MDN Web Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [MDN Progressive web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [webOS TV developer portal](https://webostv.developer.lge.com/)

## Why this matters to this repo
- The repo already has separate engine, genre, Steam, and release notes.
- Without a dedicated cross-platform note, platform tasks can still collapse into vague "PC first" language even when the release plan needs a support tier.
- This note gives the agent a source-backed way to decide whether a family is a ship target, a demo target, or a research lane.

## Decision impact
- Treat Windows, macOS, Linux / Steam Deck, web, mobile, and TV as different support contracts.
- Use Steam as a distribution and verification surface, not as a substitute for platform planning.
- Use web as a startup and memory-budget surface, not as a smaller desktop build.
- Use mobile as a touch and battery contract, not as a simple UI reskin.

## Signal map
| Family | Watch first | Typical proof |
|---|---|---|
| Windows / macOS / Linux | Input parity, installer path, graphics options, frame pacing | One runnable build and a short checklist of OS-specific deltas |
| Steam / Steam Deck | Steamworks, controller coverage, Proton / SteamOS behavior, verification evidence | A Steam-specific readiness note and controller test summary |
| Web | Startup cost, memory ceiling, focus loss, persistence | A browser-safe load and resume check plus a size budget |
| Android / iOS | Touch layout, battery, thermal load, suspend / resume | One mobile session test and one device-family risk note |
| webOS / TV | Remote navigation, 10-foot readability, safe areas, TV store rules | One focus-navigation pass and one display-scale note |

## What to watch out for
- Treating web as just another desktop target
- Treating mobile as a performance-only problem
- Treating TV as if it were a controller-only living-room PC
- Letting Steam Deck or Steamworks details get buried inside a generic desktop note

## Repo impact
- Keep `studio/docs/active/platform-targets.md` family-based, support-tier aware, and explicit.
- Use `docs/reference/cross-platform-guide.md` for support strategy and sequencing.
- Use `docs/examples/cross-platform-example.md` for support-tier matrix and chart-pack examples.
- Use `docs/reference/platform-guide.md` for the family-by-family compatibility matrix.

## Related docs
- [docs/reference/cross-platform-guide.md](../../../reference/cross-platform-guide.md)
- [docs/examples/cross-platform-example.md](../../../examples/cross-platform-example.md)
- [docs/reference/platform-guide.md](../../../reference/platform-guide.md)
- [docs/examples/platform-example.md](../../../examples/platform-example.md)
- [docs/research/game-development/production/platform-compatibility.md](platform-compatibility.md)
- [docs/research/game-development/production/README.md](README.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
