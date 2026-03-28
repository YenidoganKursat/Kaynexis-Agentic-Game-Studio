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

Inventory and equipment:

```bash
python3 scripts/codex_studio.py next \
  "Design inventory, equipment, and persistence boundaries for a roguelite loadout system"
```

Character architecture:

```bash
python3 scripts/codex_studio.py next \
  "Define the player character locomotion, ability, and animation ownership model for Unreal"
```

Enemy architecture:

```bash
python3 scripts/codex_studio.py next \
  "Design enemy patrol, aggro, and encounter roles for the first biome"
```

Controls and remapping:

```bash
python3 scripts/codex_studio.py next \
  "Design controller remapping, pause flow, and keyboard/gamepad parity for the settings menu"
```

UI and HUD:

```bash
python3 scripts/codex_studio.py next \
  "Design a compact upgrade screen and HUD state flow for controller-first navigation"
```

Skills and upgrades:

```bash
python3 scripts/codex_studio.py next \
  "Separate authored skill definitions, current-run upgrades, and durable meta unlocks"
```

Interactions and pickups:

```bash
python3 scripts/codex_studio.py next \
  "Design pickup prompts, interaction validation, and loot persistence for reward chests"
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
- "Define keyboard, gamepad, and UI focus rules before adding remapping."

Save systems:

- "Define what should persist after a failed run versus what resets."
- "Plan a migration-safe save structure for progression unlocks."
- "Separate item definitions, runtime inventory state, and persistent equipment state."

Character architecture:

- "Decide what owns dash validation, locomotion, animation transitions, and stamina costs."
- "Define how player state, equipment state, and temporary combat state stay separate."

Enemy architecture:

- "Define enemy archetype data versus runtime behavior state before adding a second faction."
- "Plan patrol, aggro, and encounter-role boundaries before scaling enemy count."

Controls and UI architecture:

- "Decide which action map powers gameplay, which powers menus, and where rebinding is saved."
- "Define what the camera reacts to and what it must never silently control."

Skills and upgrades:

- "Separate authored skill definitions, current-run upgrades, and durable profile unlocks."
- "Decide which system owns cooldown state, stack rules, and upgrade UI projection."

Interactions:

- "Define how pickup prompts, interaction checks, and loot grants stay separate."
- "Choose whether prompts are proximity-only, facing-based, or target-selection based before adding content scale."

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
