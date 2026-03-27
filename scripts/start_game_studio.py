#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys

from _studio_common import REPO_ROOT, available_presets, build_genre_replacements, parse_preset_metadata, preset_path

DEFAULT_PROJECT_NAME = REPO_ROOT.name


def preset_options(group: str) -> list[dict[str, str]]:
    options: list[dict[str, str]] = []
    for slug in available_presets(group):
        metadata = parse_preset_metadata(preset_path(group, slug))
        options.append(
            {
                "slug": slug,
                "label": str(metadata.get("display_name") or slug),
                "summary": str(metadata.get("summary") or ""),
            }
        )
    return options


def print_options(group_label: str, options: list[dict[str, str]]) -> None:
    print(group_label, flush=True)
    print("-" * len(group_label), flush=True)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option['label']} ({option['slug']})", flush=True)
        if option["summary"]:
            print(f"   {option['summary']}", flush=True)
    print(flush=True)


def choose_option(group_label: str, options: list[dict[str, str]], current: str | None = None) -> str:
    if current:
        return current

    print_options(group_label, options)
    slug_map = {option["slug"]: option["slug"] for option in options}

    while True:
        raw = input(f"{group_label} secimi [1-{len(options)} veya slug]: ").strip()
        if raw.isdigit():
            index = int(raw)
            if 1 <= index <= len(options):
                return options[index - 1]["slug"]
        elif raw in slug_map:
            return slug_map[raw]
        print("Gecersiz secim. Lutfen listedeki numaralardan birini veya slug degerini gir.", flush=True)


def prompt_text(label: str, current: str | None, default: str) -> str:
    if current:
        return current
    raw = input(f"{label} [{default}]: ").strip()
    return raw or default


def build_setup_command(args: argparse.Namespace) -> list[str]:
    command = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "setup_repo.py"),
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
    for flag in ("overwrite", "all_templates", "init_git", "skip_hooks", "skip_validate", "skip_doctor"):
        if getattr(args, flag):
            command.append(f"--{flag.replace('_', '-')}")
    return command


def main() -> int:
    parser = argparse.ArgumentParser(description="Guided interactive setup for a genre-aligned game repo.")
    parser.add_argument("--project-name")
    parser.add_argument("--engine")
    parser.add_argument("--engine-version", default="TBD")
    parser.add_argument("--platform")
    parser.add_argument("--genre")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--all-templates", action="store_true")
    parser.add_argument("--init-git", action="store_true")
    parser.add_argument("--skip-hooks", action="store_true")
    parser.add_argument("--skip-validate", action="store_true")
    parser.add_argument("--skip-doctor", action="store_true")
    parser.add_argument("--list", action="store_true", help="List available engine, platform, and genre options.")
    parser.add_argument("--yes", action="store_true", help="Skip the final confirmation prompt.")
    args = parser.parse_args()

    engines = preset_options("engine")
    platforms = preset_options("platform")
    genres = preset_options("genre")

    if args.list:
        print_options("Engine secenekleri", engines)
        print_options("Platform secenekleri", platforms)
        print_options("Genre secenekleri", genres)
        return 0

    interactive = sys.stdin.isatty()
    if not interactive and not all([args.project_name, args.engine, args.platform, args.genre]):
        parser.error("Non-interactive usage requires --project-name, --engine, --platform, and --genre. Use --list to inspect choices.")

    print("Codex Game Studio Baslangic", flush=True)
    print("===========================", flush=True)

    if interactive:
        args.project_name = prompt_text("Proje adi", args.project_name, DEFAULT_PROJECT_NAME)
        args.engine = choose_option("Engine", engines, args.engine)
        args.platform = choose_option("Platform", platforms, args.platform)
        args.genre = choose_option("Genre", genres, args.genre)

    guidance = build_genre_replacements(args.genre)
    print(flush=True)
    print("Secilen kurulum", flush=True)
    print("----------------", flush=True)
    print(f"Proje: {args.project_name}", flush=True)
    print(f"Engine: {args.engine}", flush=True)
    print(f"Platform: {args.platform}", flush=True)
    print(f"Genre: {guidance['GENRE_NAME']}", flush=True)
    print(f"Ozet: {guidance['GENRE_SUMMARY']}", flush=True)
    print("Ilk slice onerisi:", flush=True)
    for line in guidance["GENRE_FIRST_SLICE"].splitlines():
        print(line, flush=True)
    print(flush=True)

    if interactive and not args.yes:
        confirm = input("Kuruluma devam edilsin mi? [Y/n]: ").strip().lower()
        if confirm not in ("", "y", "yes"):
            print("Kurulum iptal edildi.", flush=True)
            return 1

    command = build_setup_command(args)
    sys.stdout.flush()
    return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
