# Theory

## Date
- 2026-03-30

## Summary

Theoretical infrastructure for this repo should be treated as a lens stack, not as a vague "design philosophy" note. The stack helps the agent explain why a feature exists, what experience it should create, what evidence supports the claim, and what would falsify it.

## Primary sources

- `docs/reference/theory-guide.md`
- `docs/reference/architecture-guide.md`
- `docs/research/game-development/foundations/frameworks.md`
- `docs/research/game-development/foundations/ux.md`
- `docs/research/game-development/foundations/balance.md`
- `docs/research/game-development/foundations/quality.md`
- Hunicke, LeBlanc, and Zubek, "MDA: A Formal Approach to Game Design and Game Research" — https://www.cs.northwestern.edu/~hunicke/MDA.pdf
- Sweetser and Wyeth, "GameFlow: a model for evaluating player enjoyment in games" — https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf
- Ryan, Rigby, and Przybylski, "The Motivational Pull of Video Games: A Self-Determination Theory Approach" — https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf
- PENS overview — https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/
- Swink, game-feel review summary — https://arxiv.org/abs/2011.09201

## Why this matters to this repo

- Codex can generate many valid-looking mechanics, but theory keeps the repo from shipping systems that are plausible on paper and hollow in play.
- The theory stack gives designers, programmers, QA, and maintainers a shared vocabulary for outcome, tension, motivation, readability, and proof.
- It also makes genre planning, feature briefs, and review passes easier to compare because the same lens order can be reopened later.

## Decision impact

- The player outcome should be stated before the lens stack.
- The lens stack should be narrow enough to be actionable.
- Theory claims should point to evidence or research notes, not intuition alone.
- When theory and implementation disagree, keep the disagreement visible instead of hiding it in implementation details.

## Theory stack model

- MDA for mechanic to experience mapping
- GameFlow for challenge, control, and feedback
- SDT / PENS for motivation and social need support
- Affordance and cognitive load for readability and learning
- Balance and difficulty for pressure, fairness, and adaptation
- Systems thinking for long-loop behavior and feedback chains

## Repo impact

- Add a theory guide and example when a task needs a durable lens stack before implementation.
- Start theory-heavy feature briefs with the outcome, the lens stack, the evidence, and the first failure mode.
- Keep the theory lane separate from engine choice, custom architecture, and extension packs.

## Related docs

- `docs/reference/theory-guide.md`
- `docs/examples/theory-example.md`
- `docs/research/game-development/foundations/frameworks.md`
- `docs/research/game-development/foundations/ux.md`
- `docs/research/game-development/foundations/balance.md`
- `docs/research/game-development/foundations/quality.md`
- `studio/checklists/discipline/theory.toml`
- `studio/docs/active/eval-theory.md`
