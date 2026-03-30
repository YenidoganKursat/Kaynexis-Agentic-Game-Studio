# Godot Atlas

This page is the deeper Godot companion to `engine-map.md` and `engine-atlas.md`.

Use it when an agent needs to make a Godot-specific ownership decision and wants the practical shape of the main classes, objects, and editor surfaces.

This is not every Godot class. It is the set of core class families you should reach for first in gameplay, UI, tools, persistence, and visuals.

## Read this with

- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/research/game-development/engines/godot-map.md`
- `docs/research/game-development/engines/godot-classes.md`
- `docs/research/game-development/engines/godot-systems.md`

## Core ownership model

| Family | Runtime owner | Shared data owner | Editor owner | Example use |
| --- | --- | --- | --- | --- |
| Scene tree | `Node` | `Resource` | Inspector / `@tool` / plugins | orchestration, scene composition |
| 2D body | `CharacterBody2D` | `Resource` | Inspector | player movement, enemy movement |
| 3D body | `CharacterBody3D` | `Resource` | Inspector | 3D locomotion, AI movement |
| Overlap volume | `Area2D` / `Area3D` | `Resource` | Inspector | pickups, damage zones, triggers |
| UI | `Control` / `CanvasLayer` | `Resource` | Control scene editor | HUD, menus, overlays |
| Presentation | `AnimationPlayer` / `AnimationTree` | `Resource` | Inspector | windups, reactions, state blends |
| Reuse blueprint | `PackedScene` | `Resource` | Scene editor | repeated enemies, props, projectiles |

## Core classes and what they are for

### `Node`

- What it is: the base tree object that owns lifecycle and child orchestration
- Good for: spawning child nodes, listening to signals, delegating work
- Not good for: storing all game state, doing heavy per-frame logic, becoming a global manager dump
- Input: tree enter/exit, child events, signals
- Output: orchestration, setup, cleanup, routing
- Example use: a combat room root node that spawns the player, enemy, HUD, and upgrade panel

### `Node2D` and `Node3D`

- What they are: transform-bearing scene roots for 2D and 3D content
- Good for: positioning, grouping, parent-relative motion
- Not good for: hiding major gameplay logic or shared data
- Input: transform updates, child attachment
- Output: spatial hierarchy and scene organization
- Example use: a 2D room root, a 3D encounter root, a visual grouping node

### `CharacterBody2D` and `CharacterBody3D`

- What they are: authored movement bodies for controllable characters
- Good for: player movement, enemy movement, floor interaction, knockback
- Not good for: camera ownership, UI ownership, save ownership, item database ownership
- Input: player input, AI intent, gravity, movement tuning
- Output: motion, floor state, collision-aware movement
- Example use: player dash movement, enemy chase movement, boss repositioning

### `Area2D` and `Area3D`

- What they are: detection and overlap surfaces
- Good for: pickups, damage zones, aggro ranges, interaction prompts
- Not good for: owning the whole mechanic or storing permanent inventory state
- Input: trigger overlaps, bodies entering/leaving, queries
- Output: events or handoff signals to gameplay systems
- Example use: pickup ring, hitbox, enemy sensing radius, checkpoint zone

### `Resource`

- What it is: shared authored data
- Good for: items, upgrades, tuning tables, encounter definitions, dialogue data
- Not good for: per-run mutable state, scene-specific transient values
- Input: inspector editing, import data
- Output: reusable tuning or definition data
- Example use: damage card, item stat block, enemy archetype data

### `PackedScene`

- What it is: reusable scene blueprint
- Good for: enemies, bullets, props, UI fragments
- Not good for: being the runtime state store
- Input: authored scene tree
- Output: instanced scene copies
- Example use: spawn a repeated enemy or projectile from a scene asset

### `Control` and `CanvasLayer`

- What they are: UI layout and screen-space stacking
- Good for: HUD, menus, upgrade panels, tool panels
- Not good for: storing gameplay authority
- Input: projected game state, focus, user interaction
- Output: visible UI, commands, selection events
- Example use: an upgrade screen that only reads the runtime selection model

### `AnimationPlayer`, `AnimationTree`, `AnimatedSprite2D`

- What they are: presentation and timing tools
- Good for: windups, hit reactions, death states, blend trees, sprite playback
- Not good for: hiding gameplay rules in animation callbacks
- Input: state transitions, timeline cues, parameters
- Output: motion, blend, timing feedback
- Example use: attack windup, dash trail, hurt flash, enemy spawn animation

### `Camera2D` and `Camera3D`

- What they are: view framing objects
- Good for: follow logic, shake, cutscenes, camera bounds
- Not good for: input authority, damage authority, save state
- Input: player position, cutscene events, screen shake requests
- Output: composition and framing
- Example use: a combat room follow camera with explicit arena bounds

### `NavigationAgent2D` and `NavigationAgent3D`

- What they are: path intent helpers
- Good for: enemy chase logic, path progress, steering hints
- Not good for: owning the whole AI decision tree by itself
- Input: target position, navigation mesh/space
- Output: path hints and steering results
- Example use: enemy chase behavior around arena obstacles

### `RayCast2D`, `RayCast3D`, and query APIs

- What they are: direct sensing tools
- Good for: line-of-sight, interaction checks, targeting, cheap hit checks
- Not good for: running expensive repeated checks without gating
- Input: origin, direction, mask
- Output: hit result or no hit
- Example use: interact prompt, firing line, sight check

### `MultiMesh`

- What it is: batched repeated rendering support
- Good for: large repeated visual counts
- Not good for: bespoke unique actors
- Input: repeated transform data
- Output: high-count rendering efficiency
- Example use: many bullets, debris, repeated props, crowd-like visuals

## GPU and render-scale family

| Family | Runtime / render owner | Shared data owner | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| Render server | `RenderingServer` | `Resource` | render-side batching and ownership | do not use it when the scene tree is not the real bottleneck |
| GPU device | `RenderingDevice` | `Resource` or packed buffer data | compute, buffer-driven work, lower-level GPU control | do not hide gameplay authority inside a render helper |
| Repeated visuals | `MultiMesh` / `MultiMeshInstance3D` | `Resource` | instanced repeated visuals | do not confuse visual batching with simulation ownership |
| Material / shader | `ShaderMaterial` | `Resource` | material-level GPU behavior | do not make shaders own gameplay truth |

## Common Godot mechanic patterns

| Mechanic | Likely owner | Example class pair | Common mistake |
| --- | --- | --- | --- |
| Movement | body node | `CharacterBody2D` + `Camera2D` | mixing camera logic into the body |
| Pickup | detection + data | `Area2D` + `Resource` | storing item database state in the pickup node |
| HUD | UI node | `Control` + `CanvasLayer` | letting HUD own gameplay rules |
| Upgrade choice | scene + data | `PackedScene` + `Resource` | hardcoding every upgrade in the node tree |
| Enemy AI | scene + nav helper | `Node` + `NavigationAgent2D` | putting decision logic into the navigation helper |
| VFX | animation + reuse | `AnimationPlayer` + `PackedScene` | encoding gameplay logic in particles/animation |

## Typical input/output contracts

- `Node` inputs lifecycle and signals, outputs orchestration
- `CharacterBody2D/3D` inputs movement intent, outputs motion
- `Area2D/3D` inputs overlap events, outputs gameplay triggers
- `Resource` inputs authored values, outputs reusable tuning
- `Control` inputs projected data and UI events, outputs screen state and commands

## Best first examples

- `Node2D` + `CharacterBody2D` for readable movement
- `Area2D` + `Resource` for pickups and damage
- `Control` + `CanvasLayer` for HUD
- `AnimationPlayer` for attack telegraphs
- `PackedScene` for reusable enemies or projectiles

## Example snippets

### Movement and contact

```gdscript
extends CharacterBody2D

@export var speed := 220.0
@export var dash_speed := 420.0

func _physics_process(delta):
    var input_dir = Input.get_vector("move_left", "move_right", "move_up", "move_down")
    velocity = input_dir * speed
    move_and_slide()
```

### Pickup detection

```gdscript
extends Area2D

@export var item_id: String

func _on_body_entered(body):
    if body.has_method("add_item"):
        body.add_item(item_id)
        queue_free()
```

### HUD projection

```gdscript
extends Control

@onready var hp_label := %HpLabel

func set_hp(current_hp: int, max_hp: int) -> void:
    hp_label.text = "%d / %d" % [current_hp, max_hp]
```

## Additional snippets

### Inventory model

```gdscript
extends Node

var items: Array[String] = []

func add_item(item_id: String) -> void:
    items.append(item_id)
```

### Enemy chase

```gdscript
extends CharacterBody2D

@onready var nav := $NavigationAgent2D
@export var speed := 150.0

func _physics_process(_delta):
    var next_pos = nav.get_next_path_position()
    velocity = (next_pos - global_position).normalized() * speed
    move_and_slide()
```

### Camera follow

```gdscript
extends Camera2D

@export var target_path: NodePath

func _process(_delta):
    var target = get_node_or_null(target_path)
    if target:
        global_position = global_position.lerp(target.global_position, 0.15)
```

### Save projection

```gdscript
extends Node

func save_run(data: Dictionary) -> void:
    var file := FileAccess.open("user://save.json", FileAccess.WRITE)
    file.store_string(JSON.stringify(data))
```

### Skill tree choice

```gdscript
extends Resource
class_name SkillNodeData

@export var id: String
@export var label: String
@export var cost: int = 1
```

### UI flow

```gdscript
extends Control

func show_upgrade_panel() -> void:
    visible = true
    grab_focus()
```

### Animation trigger

```gdscript
extends AnimationPlayer

func play_attack() -> void:
    play("attack")
```

### Pathfinding intent

```gdscript
extends NavigationAgent2D

func set_target(target: Vector2) -> void:
    target_position = target
```

### Combat hook

```gdscript
extends Area2D

@export var damage := 10

func _on_body_entered(body):
    if body.has_method("apply_damage"):
        body.apply_damage(damage)
```

### Loot projection

```gdscript
extends Resource
class_name ItemData

@export var id: String
@export var title: String
@export var rarity: String
```

### Dialogue entry

```gdscript
extends Resource
class_name DialogueLine

@export var speaker: String
@export var text: String
```

### Quest state

```gdscript
extends Node

var active_quests: Array[String] = []

func add_quest(quest_id: String) -> void:
    if quest_id not in active_quests:
        active_quests.append(quest_id)
```

### Crafting flow

```gdscript
extends Node

func can_craft(recipe: Dictionary) -> bool:
    return true
```

### Input remap

```gdscript
extends Control

func set_rebind(action_name: String, event: InputEvent) -> void:
    InputMap.action_erase_events(action_name)
    InputMap.action_add_event(action_name, event)
```

### UI menu flow

```gdscript
extends Control

func show_menu() -> void:
    visible = true
    grab_focus()
```

### Status effects

```gdscript
extends Node

var status_effects: Array[String] = []

func add_status(effect_id: String) -> void:
    status_effects.append(effect_id)
```

### Inventory UI

```gdscript
extends Control

func render_inventory(items: Array[String]) -> void:
    $Label.text = ", ".join(items)
```

### Boss phase state

```gdscript
extends Node

var phase := 1

func set_phase(next_phase: int) -> void:
    phase = next_phase
```

### Camera shake

```gdscript
extends Camera2D

func shake(amount: float) -> void:
    offset = Vector2(randf_range(-amount, amount), randf_range(-amount, amount))
```

### Interaction prompt

```gdscript
extends Control

func show_prompt(text: String) -> void:
    visible = true
    $Label.text = text
```

### Tutorial gating

```gdscript
extends Node

var tutorial_flags: Dictionary = {}

func unlock(flag: String) -> void:
    tutorial_flags[flag] = true
```

### Network state

```gdscript
extends Node

var is_authority := false

func apply_network_state(data: Dictionary) -> void:
    is_authority = data.get("authority", false)
```

### Save migration edge case

```gdscript
extends Node

func migrate_save(data: Dictionary) -> Dictionary:
    if not data.has("version"):
        data["version"] = 1
    return data
```

### Accessibility hook

```gdscript
extends Control

func set_large_text(enabled: bool) -> void:
    $Label.add_theme_font_size_override("font_size", 24 if enabled else 16)
```

### Economy / shop

```gdscript
extends Node

var coins := 0

func can_buy(price: int) -> bool:
    return coins >= price
```

### Meta progression

```gdscript
extends Node

var unlocks: Dictionary = {}

func unlock_meta(id: String) -> void:
    unlocks[id] = true
```

### Live ops / event flow

```gdscript
extends Node

var active_event := ""

func start_event(event_id: String) -> void:
    active_event = event_id
```

### Accessibility options

```gdscript
extends Node

var large_text := false
var subtitles := true

func set_accessibility(large_text_enabled: bool, subtitles_enabled: bool) -> void:
    large_text = large_text_enabled
    subtitles = subtitles_enabled
```

### Economy / shop projection

```gdscript
extends Node

var coins := 0

func can_buy(price: int) -> bool:
    return coins >= price
```

### Meta progression service

```gdscript
extends Node

var meta_unlocks: Dictionary = {}

func unlock_meta(id: String) -> void:
    meta_unlocks[id] = true
```

### Live ops event flag

```gdscript
extends Node

var live_event_id := ""

func set_live_event(event_id: String) -> void:
    live_event_id = event_id
```

## Common mistakes

- making `Node` the place where all systems live
- putting per-run mutable state inside `Resource`
- letting `Control` own combat authority
- using `Area2D` as a full gameplay system instead of a detector
- using `AnimationTree` to hide gameplay logic that should be explicit

## Engine-specific deep dive

### Core runtime

- `Node` / `Node2D` / `Node3D` own structure and orchestration first
- `CharacterBody2D` / `CharacterBody3D` own movement, floor interaction, and knockback
- `SceneTree` should remain a coordination layer, not a shared-state junk drawer

### Editor and tooling

- `@tool` is for live editor feedback that materially improves authoring
- editor plugins and inspector plugins should expose one job clearly, not a kitchen-sink dock
- when the task is validation or content audit, keep the editor surface separate from runtime nodes

### Data and persistence

- `Resource` is the shared tuning layer for items, upgrades, enemy archetypes, and dialogue data
- `PackedScene` is the reuse blueprint for repeated content, not the place to store transient per-run logic
- runtime save projection should live outside reusable assets and should be explicit in the implementation

### Gameplay and interaction

- `Area2D` / `Area3D` should detect and hand off; they do not own the damage or pickup system
- `NavigationAgent2D` / `NavigationAgent3D` should provide path intent, not the full AI policy
- `RayCast2D` / `RayCast3D` should be query helpers, not repeated heavy loops

### UI

- `Control` owns screen-space interaction and `CanvasLayer` owns overlay stacking
- HUD should only read projected state and should not mutate combat or inventory authority directly
- menu transitions should stay explicit so the UI does not become an invisible state machine

### Visuals and animation

- `AnimationPlayer` handles explicit timed events and attack telegraphs
- `AnimationTree` handles blends and locomotion state, not hidden combat rules
- `AnimatedSprite2D` and `Sprite2D` stay presentation-only
- `MultiMesh` is the first thought when repeated visuals become the bottleneck

## What the agent should say

Before implementation, state:

1. which node owns runtime state
2. which resource owns shared tuning
3. which scene owns reuse
4. which UI node owns presentation
5. which class is only a detector
6. what fails first when the scene scales

## Related docs

- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/agent-guide.md`
- `docs/reference/engine-examples.md`
- the matching engine research notes in `docs/research/game-development/engines/`
