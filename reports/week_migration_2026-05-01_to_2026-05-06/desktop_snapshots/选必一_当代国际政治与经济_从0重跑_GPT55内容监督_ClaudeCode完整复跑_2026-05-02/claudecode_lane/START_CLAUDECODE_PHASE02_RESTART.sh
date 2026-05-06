#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_PHASE02_RESTART_PROMPT.md"
LOG_DIR="$RUN_DIR/claudecode_lane/logs"
STAMP="$(date +%Y%m%d_%H%M%S)"

mkdir -p "$LOG_DIR"

cd "$RUN_DIR"

/Users/wanglifei/.local/bin/claude \
  -p \
  --output-format stream-json \
  --verbose \
  --include-partial-messages \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --effort max \
  --name "选必一Phase02证据矩阵-ClaudeCode重启-$STAMP" \
  --add-dir "/Users/wanglifei/Desktop/2024模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2025模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2026模拟题" \
  --add-dir "$RUN_DIR" \
  --debug-file "$LOG_DIR/claude-phase02-restart-$STAMP.debug.log" \
  "$(< "$PROMPT_FILE")" \
  > "$LOG_DIR/claude-phase02-restart-$STAMP.stream.json" \
  2> "$LOG_DIR/claude-phase02-restart-$STAMP.stderr"
