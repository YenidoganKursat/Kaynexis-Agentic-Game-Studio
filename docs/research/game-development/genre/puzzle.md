# Puzzle

## Date
- 2026-03-29

## Summary
- Puzzle games fail first on rule ambiguity, hinting quality, and misunderstanding recovery. A puzzle should teach the rule, test the rule, then twist the rule without making the player feel tricked.
- The dominant loop is:
  - learn a rule
  - apply it
  - watch the condition change
  - solve by reasoning, not by memorizing hidden exceptions
- The first systems that usually break are:
  - rules that are too vague to infer
  - hint systems that reveal too much or too little
  - reset/undo behavior that is not forgiving enough
  - puzzle composition that hides the intended insight
- This genre needs explicit architecture for:
  - affordance clarity
  - deterministic rule ownership
  - hint and undo systems
  - puzzle state resets
  - teach/test/twist sequencing

## Primary sources
- [Portal 2 on Steam](https://store.steampowered.com/app/620/Portal_2/)
- [The Witness on Steam](https://store.steampowered.com/app/210970/the-witness/)

## Why this matters to this repo
- Puzzle tasks in this repo should not be routed like ordinary level or UI tasks. They are rule-design and misunderstanding-recovery problems first.
- Agents should explicitly name:
  - the one rule the player must learn
  - how the game proves the rule is real
  - what happens when the condition changes
  - how the player recovers from a wrong assumption
- First slices should prove one rule, one test, and one twist before the puzzle space expands.

## Decision impact
- Future presets and feature briefs should require:
  - deterministic rule state
  - undo/reset or recovery support
  - hint timing and hint scope
  - a teach/test/twist sequence that does not hide the actual rule
- When a project selects this genre, route output should surface rule clarity, recovery, and sequencing notes together.
