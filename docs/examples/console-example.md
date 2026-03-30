# Console Example

## Scenario
- The project has a console-premium target and the team wants a PS5-like porting and submission-readiness readout before scope hardens.

## Baseline
- The project already has a console-premium target and a shared build that can be evaluated family by family.

## Decision order
1. Name the console family and support tier.
2. Check controller-first UX and suspend/resume behavior.
3. Check save, entitlement, and packaging assumptions.
4. Name the first submission blocker before implementation starts.

## Input
- Source family: desktop premium
- Target family: PS5-like console premium
- Primary concern: controller-first UX, suspend/resume, entitlement, save integrity, and submission evidence

## Output shape
- One family matrix
- One cert-risk card
- One release-order card
- One repository implication

## Example matrix
| Family | Tier | First delta | First gate |
| --- | --- | --- | --- |
| PS5-like | supported | Controller-first UI, suspend/resume, entitlement, and save behavior | Controller pass plus one suspend/resume proof |
| Xbox-like | supported | Submission evidence, controller behavior, and packaging notes | Submission checklist pass |
| Switch-like | research | Handheld frame pacing, memory, and safe-area constraints | Portable build smoke |

## Example chart pack
- Family heatmap: readiness by console family
- Decision card: core family, next family, first blocker
- Submission board: account, metadata, build, evidence, and risk

## Repo impact
- Keep `studio/docs/active/platform-targets.md` honest with a console row.
- Keep `studio/checklists/discipline/console.toml` synchronized with the console guide and research note.
- Keep `studio/docs/templates/cert-checklist.md` aligned with the submission evidence trail.

## Related docs
- [docs/reference/console-guide.md](../reference/console-guide.md)
- [docs/reference/platform-guide.md](../reference/platform-guide.md)
- [docs/reference/cross-platform-guide.md](../reference/cross-platform-guide.md)
- [docs/research/game-development/production/console.md](../research/game-development/production/console.md)
- [studio/docs/templates/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/templates/platform-targets.md)
