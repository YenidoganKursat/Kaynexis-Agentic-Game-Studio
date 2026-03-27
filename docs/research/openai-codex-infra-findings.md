# OpenAI Codex Infrastructure Findings

Last reviewed: `2026-03-27`

This note captures the official Codex guidance that most directly shaped this repository's infrastructure. It is intentionally short; the linked source pages remain the source of truth.

## Source pages

- Config basics: [developers.openai.com/codex/config-basic](https://developers.openai.com/codex/config-basic)
- Subagents: [developers.openai.com/codex/subagents](https://developers.openai.com/codex/subagents)
- Best practices: [developers.openai.com/codex/learn/best-practices](https://developers.openai.com/codex/learn/best-practices)
- Working with evals: [developers.openai.com/api/docs/guides/evals](https://developers.openai.com/api/docs/guides/evals)

## Findings adopted in this repo

### 1. Shared behavior belongs in project config

Official Codex docs place repo-scoped defaults in `.codex/config.toml`. This repo uses that file for shared model, sandbox, approval, web search, and subagent limits.

### 2. Recursive delegation should stay conservative

The subagents docs say `agents.max_depth` defaults to `1` and recommend keeping that default unless recursive delegation is explicitly needed. This repo adopts that policy and treats deeper nesting as an exception that should be documented.

### 3. Narrow custom agents are safer than broad super-agents

The subagents docs emphasize focused roles such as `explorer`, `reviewer`, and `docs_researcher`, with each role keeping a clear tool surface and responsibility boundary. This repo follows that pattern by favoring specialized agents over general-purpose role blobs.

### 4. Review policy should be explicit and durable

OpenAI's Codex guidance repeatedly centers review on correctness, security, regressions, and missing tests. This repo interprets that as a reason to keep a dedicated review checklist in `docs/reference/code-review.md` instead of overloading the root instruction file.

### 5. Instruction changes deserve an eval surface

The official docs expose a dedicated evaluation surface, which is a strong signal that prompt and workflow changes should be measured, not just reasoned about. This repo therefore treats shared instruction, agent, and routing changes as eval-worthy changes.

### 6. Cached web search is the safer default for local work

Config basics states that cached web search is the default and reduces exposure to prompt injection from arbitrary live content, while still requiring normal skepticism toward results. This repo keeps `web_search = "cached"` unless a task explicitly needs live freshness.

## Resulting repo guardrails

- review risky changes with `docs/reference/code-review.md`
- create `eval-plan-*.md` files for meaningful instruction or workflow changes
- keep root instructions concise and move detailed policy into dedicated docs
- keep subagent depth conservative unless a documented workflow needs more
