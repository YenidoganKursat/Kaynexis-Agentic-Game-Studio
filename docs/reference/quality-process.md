# Quality Control Process

Use this page when the task is about running a quality pass, reviewing a refactor, or deciding whether an optimization is actually worth doing.

`quality-guide.md` defines the rubric. This page defines the operating loop.

## Summary

- Quality work should be explicit about ownership, proof, and decision gates.
- A pass is not complete until the validation path is narrow, evidence is recorded, and the go/no-go decision is clear.
- If the change crosses engine, architecture, or performance boundaries, the same vocabulary should appear in the guide, example, checklist, and eval notes.

## Control loop

| Step | Question | Output |
| --- | --- | --- |
| Frame the change | What player or operator outcome should improve? | One-sentence scope statement |
| Name ownership | Who owns runtime truth, shared data, and editor/tooling? | Ownership model |
| Choose proof | What test, smoke, or manual loop proves the change? | Validation path |
| Gather evidence | What command output, artifact, or transcript proves the result? | Evidence list |
| Decide optimization | If tuning is involved, what is the baseline, first lever, and fallback lever? | Measurement note |
| Align globally | Which docs, examples, checklists, or evals must change with the code? | Update list |

## Test and evaluation order

1. Read the quality guide and the matching example first.
2. Name the ownership model and the narrowest validation path.
3. Write or update the smallest automated test, smoke, or manual loop that proves the change.
4. If the task changes instructions, routing, or global behavior, add or update the matching eval notes.
5. If optimization is in scope, capture the baseline before tuning and keep the fallback lever explicit.
6. Keep the docs, checklist, and validation output in the same change so the review bundle stays coherent.

## Global alignment

- Use the same short canonical names across docs, checklists, routes, and examples.
- Keep the quality guide, quality process, example, checklist, and eval aligned together.
- Do not let one doc say "optimization" while another doc still talks only about cleanup or maintainability.
- Keep the same ownership terms in every engine family: runtime owner, shared data owner, editor owner, validation path.

## Engine-specific notes

### Godot 4
- Keep scene ownership, `Resource` ownership, and editor-tool ownership separate.
- Prefer static smoke first, then runtime smoke when the local binary exists.
- Treat `@tool` and server-style scale choices as measured decisions, not defaults.

### Unity 6
- Keep `GameObject`, `MonoBehaviour`, `ScriptableObject`, and editor-only code in separate lanes.
- Prefer EditMode or PlayMode tests plus a manual validation loop for user-facing changes.
- Use pooling and `NonAlloc` paths before reaching for heavier scale systems.

### Unreal 5
- Keep `AActor`, `UActorComponent`, `UObject`, and Data Asset ownership clear.
- Prefer Blueprint compile, Details-panel checks, and PIE/SIE before packaging work.
- Use instancing, Mass, or GAS only when the scale or authority problem is proven.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate"
python3 scripts/codex_studio.py checklist --task "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate"
python3 scripts/codex_studio.py next "Review a Godot combat room and keep the quality process, proof path, and ownership model explicit"
python3 scripts/codex_studio.py next "Compare Unreal quality checks for an Actor, component, and Data Asset refactor before tuning"
```

## Related docs

- `docs/reference/quality-guide.md`
- `docs/examples/quality-example.md`
- `docs/examples/quality-process-example.md`
- `docs/reference/code-review.md`
- `docs/reference/perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/system-atlas.md`
- `docs/reference/agent-guide.md`
- `docs/research/game-development/foundations/quality.md`
