extends RefCounted

const TELEMETRY_LOG_PATH := "user://telemetry_events.jsonl"

var session_id := ""


func _init() -> void:
    session_id = "%s-%s" % [OS.get_name().to_lower(), Time.get_unix_time_from_system()]


func log_event(event_name: String, properties: Dictionary = {}) -> void:
    var payload := {
        "session_id": session_id,
        "event": event_name,
        "ts_unix": Time.get_unix_time_from_system(),
        "properties": properties,
    }

    var file := FileAccess.open(TELEMETRY_LOG_PATH, FileAccess.READ_WRITE)
    if file == null:
        file = FileAccess.open(TELEMETRY_LOG_PATH, FileAccess.WRITE_READ)
    if file != null:
        file.seek_end()
        file.store_line(JSON.stringify(payload))
        file.close()

    print("[telemetry] %s" % JSON.stringify(payload))
