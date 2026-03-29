# Platform Targets — Kaynexis Agentic Game Studio

## Supported platforms
| Platform | Priority | Input | Perf target | Special constraints |
|---|---|---|---|---|
| PC Premium | Primary | Keyboard/mouse + controller | 60 FPS target | Settings scalability and sane defaults |
| Web Demo | Secondary | Keyboard/mouse + controller | 60 FPS target with shorter sessions | Asset size, startup latency, browser-safe persistence |
| Console Premium | Research | Controller-first | 60 FPS target with stable frame pacing | Save safety, certification flows, stricter memory/perf discipline |
| Mobile | Deferred research | Touch + controller if supported | 30-60 FPS depending on class | Battery, thermal load, UI scale, session compression |

## Store / submission notes
- PC storefront readiness should include screenshots, controller support notes, and a demo-friendly build path
- Web demo should be treated as a discovery funnel, not as parity with the full PC target
- Console work should not start until build/export, save, and TRC-style compliance assumptions are explicit

## Input & UX implications
- Keyboard/mouse must feel native
- Controller parity should exist before external playtests
- Accessibility should cover subtitle readability, remappable controls where practical, and clear feedback
- Web should degrade gracefully if persistence is browser-backed only
- Mobile should only move forward once touch affordances and pause/resume handling are designed on purpose
