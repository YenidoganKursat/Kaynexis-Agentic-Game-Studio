#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _studio_common import ACTIVE_DIR, append_preset_pack, build_bootstrap_replacements, default_engine_version, humanize_slug, write_text


def engine_label(engine: str) -> str:
    mapping = {
        "godot-4": "Godot 4",
        "unity-6": "Unity 6",
        "unreal-5": "Unreal 5",
    }
    return mapping.get(engine, humanize_slug(engine))


def platform_label(platform: str) -> str:
    mapping = {
        "pc-premium": "PC Premium",
        "console-premium": "Console Premium",
        "mobile-f2p": "Mobile F2P",
        "web-demo": "Web Demo",
        "vr-prototype": "VR Prototype",
    }
    return mapping.get(platform, humanize_slug(platform))


def seed_art_direction_lite(project_name: str, genre_name: str) -> str:
    return f"""# Art Direction Lite — {project_name}

## Visual pillars
- Clear silhouettes and readable threat timing over decoration-first detail
- Strong foreground-vs-background separation so encounter readability survives content growth
- A restrained but distinctive mood board that supports a {genre_name.lower()} reference slice

## Readability rules
- Enemy telegraphs need unique shape and color language before extra VFX are added
- HUD accents should never be brighter than critical world-space danger cues
- Interactive props should read differently from decorative dressing at a glance

## Reference cues
- High-contrast combat readability
- Compact arena compositions with low clutter
- Materials and palette chosen for fast scanability, not realism

## Production notes
- Favor reusable modular pieces and low-risk placeholder art over one-off hero assets early
- Lock a small palette before expanding environment scope
- Treat every added VFX layer as a readability review item, not a free embellishment
"""


def seed_audio_direction_lite(project_name: str) -> str:
    return f"""# Audio Direction Lite — {project_name}

## Audio pillars
- Critical gameplay timing cues always cut through the mix
- Audio feedback reinforces state changes before it chases spectacle
- The room should feel tense and reactive without drowning out player input feedback

## Mix hierarchy
- Highest priority: damage windows, dodge success, incoming threat pulses
- Secondary: enemy loop, room state changes, upgrade selection feedback
- Tertiary: ambience and musical support that can duck under combat-critical cues

## Event priorities
- Dodge success and failure need different envelopes and tonal identity
- Enemy pulse wind-up should be readable even with effects-heavy visuals
- Upgrade reward should feel distinct from combat resolution

## Implementation notes
- Start with engine-native playback unless a middleware need is proven
- Keep one-shot variation lightweight and deterministic
- Review repeated combat cues for fatigue before adding content scale
"""


def seed_telemetry_schema(project_name: str, genre_first_feature: str) -> str:
    return f"""# Telemetry Schema — {project_name}

## Questions to answer
- Do players understand the first playable slice around `{genre_first_feature}`?
- Where do players fail, reset, or abandon the combat room?
- Which upgrade choices are selected and which ones are ignored?

## Event catalog
| Event | Trigger | Key properties | Why it matters |
|---|---|---|---|
| session_start | App enters playable state | platform, build, locale | Session health baseline |
| combat_room_start | Player enters the first room | room_id, difficulty_seed | Funnel entry |
| combat_room_fail | Player loses the room or resets | fail_reason, remaining_health | Readability and balance signal |
| combat_room_clear | Player defeats the encounter | clear_time_s, damage_taken | Core loop validation |
| upgrade_selected | Player chooses a reward | upgrade_id, offered_ids | Build-choice usefulness |

## Privacy & safety
- Avoid personal identifiers and free-form text
- Keep event payloads minimal and slice-focused
- Separate local debug logs from any eventual shipped telemetry backend

## Validation
- Validate event firing in local logs before wiring external telemetry
- Document every schema change in the decision log
- Reject instrumentation that cannot answer a concrete design or quality question
"""


def seed_localization_glossary(project_name: str) -> str:
    return f"""# Localization Glossary — {project_name}

## Term list
| Source term | Meaning | Notes | Do not translate? |
|---|---|---|---|
| Pulse Warden | First encounter enemy | Keep encounter naming consistent across UI and docs | No |
| Dash Window | Short timing window for safe evade | Avoid mixing with generic dodge wording in tutorials | No |
| Upgrade Choice | Between-room reward selection | Use consistently in HUD, docs, and test plans | No |

## Formatting constraints
- Preserve input prompts and tokenized values
- Keep combat callouts short enough for HUD and subtitle overlays
- Avoid puns or culture-specific shorthand in critical instruction text

## Text expansion risks
- Short HUD labels may need wider containers in localized builds
- Tutorial prompts can become unreadable if multiple verbs expand at once
- Upgrade card layouts should allow for longer nouns than English defaults
"""


def seed_monetization_guardrails(project_name: str) -> str:
    return f"""# Monetization Guardrails — {project_name}

## Allowed patterns
- Premium purchase with transparent scope and no hidden monetization layers
- Optional soundtrack or cosmetic extras only if they do not distort game balance

## Disallowed patterns
- Pay-to-win progression shortcuts
- Manipulative timers, energy systems, or opaque scarcity pressure
- Reward structures that push players into external storefront decisions mid-run

## Review questions
- Does the monetization choice preserve player trust?
- Can the design still stand on its own without the monetization layer?
- Would a first-time player understand the offering without reading legal fine print?

## Comms notes
- State the premium-first stance clearly in public-facing material
- If paid extras ever exist, separate them from gameplay power
- Update this doc before any pricing or DLC discussions leave prototype territory
"""


def seed_content_pipeline(project_name: str, engine_name: str) -> str:
    return f"""# Content Pipeline — {project_name}

## Content types
- Engine-native scenes/prefabs/maps
- Gameplay data such as enemy archetypes, encounters, and upgrade definitions
- UI, VFX, audio, and documentation needed to validate the slice

## Authoring flow
- Designers define feature intent in active docs before content scale grows
- Runtime content lands in the engine-specific project layer and keeps naming deterministic
- Tooling or import helpers belong in `tools/` or `scripts/`, not inside ad-hoc content folders

## Validation & naming
- Names should reflect gameplay purpose, not temporary author shorthand
- New content should link to at least one validation path: test, smoke, or manual QA artifact
- Treat engine-specific import settings as part of the review surface for {engine_name}

## Ownership & change management
- Technical direction owns structure and import assumptions
- Design/content owners update the linked active docs when behavior or data contracts change
- Large content waves should ship with checklist coverage and at least one review note about risk
"""


def seed_game_brief(project_name: str, genre_name: str, platform_name: str) -> str:
    return f"""# Game Brief — {project_name}

## High concept
- Codex-first {genre_name} project focused on a small but high-quality first playable slice
- Target audience: players who value readable action, replayable runs, and build experimentation
- Reference titles / contrast set: Hades, Dead Cells, Risk of Rain 2

## Player fantasy
- Survive a compact high-pressure encounter and come out stronger through clear build choices
- Keep playing to master combat readability and discover stronger run combinations

## Core pillars
- Readable moment-to-moment combat
- Short sessions with meaningful upgrade choice
- A small vertical slice that can grow without losing clarity

## Scope guardrails
- In scope: first combat room, basic enemy telegraphs, one upgrade choice, PC-first controls
- Out of scope: full metaprogression, content volume, liveops, monetization, multiplayer
- Nice-to-have later: expanded build diversity, content scale, external demo polish

## Platforms & business model
- Platforms: {platform_name}
- Input assumptions: keyboard/mouse plus controller parity
- Pricing / monetization stance: premium-first baseline with no F2P systems in the first slice

## Milestone target
- Prototype -> vertical slice
- Exit criteria: one stable, replayable combat slice with clear validation and genre fit

## Operating loop
- Route work with `python3 scripts/codex_studio.py next "..."`
- Resolve the checklist bundle with `python3 scripts/codex_studio.py checklist --task "..."`
- Link or create research in `docs/research/game-development/`
- Update `studio/docs/active/current-sprint.md` and `studio/docs/active/decision-log.md` as the slice changes

## Known risks
- Readability can collapse before depth is proven
- Scope can grow faster than validation
- Engine and build assumptions still need to be confirmed with real project files
"""


def seed_engine_profile(project_name: str, engine: str, engine_version: str, platform_name: str) -> str:
    label = engine_label(engine)
    version = engine_version or default_engine_version(engine)
    return f"""# Engine Profile — {project_name}

## Engine
- Engine: {label}
- Version: {version}
- Rendering path / pipeline: confirm once real engine-native project files land

## Repository layout
- Shared studio config: `studio.toml`
- Front-door workflow: `scripts/codex_studio.py`
- Expected runtime code: `src/`
- Expected content/assets: `assets/`
- Expected tests or manual validation artifacts: `tests/`
- Expected tools/import helpers: `tools/`

## Build targets
- Primary platforms: {platform_name}
- Export/package notes: PC-first baseline, controller support expected, artifact names should stay deterministic
- CI/build assumptions: local checks via `make ci-local`, starter-kit validation via `python3 scripts/validate_engine_kits.py`, optional container check via `make docker-verify`, GitHub workflows for validation and Docker smoke

## Starter-kit parity
- Supported engine families: Godot 4, Unity 6, Unreal 5
- Primary engine for this project: {label}
- Engine-specific caveats and research should be linked from `docs/research/game-development/engines/`

## Core technical constraints
- Performance target: stable 60 FPS on target PC baseline
- Save/network assumptions: local save-safe behavior, no netcode in the first slice
- Native plugins / SDKs: none by default until explicitly added

## Validation workflow
- Fast local checks: `make validate`, `python3 scripts/run_local_evals.py`
- Full validation path: `make ci-local` plus engine-native smoke once the actual project exists
- Release gating notes: add engine-native build/export validation before external demos or shipping branches
"""


def seed_platform_targets(project_name: str, platform_name: str) -> str:
    return f"""# Platform Targets — {project_name}

## Supported platforms
| Platform | Priority | Input | Perf target | Special constraints |
|---|---|---|---|---|
| {platform_name} | Primary | Keyboard/mouse + controller | 60 FPS target | Settings scalability and sane defaults |

## Store / submission notes
- PC storefront readiness should include screenshots, controller support notes, and a demo-friendly build path

## Input & UX implications
- Keyboard/mouse must feel native
- Controller parity should exist before external playtests
- Accessibility should cover subtitle readability, remappable controls where practical, and clear feedback
"""


def seed_build_pipeline(project_name: str) -> str:
    return f"""# Build Pipeline — {project_name}

## Build graph
- Source -> route/checklist/research alignment -> repo validation -> starter-kit validation -> local evals -> engine-native smoke -> package -> artifact -> distribution

## Environments
- Local: `make ci-local`
- Front door: `python3 scripts/codex_studio.py`
- CI: `.github/workflows/repo-validate.yml`
- Container check: `.github/workflows/docker-smoke.yml` and `make docker-verify`
- Adapter contract smoke: repo-local Unity/Unreal tool stubs keep dry-run checks honest in CI
- Release: real editor/export jobs only count as complete once engine binaries are present on the runner

## Engine contracts
- Godot 4: `python3 scripts/godot_smoke.py --static-only`, optional runtime smoke, then `python3 scripts/godot_export.py --preset "..."`
- Unity 6: use `tools/engine-stubs/unity/Unity` for command-contract smoke; switch to a real `UNITY_CLI` path for editor-backed tests/builds
- Unreal 5: use `tools/engine-stubs/unreal/RunUAT.sh` for command-contract smoke; switch to a real `UNREAL_UAT` or `UNREAL_EDITOR` path for packaging work

## Artifacts & versioning
- Keep artifact names deterministic
- Store release notes, validation commands, and build provenance alongside artifacts
- Add symbols or crash artifacts once the engine-specific build pipeline exists

## Failure / rollback
- If validation or evals regress, stop before merge
- If Docker or workflow changes break, revert the smallest change first
- Record release or infra regressions in `studio/docs/active/risk-register.md` and an eval plan when shared behavior changed
"""


def seed_current_sprint(project_name: str, genre_first_feature: str) -> str:
    return f"""# Current Sprint — {project_name}

## Sprint goal
- Prove the first playable slice around `{genre_first_feature}`

## In scope
- Confirm engine and repo layout decisions
- Confirm `studio.toml`, starter-kit, and checklist assumptions
- Harden the Godot reference slice so it stays trustworthy
- Keep Unity and Unreal support honest at adapter/contract level until real editor automation is configured
- Establish one repeatable validation path
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Real Unity and Unreal tool paths are still external | Owner: technical_director | Mitigation: keep adapter contracts green with stubs, then wire real CLI/UAT paths before claiming full editor integration
- Runtime export confidence still depends on a local Godot binary or a runner with Godot installed | Owner: lead_programmer | Mitigation: keep static smoke green and add runtime smoke where `GODOT_BIN` is available
- GitHub remote and rulesets are not configured yet | Owner: producer | Mitigation: create remote and apply maintainer setup doc

## Definition of done
- The first slice remains fair, bounded, and validated
- Validation is documented locally and mirrored in CI without fake tool-path confidence
- Docs, checklist output, and research links updated to reflect the real project state instead of template assumptions
"""


def seed_risk_register(project_name: str) -> str:
    return f"""# Risk Register — {project_name}

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
"""


def seed_milestones(project_name: str, genre_first_feature: str) -> str:
    return f"""# Milestones — {project_name}

## Milestones
| Milestone | Goal | Exit criteria | Target window | Risks |
|---|---|---|---|---|
| Prototype | Prove the core loop and repo operating model | `{genre_first_feature}` is playable, documented, and validated | Near-term | Engine drift, scope creep |
| Vertical Slice | Prove quality bar and retention promise | One polished slice with clear content, UX, performance bar, and research-backed workflow | Next milestone | Content throughput, readability |
| Demo/Beta | Prove release path and external stability | Stable external build plus store/demo readiness | Later | Build pipeline maturity, UX polish |

## Dependencies
- `studio.toml` and starter-kit manifests stay current
- Remote repository and branch ruleset setup
- Engine-native project files and export settings
- First test or manual validation artifact beyond template placeholders
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed active docs with a concrete baseline project plan.")
    parser.add_argument("--project-name", default=Path.cwd().name)
    parser.add_argument("--engine", default="godot-4")
    parser.add_argument("--engine-version")
    parser.add_argument("--platform", default="pc-premium")
    parser.add_argument("--genre", default="action-roguelite")
    args = parser.parse_args()
    args.engine_version = args.engine_version or default_engine_version(args.engine)

    replacements = build_bootstrap_replacements(args.project_name, args.engine, args.engine_version, args.platform, args.genre)
    genre_name = replacements["GENRE_NAME"]
    platform_name = platform_label(args.platform)

    write_text(ACTIVE_DIR / "game-brief.md", seed_game_brief(args.project_name, genre_name, platform_name))
    write_text(ACTIVE_DIR / "engine-profile.md", seed_engine_profile(args.project_name, args.engine, args.engine_version, platform_name))
    write_text(ACTIVE_DIR / "platform-targets.md", seed_platform_targets(args.project_name, platform_name))
    write_text(ACTIVE_DIR / "build-pipeline.md", seed_build_pipeline(args.project_name))
    write_text(ACTIVE_DIR / "current-sprint.md", seed_current_sprint(args.project_name, replacements["GENRE_FIRST_FEATURE"]))
    write_text(ACTIVE_DIR / "risk-register.md", seed_risk_register(args.project_name))
    write_text(ACTIVE_DIR / "milestones.md", seed_milestones(args.project_name, replacements["GENRE_FIRST_FEATURE"]))
    write_text(ACTIVE_DIR / "art-direction-lite.md", seed_art_direction_lite(args.project_name, genre_name))
    write_text(ACTIVE_DIR / "audio-direction-lite.md", seed_audio_direction_lite(args.project_name))
    write_text(ACTIVE_DIR / "telemetry-schema.md", seed_telemetry_schema(args.project_name, replacements["GENRE_FIRST_FEATURE"]))
    write_text(ACTIVE_DIR / "localization-glossary.md", seed_localization_glossary(args.project_name))
    write_text(ACTIVE_DIR / "monetization-guardrails.md", seed_monetization_guardrails(args.project_name))
    write_text(ACTIVE_DIR / "content-pipeline.md", seed_content_pipeline(args.project_name, engine_label(args.engine)))
    append_preset_pack(engine=args.engine, platform=args.platform, genre=args.genre, replace=True)

    print("Seeded baseline docs:")
    for name in [
        "game-brief.md",
        "engine-profile.md",
        "platform-targets.md",
        "build-pipeline.md",
        "current-sprint.md",
        "risk-register.md",
        "milestones.md",
        "art-direction-lite.md",
        "audio-direction-lite.md",
        "telemetry-schema.md",
        "localization-glossary.md",
        "monetization-guardrails.md",
        "content-pipeline.md",
        "preset-pack.md",
    ]:
        print(f"- {ACTIVE_DIR / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
