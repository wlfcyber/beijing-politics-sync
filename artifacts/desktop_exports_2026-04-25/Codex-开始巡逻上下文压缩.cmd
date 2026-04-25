@echo off
chcp 65001 >nul
set "WATCHDOG=%USERPROFILE%\.codex\network-tools\run_compact_watchdog_loop.ps1"

if not exist "%WATCHDOG%" (
  echo [ERROR] Watchdog script not found:
  echo %WATCHDOG%
  pause
  exit /b 1
)

start "Codex Compact Watchdog" powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "%WATCHDOG%"

echo Codex 上下文压缩巡逻已启动。
echo.
echo 它会在后台每 3 分钟检查一次所有 Codex 线程：
echo - 如果发现某线程自动压缩上下文卡住超过 10 分钟
echo - 会备份线程、写恢复摘要、软打断卡死状态
echo - 并把接管提示放进 continuation_queue.jsonl
echo.
echo 重复点击不会开多个巡逻进程。
timeout /t 5 >nul
