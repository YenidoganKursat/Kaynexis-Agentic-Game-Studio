# Task And Prompt Examples

This repo works best when tasks are concrete.

The goal is not to write fancy prompts. The goal is to give Codex enough shape to route, checklist, and validate the work correctly.

## Strong task patterns

Good tasks usually include at least two of these:

- the player or system outcome
- the engine or platform context
- the constraint
- the validation goal

Example:

- "Implement a readable dodge cancel window for the first Godot combat room."
- "Design a Unity-friendly save-state ownership model for mission progress."
- "Prepare the first Unreal Win64 packaging path and document the constraints."

## Weak task patterns

These are too broad:

- "work on combat"
- "fix the engine stuff"
- "make the UI better"
- "optimize performance"

These give weak routing and weak checklists because the system cannot tell what actually changed.

## Good `next` examples

Gameplay:

```bash
python3 scripts/codex_studio.py next \
  "Implement a short parry window with clear failure feedback for the tutorial encounter"
```

AI and navigation:

```bash
python3 scripts/codex_studio.py next \
  "Design a performant 2D enemy pathfinding setup for Unity rooms with blockers"
```

Build and release:

```bash
python3 scripts/codex_studio.py next \
  "Prepare the first Unreal package flow for a Win64 demo build"
```

Tools:

```bash
python3 scripts/codex_studio.py next \
  "Create a small import helper for batch-tagging combat VFX assets"
```

## Good `checklist` examples

```bash
python3 scripts/codex_studio.py checklist \
  --task "Ship the first Godot combat room"
```

```bash
python3 scripts/codex_studio.py checklist \
  --task "Refactor Unity combat projectiles into a pooled runtime path"
```

```bash
python3 scripts/codex_studio.py checklist \
  --task "Prepare Unreal 5 package validation for the first external demo"
```

## Good `research` examples

```bash
python3 scripts/codex_studio.py research \
  --category systems \
  --title "Combat readability baseline"
```

```bash
python3 scripts/codex_studio.py research \
  --category production \
  --title "First external demo release validation"
```

```bash
python3 scripts/codex_studio.py research \
  --category engines \
  --title "Unity prefab ownership for combat rooms"
```

## Better phrasing by discipline

Combat:

- "Add a heavier melee enemy with a slower but more legible windup."
- "Tune damage feedback so failure reads immediately without freezing the pace."

UI:

- "Design a compact upgrade choice screen that fits controller-first navigation."
- "Add a pause menu flow with resume, restart, and settings."

Save systems:

- "Define what should persist after a failed run versus what resets."
- "Plan a migration-safe save structure for progression unlocks."

Performance:

- "Measure projectile count scaling and choose between pooling and representation change."
- "Decide whether this Unity crowd problem should stay classic-object based or move toward data-oriented scale."

Build pipeline:

- "Document the first reproducible demo export path and its artifact naming."
- "Add a release-readiness review step for nightly engine-contract smoke."

## Ask for one slice, not one department

Good:

- "Implement the first upgrade choice after room clear."
- "Investigate why dodge sometimes exits the arena bounds."

Bad:

- "Finish progression."
- "Do the whole build pipeline."

If a task sounds like multiple weeks, split it before routing it.

## Good direct prompts to Codex

If you are talking directly to Codex in the thread, these patterns work well:

- "Route this task and tell me which docs I should update first: ..."
- "Give me the merged checklist for this Unreal packaging task and keep it practical."
- "Turn this idea into a smaller vertical slice before we implement it: ..."
- "Find the highest-risk part of this feature and suggest a validation-first plan."
- "Convert this vague bug into reproducible steps, hypotheses, and next action."

## Prompt upgrade examples

Weak:

- "add enemy"

Better:

- "Add a second enemy type that pressures movement rather than burst damage, and keep the tutorial room readable."

Weak:

- "optimize unity"

Better:

- "Review whether our Unity projectile handling should stay pooled MonoBehaviours or move toward a more data-oriented scale path."

Weak:

- "release setup"

Better:

- "Prepare a realistic release-readiness checklist for the first external PC demo and show which CI checks should be mandatory."

## When to make a feature brief first

Make a brief before routing if the task changes:

- save ownership
- combat rules
- progression structure
- architecture boundaries
- engine representation choice
- packaging or release expectations

Use:

```bash
python3 scripts/scaffold_feature.py "Your Feature" --with-adr --with-test-plan
```

Then route the brief-driven task, not the vague idea.
