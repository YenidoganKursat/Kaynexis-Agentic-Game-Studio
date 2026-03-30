# Eval Plan — Engine Fit

## Change under test
- Add a durable engine-fit lane that compares Godot 4, Unity 6, and Unreal 5 against developer profiles, team shapes, and workflow appetite.

## Goal
- Make engine recommendations reproducible for different kinds of developers instead of assuming one engine is best for everyone.

## Risks
- The lane can drift into generic engine evaluation if developer profile and workflow appetite are not named explicitly.
- The lane can become stale if the recommendation matrix is not updated when engine docs or repo support changes.

## Validation
- Route a developer-fit request through the studio router and confirm the engine-fit docs, checklist, and active scorecard appear.
- Confirm the docs validator accepts the new guide, example, and research note.
- Confirm the repo layout validator knows the new files.

## Success criteria
- The guide, example, research note, checklist, and active scorecard are present and cross-linked.
- The agent can recommend an engine for a developer profile and explain the tradeoff clearly.
- The operating model keeps the single-specialist option visible while allowing fit work to fan out if needed.
