# Quality Example

## Scope

- Unity 6 inventory HUD cleanup with controller remap support and a small optimization pass

## Baseline

| Case | Current pain | Quality target |
| --- | --- | --- |
| Unity HUD | item definitions, runtime slot state, and UI projection are mixed together | separate owner boundaries and keep the validation path narrow |
| Godot combat slice | scene ownership and resource ownership are blurred | make runtime and data ownership explicit before refactoring |
| Unreal gameplay slice | Actor, component, and data asset responsibilities are unclear | keep runtime, shared data, and editor ownership separate |

## Decision order

- Name the runtime owner, shared data owner, and editor owner first
- Decide which state is runtime truth and which state is projection
- Keep the smallest proof path visible before broadening the change
- If optimization is in scope, capture the baseline before tuning
- Keep the fallback lever explicit if the first lever does not matter

## Quality criteria

- short, canonical names
- explicit ownership boundaries
- one narrow validation path
- docs and code updated together
- baseline measured before optimization

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

- "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring."
- "Refactor a Godot combat room so ownership boundaries are explicit and the first optimization lever is measured."
- "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter."
- "Improve maintainability first, then measure whether optimization is actually needed."

## Validation

- state the ownership model
- name the validation loop
- if optimizing, state baseline, first lever, and fallback lever
- show the before and after evidence or explain why optimization was deferred
