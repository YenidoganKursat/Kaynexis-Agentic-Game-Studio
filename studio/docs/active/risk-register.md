# Risk Register — Kaynexis Agentic Game Studio

## Risk table
| Risk | Area | Severity | Probability | Mitigation | Owner |
|---|---|---|---|---|---|
| Engine assumptions drift from the actual project | Tech | High | Medium | Confirm engine-native files and update engine profile early | Technical Director |
| Starter-kit parity drifts between Godot, Unity, and Unreal | Tech | Medium | Medium | Validate manifests and scaffold markers on every CI-equivalent run | Technical Director |
| Scope grows before the first slice is validated | Production | High | Medium | Freeze first-slice goals and gate expansions behind QA evidence | Producer |
| Combat readability loses clarity as features are added | Design | Medium | Medium | Test one encounter loop before adding system depth | Game Designer |
| Hosted ruleset drifts away from actual workflow coverage | Ops | Medium | Medium | Audit `main` ruleset whenever workflow triggers or required checks change | Maintainer |
| Protected build assumptions drift from trust-boundary or symbol-policy rules | Release | High | Medium | Keep the release-hardening guide, checklist, and eval plan in the same bundle as the release path | Release Manager |

## Escalation notes
- Re-plan if runner-backed engine-native validation is not wired into CI this sprint
- Cut scope before adding secondary systems
- Delay external sharing until engine-native build/export validation exists
