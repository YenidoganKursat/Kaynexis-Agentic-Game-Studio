# Platform Readiness: PC, Web, Mobile, and Console

## Date
- 2026-03-28

## Summary
- Platform readiness should not start at the packaging step. Each platform family shifts what "done" means for input, performance, save behavior, startup flow, storefront metadata, and recovery from failure.
- PC and web often tolerate iteration speed but expose hardware and browser variance. Mobile adds thermal, session-length, touch UX, and store-review constraints. Console adds stricter submission, entitlement, suspend/resume, and certification expectations.
- The repo should therefore treat platform readiness as a first-class planning surface, not a release-week checklist.
- A safe early rule is: every milestone should name the current primary platform, the next target platform, and the biggest delta between them.

## Primary sources
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Android quality guidelines](https://developer.android.com/docs/quality-guidelines)
- [MDN Performance guide](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Microsoft game development documentation](https://learn.microsoft.com/en-us/gaming/)

## Why this matters to this repo
- This repo already routes release, porting, and mobile work, but without a durable platform note the advice stays too generic.
- Tasks about mobile, web builds, console submission, or PC storefront launch should surface platform deltas early:
  - control assumptions
  - memory and performance budgets
  - suspend/resume behavior
  - save path expectations
  - storefront and certification constraints
- Platform-target docs should become a living risk surface, not a late packaging note.

## Decision impact
- Release, porting, and mobile tasks should surface this note by default.
- `studio/docs/active/platform-targets.md` should explicitly name platform deltas, not just target names.
- Checklists and examples should assume one primary platform and one next platform rather than vague "ship everywhere" intent.

## Platform deltas

### PC
- Watch first:
  - hardware variance
  - graphics/options scalability
  - keyboard/mouse vs controller parity
  - patch and branch workflow
- Typical first failure:
  - the build technically launches but lacks robust options, controller handling, or reproducible crash evidence

### Web
- Watch first:
  - load time
  - asset size
  - browser memory limits
  - tab focus and pause behavior
  - keyboard/mouse capture quirks
- Typical first failure:
  - the game runs locally but collapses under browser startup cost, memory pressure, or input focus loss

### Mobile
- Watch first:
  - touch-first readability
  - short session rhythm
  - battery and thermal behavior
  - interrupted-session recovery
  - store-review safe UX
- Typical first failure:
  - the game feels like a shrunk desktop build rather than a mobile-shaped experience

### Console
- Watch first:
  - suspend/resume behavior
  - entitlement and account assumptions
  - controller-only flows
  - save integrity
  - platform-holder certification requirements
- Typical first failure:
  - a build that is content-complete but not certification-safe or controller-complete

## What to watch out for
- Calling a port "minor" when input, save, or performance assumptions are actually different
- Treating web like PC with smaller buttons
- Treating mobile as only a rendering/perf problem
- Leaving platform compliance notes outside the repo because the work feels "later"
- Failing to name which platform owns design decisions when targets conflict
