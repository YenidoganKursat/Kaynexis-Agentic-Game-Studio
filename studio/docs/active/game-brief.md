# Game Brief — Codex Game Studio Pro Max

## High concept
- Codex-first Action Roguelite project focused on a small but high-quality first playable slice
- Target audience: players who value readable action, replayable runs, and build experimentation
- Reference titles / contrast set: Hades, Dead Cells, Risk of Rain 2
- Current example baseline uses `godot-4` as the active engine, while the repo itself keeps Unity 6 and Unreal 5 starter-kit, checklist, research, and CI support ready

## Player fantasy
- Survive a compact high-pressure encounter and come out stronger through clear build choices
- Keep playing to master combat readability and discover stronger run combinations

## Core pillars
- Readable moment-to-moment combat
- Short sessions with meaningful upgrade choice
- A small vertical slice that can grow without losing clarity

## Scope guardrails
- In scope: first combat room, basic enemy telegraphs, one upgrade choice, PC-first controls
- Out of scope: full metaprogression, content volume, liveops, monetization, multiplayer
- Nice-to-have later: expanded build diversity, content scale, external demo polish

## Platforms & business model
- Platforms: PC Premium
- Input assumptions: keyboard/mouse plus controller parity
- Pricing / monetization stance: premium-first baseline with no F2P systems in the first slice

## Milestone target
- Prototype -> vertical slice
- Exit criteria: one stable, replayable combat slice with clear validation and genre fit

## Operating loop
- Route work with `python3 scripts/codex_studio.py next "..."`
- Resolve the checklist bundle with `python3 scripts/codex_studio.py checklist --task "..."`
- Link or create research in `docs/research/game-development/`
- Update `studio/docs/active/current-sprint.md` and `studio/docs/active/decision-log.md` as the slice changes

## Known risks
- Readability can collapse before depth is proven
- Scope can grow faster than validation
- Engine and build assumptions still need to be confirmed with real project files
