@echo off
chcp 65001 >nul
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*run_compact_watchdog_loop.ps1*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
echo Codex 上下文压缩巡逻已停止。
timeout /t 3 >nul
