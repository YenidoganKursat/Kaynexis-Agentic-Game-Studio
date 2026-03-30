# Agent Validation Matrix Example

## Scope

- A broad multi-agent UI and QA pass that might stay single-specialist, split into a pair, or fan out into a small panel

## Baseline

- The repo already has a controller, a role matrix, a hierarchy, prompt history, and an agent transcript.
- The user wants a simple answer even when the internal validation path branches.

## Decision order

1. Decide whether the task can stay single-specialist.
2. If not, decide whether a pair is enough.
3. If not, decide the smallest panel that still keeps ownership narrow.
4. Decide whether the work needs a hierarchy and async packet shape.
5. Decide whether the work needs prompt history, transcript, or model overrides.

## Example validation matrix

| Mode | What to prove | Pass signal | Evidence |
| --- | --- | --- | --- |
| Single specialist | One lane can safely own the answer | One clear owner, one narrow proof path | Route output, checklist, or manual smoke |
| Paired specialist | One doer plus one validator is enough | The validator catches the risky edge | Review note, QA note, or small smoke |
| Multi-agent panel | The task really crosses boundaries | Each lane owns one scope and one output | Role matrix, handoff map, and output bundle |
| Hierarchy | Titles and reporting lines matter | Every lane reports upward once | Command tree and async packet |
| Transcript | The work should be reopened later | Assignments and replies stay append-only | Transcript file plus prompt history link |
| Model override | One lane needs a different speed/precision tradeoff | Defaults and overrides stay visible | Route output with `--agent-model` details |

## Good agent prompts

- "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible."
- "Keep the controller simple, then prove whether a pair or a panel is needed with one small matrix."
- "Show the role matrix, hierarchy, transcript, and lane model overrides in one reviewable bundle."

## Validation

- Open `docs/reference/agent-validation-matrix.md` and confirm the matrix catalog matches the task.
- Run `python3 scripts/codex_studio.py checklist --task "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible" --json`.
- Confirm the output names the operating mode, the lane split, and the proof path.

## Related docs

- `docs/reference/agent-validation-matrix.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/codex-model-guide.md`
