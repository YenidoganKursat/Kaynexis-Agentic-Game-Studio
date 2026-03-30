# Console Readiness

## Date
- 2026-03-30

## Summary
- Console work in this repo means PS5-like, Xbox-like, or Switch-like targets that need submission evidence, controller-first UX, suspend/resume safety, save and entitlement correctness, and a clear first blocker.
- Public first-party web docs are usually high level; the real cert and submission contracts often live in platform-holder partner portals. This note therefore treats the public docs as the orientation layer and the partner portal as the source of truth when available.

## Primary sources
- [Official Licensing Program - Sony Interactive Entertainment](https://sonyinteractive.com/en/contact-us/official-licensing-program/)
- [Microsoft Gaming Documentation Hub](https://learn.microsoft.com/en-us/gaming/)
- [docs/reference/platform-guide.md](../../../reference/platform-guide.md)
- [docs/reference/cross-platform-guide.md](../../../reference/cross-platform-guide.md)
- [studio/docs/templates/cert-checklist.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/templates/cert-checklist.md)
- [studio/playbooks/porting-program.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/playbooks/porting-program.md)

## Why this matters to this repo
- The repo already models platform compatibility, cross-platform support tiers, and release sequencing, but PS5-like work needs a more explicit console lane.
- The `console-premium` preset and the cert checklist template are already present; this note defines how they should be used together.

## Decision impact
- Separate PS5-like, Xbox-like, and Switch-like families when they differ in input, cert, or submission gates.
- Name the first submission gate, the first cert blocker, and the first runtime blocker before scope hardens.
- Keep console support tier explicit instead of silently collapsing everything into "console".

## Delta map
| Delta | What usually changes first | Repo implication |
| --- | --- | --- |
| Input | Controller-first navigation, remapping, focus order, and pause behavior | Keep `docs/reference/console-guide.md` and `studio/docs/templates/platform-targets.md` aligned |
| Runtime | Suspend/resume, save integrity, entitlement flow, and network reconnects | Keep `studio/docs/templates/cert-checklist.md` explicit about evidence |
| Packaging | Build signing, submission metadata, store assets, and submission gates | Keep `studio/playbooks/porting-program.md` paired with the active platform target note |
| Performance | Memory ceilings, frame pacing, and loading expectations | Keep the first performance gate visible before tuning other families |

## Repo impact
- Add console as a first-class family in the platform target matrix.
- Route PS5-like tasks through a dedicated console lane instead of a generic porting note.
- Keep submission evidence, controller-first UX, and save/suspend safety reviewable in the active docs.

## Related docs
- [docs/reference/console-guide.md](../../../reference/console-guide.md)
- [docs/examples/console-example.md](../../../examples/console-example.md)
- [docs/reference/platform-guide.md](../../../reference/platform-guide.md)
- [docs/reference/cross-platform-guide.md](../../../reference/cross-platform-guide.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
- [studio/checklists/discipline/console.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/console.toml)
- [studio/docs/active/eval-console.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-console.md)
