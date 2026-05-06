#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02"
LOG_DIR="$RUN_DIR/claudecode_lane/logs"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_OVERNIGHT_FINAL_PROMPT.md"
TS="$(date +%Y%m%d_%H%M%S)"

mkdir -p "$LOG_DIR"
cd "$RUN_DIR"

/Users/wanglifei/.local/bin/claude \
  -p "$(cat "$PROMPT_FILE")" \
  --output-format stream-json \
  --verbose \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  > "$LOG_DIR/claude-overnight-final-$TS.stream.json" \
  2> "$LOG_DIR/claude-overnight-final-$TS.stderr"
