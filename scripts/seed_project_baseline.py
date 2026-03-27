#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _studio_common import ACTIVE_DIR, append_preset_pack, build_bootstrap_replacements, humanize_slug, write_text


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
    version = engine_version if engine_version != "TBD" else "4.x baseline" if engine == "godot-4" else "TBD"
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
- Release: add engine-native export jobs once the real project is wired

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
- Build the first core gameplay slice
- Establish one repeatable validation path
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Engine-native files are not in the repo yet | Owner: technical_director | Mitigation: land the first engine scaffold
- Runtime and tests are still placeholder-only | Owner: lead_programmer | Mitigation: add the first real slice and at least one validation artifact
- GitHub remote and rulesets are not configured yet | Owner: producer | Mitigation: create remote and apply maintainer setup doc

## Definition of done
- Implementation done for the first slice
- Validation done locally and documented
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
    parser.add_argument("--engine-version", default="TBD")
    parser.add_argument("--platform", default="pc-premium")
    parser.add_argument("--genre", default="action-roguelite")
    args = parser.parse_args()

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
        "preset-pack.md",
    ]:
        print(f"- {ACTIVE_DIR / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
