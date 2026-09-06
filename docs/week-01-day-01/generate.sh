#!/usr/bin/env bash
# Rebuild Week 1 PDFs + PPTX using a local venv (Ubuntu PEP 668 safe).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.venv-docs"
REQ="$(dirname "$0")/requirements.txt"

if ! command -v python3 >/dev/null; then
  echo "Install Python first: sudo apt install python3 python3-venv python3-full" >&2
  exit 1
fi

if [[ ! -x "$VENV/bin/python" ]]; then
  python3 -m venv "$VENV"
fi
"$VENV/bin/pip" install -q -r "$REQ"

if [[ "${1:-}" == "--pptx-only" ]]; then
  exec "$VENV/bin/python" "$ROOT/docs/week-01-day-01/build_editable_pptx.py"
fi

exec "$VENV/bin/python" "$ROOT/docs/week-01-day-01/generate-pdfs.py"
