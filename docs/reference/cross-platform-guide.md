# Cross-Platform Guide

## Summary
- Use this guide when the question is not just "can we ship to a platform?" but "what support tier does each platform family deserve, in what order should we ship them, and what proof do we need before we promise anything?"
- A cross-platform plan is a support-strategy problem first and a packaging problem second.
- The goal is to keep one codebase honest while still naming the families that are truly core, truly supported, demo-only, research-only, or deferred, including console / PS5-like families when they are in scope.

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
- [Official Licensing Program - Sony Interactive Entertainment](https://sonyinteractive.com/en/contact-us/official-licensing-program/)

## Why this matters to this repo
- The repo already has platform compatibility notes, platform targets, and store/release surfaces.
- This guide adds the missing support-strategy layer: what is core, what is supported, what is a demo surface, and what is still research-only.
- Without that layer, agents tend to flatten every platform into the same release promise.

## Decision impact
- Name the support tier before naming the build target.
- Decide whether a family is a core ship, a supported ship, a demo-only surface, or a research-only target.
- Decide whether the delta is one binary with different policy, or a different binary with different input and performance assumptions.

## Support tiers
| Tier | Meaning | Typical rule |
|---|---|---|
| `core` | The project is built and tuned for this family first | It owns the first slice and the primary validation path |
| `supported` | The project should ship here with known deltas and a real test pass | It gets family-specific proof before release |
| `demo` | The family is useful as a discovery or marketing surface | It can have reduced scope, but the limitations must be explicit |
| `research` | The family is being evaluated for fit or future investment | It needs a proof note, not a promise |
| `deferred` | The family is not in scope yet | It should remain visible as out-of-scope, not forgotten |

## Cross-platform support rules
- Treat input as a first-class delta: keyboard/mouse, controller, touch, remote, and focus navigation are not interchangeable.
- Treat session length as a design delta: web and mobile often need shorter, more resumable sessions than desktop.
- Treat save and suspend behavior as a compatibility delta: browser persistence, mobile backgrounding, and desktop save trust are not the same contract.
- Treat UI scale and safe-area behavior as a platform delta: 10-foot TV, touch-first mobile, and desktop windowing need different readability assumptions.
- Treat packaging and policy as a platform delta: sandbox, signing, review, controller coverage, and store metadata can be release blockers.
- Treat load time and memory as platform deltas: web and mobile usually break first on startup and memory budget, while desktop often breaks first on input or UI assumptions.

## Family-by-family quick lens
| Family | First question | First validation |
|---|---|---|
| Windows / macOS / Linux | Does it feel native on each desktop OS and input combo? | Run launch, controller, and windowing checks on all three desktop targets |
| Steam / Steam Deck | What does Steamworks, Deck verification, and Linux / Proton support change? | Run a Steam-specific controller and launch pass and record the verification note |
| Console / PS5-like | Does the family need a cert gate, a submission gate, or a different input and suspend model? | Run a controller-first and suspend/resume pass and record the first submission blocker |
| Web | Can the game survive browser startup, focus loss, and memory ceilings? | Measure startup, pause/resume, and asset budget on a browser target |
| Android / iOS | Does the session fit touch, battery, thermal, and backgrounding reality? | Run one touch session and one suspend/resume pass |
| webOS / TV | Does the UI work at 10-foot distance with remote or controller focus? | Run a focus-navigation and readability pass on a TV-sized layout |

## Support-sequence rules
1. Pick one core family.
2. Pick one next family that stresses the same loop.
3. Decide what can be shared and what must be split.
4. Decide which families are release gates and which are future proofing.
5. Keep the release order visible in the active platform target note.

## Visualization pack
- Support matrix: family, tier, input model, performance envelope, policy risk, release order
- Heatmap: readiness by family
- Decision card: core family, next family, first delta, fallback
- Release board: build order and proof gate per family

## Example prompts for the agent
- "Turn our platform targets into a support-tier matrix and tell me which families are core, supported, demo-only, or research-only."
- "Map the biggest cross-platform deltas for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and webOS TV, then give me one release order card."
- "Map the biggest cross-platform deltas for Windows, macOS, Linux/Steam Deck, console/PS5-like, web, Android/iOS, and webOS TV, then give me one release order card."
- "Tell me which platform differences are launch blockers versus future research for a Steam-first build."
- "Tell me which platform differences are launch blockers versus future research for a PS5-like console premium build."

## Validation
- Name the support tier before naming the build target.
- Separate input, session, save, policy, packaging, and performance deltas.
- Return one matrix or chart pack plus one release-sequence implication.

## Related docs
- [docs/reference/platform-guide.md](platform-guide.md)
- [docs/examples/cross-platform-example.md](../examples/cross-platform-example.md)
- [docs/examples/platform-example.md](../examples/platform-example.md)
- [docs/examples/console-example.md](../examples/console-example.md)
- [docs/reference/console-guide.md](console-guide.md)
- [docs/research/game-development/production/cross-platform.md](../research/game-development/production/cross-platform.md)
- [docs/research/game-development/production/console.md](../research/game-development/production/console.md)
- [docs/research/game-development/production/platform-compatibility.md](../research/game-development/production/platform-compatibility.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
