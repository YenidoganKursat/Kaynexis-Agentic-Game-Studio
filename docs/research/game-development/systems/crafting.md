# Crafting

## Date
- 2026-03-28

## Summary
- Crafting systems fail first when authored recipe data, runtime inventory state, and world resource logic all mutate each other directly. The stable shape is: authored item and recipe definitions stay data-only, runtime crafting jobs resolve against a deterministic inventory/resource snapshot, and world interactables just grant or consume resources through contracts.
- The earliest architecture choice is whether crafting is a player-local interaction, a base-building production chain, or a multiplayer/shared authority system. The UI can look similar in all three cases, but the ownership model is completely different.
- Recipe systems scale better when ingredients, outputs, station requirements, unlock conditions, and tags are authored as explicit data rather than spread across UI code, actor scripts, or quest logic.
- Resource-flow debugging matters earlier than most teams expect. Once players gather, refine, split, stack, or auto-route resources, the game needs one clear source of truth for why a recipe is craftable, blocked, or partially fulfilled.

## Primary sources
- [Minecraft official site](https://www.minecraft.net/)
- [Valheim official site](https://www.valheimgame.com/)
- [Factorio official site](https://www.factorio.com/)

## Why this matters to this repo
- Crafting tasks should not be routed as "just UI" or "just inventory." The real architecture spans authored data, runtime inventory rules, station/world interactions, save persistence, and feedback surfaces.
- Engine-specific work should answer the same questions before implementation:
  - what authored asset owns item and recipe definitions
  - what runtime object validates craftability
  - what inventory or stash authority spends inputs and grants outputs
  - what UI layer explains missing ingredients, station requirements, and queue state
- This repo should push agents to separate recipe definition, crafting validation, inventory mutation, and world feedback from the first slice.

## Decision impact
- Feature briefs that mention crafting, recipes, gathering, or stations should include explicit ownership for:
  - item data
  - recipe data
  - inventory mutation
  - station validation
  - save persistence
- Checklists and route output should surface this note for tasks mentioning craft, recipe, workbench, forge, gather, harvest, refine, or production chain.
- Example first slices should prefer one small crafting loop with clear blocked states over a broad recipe list.

## Architecture guidance

### Separate authored data from runtime state
- Authored data should answer:
  - what this item is
  - what tags it has
  - whether it stacks
  - which recipes can create it
  - which stations or unlocks are required
- Runtime state should answer:
  - how many items the player or colony currently has
  - which crafting jobs are queued or in progress
  - whether a recipe is currently valid
  - which resources are reserved for another job

### Treat craftability as a query, not a side effect
- The craft screen should be able to ask "Can I craft this right now?" without spending resources.
- A separate commit step should spend inputs, grant outputs, and emit feedback.
- This avoids common bugs where UI hover or list refresh accidentally mutates inventory or quest progress.

### Use one inventory mutation contract
- Every craft should eventually resolve through the same rules used by pickup, loot, stash, and save/load.
- Avoid special-case recipe code that bypasses stack limits, durability rules, ownership checks, or persistence boundaries.

### Keep station/world interactions thin
- Workbenches, campfires, anvils, and factories should mostly provide context:
  - station type
  - placement state
  - power or fuel requirement
  - nearby inventory or network scope
- They should not become the hidden owner of all recipe logic.

### Design for blocked-state readability
- A good crafting architecture can answer:
  - missing ingredient
  - missing station
  - wrong unlock state
  - full inventory / no output space
  - resource reserved elsewhere
- If the player cannot tell why crafting failed, the architecture is already too coupled.

## What to watch out for
- Unlock logic embedded in UI widgets instead of shared validation code
- Recipe data duplicated across quest scripts, tutorial scripts, and crafting UI
- World stations directly editing save data or quest state
- Split authority between local inventory and world stash without reservation rules
- Crafting queues that do not serialize cleanly into save files
