extends Area2D

signal room_cleared

@export var idle_duration := 1.35
@export var telegraph_duration := 0.85
@export var pulse_duration := 0.25
@export var pulse_radius := 90.0
@export var pulse_band_width := 22.0

enum State { IDLE, TELEGRAPH, PULSE, DEFEATED }

var state: State = State.IDLE
var state_timer := 0.0


func _ready() -> void:
    queue_redraw()


func _process(delta: float) -> void:
    if state == State.DEFEATED:
        return

    state_timer += delta
    match state:
        State.IDLE:
            if state_timer >= idle_duration:
                _set_state(State.TELEGRAPH)
        State.TELEGRAPH:
            if state_timer >= telegraph_duration:
                _set_state(State.PULSE)
        State.PULSE:
            if state_timer >= pulse_duration:
                _set_state(State.IDLE)

    queue_redraw()


func _set_state(next_state: State) -> void:
    state = next_state
    state_timer = 0.0


func is_pulsing() -> bool:
    return state == State.PULSE


func is_defeated() -> bool:
    return state == State.DEFEATED


func get_status_label() -> String:
    match state:
        State.IDLE:
            return "idle"
        State.TELEGRAPH:
            return "telegraph"
        State.PULSE:
            return "pulse"
        State.DEFEATED:
            return "cleared"
    return "unknown"


func resolve_player_contact(player_position: Vector2, player_radius: float, player_is_dashing: bool) -> String:
    if not is_pulsing():
        return "none"

    var distance_to_player := global_position.distance_to(player_position)
    var half_band := pulse_band_width * 0.5
    var inner_bound := pulse_radius - half_band - player_radius
    var outer_bound := pulse_radius + half_band + player_radius
    if distance_to_player < inner_bound or distance_to_player > outer_bound:
        return "none"
    return "defeat" if player_is_dashing else "hit"


func defeat() -> void:
    if state == State.DEFEATED:
        return
    state = State.DEFEATED
    state_timer = 0.0
    monitoring = false
    monitorable = false
    emit_signal("room_cleared")
    queue_redraw()


func reset_room() -> void:
    monitoring = true
    monitorable = true
    _set_state(State.IDLE)
    queue_redraw()


func _draw() -> void:
    var core_color := Color("ff7a59")
    if state == State.DEFEATED:
        core_color = Color("7ae582")
    draw_circle(Vector2.ZERO, 26.0, core_color)

    var ring_color := Color("3a5166")
    var ring_width := 4.0
    if state == State.TELEGRAPH:
        ring_color = Color("ffe082")
        ring_width = max(pulse_band_width - 4.0, 8.0)
    elif state == State.PULSE:
        ring_color = Color("ff5c7a")
        ring_width = pulse_band_width
    elif state == State.DEFEATED:
        ring_color = Color("7ae582")
        ring_width = 6.0

    draw_arc(Vector2.ZERO, pulse_radius, 0.0, TAU, 64, ring_color, ring_width, true)
