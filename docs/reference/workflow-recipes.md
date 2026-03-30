# Workflow Recipes

These are practical, repeatable ways to use the repo.

Use them when you want a reliable path instead of inventing your own flow every time.

## Recipe: Start a new game baseline

Use this when the repo is fresh or the project identity changed.

```bash
# Replace --engine with godot-4, unity-6, or unreal-5 depending on the real project.
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes
python3 scripts/codex_studio.py doctor
```

Then open:

- `studio/docs/active/game-brief.md`
- `studio/docs/active/engine-profile.md`
- `studio/docs/active/current-sprint.md`
- the matching `docs/research/game-development/engines/*-2d-3d-class-and-mechanic-guide.md`

## Recipe: Turn an idea into a real slice

Use this when you have a feature idea but not yet a buildable task.

```bash
python3 scripts/codex_studio.py next "Add a short-range parry that rewards precise timing"
python3 scripts/codex_studio.py checklist --task "Add a short-range parry that rewards precise timing"
python3 scripts/scaffold_feature.py "Parry Mechanic" --with-adr --with-test-plan --with-eval-plan
```

The scaffold now also writes a default handoff contract, traceability doc, and optional validation docs so the slice is easier to review and continue.

Good outcome:

- one routed task
- one merged checklist
- one durable feature brief
- one explicit validation path

## Recipe: Use the speed pack for the fastest safe start

Use this when the work is narrow, urgent, or needs the smallest useful bundle before anything else.

```bash
python3 scripts/codex_studio.py next "Use the speed pack for a short UI fix and keep the proof path minimal"
python3 scripts/codex_studio.py checklist --task "Use the speed pack for a short UI fix and keep the proof path minimal"
```

Then read:

- `docs/reference/agent-speedpack.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/setup/quick-access.md`

Keep the brief explicit about:

- the owner
- the narrow route
- the one proof path
- the shortest useful bundle
- whether history artifacts are actually needed later

## Recipe: Plan a game by genre

Use this when the team knows the genre family but needs a real planning schema before the first feature brief.

```bash
python3 scripts/codex_studio.py next "Write a genre plan schema for a tactical RPG"
python3 scripts/codex_studio.py checklist --task "Write a genre plan schema for a tactical RPG"
```

Then read:

- `docs/reference/genre-plan.md`
- `docs/examples/genre-plan-example.md`
- `docs/examples/genre-gallery-example.md`
- `docs/research/game-development/genre/genre-plan.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`

Keep the brief explicit about:

- player outcome
- dominant tension
- contrast set
- loop ladder
- state owner
- accessibility envelope
- performance envelope
- validation ladder

## Recipe: Present the studio capability catalog

Use this when someone asks what the repo can do at a high level and wants a short, scannable answer instead of a lane-specific deep dive.

```bash
python3 scripts/codex_studio.py next "Summarize everything this studio can do and point me at the right starting docs for each lane"
python3 scripts/codex_studio.py checklist --task "Show me the studio capability catalog and the shortest starting docs for each family"
```

Then read:

- `docs/reference/capabilities.md`
- `docs/examples/capabilities-example.md`
- `docs/research/game-development/foundations/capabilities.md`

Keep the brief explicit about:

- the major capability families
- the best starting docs for each family
- the narrow lane to use next
- the simple user summary the repo should preserve

## Recipe: Investigate a bug without thrashing

Use this when a bug is vague or emotionally noisy.

```bash
python3 scripts/scaffold_bugfix.py "Player gets stuck after dodge near a wall" --with-test-plan --with-eval-plan
python3 scripts/codex_studio.py next "Investigate player gets stuck after dodge near a wall"
python3 scripts/codex_studio.py checklist --task "Investigate player gets stuck after dodge near a wall"
```

Then document:

- reproduction steps
- engine/runtime assumptions
- likely owner
- smallest validation loop
- the matching system atlas entry and engine class atlas lookup

## Recipe: Classify recurring engine bugs

Use this when the task is about recurring engine error families or troubleshooting surfaces rather than one concrete repro.

```bash
python3 scripts/codex_studio.py next "Classify recurring Godot signal and node-path bugs before patching anything"
python3 scripts/codex_studio.py checklist --task "Classify recurring Unity null reference and prefab override bugs before patching anything"
```

Then read:

- `docs/reference/engine-bugs.md`
- `docs/examples/engine-bugs-example.md`
- `docs/research/game-development/foundations/engine-bugs.md`
- `studio/docs/templates/bug-report.md`
- `studio/docs/templates/crash-triage.md`

Keep the brief explicit about:

- the engine family
- the likely bug family
- the first debug surface
- whether the failure is editor-only, runtime-only, or packaged-build-only
- the later bugfix packet if the task turns into a concrete repro

## Recipe: Record prompt history and agent notes

Use this when the work should be easy to reopen later without reading the whole chat.

```bash
python3 scripts/codex_studio.py journal prompt \
  --prompt "Add a prompt history log and an agent journal so the user can review later." \
  --route "prompt history / agent journal" \
  --summary "Created append-only journal sections and a journal command." \
  --doc docs/reference/prompt-journal.md \
  --json

python3 scripts/codex_studio.py journal agent \
  --step "Draft the journal template and journal command" \
  --expected "One active file with two append-only sections" \
  --found "The repo had no durable history trail yet" \
  --improved "Added a shared prompt journal file and append helper" \
  --evaluation "The record is now easy to reopen later without reading the whole chat" \
  --doc docs/reference/prompt-journal.md \
  --validation "python3 scripts/journal.py prompt --dry-run --json" \
  --json
```

Then read:

- `docs/reference/prompt-journal.md`
- `docs/examples/prompt-journal-example.md`

Keep the brief explicit about:

- the user prompt or task title
- the route or owning discipline
- the expectation, finding, improvement, and evaluation
- the later review path

## Recipe: Record task assignments and agent conversation turns

Use this when the work fans out across agents and you need the assignment history plus the conversation turns to stay reviewable later.

```bash
python3 scripts/codex_studio.py journal transcript \
  --kind assignment \
  --task "Profile the inventory HUD and report the first bottleneck" \
  --speaker "Kaynexis" \
  --target "technical_director, qa_lead" \
  --message "Capture one baseline, one likely bottleneck, and one first lever before any refactor." \
  --json

python3 scripts/codex_studio.py journal transcript \
  --kind conversation \
  --speaker "technical_director" \
  --target "qa_lead" \
  --message "Use a shared baseline before changing pooling or layout code." \
  --json
```

Then read:

- `docs/reference/agent-transcript.md`
- `docs/examples/agent-transcript-example.md`
- `docs/reference/prompt-journal.md`
- `docs/examples/prompt-journal-example.md`

Keep the brief explicit about:

- the task or thread title
- the speaker and target
- the assignment or reply text
- the result or follow-up
- the later review path

## Recipe: Build an agent execution packet

Use this when the task needs a reusable pre-flight contract before implementation starts.

```bash
python3 scripts/codex_studio.py packet \
  --task "Build an execution packet for a UI refactor" \
  --owner "Kaynexis" \
  --mode "single-specialist" \
  --goal "Keep the refactor narrow and reviewable" \
  --route "agent execution / work packet" \
  --proof-path "python3 scripts/codex_studio.py packet --dry-run --json"
```

Then read:

- `docs/reference/agent-execution.md`
- `docs/examples/agent-execution-example.md`
- `docs/research/game-development/foundations/agent-execution.md`

Keep the brief explicit about:

- the owner and operating mode
- the goal and expected outputs
- the custom rules or overrides
- the proof path and stop conditions
- the later review path

## Recipe: Build an agent validation matrix

Use this when you need to prove why a single specialist, pair, or panel is the right operating choice.

```bash
python3 scripts/codex_studio.py next "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
python3 scripts/codex_studio.py checklist --task "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
```

Then read:

- `docs/reference/agent-validation-matrix.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/research/game-development/foundations/agent-validation-matrix.md`

Keep the brief explicit about:

- the operating mode
- the lane split or single-specialist fallback
- the proof rows
- the evidence path
- the later review trail

## Recipe: Research before architecture work

Use this when the task affects save, combat, AI, pathfinding, data ownership, authority, projection, or engine structure.

```bash
python3 scripts/codex_studio.py next "Design boss phase authority and projection boundaries"
python3 scripts/codex_studio.py checklist --task "Design boss phase authority and projection boundaries"
```

Before implementation, make sure the final task references at least one relevant research note.
If the task is visual or presentation-heavy, also read the matching `*-visuals-animation-playbook.md` for the engine before writing code or content.
If the task is audio, animation, or presentation-heavy, also read the matching `*-presentation.md` playbook and `docs/reference/audio-animation-guide.md` before writing code or content.
If the task is system-heavy, also start from `docs/reference/system-atlas.md` so the ownership model is explicit before the slice grows.
If the task is architecture-heavy, also start from `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` so the owner, boundary, proof path, diagram shape, and architecture checklist evidence are explicit before the slice grows.

## Recipe: Design a custom architecture or rule pack

Use this when the task needs project-specific rules, fixed-versus-overrideable request contracts, or house-rule layers on top of the canonical architecture families.

```bash
python3 scripts/codex_studio.py next "Design a custom architecture and rule pack for project-specific inventory overrides"
python3 scripts/codex_studio.py checklist --task "Design a custom architecture and rule pack for project-specific inventory overrides"
```

Then read:

- `docs/reference/custom-architecture.md`
- `docs/examples/custom-architecture-example.md`
- `docs/research/game-development/foundations/custom-architecture.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/agent-system.md`

Keep the brief explicit about:

- the request source
- fixed versus overrideable rules
- the canonical owner
- precedence order
- fallback behavior
- one narrow proof path

If the work needs a reusable registry of custom feature bundles instead of one custom contract, start with `docs/reference/custom-packs.md` and `docs/examples/custom-packs-example.md` first.

## Recipe: Design a custom pack registry

Use this when the task needs reusable project-specific feature bundles, named registry rows, or fallback behavior that should stay reviewable later.

```bash
python3 scripts/codex_studio.py next "Design a custom pack registry for project-specific inventory and UI overrides"
python3 scripts/codex_studio.py checklist --task "Design a custom pack registry for project-specific inventory and UI overrides"
```

Then read:

- `docs/reference/custom-packs.md`
- `docs/examples/custom-packs-example.md`
- `docs/research/game-development/foundations/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/architecture-guide.md`

Keep the brief explicit about:

- pack type
- owner
- fixed rules
- overrideable rules
- hook points
- fallback behavior
- one narrow proof path

## Recipe: Design an extension pack

Use this when the task needs optional capability surfaces, plugin-like add-ons, or hook packs that should sit beside the canonical architecture.

```bash
python3 scripts/codex_studio.py next "Design a custom extension pack for inventory hooks and UI panels"
python3 scripts/codex_studio.py checklist --task "Design a custom extension pack for inventory hooks and UI panels"
```

Then read:

- `docs/reference/extensions-guide.md`
- `docs/examples/extensions-example.md`
- `docs/research/game-development/foundations/extensions.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/architecture-guide.md`

Keep the brief explicit about:

- the request source
- manifest fields
- hook points
- override points
- fallback behavior
- one narrow proof path

## Recipe: Prepare for an audio and animation presentation pass

Use this when a feature needs sound cues, animation timing, or synchronized presentation but the gameplay truth should stay elsewhere.

```bash
python3 scripts/codex_studio.py next "Run an audio and animation pass on a Unity 6 inventory HUD and name the sync owner"
python3 scripts/codex_studio.py checklist --task "Run an audio and animation pass on a Unity 6 inventory HUD and name the sync owner"
```

Then read:

- `docs/reference/audio-animation-guide.md`
- `docs/examples/audio-animation-example.md`
- the matching engine presentation note in `docs/research/game-development/engines/`

Keep the brief explicit about:

- playback owner
- timing owner
- gameplay owner
- sync surface
- proof path

## Recipe: Prepare a UI architecture and template pass

Use this when the task is a HUD, menu, settings, onboarding, inventory UI, or template-selection decision.

```bash
python3 scripts/codex_studio.py next "Design a controller-first pause menu in Unity 6 and name the template source"
python3 scripts/codex_studio.py checklist --task "Design a controller-first pause menu in Unity 6 and name the template source"
```

Then read:

- `docs/reference/ui-guide.md`
- `docs/examples/ui-example.md`
- the matching engine UI note in `docs/research/game-development/engines/`

Keep the brief explicit about:

- screen owner
- projected data owner
- focus and navigation owner
- template or starter source
- validation path for keyboard, controller, and pointer

## Recipe: Build world graph or lorebook support

Use this when the task affects canon, codices, faction histories, relationship networks, or timeline-driven world state.

```bash
python3 scripts/codex_studio.py next "Design a world graph that keeps faction history queryable without making dialogue own canon"
python3 scripts/codex_studio.py checklist --task "Design a world graph that keeps faction history queryable without making dialogue own canon"
python3 scripts/codex_studio.py research --category narrative --title "World graph relationship and history architecture"
```

Then read:

- `docs/reference/world-graph-methodology.md`
- `docs/reference/lorebook-methodology.md`
- `docs/research/game-development/narrative/world-graph.md`
- `docs/research/game-development/narrative/lorebook.md`

Keep the brief explicit about:

- canonical node types
- canonical edge types
- append-only history versus snapshot state
- which system owns runtime deltas
- the fast read path for the common graph query

## Recipe: Coordinate a broad task with a master mind loop

Use this when the request is broad, cross-functional, or likely to split across specialist workers.

```bash
python3 scripts/codex_studio.py next "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs"
python3 scripts/codex_studio.py checklist --task "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs"
```

Then read:

- `docs/reference/mastermind-guide.md`
- `docs/examples/mastermind-example.md`
- `docs/research/game-development/foundations/mastermind.md`

Keep the brief explicit about:

- the simple user summary
- the control loop
- the specialist handoffs
- the narrow validation path
- the durable doc update if the change affects repo behavior

## Recipe: Prepare the agent operating model

Use this when you need the repo's multi-agent operating model to stay explicit while single-specialist mode remains available.

```bash
python3 scripts/codex_studio.py next "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail"
python3 scripts/codex_studio.py checklist --task "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail"
```

Then read:

- `docs/reference/agent-system.md`
- `docs/examples/agent-system-example.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/prompt-journal.md`

Keep the brief explicit about:

- the controller title
- the single-specialist default
- the role matrix or panel choice
- the command tree if reporting lines matter
- the prompt history or review trail
- the narrow validation path

## Recipe: Prepare an OpenAI/Codex agent workflow

Use this when the task is about OpenAI, Codex, prompt steering, traceable evals, or agent-platform wiring.

```bash
python3 scripts/codex_studio.py next "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals"
python3 scripts/codex_studio.py checklist --task "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals"
```

Then read:

- `docs/research/openai-codex-infra-findings.md`
- `docs/reference/codex-compatibility.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `studio/checklists/discipline/openai_codex.toml`
- `studio/docs/active/eval-openai-codex.md`
- `docs/reference/quality-process.md`
- `docs/reference/benchmark-guide.md`
- `docs/reference/prompt-journal.md`

Keep the brief explicit about:

- the stable policy versus the task-specific prompt text
- the prompt version or prompt object if the work leaves the repo
- the eval path or trace grading path
- the tool-approval and internet-access assumptions
- the narrow validation path

## Recipe: Choose a Codex model or plan tier

Use this when the task is about model choice, reasoning level, subscription fit, or API-versus-ChatGPT surface decisions.

```bash
python3 scripts/codex_studio.py next "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor"
python3 scripts/codex_studio.py checklist --task "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor"
```

Then read:

- `docs/research/openai-codex-models.md`
- `docs/reference/codex-model-guide.md`
- `docs/research/openai-codex-infra-findings.md`
- `docs/reference/codex-compatibility.md`
- `studio/checklists/discipline/openai_models.toml`
- `studio/docs/active/eval-openai-models.md`

Keep the brief explicit about:

- the surface: ChatGPT/Codex app or API
- the selected model
- the reasoning level
- the plan tier if relevant
- the fallback if the first choice is too slow, too costly, or too weak

## Recipe: Assign sub-agent models

Use this when the task fans out into specialists and the user wants to override the default lane model for one or more agents.

```bash
python3 scripts/codex_studio.py next "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini
python3 scripts/codex_studio.py checklist --task "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini
```

Then read:

- `docs/reference/codex-model-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/research/openai-codex-models.md`
- `docs/research/openai-codex-infra-findings.md`

Keep the brief explicit about:

- the default model from each agent profile
- the explicit override for each selected lane
- the controller model if the task also uses a controller
- the narrow validation path

## Recipe: Choose a single specialist or a small panel

Use this when the request is about the agent system itself or when you need to decide whether a task should stay single-agent, pair up, or fan out into a small panel.

```bash
python3 scripts/codex_studio.py next "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode"
python3 scripts/codex_studio.py checklist --task "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode"
```

Then read:

- `docs/reference/agent-portfolio.md`
- `docs/reference/mastermind-guide.md`
- `docs/examples/agent-portfolio-example.md`
- `docs/research/game-development/foundations/agent-portfolio.md`

Keep the brief explicit about:

- the controller mode
- the specialist lane for each agent
- what each lane does not own
- the narrow validation path

## Recipe: Build a command tree

Use this when the request needs titles, reporting lines, or async status packets, but single specialist mode should still remain available if the scope shrinks.

```bash
python3 scripts/codex_studio.py next "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane"
python3 scripts/codex_studio.py checklist --task "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane"
```

Then read:

- `docs/reference/agent-hierarchy.md`
- `docs/examples/agent-hierarchy-example.md`
- `docs/research/game-development/foundations/agent-hierarchy.md`

Keep the brief explicit about:

- the controller tier
- the public title for each lane
- the parent tier for each lane
- the async status packet
- the narrow validation path

## Recipe: Rename or simplify names

Use this when a doc, example, checklist, preset, or script name is too long or drifted from the short canonical form.

```bash
python3 scripts/doc_sync_audit.py --json
python3 scripts/validate_docs.py
```

Then keep these in the same change:

- the file name itself
- incoming links from README or repo tour pages
- any checklist references to the renamed surface
- any validation surface that mentions the old name

## Recipe: Prepare for a quality control pass

Use this when code quality, maintainability, or optimization criteria are the real question and you need the operating loop, not only the rubric.

```bash
python3 scripts/codex_studio.py next "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate"
python3 scripts/codex_studio.py checklist --task "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate"
```

Then decide explicitly:

- the runtime owner, data owner, and editor owner
- the quality-control process step, evidence artifact, and go/no-go gate
- the validation path
- the baseline and first lever if optimization is part of the task

Also read:

- `docs/reference/quality-guide.md`
- `docs/reference/quality-process.md`
- `docs/examples/quality-example.md`
- `docs/examples/quality-process-example.md`
- `docs/reference/code-review.md`
- `docs/reference/code-review.md`
- the matching engine class atlas
- the matching engine performance note if tuning is involved

## Recipe: Build a theory stack

Use this when the task needs a durable lens stack before design or implementation and the team wants the player outcome, lens order, and evidence path explicit.

```bash
python3 scripts/codex_studio.py next "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses"
python3 scripts/codex_studio.py checklist --task "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses"
```

Then read:

- `docs/reference/theory-guide.md`
- `docs/examples/theory-example.md`
- `docs/research/game-development/foundations/theory.md`
- `docs/research/game-development/foundations/frameworks.md`
- `docs/research/game-development/foundations/ux.md`
- `docs/research/game-development/foundations/balance.md`
- `docs/research/game-development/foundations/quality.md`
- `studio/checklists/discipline/theory.toml`
- `studio/docs/active/eval-theory.md`

Keep the brief explicit about:

- the player outcome
- the dominant tension
- the minimum lens stack
- the evidence source for each lens
- the first failure mode
- the narrow validation path

## Recipe: Prepare for a benchmark pass

Use this when you want to compare route accuracy, checklist quality, docs sync, or a custom harness against a named benchmark family.

```bash
python3 scripts/codex_studio.py next "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio"
python3 scripts/codex_studio.py checklist --task "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio"
python3 scripts/scaffold_eval_plan.py "Benchmark Routing"
python3 scripts/run_bench.py --json
```

Then decide explicitly:

- the benchmark family
- the baseline
- the metric
- the threshold
- the artifact path
- whether the case belongs to a ready-made family or the repo-local suite

Also read:

- `docs/reference/benchmark-guide.md`
- `docs/examples/benchmark-example.md`
- `docs/research/game-development/foundations/benchmarks.md`
- `docs/reference/eval-strategy.md`

## Recipe: Prepare for a performance pass

Use this when FPS, memory, or scale is becoming risky.

```bash
python3 scripts/codex_studio.py next "Run a performance pass on enemy projectile scale"
python3 scripts/codex_studio.py checklist --task "Run a performance pass on enemy projectile scale"
python3 scripts/scaffold_feature.py "Projectile Scale Perf Pass" --with-test-plan --with-eval-plan
```

Then decide explicitly:

- the target hardware and baseline
- the first lever before micro-optimization
- representation choice
- contact model
- measurement path
- rollback plan if the optimization is not worth it

Also read:

- `docs/reference/perf-guide.md`
- `docs/examples/perf-example.md`
- the matching engine performance note

## Recipe: Prepare for a genre-specific performance pass

Use this when the genre itself is the main source of scale pressure.

```bash
python3 scripts/codex_studio.py next "Run a performance pass on a survivorlike and cap active enemies before changing combat logic"
python3 scripts/codex_studio.py checklist --task "Run a performance pass on a city-builder and chunk simulation before adding more AI detail"
```

Then decide explicitly:

- the genre family
- the dominant pressure
- the first genre lever
- the fallback lever if the first one does not move the needle
- whether the problem is still genre-shaped after the first pass

Also read:

- `docs/reference/genre-perf-guide.md`
- `docs/examples/genre-perf-example.md`
- `docs/reference/perf-guide.md`
- `docs/examples/perf-example.md`
- the matching engine performance note

## Recipe: Prepare for a genre pattern pass

Use this when the team already knows the genre family but needs the software pattern family, contrast set, and first slice shape before implementation.

```bash
python3 scripts/codex_studio.py next "Research genre software patterns and contrast sets for a deckbuilder roguelike before implementation"
python3 scripts/codex_studio.py checklist --task "Research genre software patterns and contrast sets for a deckbuilder roguelike before implementation"
```

Then decide explicitly:

- the dominant genre tension
- the software pattern family that should own the loop
- the example games that prove the pattern is real
- the first slice and the first failure mode
- the ownership boundary between runtime, projection, and tooling

Also read:

- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-examples.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `docs/reference/genre-presets.md`

## Recipe: Prepare for an advanced optimization pass

Use this when the scale question is about culling, partitioning, batching, instancing, job systems, or state compression rather than basic FPS tuning.

```bash
python3 scripts/codex_studio.py next "Research advanced optimization algorithms for a Godot 4 survivorlike and decide whether spatial hashing or MultiMesh is the first lever"
python3 scripts/codex_studio.py checklist --task "Research advanced optimization algorithms for a Unity 6 city-builder and compare Burst jobs with occlusion culling"
```

Then decide explicitly:

- the algorithm family
- the baseline measurement
- the first algorithmic lever
- the fallback lever if the first one does not move the needle
- the validation path that proves the algorithm choice beat the alternatives

Also read:

- `docs/reference/advanced-perf-guide.md`
- `docs/examples/advanced-perf-example.md`
- `docs/reference/perf-guide.md`
- `docs/reference/genre-perf-guide.md`
- the advanced_performance and performance checklist layers
- the matching engine performance note

## Recipe: Prepare for a GPU pass

Use this when the task is about GPU ownership, render-side representation, repeated visuals, or CPU-GPU communication.

```bash
python3 scripts/codex_studio.py next "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever"
python3 scripts/codex_studio.py checklist --task "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever"
```

Then decide explicitly:

- the CPU owner
- the GPU owner
- the upload path
- the readback policy
- the first lever

Also read:

- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- the matching engine GPU note

## Recipe: Prepare for a library selection pass

Use this when the task is about choosing the smallest official library, package, plugin, or SDK for a specific case.

```bash
python3 scripts/codex_studio.py next "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow"
python3 scripts/codex_studio.py checklist --task "Choose the smallest official library set for a Godot 4 stealth prototype with input, navigation, and save"
```

Then decide explicitly:

- the case
- the built-in option
- the official package or plugin if the built-in option is not enough
- the fallback if no external dependency is actually needed
- the validation loop that proves the chosen stack is enough

Also read:

- `docs/reference/library-guide.md`
- `docs/examples/library-example.md`
- `docs/reference/engine-selection-guide.md`
- the library and research checklist layers
- the matching engine or package docs

## Recipe: Prepare for an asset pipeline pass

Use this when source art, import rules, compression, shared tuning, or streamable libraries are the real question.

```bash
python3 scripts/codex_studio.py next "Compare Godot Resource, PackedScene, and imported texture ownership for a HUD icon set"
python3 scripts/codex_studio.py checklist --task "Compare Unity ScriptableObject, Sprite Atlas, and Addressables for inventory art"
```

Then decide explicitly:

- the source asset
- the runtime owner
- the shared data owner
- the import or load boundary
- the compression, atlas, or packaging rule
- the validation loop that proves the chosen alternative is safe

Also read:

- `docs/reference/asset-guide.md`
- `docs/examples/asset-example.md`
- `docs/research/game-development/assets/README.md`
- `docs/research/game-development/production/content-pipeline.md`

## Recipe: Validate the engine contract before real work

Godot:

```bash
python3 scripts/godot_smoke.py --static-only
```

Unity:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --dry-run --json
```

Unreal:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

Unity auto-detects standard local editor installs when possible. If no local editor is present, add `--unity-path tools/engine-stubs/unity/Unity` for contract shape only. Keep the Unreal stub command for contract smoke unless a real `UNREAL_UAT` or `UNREAL_EDITOR` path is available.

## Recipe: Compare the same mechanic across engines

Use this when you want concrete examples instead of abstract engine advice.

```bash
python3 scripts/codex_studio.py next "Compare the best Godot, Unity, and Unreal ownership model for a controller-first upgrade screen"
python3 scripts/codex_studio.py next "Show me the concrete 2D and 3D class choices for a stealth prototype in each engine"
python3 scripts/codex_studio.py next "List the best starter slice for a combat room in Godot, Unity, and Unreal and explain the differences"
```

Then read:

- `docs/reference/engine-examples.md`
- `docs/reference/engine-selection-guide.md`
- `docs/reference/system-atlas.md`
- the engine-specific `*-class-editor-object-map.md` and `*-systems-playbook.md` notes

## Recipe: Pre-merge confidence pass

Use this before calling a shared change "done".

```bash
python3 scripts/validate_docs.py
python3 scripts/validate_repo_layout.py
python3 scripts/run_local_evals.py --json
python3 -m pytest -q tests
make ci-local
```

## Recipe: Prepare a release-readiness bundle

Use this when you want a structured review package before an external demo or milestone branch.

```bash
make ci-report
python3 scripts/ci_artifact_report.py --output-dir build/ci/manual-release --label release-readiness --json
```

Then review:

- `build/ci/manual-release/ci-report.json`
- `build/ci/manual-release/ci-report.md`

If this bundle is part of a naming simplification, keep the workflow name, job labels, artifact labels, and report filenames short and canonical so the CI short-name rule stays visible in the release path.
Release bundles also pull in the build-release checklist, so keep the release and packaging vocabulary aligned instead of letting them diverge.

## Recipe: Prepare a release hardening bundle

Use this when the release needs code protection, symbol policy, or a multiplayer trust boundary before shipping.

```bash
python3 scripts/codex_studio.py next \
  "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split"
python3 scripts/codex_studio.py checklist \
  --task "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split"
```

Then read:

- `docs/reference/release-hardening-guide.md`
- `docs/examples/release-hardening-example.md`
- `docs/research/game-development/production/release-hardening.md`
- `studio/docs/templates/release-hardening.md`
- `studio/checklists/discipline/release_hardening.toml`
- `studio/docs/active/eval-release-hardening.md`

Keep the brief explicit about:

- build integrity
- code protection
- multiplayer trust boundary
- symbol policy
- rollback owner

## Recipe: Prepare a versioning bundle

Use this when the repo version, changelog, and release tag policy need to move together.

Before making changes, compare `docs/reference/version-guide.md`, `docs/examples/version-example.md`, and `docs/research/game-development/production/versioning.md` so the version file, changelog, and tag policy stay in the same contract.
Draft the commit subject and body at the same time so the version bump, changelog entry, and commit note tell the same story.

```bash
python3 scripts/version_guard.py --json
make version
python3 scripts/ci_artifact_report.py --output-dir build/ci/version --label version-check --json
```

Then review:

- `VERSION`
- `CHANGELOG.md`
- `build/ci/version/version-report.json`
- `build/ci/version/version-report.md`

If the repo is still in prerelease mode, keep `Unreleased` visible in the changelog and make sure the tag policy is documented instead of pretending the release already exists.
If the versioning bundle is more than a single-file metadata tweak, use a commit body that says what changed before tagging.

## Recipe: Track current sector signals

Use this when the task needs current game-industry, platform, or market signals instead of implementation work.

```bash
python3 scripts/codex_studio.py next "Summarize the current game-industry signals that matter for a Steam-first indie survival game"
python3 scripts/codex_studio.py checklist --task "Track current sector signals for a Steam-first indie survival game"
```

Then read:

- `docs/reference/sector-intel.md`
- `docs/examples/sector-intel-example.md`
- `docs/research/game-development/production/sector-intel.md`

Keep the brief explicit about:

- source hierarchy
- current window
- signal
- implication
- next action

## Recipe: Track Steam store signals

Use this when the task is specifically about Steam store traffic, wishlists, community themes, or hardware mix instead of broader sector work.

```bash
python3 scripts/codex_studio.py next "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game"
python3 scripts/codex_studio.py checklist --task "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game"
```

Then read:

- `docs/reference/steam-intel.md`
- `docs/examples/steam-intel-example.md`
- `docs/research/game-development/production/steam-intel.md`
- `docs/reference/sector-intel.md`
- `docs/reference/marketing-guide.md`

Keep the brief explicit about:

- source family
- current window
- store traffic
- wishlist flow
- forum themes
- hardware mix
- chart pack
- next action

## Recipe: Track platform compatibility

Use this when the task is about family-by-family compatibility across Windows, macOS, Linux/Steam Deck, web, Android/iOS, or TV/webOS instead of only one narrow port.

```bash
python3 scripts/codex_studio.py next "Map platform compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS"
python3 scripts/codex_studio.py checklist --task "Map platform compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS"
```

Then read:

- `docs/reference/platform-guide.md`
- `docs/examples/platform-example.md`
- `docs/research/game-development/production/platform-compatibility.md`
- `docs/research/game-development/production/platform.md`
- `studio/docs/active/platform-targets.md`

Keep the brief explicit about:

- source hierarchy
- platform family split
- input model
- performance envelope
- policy or store constraints
- dashboard pack
- next action

## Recipe: Plan cross-platform support tiers

Use this when the task needs support tiers, release sequencing, or an explicit core/supported/demo/research/deferred split instead of only a compatibility matrix.

```bash
python3 scripts/codex_studio.py next "Turn our platform targets into a support-tier matrix and release order card"
python3 scripts/codex_studio.py checklist --task "Turn our platform targets into a support-tier matrix and release order card"
```

Then read:

- `docs/reference/cross-platform-guide.md`
- `docs/examples/cross-platform-example.md`
- `docs/research/game-development/production/cross-platform.md`
- `docs/reference/platform-guide.md`
- `docs/examples/platform-example.md`
- `docs/research/game-development/production/platform-compatibility.md`
- `studio/docs/active/platform-targets.md`

Keep the brief explicit about:

- source hierarchy
- support tier per family
- release order
- input, session, save, policy, packaging, and performance deltas
- dashboard pack
- next action

## Recipe: Plan console premium readiness

Use this when a task is about PS5-like, Xbox-like, or Switch-like support and needs controller-first UX, suspend/resume, save / entitlement, or submission evidence before implementation starts.

```bash
python3 scripts/codex_studio.py next "Plan console premium readiness for a PS5-like port"
python3 scripts/codex_studio.py checklist --task "Plan console premium readiness for a PS5-like port"
```

Then read:

- `docs/reference/console-guide.md`
- `docs/examples/console-example.md`
- `docs/research/game-development/production/console.md`
- `studio/checklists/discipline/console.toml`
- `studio/docs/active/eval-console.md`
- `studio/docs/templates/cert-checklist.md`
- `studio/docs/templates/platform-targets.md`

Keep the brief explicit about:

- source hierarchy
- console family split
- controller-first UX
- suspend/resume
- save / entitlement
- submission gate
- dashboard pack
- next action

## Recipe: Plan a marketing strategy

Use this when you need a strategy decision instead of a one-off launch beat.

```bash
python3 scripts/codex_studio.py next "Build a marketing strategy for a Steam-first indie survival game"
python3 scripts/codex_studio.py checklist --task "Build a marketing strategy for a Steam-first indie survival game"
```

Then read:

- `docs/reference/marketing-guide.md`
- `docs/examples/marketing-example.md`
- `docs/research/game-development/production/marketing.md`
- `docs/reference/sector-intel.md`

Keep the brief explicit about:

- objective
- audience
- channel fit
- asset readiness
- measurement path
- policy constraints

## Recipe: Review current marketing status

Use this when you need the current marketing picture as numbers, trends, and chart families instead of strategy.

```bash
python3 scripts/codex_studio.py next "Turn the latest marketing signals into a chart pack and one recommendation"
python3 scripts/codex_studio.py checklist --task "Turn the latest marketing signals into a chart pack and one recommendation"
```

Then read:

- `docs/reference/marketing-intel.md`
- `docs/examples/marketing-intel-example.md`
- `docs/research/game-development/production/marketing-intel.md`
- `docs/reference/marketing-guide.md`
- `docs/reference/steam-intel.md`
- `docs/reference/sector-intel.md`

Keep the brief explicit about:

- source family
- current window
- baseline
- chart pack
- one repo implication

## Recipe: Daily operator loop

This is a good default daily rhythm:

1. `python3 scripts/codex_studio.py doctor`
2. open `studio/docs/active/current-sprint.md`
3. route the next task
4. resolve the checklist for the same task
5. touch the minimum docs required for that task
6. keep one validation path green while you work
7. end with `python3 scripts/run_local_evals.py`

## Recipe: New contributor handoff

Use this when someone new joins the repo.

Ask them to read:

1. `README.md`
2. `docs/setup/getting-started.md`
3. `docs/setup/first-hour-walkthrough.md`
4. `docs/reference/engine-selection-guide.md`
5. `docs/reference/command-cheatsheet.md`
6. `studio/docs/active/game-brief.md`
7. `studio/docs/active/engine-profile.md`

Then ask them to run:

```bash
python3 scripts/codex_studio.py doctor
python3 scripts/codex_studio.py engine --list --json
python3 scripts/codex_studio.py next "Summarize the most credible next task for this repo"
```
