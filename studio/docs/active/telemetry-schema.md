# Telemetry Schema — Codex Game Studio Pro Max

## Questions to answer
- Do players understand the first playable slice around `First Combat Room`?
- Where do players fail, reset, or abandon the combat room?
- Which upgrade choices are selected and which ones are ignored?

## Event catalog
| Event | Trigger | Key properties | Why it matters |
|---|---|---|---|
| session_start | App enters playable state | platform, build, locale | Session health baseline |
| combat_room_start | Player enters the first room | room_id, difficulty_seed | Funnel entry |
| combat_room_fail | Player loses the room or resets | fail_reason, remaining_health | Readability and balance signal |
| combat_room_clear | Player defeats the encounter | clear_time_s, damage_taken | Core loop validation |
| upgrade_selected | Player chooses a reward | upgrade_id, offered_ids | Build-choice usefulness |

## Privacy & safety
- Avoid personal identifiers and free-form text
- Keep event payloads minimal and slice-focused
- Separate local debug logs from any eventual shipped telemetry backend

## Validation
- Validate event firing in local logs before wiring external telemetry
- Document every schema change in the decision log
- Reject instrumentation that cannot answer a concrete design or quality question
