# Eval Plan - Engine Bugs

## Change under test

Add a source-backed engine bug atlas that groups common Godot, Unity, and Unreal bug families and gives agents the first check for each.

## Goal

The bug atlas should help an agent classify a bug or error before it tries to patch anything.

## Risks

- The note might become a catch-all troubleshooting dump if the families are too broad.
- The router might confuse general bugfix work with engine-family bug classification.
- The catalog might drift from the engine troubleshooting docs if the indexes are not kept in sync.

## Validation

- The guide should stay short enough to scan.
- The research note should name the common bug families per engine.
- The example should show the answer shape and first-check table.
- The router should surface the lane for engine-specific bug or troubleshooting requests.
- The checklist should keep bug classification separate from bugfix repro work.

## Success criteria

- A user asking for common engine bugs gets the engine-bugs lane first.
- An agent can name the first debug surface for Godot, Unity, and Unreal.
- The guide, example, research note, checklist, eval plan, and indexes stay synchronized.

