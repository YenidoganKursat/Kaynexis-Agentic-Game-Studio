# Quality Process Example

## Scope

- Unity 6 inventory HUD cleanup with controller remap support and a small optimization pass

## Baseline

| Case | Current pain | Quality target |
| --- | --- | --- |
| Unity HUD | item definitions, runtime slot state, and UI projection are mixed together | separate ownership boundaries and keep the validation path narrow |
| Godot combat slice | scene ownership and resource ownership are blurred | make runtime and data ownership explicit before refactoring |
| Unreal gameplay slice | Actor, component, and data asset responsibilities are unclear | keep runtime, shared data, and editor ownership separate |

## Control loop

| Step | What to answer | Example answer |
| --- | --- | --- |
| Frame | What is the quality problem? | HUD logic mixes slot state with item definitions |
| Owner | Who owns runtime truth? | `MonoBehaviour` owns runtime slots; `ScriptableObject` owns shared item data |
| Proof | What proves the pass worked? | One EditMode test and one manual controller loop |
| Evidence | What artifact will we keep? | Test output plus a short before/after note |
| Gate | What is the go/no-go decision? | Merge only if the ownership split stays readable and the proof path is green |
| Optimize | Is tuning worth it? | Only if the baseline shows a real issue |

## Decision order

- Name the runtime owner, shared data owner, and editor owner first
- Decide which state is runtime truth and which state is projection
- Keep the smallest proof path visible before broadening the change
- If optimization is in scope, capture the baseline before tuning
- Keep the fallback lever explicit if the first lever does not matter

## Engine-shaped examples

### Godot 4
- Keep `Node` / scene ownership separate from `Resource` ownership
- Use `@tool` only when editor behavior must react live
- Avoid hidden runtime state inside data resources

### Unity 6
- Keep `GameObject` / `MonoBehaviour` separate from `ScriptableObject`
- Use prefabs for repeated hierarchies
- Prefer pooling and `NonAlloc` queries before introducing heavier scale systems

### Unreal 5
- Keep `AActor`, `UActorComponent`, `UObject`, and Data Asset ownership distinct
- Keep designer-facing tuning in Blueprint defaults or the Details panel when possible
- Use instancing or larger frameworks only when scale proves the need

## Good agent prompts

- "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate."
- "Refactor a Godot combat room so runtime ownership, data ownership, and editor ownership are explicit."
- "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter."
- "Improve maintainability first, then measure whether optimization is actually needed."

## Validation

- state the ownership model
- name the validation loop
- if optimizing, state baseline, first lever, and fallback lever
- show the before and after evidence or explain why optimization was deferred
