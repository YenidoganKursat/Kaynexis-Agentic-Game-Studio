# Telemetry Schema — Kaynexis Agentic Game Studio

## Questions to answer
- Do players understand the first playable slice around `First Combat Room`?
- Where do players fail, reset, or abandon the combat room?
- Which upgrade choices are selected and which ones are ignored?
- Are players using dash as the intended mastery verb or only as panic recovery?

## Event catalog
| Event | Trigger | Key properties | Why it matters |
|---|---|---|---|
| session_start | App enters playable state | platform, build, locale | Session health baseline |
| combat_room_start | Player enters or restarts the first room | room_id, difficulty_seed, restart_reason | Funnel entry and retry context |
| dash_used | Player commits to the signature evade verb | room_id, remaining_health, elapsed_time_s | Whether the core verb is actually being used |
| combat_room_fail | Player loses the room or resets | fail_reason, remaining_health | Readability and balance signal |
| combat_room_clear | Player defeats the encounter | clear_time_s, damage_taken | Core loop validation |
| upgrade_selected | Player chooses a reward | upgrade_id, offered_ids | Build-choice usefulness |

## Current local sink
- Godot reference slice writes newline-delimited local events to `user://telemetry_events.jsonl`
- Current implementation lives in `src/telemetry.gd` and is wired from `src/main.gd`
- This is for local validation and balancing only, not for shipping analytics yet

## Privacy & safety
- Avoid personal identifiers and free-form text
- Keep event payloads minimal and slice-focused
- Separate local debug logs from any eventual shipped telemetry backend

## Validation
- Validate event firing in local logs before wiring external telemetry
- Document every schema change in the decision log
- Reject instrumentation that cannot answer a concrete design or quality question
- For the current slice, verify at least one `dash_used`, one `combat_room_fail`, one `combat_room_clear`, and one `upgrade_selected` record in local logs
