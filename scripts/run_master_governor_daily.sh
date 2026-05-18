#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${WORKSPACE:-/Users/wanglifei/Desktop/北京高考政治}"
SYNC_ROOT="${SYNC_ROOT:-/Users/wanglifei/GaokaoPolitics/beijing-politics-sync}"

python3 "$SYNC_ROOT/scripts/master_governor.py" report \
  --workspace "$WORKSPACE" \
  --sync-root "$SYNC_ROOT"
