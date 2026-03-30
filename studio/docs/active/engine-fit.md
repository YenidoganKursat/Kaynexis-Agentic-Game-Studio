# Engine Fit Guide — Kaynexis Agentic Game Studio

## Summary
- Use this active frame when the real question is which engine fits a specific developer profile, team shape, or workflow appetite.
- Keep fit separate from engine-eval: fit tells you who will be productive, eval tells you what is measurable.
- This active page tracks the current fit matrix for the supported engines and should stay aligned with the durable guide.

## Primary sources
- [Godot scripting languages](https://docs.godotengine.org/en/4.4/getting_started/step_by_step/scripting_languages.html)
- [Unity scripting tutorial](https://docs.unity3d.com/400/Documentation/Images/manual/ScriptingTutorial.pdf)
- [Unity profiler manual](https://docs.unity3d.com/Manual/Profiler.html)
- [Unity Test Framework package](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unreal Blueprint visual scripting reference](https://dev.epicgames.com/documentation/es-mx/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal BuildGraph script tasks reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
- [Unreal command-line arguments](https://dev.epicgames.com/documentation/es-mx/unreal-engine/command-line-arguments-in-unreal-engine)

## Why this matters to this repo
- The repo supports Godot 4, Unity 6, and Unreal 5 at the studio-OS level, so engine choice should reflect both the game and the developer who will carry it.
- A strong fit avoids false starts: a beginner can still fail in a "good" engine if the workflow is wrong for them.
- The routing system can only make good suggestions if it can separate fit from scorecard-style engine evaluation.

## Decision impact
- Prefer the engine that matches the current team's skill shape and iteration style before optimizing for abstract power.
- When two engines are close, choose the one with the smallest proof path and the least workflow friction for the people doing the work.
- Use `docs/reference/engine-eval.md` only after the fit matrix still leaves a real choice on the table.

## Developer profiles

| Profile | Best default | Why | Main tradeoff |
| --- | --- | --- | --- |
| Beginner / first engine | Godot 4 | GDScript is the beginner-first path in the official docs | Smaller ecosystem than Unity |
| Solo 2D maker / fast prototyper | Godot 4 | Scene/resource ownership stays compact and the iteration loop stays short | Web/C# constraints may matter if the project changes direction later |
| C# gameplay engineer | Unity 6 | C#-centric scripting, profiler, and test tooling | Package governance is necessary |
| Tools-heavy content team | Unity 6 | Editor scripting, ScriptableObject data, and package boundaries fit content throughput | Too much editor freedom can create drift without naming and checklist discipline |
| Designer-first / Blueprint-heavy team | Unreal 5 | Blueprint and gameplay-framework collaboration fit designer-programmer ownership | The setup and compile/package cost are heavier than the lighter engines |
| C++ / engine / build engineer | Unreal 5 | BuildGraph, C++, and command-line automation are first-class | Iteration is slower and the toolchain footprint is larger |

## Fit matrix
| Developer profile | Best default | Why | Main tradeoff |
| --- | --- | --- | --- |
| Beginner / first engine | Godot 4 | GDScript is the beginner-first path in the official docs | Smaller ecosystem than Unity |
| C# gameplay engineer | Unity 6 | C#-centric scripting, profiler, and test tooling | Package governance is necessary |
| Designer-first team | Unreal 5 | Blueprint and gameplay-framework collaboration | Heavier setup and iteration cost |
| C++ / build engineer | Unreal 5 | C++ and BuildGraph are first-class | Large toolchain footprint |

## Strengths and tradeoffs

### Godot 4
- Strengths: beginner-friendly GDScript, tight editor integration, compact scene/resource ownership, good small-team speed.
- Tradeoffs: smaller ecosystem than Unity, fewer off-the-shelf enterprise patterns, and C# web export is not supported in Godot 4.

### Unity 6
- Strengths: C# workflow, large ecosystem, profiler and test framework support, strong editor-tooling culture, and broad platform reach.
- Tradeoffs: package and project governance can get noisy, so teams need discipline around dependencies and assemblies.

### Unreal 5
- Strengths: Blueprint and C++ split, gameplay-framework-first architecture, strong automation and packaging tooling, and a clear path for large 3D work.
- Tradeoffs: larger setup footprint, heavier compile/iteration cost, and a steeper learning curve for teams that do not want Unreal-native structure.

## Current frame
- Supported engines: Godot 4, Unity 6, Unreal 5
- Current recommendation context: fit the engine to the developer profile before comparing scorecards
- Current comparison frame:
  - Godot 4 for beginners, solo prototypers, and lightweight scene-driven work
  - Unity 6 for C# teams and editor/tooling-heavy workflows
  - Unreal 5 for Blueprint/C++ teams and production-heavy 3D collaboration

## How to use this guide
- Start by naming the developer profile and team shape.
- Decide whether the team is optimizing for iteration speed, editor tools, visual scripting, C++ ownership, or platform spread.
- If the fit is still unclear, compare the fit matrix with `docs/reference/engine-eval.md` before making a final call.

## Example prompts for the agent
- "Which engine fits a beginner solo developer building a small 2D game?"
- "Which engine fits a C# gameplay engineer who needs editor tooling and tests?"
- "Which engine fits a designer-first team that wants Blueprint-heavy collaboration?"

## Validation
- Name the developer profile before recommending an engine.
- Separate fit from build/test/performance proof.
- Return one matrix or recommendation card plus one repo implication.

## Recommendation state
- Favor the engine that minimizes workflow friction for the people who will actually build the slice.
- When the fit is unclear, keep the matrix current and rerun the fit eval plan before locking the choice.

## Related docs
- `docs/reference/engine-fit.md`
- `docs/examples/engine-fit-example.md`
- `docs/reference/engine-selection-guide.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-examples.md`
- `docs/reference/engine-eval.md`
- `docs/research/game-development/foundations/engine-fit.md`
- `studio/checklists/discipline/engine_fit.toml`
- `studio/docs/active/eval-engine-fit.md`
