$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RunDir = "C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24"
$LaneDir = Join-Path $RunDir "03_claudecode_lane"
$PromptPath = Join-Path $LaneDir "CLAUDECODE_B_LINE_PROMPT.md"
$StdoutPath = Join-Path $LaneDir "logs\claudecode_b_line_stdout.log"
$StderrPath = Join-Path $LaneDir "logs\claudecode_b_line_stderr.log"
$VersionPath = Join-Path $LaneDir "claudecode_version.txt"
$CommandPath = Join-Path $LaneDir "claudecode_command.txt"
$ReturnPath = Join-Path $LaneDir "claudecode_return_code.txt"
$StartedPath = Join-Path $LaneDir "claudecode_started_at.txt"

New-Item -ItemType Directory -Force -Path (Join-Path $LaneDir "logs") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $LaneDir "entries") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $LaneDir "suite_reports") | Out-Null

Get-Date -Format o | Set-Content -LiteralPath $StartedPath -Encoding UTF8
(& claude --version) 2>&1 | Set-Content -LiteralPath $VersionPath -Encoding UTF8

$ArgsList = @(
  "-p",
  "--model", "opus",
  "--effort", "max",
  "--permission-mode", "bypassPermissions",
  "--output-format", "text",
  "--add-dir", "C:\Users\Administrator\Desktop\2024各区模拟题",
  "C:\Users\Administrator\Desktop\2025各区模拟题",
  "C:\Users\Administrator\Desktop\2026各区模拟题",
  "C:\Users\Administrator\Desktop\beijing_politics_research",
  "C:\Users\Administrator\Desktop\飞哥的政治庄园",
  "C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible"
)

("claude " + (($ArgsList | ForEach-Object { if($_ -match '\s') { '"' + $_ + '"' } else { $_ } }) -join " ") + " < " + '"' + $PromptPath + '"') |
  Set-Content -LiteralPath $CommandPath -Encoding UTF8

Get-Content -LiteralPath $PromptPath -Raw |
  & claude @ArgsList 1> $StdoutPath 2> $StderrPath

$LASTEXITCODE | Set-Content -LiteralPath $ReturnPath -Encoding UTF8

