# OpenAI Codex Model Guidance

Last reviewed: `2026-03-30`

This note turns the current OpenAI model catalog into a repo-local decision map for model choice and plan-tier choice. Use it when the task is about Codex, model selection, plan limits, or the tradeoff between speed, cost, and precision.

## Source pages

- Models catalog: https://developers.openai.com/api/docs/models
- GPT-5.4 model page: https://developers.openai.com/api/docs/models/gpt-5.4
- GPT-5.4 pro model page: https://developers.openai.com/api/docs/models/gpt-5.4-pro
- GPT-5.4 mini model page: https://developers.openai.com/api/docs/models/gpt-5.4-mini
- GPT-5.4 nano model page: https://developers.openai.com/api/docs/models/gpt-5.4-nano
- OpenAI for developers homepage: https://developers.openai.com/
- ChatGPT developer mode: https://developers.openai.com/api/docs/guides/developer-mode
- GPT-5.2 and GPT-5.2-Codex pages for compatibility context only: https://developers.openai.com/api/docs/models/gpt-5.2 and https://developers.openai.com/api/docs/models/gpt-5.2-codex

## Findings

### 1. Model choice is separate from routing policy

The agent controller decides who should do the work. The model guide decides which model family is the best fit once the lane is known.

### 2. `gpt-5.4` is the default when the task is hard

The current model catalog describes `gpt-5.4` as the flagship choice for complex reasoning, coding, and professional workflows. Use it first when the task needs broad context, multi-step reasoning, or tool-heavy code work.

### 3. `gpt-5.4-pro` is for the hardest or most correctness-sensitive cases

The current model page describes `gpt-5.4-pro` as the more compute-heavy choice that produces smarter and more precise responses. It is the right fit when the task can justify extra latency and cost. It is not the right fit for routine edits, small refactors, or cheap fan-out.

### 4. `gpt-5.4-mini` is the best small model for agentic coding support

The model catalog describes `gpt-5.4-mini` as the strongest mini model for coding, computer use, and subagents. Use it for specialist workers, cheaper parallel tasks, and small code or doc edits that still need real reasoning. Do not promote it to the final hard pass when the task still needs broad synthesis.

### 5. `gpt-5.4-nano` is for simple, high-volume shaping work

The model catalog describes `gpt-5.4-nano` as the cheapest GPT-5.4-class choice for simple high-volume tasks such as classification, data extraction, ranking, and sub-agents. Use it for routing, tagging, extraction, and trivial summaries. Do not use it for architecture, correctness review, or multi-file reasoning.

### 6. Older Codex-branded and GPT-5.x model pages are compatibility surfaces

The catalog still includes older Codex-branded model pages and older GPT-5 family pages. Those are useful when maintaining a legacy prompt, but the current docs recommend `gpt-5.4` and `gpt-5.4-pro` as the latest choices and `gpt-5.4-mini` or `gpt-5.4-nano` as the smaller variants.

### 7. ChatGPT subscription tier and API usage are separate decisions

OpenAI's developer homepage says Codex is included in ChatGPT Free and Go for a limited time, and that Plus, Pro, Business, and Enterprise get 2x Codex rate limits. The developer-mode page says developer mode is available in beta to Pro, Plus, Business, Enterprise, and Education accounts on the web.

This repo treats that as a practical fit rule:

- Free / Go: trial or light interactive use only
- Plus: good for an individual who uses Codex regularly
- Pro: good for a power user who wants heavier interactive use and developer-mode access
- Business: good for a team that wants shared control and higher Codex limits
- Enterprise / Education: good for org-managed usage and access controls

That fit rule is an inference from the current docs, not a guaranteed entitlement contract. When in doubt, check the live OpenAI docs before relying on a plan-specific assumption.

### 8. API usage is separate from ChatGPT subscriptions

If the workflow uses the API instead of the ChatGPT app, use the model catalog and rate-limit tables directly. The plan-tier recommendations above are for ChatGPT/Codex app usage, not API billing.

### 9. Record the decision path when model choice matters

When a task depends on the model choice, record:

- the surface: ChatGPT app, Codex app, or API
- the selected model
- the reasoning level
- the plan tier if the task is plan-sensitive
- the fallback model if the first choice fails

### 10. Specialist lanes inherit defaults but may be overridden explicitly

When a task fans out into specialists, each lane should inherit the model declared in its agent profile by default. If the user wants a different tradeoff for one lane, the override should be explicit in the route or checklist command so the decision is visible later.

That means:

- keep the default model in `.codex/agents/*.toml`
- use `--agent-model agent=model` when a specific lane needs a different speed/precision balance
- keep the override in the route output or review trail so the choice can be reopened later

## Decision map

| Need | Best default | Avoid | Why |
| --- | --- | --- | --- |
| Broad coding, architecture, or long-horizon reasoning | `gpt-5.4` | `gpt-5.4-nano` | `gpt-5.4` is the flagship general model for hard agentic work |
| Final correctness pass on a hard problem | `gpt-5.4-pro` | `gpt-5.4-mini` | `gpt-5.4-pro` uses more compute and is the precision choice |
| Small specialist workers or cheap parallel fan-out | `gpt-5.4-mini` | `gpt-5.4-pro` | `gpt-5.4-mini` is the best small model for coding and subagents |
| Routing, extraction, ranking, or simple classification | `gpt-5.4-nano` | `gpt-5.4` | `gpt-5.4-nano` is the cheapest fit for high-volume simple work |
| ChatGPT app trial or very light use | Free / Go | Business / Enterprise | Use the smallest practical plan tier when you just need to explore |
| Daily individual Codex work | Plus | Free / Go | Plus is the practical step up when Codex becomes part of the workflow |
| Heavy interactive Codex use or developer-mode testing | Pro | Free / Go | Pro gives the strongest personal-surface fit in the current docs |
| Team or org-managed usage | Business / Enterprise / Education | Free / Go | These tiers fit shared controls and access management better |

## Related docs

- `docs/reference/codex-model-guide.md`
- `docs/examples/codex-model-guide-example.md`
- `studio/checklists/discipline/openai_models.toml`
- `studio/docs/active/eval-openai-models.md`

## Repo rule

- Prefer the smallest model that can safely complete the task.
- Do not default to a harder model just because it exists.
- Do not conflate model selection with routing policy.
- Keep the model guide, the example, the checklist, and the eval plan in sync whenever the recommendation changes.
