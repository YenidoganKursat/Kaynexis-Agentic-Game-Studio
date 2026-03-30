# Quality

## Date
- 2026-03-29

## Summary
- Code quality in this repo means explicit ownership, short canonical names, deterministic state boundaries, and validation that stays close to the change.
- Optimization criteria are part of quality only when they are measured. The repo should not call a pass "optimized" unless it can name the baseline, the first lever, and the fallback lever.
- For this repo, quality work should usually remove ambiguity before it tries to make code faster. That means separating runtime truth from data truth, editor truth, and UI projection.

## Primary sources
- Godot code style guidelines — https://docs.godotengine.org/en/stable/community/contributing/code_style_guidelines.html
- Godot using servers for optimization — https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html
- Unity scripting optimization — https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html
- Unity physics optimization — https://docs.unity3d.com/6000.0/Documentation/Manual/physics-optimization.html
- Unreal C++ coding standard — https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine
- Unreal UMG optimization guidelines — https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine

## Why this matters to this repo
- The repo already routes features, performance, library choices, and systems. Quality needs the same treatment so refactors do not become untracked architecture changes.
- Codex can generate readable code quickly, but it still needs a durable rubric for when a change is merely tidy versus actually maintainable.
- This note gives the repo a shared vocabulary for code review, maintainability, and optimization guardrails across Godot, Unity, and Unreal.

## Decision impact
- Feature briefs and handoffs should state the ownership model before a refactor starts.
- Quality work should name the validation path and, if optimization is in scope, the measurement baseline and first lever.
- If a change depends on a bigger algorithmic or scale choice, escalate to the perf notes instead of hiding that decision inside a generic cleanup pass.
- Quality work should also name the control loop step, the evidence artifact, and the go/no-go gate so the review remains globally consistent across engine families.

## Quality control process
- Frame the change before tuning anything.
- Name the runtime, shared-data, and editor owners before refactoring.
- Choose the smallest proof path before broadening the change.
- Record the baseline and first lever before optimizing.
- Keep the guide, process, example, and checklist aligned together.

## Global alignment
- Use the same short canonical names in the guide, process doc, examples, checklist, and eval notes.
- Keep the quality vocabulary consistent with code review, workflow recipes, and task prompts.
- Treat "quality" as a control loop, not just a style preference.

## Practical framing
- Quality means the reader can tell who owns runtime truth, shared data, editor tooling, and UI projection.
- Quality means the validation loop is narrow enough that one operator can prove the change without guessing.
- Quality means the team can explain what would break first if the feature grew.
- Optimization quality means the team can explain the baseline, the target, the first lever, and the fallback lever before tuning code.

## What to watch out for
- Do not confuse "looks tidy" with "is maintainable."
- Do not optimize without a baseline.
- Do not move to a larger architecture just because it sounds more professional.
- Do not let editor/runtime ownership blur just to save a file.

## Repo impact
- Add `quality-guide.md` and `quality-example.md` to the user-facing docs and routing surface.
- Use this note when a refactor or optimization pass needs a clear rubric before code changes.
