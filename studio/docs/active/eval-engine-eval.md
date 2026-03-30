# Eval Plan — Engine Eval

## Change under test
- Add a durable engine-evaluation lane that compares build, test, performance, and toolchain readiness across Godot 4, Unity 6, and Unreal 5.

## Goal
- Make engine choice and engine support decisions reproducible instead of opinion-driven.

## Risks
- The lane can drift into generic benchmark language if build and test surfaces are not named explicitly.
- The lane can become stale if one engine's build or test contract changes without a docs update.

## Validation
- Route an engine-comparison request through the studio router and confirm the engine-eval docs, checklist, and active scorecard appear.
- Confirm the docs validator accepts the new guide, example, and research note.
- Confirm the repo layout validator knows the new files.

## Success criteria
- The guide, example, research note, checklist, and active scorecard are present and cross-linked.
- The agent can produce a build/test/performance scorecard for each engine family without guessing.
- The operating model keeps the single-specialist option visible while allowing comparison work to fan out if needed.
