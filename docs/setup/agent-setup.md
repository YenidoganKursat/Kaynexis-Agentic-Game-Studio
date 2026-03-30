# Agent Setup

Use this guide when you want to install or bootstrap the Codex agent stack on a fresh machine or new clone.

The repo does not need a separate background service for agents. The main runtime install is the Codex CLI; the actual agent system is carried by repo files such as `AGENTS.md`, `.codex/agents/*.toml`, and `.agents/skills/`.

## What is installed

| Layer | What it is | Why it matters |
| --- | --- | --- |
| Codex CLI | `npm i -g @openai/codex` | Gives you the command surface for routing, checks, journals, and local helpers |
| Agent operating model | `AGENTS.md`, `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md` | Keeps the single-specialist default, controller, and panel choices explicit |
| Role matrix | `docs/reference/agent-portfolio.md`, `docs/reference/agent-hierarchy.md` | Lets the controller choose single-agent or multi-agent work deliberately |
| Execution packet | `docs/reference/agent-execution.md`, `docs/examples/agent-execution-example.md` | Keeps the owner, mode, proof path, custom rules, and stop conditions explicit before work starts |
| Review trail | `docs/reference/prompt-journal.md`, `docs/reference/agent-transcript.md` | Keeps prompt history and agent conversations reviewable later |
| Metadata checks | `scripts/validate_agent_metadata.py`, `scripts/run_local_evals.py` | Proves the agent stack is still aligned after edits |

## Recommended install order

1. Install Python `3.11+`, Git, and the Codex CLI.
2. Clone the repo and keep the hidden folders (`.codex/`, `.agents/`) intact.
3. Run `python3 scripts/setup_repo.py --init-git` if the repo is not already initialized.
4. Run `python3 scripts/codex_studio.py doctor` to confirm the repo can see the agent and setup contract.
5. Read `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, and `docs/reference/agent-hierarchy.md`.
6. Decide whether the task should stay single-specialist or fan out into a small panel.
7. Validate the agent metadata before you claim the setup is complete.

## Single specialist default

Keep this available at all times.

- Use one specialist when the task is narrow and the validation loop is obvious.
- Keep the controller visible even when only one specialist is active.
- Use the panel only when the work genuinely needs multiple bounded roles.

## Multi-agent optional

If the work needs more than one lane, use the controller model already documented in the repo:

- `Kaynexis` for the controller title
- specialist lanes with stable internal role ids
- reporting lines for the panel
- append-only prompt journal and transcript trails

The point is not to create more agents by default. The point is to make the split explicit when it helps.

## Common setup commands

```bash
python3 scripts/codex_studio.py next "Describe the next task"
python3 scripts/codex_studio.py checklist --task "Describe the next task"
python3 scripts/codex_studio.py doctor
python3 scripts/codex_studio.py journal prompt "Describe a prompt history entry"
python3 scripts/codex_studio.py journal agent "Describe an agent note"
python3 scripts/codex_studio.py journal transcript "Describe a conversation turn"
python3 scripts/codex_studio.py packet --task "Describe a work packet" --goal "Keep the owner and proof path explicit"
python3 scripts/validate_agent_metadata.py --json
```

## Environment

- `OPENAI_API_KEY` for OpenAI API-powered helper scripts
- `GH_TOKEN` for GitHub CLI flows when needed
- `SENTRY_AUTH_TOKEN` only when you use the Sentry helper flows

Do not treat those as required for the basic repo bootstrap. They are optional integrations.

## Validation

Run these after changing the agent stack, controller flow, or role layout:

```bash
python3 scripts/validate_agent_metadata.py --json
python3 scripts/run_local_evals.py --json
python3 -m pytest -q tests/test_studio_system.py
make validate
```

If the change affects shared instructions, routing, or the controller policy, also pair it with an eval plan before you call it done.

## Primary sources

- [OpenAI Developers](https://developers.openai.com/)
- [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk)
- [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
- [OpenAI/Codex infra findings](../research/openai-codex-infra-findings.md)
- [OpenAI/Codex models](../research/openai-codex-models.md)
- [Codex compatibility](../reference/codex-compatibility.md)
- [Codex model guide](../reference/codex-model-guide.md)

## Related docs

- [Agent System](../reference/agent-system.md)
- [Mastermind Guide](../reference/mastermind-guide.md)
- [Agent Portfolio](../reference/agent-portfolio.md)
- [Agent Hierarchy](../reference/agent-hierarchy.md)
- [Prompt Journal](../reference/prompt-journal.md)
- [Agent Transcript](../reference/agent-transcript.md)
- [Agent Execution Packet](../reference/agent-execution.md)
- [Agent Guide](../reference/agent-guide.md)
- [Quick Access](quick-access.md)
- [Getting Started](getting-started.md)
