extends Node2D

const ARENA_RECT := Rect2(Vector2(96.0, 96.0), Vector2(1088.0, 528.0))
const HIT_FLASH_DURATION := 0.35

@onready var player = $Player
@onready var pulse_warden = $PulseWarden
@onready var title_label: Label = $Hud/TitleLabel
@onready var status_label: Label = $Hud/StatusLabel
@onready var objective_label: Label = $Hud/ObjectiveLabel
@onready var choice_label: Label = $Hud/ChoiceLabel
@onready var result_label: Label = $Hud/ResultLabel

var player_health := 3
var pulse_contact_resolved := false
var upgrade_pending := false
var upgrade_taken := ""
var hit_flash_timer := 0.0


func _ready() -> void:
    pulse_warden.room_cleared.connect(_on_room_cleared)
    _refresh_hud()
    queue_redraw()
    print("Kaynexis Agentic Game Studio ready")


func _process(delta: float) -> void:
    if hit_flash_timer > 0.0:
        hit_flash_timer = max(hit_flash_timer - delta, 0.0)
    _refresh_hud()
    queue_redraw()


func _physics_process(_delta: float) -> void:
    if pulse_warden.is_pulsing():
        var distance_to_warden := player.global_position.distance_to(pulse_warden.global_position)
        if distance_to_warden <= pulse_warden.pulse_radius and not pulse_contact_resolved:
            pulse_contact_resolved = true
            if player.is_dashing():
                pulse_warden.defeat()
            else:
                _player_hit()
    else:
        pulse_contact_resolved = false


func _unhandled_input(event: InputEvent) -> void:
    if not upgrade_pending:
        return

    if event is InputEventKey and event.pressed and not event.echo:
        match event.keycode:
            KEY_1:
                _apply_upgrade("speed")
            KEY_2:
                _apply_upgrade("dash")


func _player_hit() -> void:
    player_health -= 1
    hit_flash_timer = HIT_FLASH_DURATION
    player.reset_to_spawn()

    if player_health <= 0:
        player_health = 3
        upgrade_pending = false
        upgrade_taken = ""
        pulse_warden.reset_room()


func _on_room_cleared() -> void:
    upgrade_pending = true


func _apply_upgrade(kind: String) -> void:
    if kind == "speed":
        player.apply_speed_upgrade()
        upgrade_taken = "Stride Module"
    else:
        player.apply_dash_upgrade()
        upgrade_taken = "Phase Module"
    upgrade_pending = false


func _build_objective_text() -> String:
    if pulse_warden.is_defeated() and upgrade_pending:
        return "The Pulse Warden is down. Pick an upgrade with 1 or 2."
    if not upgrade_taken.is_empty():
        return "Upgrade locked in. The slice now proves combat, failure, and reward in one room."
    if player_health < 3:
        return "Taking a pulse resets your position and costs health, so wait for the telegraph."
    return "Move into range, wait for the yellow telegraph, then dash through the red pulse."


func _refresh_hud() -> void:
    title_label.text = "First Combat Room"
    status_label.text = "Move: WASD / arrows | Dash: Space / Enter | Health: %d | Enemy: %s" % [
        player_health,
        pulse_warden.get_status_label(),
    ]
    objective_label.text = _build_objective_text()

    if upgrade_pending:
        choice_label.visible = true
        choice_label.text = "Choose one reward: [1] Stride Module (+move speed)   [2] Phase Module (-dash cooldown)"
    else:
        choice_label.visible = false
        choice_label.text = ""

    if upgrade_taken.is_empty():
        result_label.text = "Goal: read the telegraph, commit to the dash, then claim one upgrade."
    else:
        result_label.text = "Slice clear: %s unlocked. This room is ready to branch into a second enemy or a second wave." % upgrade_taken


func _draw() -> void:
    var floor_color := Color("101722")
    if hit_flash_timer > 0.0:
        floor_color = Color("2b1014")

    draw_rect(ARENA_RECT, floor_color, true)
    draw_rect(ARENA_RECT, Color("41546b"), false, 4.0)

    var divider_x := ARENA_RECT.position.x + 184.0
    draw_line(
        Vector2(divider_x, ARENA_RECT.position.y),
        Vector2(divider_x, ARENA_RECT.position.y + ARENA_RECT.size.y),
        Color("223446"),
        2.0,
    )
