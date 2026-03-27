# Codex Game Studio Pro Max

Treat this repository as a disciplined game studio operating system for Codex, not as a one-shot assistant prompt.

## Operating stance

- Default to **small, reversible, well-validated vertical slices**.
- Use the repo as the durable source of truth. Chat is ephemeral; docs and code are durable.
- Keep mutable studio state in `studio/docs/active/`.
- Keep durable behavior in `AGENTS.md`, `.codex/config.toml`, `.codex/agents/`, `.agents/skills/`, and nested `AGENTS.md` files.
- Prefer **evidence over confidence**: cite files, systems, scenes, prefabs, modules, data assets, logs, or docs that support your recommendation.
- When version-sensitive behavior matters, verify with primary documentation before committing to design or implementation.

## Protected-path rule

This template assumes normal Codex `workspace-write` usage.
In many environments, `.git/` and `.codex/` remain protected even when the workspace is writable.
Therefore:

- do not store living project status in `.codex/`
- do not expect to mutate `.codex/` or `.agents/` during normal feature work
- place mutable production docs in `studio/docs/active/`

## Default response contract

For any non-trivial task, structure work around:

1. **Current state**
   - What the repo or docs already say
   - What is still ambiguous
2. **Plan**
   - Smallest viable path
   - Systems / files / docs likely to change
3. **Execution or recommendation**
   - What changed or what should change
   - Why this route is preferred
4. **Validation**
   - Commands run, tests, manual checks, or missing evidence
5. **Risks and next step**
   - What is still uncertain
   - Which skill or role should engage next

## Review and eval discipline

- Keep detailed review criteria in `docs/reference/code-review.md` instead of expanding this file.
- When changing `AGENTS.md`, `.codex/config.toml`, `.codex/agents/`, `.agents/skills/`, or shared routing/setup scripts, create or update an `eval-plan-*.md` in `studio/docs/active/`.
- Prefer read-heavy reviewer or docs roles first when a change could affect correctness, safety, or version-sensitive behavior.

## Routing heuristic

When the task is ambiguous, start with `$intake-router` or `python3 scripts/route_task.py "<task>"`.

Use these broad lanes:

- **Project framing / milestone / audit** -> `$studio-start`, `$project-radar`, `$scope-rescue`
- **Feature design** -> `$feature-brief`, `$mechanic-design`, `$combat-loop`, `$quest-flow`
- **Implementation** -> `$gameplay-slice`, `$ui-flow`, `$save-system`, `$multiplayer-slice`
- **Content / style** -> `$art-style-pack`, `$audio-style-pack`, `$content-pipeline`
- **Risk / quality** -> `$qa-matrix`, `$bug-triage`, `$perf-pass`, `$accessibility-audit`
- **Release / go-to-market** -> `$storefront-launch`, `$console-cert-readiness`, `$release-gate`, `$marketing-beat-brief`

## Decision protocol

Use this protocol for meaningful design or implementation work:

1. Frame the player outcome.
2. Map the real code/content path.
3. Choose the smallest validated slice.
4. Surface tradeoffs: scope, feel, maintainability, performance, release risk.
5. Record durable decisions in docs when they matter.
6. Validate honestly and report evidence.

## Subagent policy

Use subagents intentionally, not reflexively.

- Prefer at most **4 concurrent subagents** unless the user explicitly asks for wider fan-out.
- Use read-heavy roles first when the problem is still being mapped.
- Use implementation specialists after the touched systems are known.
- If subagents are unavailable, emulate the same workflow sequentially while preserving role boundaries.

Each subagent result should include:

- what it examined
- the main finding
- the biggest risk it sees
- the recommended next action

## Durable doc policy

Use `studio/docs/active/` for mutable project state, especially:

- `game-brief.md`
- `engine-profile.md`
- `current-sprint.md`
- `milestones.md`
- `risk-register.md`
- `decision-log.md`
- platform, art, audio, telemetry, monetization, build, content, and localization docs
- feature briefs, ADRs, test plans, bug reports, perf passes, release checklists, and postmortems
- eval plans for behavior-changing instruction, routing, or agent updates

## File and task conventions

### Code
- Prefer small diffs over broad refactors.
- Preserve engine-native layout where the engine clearly dictates it.
- When changing behavior, update tests or write the manual validation story explicitly.

### Content
- Use lower_snake_case for new asset filenames where the engine permits it.
- Keep content naming deterministic.
- Note import, compression, and memory-sensitive changes in docs if they affect runtime behavior.

### Design and production docs
- Update existing docs before creating near-duplicate docs.
- One durable source of truth per decision.
- Keep docs concise enough to maintain, but concrete enough to execute.

## Role boundaries

- Directors/producers own framing, scope, sequencing, and risk.
- Designers own player-facing rules, pacing, progression, economy, and flow.
- Programmers own implementation, integration, and technical validation.
- QA/perf/security/release roles own confidence, abuse-path review, and ship risk.
- Art/audio roles own style, readability, pipeline implications, and production constraints.
- `docs_researcher` only backs claims with primary docs; it should not silently override design/product judgment.

Do not let one role silently consume several disciplines on high-risk tasks. Surface the cross-functional tradeoff explicitly.

## Engine hints

Inspect the repo before guessing the engine:

- Godot clues: `project.godot`, `.tscn`, `.tres`, `.gd`
- Unity clues: `Assets/`, `ProjectSettings/`, `Packages/manifest.json`
- Unreal clues: `*.uproject`, `Config/`, `Content/`, `Source/`

When the engine is version-sensitive, verify before relying on memory.

## Recommended first moves in a fresh repo

1. run `$studio-start`
2. confirm `studio/docs/active/game-brief.md`
3. confirm `studio/docs/active/engine-profile.md`
4. run `$project-radar`
5. create a feature brief
6. implement one small slice
7. generate a QA matrix before calling it done
