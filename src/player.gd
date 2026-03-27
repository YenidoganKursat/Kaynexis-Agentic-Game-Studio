extends CharacterBody2D

@export var move_speed := 240.0
@export var dash_speed := 680.0
@export var dash_duration := 0.18
@export var dash_cooldown := 0.85
@export var collision_radius := 18.0

var dash_timer := 0.0
var dash_cooldown_timer := 0.0
var facing := Vector2.RIGHT
var spawn_position := Vector2.ZERO
var arena_bounds := Rect2()


func _ready() -> void:
    spawn_position = global_position
    queue_redraw()


func _physics_process(delta: float) -> void:
    var input_vector := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    if input_vector.length() > 0.0:
        facing = input_vector.normalized()

    if dash_cooldown_timer > 0.0:
        dash_cooldown_timer = max(dash_cooldown_timer - delta, 0.0)

    if dash_timer > 0.0:
        dash_timer = max(dash_timer - delta, 0.0)
        velocity = facing * dash_speed
    else:
        if Input.is_action_just_pressed("ui_accept") and dash_cooldown_timer <= 0.0:
            dash_timer = dash_duration
            dash_cooldown_timer = dash_cooldown
            velocity = facing * dash_speed
        else:
            velocity = input_vector * move_speed

    move_and_slide()
    if arena_bounds.size != Vector2.ZERO:
        global_position = global_position.clamp(
            arena_bounds.position + Vector2.ONE * collision_radius,
            arena_bounds.position + arena_bounds.size - Vector2.ONE * collision_radius,
        )
    queue_redraw()


func is_dashing() -> bool:
    return dash_timer > 0.0


func get_collision_radius() -> float:
    return collision_radius


func set_arena_bounds(bounds: Rect2) -> void:
    arena_bounds = bounds


func reset_to_spawn() -> void:
    global_position = spawn_position
    velocity = Vector2.ZERO
    dash_timer = 0.0
    queue_redraw()


func apply_speed_upgrade() -> void:
    move_speed += 40.0


func apply_dash_upgrade() -> void:
    dash_cooldown = max(0.35, dash_cooldown - 0.2)


func _draw() -> void:
    var body_color := Color("64d2ff")
    if is_dashing():
        body_color = Color("f7ff7a")

    draw_circle(Vector2.ZERO, collision_radius, body_color)
    draw_circle(facing * 10.0, 5.0, Color("0d1117"))
