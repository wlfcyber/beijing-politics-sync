#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03"
LOG_DIR="$RUN_DIR/claudecode_lane/logs"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_BATCH04H_PROMPT.md"
TS="$(date +%Y%m%d_%H%M%S)"

mkdir -p "$LOG_DIR"
cd "$RUN_DIR"

/Users/wanglifei/.local/bin/claude -p \
  --output-format stream-json \
  --verbose \
  --permission-mode bypassPermissions \
  --model opus \
  --debug-file "$LOG_DIR/claudecode_batch04H_${TS}.debug.log" \
  "$(cat "$PROMPT_FILE")" \
  > "$LOG_DIR/claudecode_batch04H_${TS}.stream.json" \
  2> "$LOG_DIR/claudecode_batch04H_${TS}.stderr"

ln -sfn "$LOG_DIR/claudecode_batch04H_${TS}.debug.log" "$LOG_DIR/latest"
