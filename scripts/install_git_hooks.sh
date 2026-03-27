#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
if [ ! -d "$ROOT_DIR/.git" ]; then
  echo "No .git directory found at $ROOT_DIR"
  echo "Initialize git first, then rerun this script."
  exit 1
fi

mkdir -p "$ROOT_DIR/.git/hooks"
for hook in pre-commit pre-push commit-msg; do
  cp "$ROOT_DIR/.githooks/$hook" "$ROOT_DIR/.git/hooks/$hook"
  chmod +x "$ROOT_DIR/.git/hooks/$hook"
done

echo "Installed hooks into $ROOT_DIR/.git/hooks"
