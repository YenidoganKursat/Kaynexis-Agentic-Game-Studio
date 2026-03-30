# Codex Model Guide Example

Use this example when the task is about choosing a model or plan tier before work starts.

## Example 1: Broad refactor

Prompt:

> Refactor the Unity inventory HUD so the item definitions, runtime slots, and save projection stay separate.

Recommended choice:

- Model: `gpt-5.4`
- Reasoning: medium or high
- Why: the task needs broad reasoning across several files and should preserve ownership boundaries

## Example 2: Cheap helper or subagent

Prompt:

> Extract the inventory item names from the latest content sheet and classify them by rarity.

Recommended choice:

- Model: `gpt-5.4-nano`
- Reasoning: low or medium
- Why: this is a high-volume, low-branching task that mostly needs speed and cost control

## Example 3: Parallel specialist work

Prompt:

> Split the UI flow, save migration, and input remap work into three small specialist passes.

Recommended choice:

- Model: `gpt-5.4-mini`
- Reasoning: medium
- Why: the task benefits from cheaper fan-out and specialist workers more than from one large pass

## Example 4: Final hard pass

Prompt:

> Review the architecture for a late-stage release and decide if the state, event, and projection boundaries are still correct.

Recommended choice:

- Model: `gpt-5.4-pro`
- Reasoning: high or xhigh
- Why: the task is correctness-sensitive and can justify extra compute

## Example 5: Plan-tier decision

Prompt:

> Choose the right ChatGPT plan tier for a developer who wants to use the Codex app every day and occasionally test developer mode.

Recommended choice:

- Surface: ChatGPT / Codex app
- Plan fit: `Plus` for a solo developer, or `Pro` if the user wants the strongest personal surface and developer-mode access
- Why: the task is about access and rate-limit fit, not just model quality

## Example 6: Sub-agent override

Prompt:

> Define a role matrix for a multi-agent UI and QA pass, then let the technical director use a stronger model while the QA lane stays cheap.

Recommended choice:

- Surface: `scripts/codex_studio.py next`
- Agent override: `technical_director=gpt-5.4-pro`, `qa_lead=gpt-5.4-mini`
- Why: each lane keeps its default, but the user can trade precision and cost per specialist when the task fans out

## What the agent should record

When this choice matters, write down:

- the task surface
- the selected model
- the plan tier if relevant
- the fallback if the first choice fails
- the next validation step
