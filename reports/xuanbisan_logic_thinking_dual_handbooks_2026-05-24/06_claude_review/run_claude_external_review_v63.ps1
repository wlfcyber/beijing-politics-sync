$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$reviewDir = $PSScriptRoot
$runDir = Split-Path -Parent $reviewDir
$packet = Join-Path $runDir '10_packets\CLAUDE_REVIEW_PACKET_V63.md'
$gptResult = Join-Path $runDir '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md'
$gptIntakeCheck = Join-Path $runDir '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md'
$gptTriage = Join-Path $runDir '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md'
$gptTriageReadyCheck = Join-Path $runDir '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md'
$result = Join-Path $reviewDir 'CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'
$stdout = Join-Path $reviewDir 'claude_external_review_v63_stdout.log'
$stderr = Join-Path $reviewDir 'claude_external_review_v63_stderr.log'
$returnCode = Join-Path $reviewDir 'claude_external_review_v63_return_code.txt'
$startedAt = Join-Path $reviewDir 'claude_external_review_v63_started_at.txt'
$versionFile = Join-Path $reviewDir 'claude_external_review_v63_version.txt'
$blockedFile = Join-Path $reviewDir 'claude_external_review_v63_blocked.txt'

if (-not (Test-Path -LiteralPath $gptResult)) {
  "blocked: missing GPT Pro V65 result at $gptResult" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 result exists."
}

$gptText = Get-Content -LiteralPath $gptResult -Raw -Encoding UTF8
if ([string]::IsNullOrWhiteSpace($gptText)) {
  "blocked: GPT Pro V65 result file is empty at $gptResult" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked because GPT Pro V65 result file is empty."
}

if (-not (Test-Path -LiteralPath $gptIntakeCheck)) {
  "blocked: missing GPT Pro V65 intake check at $gptIntakeCheck" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 intake check exists."
}

$gptIntakeText = Get-Content -LiteralPath $gptIntakeCheck -Raw -Encoding UTF8
if ($gptIntakeText -notmatch 'Status:\s*`?READY_FOR_GPTPRO_TRIAGE`?') {
  "blocked: GPT Pro V65 intake check is not READY_FOR_GPTPRO_TRIAGE at $gptIntakeCheck" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 intake check is READY_FOR_GPTPRO_TRIAGE."
}

if (-not (Test-Path -LiteralPath $gptTriage)) {
  "blocked: missing filled GPT Pro V65 triage at $gptTriage" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 triage is filled."
}

$gptTriageText = Get-Content -LiteralPath $gptTriage -Raw -Encoding UTF8
if ([string]::IsNullOrWhiteSpace($gptTriageText)) {
  "blocked: filled GPT Pro V65 triage is empty at $gptTriage" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked because GPT Pro V65 triage file is empty."
}

if (-not (Test-Path -LiteralPath $gptTriageReadyCheck)) {
  "blocked: missing GPT Pro V65 V83 triage ready check at $gptTriageReadyCheck" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 triage passes the V83 quality gate."
}

$gptTriageReadyText = Get-Content -LiteralPath $gptTriageReadyCheck -Raw -Encoding UTF8
if ($gptTriageReadyText -notmatch 'Status:\s*`?READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`?') {
  "blocked: GPT Pro V65 V83 triage ready check is not ready at $gptTriageReadyCheck" | Set-Content -LiteralPath $blockedFile -Encoding UTF8
  2 | Set-Content -LiteralPath $returnCode -Encoding UTF8
  throw "Claude V63 is blocked until GPT Pro V65 V83 triage ready check is READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE."
}

if (Test-Path -LiteralPath $blockedFile) {
  Remove-Item -LiteralPath $blockedFile -Force
}

Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz' | Set-Content -LiteralPath $startedAt -Encoding UTF8
claude --version | Set-Content -LiteralPath $versionFile -Encoding UTF8

$prompt = @"
$(Get-Content -LiteralPath $packet -Raw -Encoding UTF8)

## Captured GPT Pro V65 Result

$gptText
"@

$ErrorActionPreference = 'Continue'
$prompt | & claude -p --model opus --effort max --permission-mode bypassPermissions --output-format text --add-dir $runDir 1> $stdout 2> $stderr
$exitCode = $LASTEXITCODE
$exitCode | Set-Content -LiteralPath $returnCode -Encoding UTF8

if ($exitCode -eq 0 -and -not (Test-Path -LiteralPath $result) -and (Test-Path -LiteralPath $stdout)) {
  $stdoutText = Get-Content -LiteralPath $stdout -Raw -Encoding UTF8
  if (-not [string]::IsNullOrWhiteSpace($stdoutText)) {
    $stdoutText | Set-Content -LiteralPath $result -Encoding UTF8
  }
}
