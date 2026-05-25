$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$auditDir = $PSScriptRoot
$sourceIntake = Join-Path $auditDir 'run_gptpro_v65_intake_check.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_gptpro_intake_v82_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_gptpro_intake_v82_test_*') {
    throw "Refusing to delete unexpected temp path: $resolved"
  }
  Remove-Item -LiteralPath $resolved -Recurse -Force
}

function Assert-True {
  param([bool]$Condition, [string]$Message)
  if (-not $Condition) { throw $Message }
}

function Assert-Equal {
  param([object]$Actual, [object]$Expected, [string]$Message)
  if ($Actual -ne $Expected) { throw "$Message Expected=[$Expected] Actual=[$Actual]" }
}

function New-TestRun {
  Remove-SafeTempRoot $tempRoot
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '05_gptpro_review') | Out-Null
  Copy-Item -LiteralPath $sourceIntake -Destination (Join-Path $tempRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1') -Force
}

function New-LongPlaceholderResult {
  $lines = @()
  $lines += '# GPT Pro V65 result placeholder'
  $lines += ''
  $lines += 'TODO: paste the real GPT Pro response here after upload.'
  $lines += 'Do not treat this template as the actual external review result.'
  $lines += ''
  $lines += 'Verdict: not_final'
  $lines += 'P0 findings: placeholder section waiting for real model output.'
  $lines += 'P1 findings: placeholder section waiting for real model output.'
  $lines += 'Thinking handbook structure judgment: 思维宝典 framework and 触发链 placeholder.'
  $lines += 'Reasoning handbook structure judgment: 推理宝典 同形 题型 placeholder.'
  $lines += 'Must-fix-before-Claude list: must-fix before Claude placeholder.'
  $lines += 'Forbidden claims: final pass is forbidden in this placeholder.'
  $lines += 'Source verification request: 回源 source verification ledger placeholder.'
  $lines += ''
  for ($i = 0; $i -lt 30; $i++) {
    $lines += "PLACEHOLDER line ${i}: this is only a template and the real GPT Pro review has not been pasted yet."
  }
  return ($lines -join "`r`n")
}

function New-CompleteGptResult {
  $lines = @()
  $lines += 'Verdict: ready_for_claude_review_after_gptpro'
  $lines += 'P0 findings: none that block source-verified triage, but this is not final approval.'
  $lines += 'P1 findings: verify a few source-facing trigger chains before Claude V63.'
  $lines += 'Thinking handbook structure judgment: 思维宝典 framework keeps material action, 触发链, method, and answer sentence visible.'
  $lines += 'Reasoning handbook structure judgment: 推理宝典 groups the same 推理形式 and 同形题型 together.'
  $lines += 'Must-fix-before-Claude list: must-fix items require 回源 source verification against 原题, 评分细则, 答案表, ledger, and source-lock before Claude.'
  $lines += 'Forbidden claims: do not claim final pass, 终稿, 可发布, or 已通过.'
  for ($i = 0; $i -lt 25; $i++) {
    $lines += "Review detail ${i}: source-verified patching remains required before any student-facing change affects the final artifact."
  }
  return ($lines -join "`r`n")
}

try {
  Assert-True (Test-Path -LiteralPath $sourceIntake) 'Missing intake script.'

  New-TestRun
  New-LongPlaceholderResult | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'placeholder_host_output.txt')
  Assert-Equal $LASTEXITCODE 2 'Long placeholder result should be blocked.'
  $placeholderReport = Get-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md') -Raw -Encoding UTF8
  Assert-True ($placeholderReport -match 'BLOCKED_PLACEHOLDER_GPTPRO_RESULT') 'Placeholder report should use the dedicated V82 status.'
  Assert-True ($placeholderReport -match 'placeholder|TODO|template') 'Placeholder report should name placeholder signals.'

  New-TestRun
  New-CompleteGptResult | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'complete_host_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Complete non-placeholder result should pass intake.'
  $readyReport = Get-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md') -Raw -Encoding UTF8
  Assert-True ($readyReport -match 'READY_FOR_GPTPRO_TRIAGE') 'Complete result should be ready for GPT Pro triage.'

  'PASS'
} finally {
  if ($env:KEEP_GPTPRO_INTAKE_V82_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
