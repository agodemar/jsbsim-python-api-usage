#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="/usr/local/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
  PYTHON_BIN="$(command -v python3 || command -v python)"
fi

mkdir -p .codespaces

"$PYTHON_BIN" --version > .codespaces/python-version.txt
"$PYTHON_BIN" -m pip freeze > .codespaces/requirements-session-lock.txt
"$PYTHON_BIN" -m pip list --format=json > .codespaces/pip-list-session.json

if command -v code >/dev/null 2>&1; then
  {
    echo "# VS Code extensions (id@version)"
    code --list-extensions --show-versions | grep -E '^[A-Za-z0-9._-]+@[0-9]'
  } > .codespaces/vscode-extensions.txt
else
  echo "# VS Code CLI unavailable in this environment" > .codespaces/vscode-extensions.txt
fi

echo "Session snapshot updated in .codespaces/"
