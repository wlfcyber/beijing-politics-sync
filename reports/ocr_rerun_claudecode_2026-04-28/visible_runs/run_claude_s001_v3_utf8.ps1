$ErrorActionPreference='Continue'
Set-Location 'C:\bp_sync_visible'
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:LANG='C.UTF-8'
try {
  Get-Content -Raw -Encoding UTF8 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\CLAUDE_OCR_RERUN_S001_WINDOWS_PROMPT_V3_UTF8.md' | & claude -p --verbose --model opus --effort max --permission-mode bypassPermissions --dangerously-skip-permissions --output-format stream-json --include-partial-messages --debug-file 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_debug_v3.log' --add-dir 'C:\bp_sync_visible' --add-dir 'C:\Users\Administrator\Desktop\beijing_politics_research' --add-dir 'C:\Users\Administrator\Desktop\2024各区模拟题' 1> 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stream_v3.jsonl' 2> 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stderr_v3.log'
  $code = $LASTEXITCODE
} catch {
  $code = 999
  $_ | Out-File -FilePath 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stderr_v3.log' -Append -Encoding UTF8
}
"exit_code=$code
time=$(Get-Date -Format o)" | Out-File -FilePath 'C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_done_v3.txt' -Encoding UTF8
exit $code
