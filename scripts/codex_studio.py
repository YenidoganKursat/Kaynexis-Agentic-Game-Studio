#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys

from _studio_common import REPO_ROOT, available_presets, build_genre_replacements, default_engine_version, parse_preset_metadata, preset_path
from studio_core import (
    available_starter_kits,
    configured_project_name,
    infer_engine_from_text,
    primary_engine_slug,
    related_research_refs,
    render_checklist_markdown,
    resolve_checklists,
    scaffold_research_note,
    starter_kit_summary,
)


def _run(command: list[str]) -> int:
    return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode


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
    print(group_label)
    print("-" * len(group_label))
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option['label']} ({option['slug']})")
        if option["summary"]:
            print(f"   {option['summary']}")
    print()


def choose_option(group_label: str, options: list[dict[str, str]], current: str | None = None) -> str:
    if current:
        return current
    print_options(group_label, options)
    valid = {option["slug"] for option in options}
    while True:
        raw = input(f"Choose {group_label} [1-{len(options)} or slug]: ").strip()
        if raw.isdigit():
            index = int(raw)
            if 1 <= index <= len(options):
                return options[index - 1]["slug"]
        elif raw in valid:
            return raw
        print("Invalid selection. Use a listed number or slug.")


def prompt_text(label: str, current: str | None, default: str) -> str:
    if current:
        return current
    raw = input(f"{label} [{default}]: ").strip()
    return raw or default


def build_init_command(args: argparse.Namespace) -> list[str]:
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
        if getattr(args, flag, False):
            command.append(f"--{flag.replace('_', '-')}")
    return command


def handle_init(args: argparse.Namespace) -> int:
    engines = preset_options("engine")
    platforms = preset_options("platform")
    genres = preset_options("genre")

    if args.list:
        print_options("Engine options", engines)
        print_options("Platform options", platforms)
        print_options("Genre options", genres)
        print("Starter kits")
        print("------------")
        for slug in available_starter_kits():
            summary = starter_kit_summary(slug)
            print(f"- {slug}: {summary['version_family']} | platforms: {', '.join(summary['supported_platforms'])}")
        return 0

    interactive = sys.stdin.isatty()
    if interactive:
        print("Codex Studio")
        print("============")
        args.project_name = prompt_text("Project name", args.project_name, configured_project_name(REPO_ROOT.name))
        args.engine = choose_option("engine", engines, args.engine)
        args.platform = choose_option("platform", platforms, args.platform)
        args.genre = choose_option("genre", genres, args.genre)
    else:
        missing = [name for name in ("project_name", "engine", "platform", "genre") if not getattr(args, name)]
        if missing:
            raise SystemExit(f"Non-interactive init requires: {', '.join('--' + item.replace('_', '-') for item in missing)}")

    args.engine_version = args.engine_version or default_engine_version(args.engine)
    guidance = build_genre_replacements(args.genre)
    if not (args.dry_run and args.json):
        print()
        print("Selected setup")
        print("--------------")
        print(f"Project: {args.project_name}")
        print(f"Engine: {args.engine}")
        print(f"Engine version: {args.engine_version}")
        print(f"Platform: {args.platform}")
        print(f"Genre: {guidance['GENRE_NAME']}")
        print(f"Summary: {guidance['GENRE_SUMMARY']}")
        print("First slice suggestion:")
        for line in guidance["GENRE_FIRST_SLICE"].splitlines():
            print(line)
        print()

    if interactive and not args.yes:
        confirm = input("Continue with setup? [Y/n]: ").strip().lower()
        if confirm not in ("", "y", "yes"):
            print("Setup cancelled.")
            return 1

    command = build_init_command(args)
    if args.dry_run:
        payload = {"command": command}
        print(json.dumps(payload, indent=2))
        return 0
    return _run(command)


def handle_next(args: argparse.Namespace) -> int:
    command = [sys.executable, str(REPO_ROOT / "scripts" / "route_task.py"), args.task]
    if args.engine:
        command.extend(["--engine", args.engine])
    if args.json:
        command.append("--json")
    return _run(command)


def handle_doctor(args: argparse.Namespace) -> int:
    command = [sys.executable, str(REPO_ROOT / "scripts" / "doctor.py")]
    if args.json:
        command.append("--json")
    return _run(command)


def handle_engine(args: argparse.Namespace) -> int:
    if args.list or not args.engine:
        payload = [starter_kit_summary(slug) for slug in available_starter_kits()]
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print("Starter kits")
            print("------------")
            for item in payload:
                print(f"- {item['id']} ({item['version_family']})")
                print(f"  smoke: {', '.join(item['smoke_commands'])}")
                print(f"  export: {', '.join(item['export_commands'])}")
        return 0

    payload = starter_kit_summary(args.engine)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"{payload['id']} starter kit")
        print("-----------------------")
        print(f"Engine: {payload['engine']}")
        print(f"Version family: {payload['version_family']}")
        print(f"Platforms: {', '.join(payload['supported_platforms'])}")
        print(f"Scaffold: {payload['scaffold_dir']}")
        print(f"Bootstrap: {payload['bootstrap_command']}")
        print("Smoke commands:")
        for command in payload["smoke_commands"]:
            print(f"- {command}")
        print("Export commands:")
        for command in payload["export_commands"]:
            print(f"- {command}")
    return 0


def handle_checklist(args: argparse.Namespace) -> int:
    disciplines = list(args.discipline or [])
    if args.task and not disciplines:
        from studio_core import infer_disciplines_from_task

        disciplines = infer_disciplines_from_task(args.task)
    resolved_engine = args.engine or (infer_engine_from_text(args.task) if args.task else None) or primary_engine_slug()

    items = resolve_checklists(
        engine_slug=resolved_engine,
        disciplines=disciplines,
        milestone=args.milestone,
        agent_name=args.agent,
    )
    payload = {
        "engine": resolved_engine,
        "disciplines": disciplines,
        "milestone": args.milestone,
        "agent": args.agent,
        "items": items,
        "research_refs": related_research_refs(disciplines, engine_slug=resolved_engine),
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        title = "Merged Checklist"
        print(render_checklist_markdown(items, title))
        if payload["research_refs"]:
            print()
            print("## Related research")
            for path in payload["research_refs"]:
                print(f"- {path}")
    return 0


def handle_research(args: argparse.Namespace) -> int:
    if args.dry_run:
        payload = {
            "path": f"docs/research/game-development/{args.category}/{args.slug or args.title.lower().replace(' ', '-')}.md",
            "category": args.category,
            "title": args.title,
        }
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"Would create research note: {payload['path']}")
        return 0
    path = scaffold_research_note(args.category, args.title, sources=args.source, slug=args.slug)
    payload = {"path": str(path.relative_to(REPO_ROOT))}
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Created research note: {payload['path']}")
    return 0


def interactive_menu() -> argparse.Namespace:
    print("Codex Studio")
    print("============")
    print("1. Init a project baseline")
    print("2. Route the next task")
    print("3. Render a checklist")
    print("4. Scaffold a research note")
    print("5. Run doctor")
    print("6. List engine starter kits")
    raw = input("Choose an action [1-6]: ").strip()
    parser = build_parser()
    if raw == "1":
        return parser.parse_args(["init"])
    if raw == "2":
        task = input("Describe the task: ").strip() or "Describe the next gameplay slice"
        return parser.parse_args(["next", task])
    if raw == "3":
        task = input("Task for checklist context: ").strip() or "Prototype the next combat mechanic"
        return parser.parse_args(["checklist", "--task", task])
    if raw == "4":
        title = input("Research title: ").strip() or "New research note"
        return parser.parse_args(["research", "--category", "systems", "--title", title])
    if raw == "5":
        return parser.parse_args(["doctor"])
    return parser.parse_args(["engine", "--list"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Front-door CLI for the Codex-first multi-engine studio repo.")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Guided repo setup and baseline seeding.")
    init_parser.add_argument("--project-name")
    init_parser.add_argument("--engine")
    init_parser.add_argument("--engine-version")
    init_parser.add_argument("--platform")
    init_parser.add_argument("--genre")
    init_parser.add_argument("--overwrite", action="store_true")
    init_parser.add_argument("--all-templates", action="store_true")
    init_parser.add_argument("--init-git", action="store_true")
    init_parser.add_argument("--skip-hooks", action="store_true")
    init_parser.add_argument("--skip-validate", action="store_true")
    init_parser.add_argument("--skip-doctor", action="store_true")
    init_parser.add_argument("--list", action="store_true")
    init_parser.add_argument("--yes", action="store_true")
    init_parser.add_argument("--dry-run", action="store_true")
    init_parser.add_argument("--json", action="store_true")

    next_parser = subparsers.add_parser("next", help="Route a task to likely skills, agents, docs, and checklists.")
    next_parser.add_argument("task")
    next_parser.add_argument("--engine")
    next_parser.add_argument("--json", action="store_true")

    checklist_parser = subparsers.add_parser("checklist", help="Resolve the layered checklist bundle for a task, engine, milestone, or agent.")
    checklist_parser.add_argument("--task")
    checklist_parser.add_argument("--engine")
    checklist_parser.add_argument("--discipline", action="append")
    checklist_parser.add_argument("--milestone")
    checklist_parser.add_argument("--agent")
    checklist_parser.add_argument("--json", action="store_true")

    research_parser = subparsers.add_parser("research", help="Scaffold a date-stamped research note in the game-development knowledge base.")
    research_parser.add_argument("--category", default="systems")
    research_parser.add_argument("--title", required=True)
    research_parser.add_argument("--slug")
    research_parser.add_argument("--source", action="append")
    research_parser.add_argument("--json", action="store_true")
    research_parser.add_argument("--dry-run", action="store_true")

    doctor_parser = subparsers.add_parser("doctor", help="Run repo health checks.")
    doctor_parser.add_argument("--json", action="store_true")

    engine_parser = subparsers.add_parser("engine", help="Inspect starter-kit parity for supported engines.")
    engine_parser.add_argument("--engine")
    engine_parser.add_argument("--list", action="store_true")
    engine_parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None and sys.stdin.isatty():
        args = interactive_menu()
    elif args.command is None:
        parser.print_help()
        return 1

    if args.command == "init":
        return handle_init(args)
    if args.command == "next":
        return handle_next(args)
    if args.command == "checklist":
        return handle_checklist(args)
    if args.command == "research":
        return handle_research(args)
    if args.command == "doctor":
        return handle_doctor(args)
    if args.command == "engine":
        return handle_engine(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
