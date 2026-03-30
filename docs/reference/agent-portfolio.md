# Agent Portfolio

## Summary

Use this page when a task needs one specialist, a paired handoff, or a small multi-agent panel.
Single specialist mode is always available and should remain the default unless a broader panel is clearly justified.
If the task also needs titles, reporting lines, or async packets, pair this page with `docs/reference/agent-hierarchy.md`.
The public title layer uses `Kaynexis` for the controller and scientist names for specialist lanes, while the internal role ids stay stable in routing and metadata.

The master mind stays the controller. The specialist agents stay narrow and single-purpose.
The Kaynexis controller title and scientist public-title layer are mirrored in `.codex/agents/*.toml` and surfaced in route output as `agent_titles`.
If the task needs proof of an operating-model choice, also read `docs/reference/agent-validation-matrix.md` and `docs/examples/agent-validation-matrix-example.md` so the mode decision stays reviewable instead of implicit.
For the full operating model above this page, start with `docs/reference/agent-system.md` and `docs/examples/agent-system-example.md`.
If the task is about OpenAI, Codex, or agent-platform wiring, also start with `docs/research/openai-codex-infra-findings.md` and `docs/reference/codex-compatibility.md` before choosing single specialist, paired specialist, or panel mode.
If you need the repo-local control contract for that workflow, also read `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md`.

## Primary sources

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- HuggingGPT: https://arxiv.org/abs/2303.17580

These sources all support the same repo pattern:

- keep a controller that turns a broad request into a control plan
- keep specialists narrow so responsibility stays obvious
- use a small panel when one specialist cannot safely own the whole task
- keep the user-facing summary simple even when the internal plan is multi-agent

## Why this matters to this repo

- The repo already has many specialist roles and routing rules.
- Without a portfolio view, broad tasks can overuse a generic agent or blur ownership.
- A role matrix keeps each agent narrow enough to be testable and easy to hand off.
- Role-specific checklist packs in `studio/checklists/discipline/` keep each lane's control contract honest.
- The controller can then choose single-agent, paired-agent, or panel mode based on the request.
- Each specialist lane keeps a default model in its agent profile, and the user may override that lane explicitly when a task needs a different speed/precision tradeoff.
- If the task includes state, authority, event, or projection architecture, pair the role matrix with the architecture guide diagrams before splitting lanes.
- If the work should be reviewable later, pair the role matrix with the prompt journal. If there are handoffs or back-and-forth agent messages, also pair it with the transcript so the prompt history, step notes, and message turns stay together.

## Operating modes

### Single specialist

Use one specialist when one lane owns the answer and validation is small.
This is the default mode, not a fallback after panel mode fails.

### Paired specialist

Use a doer plus a validator when the change is narrow but should be checked by a second lane.

### Multi-agent panel

Use a small panel when the request crosses design, implementation, docs, QA, or release boundaries.

### Master Mind controller

Use the master mind when the task needs routing, a simple user summary, and several specialist handoffs.

## Core role matrix

| Role | Public title | Owns | Does not own | Use when | Common pair |
| --- | --- | --- | --- | --- | --- |
| `mastermind` | Kaynexis | control loop, delegation, summary, validation order | all implementation details | broad, cross-functional, or multi-step requests | `producer`, `technical_director`, `docs_researcher` |
| `producer` | Marie Curie | scope, sequencing, dependency order, risk | architecture or craft taste | sprint planning, roadmap shaping, handoff sequencing | `technical_director` |
| `technical_director` | Alan Turing | architecture, boundaries, feasibility, technical risk | pure taste or final narrative polish | system design, engine risk, cross-layer decisions | `lead_programmer` |
| `game_designer` | Ada Lovelace | player outcome, rules, pacing, loop shape | engine plumbing or release ops | mechanics, genre support, tuning of the core loop | `gameplay_programmer` |
| `docs_researcher` | Charles Darwin | primary-source evidence, doc-backed claims | product or architecture ownership | version-sensitive research and evidence gathering | `technical_director` |
| `qa_lead` | Rosalind Franklin | validation strategy, go/no-go, evidence quality | design authorship or implementation detail | review gates, acceptance criteria, test planning | `qa_tester` |
| `performance_analyst` | Richard Feynman | baseline, bottleneck, first lever | feature design or narrative judgment | FPS, memory, scale, or algorithmic tuning | `rendering_programmer` |
| `build_release_engineer` | Claude Shannon | CI, packaging, artifacts, build contracts | gameplay tuning or art style | release engineering, reproducible builds, delivery | `release_manager` |
| `release_manager` | Stephen Hawking | release readiness, ship sequencing, publish risk | low-level implementation | launch prep, freeze windows, release go/no-go | `build_release_engineer` |
| `art_director` | Leonardo da Vinci | visual direction, readability, asset priorities | engine-specific implementation details | style coherence, content direction, presentation gates | `technical_artist` |
| `audio_director` | Hermann von Helmholtz | audio language, mix hierarchy, presentation priorities | gameplay rule design | sound direction, cues, and mix planning | `sound_designer` |
| `narrative_director` | Carl Sagan | story beats, lore structure, dialogue direction | engine plumbing | lorebook, quest flow, world graph, branching story | `quest_designer` |
| `ui_programmer` | Grace Hopper | screens, HUDs, flows, projection boundaries | release or narrative design | menus, HUDs, onboarding, settings, UI templates | `ux_designer` |
| `engine specialists` | Nikola Tesla / Katherine Johnson / Margaret Hamilton / Enrico Fermi | engine-native setup, node/component/class ownership | cross-engine product strategy | engine-specific slices and validation loops | `technical_director` |

## Example allocation patterns

- Broad engine + genre research: `mastermind` + `technical_director` + `docs_researcher`
- Feature slice with a quality gate: `producer` + `game_designer` + `qa_lead`
- Performance pass: `performance_analyst` + `technical_director` + `rendering_programmer`
- Release readiness: `release_manager` + `build_release_engineer` + `qa_lead`
- UI flow: `ui_programmer` + `ux_designer` + `qa_lead`
- Narrative system: `narrative_director` + `quest_designer` + `docs_researcher`

## Validation

A good portfolio pass should leave behind:

- one simple user summary
- one chosen operating mode
- one role matrix or handoff map
- one narrow validation path
- one durable doc update if the role mapping changes repo behavior
- one prompt-history entry, one agent journal note, and one transcript entry if the work should be reopened later
- the Kaynexis controller title and scientist public-title map mirrored in `.codex/agents/*.toml`
- the lane model defaults and any explicit model overrides mirrored in route output or the review trail

## Related docs

- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-guide.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/examples/agent-portfolio-example.md`
- `docs/examples/agent-system-example.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/examples/prompt-journal-example.md`
- `docs/examples/agent-transcript-example.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/architecture-guide.md`
- `docs/examples/agent-hierarchy-example.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/research/game-development/foundations/agent-portfolio.md`
- `docs/research/game-development/foundations/agent-validation-matrix.md`
