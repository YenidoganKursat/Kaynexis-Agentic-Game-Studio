# Engine Fit Example

## Scope
- Compare Godot 4, Unity 6, and Unreal 5 for three concrete developer profiles: a beginner solo maker, a C# tools-heavy team, and a designer/programmer Unreal team.

## Baseline
- Use the same target game shape and the same quality bar, but change the developer profile and workflow appetite.
- The question is not "which engine is strongest in general?" The question is "which engine is least likely to fight this team?"

## Decision order
1. Name the developer profile.
2. Name the team size and collaboration model.
3. Name the platform appetite and workflow tolerance.
4. Name the engine that best matches the people, not only the game.
5. Name the first proof path that would change the recommendation.

## Example profile scan
- Beginner solo 2D maker: Godot 4 because GDScript is beginner-friendly and the scene-tree model stays compact.
- C# tools-heavy team: Unity 6 because the workflow leans into C#, editor tooling, packages, profiling, and tests.
- Designer/programmer mixed team: Unreal 5 because Blueprint and C++ split naturally across designer and engineer ownership.

## Dashboard schema
- Header cards: developer profile, best engine, language/workflow fit, biggest tradeoff, first proof path
- Matrix: profile vs engine, with green/yellow/red fit markers
- Notes: what the team gains, what the team gives up, and what would make the recommendation flip

## Good agent prompts
- "Which engine fits a beginner solo developer building a small 2D prototype?"
- "Which engine fits a C# tools-heavy team that wants editor tooling, profilers, and tests?"
- "Which engine fits a designer/programmer team that wants Blueprint collaboration and C++ ownership?"

## Validation
- The output keeps fit separate from scorecard-style engine evaluation.
- The output names the developer profile before it names the engine.
- The output includes one matrix or chart pack plus one repo implication.

## Related docs
- [docs/reference/engine-fit.md](../reference/engine-fit.md)
- [docs/reference/engine-selection-guide.md](../reference/engine-selection-guide.md)
- [docs/reference/engine-map.md](../reference/engine-map.md)
- [docs/reference/engine-examples.md](../reference/engine-examples.md)
- [docs/reference/engine-eval.md](../reference/engine-eval.md)
- [docs/research/game-development/foundations/engine-fit.md](../research/game-development/foundations/engine-fit.md)
- [studio/docs/active/engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-fit.md)
- [studio/checklists/discipline/engine_fit.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_fit.toml)
- [studio/docs/active/eval-engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-fit.md)
