# System Atlas

This page is the systems companion to the engine class atlases.

Use it when an agent needs to map a gameplay system to:

- the right runtime owner
- the right shared data owner
- the right editor or tooling surface
- the smallest implementation slice
- the most common failure mode

This is not a theory essay. It is a practical ownership map for the systems this repo keeps reusing.

## Read this with

- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/godot-atlas.md`
- `docs/reference/unity-atlas.md`
- `docs/reference/unreal-atlas.md`
- `docs/research/game-development/systems/README.md`

## Core systems map

| System | Runtime owner | Shared data owner | Editor / tooling owner | Smallest validated slice | Common failure |
| --- | --- | --- | --- | --- | --- |
| Combat | body / actor / component | resource / scriptable object / data asset | inspector, blueprint, editor tools | one hit, one damage number, one feedback event | combat and presentation collapsing into one object |
| Inventory | runtime model + UI projection | item definition asset | inspector, editor tool, debug UI | add one item, show one slot | live state stored in the data definition |
| Dialogue | state model + presentation | dialogue asset / resource | narrative editor, spreadsheet import, tools | one line, one choice, one branch | mixing authored text, runtime state, and UI ownership |
| Quest | quest log / state component | quest definition asset | quest editor / authoring tool | accept one quest, complete one objective | quest state hiding inside UI or dialogue |
| Crafting | crafting service / component | recipe asset | recipe editor / balance sheet | craft one item, spend one resource | recipe logic and inventory logic welded together |
| Save / migration | save projection / serializer | versioned save schema | migration plan, validation tool | save one run, load one run, migrate one version | saving live object graphs instead of projections |
| AI / enemy | actor / body / component | archetype asset | AI tuning panel, behavior editor | one enemy sees, moves, and attacks once | nav, decision, and animation all in one loop |
| UI / HUD | UI node / widget / canvas | projected data model | UI builder, inspector, menu flow test | open one menu, show one state | UI becoming the gameplay authority |
| Presentation / audio / animation | presentation driver / audio source / animation controller | cue table / animation asset | animation editor, audio mixer, timeline | one cue, one animation, one sync event | timing or gameplay truth trapped in presentation callbacks |
| Economy / shop | economy service / model | item price / shop table | balance sheet, economy tuner | buy one item, spend one currency | prices and sinks not validated together |
| Network / multiplayer | authority layer / replicated state | net schema / sync definition | net debug tools, replay validator | one authoritative action, one sync event | client prediction with no contract |
| Accessibility | presentation layer + options model | accessibility config | options screen, accessibility checklist | toggle one setting, see one visible effect | accessibility left as a late polish afterthought |
| Meta progression | meta service / profile state | unlock table / meta asset | progression editor, balance sheet | unlock one meta item | meta and run progression bleeding together |
| Live ops / events | event state / campaign service | event config / schedule | live-ops planner / config tool | start one event, show one player change | event logic hidden in release code |

## Engine jump links by system

Use these when the system is clear but you need the right engine starting point immediately.

| System | Godot first | Unity first | Unreal first | Direct snippet |
| --- | --- | --- | --- | --- |
| Combat | `godot-atlas.md` + `combat.md` | `unity-atlas.md` + `combat.md` | `unreal-atlas.md` + `combat.md` | [Godot](godot-atlas.md#combat-hook) / [Unity](unity-atlas.md#combat-hook) / [Unreal](unreal-atlas.md#combat-hook) |
| Inventory | `godot-atlas.md` + `inventory.md` | `unity-atlas.md` + `inventory.md` | `unreal-atlas.md` + `inventory.md` | [Godot](godot-atlas.md#inventory-model) / [Unity](unity-atlas.md#inventory-model) / [Unreal](unreal-atlas.md#inventory-model) |
| Dialogue | `godot-atlas.md` + `dialogue.md` | `unity-atlas.md` + `dialogue.md` | `unreal-atlas.md` + `dialogue.md` | [Godot](godot-atlas.md#dialogue-entry) / [Unity](unity-atlas.md#dialogue-entry) / [Unreal](unreal-atlas.md#dialogue-entry) |
| Quest | `godot-atlas.md` + `dialogue.md` | `unity-atlas.md` + `dialogue.md` | `unreal-atlas.md` + `dialogue.md` | [Godot](godot-atlas.md#quest-state) / [Unity](unity-atlas.md#quest-state) / [Unreal](unreal-atlas.md#quest-state) |
| Crafting | `godot-atlas.md` + `crafting.md` | `unity-atlas.md` + `crafting.md` | `unreal-atlas.md` + `crafting.md` | [Godot](godot-atlas.md#crafting-flow) / [Unity](unity-atlas.md#crafting-flow) / [Unreal](unreal-atlas.md#crafting-flow) |
| Save / migration | `godot-atlas.md` + `save.md` | `unity-atlas.md` + `save.md` | `unreal-atlas.md` + `save.md` | [Godot](godot-atlas.md#save-projection) / [Unity](unity-atlas.md#save-projection) / [Unreal](unreal-atlas.md#save-projection) |
| AI / enemy | `godot-atlas.md` + `enemy.md` | `unity-atlas.md` + `enemy.md` | `unreal-atlas.md` + `enemy.md` | [Godot](godot-atlas.md#enemy-chase) / [Unity](unity-atlas.md#enemy-chase) / [Unreal](unreal-atlas.md#enemy-chase) |
| UI / HUD | `godot-atlas.md` + `ui.md` | `unity-atlas.md` + `ui.md` | `unreal-atlas.md` + `ui.md` | [Godot](godot-atlas.md#ui-flow) / [Unity](unity-atlas.md#ui-flow) / [Unreal](unreal-atlas.md#ui-flow) |
| Presentation / audio / animation | `audio-animation-guide.md` + `godot-presentation.md` | `audio-animation-guide.md` + `unity-presentation.md` | `audio-animation-guide.md` + `unreal-presentation.md` | [Godot](audio-animation-guide.md#godot-4) / [Unity](audio-animation-guide.md#unity-6) / [Unreal](audio-animation-guide.md#unreal-5) |
| Economy / shop | `godot-atlas.md` + `economy-balance` | `unity-atlas.md` + `economy-balance` | `unreal-atlas.md` + `economy-balance` | [Godot](godot-atlas.md#economy--shop-projection) / [Unity](unity-atlas.md#economy--shop-projection) / [Unreal](unreal-atlas.md#economy--shop-projection) |
| Network / multiplayer | `godot-atlas.md` + `multiplayer-slice` | `unity-atlas.md` + `multiplayer-slice` | `unreal-atlas.md` + `multiplayer-slice` | [Godot](godot-atlas.md#network-state) / [Unity](unity-atlas.md#network-state) / [Unreal](unreal-atlas.md#network-state) |
| Accessibility | `godot-atlas.md` + `accessibility-audit` | `unity-atlas.md` + `accessibility-audit` | `unreal-atlas.md` + `accessibility-audit` | [Godot](godot-atlas.md#accessibility-options) / [Unity](unity-atlas.md#accessibility-options) / [Unreal](unreal-atlas.md#accessibility-options) |
| Meta progression | `godot-atlas.md` + `metaprogression-loop` | `unity-atlas.md` + `metaprogression-loop` | `unreal-atlas.md` + `metaprogression-loop` | [Godot](godot-atlas.md#meta-progression-service) / [Unity](unity-atlas.md#meta-progression-service) / [Unreal](unreal-atlas.md#meta-progression-service) |
| Live ops / events | `godot-atlas.md` + `liveops-calendar` | `unity-atlas.md` + `liveops-calendar` | `unreal-atlas.md` + `liveops-calendar` | [Godot](godot-atlas.md#live-ops--event-flow) / [Unity](unity-atlas.md#live-ops-event-flow) / [Unreal](unreal-atlas.md#live-ops-event-flow) |

## System-by-system notes

### Combat

- Inputs: movement, target selection, hit detection, timing windows
- Outputs: damage, recoil, effects, audio, screen feedback
- Watch out: the collider or animation graph should not become the full combat authority
- Study first: `combat.md`, the engine class atlases, and the engine combat snippets

### Inventory

- Inputs: pickup, drop, equip, stack changes, slot changes
- Outputs: UI projection, save projection, loadout state
- Watch out: runtime stacks should not live in the item definition asset
- Study first: `inventory.md`

### Dialogue

- Inputs: speaker, line, branch choice, condition flags
- Outputs: conversation state, quest triggers, lorebook unlocks
- Watch out: text authoring, branch state, and UI display should remain separate
- Study first: `dialogue.md`, lorebook methodology

### Quest

- Inputs: objectives, triggers, state changes, fail states
- Outputs: progression, rewards, unlocks, world mutations
- Watch out: quests should not be hidden inside dialogue only
- Study first: `dialogue.md`, `quest-flow` skill

### Crafting

- Inputs: recipe, inventory, costs, station availability
- Outputs: crafted item, resource spend, UI confirmation
- Watch out: craft eligibility should be explicit and testable
- Study first: `crafting.md`

### Save / migration

- Inputs: runtime snapshot, version, migration path
- Outputs: save blob, profile state, checkpoint restore
- Watch out: never serialize the live scene graph unless the engine truly supports the exact contract
- Study first: `save.md`, `save-system` skill

### AI / enemy

- Inputs: perception, path intent, arena conditions, archetype tuning
- Outputs: patrol, chase, attack, retreat, phase shift
- Watch out: sensing, navigation, and decision making need separate ownership
- Study first: `enemy.md`, `navigation.md`

### UI / HUD

- Inputs: projected game state, input focus, accessibility settings
- Outputs: menus, overlays, prompts, settings, inventory views
- Watch out: UI should not mutate authority directly unless the flow explicitly requires it
- Study first: `ui-guide.md`, `ui.md`, engine UI snippets

### Presentation / audio / animation

- Inputs: cue timing, state changes, motion triggers, UI confirmation, mix priority
- Outputs: sound feedback, motion feedback, telegraphs, confirmations, presentation state
- Watch out: the animation graph or audio graph should not become the full gameplay authority
- Study first: `audio-animation-guide.md`, the engine presentation notes, and the matching visuals playbook when the work is image-heavy

### Economy / shop

- Inputs: currency, pricing, unlock state, item table
- Outputs: purchase, sink, upgrade, availability gating
- Watch out: prices and sinks need balance review, not just implementation
- Study first: `economy-balance` skill, `balance-simulator.md`

### Network / multiplayer

- Inputs: authoritative action, local prediction, replicated state
- Outputs: sync events, state updates, rollback or reconciliation
- Watch out: networking without an explicit authority model becomes expensive confusion
- Study first: `multiplayer-slice` skill, backend foundation notes if needed

### Accessibility

- Inputs: player preference, platform guideline, readability budget
- Outputs: text scale, contrast, remap, subtitle, timing adjustment
- Watch out: accessibility cannot be a post-hoc menu checkbox only
- Study first: `ux.md`, `accessibility-audit` skill

### Meta progression

- Inputs: run results, unlock currency, meta achievements
- Outputs: permanent unlocks, profile progression, long-term goals
- Watch out: meta progression should not flatten the run loop
- Study first: `metaprogression-loop` skill, progression research notes

### Live ops / events

- Inputs: event config, schedule, reward table
- Outputs: active event state, altered gameplay windows, promotions
- Watch out: event flow needs rollback and staging discipline
- Study first: `liveops-calendar` skill, production notes

## Example ownership statements

When writing a feature brief or implementation plan, say things like:

- "Combat is owned by the actor/component/body layer, while the collider only detects contact."
- "Inventory state lives in a runtime model; item data lives in the definition asset."
- "Dialogue text is authored data; conversation state is runtime projection."
- "Save data is a projection of runtime state, not the live scene itself."
- "UI reads projected state and never owns combat authority."

## Related docs

- `docs/research/game-development/systems/README.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/godot-atlas.md`
- `docs/reference/unity-atlas.md`
- `docs/reference/unreal-atlas.md`
- the matching research notes in `docs/research/game-development/systems/`
