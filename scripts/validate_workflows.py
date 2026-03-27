#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

from _studio_common import REPO_ROOT

WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"

REQUIRED_WORKFLOWS: dict[str, dict[str, Any]] = {
    "repo-validate.yml": {
        "jobs": {"repo-validate", "ci-artifacts"},
        "triggers": {"workflow_dispatch", "pull_request", "push"},
        "needs_upload_artifact": True,
    },
    "docker-smoke.yml": {
        "jobs": {"docker-smoke"},
        "triggers": {"workflow_dispatch", "pull_request", "push"},
        "needs_upload_artifact": True,
    },
    "starter-kit-contracts.yml": {
        "jobs": {"starter-kit-contracts"},
        "triggers": {"workflow_dispatch", "pull_request", "push"},
        "needs_upload_artifact": True,
    },
    "release-readiness.yml": {
        "jobs": {"release-readiness"},
        "triggers": {"workflow_dispatch"},
        "needs_upload_artifact": True,
    },
    "nightly-audit.yml": {
        "jobs": {"nightly-audit"},
        "triggers": {"workflow_dispatch", "schedule"},
        "needs_upload_artifact": True,
    },
}

PINNED_ACTIONS = {
    "actions/checkout",
    "actions/setup-python",
    "actions/upload-artifact",
}


def load_workflow(path: Path) -> dict[str, Any]:
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    return data if isinstance(data, dict) else {}


def normalized_triggers(workflow: dict[str, Any]) -> set[str]:
    value = workflow.get("on", {})
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return {str(item) for item in value}
    if isinstance(value, dict):
        return {str(key) for key in value.keys()}
    return set()


def job_steps(job: dict[str, Any]) -> list[dict[str, Any]]:
    steps = job.get("steps", [])
    return steps if isinstance(steps, list) else []


def is_sha_pinned(uses_value: str) -> bool:
    match = re.match(r"^[^@]+@([0-9a-f]{40})$", uses_value)
    return bool(match)


def collect_workflow_summary(path: Path) -> dict[str, Any]:
    workflow = load_workflow(path)
    jobs = workflow.get("jobs", {})
    job_names = sorted(jobs.keys()) if isinstance(jobs, dict) else []

    uses_values: list[str] = []
    upload_artifact_steps = 0
    matrix_keys: list[str] = []
    for job_name in job_names:
        job = jobs.get(job_name, {})
        if not isinstance(job, dict):
            continue
        strategy = job.get("strategy", {})
        if isinstance(strategy, dict):
            matrix = strategy.get("matrix", {})
            if isinstance(matrix, dict):
                matrix_keys.extend(str(key) for key in matrix.keys())
        for step in job_steps(job):
            if not isinstance(step, dict):
                continue
            uses_value = step.get("uses")
            if isinstance(uses_value, str):
                uses_values.append(uses_value)
                if uses_value.startswith("actions/upload-artifact@"):
                    upload_artifact_steps += 1

    return {
        "name": workflow.get("name", path.name),
        "path": str(path.relative_to(REPO_ROOT)),
        "jobs": job_names,
        "triggers": sorted(normalized_triggers(workflow)),
        "upload_artifact_steps": upload_artifact_steps,
        "matrix_keys": sorted(set(matrix_keys)),
        "uses": uses_values,
    }


def validate_workflows() -> tuple[list[str], dict[str, dict[str, Any]]]:
    failures: list[str] = []
    summaries: dict[str, dict[str, Any]] = {}

    for name, expectations in REQUIRED_WORKFLOWS.items():
        path = WORKFLOWS_DIR / name
        if not path.exists():
            failures.append(f"Missing required workflow: {path}")
            continue

        summary = collect_workflow_summary(path)
        summaries[name] = summary

        if not summary["jobs"]:
            failures.append(f"{name}: workflow has no jobs")
        missing_jobs = sorted(expectations["jobs"] - set(summary["jobs"]))
        if missing_jobs:
            failures.append(f"{name}: missing required jobs: {', '.join(missing_jobs)}")

        trigger_set = set(summary["triggers"])
        missing_triggers = sorted(expectations["triggers"] - trigger_set)
        if missing_triggers:
            failures.append(f"{name}: missing required triggers: {', '.join(missing_triggers)}")

        if expectations.get("needs_upload_artifact") and summary["upload_artifact_steps"] == 0:
            failures.append(f"{name}: workflow does not upload any artifact")

        if name == "repo-validate.yml":
            if "python-version" not in summary["matrix_keys"]:
                failures.append("repo-validate.yml: repo-validate job should use a python-version matrix")

        for uses_value in summary["uses"]:
            if uses_value.startswith("./"):
                continue
            if "@" not in uses_value:
                failures.append(f"{name}: step uses value is missing an explicit ref: {uses_value}")
                continue
            action_name = uses_value.split("@", 1)[0]
            if action_name in PINNED_ACTIONS and not is_sha_pinned(uses_value):
                failures.append(f"{name}: {action_name} should be pinned to a full commit SHA")

    return failures, summaries


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate GitHub workflow coverage, triggers, and artifact expectations.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    failures, summaries = validate_workflows()
    payload = {"failures": failures, "workflows": summaries}

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Workflow Validation")
        print("===================")
        for name, summary in summaries.items():
            print(f"- {name}: jobs={', '.join(summary['jobs'])} | triggers={', '.join(summary['triggers'])}")
        if failures:
            print()
            for failure in failures:
                print(f"ERROR: {failure}")
        else:
            print()
            print("All required workflows passed validation.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
