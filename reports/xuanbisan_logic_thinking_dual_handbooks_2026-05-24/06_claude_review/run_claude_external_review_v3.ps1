$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$reviewDir = $PSScriptRoot
$runDir = Split-Path -Parent $reviewDir
$packet = Join-Path $runDir '10_packets\CLAUDE_REVIEW_PACKET_V3.md'
$stdout = Join-Path $reviewDir 'claude_external_review_v3_stdout.log'
$stderr = Join-Path $reviewDir 'claude_external_review_v3_stderr.log'
$returnCode = Join-Path $reviewDir 'claude_external_review_v3_return_code.txt'
$startedAt = Join-Path $reviewDir 'claude_external_review_v3_started_at.txt'
$versionFile = Join-Path $reviewDir 'claude_external_review_v3_version.txt'

Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz' | Set-Content -LiteralPath $startedAt -Encoding UTF8
claude --version | Set-Content -LiteralPath $versionFile -Encoding UTF8

$ErrorActionPreference = 'Continue'
Get-Content -LiteralPath $packet -Raw -Encoding UTF8 | & claude -p --model opus --effort max --permission-mode bypassPermissions --output-format text --add-dir $runDir 1> $stdout 2> $stderr
$LASTEXITCODE | Set-Content -LiteralPath $returnCode -Encoding UTF8
