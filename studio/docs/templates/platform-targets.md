# Platform Targets — {PROJECT_NAME}

## Supported platforms
| Platform | Priority | Input | Perf target | Special constraints |
|---|---|---|---|---|
| {PLATFORM} | Primary | Fill from the active project profile | Set a measurable target before implementation | Note cert, input, browser, touch, focus, or packaging constraints here |
| Windows PC | Primary / Secondary | Keyboard/mouse + controller | Set a measurable target before implementation | Installer, windowing, GPU driver, and storefront assumptions |
| macOS | Primary / Secondary | Keyboard/mouse + controller | Set a measurable target before implementation | App Sandbox, signing, controller, and Metal / Apple Silicon assumptions |
| Linux / Steam Deck | Secondary / Research | Controller + keyboard/mouse | Set a measurable target before implementation | Steamworks, Proton / SteamOS, and Deck verification assumptions |
| Console / PS5-like | Secondary / Research | Controller | Set a measurable target before implementation | Submission gates, suspend/resume, entitlement, and cert evidence assumptions |
| Web Demo | Secondary | Keyboard/mouse + controller where supported | Set a measurable target before implementation | Browser memory, asset budget, focus loss, and PWA / persistence assumptions |
| Android / iOS | Deferred research | Touch + controller if supported | Set a measurable target before implementation | Battery, thermal load, session length, store-review, and safe area assumptions |
| webOS / TV | Deferred research | Remote + controller | Set a measurable target before implementation | 10-foot UI, focus navigation, remote input, and TV storefront assumptions |

If a platform is not in scope yet, leave it out instead of pretending it has full support.

## Store / submission notes
- Accounts, sandboxes, entitlements, cert, browser/mobile specifics, Steam Deck / Steamworks notes, and TV store rules

## Input & UX implications
- Keyboard/mouse, controller, touch, handheld, focus navigation, safe areas, accessibility, and 10-foot readability

## Read this alongside
- `docs/reference/platform-guide.md`
- `docs/reference/console-guide.md`
- `docs/examples/platform-example.md`
- `docs/examples/console-example.md`
- `docs/research/game-development/production/platform-compatibility.md`
