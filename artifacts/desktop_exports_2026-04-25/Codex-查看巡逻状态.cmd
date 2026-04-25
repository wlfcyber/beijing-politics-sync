@echo off
chcp 65001 >nul
echo === Codex Compact Watchdog Status ===
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$p=Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*run_compact_watchdog_loop.ps1*' }; if ($p) { '状态: 正在巡逻'; $p | Select-Object ProcessId,Name,CommandLine | Format-List } else { '状态: 未运行' }; ''; '最近日志:'; $log=\"$env:USERPROFILE\.codex\network-tools\compact-watchdog\compact_watchdog.log\"; if (Test-Path $log) { Get-Content -LiteralPath $log -Tail 20 } else { '还没有日志' }; ''; '接管队列:'; $queue=\"$env:USERPROFILE\.codex\network-tools\compact-watchdog\continuation_queue.jsonl\"; if (Test-Path $queue) { Get-Content -LiteralPath $queue -Tail 5 } else { '当前没有接管队列' }"
echo.
pause
