# Eval Plan: OpenAI / Codex Model Guidance

## Change under test

Add a repo-local model-selection guide for OpenAI / Codex tasks, including plan-tier fit guidance and routing support.

## Goal

- Keep model choice explicit instead of implicit.
- Make the model ladder easy for the agent to reopen later.
- Keep ChatGPT plan fit separate from API usage guidance.

## Risks

- Old model names can drift into new docs if we do not keep the ladder explicit.
- Plan-tier advice can be mistaken for API advice if the surface is not named.
- Route keywords may overmatch generic text if the lane is too broad.

## Validation

- `python3 scripts/route_task.py "Which OpenAI model should I use for a multi-file Codex refactor?" --json`
- `python3 scripts/route_task.py "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini --json`
- `python3 scripts/codex_studio.py checklist --task "Choose the best Codex model and ChatGPT plan tier for a heavy refactor" --json`
- `python3 scripts/codex_studio.py next "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini`
- `python3 scripts/validate_docs.py --strict`
- `python3 scripts/validate_repo_layout.py`
- `python3 -m pytest -q tests/test_studio_system.py`

## Success criteria

- The model guide is discoverable from the repo entry docs.
- The route output names the model-selection lane when the task is clearly about model choice or plan tier.
- The route output surfaces default agent models and explicit per-lane overrides when the task fans out into specialists.
- The checklist bundle includes explicit model-choice and plan-tier rules.
- The docs explain when to use `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`, and `gpt-5.4-pro`.
