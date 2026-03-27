# Risk Register — kaynexisGame

## Risk table
| Risk | Area | Severity | Probability | Mitigation | Owner |
|---|---|---|---|---|---|
| Local Godot runtime is missing on contributor machines | Tech | Medium | High | Document `GODOT_BIN`, add runtime smoke script, and keep static smoke as the baseline fallback | Technical Director |
| Scope grows before the first slice is validated | Production | High | Medium | Freeze first-slice goals and gate expansions behind QA evidence | Producer |
| Combat readability loses clarity as features are added | Design | Medium | Medium | Test one encounter loop before adding system depth | Game Designer |
| GitHub policy is configured too late | Ops | Medium | Medium | Apply CODEOWNERS, rulesets, and workflows before broader collaboration | Maintainer |

## Escalation notes
- Re-plan if runtime smoke or a real export cannot be exercised before the next milestone boundary
- Cut scope before adding secondary systems
- Delay external sharing until engine-native build/export validation exists
