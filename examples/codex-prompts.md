# Codex Prompt Recipes

## Bootstrap / intake

```text
$studio-start We are building a compact single-player action roguelite for PC in Godot 4. The first milestone is a combat-heavy vertical slice with one arena, three enemies, one boss, and full controller support.
```

```text
$intake-router I need to turn this messy repo into a release-ready Steam Next Fest demo in 6 weeks. Tell me the best skill sequence and highest risks.
```

```text
python3 scripts/route_task.py "We need to add co-op, cloud saves, and a mobile port next quarter. What should we tackle first?"
```

## Feature design

```text
$feature-brief Add a grapple hook traversal feature that supports controller aim assist and doesn’t trivialize combat arenas.
```

```text
$mechanic-design Design a chargeable dodge counter mechanic for a fast melee combat game. Keep it readable and testable.
```

```text
$tutorial-onboarding Our first 10 minutes are too confusing. Rebuild the onboarding around three essential verbs only.
```

## Implementation

```text
$gameplay-slice Implement one vertical slice for a stamina-based sprint + dodge system. Summarize files touched and validation.
```

```text
$ui-flow Build a settings flow for graphics, audio, controller remapping, and accessibility toggles.
```

```text
$save-system We need profile saves, mid-run checkpoints, and migration safety for future updates.
```

## Multiplayer / backend

```text
$multiplayer-slice Add a co-op revive mechanic with clear authority rules and a QA matrix for latency/desync checks.
```

```text
$backend-foundation Frame the minimal backend needed for lobby creation, match join, and entitlement-safe profile sync.
```

```text
$security-threat-model Threat-model our co-op inventory sync and loot economy before implementation.
```

## Quality / release

```text
$bug-triage Players say the game sometimes soft-locks after pausing during a boss intro. Turn this into a repro-ready bug report.
```

```text
$perf-pass FPS tanks when three elite enemies spawn and VFX stack. Give me the smallest high-impact optimization path.
```

```text
$release-gate Review this milestone as a ship/no-ship candidate for Steam demo release.
```

## Content / go-to-market

```text
$art-style-pack Build a lightweight visual style pack for a stylized sci-fi extraction-lite game that must read well at top-down camera distance.
```

```text
$localization-pass Prepare our UI and glossary for English, Turkish, German, and Japanese.
```

```text
$storefront-launch Prepare a Steam page readiness checklist and asset gap list for our first public demo.
```

```text
$marketing-beat-brief Build the messaging for our festival demo announcement with CTA, proof points, and follow-up beats.
```
