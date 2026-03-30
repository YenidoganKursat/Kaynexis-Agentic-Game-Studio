# Loop

## Date
- 2026-03-27

## Summary
- Games need an explicit ownership model for frame updates, fixed-step simulation, and match or session state. Across engines, the common mistake is to let state sprawl across too many runtime objects before defining who owns rules, who owns world state, and who owns presentation reactions.
- Godot explicitly separates `_process()` from `_physics_process()` and gives pause/process-mode controls through the scene tree. Unity separates frame callbacks and fixed-step physics callbacks through its event execution model. Unreal pushes teams toward gameplay-framework ownership, where rules, player control, and shared world state are distinct concepts rather than one giant actor or singleton.
- The architectural implication is that every slice should define:
  - where frame-rate dependent presentation updates live
  - where fixed-step physics or combat simulation lives
  - what object owns the current run/match/session state
  - what object or asset acts as the durable source of tuning truth
- Small prototypes can survive with looser structure, but once a game adds menus, pause, retries, save/load, upgrades, or multiplayer-sensitive rules, update order and state ownership become core architecture rather than incidental implementation detail.

## Primary sources
- [Godot idle and physics processing](https://docs.godotengine.org/en/4.0/tutorials/scripting/idle_and_physics_processing.html)
- [Godot pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)
- [Godot key concepts overview](https://docs.godotengine.org/en/4.0/getting_started/introduction/key_concepts_overview.html)
- [Unity event functions](https://docs.unity3d.com/ja/current/Manual/event-functions.html)
- [Unity managing update and execution order](https://docs.unity3d.com/ja/current/Manual/managing-update-order.html)
- [Unity script serialization](https://docs.unity3d.com/kr/6000.0/Manual/script-serialization.html)
- [Unreal Engine terminology](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-terminology)
- [Unreal gameplay systems](https://dev.epicgames.com/documentation/fr-fr/unreal-engine/gameplay-systems-in-unreal-engine)
- [AGameStateBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/AGameStateBase)

## Why this matters to this repo
- Feature briefs should stop at least once to name the runtime state owners. For example:
  - run rules / session rules
  - world state snapshot
  - player-owned mutable state
  - presentation-only widgets or effects
- Agents should avoid recommending broad global singletons for everything. Godot autoloads, Unity single-scene managers, and Unreal globally reachable objects all have valid uses, but they should not become the unexamined default for game rules, combat state, progression, UI, and save data all at once.
- This repo's iterative loop depends on deterministic validation. That only works if the update model is explicit enough that a mechanic can be tested in the right timing domain and paused or reset without hidden side effects.

## Decision impact
- Gameplay and mechanic recommendations should always state:
  - frame/update domain
  - fixed-step or physics domain
  - session or run state owner
  - durable tuning/data owner
- Future feature templates and checklists should treat unclear state ownership as an architectural risk, not just a code-style issue.
- When the slice grows, the active docs should record state-owner decisions in `game-brief.md` or `decision-log.md` instead of letting them remain implicit in code.
