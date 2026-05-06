#!/usr/bin/env bash
set -uo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02"
PROMPT_FILE="$RUN_DIR/CLAUDECODE_START_PROMPT.md"
MASTER_FILE="$RUN_DIR/MASTER_REQUIREMENTS_FOR_CLAUDECODE_2026-05-02.md"
SUPERVISOR_FILE="$RUN_DIR/SUPERVISOR_DIRECTIVE_2026-05-02.md"
PATCH_FILE="$RUN_DIR/SUPERVISOR_PATCH_2026-05-02_HEARTBEAT_CLEAN_FINAL.md"
LOG_DIR="$RUN_DIR/logs"
mkdir -p "$LOG_DIR"

cd "$RUN_DIR"

claude auth status || true

claude \
  --name "必修四从0重跑_2026-05-02_最终收口" \
  --model opus \
  --effort max \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --add-dir "/Users/wanglifei/Desktop/2024模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2025模拟题" \
  --add-dir "/Users/wanglifei/Desktop/2026模拟题" \
  --add-dir "/Users/wanglifei/.codex/skills/feige-politics-garden-bixiu4" \
  --debug-file "$LOG_DIR/claude-debug-finish.log" \
  "$(cat "$PROMPT_FILE"; printf '\n\n'; cat "$MASTER_FILE"; printf '\n\n'; cat "$SUPERVISOR_FILE"; printf '\n\n'; cat "$PATCH_FILE")"
