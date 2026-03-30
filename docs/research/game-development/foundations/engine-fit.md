# Engine Fit

## Date
- 2026-03-30

## Summary
- Official engine docs point toward different default developer fits.
- Godot explicitly recommends GDScript for beginners, keeps scene/resource ownership tight, and supports C# for experienced users and C++ via GDExtension for performance-heavy work.
- Unity centers C# scripting, profiling, and automated tests, which aligns well with C#-first and editor-tooling-heavy teams.
- Unreal centers Blueprints, C++, BuildGraph, and command-line automation, which aligns well with designer/programmer collaboration and production-heavy 3D teams.
- The fit recommendation in this repo is therefore an inference from official docs plus the repo's supported starter kits, adapters, and validation surfaces.

## Primary sources
- [Godot scripting languages](https://docs.godotengine.org/en/4.4/getting_started/step_by_step/scripting_languages.html)
- [Unity scripting tutorial](https://docs.unity3d.com/400/Documentation/Images/manual/ScriptingTutorial.pdf)
- [Unity profiler manual](https://docs.unity3d.com/Manual/Profiler.html)
- [Unity Test Framework package](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [Unreal Blueprint visual scripting reference](https://dev.epicgames.com/documentation/es-mx/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal BuildGraph script tasks reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine)
- [Unreal command-line arguments](https://dev.epicgames.com/documentation/es-mx/unreal-engine/command-line-arguments-in-unreal-engine)

## Why this matters to this repo
- The repo already routes engine selection, engine proof paths, and engine starter kits separately.
- A fit layer helps the agent explain *why a developer should choose a specific engine* before the more expensive proof path begins.
- It also keeps the advice honest when the right answer is "the best engine for the team is not the strongest engine on paper."

## Decision impact
- Use fit first, then engine-eval if the team is still undecided.
- For beginners, prioritize an engine that reduces cognitive load and helps the first playable slice arrive quickly.
- For C# teams, prioritize editor tooling, test surfaces, and package discipline.
- For designer/programmer teams, prioritize visual scripting, gameplay-framework structure, and packaging clarity.

## Developer profile map
| Profile | Best default | Why | Tradeoff |
| --- | --- | --- | --- |
| Beginner / first engine | Godot 4 | Official docs recommend GDScript for beginners, and the language is tuned for the engine. | Smaller ecosystem and fewer large-team conventions. |
| Solo 2D / lightweight prototype | Godot 4 | Scene/resource ownership stays compact and the iteration loop stays short. | C# web export support is not available in Godot 4. |
| C# gameplay engineer | Unity 6 | Unity's scripting, profiler, and testing docs all center the C# workflow. | Package governance matters a lot. |
| Content/tools-heavy mid-size team | Unity 6 | Editor scripting, ScriptableObject data, and package boundaries align with tool-driven iteration. | Project complexity grows if the team does not enforce standards. |
| Designer-first / Blueprint-heavy team | Unreal 5 | Unreal's visual scripting and gameplay framework fit designer/programmer collaboration. | Compile and tooling overhead are heavier. |
| C++ / build / engine engineer | Unreal 5 | BuildGraph and command-line automation are official first-class surfaces. | The setup cost is higher than lighter engines. |
| High-fidelity 3D / production-heavy team | Unreal 5 | Unreal is strongest when the team wants larger 3D system structure and packaging discipline. | The engine rewards teams that are willing to invest in its conventions. |

## What to watch out for
- Fit is not the same as final production readiness.
- Godot's beginner friendliness does not mean it is always the right choice for teams that need a large plugin ecosystem or C# web support.
- Unity's C# workflow does not mean package sprawl can be ignored.
- Unreal's designer-friendly surface does not mean the team can skip build and packaging discipline.

## Repo impact
- Add a dedicated engine-fit lane so agent prompts can route profile questions separately from proof-path questions.
- Keep `engine-fit.md` paired with `engine-selection-guide.md`, `engine-map.md`, `engine-examples.md`, and `engine-eval.md`.

## Related docs
- [docs/reference/engine-fit.md](../../../reference/engine-fit.md)
- [docs/examples/engine-fit-example.md](../../../examples/engine-fit-example.md)
- [docs/reference/engine-selection-guide.md](../../../reference/engine-selection-guide.md)
- [docs/reference/engine-map.md](../../../reference/engine-map.md)
- [docs/reference/engine-examples.md](../../../reference/engine-examples.md)
- [docs/reference/engine-eval.md](../../../reference/engine-eval.md)
- [studio/docs/active/engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/engine-fit.md)
- [studio/checklists/discipline/engine_fit.toml](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/checklists/discipline/engine_fit.toml)
- [studio/docs/active/eval-engine-fit.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/eval-engine-fit.md)
