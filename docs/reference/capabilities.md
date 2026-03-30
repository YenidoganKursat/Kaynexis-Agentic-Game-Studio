# Capability Catalog

## Summary

Use this page when you want the shortest durable explanation of what this studio can do.
This is the master overview for the repo's capability surface: it is the brochure, not the deep-dive.
If a request is narrower, jump directly to the matching lane instead of expanding this page into a feature brief.

## Primary sources

- `docs/README.md`
- `docs/reference/repo-tour.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-execution.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/engine-bugs.md`
- `docs/reference/system-atlas.md`
- `docs/reference/perf-guide.md`
- `docs/reference/benchmark-guide.md`
- `docs/reference/quality-guide.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/library-guide.md`
- `docs/reference/asset-guide.md`
- `docs/reference/sector-intel.md`
- `docs/reference/steam-intel.md`
- `docs/reference/platform-guide.md`
- `docs/reference/marketing-guide.md`
- `docs/reference/marketing-intel.md`
- `docs/reference/audio-animation-guide.md`
- `docs/reference/ui-guide.md`
- `docs/reference/gpu-guide.md`
- `docs/reference/theory-guide.md`
- `docs/research/game-development/production/content-pipeline.md`
- `studio/docs/active/telemetry-schema.md`
- `studio/playbooks/porting-program.md`

## Why this matters to this repo

- New contributors and agents need a fast answer to "what can this system help with?"
- The repo already has many specialized lanes; without a master map, those lanes can feel disconnected.
- A capability catalog keeps the public summary short while still pointing to the right starting docs.
- It also helps the routing layer pick the correct narrow lane before work starts.

## Decision impact

- Use this page for a high-level tour of the studio, not for a feature contract.
- Use a narrower lane when the request is already specific enough to need implementation details.
- Keep the catalog aligned with the route table, the README indexes, the examples index, and the research tree.
- Keep every capability family backed by a guide, an example, and a validation path.

## Capability families

| Family | What it covers | Best starting docs |
| --- | --- | --- |
| agent control | controller, role matrix, hierarchy, execution packets, prompt history, transcripts, and validation matrices | `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/reference/agent-hierarchy.md`, `docs/reference/agent-execution.md`, `docs/reference/prompt-journal.md`, `docs/reference/agent-transcript.md`, `docs/reference/agent-validation-matrix.md` |
| model and platform fit | OpenAI/Codex compatibility, model choice, plan-tier fit, and sub-agent overrides | `docs/research/openai-codex-infra-findings.md`, `docs/research/openai-codex-models.md`, `docs/reference/codex-compatibility.md`, `docs/reference/codex-model-guide.md` |
| engine and gameplay | engine selection, engine eval, engine-fit, engine atlas, system atlas, and engine-specific class ownership | `docs/reference/engine-selection-guide.md`, `docs/reference/engine-eval.md`, `docs/reference/engine-fit.md`, `docs/reference/engine-map.md`, `docs/reference/engine-atlas.md`, `docs/reference/system-atlas.md` |
| engine troubleshooting | recurring engine bug families, first checks, and debug surfaces | `docs/reference/engine-bugs.md`, `docs/examples/engine-bugs-example.md`, `docs/research/game-development/foundations/engine-bugs.md` |
| gameplay design | feature briefs, mechanics, combat, quests, puzzles, UI flow, tutorial flow, save, multiplayer, and progression | `docs/reference/feature-traceability.md`, `docs/reference/genre-plan.md`, `docs/reference/genre-presets.md`, `docs/research/game-development/systems/` |
| genre planning | genre family shape, contrast sets, loop ladders, and maturity checks | `docs/reference/genre-plan.md`, `docs/research/game-development/genre/genre-guide.md`, `docs/research/game-development/genre/genre-patterns.md`, `docs/research/game-development/genre/genre-maturity.md` |
| content and presentation | assets, content pipeline, audio, animation, art readability, localization, UI, and narrative production | `docs/reference/asset-guide.md`, `docs/research/game-development/production/content-pipeline.md`, `docs/reference/audio-animation-guide.md`, `docs/reference/ui-guide.md`, `docs/reference/lorebook-methodology.md`, `docs/reference/world-graph-methodology.md`, `docs/research/game-development/narrative/` |
| architecture, custom packs, and extensibility | authority, state, events, projection, custom packs, custom architecture, request rules, and extension packs | `docs/reference/architecture-guide.md`, `docs/reference/custom-packs.md`, `docs/examples/custom-packs-example.md`, `docs/research/game-development/foundations/custom-packs.md`, `docs/reference/custom-architecture.md`, `docs/reference/extensions-guide.md` |
| quality and measurement | QA matrices, bug triage, perf, advanced perf, GPU, benchmarks, engine eval, and quality processes | `docs/reference/feature-traceability.md`, `docs/reference/perf-guide.md`, `docs/reference/advanced-perf-guide.md`, `docs/reference/gpu-guide.md`, `docs/reference/benchmark-guide.md`, `docs/reference/quality-guide.md`, `docs/reference/quality-process.md`, `docs/reference/engine-eval.md`, `studio/checklists/discipline/qa_lead.toml` |
| production and market | CI/CD, release hardening, versioning, platform compatibility, console readiness, Steam signals, sector signals, marketing strategy, and marketing status | `docs/reference/ci-cd.md`, `docs/reference/release-hardening-guide.md`, `docs/reference/version-guide.md`, `docs/reference/platform-guide.md`, `docs/reference/console-guide.md`, `docs/reference/steam-intel.md`, `docs/reference/sector-intel.md`, `docs/reference/marketing-guide.md`, `docs/reference/marketing-intel.md` |
| telemetry and market intelligence | funnels, metrics, dashboards, chart packs, and current signal summaries | `studio/docs/active/telemetry-schema.md`, `docs/reference/steam-intel.md`, `docs/reference/sector-intel.md`, `docs/reference/marketing-intel.md` |
| platform and porting | PC, console, web, mobile, Steam Deck, TV/webOS, support tiers, and platform-readiness deltas | `docs/reference/platform-guide.md`, `docs/reference/console-guide.md`, `docs/reference/cross-platform-guide.md`, `docs/research/game-development/production/platform-compatibility.md`, `docs/research/game-development/production/console.md`, `studio/playbooks/porting-program.md`, `studio/playbooks/demo-festival.md` |

## How to present the capability surface

When the user asks "what can this repo do?", answer in this order:

1. one short sentence that explains the studio's overall scope
2. the 5 to 8 biggest capability families
3. the best starting docs for the specific family the user seems to care about
4. the narrow lane to use next if they want implementation, measurement, or validation

## Example prompts for the agent

- "Summarize everything this studio can do and point me at the right starting docs for each lane."
- "Turn the repo's capability surface into a one-page intro for a new contributor."
- "Show me the studio capability catalog and the shortest starting docs for each family."
- "I want the full surface area of this repo, but keep the answer simple and scannable."

## Validation

A good capabilities pass should leave behind:

- one master catalog that groups the studio's major capabilities
- one example showing how to present the catalog simply
- one research note that keeps the catalog evidence-backed
- one checklist that keeps the catalog narrow and current
- one eval plan that proves the broad intro routes to the right docs
- one short repo summary that a newcomer can read quickly

## Related docs

- `docs/examples/capabilities-example.md`
- `docs/research/game-development/foundations/capabilities.md`
- `docs/reference/repo-tour.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/system-atlas.md`
- `docs/reference/marketing-intel.md`
- `docs/reference/steam-intel.md`
- `docs/reference/platform-guide.md`
- `docs/reference/console-guide.md`
- `docs/reference/cross-platform-guide.md`
- `docs/examples/console-example.md`
- `docs/examples/cross-platform-example.md`
- `docs/research/game-development/production/console.md`
- `docs/research/game-development/production/cross-platform.md`
- `docs/reference/release-hardening-guide.md`
- `docs/examples/release-hardening-example.md`
- `docs/research/game-development/production/release-hardening.md`
- `docs/research/game-development/production/content-pipeline.md`
- `studio/docs/active/telemetry-schema.md`
- `studio/playbooks/porting-program.md`
