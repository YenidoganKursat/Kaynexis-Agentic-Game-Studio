# Engine Bugs Example

## Example prompt

- "Classify recurring Godot signal and node-path bugs before patching anything."

## Example answer shape

Short answer:

- engine: Godot 4
- bug family: signal wiring / node-path drift
- first check: Debugger panel
- likely boundary: scene ownership or resource ownership

## Debug surfaces by engine

| Engine | Common bug families | First check | Debug surface |
| --- | --- | --- | --- |
| Godot 4 | signal mistakes, node-path drift, resource/scene boundary bugs, export issues | debugger panel, warning system, troubleshooting page | Debugger panel and Output |
| Unity 6 | null references, prefab override drift, execution-order bugs, Addressables assumptions | Console stack trace, script execution order, prefab overrides | Console and Inspector |
| Unreal 5 | UObject lifetime bugs, Blueprint compile issues, Live Coding mismatch, cook/package failures | Output Log, actor lifecycle, GC assumptions | Output Log and Live Coding console |

## Scope

Show how to present the most common bug families for Godot 4, Unity 6, and Unreal 5 without turning the answer into a giant troubleshooting dump.

## Baseline

- The user wants a broad bug or error summary.
- We do not yet have one concrete repro.
- The answer should stay short enough that a newcomer can scan it.

## Decision order

1. Name the engine.
2. Name the bug family.
3. Name the first check surface.
4. Name the likely boundary that owns the fix.
5. Only then decide whether to open a bugfix packet.

## Example bug atlas

| Engine | Common bug families | First check | Debug surface |
| --- | --- | --- | --- |
| Godot 4 | signal mistakes, node-path drift, resource/scene boundary bugs, export issues | debugger panel, warning system, troubleshooting page | Debugger panel and Output |
| Unity 6 | null references, prefab override drift, execution-order bugs, Addressables assumptions | Console stack trace, script execution order, prefab overrides | Console and Inspector |
| Unreal 5 | UObject lifetime bugs, Blueprint compile issues, Live Coding mismatch, cook/package failures | Output Log, actor lifecycle, GC assumptions | Output Log and Live Coding console |

## Good agent prompts

- "Show me the most common bug families for Godot, Unity, and Unreal and tell me the first check for each."
- "Turn this crash into a bug-family map before we patch anything."
- "Explain which debug surface I should inspect first for an engine bug."

## Validation

- The answer stays short.
- The answer names the engine.
- The answer names the likely family and first check.
- The answer keeps bugfix work separate from bug classification work.

## Related docs

- `docs/reference/engine-bugs.md`
- `docs/research/game-development/foundations/engine-bugs.md`
- `studio/checklists/discipline/engine_bugs.toml`
- `studio/docs/active/eval-engine-bugs.md`
- `docs/reference/bugfix` templates in `studio/docs/templates/`
- `docs/reference/agent-guide.md`
