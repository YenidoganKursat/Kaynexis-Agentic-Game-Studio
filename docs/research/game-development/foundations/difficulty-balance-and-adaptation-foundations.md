# Difficulty, Balance, and Adaptation Foundations

## Date
- 2026-03-28

## Summary
- Difficulty, balance, and adaptation are not the same thing. Balance is about relationship quality between options and systems; difficulty is about challenge level and pressure; adaptation is about changing the experience in response to the player or run state.
- Dynamic difficulty adjustment can help when a game has strong session goals and large player-skill variance, but it can also destroy trust if it is hidden, overly reactive, or in conflict with mastery.
- For this repo, difficulty work should start with authored targets, readable failure states, and instrumentation. Adaptation is a tool, not the default answer.

## Primary sources
- Hunicke, "The Case for Dynamic Difficulty Adjustment in Games" — https://www.cs.northwestern.edu/~hunicke/pubs/Hamlet.pdf
- AAAI Workshop on Challenges in Game AI: player modeling and adaptive challenge context — https://www.aaai.org/Library/Workshops/ws04-04.php
- Ryan, Rigby, and Przybylski, "The Motivational Pull of Video Games: A Self-Determination Theory Approach" — https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf
- Sweetser and Wyeth, "GameFlow: a model for evaluating player enjoyment in games" — https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf

## Why this matters to this repo
- Difficulty and balance conversations are some of the easiest places for teams to drift into vague opinions. A durable repo needs clearer language than "too hard," "too easy," or "needs more juice."
- Codex can help generate balance assumptions and validation plans, but it should be grounded in a clear distinction between tuning authored values, preserving build variety, and adapting challenge during play.
- This note supports economy, combat, progression, and onboarding work by clarifying what should be tuned directly and what should only adapt carefully.

## Decision impact
- Feature briefs should identify whether the problem is balance, difficulty, or adaptation before proposing a fix.
- Telemetry and QA plans should define which signals matter for challenge tuning: failure location, attempt count, time-to-success, build diversity, abandon points, and assist usage.
- Adaptation logic should be documented explicitly when used. Hidden reactive systems should not be added casually.

## Practical framing
- Treat balance as:
  - the relationship between options, builds, encounters, or resources
  - a question of meaningful tradeoffs, not perfect equality
  - something that can often be improved with authored data and clearer affordances
- Treat difficulty as:
  - pressure, execution demand, and information load
  - something that depends on onboarding, readability, and recovery as much as raw numbers
  - something that should have an explicit target audience and validation loop
- Use adaptation carefully when:
  - player skill variance is high and static tuning produces avoidable churn
  - the adaptation can be explained, bounded, and tested
  - the system preserves trust and does not invalidate player mastery or planning

## What to watch out for
- Do not use DDA as a substitute for bad onboarding, unreadable combat, or broken economy curves.
- Hidden rubber-banding can create a strong sense that the game is cheating or that mastery is fake.
- Balance patches often create new difficulty problems because the team changed numbers without revisiting information load or recovery windows.
- If the repo cannot explain how adaptation works and how it preserves fairness, it should not ship that system yet.
