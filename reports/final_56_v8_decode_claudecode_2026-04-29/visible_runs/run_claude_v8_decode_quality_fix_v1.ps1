$ErrorActionPreference = 'Continue'
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
Set-Location 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible'
try {
  Get-Content -LiteralPath 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\CLAUDE_PROMPT_V8_DECODE_QUALITY_FIX.md' -Encoding UTF8 | claude -p --verbose --model opus --effort max --output-format stream-json --include-partial-messages --debug-file 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\visible_runs\claude_v8_decode_quality_fix_debug_v1.log' --max-budget-usd 40 > 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\visible_runs\claude_v8_decode_quality_fix_stream_v1.jsonl' 2> 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\visible_runs\claude_v8_decode_quality_fix_stderr_v1.log'
  "exit_code=$LASTEXITCODE
time=$(Get-Date -Format o)" | Set-Content -LiteralPath 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\visible_runs\claude_v8_decode_quality_fix_done_v1.txt' -Encoding UTF8
} catch {
  "exception=$($_.Exception.Message)
time=$(Get-Date -Format o)" | Set-Content -LiteralPath 'C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29\visible_runs\claude_v8_decode_quality_fix_done_v1.txt' -Encoding UTF8
  throw
}
