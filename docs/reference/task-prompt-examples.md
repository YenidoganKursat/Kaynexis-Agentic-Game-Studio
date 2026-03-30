# Task And Prompt Examples

This repo works best when tasks are concrete.

The goal is not to write fancy prompts. The goal is to give Codex enough shape to route, checklist, and validate the work correctly.

## Strong task patterns

Good tasks usually include at least two of these:

- the player or system outcome
- the engine or platform context
- the constraint
- the validation goal

Example:
- "Implement a readable dodge cancel window for the first Godot combat room."
- "Design a Unity-friendly save-state ownership model for mission progress."
- "Prepare the first Unreal Win64 packaging path and document the constraints."
- "Rename the long-form example docs to short canonical names and keep every link surface updated in the same change."
- "Keep CI workflow names, job labels, artifact labels, and report filenames short and canonical while refreshing the release docs."
- "Record the prompt history and one agent journal entry for this task so the user can review it later."

## Speed pack / fast path

If the task is urgent or narrow, ask for the speed pack instead of a full orchestration bundle.
Start with `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, and `docs/setup/quick-access.md` so the router can keep the bundle short and the proof path obvious.

Good examples:

- "Give me the speed pack for a short HUD fix and keep the proof path minimal."
- "Route this task through the fastest safe bundle and do not fan out unless needed."
- "Prepare the smallest reviewable bundle for a narrow gameplay fix."

```bash
python3 scripts/codex_studio.py next \
  "Give me the speed pack for a short HUD fix and keep the proof path minimal"

python3 scripts/codex_studio.py checklist \
  --task "Route this task through the fastest safe bundle and do not fan out unless needed"
```

## Capability catalog

If the task is about the repo's full capability surface, keep the summary broad but the output simple.
Start with `docs/reference/capabilities.md`, `docs/examples/capabilities-example.md`, and `docs/research/game-development/foundations/capabilities.md` so the answer can name the major families before it dives into a narrower lane.

Good examples:

- "Summarize everything this studio can do and point me at the right starting docs for each lane."
- "Turn the repo's capability surface into a one-page intro for a new contributor."
- "Show me the studio capability catalog and the shortest starting docs for each family."

```bash
python3 scripts/codex_studio.py next \
  "Summarize everything this studio can do and point me at the right starting docs for each lane"

python3 scripts/codex_studio.py checklist \
  --task "Show me the studio capability catalog and the shortest starting docs for each family"
```

## Lorebook and narrative

If the task is about canon, lorebooks, world knowledge, or story bible work, include the stability rule and the unlock rule up front.
Start with `docs/reference/lorebook-methodology.md` when the task is about durable canon and unlockable lore.

Example:

- "Design a lorebook flow that keeps faction canon stable while quest unlocks change between runs."

If the task is system-heavy, mention the system atlas entry or the engine class family explicitly so the router can land on the right ownership docs first.

## World graph and history

If the task is about relationship graphs, faction networks, world history, or organizational structure, include the ownership rule, append-only rule, and fast-path rule up front.
Start with `docs/reference/world-graph-methodology.md` when the task is about durable relationships and history projections.

Example:

- "Design a world graph flow that keeps faction history queryable without making every dialogue line own the canon."

Example:

- "Use the world graph methodology to design a faction network with stable ids, append-only history, and cached codex reads."

Example:

- "Use the game systems atlas and Unity class atlas to design an inventory UI that separates item definitions, slot state, and persistence."

## Master Mind / orchestration

If the task is broad, cross-functional, or likely to split across specialist workers, include the control loop, handoff roles, and narrow validation path up front.
Start with `docs/reference/mastermind-guide.md` and `docs/examples/mastermind-example.md` when the work needs a controller-style summary instead of a single-specialist prompt.

Good examples:

- "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs."
- "Run the master mind loop on a routing change and keep the user-facing answer short."
- "Break a broad request into specialist tasks, then report one simple summary plus the validation path."

```bash
python3 scripts/codex_studio.py next "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs"
python3 scripts/codex_studio.py checklist --task "Run the master mind loop on a routing change and keep the user-facing answer short"
```

## Agent system / operating model

If the task is about the repo's overall multi-agent operating model, include the controller title, the single-specialist default, the role matrix, the hierarchy, and the review trail up front.
Start with `docs/reference/agent-system.md` and `docs/examples/agent-system-example.md` when the work is about the whole operating model instead of one lane.

Good examples:

- "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail."
- "Keep the single specialist path visible while you make the controller title, role matrix, and command tree explicit."
- "Define the smallest operating model that still keeps the prompt history durable later."

```bash
python3 scripts/codex_studio.py next "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail"
python3 scripts/codex_studio.py checklist --task "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail"
```

## OpenAI / Codex / agent platform

If the task is about OpenAI or Codex, include the prompt policy, the eval path, and the tool-access assumptions up front.
Start with `docs/research/openai-codex-infra-findings.md`, `docs/reference/codex-compatibility.md`, and `docs/reference/agent-system.md` when the work is about the agent platform instead of one lane.
If you need a checklist bundle or eval trail, surface `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` alongside the routed docs.

Good examples:

- "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals."
- "Define the smallest OpenAI-aligned agent loop that keeps system instructions stable, task details in user prompts, and trace grading in the loop."
- "Update the Codex routing rules so the controller keeps the single specialist default visible while allowing a small panel when needed."

```bash
python3 scripts/codex_studio.py next "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals"
python3 scripts/codex_studio.py checklist --task "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals"
```

## OpenAI / Codex / model selection

If the task is about choosing a model or a ChatGPT / Codex plan tier, include the surface, the model, the reasoning level, and the fallback up front.
Start with `docs/research/openai-codex-models.md` and `docs/reference/codex-model-guide.md` when the work is about fit, latency, cost, or access instead of one lane.
If the task fans out into specialists, also let the user override lane models explicitly with `--agent-model agent=model` so sub-agent tradeoffs stay visible.
If you need a checklist bundle or eval trail, surface `studio/checklists/discipline/openai_models.toml` and `studio/docs/active/eval-openai-models.md` alongside the routed docs.

Good examples:

- "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor."
- "Compare GPT-5.4, GPT-5.4-mini, GPT-5.4-nano, and GPT-5.4-pro for a routing agent."
- "Select the best OpenAI model for a cheap high-volume extraction pass and explain why the others are worse."
- "Override `qa_lead` to `gpt-5.4-mini` and `technical_director` to `gpt-5.4-pro` when a multi-agent panel needs asymmetric tradeoffs."

```bash
python3 scripts/codex_studio.py next "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor"
python3 scripts/codex_studio.py checklist --task "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor"
python3 scripts/codex_studio.py next "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini
```

## Agent portfolio / role matrix

If the task is about the agent system itself, or if you need to choose between a single specialist, a paired handoff, or a small multi-agent panel, include the controller mode and the narrow lane for each role up front.
Start with `docs/reference/agent-portfolio.md` and `docs/examples/agent-portfolio-example.md` when the work is about role boundaries instead of a single feature.

Good examples:

- "Define a role matrix for the agent system so each specialist stays narrow."
- "Choose single specialist versus multi-agent panel mode for a broad repo task."
- "Map producer, technical director, docs researcher, and qa roles to one broad orchestration request."
- "Assign the Kaynexis controller title and scientist public titles to the agent roles so the user-facing summary stays readable."

```bash
python3 scripts/codex_studio.py next "Define a role matrix for the agent system so each specialist stays narrow"
python3 scripts/codex_studio.py checklist --task "Choose single specialist versus multi-agent panel mode for a broad repo task"
```

## Agent hierarchy / command tree

If the task needs titles, reporting lines, or async packets, include the controller, the parent tier, and the lane title up front while keeping single specialist mode available.
Start with `docs/reference/agent-hierarchy.md` and `docs/examples/agent-hierarchy-example.md` when the work is about command structure instead of only a role matrix.

Good examples:

- "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane."
- "Assign the Kaynexis controller title, scientist public titles, and reporting lines for an async multi-agent panel without losing the single specialist fallback."
- "Design the agent hierarchy so every lane reports upward through one owner."

```bash
python3 scripts/codex_studio.py next "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane"
python3 scripts/codex_studio.py checklist --task "Assign the Kaynexis controller title, scientist public titles, and reporting lines for an async multi-agent panel without losing the single specialist fallback"
```

## Prompt journal

If the task should be easy to review later, include the user prompt, the route, the short outcome, and one agent step note before the chat closes.
Start with `docs/reference/prompt-journal.md` and `docs/examples/prompt-journal-example.md` when the task needs a durable review trail instead of only an ephemeral chat memory.

Good examples:

- "Append this user request to prompt history and add one agent journal entry after validation."
- "Record the route, summary, and review path for this task so the user can reopen it later."
- "Write a short agent journal note with expectation, found, improvement, and evaluation."

```bash
python3 scripts/codex_studio.py journal prompt \
  --prompt "Record prompt history and one agent note for the current task." \
  --route "prompt history / agent journal" \
  --summary "Created append-only journal sections." \
  --json

python3 scripts/codex_studio.py journal agent \
  --step "Draft the journal template and journal command" \
  --expected "One active file with two append-only sections" \
  --found "The repo had no durable history trail yet" \
  --improved "Added a shared prompt journal file and append helper" \
  --evaluation "The review trail is now easy to reopen later" \
  --json
```

## Agent transcript

If the task fans out into worker handoffs or agent-to-agent replies, capture the assignment history and the conversation turns in a separate transcript.
Start with `docs/reference/agent-transcript.md` and `docs/examples/agent-transcript-example.md` when the task needs a durable transcript instead of only prompt history.

Good examples:

- "Record the task assignment history and keep the conversation transcript append-only."
- "Append a short agent-to-agent transcript entry for this handoff."
- "Store the assignment and reply history so the user can reopen the thread later."

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

## Agent execution packet

If the task needs a pre-flight contract, include the owner, operating mode, proof path, custom rules, and stop conditions up front.
Start with `docs/reference/agent-execution.md` and `docs/examples/agent-execution-example.md` when you want the task shape to stay compact before work starts.

Good examples:

- "Build an execution packet for a UI refactor with one owner and one proof path."
- "Write the work packet that keeps custom rules, stop conditions, and validation visible."
- "Define the smallest packet that still lets this task be reopened later."

```bash
python3 scripts/codex_studio.py packet \
  --task "Build an execution packet for a UI refactor" \
  --owner "Kaynexis" \
  --mode "single-specialist" \
  --goal "Keep the refactor narrow and reviewable" \
  --route "agent execution / work packet"
```

## Agent validation matrix

If the task needs proof that a single specialist, pair, or panel was the right operating choice, use a validation matrix instead of burying the decision in chat.
Start with `docs/reference/agent-validation-matrix.md` and `docs/examples/agent-validation-matrix-example.md` when the task needs the proof rows to stay separate from prompt history and transcript history.

Good examples:

- "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible."
- "Show the operating mode, proof rows, and model override checks in one compact bundle."
- "Keep the validation matrix small enough that another operator can replay it later."

```bash
python3 scripts/codex_studio.py next "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
python3 scripts/codex_studio.py checklist --task "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
```

## Theory stack

If the task needs a durable design-lens stack before implementation, include the player outcome, the lens order, the evidence source, and the first failure mode up front.
Start with `docs/reference/theory-guide.md`, `docs/examples/theory-example.md`, and `docs/research/game-development/foundations/theory.md` when the work is about a theory stack instead of one feature slice.

Good examples:

- "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses before implementation."
- "Review a combat room for affordance, cognitive load, and feedback order before the first refactor."
- "Create a theory pack for a cozy sim progression loop and identify the player outcome, friction budget, and validation path."

```bash
python3 scripts/codex_studio.py next "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses"
python3 scripts/codex_studio.py checklist --task "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses"
```

## Architecture

If the task is about state ownership, authority, event flow, projection, or phase graphs, include the owner, boundary, and proof path up front.
Start with `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` when the task is about durable architecture decisions. Use the diagrams first if you need a quick owner/boundary map, and name the checklist evidence when the task is broad enough to need a hierarchy or multi-step proof path.

Good examples:

- "Design a boss phase authority model that keeps HUD and save projection separate."
- "Design an event layer for combat feedback without moving rule ownership into the UI."
- "Design a state graph for stealth detection, alertness, and recovery."

```bash
python3 scripts/codex_studio.py next "Design a boss phase authority model that keeps HUD and save projection separate"
python3 scripts/codex_studio.py checklist --task "Design a boss phase authority model that keeps HUD and save projection separate"
```

## Custom architecture and rule packs

If the task is about project-specific architecture, house rules, or overrideable request contracts, include the fixed rules, overrideable rules, precedence, and fallback up front.
Start with `docs/reference/custom-architecture.md` and `docs/examples/custom-architecture-example.md` when the task needs a durable custom contract instead of a one-off chat answer.

Good examples:

- "Design a custom architecture and rule pack for project-specific inventory overrides."
- "Define a custom request contract that lets designers change pacing rules without changing canonical combat ownership."
- "Build a custom rule layer for a mod-friendly UI flow while keeping the projection boundary explicit."

```bash
python3 scripts/codex_studio.py next "Design a custom architecture and rule pack for project-specific inventory overrides"
python3 scripts/codex_studio.py checklist --task "Define a custom request contract that lets designers change pacing rules without changing canonical combat ownership"
```

## Custom packs

If the task is about reusable custom feature bundles, registry rows, or pack families that sit above a narrower custom contract, include the pack type, owner, fixed rules, overrideable rules, hook points, and fallback up front.
Start with `docs/reference/custom-packs.md` and `docs/examples/custom-packs-example.md` when the task needs a durable pack registry instead of a one-off custom answer.

Good examples:

- "Design a custom pack registry for project-specific inventory and UI overrides."
- "Define a feature pack that combines fixed combat rules with overrideable progression hooks."
- "Build a custom pack contract that keeps the fallback explicit when an optional hook is missing."

```bash
python3 scripts/codex_studio.py next "Design a custom pack registry for project-specific inventory and UI overrides"
python3 scripts/codex_studio.py checklist --task "Design a custom pack registry for project-specific inventory and UI overrides"
```

## Custom extension packs

If the task is about optional capability surfaces, plugin-like add-ons, or hook packs, include the manifest, hook points, override points, and fallback up front.
Start with `docs/reference/extensions-guide.md` and `docs/examples/extensions-example.md` when the task needs an opt-in pack instead of a one-off chat answer.

Good examples:

- "Design a custom extension pack for inventory hooks and UI panels."
- "Define a plugin-like add-on that can be disabled without touching canonical combat state."
- "Build an extension manifest for a debug overlay and keep the fallback explicit."

```bash
python3 scripts/codex_studio.py next "Design a custom extension pack for inventory hooks and UI panels"
python3 scripts/codex_studio.py checklist --task "Design a custom extension pack for inventory hooks and UI panels"
```

## Weak task patterns

These are too broad:

- "work on combat"
- "fix the engine stuff"
- "make the UI better"
- "optimize performance"

These give weak routing and weak checklists because the system cannot tell what actually changed.

## Performance

If the task is about FPS, frame time, memory, or scale, include the target hardware, the baseline, and the first lever before implementation.
Start with `docs/reference/perf-guide.md` and `docs/examples/perf-example.md` so the agent has the correct first-lever order before it optimizes.

Good examples:

- "Run a performance pass on a Godot survivorlike and prefer node reduction, pooling, and MultiMesh before micro-optimizing scripts."
- "Optimize Unity projectile spam with pooling and NonAlloc queries before considering DOTS."
- "Profile an Unreal horde encounter and decide between Actor, instancing, and Mass after measuring the real bottleneck."

## Benchmark and measurement

If the task is about route accuracy, checklist quality, docs sync, or a measurement harness, include the benchmark family, baseline, metric, threshold, and artifact before implementation.
Start with `docs/reference/benchmark-guide.md`, `docs/examples/benchmark-example.md`, and `docs/research/game-development/foundations/benchmarks.md` so the agent has the correct measurement order before it compares behavior.

Good examples:

- "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio."
- "Compare SWE-bench and OpenAI Evals for code-edit regression coverage before choosing a harness."
- "Compare AgentBench, GAIA, OSWorld, and WebArena for broad agent coverage before picking a benchmark family."
- "Design a benchmark pass for a Unity 6 inventory HUD and keep the metric, baseline, and artifact explicit."

```bash
python3 scripts/codex_studio.py next "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio"
python3 scripts/codex_studio.py next "Compare SWE-bench and OpenAI Evals for code-edit regression coverage before choosing a harness"
python3 scripts/codex_studio.py next "Compare AgentBench, GAIA, OSWorld, and WebArena for broad agent coverage before picking a benchmark family"
```

## Genre-specific performance

If the task is performance work and the genre itself shapes the bottleneck, include the genre family, the dominant pressure, and the first genre lever before implementation.
Start with `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` when the scale problem is genre-shaped.

Good examples:

- "Run a performance pass on a survivorlike and cap active enemies before changing combat logic."
- "Run a performance pass on a city-builder and chunk simulation before adding more AI detail."
- "Run a performance pass on a factory-automation game and trace throughput bottlenecks before increasing machine count."
- "Run a performance pass on a grand-strategy game and batch campaign state before adding more diplomacy."
- "Run a performance pass on a co-op survival game and tighten replication ownership before changing combat."
- "Run a performance pass on a stealth game and cache visibility before adding patrol complexity."

```bash
python3 scripts/codex_studio.py next "Run a performance pass on a survivorlike and cap active enemies before changing combat logic"
python3 scripts/codex_studio.py next "Run a performance pass on a city-builder and chunk simulation before adding more AI detail"
python3 scripts/codex_studio.py next "Run a performance pass on a factory-automation game and trace throughput bottlenecks before increasing machine count"
```

## Genre software patterns

If the task is about genre support, include the dominant tension, the software pattern family, and the contrast set before implementation.
Start with `docs/research/game-development/genre/genre-guide.md`, `docs/research/game-development/genre/genre-patterns.md`, and `docs/research/game-development/genre/genre-examples.md` when the work is about choosing how the genre should be built. If you need more than one contrast set, add `docs/examples/genre-gallery-example.md` too.

Good examples:

- "Research genre software patterns and contrast sets for a deckbuilder roguelike before implementation."
- "Choose the software pattern family that should own a grand-strategy campaign before refactoring the map."
- "Compare state projection, graph routing, and scheduler patterns for a colony sim before adding more content."

```bash
python3 scripts/codex_studio.py next "Research genre software patterns and contrast sets for a deckbuilder roguelike before implementation"
python3 scripts/codex_studio.py checklist --task "Choose the software pattern family that should own a grand-strategy campaign before refactoring the map"
```

## Genre planning schema

If the task is about turning a genre preset into a buildable plan, include the player outcome, dominant tension, contrast set, loop ladder, canonical owner, accessibility envelope, performance envelope, and validation ladder before implementation.
Start with `docs/reference/genre-plan.md` and `docs/examples/genre-plan-example.md` when the work is about planning a genre instead of only choosing how to build it. If the genre needs more than one contrast set, add `docs/examples/genre-gallery-example.md`.

Good examples:

- "Write a genre plan schema for a tactical RPG that names the player outcome, loop ladder, state owner, accessibility envelope, and first broken system."
- "Plan a city-builder by naming the bottleneck, the diagnostic overlays, and the first district that proves the genre."
- "Write a genre plan for a co-op survival game that keeps session authority, shared scarcity, and recovery explicit."

```bash
python3 scripts/codex_studio.py next "Write a genre plan schema for a tactical RPG"
python3 scripts/codex_studio.py checklist --task "Plan a city-builder by naming the bottleneck, the diagnostic overlays, and the first district that proves the genre"
```

## Advanced optimization algorithms

If the task is about culling, partitioning, batching, instancing, job systems, or state compression, include the algorithm family, the baseline, and the first algorithmic lever before implementation.
Start with `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` when the scale problem is algorithm-shaped.

Good examples:

- "Research advanced optimization algorithms for a Godot 4 survivorlike and decide whether spatial hashing or MultiMesh is the first lever."
- "Compare Unity Burst jobs, GPU occlusion culling, and LODGroup for a dense city-builder before rewriting simulation code."
- "Choose between Unreal HLOD, Instanced Static Meshes, and Mass for a grand-strategy map before increasing world detail."
- "For a co-op survival game, compare interest management, replication grouping, and chunked state updates before increasing actor count."

```bash
python3 scripts/codex_studio.py next "Research advanced optimization algorithms for a Godot 4 survivorlike and decide whether spatial hashing or MultiMesh is the first lever"
python3 scripts/codex_studio.py next "Compare Unity Burst jobs, GPU occlusion culling, and LODGroup for a dense city-builder before rewriting simulation code"
python3 scripts/codex_studio.py next "Choose between Unreal HLOD, Instanced Static Meshes, and Mass for a grand-strategy map before increasing world detail"
```

## GPU and render communication

If the task is about GPU ownership, render-side representation, buffer shape, or CPU-GPU communication, include the CPU owner, GPU owner, upload path, readback policy, and first lever up front.
Start with `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` so the agent can name the render contract before it changes code.

Good examples:

- "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever."
- "Compare Unity GraphicsBuffer, ComputeShader, and indirect instancing for a dense projectile field before changing gameplay code."
- "Choose between Unreal Instanced Static Meshes, Nanite, and HLOD for repeated world objects before scaling Actor count."

```bash
python3 scripts/codex_studio.py next "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever"
python3 scripts/codex_studio.py next "Compare Unity GraphicsBuffer, ComputeShader, and indirect instancing for a dense projectile field before changing gameplay code"
python3 scripts/codex_studio.py next "Choose between Unreal Instanced Static Meshes, Nanite, and HLOD for repeated world objects before scaling Actor count"
```

## Code quality and optimization criteria

If the task is about code quality, maintainability, or optimization criteria, include the ownership model, the quality-control process step, and the validation path up front.
Start with `docs/reference/quality-guide.md`, `docs/reference/quality-process.md`, `docs/examples/quality-example.md`, and `docs/examples/quality-process-example.md` when the task is about refactoring or a reviewable optimization pass.

Good examples:

- "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring."
- "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate."
- "Refactor a Godot combat room so runtime ownership, data ownership, and editor ownership are explicit."
- "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter."

```bash
python3 scripts/codex_studio.py next "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate"
python3 scripts/codex_studio.py next "Refactor a Godot combat room so runtime ownership, data ownership, and editor ownership are explicit"
python3 scripts/codex_studio.py next "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter"
```

If the task is still vague, ask for:

- target hardware
- baseline repro
- first lever
- fallback path

## Library selection

If the task is about choosing the smallest official library, package, plugin, or SDK for a case, include the case and the fallback rule up front.
Start with `docs/reference/library-guide.md` and `docs/examples/library-example.md` so the agent has a concrete stack-selection path before it implements anything.

Good examples:

- "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow."
- "For a Godot 4 stealth slice, decide whether built-in APIs already cover input, navigation, and save."
- "For an Unreal 5 co-op combat slice, name the minimum official stack for input, UI, networking, and effects."

```bash
python3 scripts/codex_studio.py next "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow"
python3 scripts/codex_studio.py next "For a Godot 4 stealth slice, decide whether built-in APIs already cover input, navigation, and save"
python3 scripts/codex_studio.py next "For an Unreal 5 co-op combat slice, name the minimum official stack for input, UI, networking, and effects"
```

## Asset management and import

If the task is about source art, imported assets, shared tuning, packaging, or load boundaries, include the source asset, the runtime owner, and the import rule up front.
Start with `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` so the agent has a concrete asset-selection path before it implements anything.

Good examples:

- "Compare Godot Resource, PackedScene, and imported texture ownership for a HUD icon set."
- "Choose between Unity ScriptableObject, Sprite Atlas, and Addressables for inventory art."
- "Decide whether Unreal should use Data Assets or soft references for shop items and their loading path."

```bash
python3 scripts/codex_studio.py next "Compare Godot Resource, PackedScene, and imported texture ownership for a HUD icon set"
python3 scripts/codex_studio.py next "Choose between Unity ScriptableObject, Sprite Atlas, and Addressables for inventory art"
python3 scripts/codex_studio.py next "Decide whether Unreal should use Data Assets or soft references for shop items and their loading path"
```

## UI and templates

If the task is about HUDs, menus, settings, onboarding, inventory UI, or choosing a UI template source, include the screen owner, the projection boundary, the focus model, and the starter source up front.
Start with `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` when the task is about durable UI flow or template choice.

Good examples:

- "Design a controller-first pause menu in Godot using Control, CanvasLayer, and a Theme source."
- "Use Unity UI Toolkit and UI Builder to build an inventory screen with UXML templates and USS styles."
- "Choose UMG, CommonUI, and Enhanced Input for an Unreal settings menu and name the widget template source."

```bash
python3 scripts/codex_studio.py next "Design a controller-first pause menu in Godot using Control, CanvasLayer, and a Theme source"
python3 scripts/codex_studio.py checklist --task "Use Unity UI Toolkit and UI Builder to build an inventory screen with UXML templates and USS styles"
python3 scripts/codex_studio.py next "Choose UMG, CommonUI, and Enhanced Input for an Unreal settings menu and name the widget template source"
```

## Audio and animation

If the task is about audio playback, animation timing, presentation ownership, or cue sync, include the playback owner, timing owner, fallback path, and proof path up front.
Start with `docs/reference/audio-animation-guide.md` and `docs/examples/audio-animation-example.md` when the task is about presentation layers.

Good examples:

- "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation."
- "Compare Unity AudioSource, AudioMixer, and Animator ownership for a menu open and close flow."
- "Design an Unreal telegraph that uses MetaSounds and Animation Blueprints without hiding gameplay truth."

```bash
python3 scripts/codex_studio.py next "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation"
python3 scripts/codex_studio.py next "Compare Unity AudioSource, AudioMixer, and Animator ownership for a menu open and close flow"
python3 scripts/codex_studio.py next "Design an Unreal telegraph that uses MetaSounds and Animation Blueprints without hiding gameplay truth"
```

## Good `next` examples

Gameplay:

```bash
python3 scripts/codex_studio.py next \
  "Implement a short parry window with clear failure feedback for the tutorial encounter"
```

AI and navigation:

```bash
python3 scripts/codex_studio.py next \
  "Design a performant 2D enemy pathfinding setup for Unity rooms with blockers"
```

Inventory and equipment:

```bash
python3 scripts/codex_studio.py next \
  "Design inventory, equipment, and persistence boundaries for a roguelite loadout system"
```

Character architecture:

```bash
python3 scripts/codex_studio.py next \
  "Define the player character locomotion, ability, and animation ownership model for Unreal"
```

Enemy architecture:

```bash
python3 scripts/codex_studio.py next \
  "Design enemy patrol, aggro, and encounter roles for the first biome"
```

Engine bugs and troubleshooting:

```bash
python3 scripts/codex_studio.py next \
  "Classify recurring Godot signal and node-path bugs before patching anything"
python3 scripts/codex_studio.py checklist \
  --task "Classify recurring Unity null reference and prefab override bugs before patching anything"
```

Performance:

```bash
python3 scripts/codex_studio.py next \
  "Run a performance pass on a Godot survivorlike and prefer node reduction before MultiMesh"
python3 scripts/codex_studio.py next \
  "Optimize Unity projectile spam with pooling and NonAlloc queries before DOTS"
python3 scripts/codex_studio.py next \
  "Optimize an Unreal horde encounter by choosing between Actor, instancing, and Mass"
```

Controls and remapping:

```bash
python3 scripts/codex_studio.py next \
  "Design controller remapping, pause flow, and keyboard/gamepad parity for the settings menu"
```

UI and HUD:

```bash
python3 scripts/codex_studio.py next \
  "Design a compact upgrade screen and HUD state flow for controller-first navigation"
```

Audio and animation:

```bash
python3 scripts/codex_studio.py next \
  "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation"
python3 scripts/codex_studio.py checklist --task "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation"
```

Visuals and presentation:

```bash
python3 scripts/codex_studio.py next \
  "Plan the sprite atlas and animation pass for Unity"
```

```bash
python3 scripts/codex_studio.py next \
  "Use the game systems atlas to design a Godot combat room where collision, damage, loot, and UI feedback stay separately owned"
```

Engine comparisons:

```bash
python3 scripts/codex_studio.py next \
  "Compare the best Godot, Unity, and Unreal ownership model for a controller-first upgrade screen"
```

```bash
python3 scripts/codex_studio.py next \
  "Show me the concrete 2D and 3D class choices for a stealth prototype in each engine"
```

```bash
python3 scripts/codex_studio.py next \
  "List the best starter slice for a combat room in Godot, Unity, and Unreal and explain the differences"
```

Skills and upgrades:

```bash
python3 scripts/codex_studio.py next \
  "Separate authored skill definitions, current-run upgrades, and durable meta unlocks"
```

Interactions and pickups:

```bash
python3 scripts/codex_studio.py next \
  "Design pickup prompts, interaction validation, and loot persistence for reward chests"
```

Build and release:

## Build and release

```bash
python3 scripts/codex_studio.py next \
  "Prepare the first Unreal package flow for a Win64 demo build"
```

## Release hardening

If the task is about code protection, symbol policy, or multiplayer trust on a release build, start with `docs/reference/release-hardening-guide.md`, `docs/examples/release-hardening-example.md`, and `docs/research/game-development/production/release-hardening.md` so the build-integrity plan and trust boundary stay explicit.
If the build is co-op or online, keep the dedicated-server split or explicit fallback path in the same prompt bundle instead of hiding it in follow-up notes.

Good examples:

- "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split."
- "Review whether our Godot export should use PCK encryption and what rollback evidence must stay visible."
- "Set up an Unreal 5 shipping build with separate client and server targets and a clear trust boundary."

```bash
python3 scripts/codex_studio.py next \
  "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split"

python3 scripts/codex_studio.py checklist \
  --task "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split"
```

## Versioning

Before bumping release metadata, compare `docs/reference/version-guide.md`, `docs/examples/version-example.md`, and `docs/research/game-development/production/versioning.md` so the version file, changelog, and tag policy stay aligned.
When the bump is not a tiny metadata-only change, include commit notes with a subject and body that say what changed so the history and the changelog stay in sync.

```bash
python3 scripts/codex_studio.py next \
  "Bump the repo version and keep VERSION, CHANGELOG.md, and release tags aligned"
```

## Sector intelligence

If the task is about current game-industry, market, platform, or policy signals, name the source hierarchy and the current window up front.
Start with `docs/reference/sector-intel.md` and `docs/examples/sector-intel-example.md` when the work needs a source-backed current snapshot instead of implementation.

Good examples:

- "Summarize the current game-industry signals that matter for a Steam-first indie survival game."
- "Track the latest platform-policy and accessibility changes that could affect a mobile release plan."
- "Give me a source-backed current snapshot of the game sector, with the main implications for our scope."

```bash
python3 scripts/codex_studio.py next \
  "Summarize the current game-industry signals that matter for a Steam-first indie survival game"

python3 scripts/codex_studio.py checklist \
  --task "Track current sector signals for a Steam-first indie survival game"
```

## Steam intel

If the task is specifically about Steam store traffic, wishlists, forum signals, or hardware mix, name the Steam source family and the current window up front.
Start with `docs/reference/steam-intel.md`, `docs/examples/steam-intel-example.md`, and `docs/research/game-development/production/steam-intel.md` when the work needs a source-backed Steam snapshot instead of broad sector context.

Good examples:

- "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game."
- "Decide whether our next Steam move should be a store-page push, a forum FAQ update, or a demo beat."
- "Turn the current Steam signals into a simple chart pack and one recommendation."

```bash
python3 scripts/codex_studio.py next \
  "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game"

python3 scripts/codex_studio.py checklist \
  --task "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game"
```

## Platform compatibility

If the task is about family-by-family compatibility across Windows, macOS, Linux/Steam Deck, web, Android/iOS, or TV/webOS, name the family split and the first delta up front.
Start with `docs/reference/platform-guide.md`, `docs/examples/platform-example.md`, and `docs/research/game-development/production/platform-compatibility.md` when the work needs a source-backed compatibility matrix instead of a vague port note.
## Console / PS5-like readiness
Start with `docs/reference/console-guide.md`, `docs/examples/console-example.md`, and `docs/research/game-development/production/console.md` when the work needs a PS5-like or console-premium readiness matrix instead of a vague port note.

Good examples:

- "Map compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS, then give me one readiness matrix."
- "Tell me whether the web build or the TV build is the first compatibility risk for this game."
- "Compare Steam Deck and macOS readiness for our current build and name the first lever."

```bash
python3 scripts/codex_studio.py next \
  "Map compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS"

python3 scripts/codex_studio.py checklist \
  --task "Map compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS"
```

## Cross-platform support tiers

If the task is about support tiers, release sequencing, or deciding which families are core, supported, demo-only, research-only, or deferred, name the support tier and release order up front.
Start with `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md`, and `docs/research/game-development/production/cross-platform.md` when the work needs support-strategy guidance instead of only a compatibility matrix.

Good examples:

- "Turn our platform targets into a support-tier matrix with core, supported, demo-only, research-only, and deferred families."
- "Map release order, support tiers, and first validation steps for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS."
- "Tell me which families are ship targets versus future research for a Steam-first build."

```bash
python3 scripts/codex_studio.py next \
  "Turn our platform targets into a support-tier matrix with core, supported, demo-only, research-only, and deferred families"

python3 scripts/codex_studio.py checklist \
  --task "Map release order, support tiers, and first validation steps for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS"
```

## Marketing strategy

If the task is about campaign strategy, channel mix, audience fit, or measurement, name the objective and the channel family up front.
Start with `docs/reference/marketing-guide.md` and `docs/examples/marketing-example.md` when the work needs a source-backed strategy instead of a beat brief.

Good examples:

- "Build a marketing strategy for a Steam-first indie survival game."
- "Compare creator outreach versus a demo festival beat for our current build."
- "Evaluate whether the current Steam page can support the next marketing push."

```bash
python3 scripts/codex_studio.py next \
  "Build a marketing strategy for a Steam-first indie survival game"

python3 scripts/codex_studio.py checklist \
  --task "Compare creator outreach versus a demo festival beat for our current build"
```

## Marketing intel

If the task is about current marketing status, chart packs, or the latest campaign movement, name the source family and the time window up front.
Start with `docs/reference/marketing-intel.md` and `docs/examples/marketing-intel-example.md` when the work needs a source-backed status readout instead of a strategy memo.
Keep `docs/research/game-development/production/marketing-intel.md` in the loop so the current-status path stays source-backed, not strategy-only.

Good examples:

- "Turn the latest marketing signals into a chart pack and one recommendation."
- "Summarize the current campaign status and tell me which chart matters most."
- "Compare wishlist trend, creator mentions, and community themes for the last 14 days."

```bash
python3 scripts/codex_studio.py next \
  "Turn the latest marketing signals into a chart pack and one recommendation"

python3 scripts/codex_studio.py checklist \
  --task "Summarize the current campaign status and tell me which chart matters most"
```

Tools:

```bash
python3 scripts/codex_studio.py next \
  "Create a small import helper for batch-tagging combat VFX assets"
```

## Good `checklist` examples

```bash
python3 scripts/codex_studio.py checklist \
  --task "Ship the first Godot combat room"
```

```bash
python3 scripts/codex_studio.py checklist \
  --task "Refactor Unity combat projectiles into a pooled runtime path"
```

```bash
python3 scripts/codex_studio.py checklist \
  --task "Prepare Unreal 5 package validation for the first external demo"
```

```bash
python3 scripts/codex_studio.py checklist \
  --task "Bump the repo version and prepare the release tag contract"
```

## Good `research` examples

```bash
python3 scripts/codex_studio.py research \
  --category systems \
  --title "Combat readability baseline"
```

```bash
python3 scripts/codex_studio.py research \
  --category production \
  --title "First external demo release validation"
```

```bash
python3 scripts/codex_studio.py research \
  --category engines \
  --title "Unity prefab ownership for combat rooms"
```

## Better phrasing by discipline

Combat:

- "Add a heavier melee enemy with a slower but more legible windup."
- "Tune damage feedback so failure reads immediately without freezing the pace."

Engine bugs:

- "Classify the recurring engine bug families before choosing a patch."
- "Name the first debug surface for this Godot, Unity, or Unreal issue before implementation."
- "Separate editor-only, runtime-only, and packaged-build-only failures before fixing the bug."

UI:

- "Design a compact upgrade choice screen that fits controller-first navigation."
- "Add a pause menu flow with resume, restart, and settings."
- "Define keyboard, gamepad, and UI focus rules before adding remapping."

Save systems:

- "Define what should persist after a failed run versus what resets."
- "Plan a migration-safe save structure for progression unlocks."
- "Separate item definitions, runtime inventory state, and persistent equipment state."

Character architecture:

- "Decide what owns dash validation, locomotion, animation transitions, and stamina costs."
- "Define how player state, equipment state, and temporary combat state stay separate."

Audio and animation:

- "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation."
- "Compare Unity AudioSource, AudioMixer, and Animator ownership for a menu open and close flow."
- "Design an Unreal telegraph that uses MetaSounds and Animation Blueprints without hiding gameplay truth."

Visuals and presentation:

- "Plan the sprite atlas, animation playback, and UI image ownership for the Unity HUD."
- "Define whether Paper2D, Animation Blueprints, or Niagara owns the new Unreal effect."
- "Separate Godot sprite presentation, animation state, and VFX triggers before implementation."
- "Use the game systems atlas to separate collision, damage, loot, and UI feedback ownership before implementing a combat room."

Enemy architecture:

- "Define enemy archetype data versus runtime behavior state before adding a second faction."
- "Plan patrol, aggro, and encounter-role boundaries before scaling enemy count."

Controls and UI architecture:

- "Decide which action map powers gameplay, which powers menus, and where rebinding is saved."
- "Define what the camera reacts to and what it must never silently control."

Skills and upgrades:

- "Separate authored skill definitions, current-run upgrades, and durable profile unlocks."
- "Decide which system owns cooldown state, stack rules, and upgrade UI projection."

World graph:

- "Define the node and edge types, the append-only history layer, and the cached read model before implementation."
- "Separate canonical relationship truth from runtime deltas and codex presentation."

Interactions:

- "Define how pickup prompts, interaction checks, and loot grants stay separate."
- "Choose whether prompts are proximity-only, facing-based, or target-selection based before adding content scale."

Performance:

- "Measure projectile count scaling and choose between pooling and representation change."
- "Decide whether this Unity crowd problem should stay classic-object based or move toward data-oriented scale."

Build pipeline:

- "Document the first reproducible demo export path and its artifact naming."
- "Add a release-readiness review step for nightly engine-contract smoke."
- "Keep the version file, changelog, and release tag policy in the same contract."

## Ask for one slice, not one department

Good:

- "Implement the first upgrade choice after room clear."
- "Investigate why dodge sometimes exits the arena bounds."

Bad:

- "Finish progression."
- "Do the whole build pipeline."

If a task sounds like multiple weeks, split it before routing it.

## Good direct prompts to Codex

If you are talking directly to Codex in the thread, these patterns work well:

- "Route this task and tell me which docs I should update first: ..."
- "Give me the merged checklist for this Unreal packaging task and keep it practical."
- "Turn this idea into a smaller vertical slice before we implement it: ..."
- "Find the highest-risk part of this feature and suggest a validation-first plan."
- "Convert this vague bug into reproducible steps, hypotheses, and next action."

## Prompt upgrade examples

Weak:

- "add enemy"

Better:

- "Add a second enemy type that pressures movement rather than burst damage, and keep the tutorial room readable."

Weak:

- "optimize unity"

Better:

- "Review whether our Unity projectile handling should stay pooled MonoBehaviours or move toward a more data-oriented scale path."

Weak:

- "release setup"

Better:

- "Prepare a realistic release-readiness checklist for the first external PC demo and show which CI checks should be mandatory."

## When to make a feature brief first

Make a brief before routing if the task changes:

- save ownership
- combat rules
- progression structure
- architecture boundaries
- engine representation choice
- packaging or release expectations

Use:

```bash
python3 scripts/scaffold_feature.py "Your Feature" --with-adr --with-test-plan --with-eval-plan
```

Then route the brief-driven task, not the vague idea.
