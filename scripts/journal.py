#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from _studio_common import REPO_ROOT, append_markdown_before_marker, copy_template_to_active
from studio_core import configured_project_name

JOURNAL_TEMPLATE = "prompt-journal.md"
JOURNAL_PATH = REPO_ROOT / "studio" / "docs" / "active" / JOURNAL_TEMPLATE
TRANSCRIPT_TEMPLATE = "agent-transcript.md"
TRANSCRIPT_PATH = REPO_ROOT / "studio" / "docs" / "active" / TRANSCRIPT_TEMPLATE
PACKET_TEMPLATE = "agent-execution.md"
PACKET_PATH = REPO_ROOT / "studio" / "docs" / "active" / PACKET_TEMPLATE


def now_label() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")


def ensure_journal_file() -> Path:
    return copy_template_to_active(JOURNAL_TEMPLATE, {"PROJECT_NAME": configured_project_name(REPO_ROOT.name)}, overwrite=False)


def ensure_journal_seed() -> str:
    journal_path = ensure_journal_file()
    return journal_path.read_text(encoding="utf-8")


def ensure_transcript_file() -> Path:
    return copy_template_to_active(TRANSCRIPT_TEMPLATE, {"PROJECT_NAME": configured_project_name(REPO_ROOT.name)}, overwrite=False)


def ensure_transcript_seed() -> str:
    transcript_path = ensure_transcript_file()
    return transcript_path.read_text(encoding="utf-8")


def ensure_packet_file() -> Path:
    return copy_template_to_active(PACKET_TEMPLATE, {"PROJECT_NAME": configured_project_name(REPO_ROOT.name)}, overwrite=False)


def ensure_packet_seed() -> str:
    packet_path = ensure_packet_file()
    return packet_path.read_text(encoding="utf-8")


def bullet_lines(label: str, values: list[str] | None) -> list[str]:
    clean = [value.strip() for value in values or [] if value and value.strip()]
    if not clean:
        return []
    return [f"- {label}: {', '.join(clean)}"]


def prompt_entry(prompt: str, route: str | None, summary: str | None, docs: list[str] | None, review: str | None, timestamp: str) -> str:
    lines = [
        f"### {timestamp} — User prompt",
        f"- Prompt: {prompt}",
    ]
    if route:
        lines.append(f"- Route: {route}")
    if summary:
        lines.append(f"- Summary: {summary}")
    lines.extend(bullet_lines("Docs", docs))
    if review:
        lines.append(f"- Review: {review}")
    return "\n".join(lines)


def agent_entry(step: str, expected: str, found: str, improved: str, evaluation: str, docs: list[str] | None, validation: list[str] | None, next_step: str | None, timestamp: str) -> str:
    lines = [
        f"### {timestamp} — Agent step",
        f"- Step: {step}",
        f"- Expected: {expected}",
        f"- Found: {found}",
        f"- Improved: {improved}",
        f"- Evaluation: {evaluation}",
    ]
    lines.extend(bullet_lines("Docs", docs))
    lines.extend(bullet_lines("Validation", validation))
    if next_step:
        lines.append(f"- Next step: {next_step}")
    return "\n".join(lines)


def transcript_entry(
    kind: str,
    task: str | None,
    speaker: str | None,
    target: str | None,
    message: str,
    result: str | None,
    next_step: str | None,
    docs: list[str] | None,
    validation: list[str] | None,
    timestamp: str,
) -> str:
    title = "Task assignment" if kind == "assignment" else "Agent conversation"
    lines = [
        f"### {timestamp} — {title}",
        f"- Kind: {kind}",
    ]
    if task:
        lines.append(f"- Task: {task}")
    if speaker:
        lines.append(f"- Speaker: {speaker}")
    if target:
        lines.append(f"- Target: {target}")
    lines.append(f"- Message: {message}")
    if result:
        lines.append(f"- Result: {result}")
    if next_step:
        lines.append(f"- Next step: {next_step}")
    lines.extend(bullet_lines("Docs", docs))
    lines.extend(bullet_lines("Validation", validation))
    return "\n".join(lines)


def packet_entry(
    task: str,
    owner: str,
    mode: str,
    goal: str,
    route: str | None,
    inputs: list[str] | None,
    outputs: list[str] | None,
    proof_path: str | None,
    custom_rules: list[str] | None,
    stop_conditions: list[str] | None,
    docs: list[str] | None,
    validation: list[str] | None,
    next_step: str | None,
    timestamp: str,
) -> str:
    lines = [
        f"### {timestamp} — Execution packet",
        f"- Task: {task}",
        f"- Owner: {owner}",
        f"- Mode: {mode}",
        f"- Goal: {goal}",
    ]
    if route:
        lines.append(f"- Route: {route}")
    lines.extend(bullet_lines("Inputs", inputs))
    lines.extend(bullet_lines("Outputs", outputs))
    if proof_path:
        lines.append(f"- Proof path: {proof_path}")
    lines.extend(bullet_lines("Custom rules", custom_rules))
    lines.extend(bullet_lines("Stop conditions", stop_conditions))
    lines.extend(bullet_lines("Docs", docs))
    lines.extend(bullet_lines("Validation", validation))
    if next_step:
        lines.append(f"- Next step: {next_step}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append prompt history and agent journal entries to the active journal.")
    subparsers = parser.add_subparsers(dest="kind", required=True)

    prompt_parser = subparsers.add_parser("prompt", help="Append a user prompt history entry.")
    prompt_parser.add_argument("--prompt", required=True)
    prompt_parser.add_argument("--route")
    prompt_parser.add_argument("--summary")
    prompt_parser.add_argument("--doc", action="append")
    prompt_parser.add_argument("--review")
    prompt_parser.add_argument("--dry-run", action="store_true")
    prompt_parser.add_argument("--json", action="store_true")

    agent_parser = subparsers.add_parser("agent", help="Append an agent step journal entry.")
    agent_parser.add_argument("--step", required=True)
    agent_parser.add_argument("--expected", required=True)
    agent_parser.add_argument("--found", required=True)
    agent_parser.add_argument("--improved", required=True)
    agent_parser.add_argument("--evaluation", required=True)
    agent_parser.add_argument("--next-step")
    agent_parser.add_argument("--doc", action="append")
    agent_parser.add_argument("--validation", action="append")
    agent_parser.add_argument("--dry-run", action="store_true")
    agent_parser.add_argument("--json", action="store_true")

    transcript_parser = subparsers.add_parser("transcript", help="Append a task assignment or conversation transcript entry.")
    transcript_parser.add_argument("--kind", dest="transcript_kind", required=True, choices=["assignment", "conversation"])
    transcript_parser.add_argument("--task")
    transcript_parser.add_argument("--speaker")
    transcript_parser.add_argument("--target")
    transcript_parser.add_argument("--message", required=True)
    transcript_parser.add_argument("--result")
    transcript_parser.add_argument("--next-step")
    transcript_parser.add_argument("--doc", action="append")
    transcript_parser.add_argument("--validation", action="append")
    transcript_parser.add_argument("--dry-run", action="store_true")
    transcript_parser.add_argument("--json", action="store_true")

    packet_parser = subparsers.add_parser("packet", help="Append an execution packet entry to the active work log.")
    packet_parser.add_argument("--task", required=True)
    packet_parser.add_argument("--owner", default="Kaynexis")
    packet_parser.add_argument("--mode", default="single-specialist")
    packet_parser.add_argument("--goal", required=True)
    packet_parser.add_argument("--route")
    packet_parser.add_argument("--input", action="append")
    packet_parser.add_argument("--output", action="append")
    packet_parser.add_argument("--proof-path")
    packet_parser.add_argument("--rule", action="append")
    packet_parser.add_argument("--stop-condition", action="append")
    packet_parser.add_argument("--doc", action="append")
    packet_parser.add_argument("--validation", action="append")
    packet_parser.add_argument("--next-step")
    packet_parser.add_argument("--dry-run", action="store_true")
    packet_parser.add_argument("--json", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    timestamp = now_label()
    path = JOURNAL_PATH

    if args.kind == "prompt":
        entry = prompt_entry(args.prompt, args.route, args.summary, args.doc, args.review, timestamp)
        payload = {"kind": "prompt", "path": str(path.relative_to(REPO_ROOT)), "timestamp": timestamp, "entry": entry}
        if args.dry_run:
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                print(entry)
            return 0
        seed_text = ensure_journal_seed()
        append_markdown_before_marker(path, "prompt-history-append", entry, seed_text=seed_text)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"Appended prompt history entry to {payload['path']}")
        return 0

    if args.kind == "transcript":
        if args.transcript_kind == "assignment" and not args.task:
            raise SystemExit("--task is required for assignment transcript entries")
        entry = transcript_entry(
            args.transcript_kind,
            args.task,
            args.speaker,
            args.target,
            args.message,
            args.result,
            args.next_step,
            args.doc,
            args.validation,
            timestamp,
        )
        payload = {"kind": "transcript", "path": str(TRANSCRIPT_PATH.relative_to(REPO_ROOT)), "timestamp": timestamp, "entry": entry}
        if args.dry_run:
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                print(entry)
            return 0
        seed_text = ensure_transcript_seed()
        marker = "task-assignment-history-append" if args.transcript_kind == "assignment" else "agent-conversation-transcript-append"
        append_markdown_before_marker(TRANSCRIPT_PATH, marker, entry, seed_text=seed_text)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"Appended transcript entry to {payload['path']}")
        return 0

    if args.kind == "packet":
        entry = packet_entry(
            args.task,
            args.owner,
            args.mode,
            args.goal,
            args.route,
            args.input,
            args.output,
            args.proof_path,
            args.rule,
            args.stop_condition,
            args.doc,
            args.validation,
            args.next_step,
            timestamp,
        )
        payload = {"kind": "packet", "path": str(PACKET_PATH.relative_to(REPO_ROOT)), "timestamp": timestamp, "entry": entry}
        if args.dry_run:
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                print(entry)
            return 0
        seed_text = ensure_packet_seed()
        append_markdown_before_marker(PACKET_PATH, "agent-execution-append", entry, seed_text=seed_text)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"Appended execution packet entry to {payload['path']}")
        return 0

    entry = agent_entry(args.step, args.expected, args.found, args.improved, args.evaluation, args.doc, args.validation, args.next_step, timestamp)
    payload = {"kind": "agent", "path": str(path.relative_to(REPO_ROOT)), "timestamp": timestamp, "entry": entry}
    if args.dry_run:
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(entry)
        return 0
    seed_text = ensure_journal_seed()
    append_markdown_before_marker(path, "agent-journal-append", entry, seed_text=seed_text)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Appended agent journal entry to {payload['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
