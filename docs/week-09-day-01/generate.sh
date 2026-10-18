#!/usr/bin/env bash
# Rebuild Week 9 PDFs + PPTX using a local venv (Ubuntu PEP 668 safe).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
VENV="$ROOT/.venv-docs"
REQ="$(dirname "$0")/requirements.txt"

if ! command -v python3 >/dev/null; then
  echo "Install Python first: sudo apt install python3 python3-venv python3-full" >&2
  exit 1
fi

PY=python3
if python3 -m venv "$VENV" 2>/dev/null && [[ -x "$VENV/bin/python" ]]; then
  "$VENV/bin/pip" install -q -r "$REQ"
  PY="$VENV/bin/python"
else
  # Fallback when ensurepip/venv is unavailable (some cloud images).
  SITE="$VENV/lib/python3.12/site-packages"
  mkdir -p "$SITE"
  python3 -m pip install -q --target "$SITE" -r "$REQ"
  export PYTHONPATH="$SITE${PYTHONPATH:+:$PYTHONPATH}"
fi

if [[ "${1:-}" == "--pptx-only" ]]; then
  exec "$PY" "$ROOT/docs/week-09-day-01/build_editable_pptx.py"
fi

exec "$PY" "$ROOT/docs/week-09-day-01/generate-pdfs.py"
