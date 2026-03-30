#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from _studio_common import REPO_ROOT

ZERO_SHA = "0" * 40


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=check,
    )


def commit_exists(sha: str) -> bool:
    if not sha or sha == ZERO_SHA:
        return False
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def fetch_commit(sha: str) -> bool:
    if not sha or sha == ZERO_SHA:
        return False
    result = subprocess.run(
        ["git", "fetch", "--no-tags", "origin", sha, "--depth=1"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0 and commit_exists(sha)


def resolve_base_sha(requested_base_sha: str) -> tuple[str, str, bool]:
    requested = requested_base_sha.strip()
    if not requested or requested == ZERO_SHA:
        root_commit = git("rev-list", "--max-parents=0", "HEAD").stdout.splitlines()[-1]
        return root_commit, "root commit fallback", False

    if commit_exists(requested):
        return requested, "", False

    fetched = fetch_commit(requested)
    if fetched:
        return requested, "fetched missing base commit", True

    parent = git("rev-parse", "HEAD^", check=False)
    if parent.returncode == 0:
        return parent.stdout.strip(), "falling back to HEAD^ because base sha was unavailable", False

    root_commit = git("rev-list", "--max-parents=0", "HEAD").stdout.splitlines()[-1]
    return root_commit, "falling back to root commit because base sha was unavailable", False


def resolve_changed_paths(base_sha: str, head_sha: str) -> tuple[str, list[str], str, bool]:
    resolved_base_sha, fallback_reason, fetched = resolve_base_sha(base_sha)
    diff = git("diff", "--name-only", resolved_base_sha, head_sha, check=True)
    changed_paths = [line.strip() for line in diff.stdout.splitlines() if line.strip()]
    return resolved_base_sha, changed_paths, fallback_reason, fetched


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve changed paths between two commits, even when the original base SHA is no longer fetched locally.")
    parser.add_argument("--base-sha", required=True, help="Base commit SHA to diff against.")
    parser.add_argument("--head-sha", default="HEAD", help="Head commit SHA or ref to diff against.")
    parser.add_argument("--paths-file", type=Path, help="Optional output file for newline-separated changed paths.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    resolved_base_sha, changed_paths, fallback_reason, fetched = resolve_changed_paths(args.base_sha, args.head_sha)
    payload = {
        "requested_base_sha": args.base_sha,
        "resolved_base_sha": resolved_base_sha,
        "head_sha": args.head_sha,
        "fetched_missing_base_sha": fetched,
        "fallback_reason": fallback_reason,
        "paths": changed_paths,
    }

    if args.paths_file is not None:
        args.paths_file.parent.mkdir(parents=True, exist_ok=True)
        args.paths_file.write_text("\n".join(changed_paths) + ("\n" if changed_paths else ""), encoding="utf-8")

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        if fallback_reason:
            print(f"Resolved base SHA with fallback: {fallback_reason}")
        if args.paths_file is not None:
            print(f"Wrote {len(changed_paths)} changed paths to {args.paths_file}")
        elif changed_paths:
            for path in changed_paths:
                print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
