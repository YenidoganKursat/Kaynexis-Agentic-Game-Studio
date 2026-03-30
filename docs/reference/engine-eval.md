# Engine Eval

## Summary
- Use this page when the task is to compare Godot 4, Unity 6, and Unreal 5 on build, test, performance, and toolchain readiness instead of on taste or brand preference.
- Treat engine evaluation as a scorecard problem: the goal is to name the current family, the exact measurement surface, the first blocker, and the smallest proof path before anyone commits to an engine choice.
- This is not a general benchmark page. `docs/reference/benchmark-guide.md` is for measurement harnesses; this page is for engine-family fit.

## Primary sources
- [Godot performance documentation](https://docs.godotengine.org/en/stable/tutorials/performance/index.html)
- [Godot compiling for Linux / BSD](https://docs.godotengine.org/en/stable/reference/compiling_for_x11.html)
- [Godot 4 documentation root](https://docs.godotengine.org/en/stable/)
- [Unity Test Framework package](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unity performance profiling documentation](https://docs.unity3d.com/Manual/Profiler.html)
- [Unity performance testing package](https://docs.unity3d.com/Packages/com.unity.performance-testing@latest)
- [Unreal BuildGraph script tasks reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
- [Unreal AutomationController API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/AutomationController)
- [Unreal Insights guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-migration-guide?application_version=5.6)

## Why this matters to this repo
- The repo supports Godot, Unity, and Unreal at the studio-OS level, so a future engine choice should be evidence-backed instead of inferred from a single starter kit or a single quick smoke.
- Build time, test latency, profiler availability, and CI friction are part of engine choice, not a follow-up after the choice is already locked.
- A clear evaluation lane keeps engine selection, build pipeline design, and performance assumptions in sync.

## Decision impact
- Prefer one primary engine and one comparison engine when possible.
- Separate build, tests, performance, and toolchain friction before drawing conclusions.
- Name the first blocker that would change the decision, not just the best-looking happy path.

## Evaluation model

### Build
- Measure how quickly the engine can produce a repeatable target build or export.
- Record whether the build is editor-driven, batch-driven, headless, or adapter-driven.
- Record the smallest command that proves the contract.

### Tests
- Measure what the engine exposes for automated tests, smoke tests, or replayable validation.
- Record whether tests run in editor, batch mode, automation tool, or repo-local contract smoke.
- Record the narrowest test path that gives a useful signal.

### Performance
- Measure the frame, memory, startup, and pacing envelope that matters to the game shape.
- Record the profiler or trace path the team will use.
- Record the first lever that should move if the score is bad.

### Toolchain and CI
- Measure how much setup and CI friction exists before a new contributor can reproduce the engine contract.
- Record local binary assumptions, command-line requirements, and packaging or export helpers.
- Record whether the engine can be verified in the repo's CI shape or only on a developer machine.

## Scorecard schema
- Header cards: candidate engines, current target, strongest signal, biggest risk
- Matrix: build path, test path, performance path, toolchain friction, platform reach
- Heatmap: green/yellow/red readiness by engine family
- Decision card: recommended engine, first proof path, fallback path, and owner

```mermaid
flowchart LR
    ["Official engine docs"] --> ["Name build / test / perf surfaces"]
    ["Official engine docs"] --> ["Name toolchain friction"]
    ["Name build / test / perf surfaces"] --> ["Scorecard matrix"]
    ["Name toolchain friction"] --> ["Scorecard matrix"]
    ["Scorecard matrix"] --> ["Recommendation card"]
```

## Monitoring cadence
- Per engine change: refresh the scorecard before claims about support or readiness.
- Per milestone: re-check build, test, and performance assumptions before scope locks.
- Before an engine switch: compare the next candidate against the current scorecard rather than against memory.

## Example prompts for the agent
- "Compare Godot 4, Unity 6, and Unreal 5 for build, test, performance, and toolchain readiness on this project."
- "Turn the current engine support into a matrix with build smoke, test smoke, performance baseline, and CI friction."
- "Tell me which engine is easiest to validate in CI for a small vertical slice and what the first blocker would be."

## Validation
- Name the candidate engines and the target project shape before scoring.
- Separate build, test, performance, and toolchain deltas.
- Return one scorecard or matrix plus one repo implication.

## Related docs
- [docs/examples/engine-eval-example.md](../examples/engine-eval-example.md)
- [docs/research/game-development/foundations/engine-eval.md](../research/game-development/foundations/engine-eval.md)
- [docs/reference/engine-selection-guide.md](engine-selection-guide.md)
- [docs/reference/engine-map.md](engine-map.md)
- [docs/reference/engine-examples.md](engine-examples.md)
- [docs/reference/benchmark-guide.md](benchmark-guide.md)
- [docs/reference/perf-guide.md](perf-guide.md)
- [docs/reference/quality-guide.md](quality-guide.md)
- [docs/reference/ci-cd.md](ci-cd.md)
- [studio/docs/active/engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-eval.md)
- [studio/checklists/discipline/engine_eval.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_eval.toml)
- [studio/docs/active/eval-engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-eval.md)
