# Agent Hierarchy

## Summary

Use this page when a task needs a controller, named command tiers, and async specialist lanes.
Single specialist mode is always available and remains the default unless a broader tree is clearly justified.
The public title layer uses `Kaynexis` for the controller and scientist names for specialist lanes, while the internal role ids stay stable in routing and metadata.

The goal is not to create more drama in the prompt. The goal is to make ownership, reporting, and handoff flow visible.
If the task needs proof of an operating-model choice, also read `docs/reference/agent-validation-matrix.md` and `docs/examples/agent-validation-matrix-example.md` so the command tree stays reviewable instead of implicit.
For the full operating model that chooses whether hierarchy is needed at all, start with `docs/reference/agent-system.md` and `docs/examples/agent-system-example.md`.
If the task needs a durable pre-flight contract, also read `docs/reference/agent-execution.md` and `docs/examples/agent-execution-example.md` so the owner, mode, proof path, and custom rules stay explicit before the tree fans out.
If the hierarchy task is about OpenAI, Codex, or agent-platform wiring, also start with `docs/research/openai-codex-infra-findings.md` and `docs/reference/codex-compatibility.md` so the reporting lines stay tied to the current platform guidance.
If the hierarchy workflow needs a durable control contract, also read `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md`.

## Primary sources

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- HuggingGPT: https://arxiv.org/abs/2303.17580
- MetaGPT: https://arxiv.org/abs/2308.00352
- ChatDev: https://arxiv.org/abs/2307.07924

These sources support the same repo pattern:

- keep one controller that turns a broad request into a command tree
- keep each lane narrow enough that ownership is obvious
- keep reporting lines explicit so async work does not blur accountability
- keep the user-facing summary simple even when the internal plan fans out
- if the work should be reopened later, keep the prompt history, agent journal note, and transcript in the same review trail

## Why this matters to this repo

- The repo already has many specialist agents and routing rules.
- Broad requests can drift unless titles, reporting lines, and async packets are explicit.
- A hierarchy lets the controller choose the smallest tree that can answer the task safely.
- The single-specialist path must stay visible so hierarchy does not become the default for everything.
- Role-specific checklist packs in `studio/checklists/discipline/` keep each lane's checklist small enough to read in one pass.

## Decision impact

- Single specialist mode stays the default.
- A hierarchy is only used when the request truly needs parallel lanes or nested ownership.
- The command tree must be small enough to summarize in one view.
- Every lane reports upward through one parent; no sideways ownership.
- The chosen titles affect route prompts, checklists, validation, and durable docs.
- The chosen lane model should stay visible too: each node inherits a default from its profile, and the user may override a node explicitly if the task needs a different tradeoff.
- Role-specific checklist packs in `studio/checklists/discipline/` keep the command tree honest as it grows.

## Command tree

| Tier | Public title | Repo roles | Owns | Reports to | Async packet |
| --- | --- | --- | --- | --- | --- |
| Controller | Kaynexis | `mastermind` | control loop, delegation order, user summary, validation order | none | control plan, lane map, summary |
| Director | Marie Curie / Alan Turing / Stephen Hawking / Claude Shannon | `producer`, `technical_director`, `release_manager`, `build_release_engineer` | scope, sequencing, architecture, release gates | Controller | plan packet, risk packet, gate packet |
| Lead | Ada Lovelace / Leonardo da Vinci / Hermann von Helmholtz / Carl Sagan / Grace Hopper / Rosalind Franklin / Charles Darwin / Richard Feynman | `game_designer`, `art_director`, `audio_director`, `narrative_director`, `ui_programmer`, `qa_lead`, `docs_researcher`, `performance_analyst` | one narrow lane each | Director | lane packet, blocker packet, evidence packet |
| Specialist | Nikola Tesla / John McCarthy / Donald Knuth / Hedy Lamarr / Herbert A. Simon / Florence Nightingale / Max Planck | `engine_programmer`, `gameplay_programmer`, `tools_programmer`, `technical_artist`, `ux_designer`, `qa_tester`, `rendering_programmer` | one buildable slice | Lead | work packet, status packet, proof packet |

## Common title map

- Controller -> `Kaynexis` (`mastermind`)
- Software architect -> `Alan Turing` (`technical_director`)
- Quality controller -> `Rosalind Franklin` (`qa_lead`)
- Creator lead -> `Ada Lovelace`, `Leonardo da Vinci`, `Hermann von Helmholtz`, `Carl Sagan`, or `Grace Hopper` depending on the lane
- Implementation owner -> `Nikola Tesla`, `John McCarthy`, `Donald Knuth`, `Hedy Lamarr`, or `Herbert A. Simon`
- Release owner -> `Stephen Hawking` (`release_manager`)
- Build operator -> `Claude Shannon` (`build_release_engineer`)
- Evidence owner -> `Charles Darwin` (`docs_researcher`)
- Performance owner -> `Richard Feynman` (`performance_analyst`)

## Async contract

Every lane should pass a compact status packet upward.

Required fields:

- `title`
- `owner`
- `reports_to`
- `scope`
- `blockers`
- `evidence`
- `next_action`
- `status`

Async rules:

- One lane owns one contract.
- No lane edits another lane's contract unless it is the parent or controller.
- If a lane is blocked, it returns a blocker packet to its parent instead of stalling silently.
- The controller merges lane packets into one short user summary.
- If the task needs a pre-flight contract, keep the execution packet aligned with the status packet so the lane does not drift before implementation starts.
- If the request still fits one specialist, do not fan out just because the hierarchy exists.

## Example prompts for the agent

- "Design a command tree for a broad gameplay, UI, QA, and release request while keeping single specialist mode available."
- "Assign software architect, quality controller, and creator lead titles to a narrow async panel."
- "Keep the controller simple, the hierarchy explicit, and the validation path short."

## Validation

A good hierarchy pass should leave behind:

- one plain-language user summary
- one chosen mode
- one command tree with explicit titles
- one async packet shape
- one model choice per lane when the task needs it
- one execution packet when the task needs a durable pre-flight contract
- one narrow validation path
- one durable doc update if the hierarchy changes repo behavior
- one prompt-history entry, one agent journal note, and one transcript entry if the work should be reopened later
- the Kaynexis controller title and scientist public-title map mirrored in `.codex/agents/*.toml`

## Related docs

- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-guide.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/agent-execution.md`
- `docs/examples/agent-hierarchy-example.md`
- `docs/examples/agent-system-example.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/examples/agent-execution-example.md`
- `docs/examples/prompt-journal-example.md`
- `docs/examples/agent-transcript-example.md`
- `docs/examples/mastermind-example.md`
- `docs/examples/agent-portfolio-example.md`
- `docs/research/game-development/foundations/agent-hierarchy.md`
- `docs/research/game-development/foundations/agent-execution.md`
- `docs/research/game-development/foundations/agent-validation-matrix.md`
