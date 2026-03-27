# Risk Register — kaynexisGame

## Risk table
| Risk | Area | Severity | Probability | Mitigation | Owner |
|---|---|---|---|---|---|
| Engine assumptions drift from the actual project | Tech | High | Medium | Confirm engine-native files and update engine profile early | Technical Director |
| Starter-kit parity drifts between Godot, Unity, and Unreal | Tech | Medium | Medium | Validate manifests and scaffold markers on every CI-equivalent run | Technical Director |
| Scope grows before the first slice is validated | Production | High | Medium | Freeze first-slice goals and gate expansions behind QA evidence | Producer |
| Combat readability loses clarity as features are added | Design | Medium | Medium | Test one encounter loop before adding system depth | Game Designer |
| GitHub policy is configured too late | Ops | Medium | Medium | Apply CODEOWNERS, rulesets, and workflows before broader collaboration | Maintainer |

## Escalation notes
- Re-plan if the first slice is not validated with real runtime files this sprint
- Cut scope before adding secondary systems
- Delay external sharing until engine-native build/export validation exists
