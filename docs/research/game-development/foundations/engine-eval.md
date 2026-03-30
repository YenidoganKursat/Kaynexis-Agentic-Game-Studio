# Engine Eval

## Date
- 2026-03-30

## Summary
- Engine evaluation in this repo should be treated as a source-backed scorecard for build, test, performance, and toolchain readiness across Godot 4, Unity 6, and Unreal 5.
- The goal is to compare engine families on measurable proof paths, not on reputation or memory.
- The evaluation should tell the agent what to measure first, what the first blocker is, and what recommendation should survive a broader review.

## Primary sources
- [Godot Docs - performance](https://docs.godotengine.org/en/stable/tutorials/performance/index.html)
- [Godot Docs - compiling for Linux / BSD](https://docs.godotengine.org/en/stable/reference/compiling_for_x11.html)
- [Godot Docs root](https://docs.godotengine.org/en/stable/)
- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unity Profiler manual](https://docs.unity3d.com/Manual/Profiler.html)
- [Unity Performance Testing package](https://docs.unity3d.com/Packages/com.unity.performance-testing@latest)
- [Unreal BuildGraph script tasks reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
- [Unreal AutomationController API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Developer/AutomationController)
- [Unreal Engine 5 migration guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-migration-guide?application_version=5.6)

## Why this matters to this repo
- The repo already treats engine choice, platform choice, quality, benchmarking, and performance as separate decisions.
- Engine choice should be justified with a build/test/perf scorecard because the starter kits and adapters make different assumptions per engine family.
- A consistent eval structure keeps the agent from confusing "works in a stub" with "fits the project."

## Decision impact
- Choose one current engine and one comparison engine when possible.
- Keep build, test, performance, and toolchain signals separate.
- Record the smallest proof path that would change the decision.

## Scorecard model
| Axis | What it asks | What to record |
|---|---|---|
| Build | How quickly can the engine produce a reproducible target build? | command path, artifact path, friction |
| Tests | What automated test surface exists and how fast is it? | test runner, results path, headless support |
| Performance | What profiler or trace path proves frame, memory, and load behavior? | profiler path, baseline, first lever |
| Toolchain | How much setup or binary friction exists? | local prerequisites, CI parity, release blockers |
| Platform | How much platform drift is implied by the engine? | desktop, web, mobile, TV, Deck or console assumptions |

## Signal map
| Family | Watch first | Typical proof |
|---|---|---|
| Godot 4 | export path, static smoke, runtime smoke, performance docs | export command plus a stable smoke result |
| Unity 6 | batch build path, Test Framework, Profiler, performance testing package | test/build command plus a timing or profile artifact |
| Unreal 5 | BuildGraph / UAT, AutomationController, Insights / trace path | package command plus an automation or trace artifact |

## Repo impact
- Keep `studio/docs/active/engine-profile.md` explicit about the current reference engine and the current comparison context.
- Keep `docs/reference/engine-selection-guide.md` and `docs/reference/engine-map.md` paired with the eval guide when a choice is being made.
- Use the eval scorecard before a new engine claim lands in a milestone, a porting note, or a release conversation.

## Related docs
- [docs/reference/engine-eval.md](../../../reference/engine-eval.md)
- [docs/examples/engine-eval-example.md](../../../examples/engine-eval-example.md)
- [docs/reference/engine-selection-guide.md](../../../reference/engine-selection-guide.md)
- [docs/reference/engine-map.md](../../../reference/engine-map.md)
- [docs/reference/benchmark-guide.md](../../../reference/benchmark-guide.md)
- [docs/reference/perf-guide.md](../../../reference/perf-guide.md)
- [docs/reference/quality-process.md](../../../reference/quality-process.md)
- [docs/research/game-development/engines/README.md](../README.md)
- [studio/docs/active/engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-eval.md)
- [studio/checklists/discipline/engine_eval.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_eval.toml)
- [studio/docs/active/eval-engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-eval.md)
