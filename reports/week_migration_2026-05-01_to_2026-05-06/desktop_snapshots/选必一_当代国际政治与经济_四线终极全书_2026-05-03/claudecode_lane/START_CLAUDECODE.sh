#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03"
ROOT="/Users/wanglifei/Desktop/北京高考政治"
LOG_DIR="$RUN_DIR/claudecode_lane/logs"
TS="$(date +%Y%m%d_%H%M%S)"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_START_PROMPT.md"

mkdir -p "$LOG_DIR"

cd "$RUN_DIR"

/Users/wanglifei/.local/bin/claude -p \
  --verbose \
  --output-format stream-json \
  --include-partial-messages \
  --permission-mode bypassPermissions \
  --add-dir "$ROOT" \
  --debug-file "$LOG_DIR/claudecode_full_${TS}.debug.log" \
  "$(cat "$PROMPT_FILE")" \
  > "$LOG_DIR/claudecode_full_${TS}.stream.json" \
  2> "$LOG_DIR/claudecode_full_${TS}.stderr"
