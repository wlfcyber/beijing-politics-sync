#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02"
STAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$RUN_DIR/logs/supervisor_restart_finish_$STAMP.log"

mkdir -p "$RUN_DIR/logs"
cd "$RUN_DIR"

nohup bash "$RUN_DIR/START_CLAUDECODE_BIXIU4_FROM_ZERO.sh" > "$LOG_FILE" 2>&1 &
echo "restarted_pid=$!"
echo "restart_log=$LOG_FILE"
