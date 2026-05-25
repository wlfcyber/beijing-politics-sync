$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$auditDir = $PSScriptRoot
$runDir = Split-Path -Parent $auditDir
$sourceResume = Join-Path $auditDir 'resume_after_gptpro_v65.ps1'
$sourceIntake = Join-Path $runDir '05_gptpro_review\run_gptpro_v65_intake_check.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_post_gptpro_resume_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_post_gptpro_resume_test_*') {
    throw "Refusing to delete unexpected temp path: $resolved"
  }
  Remove-Item -LiteralPath $resolved -Recurse -Force
}

function Assert-Equal {
  param(
    [object]$Actual,
    [object]$Expected,
    [string]$Message
  )
  if ($Actual -ne $Expected) {
    throw "$Message Expected=[$Expected] Actual=[$Actual]"
  }
}

function Assert-True {
  param(
    [bool]$Condition,
    [string]$Message
  )
  if (-not $Condition) {
    throw $Message
  }
}

function New-CompleteGptResult {
  $body = @"
# GPT Pro V65 External Review Result

Verdict: ready_for_claude_review_after_gptpro after source verification.

## P0 findings

- P0: no direct final pass; all severe issues must be routed back to source verification before Claude.

## P1 findings

- P1: check structure and transfer clarity before final delivery.

## Thinking handbook structure judgment

The thinking handbook should keep a framework trigger chain: material signal -> method -> answer hook.

## Reasoning handbook structure judgment

The reasoning handbook should group by reasoning form and same-form question families.

## Must-fix-before-Claude list

- Claude V63 can run only after GPT Pro triage and source-verified patches.
- must-fix before Claude: verify P0/P1 claims against source-lock ledgers.

## Forbidden claims

- forbidden claims: no final pass, no publish-ready statement, no strict completion claim before Governor and Confucius.

## Source verification requests

- source verification: route each suggested patch to original question, answer key, rubric, source-lock, and ledger.

This body is deliberately long enough for the intake length gate. It repeats the required review signals in natural language so the intake runner can classify it as complete enough for triage, while still requiring local source verification before any patch affects the student-facing artifacts. The result should never be treated as final approval by itself.
"@
  return $body
}

function New-TestRun {
  Remove-SafeTempRoot $tempRoot
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '05_gptpro_review') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '06_claude_review') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '07_governor_confucius') | Out-Null
  Copy-Item -LiteralPath $sourceResume -Destination (Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1') -Force
  Copy-Item -LiteralPath $sourceIntake -Destination (Join-Path $tempRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1') -Force
  @'
$ErrorActionPreference = 'Stop'
'claude runner invoked' | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'fake_claude_invoked.txt') -Encoding UTF8
'fake Claude V63 result' | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md') -Encoding UTF8
0 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'claude_external_review_v63_return_code.txt') -Encoding UTF8
exit 0
'@ | Set-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\run_claude_external_review_v63.ps1') -Encoding UTF8
}

function Invoke-Resume {
  param([switch]$RunClaude)
  $script = Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1'
  $output = Join-Path $tempRoot 'resume_host_output.txt'
  $ErrorActionPreference = 'Continue'
  try {
    if ($RunClaude) {
      & powershell -NoProfile -ExecutionPolicy Bypass -File $script -ProjectRoot $tempRoot -RunClaude *> $output
    } else {
      & powershell -NoProfile -ExecutionPolicy Bypass -File $script -ProjectRoot $tempRoot *> $output
    }
    return $LASTEXITCODE
  } finally {
    $ErrorActionPreference = 'Stop'
  }
}

try {
  Assert-True (Test-Path -LiteralPath $sourceResume) 'Missing resume runner: resume_after_gptpro_v65.ps1'

  New-TestRun
  $exit = Invoke-Resume
  Assert-Equal $exit 2 'Missing GPT result should keep the resume gate blocked.'
  $report = Get-Content -LiteralPath (Join-Path $tempRoot '07_governor_confucius\POST_GPTPRO_RESUME_CHECK_V78.md') -Raw -Encoding UTF8
  Assert-True ($report -match 'BLOCKED_MISSING_GPTPRO_RESULT') 'Report should preserve the intake blocked status.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt'))) 'Claude runner must not run while GPT result is missing.'

  New-TestRun
  New-CompleteGptResult | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  $exit = Invoke-Resume
  Assert-Equal $exit 3 'Ready intake without filled triage should stop before Claude.'
  $report = Get-Content -LiteralPath (Join-Path $tempRoot '07_governor_confucius\POST_GPTPRO_RESUME_CHECK_V78.md') -Raw -Encoding UTF8
  Assert-True ($report -match 'READY_FOR_GPTPRO_TRIAGE') 'Report should show the GPT intake ready status.'
  Assert-True ($report -match 'NEEDS_GPTPRO_TRIAGE') 'Report should require filled GPT triage before Claude.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt'))) 'Claude runner must not run before triage is filled.'

  New-TestRun
  New-CompleteGptResult | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  'filled source-verified GPT Pro triage' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  $exit = Invoke-Resume -RunClaude
  Assert-Equal $exit 0 'Ready intake plus triage should allow the explicit Claude run.'
  Assert-True (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt')) 'Explicit RunClaude should invoke the Claude runner only after gates are ready.'
  $report = Get-Content -LiteralPath (Join-Path $tempRoot '07_governor_confucius\POST_GPTPRO_RESUME_CHECK_V78.md') -Raw -Encoding UTF8
  Assert-True ($report -match 'CLAUDE_V63_RUN_COMPLETED') 'Report should record the Claude run completion status.'

  'PASS'
} finally {
  if ($env:KEEP_POST_GPTPRO_RESUME_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
