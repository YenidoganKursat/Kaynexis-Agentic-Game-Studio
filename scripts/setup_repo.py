#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from bootstrap_studio import CORE_DOCS
from _studio_common import ACTIVE_DIR, PRESET_DIR, append_preset_pack, build_bootstrap_replacements, copy_template_to_active, default_engine_version, sync_active_doc_titles
from studio_core import configured_project_name, sync_studio_config

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROJECT_NAME = configured_project_name(REPO_ROOT.name)


def run_step(label: str, command: list[str]) -> int:
    print(f"==> {label}", flush=True)
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    print(flush=True)
    return result.returncode


def run_baseline_seed(args: argparse.Namespace) -> int:
    command = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "seed_project_baseline.py"),
        "--project-name",
        args.project_name,
        "--engine",
        args.engine,
        "--engine-version",
        args.engine_version,
        "--platform",
        args.platform,
        "--genre",
        args.genre,
    ]
    return run_step("Seeding baseline project docs", command)


def bootstrap_docs(args: argparse.Namespace) -> tuple[list[Path], Path]:
    replacements = build_bootstrap_replacements(args.project_name, args.engine, args.engine_version, args.platform, args.genre)

    docs = CORE_DOCS
    if args.all_templates:
        docs = sorted(p.name for p in (ACTIVE_DIR.parent / "templates").glob("*.md"))

    written = []
    for name in docs:
        dest = ACTIVE_DIR / name
        before = dest.exists()
        path = copy_template_to_active(name, replacements, overwrite=args.overwrite)
        if args.overwrite or not before:
            written.append(path)

    preset_target = ACTIVE_DIR / "preset-pack.md"
    if args.overwrite or not preset_target.exists():
        preset_target = append_preset_pack(
            engine=args.engine if (PRESET_DIR / "engine" / f"{args.engine}.md").exists() else None,
            platform=args.platform if (PRESET_DIR / "platform" / f"{args.platform}.md").exists() else None,
            genre=args.genre if (PRESET_DIR / "genre" / f"{args.genre}.md").exists() else None,
            replace=True,
        )

    return written, preset_target


def maybe_init_git(args: argparse.Namespace) -> None:
    if (REPO_ROOT / ".git").exists() or not args.init_git:
        return
    git_path = shutil.which("git")
    if not git_path:
        raise RuntimeError("Cannot initialize git because `git` is not installed.")
    subprocess.run([git_path, "init", str(REPO_ROOT)], cwd=REPO_ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="One-command bootstrap for Codex Game Studio repositories.")
    parser.add_argument("--project-name", default=DEFAULT_PROJECT_NAME)
    parser.add_argument("--engine", default="godot-4", help="Preset slug under studio/presets/engine")
    parser.add_argument("--engine-version")
    parser.add_argument("--platform", default="pc-premium", help="Preset slug under studio/presets/platform")
    parser.add_argument("--genre", default="action-roguelite", help="Preset slug under studio/presets/genre")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing active docs.")
    parser.add_argument("--all-templates", action="store_true", help="Copy every template into the active docs folder.")
    parser.add_argument("--init-git", action="store_true", help="Initialize git if .git does not exist yet.")
    parser.add_argument("--skip-hooks", action="store_true", help="Do not attempt to install git hooks.")
    parser.add_argument("--skip-bootstrap", action="store_true", help="Skip writing active docs.")
    parser.add_argument("--skip-baseline", action="store_true", help="Skip seeding baseline active docs.")
    parser.add_argument("--skip-validate", action="store_true", help="Skip validation scripts.")
    parser.add_argument("--skip-doctor", action="store_true", help="Skip the doctor health check.")
    args = parser.parse_args()
    args.engine_version = args.engine_version or default_engine_version(args.engine)

    print("Codex Game Studio Setup", flush=True)
    print("=======================", flush=True)
    print(f"Repo: {REPO_ROOT}", flush=True)
    print(f"Project: {args.project_name}", flush=True)
    print(f"Engine / version / platform / genre: {args.engine} / {args.engine_version} / {args.platform} / {args.genre}", flush=True)
    print(flush=True)

    sync_studio_config(args.project_name, args.engine, args.engine_version, args.platform, args.genre)

    try:
        maybe_init_git(args)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    if not args.skip_bootstrap:
        created, preset_target = bootstrap_docs(args)
        print("Bootstrapped active docs:", flush=True)
        if created:
            for path in created:
                print(f"- {path.relative_to(REPO_ROOT)}", flush=True)
        else:
            print("- No new docs were written; existing active docs were kept.", flush=True)
        print(f"- {preset_target.relative_to(REPO_ROOT)}", flush=True)
        print(flush=True)

    if not args.skip_baseline:
        if run_baseline_seed(args) != 0:
            return 1

    sync_active_doc_titles(args.project_name)

    if not args.skip_hooks:
        if (REPO_ROOT / ".git").exists():
            if run_step("Installing git hooks", [str(REPO_ROOT / "scripts" / "install_git_hooks.sh")]) != 0:
                return 1
        else:
            print("==> Skipping git hooks", flush=True)
            print("No .git directory detected. Initialize git first or rerun with --init-git.\n", flush=True)

    if not args.skip_validate:
        validations = [
            ("Validating repo layout", [sys.executable, str(REPO_ROOT / "scripts" / "validate_repo_layout.py")]),
            ("Validating docs", [sys.executable, str(REPO_ROOT / "scripts" / "validate_docs.py")]),
            ("Validating assets", [sys.executable, str(REPO_ROOT / "scripts" / "validate_assets.py")]),
        ]
        for label, command in validations:
            if run_step(label, command) != 0:
                return 1

    if not args.skip_doctor:
        if run_step("Running repo doctor", [sys.executable, str(REPO_ROOT / "scripts" / "doctor.py")]) != 0:
            return 1

    print("Setup complete.", flush=True)
    print("Next steps:", flush=True)
    print("- Read docs/setup/getting-started.md", flush=True)
    print("- Read docs/reference/code-review.md", flush=True)
    print("- Read docs/reference/eval-strategy.md", flush=True)
    print("- Read docs/research/game-development/README.md", flush=True)
    print("- Review studio/docs/active/game-brief.md", flush=True)
    print("- Review studio/docs/active/genre-starter.md", flush=True)
    print("- Review studio/docs/active/engine-profile.md", flush=True)
    print('- Run: python3 scripts/project_radar.py --warn-only', flush=True)
    print('- Run: python3 scripts/codex_studio.py next "describe your next task"', flush=True)
    print('- Run: python3 scripts/codex_studio.py checklist --task "describe your next task"', flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
