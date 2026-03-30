# Studio Map

This page is the compact front door for the repo. If you only want one page that explains how the studio is organized, start here.

## Core flow

1. Read the compact map.
2. Pick the lane that matches the task.
3. Route the task through `scripts/codex_studio.py next` or `scripts/route_task.py`.
4. Render the matching checklist.
5. Update the durable active doc in `studio/docs/active/`.
6. Validate with the narrowest proof path.

## Main lanes

| Lane | What it is for | Start here |
| --- | --- | --- |
| setup | onboarding, engine install, agent bootstrap, and quick access | `docs/setup/quick-access.md`, `docs/setup/getting-started.md`, `docs/setup/first-hour-walkthrough.md` |
| speed pack | fastest safe start, smallest useful bundle, and short validation | `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `docs/research/game-development/foundations/agent-speedpack.md` |
| capability map | the studio brochure, lane chooser, and first-step guidance | `docs/reference/capabilities.md`, `docs/examples/capabilities-example.md`, `docs/research/game-development/foundations/capabilities.md` |
| operating model | controller, roles, hierarchy, execution packets, history, and transcripts | `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/reference/agent-hierarchy.md`, `docs/reference/agent-execution.md`, `docs/reference/prompt-journal.md`, `docs/reference/agent-transcript.md` |
| engine choice | engine fit, object ownership, engine atlas, bugs, and evaluation | `docs/reference/engine-selection-guide.md`, `docs/reference/engine-fit.md`, `docs/reference/engine-map.md`, `docs/reference/engine-atlas.md`, `docs/reference/engine-bugs.md`, `docs/reference/engine-eval.md` |
| gameplay planning | genre presets, genre plans, example games, theory, and mechanics | `docs/reference/genre-presets.md`, `docs/reference/genre-plan.md`, `docs/reference/genre-perf-guide.md`, `docs/reference/advanced-perf-guide.md`, `docs/reference/theory-guide.md`, `docs/reference/architecture-guide.md` |
| production and release | CI/CD, versioning, release hardening, platform fit, console readiness, Steam, sector signals, and marketing | `docs/reference/ci-cd.md`, `docs/reference/version-guide.md`, `docs/reference/release-hardening-guide.md`, `docs/reference/platform-guide.md`, `docs/reference/console-guide.md`, `docs/reference/cross-platform-guide.md`, `docs/reference/steam-intel.md`, `docs/reference/sector-intel.md`, `docs/reference/marketing-guide.md`, `docs/reference/marketing-intel.md` |
| scale and customization | custom packs, custom architecture, extensions, libraries, assets, benchmarks, quality, perf, and GPU | `docs/reference/custom-packs.md`, `docs/reference/custom-architecture.md`, `docs/reference/extensions-guide.md`, `docs/reference/library-guide.md`, `docs/reference/asset-guide.md`, `docs/reference/benchmark-guide.md`, `docs/reference/quality-guide.md`, `docs/reference/perf-guide.md`, `docs/reference/gpu-guide.md` |

## Where durable truth lives

- `studio/docs/active/` for living project state
- `docs/reference/` for stable operating rules
- `docs/examples/` for short, concrete bundles
- `docs/research/game-development/` for source-backed explanations
- `studio/checklists/` for merge-ready review criteria
- `tests/` and `scripts/` for proof, smoke, and validation

## If you only read one page

Start with this file, then go to:

1. `docs/setup/quick-access.md`
2. `docs/reference/repo-tour.md`
3. `docs/reference/capabilities.md`
4. `docs/reference/agent-system.md`
5. `docs/reference/engine-selection-guide.md`

## Professional rule

Keep one lane, one proof path, and one durable active doc for each meaningful piece of work. If the answer needs more than one lane, make the split explicit before implementation.
