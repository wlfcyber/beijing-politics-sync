#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30"
PROMPT="$RUN_DIR/claudecode_lane/prompts/START_CLAUDECODE_XUANBIER_FULL_AUDIT_20260504.md"
STAMP="$(date +%Y%m%d_%H%M%S)"
SESSION="xuanbier_claudecode_full_$STAMP"
OUT="$RUN_DIR/claudecode_lane/logs/${SESSION}.jsonl"
DBG="$RUN_DIR/claudecode_lane/logs/${SESSION}.debug.log"

mkdir -p "$RUN_DIR/claudecode_lane/logs" "$RUN_DIR/claudecode_lane/outputs"

screen -dmS "$SESSION" bash -lc "cd /Users/wanglifei/Desktop/北京高考政治 && /Users/wanglifei/.local/bin/claude -p --output-format stream-json --verbose --permission-mode bypassPermissions --model opus --debug-file '$DBG' \"\$(cat '$PROMPT')\" > '$OUT' 2>&1"

printf '%s\n' "$SESSION" > "$RUN_DIR/claudecode_lane/CURRENT_SESSION.txt"
printf '%s\n' "$OUT" > "$RUN_DIR/claudecode_lane/CURRENT_LOG.txt"
printf '%s\n' "$DBG" > "$RUN_DIR/claudecode_lane/CURRENT_DEBUG_LOG.txt"
echo "started $SESSION"
echo "$OUT"
