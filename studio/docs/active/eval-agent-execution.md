# Eval Plan - Agent Execution Packet

## Change under test

- Add an execution-packet guide and example for agent tasks that need a reusable pre-flight contract.

## Goal

- Keep single-specialist mode visible while making the owner, mode, goal, proof path, custom rules, and stop conditions easy to write once and reuse.
- Keep the packet, prompt journal, transcript, and validation matrix separate but linked.

## Checkpoints

1. `route_task.py` should route work-packet requests to the new agent-execution surface.
2. `codex_studio.py packet` should create a dry-run or appendable execution packet entry.
3. `codex_studio.py` interactive menu should expose the packet lane as a quick-access option.
4. `codex_studio.py checklist` should surface the execution-packet checklist items.
5. `validate_docs.py` should keep the guide, example, research note, template, and active log in sync.
6. `tests/test_studio_system.py` should lock the route, packet, menu, and checklist behavior.
7. `AGENTS.md` should name the execution-packet lane in the routing heuristic so the operating model stays visible.

## Success criteria

- The packet guide stays short enough to skim in one pass.
- Single specialist mode remains visible and available.
- Custom rules or project overrides are explicit in the packet shape.
- The shared routing policy, CLI helper, interactive menu, and docs all point at the same execution-packet lane.

## Watch items

- Do not let the packet become a replacement for prompt history, transcript, or validation matrices.
- Do not let the packet hide the proof path or the stop conditions.
- Do not let custom rules drift into chat-only notes.
