# Engine Eval Example

## Scope
- Compare Godot 4, Unity 6, and Unreal 5 for a Steam-first prototype that needs build, test, performance, and toolchain clarity before the team commits.

## Baseline
- One slice, same gameplay shape, same target hardware, same documentation standard.
- The question is not "which engine is best in general?" The question is "which engine is easiest to prove for this repo's first slice?"

## Decision order
1. Name the engine families being compared.
2. Name the build, test, and performance surfaces that will be measured.
3. Name the first blocker for each engine.
4. Name the first validation that would change the recommendation.

## Example signal scan
- Godot 4: export path, static smoke, runtime smoke when available, profiler path, scene/resource boundary
- Unity 6: batch build path, test framework path, profiler path, performance testing path, editor tooling friction
- Unreal 5: BuildGraph / UAT path, automation test path, Insights / trace path, packaging and module friction

## Dashboard schema
- Header cards: candidate engines, current target, strongest signal, biggest risk
- Matrix: build readiness, test readiness, performance readiness, toolchain friction, platform reach
- Heatmap: green/yellow/red readiness by engine family
- Recommendation card: recommended engine, first proof path, fallback path, and owner

## Good agent prompts
- "Turn this into an engine scorecard with build, tests, performance, and CI friction for Godot, Unity, and Unreal."
- "Tell me which engine has the smallest first proof path for a Steam-first vertical slice."
- "Summarize the strongest build/test/performance signals and the first blocker for each engine family."

## Validation
- The evaluation keeps build, test, and performance separate.
- The scorecard names a first blocker, not just a favorite engine.
- The output includes one matrix or chart pack and one repo implication.

## Related docs
- [docs/reference/engine-eval.md](../reference/engine-eval.md)
- [docs/reference/engine-selection-guide.md](../reference/engine-selection-guide.md)
- [docs/reference/engine-map.md](../reference/engine-map.md)
- [docs/reference/engine-examples.md](../reference/engine-examples.md)
- [docs/reference/benchmark-guide.md](../reference/benchmark-guide.md)
- [docs/reference/perf-guide.md](../reference/perf-guide.md)
- [docs/research/game-development/foundations/engine-eval.md](../research/game-development/foundations/engine-eval.md)
- [studio/docs/active/engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-eval.md)
- [studio/checklists/discipline/engine_eval.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_eval.toml)
- [studio/docs/active/eval-engine-eval.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-eval.md)
