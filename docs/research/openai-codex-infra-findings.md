# OpenAI Codex Infrastructure Findings

Last reviewed: `2026-03-29`

This note captures the OpenAI docs that most directly shaped this repository's agent operating model, prompt routing, and eval discipline. It is intentionally short; the linked source pages remain the source of truth.

## Source pages

- Codex cloud: https://developers.openai.com/codex/cloud
- Codex internet access: https://developers.openai.com/codex/cloud/internet-access
- Codex code generation: https://platform.openai.com/docs/guides/code-generation
- Shell tool with the Agents SDK: https://platform.openai.com/docs/guides/tools-shell
- Background mode: https://platform.openai.com/docs/guides/background
- Prompt / text generation guidance: https://platform.openai.com/docs/guides/text-generation/parameter-details
- Evaluation best practices: https://platform.openai.com/docs/guides/evaluation-best-practices
- Safety best practices: https://platform.openai.com/docs/guides/safety-best-practices/constrain-user-input-and-limit-output-tokens.pls
- Messages reference: https://platform.openai.com/docs/api-reference/messages/object
- OpenAI Platform overview: https://platform.openai.com/docs/overview

## Findings adopted in this repo

### 1. Keep durable policy separate from task-specific prompt text

OpenAI's prompting guidance treats the stable instruction layer and the task payload as separate concerns. In practice, that means durable controller policy belongs in stable repo docs and role metadata, while task-specific details, examples, and constraints belong in the routed prompt or workflow note.

This repo mirrors that separation by keeping long-lived agent policy in `AGENTS.md`, `docs/reference/`, `.codex/agents/`, and `studio/docs/active/`, instead of stuffing everything into a single ephemeral request.

### 2. Version prompts and rerun evals when behavior changes

OpenAI's eval guidance emphasizes designing the eval before declaring the change done. The platform docs also frame prompt design as something you iterate, version, and measure instead of treating it as one static blob.

This repo therefore treats routing changes, agent-behavior changes, and prompt-shape changes as eval-worthy changes. If a prompt or controller rule changes, the matching eval plan should change with it.

### 3. Prefer explicit workflows, traces, and handoffs for multi-step work

Codex cloud, the shell tool, and the broader OpenAI platform now all point toward workflow-style agent operation rather than opaque "one giant prompt" thinking. The useful mental model is a controller plus explicit tools, handoffs, and traceable steps.

This repo mirrors that with:

- a simple user summary
- a named controller decision
- a narrow role matrix
- a command tree when needed
- an append-only prompt journal
- a short validation path

### 4. Keep tool access and internet access constrained

OpenAI's Codex cloud docs say agent internet access is blocked by default and can be enabled per environment when needed. They also call out prompt injection, secret exfiltration, and malicious dependencies as real risks.

This repo keeps the sandbox conservative, keeps web search cached unless freshness is required, and makes tool or internet assumptions explicit when a task crosses external boundaries.

### 5. Use agent-style workflows only when the task benefits from them

OpenAI's docs surface multiple workflow surfaces, including Codex cloud, the shell tool, and higher-level agent workflow tooling. The lesson for this repo is not "always fan out"; it is "use the smallest workflow that keeps ownership visible."

This repo keeps single specialist mode visible by default and only fans out when the task actually needs a controller, a panel, or explicit reporting lines.

### 6. Separate controller summary from internal worker detail

OpenAI's docs make it clear that traces, evals, and tooling can be rich internally, but the user does not need every internal step. The controller should still surface a short, readable answer.

This repo therefore keeps `Kaynexis` or the single specialist as the public-facing story while hiding specialist chatter in the journal, checklist, or active docs.

### 7. Model selection is a separate decision from routing policy

OpenAI's platform docs now document model and workflow surfaces for coding and agentic tasks. That is useful context, but it is still a separate decision from how we route or split work.

This repo keeps its model defaults stable unless a deliberate model-selection review says otherwise. Routing, journaling, evals, and tool safety are allowed to evolve independently of the baseline model choice.

### 8. Model choice should be reopened through a dedicated guide

When the question is specifically about which model or plan tier to use, this repo does not want the agent to improvise from memory. It should reopen the model ladder, the plan fit, and the API-vs-ChatGPT split from `docs/research/openai-codex-models.md` and `docs/reference/codex-model-guide.md` before recommending a lane.

## Resulting repo guardrails

- Use `docs/research/openai-codex-infra-findings.md` first for OpenAI/Codex questions.
- Use `docs/research/openai-codex-models.md` and `docs/reference/codex-model-guide.md` first for model-choice or plan-tier questions.
- Prefer `docs/reference/agent-system.md` for the repo operating model.
- Keep prompt history, agent journaling, eval plans, and review trails aligned whenever routing or agent behavior changes.
- Keep tool approvals, internet access, and safety assumptions explicit when any workflow touches external systems.
- Use `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` as the durable control surface for this lane.
- Create or update `eval-plan-*.md` files when instruction, routing, or agent behavior changes.
