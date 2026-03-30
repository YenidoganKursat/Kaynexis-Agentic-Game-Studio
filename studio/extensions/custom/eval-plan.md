# Extension Pack Eval Plan

## Change under test

- Pack id:
- Pack owner:
- Hook points:
- Override points:

## Goal

- Prove the extension pack attaches only to the named hook points.
- Prove the pack can be disabled cleanly without breaking the canonical core path.

## Scope

- Enabled / disabled behavior
- Manifest parsing
- Fallback path
- One narrow smoke path

## Validation

- Run the extensions checklist
- Run one narrow attach / detach smoke
- Confirm the fallback path still works

## Exit criteria

- Manifest fields are complete
- Hook points are explicit
- Fallback is named
- Core flow remains unchanged when the pack is off

