# Theory Guide

## Summary

Use this guide when a task needs a durable theory stack before design or implementation. It sits above the narrower notes in `frameworks.md`, `ux.md`, `balance.md`, and `quality.md`.

## Primary sources

- Hunicke, LeBlanc, and Zubek, "MDA: A Formal Approach to Game Design and Game Research" — https://www.cs.northwestern.edu/~hunicke/MDA.pdf
- Sweetser and Wyeth, "GameFlow: a model for evaluating player enjoyment in games" — https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf
- Ryan, Rigby, and Przybylski, "The Motivational Pull of Video Games: A Self-Determination Theory Approach" — https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf
- PENS overview — https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/
- Swink, game-feel review summary — https://arxiv.org/abs/2011.09201
- Nielsen Norman Group usability heuristics — https://www.nngroup.com/articles/ten-usability-heuristics/
- Microsoft Gaming Accessibility Guidelines — https://learn.microsoft.com/en-us/gaming/accessibility/guidelines

## Why this matters to this repo

- The repo can generate plausible mechanics quickly, but theory keeps us from producing systems that are technically coherent and experientially empty.
- A shared theory stack gives Codex a stable language for player outcome, tension, motivation, readability, and validation.
- It also keeps feature briefs, genre plans, and quality passes from drifting into vague "feels good" language.

## Decision impact

- Start from player outcome and intended experience before choosing mechanics.
- Use only the lenses that actually answer the current question; most tasks do not need the whole stack.
- Keep theory separate from implementation, engine selection, and project-specific rule packs.
- If the evidence does not support the claim, stop and reopen the lens instead of inventing confidence.

## Theory stack

| Lens | What it answers | Useful output |
|---|---|---|
| MDA | What experience the mechanic should create | Mechanic to dynamic to aesthetic chain |
| GameFlow | Whether challenge, control, feedback, and concentration are healthy | Friction and pacing notes |
| SDT / PENS | Whether the design supports competence, autonomy, and relatedness | Motivation and social-loop notes |
| Affordance and cognitive load | Whether the player can perceive and learn the system | Readability, hierarchy, and onboarding notes |
| Balance and difficulty | Whether challenge and adaptation are fair | Tuning targets and failure-recovery notes |
| Systems thinking | What feedback loops drive long-term behavior | Loop map and bottleneck map |

## How to use this guide

1. State the player outcome and dominant tension.
2. Choose the minimum lens set that answers the question.
3. Gather one piece of evidence for each lens you use.
4. Name the first failure mode or contradiction you expect to see.
5. Hand the result to a feature brief, genre plan, or system design note.

## Example prompts for the agent

- "Build a theory stack for a tactical RPG battle tutorial and name the MDA, flow, and motivation lenses before implementation."
- "Review a combat room for affordance, cognitive load, and feedback order before the first refactor."
- "Create a theory pack for a cozy sim progression loop and identify the player outcome, friction budget, and validation path."

## Validation

- Name the lens order before design starts.
- Name the evidence behind each claim.
- Name the failure mode that would falsify the theory.
- Keep the guide, example, research note, checklist, and eval plan in sync.

## Related docs

- `docs/examples/theory-example.md`
- `docs/research/game-development/foundations/theory.md`
- `docs/research/game-development/foundations/frameworks.md`
- `docs/research/game-development/foundations/ux.md`
- `docs/research/game-development/foundations/balance.md`
- `docs/research/game-development/foundations/quality.md`
- `studio/checklists/discipline/theory.toml`
- `studio/docs/active/eval-theory.md`
