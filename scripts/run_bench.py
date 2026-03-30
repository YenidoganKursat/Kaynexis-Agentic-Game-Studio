#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from _studio_common import REPO_ROOT, write_text

BENCHMARK_DIR = REPO_ROOT / "evals" / "benchmark"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "build" / "bench" / "latest"

BENCHMARK_FAMILIES = [
    {
        "name": "SWE-bench",
        "best_for": "Code-edit regression on real repositories",
        "source": "https://www.swebench.com/",
    },
    {
        "name": "AgentBench",
        "best_for": "Broad agent behavior across tools and environments",
        "source": "https://github.com/THUDM/AgentBench",
    },
    {
        "name": "GAIA",
        "best_for": "General reasoning and task completion",
        "source": "https://huggingface.co/gaia-benchmark",
    },
    {
        "name": "OSWorld",
        "best_for": "Desktop and operating-system tasks",
        "source": "https://github.com/xlang-ai/OSWorld",
    },
    {
        "name": "WebArena",
        "best_for": "Browser and website tasks",
        "source": "https://github.com/web-arena-x/webarena",
    },
    {
        "name": "OpenAI Evals",
        "best_for": "Custom harnesses and reusable evals",
        "source": "https://platform.openai.com/docs/guides/evals",
    },
    {
        "name": "Repo-local",
        "best_for": "Route, checklist, docs, and validation regression in this repo",
        "source": "docs/reference/benchmark-guide.md",
    },
]


def load_cases() -> list[dict[str, object]]:
    path = BENCHMARK_DIR / "cases.json"
    return json.loads(path.read_text(encoding="utf-8"))


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)


def normalize_set(items: object) -> set[str]:
    if not isinstance(items, list):
        return set()
    return {str(item) for item in items}


def score_case(case: dict[str, object], route_payload: dict[str, object], checklist_payload: dict[str, object]) -> dict[str, object]:
    expected_route = str(case.get("expected_route", "")).strip()
    expected_docs = [str(item) for item in case.get("expected_docs", [])]
    expected_refs = [str(item) for item in case.get("expected_research_refs", [])]
    expected_disciplines = [str(item) for item in case.get("expected_disciplines", [])]
    expected_checklist_ids = [str(item) for item in case.get("expected_checklist_ids", [])]

    route_ok = route_payload.get("route") == expected_route
    route_docs = normalize_set(route_payload.get("docs"))
    route_refs = normalize_set(route_payload.get("research_refs"))
    route_checklists = {str(item.get("id", "")) for item in route_payload.get("checklists", []) if isinstance(item, dict)}
    checklist_disciplines = normalize_set(checklist_payload.get("disciplines"))
    checklist_items = {str(item.get("id", "")) for item in checklist_payload.get("items", []) if isinstance(item, dict)}
    checklist_refs = normalize_set(checklist_payload.get("research_refs"))

    failures: list[str] = []
    if not route_ok:
        failures.append(f"route mismatch: expected {expected_route}, got {route_payload.get('route')}")

    for label, expected_values, actual_values in [
        ("route docs", expected_docs, route_docs),
        ("route research refs", expected_refs, route_refs),
        ("route checklist items", expected_checklist_ids, route_checklists),
        ("checklist disciplines", expected_disciplines, checklist_disciplines),
        ("checklist items", expected_checklist_ids, checklist_items),
        ("checklist research refs", expected_refs, checklist_refs),
    ]:
        missing = [item for item in expected_values if item not in actual_values]
        if missing:
            failures.append(f"missing {label}: {', '.join(missing)}")

    total_checks = 1 + len(expected_docs) + len(expected_refs) + len(expected_checklist_ids) + len(expected_disciplines) + len(expected_checklist_ids) + len(expected_refs)
    passed_checks = (1 if route_ok else 0)
    passed_checks += len([item for item in expected_docs if item in route_docs])
    passed_checks += len([item for item in expected_refs if item in route_refs])
    passed_checks += len([item for item in expected_checklist_ids if item in route_checklists])
    passed_checks += len([item for item in expected_disciplines if item in checklist_disciplines])
    passed_checks += len([item for item in expected_checklist_ids if item in checklist_items])
    passed_checks += len([item for item in expected_refs if item in checklist_refs])
    score = int(round((passed_checks / total_checks) * 100)) if total_checks else 100

    return {
        "task": case.get("task", ""),
        "route": route_payload.get("route"),
        "expected_route": expected_route,
        "route_ok": route_ok,
        "docs_ok": not any(label == "route docs" for label in failures),
        "research_refs_ok": not any(label == "route research refs" for label in failures),
        "checklist_ok": not any(label in {"route checklist items", "checklist disciplines", "checklist items", "checklist research refs"} for label in failures),
        "score": score,
        "failures": failures,
        "route_docs": sorted(route_docs),
        "route_research_refs": sorted(route_refs),
        "route_checklist_ids": sorted(route_checklists),
        "checklist_disciplines": sorted(checklist_disciplines),
        "checklist_items": sorted(checklist_items),
        "checklist_research_refs": sorted(checklist_refs),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Benchmark Report",
        "",
        f"- Generated: {report['generated_at_utc']}",
        f"- Label: {report['label']}",
        f"- Score: {report['summary']['score']} / 100",
        f"- Readiness: {report['summary']['readiness']}",
        "",
        "## Benchmark families",
    ]
    for family in report["families"]:
        lines.append(f"- {family['name']}: {family['best_for']} ({family['source']})")
    lines += [
        "",
        "## Cases",
    ]
    for case in report["cases"]:
        lines.append(f"- {case['task']}")
        lines.append(f"  - route: {case['route']} | score: {case['score']} / 100")
        if case["failures"]:
            for failure in case["failures"]:
                lines.append(f"  - failure: {failure}")
        else:
            lines.append("  - pass")
    lines += [
        "",
        "## Artifacts",
        f"- JSON: {report['artifacts']['json']}",
        f"- Markdown: {report['artifacts']['markdown']}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the repo-local benchmark corpus and summarize ready-made benchmark families.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--label", help="Optional label for the benchmark report.")
    parser.add_argument("--json", action="store_true", help="Print the report JSON to stdout.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    cases = load_cases()
    report_cases = []
    total_failures = 0
    total_score = 0

    route_script = REPO_ROOT / "scripts" / "route_task.py"
    checklist_script = REPO_ROOT / "scripts" / "codex_studio.py"

    for case in cases:
        task = str(case["task"])

        route_result = run_command([sys.executable, str(route_script), task, "--json"])
        if route_result.returncode != 0:
            failure = route_result.stderr.strip() or route_result.stdout.strip() or "route_task failed"
            report_cases.append(
                {
                    "task": task,
                    "route": None,
                    "expected_route": case.get("expected_route", ""),
                    "route_ok": False,
                    "docs_ok": False,
                    "research_refs_ok": False,
                    "checklist_ok": False,
                    "score": 0,
                    "failures": [failure],
                    "route_docs": [],
                    "route_research_refs": [],
                    "route_checklist_ids": [],
                    "checklist_disciplines": [],
                    "checklist_items": [],
                    "checklist_research_refs": [],
                }
            )
            total_failures += 1
            continue
        route_payload = json.loads(route_result.stdout)

        checklist_result = run_command([sys.executable, str(checklist_script), "checklist", "--task", task, "--json"])
        if checklist_result.returncode != 0:
            failure = checklist_result.stderr.strip() or checklist_result.stdout.strip() or "codex_studio checklist failed"
            report_cases.append(
                {
                    "task": task,
                    "route": route_payload.get("route"),
                    "expected_route": case.get("expected_route", ""),
                    "route_ok": False,
                    "docs_ok": False,
                    "research_refs_ok": False,
                    "checklist_ok": False,
                    "score": 0,
                    "failures": [failure],
                    "route_docs": route_payload.get("docs", []),
                    "route_research_refs": route_payload.get("research_refs", []),
                    "route_checklist_ids": [item.get("id", "") for item in route_payload.get("checklists", []) if isinstance(item, dict)],
                    "checklist_disciplines": [],
                    "checklist_items": [],
                    "checklist_research_refs": [],
                }
            )
            total_failures += 1
            continue
        checklist_payload = json.loads(checklist_result.stdout)

        case_report = score_case(case, route_payload, checklist_payload)
        report_cases.append(case_report)
        total_failures += len(case_report["failures"])
        total_score += case_report["score"]

    case_count = len(report_cases)
    score = int(round(total_score / case_count)) if case_count else 0
    readiness = "benchmark-ready" if total_failures == 0 and score >= 90 else "needs-attention"
    report = {
        "generated_at_utc": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "label": args.label or "benchmark-report",
        "families": BENCHMARK_FAMILIES,
        "cases": report_cases,
        "summary": {
            "case_count": case_count,
            "failure_count": total_failures,
            "score": score,
            "readiness": readiness,
        },
        "artifacts": {
            "json": str(output_dir / "bench-report.json"),
            "markdown": str(output_dir / "bench-report.md"),
        },
    }

    write_text(Path(report["artifacts"]["json"]), json.dumps(report, indent=2))
    write_text(Path(report["artifacts"]["markdown"]), render_markdown(report))

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Benchmark score: {report['summary']['score']} / 100")
        print(f"Readiness: {report['summary']['readiness']}")
        print(f"Wrote {report['artifacts']['json']}")
        print(f"Wrote {report['artifacts']['markdown']}")
    return 1 if total_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
