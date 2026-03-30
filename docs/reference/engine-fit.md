# Engine Fit Guide

## Summary
- Use this page when the real question is which engine fits a specific developer profile, team shape, or workflow appetite, not which engine has the best scorecard.
- Engine fit is a human/workflow question: language comfort, editor appetite, platform spread, collaboration style, and how much engine-native structure the team wants.
- If you also need proof, pair this with `docs/reference/engine-eval.md`; fit tells you who will be productive, eval tells you what is measurable.

## Primary sources
- [Godot scripting languages](https://docs.godotengine.org/en/4.4/getting_started/step_by_step/scripting_languages.html)
- [Unity scripting tutorial](https://docs.unity3d.com/400/Documentation/Images/manual/ScriptingTutorial.pdf)
- [Unity profiler manual](https://docs.unity3d.com/Manual/Profiler.html)
- [Unity Test Framework package](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unreal Blueprint visual scripting references](https://dev.epicgames.com/documentation/es-mx/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal BuildGraph script tasks reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
- [Unreal command-line arguments](https://dev.epicgames.com/documentation/es-mx/unreal-engine/command-line-arguments-in-unreal-engine)

## Why this matters to this repo
- The repo supports Godot 4, Unity 6, and Unreal 5 at the studio-OS level, so engine choice should reflect both the game and the developer who will carry it.
- A strong fit avoids false starts: a beginner can still fail in a "good" engine if the workflow is wrong for them.
- The routing system can only make good suggestions if it can separate fit from scorecard-style engine evaluation.

## Decision impact
- Keep developer fit separate from build/test/performance scorecards.
- Prefer the engine that matches the current team's skill shape and iteration style before optimizing for abstract power.
- When two engines are close, choose the one with the smallest proof path and the least workflow friction for the people doing the work.

## Developer profiles

| Profile | Best default | Why | Main tradeoff | First proof path |
| --- | --- | --- | --- | --- |
| First-time engine user / beginner | Godot 4 | Godot docs explicitly recommend GDScript for beginners, and the scene/tree model stays compact. | Smaller ecosystem and fewer "already solved" patterns than Unity. | A one-room 2D slice with `Node2D`, `CharacterBody2D`, and `Resource` data. |
| Solo 2D maker / fast prototyper | Godot 4 | Scene-driven iteration, short scripts, and lightweight ownership. | Web/C# constraints may matter if the project changes direction later. | One-room combat or puzzle slice with scene/resource separation. |
| C# gameplay engineer | Unity 6 | Unity centers C# scripting, a large package ecosystem, and strong profiling/testing tooling. | Package and project governance matter more; the repo needs assembly/package discipline. | A prefab-based vertical slice with `ScriptableObject` data and Edit Mode tests. |
| Tools-heavy content team | Unity 6 | Editor scripts, `ScriptableObject`, prefabs, and package boundaries fit content throughput. | Too much editor freedom can create drift without naming and checklist discipline. | One editor tool plus one data-driven runtime screen. |
| Designer-first / Blueprint-heavy team | Unreal 5 | Blueprint visual scripting and gameplay framework ownership fit designer-programmer collaboration. | The setup and compile/package cost are heavier than the lighter engines. | One encounter built from `ACharacter`, `UActorComponent`, and `UUserWidget`. |
| C++ / engine / build engineer | Unreal 5 | Unreal keeps C++ and BuildGraph / automation first-class, which suits engine-level and build-heavy teams. | Iteration is slower and the toolchain footprint is larger. | One gameplay module with BuildGraph or UAT validation. |
| High-fidelity 3D / production-heavy team | Unreal 5 | Unreal is strongest when the team wants deep 3D systems, packaging shape, and larger production structure. | The project pays for that structure in compile time and setup overhead. | One playable 3D encounter with packaging smoke and UI. |
| Mobile/web-first C# team | Unity 6 | The Unity ecosystem is usually the lowest-friction fit for cross-platform C# teams. | The team must actively control package/version sprawl. | A mobile-friendly UI slice with profiler and test validation. |

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

## Related docs
- [docs/examples/engine-fit-example.md](../examples/engine-fit-example.md)
- [docs/research/game-development/foundations/engine-fit.md](../research/game-development/foundations/engine-fit.md)
- [docs/reference/engine-selection-guide.md](engine-selection-guide.md)
- [docs/reference/engine-map.md](engine-map.md)
- [docs/reference/engine-examples.md](engine-examples.md)
- [docs/reference/engine-eval.md](engine-eval.md)
- [studio/docs/active/engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-fit.md)
- [studio/checklists/discipline/engine_fit.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_fit.toml)
- [studio/docs/active/eval-engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-fit.md)
