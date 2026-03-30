# UX

## Date
- 2026-03-28

## Summary
- Game feel, usability, and accessibility are related but distinct. Good feel is about responsive, legible, satisfying action; usability is about whether the player can understand and operate the system; accessibility is about whether players with different needs can meaningfully access the experience.
- A game can feel good for a narrow group and still be unusable or inaccessible. Likewise, a clean UI can still fail if action timing, feedback, or assist options are weak.
- For this repo, these concerns should be treated as part of core architecture and feature design, not as a late pass. Input, timing windows, information hierarchy, subtitle and caption support, remapping, contrast, and feedback all shape whether the system can scale.

## Primary sources
- Swink, "Game Feel: A Game Designer's Guide to Virtual Sensation" review and summary paper — https://arxiv.org/abs/2011.09201
- Nielsen Norman Group, "10 Usability Heuristics for User Interface Design" — https://www.nngroup.com/articles/ten-usability-heuristics/
- Microsoft Gaming Accessibility Guidelines — https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
- Game Accessibility Guidelines — https://accessiblegames.com/
- IGDA Game Accessibility SIG resources — https://igda-gasig.org/get-involved/sig-initiatives/resources-for-game-developers/sig-guidelines/

## Why this matters to this repo
- Many game-repo failures show up first as "this feels off" or "players get confused." Those are often not content problems; they are architecture problems around control, feedback, prioritization, and assist support.
- Codex can generate UI flows and mechanic implementations quickly, but it needs durable guidance so it does not optimize for novelty or visual complexity while sacrificing legibility.
- The repo already treats checklists and research as first-class. This note gives those surfaces a common vocabulary for readable action, understandable interfaces, and accessible input or feedback systems.

## Decision impact
- Feature briefs that change core verbs, UI, or onboarding should explicitly state which feedback, usability, and accessibility assumptions they depend on.
- Input, HUD, and combat-related tasks should surface these concerns early instead of filing them under late QA.
- Engine-specific implementations should preserve the same intent: clear action confirmation, deterministic feedback order, remap support, scalable text, caption strategy, and visual or auditory redundancy where appropriate.

## Practical framing
- Game feel questions:
  - Is the action acknowledged immediately?
  - Is the success or failure state readable within the first beat of input?
  - Are anticipation, impact, recovery, and cooldown legible enough to support mastery?
- Usability questions:
  - Can a new player understand what the system wants and what changed after an action?
  - Is screen hierarchy obvious under pressure?
  - Are state changes, errors, and dependencies visible instead of implicit?
- Accessibility questions:
  - Can the action be remapped or assisted?
  - Is critical information available through more than one channel?
  - Are timing and readability assumptions creating avoidable exclusion?

## What to watch out for
- Do not collapse accessibility into "add subtitles." Accessibility is structural across controls, timing, visuals, audio, and cognitive load.
- Do not use usability language to flatten deliberate tension. The goal is readable challenge, not sterile simplicity.
- Do not confuse noisy feedback with strong feedback. More flashes, more particles, and more sounds do not automatically create clarity.
- If a design only works for one control scheme, one sensory channel, or one timing assumption, it is fragile even before platform work begins.
