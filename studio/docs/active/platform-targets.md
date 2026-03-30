# Platform Targets — Kaynexis Agentic Game Studio

## Supported platforms
| Platform | Support tier | Priority | Input | Perf target | Special constraints |
|---|---|---|---|---|---|
| Windows PC | `core` | Primary | Keyboard/mouse + controller | 60 FPS target | Installer, drivers, windowing, and scalable settings |
| macOS | `supported` | Secondary | Keyboard/mouse + controller | 60 FPS target | App Sandbox, signing, Apple Silicon, and controller parity |
| Linux / Steam Deck | `supported` | Secondary | Controller + keyboard/mouse | 60 FPS target with stable frame pacing | Steamworks, Proton / SteamOS, Deck verification, and compatibility notes |
| Console / PS5-like | `supported` | Secondary | Controller | 60 FPS target with suspend/resume proof | Submission gates, entitlement, save safety, and cert evidence |
| Web Demo | `demo` | Secondary | Keyboard/mouse + controller | 60 FPS target with shorter sessions | Asset size, startup latency, browser-safe persistence, and focus loss |
| Android / iOS | `research` | Deferred research | Touch + controller if supported | 30-60 FPS depending on class | Battery, thermal load, UI scale, session compression, and store review |
| webOS / TV | `research` | Deferred research | Remote + controller | 30-60 FPS depending on class | 10-foot UI, focus navigation, safe areas, and TV store rules |

## Store / submission notes
- PC storefront readiness should include screenshots, controller support notes, and a demo-friendly build path
- Web demo should be treated as a discovery funnel, not as parity with the full PC target
- Steam should explicitly call out Steamworks / Steam Deck assumptions and controller coverage
- Console / PS5-like work should explicitly call out submission gates, suspend/resume, entitlement, and controller-first evidence
- Mobile and TV work should not start until touch, focus, safe-area, and store-policy assumptions are explicit

## Platform compatibility guide
- Read `docs/reference/platform-guide.md` before changing targets, store assumptions, or porting scope
- Read `docs/reference/cross-platform-guide.md` when the task also needs support tiers or release sequencing
- Use `docs/examples/platform-example.md` for dashboard and matrix examples
- Use `docs/examples/cross-platform-example.md` for support-tier and release-order examples
- Keep `docs/research/game-development/production/platform-compatibility.md` nearby for source-backed platform notes
- Keep `docs/research/game-development/production/cross-platform.md` nearby for source-backed support tiers and release sequencing

## Input & UX implications
- Keyboard/mouse must feel native
- Controller parity should exist before external playtests
- Accessibility should cover subtitle readability, remappable controls where practical, and clear feedback
- Web should degrade gracefully if persistence is browser-backed only
- Mobile should only move forward once touch affordances and pause/resume handling are designed on purpose
- TV should assume 10-foot readability and remotes or controllers as the primary input surface

## Decision prompts
- What is the primary platform family and which family comes next?
- What support tier does each family deserve, and in what order should they ship?
- What input model or store policy changes between them?
- What is the first measurable delta that would block or change the release plan?
