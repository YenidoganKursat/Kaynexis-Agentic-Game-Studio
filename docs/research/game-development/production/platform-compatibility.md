# Platform Compatibility

## Date
- 2026-03-30

## Summary
- Platform compatibility should be treated as a family-by-family planning problem, not as a generic port label.
- In practice, the big differences are not just visual. They are input model, session length, load behavior, store or review policy, controller or remote support, save / suspend behavior, and device-family performance envelope.
- Steam is best treated as a distribution and verification surface over desktop families, not as a separate build assumption that can replace platform thinking.

## Primary sources
- [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Sandbox](https://developer.apple.com/documentation/security/app_sandbox)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Microsoft Gaming Documentation Hub](https://learn.microsoft.com/en-us/gaming/)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [Android quality guidelines](https://developer.android.com/quality)
- [Google Play Games on PC development readiness](https://developer.android.com/games/playgames/development-readiness)
- [Android TV documentation](https://developer.android.com/tv)
- [MDN Web Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [MDN Progressive web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [webOS TV developer portal](https://webostv.developer.lge.com/)

## Why this matters to this repo
- The repo already has active platform targets, starter kits, engine adapters, and store/release checklists.
- Without a dedicated compatibility note, platform planning tends to collapse into "PC first" or "mobile later" language that hides the actual deltas.
- This note gives the agent a source-backed way to decide whether a platform is a core target, a near-term target, or a future research lane.

## Decision impact
- A family is ready only when input, performance, policy, and distribution assumptions are named.
- Web and TV are not just smaller screens; they are different focus, persistence, and input models.
- macOS and Linux are not just alternate installers; they add OS-specific packaging and runtime assumptions.
- Steam Deck needs controller coverage, Steamworks language, and verification awareness from the start.

## Signal map
| Family | Watch first | Typical proof |
|---|---|---|
| Windows / macOS / Linux | Input parity, installer path, graphics options, frame pacing | One runnable build and a short checklist of OS-specific deltas |
| Steam / Steam Deck | Steamworks, Deck Verified expectations, controller support, Linux / Proton behavior | A Steam-specific readiness note and controller test summary |
| Web | Browser startup, asset size, memory ceiling, focus loss, persistence | A browser-safe load and resume check plus a size budget |
| Android / iOS | Touch layout, session length, battery, thermal load, suspend / resume | One mobile session test and one device-family risk note |
| webOS / TV | Remote navigation, 10-foot readability, safe areas, TV store rules | One focus-navigation pass and one display-scale note |

## Monitoring cadence
- Weekly: official platform docs, store guidance, and survey or readiness pages
- Monthly: device mix and compatibility signals that could shift the next target
- Per milestone: refresh the compatibility matrix before a target or release gate changes

## What to watch out for
- Treating a browser build as "just another PC build"
- Treating mobile as a performance-only problem
- Treating TV as if it were a controller-only living-room PC
- Letting Steam Deck or Steamworks details get buried inside a generic desktop note

## Repo impact
- Keep `studio/docs/active/platform-targets.md` family-based and explicit.
- Use `docs/reference/platform-guide.md` as the first read for any broad platform question.
- Use `docs/reference/cross-platform-guide.md` and `docs/examples/cross-platform-example.md` when the task also needs support tiers or release sequencing.
- Use `docs/research/game-development/production/cross-platform.md` when the task needs a support-strategy note that separates core, supported, demo, research, and deferred families.
- Use `docs/examples/platform-example.md` for a simple matrix and chart-pack pattern.
- Route platform work through the compatibility checklist before packaging or release assumptions harden.

## Related docs
- [docs/reference/cross-platform-guide.md](../../../reference/cross-platform-guide.md)
- [docs/examples/cross-platform-example.md](../../../examples/cross-platform-example.md)
- [docs/reference/platform-guide.md](../../../reference/platform-guide.md)
- [docs/examples/platform-example.md](../../../examples/platform-example.md)
- [docs/research/game-development/production/platform.md](platform.md)
- [docs/research/game-development/production/README.md](README.md)
- [docs/reference/sector-intel.md](../../../reference/sector-intel.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
- [studio/checklists/discipline/platform_compatibility.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/platform_compatibility.toml)
- [studio/docs/active/eval-platform-compatibility.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-platform-compatibility.md)
