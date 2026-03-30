# Console Guide

## Summary
- Use this guide when the target is a PS5-like, Xbox-like, or Switch-like console family that needs submission evidence, controller-first UX, suspend/resume safety, and entitlement or save correctness.
- Treat console work as a porting-and-certification problem, not just a packaging step.
- If the task also needs support tiers or release sequencing, pair this guide with `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md`, and `docs/research/game-development/production/console.md`.

## Primary sources
- [Official Licensing Program - Sony Interactive Entertainment](https://sonyinteractive.com/en/contact-us/official-licensing-program/)
- [Microsoft Gaming Documentation Hub](https://learn.microsoft.com/en-us/gaming/)
- Platform-holder partner or certification portal docs when they are available to the project

## Why this matters to this repo
- The repo already has a `console-premium` platform preset, a porting playbook, a cert checklist template, and platform target templates.
- Console work becomes risky when PS5-like targets are treated as just another desktop build.
- The agent needs a source-backed way to separate controller-first UX, suspend/resume, save, entitlement, packaging, and submission evidence.

## Decision impact
- Separate PS5-like, Xbox-like, and Switch-like families when they differ in input, cert, or release gate.
- Name the first submission gate and the first cert blocker before scope hardens.
- Keep console support tier explicit: core, supported, demo, research, or deferred.

## Console family map
| Family | First question | First lever | Typical owners |
| --- | --- | --- | --- |
| PS5-like console premium | Can the build survive controller-first flow, suspend/resume, and submission evidence? | Controller-first UX, save and entitlement handling, packaging, and cert evidence | `porting_engineer`, `certification_manager`, `ux_designer`, `build_release_engineer` |
| Xbox-like console premium | Does the build match Microsoft submission and controller expectations? | Input, packaging, compliance notes, and submission evidence | `porting_engineer`, `certification_manager`, `release_manager` |
| Switch-like handheld console | Does the build respect handheld performance, suspend/resume, and safe-area constraints? | Frame pacing, memory, battery or suspend, and UI scale | `porting_engineer`, `performance_analyst`, `ux_designer` |

## Visualization pack
- Family cards
- Submission gate map
- Cert-risk heatmap
- Controller-first flow chart

## Example prompts for the agent
- "Map PS5-like console readiness for our current build and call out the first cert blocker."
- "Turn our platform targets into a console submission matrix for PS5-like, Xbox-like, and Switch-like families."
- "Compare the first porting delta between desktop premium and console premium and tell me whether it is an input, save, or cert issue."

## Validation
- Name the console family and the support tier before summarizing.
- Separate input, suspend/resume, save, entitlement, packaging, and submission deltas.
- Return one matrix or chart pack plus one repository implication.

## Related docs
- [docs/reference/platform-guide.md](platform-guide.md)
- [docs/reference/cross-platform-guide.md](cross-platform-guide.md)
- [docs/examples/platform-example.md](../examples/platform-example.md)
- [docs/examples/cross-platform-example.md](../examples/cross-platform-example.md)
- [docs/examples/console-example.md](../examples/console-example.md)
- [docs/research/game-development/production/console.md](../research/game-development/production/console.md)
- [docs/research/game-development/production/platform.md](../research/game-development/production/platform.md)
- [studio/docs/templates/cert-checklist.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/templates/cert-checklist.md)
- [studio/docs/templates/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/templates/platform-targets.md)
- [studio/playbooks/porting-program.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/playbooks/porting-program.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
- [studio/checklists/discipline/console.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/console.toml)
- [studio/docs/active/eval-console.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-console.md)
