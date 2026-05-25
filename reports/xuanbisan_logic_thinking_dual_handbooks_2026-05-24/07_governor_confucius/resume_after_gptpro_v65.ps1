param(
  [string]$ProjectRoot = "",
  [switch]$RunClaude
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$reportPath = Join-Path $ProjectRoot '07_governor_confucius\POST_GPTPRO_RESUME_CHECK_V78.md'
$intakeScript = Join-Path $ProjectRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1'
$intakeCheck = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md'
$triageValidator = Join-Path $ProjectRoot '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1'
$triageCheck = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md'
$gptResult = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md'
$gptTriage = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md'
$claudeScript = Join-Path $ProjectRoot '06_claude_review\run_claude_external_review_v63.ps1'
$claudeResult = Join-Path $ProjectRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'
$intakeHostOutput = Join-Path $ProjectRoot '05_gptpro_review\gptpro_v65_intake_host_output.txt'
$triageHostOutput = Join-Path $ProjectRoot '05_gptpro_review\gptpro_v65_triage_v83_host_output.txt'
$claudeHostOutput = Join-Path $ProjectRoot '06_claude_review\claude_v63_resume_host_output.txt'
$checkedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')

function Get-IntakeStatus {
  if (-not (Test-Path -LiteralPath $intakeCheck)) {
    return 'MISSING_INTAKE_CHECK'
  }
  $line = Select-String -LiteralPath $intakeCheck -Pattern 'Status:' | Select-Object -First 1
  if ($null -eq $line) {
    return 'MISSING_STATUS_LINE'
  }
  return (($line.Line -replace '^.*Status:\s*', '') -replace '`', '').Trim()
}

function Get-TriageStatus {
  if (-not (Test-Path -LiteralPath $triageCheck)) {
    return 'MISSING_TRIAGE_CHECK'
  }
  $line = Select-String -LiteralPath $triageCheck -Pattern 'Status:' | Select-Object -First 1
  if ($null -eq $line) {
    return 'MISSING_TRIAGE_STATUS_LINE'
  }
  return (($line.Line -replace '^.*Status:\s*', '') -replace '`', '').Trim()
}

function Write-ResumeReport {
  param(
    [string]$Status,
    [string[]]$Findings,
    [string[]]$NextActions
  )

  $lines = @()
  $lines += '# Post-GPT Pro Resume Check V78'
  $lines += ''
  $lines += "Status: ``$Status``"
  $lines += ''
  $lines += "- Checked at: $checkedAt"
  $lines += "- GPT Pro result: ``05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md``"
  $lines += "- GPT Pro intake check: ``05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md``"
  $lines += "- GPT Pro triage: ``05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md``"
  $lines += "- Claude V63 result: ``06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md``"
  $lines += "- Explicit Claude run requested: ``$RunClaude``"
  $lines += ''
  $lines += '## Findings'
  $lines += ''
  foreach ($finding in $Findings) {
    $lines += "- $finding"
  }
  $lines += ''
  $lines += '## Next Actions'
  $lines += ''
  foreach ($action in $NextActions) {
    $lines += "- $action"
  }
  $lines += ''
  $lines += '## Guardrail'
  $lines += ''
  $lines += '- This report does not count as GPT Pro review, Claude review, Governor pass, Confucius pass, Word/PDF QA, or final acceptance.'
  $lines += '- Claude V63 is only allowed after GPT Pro result, ready intake, and filled GPT Pro triage exist.'
  $lines += ''
  Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
}

if (-not (Test-Path -LiteralPath $intakeScript)) {
  Write-ResumeReport `
    -Status 'BLOCKED_MISSING_INTAKE_SCRIPT' `
    -Findings @("Missing intake script: $intakeScript.") `
    -NextActions @('Restore the GPT Pro intake script before resuming external-review closure.')
  exit 2
}

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
  & powershell -NoProfile -ExecutionPolicy Bypass -File $intakeScript -ProjectRoot $ProjectRoot *> $intakeHostOutput
  $intakeExit = $LASTEXITCODE
} finally {
  $ErrorActionPreference = $oldPreference
}

$intakeStatus = Get-IntakeStatus
if ($intakeExit -ne 0) {
  Write-ResumeReport `
    -Status $intakeStatus `
    -Findings @("GPT Pro intake runner exited with code $intakeExit.", "Intake status is ``$intakeStatus``.") `
    -NextActions @('Save or replace the real GPT Pro V65 result, then rerun this resume check.', 'Do not run Claude V63, Governor, Confucius, Word, or PDF gates yet.')
  exit $intakeExit
}

if ($intakeStatus -ne 'READY_FOR_GPTPRO_TRIAGE') {
  Write-ResumeReport `
    -Status $intakeStatus `
    -Findings @("GPT Pro intake runner exited with code 0 but status is ``$intakeStatus``.") `
    -NextActions @('Inspect the intake check before proceeding.', 'Do not run Claude V63 until the status is READY_FOR_GPTPRO_TRIAGE.')
  exit 2
}

$triageReady = (Test-Path -LiteralPath $gptTriage) -and -not [string]::IsNullOrWhiteSpace((Get-Content -LiteralPath $gptTriage -Raw -Encoding UTF8))
if (-not $triageReady) {
  Write-ResumeReport `
    -Status 'READY_FOR_GPTPRO_TRIAGE_NEEDS_GPTPRO_TRIAGE' `
    -Findings @('GPT Pro intake is READY_FOR_GPTPRO_TRIAGE.', 'Filled GPT Pro triage is missing or empty, so Claude V63 remains blocked.') `
    -NextActions @('Fill 05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md from the real GPT Pro result.', 'Apply only source-verified P0/P1 patches before Claude if GPT Pro requires them.', 'Rerun this resume check after triage is filled.')
  exit 3
}

if (-not (Test-Path -LiteralPath $triageValidator)) {
  Write-ResumeReport `
    -Status 'BLOCKED_MISSING_GPTPRO_TRIAGE_VALIDATOR' `
    -Findings @("Missing GPT Pro triage validator: $triageValidator.") `
    -NextActions @('Restore 05_gptpro_review\validate_gptpro_v65_triage_v83.ps1 before running Claude V63.')
  exit 2
}

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
  & powershell -NoProfile -ExecutionPolicy Bypass -File $triageValidator -ProjectRoot $ProjectRoot *> $triageHostOutput
  $triageExit = $LASTEXITCODE
} finally {
  $ErrorActionPreference = $oldPreference
}

$triageStatus = Get-TriageStatus
if ($triageExit -ne 0) {
  Write-ResumeReport `
    -Status $triageStatus `
    -Findings @("GPT Pro triage validator exited with code $triageExit.", "Triage status is ``$triageStatus``.") `
    -NextActions @('Complete 05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md with source-routed P0/P1/P2 triage before Claude.', 'Do not run Claude V63, Governor, Confucius, Word, or PDF gates yet.')
  exit $triageExit
}

if ($triageStatus -ne 'READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE') {
  Write-ResumeReport `
    -Status $triageStatus `
    -Findings @("GPT Pro triage validator exited with code 0 but status is ``$triageStatus``.") `
    -NextActions @('Inspect GPTPRO_V65_TRIAGE_READY_CHECK_V83.md before proceeding.', 'Do not run Claude V63 until the triage check is ready.')
  exit 3
}

if (-not $RunClaude) {
  Write-ResumeReport `
    -Status 'READY_TO_RUN_CLAUDE_V63' `
    -Findings @('GPT Pro result exists.', 'GPT Pro intake is READY_FOR_GPTPRO_TRIAGE.', 'Filled GPT Pro triage passed V83 quality gate.') `
    -NextActions @('Run this script with -RunClaude when ready to invoke Claude V63.', 'Do not claim final acceptance until Claude triage, source patches, Governor, Confucius, and Word/PDF QA are complete.')
  exit 4
}

if (-not (Test-Path -LiteralPath $claudeScript)) {
  Write-ResumeReport `
    -Status 'BLOCKED_MISSING_CLAUDE_RUNNER' `
    -Findings @("Missing Claude V63 runner: $claudeScript.") `
    -NextActions @('Restore the guarded Claude V63 runner, then rerun with -RunClaude.')
  exit 2
}

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
  & powershell -NoProfile -ExecutionPolicy Bypass -File $claudeScript *> $claudeHostOutput
  $claudeExit = $LASTEXITCODE
} finally {
  $ErrorActionPreference = $oldPreference
}

$claudeResultReady = (Test-Path -LiteralPath $claudeResult) -and -not [string]::IsNullOrWhiteSpace((Get-Content -LiteralPath $claudeResult -Raw -Encoding UTF8))
if ($claudeExit -eq 0 -and $claudeResultReady) {
  Write-ResumeReport `
    -Status 'CLAUDE_V63_RUN_COMPLETED' `
    -Findings @('GPT Pro result exists.', 'GPT Pro intake is READY_FOR_GPTPRO_TRIAGE.', 'Filled GPT Pro triage exists.', 'Claude V63 runner exited with code 0 and produced a non-empty result file.') `
    -NextActions @('Fill 06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md.', 'Route GPT Pro and Claude findings back to local source evidence before patching.', 'Only after source-verified patches may final Governor, Confucius, Word, and PDF gates run.')
  exit 0
}

Write-ResumeReport `
  -Status 'CLAUDE_V63_RUN_FAILED_OR_EMPTY_RESULT' `
  -Findings @("Claude V63 runner exited with code $claudeExit.", "Claude result ready: $claudeResultReady.") `
  -NextActions @('Inspect 06_claude_review\claude_v63_resume_host_output.txt and the Claude runner logs.', 'Do not proceed to final gates until Claude V63 returns a non-empty result.')

if ($claudeExit -eq 0) {
  exit 5
}
exit $claudeExit
