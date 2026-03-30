# Bugfix Eval

## Change under test

- `scripts/scaffold_bugfix.py` now writes atlas references into bug report, crash triage, test plan, and eval plan docs.
- The bugfix scaffold can now optionally create `test-plan-*.md` and `eval-plan-*.md` alongside the default bug and crash docs.
- The bugfix, feature, and eval scaffolds should now share the same atlas-first ownership language.

## Goal

- Make bug triage docs consistently point at the system atlas and engine class atlas.
- Reduce the gap between a bug report and a useful validation package.
- Make it obvious when a bugfix needs a test plan or eval plan attached.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Player gets stuck after dodge near a wall" | Common bug triage path | Creates bug and crash docs only | Creates bug, crash, test plan, and eval plan docs when flags are used |
| "Crash when opening inventory from pause" | Checks atlas language in triage docs | Bug docs may omit ownership refs | Bug/crash docs include system atlas and engine class atlas references |
| "Controller remap stops saving after restart" | Persistence-heavy bug path | Validation docs may be absent | Optional test plan and eval plan are generated for regression proof |
| "Route a bugfix that touches combat and UI" | Cross-system bugfix | Routing may stay too vague | Bugfix scaffold output stays tied to system atlas, engine class atlas, and quick map |

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Delegation restraint
- Validation honesty

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- Bugfix scaffold should not become verbose or noisy.
- Existing bug/crash docs should remain concise enough to use.
- Optional test/eval outputs should not be created unless requested.

## Exit criteria

- `scripts/scaffold_bugfix.py` generates atlas-aware bug and crash docs.
- `--with-test-plan` and `--with-eval-plan` generate the additional docs.
- Repo validation and local evals stay green.
