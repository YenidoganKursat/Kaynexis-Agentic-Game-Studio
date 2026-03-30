# Frameworks

## Date
- 2026-03-28

## Summary
- MDA is useful when the team needs to separate implementation choices from player-facing outcomes. It frames mechanics as authored rules, dynamics as the behavior that emerges when those rules run, and aesthetics as the felt player experience those dynamics produce.
- GameFlow is useful when the repo needs a language for challenge, clarity, feedback, concentration, and control. It helps prevent feature briefs from focusing only on content quantity instead of quality of moment-to-moment play.
- Self-Determination Theory and PENS are useful when the team is designing progression, onboarding, or social loops. They give a more defensible language for motivation than vague statements like "make it sticky" or "make it fun."
- For this repo, the right sequence is usually: define the player outcome first, map the mechanic and systemic consequences second, then validate whether challenge, clarity, feedback, and motivational needs are actually supported.
- If the task needs that sequence named explicitly for the next agent, pair this note with `docs/reference/theory-guide.md` and `docs/examples/theory-example.md` so the lens stack, evidence path, and failure mode stay explicit.

## Primary sources
- Hunicke, LeBlanc, and Zubek, "MDA: A Formal Approach to Game Design and Game Research" — https://www.cs.northwestern.edu/~hunicke/MDA.pdf
- Sweetser and Wyeth, "GameFlow: a model for evaluating player enjoyment in games" — https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf
- Ryan, Rigby, and Przybylski, "The Motivational Pull of Video Games: A Self-Determination Theory Approach" — https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf
- PENS overview — https://selfdeterminationtheory.org/player-experience-of-needs-satisfaction-pens/

## Why this matters to this repo
- Codex can generate many plausible mechanics quickly, but speed creates a risk of building systems that are technically coherent and experientially empty.
- These frameworks give the repo a durable way to ask whether a mechanic, feature brief, or milestone is supporting readable challenge, satisfying feedback, and real player motivation instead of novelty alone.
- They also make design review more grounded. A discussion can move from "this feels weak" to "the dynamics are not creating the intended tension" or "the loop is undermining competence."

## Decision impact
- Feature briefs should describe the intended aesthetic or player outcome before implementation details.
- QA matrices should include at least one readability or feedback check and one motivation or engagement check when the feature changes progression or core verbs.
- Genre research and system research should explicitly call out which dynamics are doing the real work, not just which mechanics are present.

## Practical framing
- Use MDA when:
  - the repo needs to explain why a mechanic exists at all
  - two implementations produce different player feel even if they sound similar on paper
  - a feature is expanding in scope without a clear player payoff
- Use GameFlow when:
  - the team is tuning onboarding, combat readability, feedback cadence, pacing, or failure recovery
  - the experience is busy but not engaging
  - players understand the rules eventually, but the moment-to-moment loop still feels muddy
- Use Self-Determination Theory and PENS when:
  - the task affects progression, rewards, social features, or long-session retention
  - the team is trying to understand whether players feel competent, autonomous, and meaningfully connected
  - a design is generating compliance behavior instead of genuine motivation

## What to watch out for
- Do not treat these frameworks as scorecards that can prove a design is good. They are lenses for reasoning, not automatic validators.
- MDA is most useful when the team actually traces mechanics to outcomes; it becomes empty jargon if the repo stops at naming the categories.
- GameFlow can be misused as a polish checklist. Some of its dimensions are structural and require mechanical or content changes, not UI garnish.
- Motivation language becomes sloppy quickly. Avoid claiming "autonomy" or "competence" without pointing to the actual player choices, mastery surfaces, and feedback loops that support those claims.
