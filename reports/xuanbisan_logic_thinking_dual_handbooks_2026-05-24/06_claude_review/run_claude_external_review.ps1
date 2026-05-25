$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$runDir = 'C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24'
$reviewDir = Join-Path $runDir '06_claude_review'
$packet = Join-Path $runDir '10_packets\CLAUDE_REVIEW_PACKET_V0.md'
$stdout = Join-Path $reviewDir 'claude_external_review_stdout.log'
$stderr = Join-Path $reviewDir 'claude_external_review_stderr.log'
$returnCode = Join-Path $reviewDir 'claude_external_review_return_code.txt'
$startedAt = Join-Path $reviewDir 'claude_external_review_started_at.txt'
$versionFile = Join-Path $reviewDir 'claude_external_review_version.txt'

Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz' | Set-Content -LiteralPath $startedAt -Encoding UTF8
claude --version | Set-Content -LiteralPath $versionFile -Encoding UTF8

$ErrorActionPreference = 'Continue'
Get-Content -LiteralPath $packet -Raw -Encoding UTF8 | & claude -p --model opus --effort max --permission-mode bypassPermissions --output-format text --add-dir $runDir 1> $stdout 2> $stderr
$LASTEXITCODE | Set-Content -LiteralPath $returnCode -Encoding UTF8


