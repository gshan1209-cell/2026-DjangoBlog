#!/bin/bash
# Development-only bootstrap. Never delete an existing environment automatically.
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$PROJECT_DIR"

# A successful pip call with an empty list is not a usable project setup.
if [[ ! -f requirements.txt ]] || ! grep -qE '^[[:space:]]*[^#[:space:]]' requirements.txt; then
    printf '[ERROR] requirements.txt is missing or has no dependency entries.\n' >&2
    exit 1
fi

if [[ -e .venv || -L .venv ]]; then
    if [[ ! -x .venv/bin/python ]] || ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
        printf '[ERROR] Existing .venv is unusable; preserved unchanged. Repair it explicitly.\n' >&2
        exit 1
    fi
else
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD=python3
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD=python
    else
        printf '[ERROR] Python is not installed or not in PATH.\n' >&2
        exit 1
    fi
    "$PYTHON_CMD" -m venv .venv
fi

.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
printf 'Setup completed successfully!\n'
