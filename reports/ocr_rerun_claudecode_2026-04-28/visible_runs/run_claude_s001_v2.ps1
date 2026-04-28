$ErrorActionPreference='Continue'
Set-Location 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible'
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
try {
  Get-Content -Raw -Encoding UTF8 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\CLAUDE_OCR_RERUN_S001_WINDOWS_PROMPT.md' | & claude -p --verbose --model opus --effort max --permission-mode bypassPermissions --dangerously-skip-permissions --output-format stream-json --include-partial-messages --debug-file 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_debug_v2.log' --add-dir 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible' --add-dir 'C:\Users\Administrator\Desktop\beijing_politics_research' --add-dir 'C:\Users\Administrator\Desktop\2024各区模拟题' 1> 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stream_v2.jsonl' 2> 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stderr_v2.log'
  $code = $LASTEXITCODE
} catch {
  $code = 999
  $_ | Out-File -FilePath 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_stderr_v2.log' -Append -Encoding UTF8
}
"exit_code=$code
time=$(Get-Date -Format o)" | Out-File -FilePath 'C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\ocr_rerun_claudecode_2026-04-28\visible_runs\claude_ocr_rerun_S001_windows_done_v2.txt' -Encoding UTF8
exit $code
