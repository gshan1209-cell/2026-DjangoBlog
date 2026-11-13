#!/usr/bin/env bash
# Local development only; never use Django runserver as a production server.
set -euo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$PROJECT_DIR"
PYTHON="$PROJECT_DIR/.venv/bin/python"

if [[ ! -x "$PYTHON" ]]; then
    printf '%s\n' 'Missing executable .venv/bin/python. Prepare the virtual environment and install Django first.' >&2
    exit 1
fi
if [[ ! -f manage.py ]]; then
    printf '%s\n' 'Missing manage.py in the project directory.' >&2
    exit 1
fi

# Use the virtual environment interpreter directly, without altering caller PATH.
# Migration failure stops startup and preserves its exit status.
"$PYTHON" manage.py migrate --noinput
if [[ $# -eq 0 ]]; then
    set -- 127.0.0.1:8000
fi
exec "$PYTHON" manage.py runserver "$@"
