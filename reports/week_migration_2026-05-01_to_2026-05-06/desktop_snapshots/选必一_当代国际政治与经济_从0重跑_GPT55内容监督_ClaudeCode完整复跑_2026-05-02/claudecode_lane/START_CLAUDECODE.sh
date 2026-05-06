#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_START_PROMPT.md"
LOG_DIR="$RUN_DIR/claudecode_lane/logs"

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
  --name "选必一从0重跑-ClaudeCode完整复跑-2026-05-02" \
  --add-dir "/Users/wanglifei/Desktop/2024模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2025模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2026模拟题" \
  --add-dir "/Users/wanglifei/Desktop/北京高考政治" \
  --add-dir "/Users/wanglifei/GaokaoPolitics" \
  --debug-file "$LOG_DIR/claude-debug.log" \
  "$(< "$PROMPT_FILE")" \
  > "$LOG_DIR/claude.stream.json" \
  2> "$LOG_DIR/claude.stderr"
