#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

if [ "${1:-}" = "demo" ]; then
  python -m uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
else
  python -m uvicorn backend.app:app --host 0.0.0.0 --port 8000
fi
