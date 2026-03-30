#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _studio_common import REPO_ROOT, read_project_version, write_text

VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?$")
CHANGELOG_RELEASE_RE = re.compile(r"^##\s+v(\d+\.\d+\.\d+)(?:\s+[—-].*)?$", re.MULTILINE)


def load_changelog() -> str:
    path = REPO_ROOT / "CHANGELOG.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def analyze_version(version: str | None, changelog_text: str) -> dict[str, object]:
    failures: list[str] = []
    warnings: list[str] = []

    if not version:
        failures.append("VERSION file is missing or empty.")
        return {
            "version": "",
            "major": None,
            "minor": None,
            "patch": None,
            "prerelease": "",
            "tag": "",
            "is_prerelease": False,
            "status": "invalid",
            "failures": failures,
            "warnings": warnings,
        }

    match = VERSION_RE.match(version)
    if not match:
        failures.append(f"VERSION value '{version}' is not semantic-version shaped.")
        return {
            "version": version,
            "major": None,
            "minor": None,
            "patch": None,
            "prerelease": "",
            "tag": "",
            "is_prerelease": False,
            "status": "invalid",
            "failures": failures,
            "warnings": warnings,
        }

    major, minor, patch = match.group(1), match.group(2), match.group(3)
    prerelease = match.group(4) or ""
    tag = f"v{major}.{minor}.{patch}"
    is_prerelease = bool(prerelease)
    has_unreleased = "## Unreleased" in changelog_text
    has_release_heading = bool(CHANGELOG_RELEASE_RE.search(changelog_text))
    matching_release_heading = bool(re.search(rf"^##\s+{re.escape(tag)}(?:\s+[—-].*)?$", changelog_text, re.MULTILINE))

    if is_prerelease and not has_unreleased:
        failures.append("Prerelease VERSION requires an Unreleased section in CHANGELOG.md.")
    if not is_prerelease and not matching_release_heading:
        failures.append(f"Release VERSION '{version}' requires a matching CHANGELOG heading '{tag}'.")
    if not has_release_heading and not is_prerelease:
        warnings.append("CHANGELOG.md has no release headings yet.")

    status = "version-ready"
    if not failures and not is_prerelease:
        status = "release-ready"

    return {
        "version": version,
        "major": int(major),
        "minor": int(minor),
        "patch": int(patch),
        "prerelease": prerelease,
        "tag": tag,
        "is_prerelease": is_prerelease,
        "status": status,
        "changelog": {
            "has_unreleased": has_unreleased,
            "has_release_heading": has_release_heading,
            "has_matching_release_heading": matching_release_heading,
        },
        "failures": failures,
        "warnings": warnings,
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Version Guard Report",
        "",
        f"- Version: {report['version'] or 'missing'}",
        f"- Tag: {report.get('tag') or 'missing'}",
        f"- Status: {report['status']}",
        f"- Prerelease: {report['is_prerelease']}",
        f"- Changelog has Unreleased: {report['changelog']['has_unreleased']}",
        f"- Changelog has matching release heading: {report['changelog']['has_matching_release_heading']}",
        "",
        "## Failures",
    ]
    failures = report.get("failures", [])
    if failures:
        lines += [f"- {item}" for item in failures]
    else:
        lines.append("- None")
    lines += ["", "## Warnings"]
    warnings = report.get("warnings", [])
    if warnings:
        lines += [f"- {item}" for item in warnings]
    else:
        lines.append("- None")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repo versioning metadata and changelog sync.")
    parser.add_argument("--output-dir", default=str(REPO_ROOT / "build" / "ci" / "version"))
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable summary.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    version = read_project_version()
    changelog_text = load_changelog()
    report = analyze_version(version, changelog_text)
    report["source"] = {
        "version_file": str(REPO_ROOT / "VERSION"),
        "changelog": str(REPO_ROOT / "CHANGELOG.md"),
    }
    report["artifacts"] = {
        "json": str(output_dir / "version-report.json"),
        "markdown": str(output_dir / "version-report.md"),
    }

    write_text(Path(report["artifacts"]["json"]), json.dumps(report, indent=2))
    write_text(Path(report["artifacts"]["markdown"]), render_markdown(report))

    payload = {
        "json": report["artifacts"]["json"],
        "markdown": report["artifacts"]["markdown"],
        "status": report["status"],
        "version": report["version"],
        "tag": report["tag"],
        "is_prerelease": report["is_prerelease"],
        "failures": report["failures"],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Wrote {report['artifacts']['json']}")
        print(f"Wrote {report['artifacts']['markdown']}")
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
