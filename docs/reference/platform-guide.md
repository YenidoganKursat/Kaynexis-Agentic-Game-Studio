# Platform Guide

## Summary
- Platform compatibility in this repo means mapping the real deltas between target families before scope, art, UI, save, performance, or release assumptions harden.
- A platform plan is not just "can the build launch?" It is input shape, session shape, store-policy shape, performance envelope, device-family quirks, and certification or verification shape.
- Treat Steam, Windows, macOS, Linux/Steam Deck, console/PS5-like, web, Android/iOS, and TV/webOS as different readiness conversations, even when the game content is shared.
- If the task also needs support tiers or release sequencing, pair this guide with `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md`, and `docs/research/game-development/production/cross-platform.md`.

## Primary sources
- [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Sandbox](https://developer.apple.com/documentation/security/app_sandbox)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Microsoft Gaming Documentation Hub](https://learn.microsoft.com/en-us/gaming/)
- [Official Licensing Program - Sony Interactive Entertainment](https://sonyinteractive.com/en/contact-us/official-licensing-program/)
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Steam Hardware & Software Survey](https://store.steampowered.com/hwsurvey/)
- [Android quality guidelines](https://developer.android.com/quality)
- [Google Play Games on PC development readiness](https://developer.android.com/games/playgames/development-readiness)
- [Android TV documentation](https://developer.android.com/tv)
- [MDN Web Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [MDN Progressive web apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [webOS TV developer portal](https://webostv.developer.lge.com/)

## Why this matters to this repo
- This repo already separates engine choice, genre choice, perf work, Steam intel, and release work; platform compatibility sits between those layers and should not be inferred from a single target label.
- `studio/docs/active/platform-targets.md` should name the real platform families, not just a broad target like "PC".
- The agent needs a source-backed way to decide when one platform family is a real port, when it is a verification surface, and when it is only a future research target.

## Decision impact
- Prefer one primary family and one next family when possible.
- Name the first delta that changes design, tech, or release scope.
- Separate "same build, different policy" from "different build, different input model, different perf budget."

## Platform family map
| Family | Examples | First question | First lever | Typical owners |
|---|---|---|---|---|
| Desktop premium | Windows, macOS, Linux | Does the build feel native on each desktop OS and input combo? | Input model, windowing, packaging, and scalable options | `porting_engineer`, `performance_analyst`, `build_release_engineer` |
| Steam / Steam Deck | Steam storefront, SteamOS, Proton, Deck Verified | What does Steamworks, Deck verification, or Linux compatibility change? | Steamworks docs, controller coverage, and verification evidence | `producer`, `porting_engineer`, `certification_manager` |
| Console / PS5-like | PS5-like, Xbox-like, Switch-like | Is this a submission and cert problem, not just a port? | Controller-first UX, suspend/resume, save / entitlement handling, packaging, and cert evidence | `porting_engineer`, `certification_manager`, `ux_designer`, `build_release_engineer` |
| Web | Browser, embedded demo, PWA | Does the game survive browser memory, focus loss, and startup cost? | Asset budget, PWA/offline behavior, and load path | `porting_engineer`, `build_release_engineer`, `performance_analyst` |
| Mobile | Android, iOS | Does the session and input model fit touch, battery, and thermal reality? | Touch layout, session compression, suspend/resume handling | `porting_engineer`, `ux_designer`, `performance_analyst` |
| TV | webOS, Android TV, Google TV | Does the UI work at 10-foot distance with a remote or controller? | Focus navigation, safe areas, and readable UI scale | `ux_designer`, `porting_engineer`, `certification_manager` |

## Visualization pack
- Header cards: primary family, next family, current blocker, current confidence
- Matrix view: family rows, input model, perf envelope, policy risk, and distribution path
- Heatmap: red/yellow/green readiness by family
- Decision card: go/no-go, first lever, fallback lever, owner

## Monitoring cadence
- Weekly: official platform docs, store policy pages, and survey pages
- Monthly: device mix, browser mix, Steam Hardware Survey, and platform verification pages
- Per milestone: refresh the matrix before scope locks or demo/release cuts

## Example prompts for the agent
- "Map compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and webOS TV; separate input, performance, policy, and release deltas, then give me one dashboard schema."
- "Compare the first blockers for Steam Deck and webOS TV for a shared build and tell me whether they are launch blockers or future research."
- "Compare the first blockers for PS5-like console premium and Steam Deck for a shared build and tell me whether they are launch blockers or future research."
- "Turn our platform targets into a family-based readiness matrix with one recommended first validation per family."

## Validation
- Name the source family and the current target family before summarizing.
- Separate input, performance, policy, store, and display/UX deltas.
- Return one matrix or chart pack plus one repository implication.

## Related docs
- [docs/reference/cross-platform-guide.md](cross-platform-guide.md)
- [docs/examples/cross-platform-example.md](../examples/cross-platform-example.md)
- [docs/examples/platform-example.md](../examples/platform-example.md)
- [docs/examples/console-example.md](../examples/console-example.md)
- [docs/reference/console-guide.md](console-guide.md)
- [docs/research/game-development/production/platform-compatibility.md](../research/game-development/production/platform-compatibility.md)
- [docs/research/game-development/production/console.md](../research/game-development/production/console.md)
- [docs/research/game-development/production/platform.md](../research/game-development/production/platform.md)
- [docs/reference/sector-intel.md](sector-intel.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
- [studio/checklists/discipline/platform_compatibility.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/platform_compatibility.toml)
- [studio/docs/active/eval-platform-compatibility.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-platform-compatibility.md)
