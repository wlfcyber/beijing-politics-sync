#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_双线总控_2026-05-02"
PROMPT_FILE="$RUN_DIR/claudecode_lane/CLAUDECODE_RESTART_PROMPT_2026-05-02_2202.md"
OUT_DIR="$RUN_DIR/claudecode_lane/restart_2026-05-02_2202"
LOG_DIR="$RUN_DIR/logs"

mkdir -p "$OUT_DIR/entries" "$OUT_DIR/suite_reports" "$OUT_DIR/coverage" "$OUT_DIR/blockers" "$OUT_DIR/logs" "$LOG_DIR"

exec /Users/wanglifei/.local/bin/claude -p \
  --name "选必一_独立复跑_2026-05-02_2202" \
  --model opus \
  --effort max \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --verbose \
  --output-format stream-json \
  --include-partial-messages \
  --max-budget-usd 3.00 \
  --add-dir "$RUN_DIR" \
  --add-dir "/Users/wanglifei/Desktop/2024模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2025模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2026模拟题" \
  --add-dir "/Users/wanglifei/.codex/skills/feige-politics-garden" \
  --add-dir "/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator" \
  --add-dir "/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbiyi" \
  --debug-file "$OUT_DIR/logs/claude-debug.log" \
  "$(< "$PROMPT_FILE")"
