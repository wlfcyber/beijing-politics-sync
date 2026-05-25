$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$reviewDir = $PSScriptRoot
$sourceValidator = Join-Path $reviewDir 'validate_gptpro_v65_triage_v83.ps1'
$sourceResume = Join-Path (Split-Path -Parent $reviewDir) '07_governor_confucius\resume_after_gptpro_v65.ps1'
$sourceIntake = Join-Path $reviewDir 'run_gptpro_v65_intake_check.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_gptpro_triage_v83_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_gptpro_triage_v83_test_*') {
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

function New-CompleteGptResult {
  $lines = @()
  $lines += 'Verdict: ready_for_claude_review_after_gptpro'
  $lines += 'P0 findings: none that block source-verified triage, but this is not final approval.'
  $lines += 'P1 findings: verify source-facing trigger chains before Claude V63.'
  $lines += 'Thinking handbook structure judgment: 思维宝典 framework keeps material action, 触发链, method, and answer sentence visible.'
  $lines += 'Reasoning handbook structure judgment: 推理宝典 groups the same 推理形式 and 同形题型 together.'
  $lines += 'Must-fix-before-Claude list: must-fix items require 回源 source verification against 原题, 评分细则, 答案表, ledger, and source-lock before Claude.'
  $lines += 'Forbidden claims: do not claim final pass, 终稿, 可发布, or 已通过.'
  for ($i = 0; $i -lt 25; $i++) {
    $lines += "Review detail ${i}: source-verified patching remains required before any student-facing change affects the final artifact."
  }
  return ($lines -join "`r`n")
}

function New-WeakTriage {
  return 'filled source-verified GPT Pro triage'
}

function New-BlockingP0Triage {
  $lines = @()
  $lines += '# GPT Pro V65 Triage Filled'
  $lines += ''
  $lines += 'Verdict: not_final'
  $lines += ''
  $lines += '## P0 Findings'
  $lines += ''
  $lines += '| id | severity | GPT Pro finding | affected artifact | traceability route | local evidence to inspect | Codex source verdict | patch target | status |'
  $lines += '|---|---|---|---|---|---|---|---|---|'
  $lines += '| GPTV65-001 | P0 | Q0141 source identity conflict must be resolved before Claude V63 | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 40 Q0141 | QUESTION_COVERAGE_MATRIX.csv; REASONING_FORM_LEDGER.csv; source-lock note | blocked | Q0141 source verification | pending |'
  $lines += '| GPTV65-002 | P0 | Q0143三段论大前提过宽，Claude前必须回源修补 | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 27 Q0143 | QUESTION_COVERAGE_MATRIX.csv; REASONING_FORM_LEDGER.csv; local evidence | blocked | Q0143 wording patch | pending |'
  $lines += ''
  $lines += '## P1 Findings'
  $lines += ''
  $lines += '| GPTV65-003 | P1 | Q0142条件关系表述需核对 | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 5 Q0142 | QUESTION_COVERAGE_MATRIX.csv; source verification | pending | Q0142 wording | pending |'
  $lines += ''
  $lines += '## Source Verification Summary'
  $lines += ''
  $lines += '- source verdict: blocked for P0 items; source_verified patches are not complete.'
  $lines += '- traceability matrix used: STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv.'
  $lines += '- local ledgers checked: QUESTION_COVERAGE_MATRIX.csv, MAIN_THINKING_LEDGER.csv, REASONING_FORM_LEDGER.csv, CHOICE_TRAP_LEDGER.csv.'
  $lines += ''
  $lines += '## Claude V63 Gate'
  $lines += ''
  $lines += '- Claude V63 remains blocked before Claude because P0 source patches are pending.'
  $lines += '- final pass, Word, PDF, Governor final, and Confucius final remain forbidden.'
  return ($lines -join "`r`n")
}

function New-StrongTriage {
  $lines = @()
  $lines += '# GPT Pro V65 Triage Filled'
  $lines += ''
  $lines += 'Verdict: ready_for_claude_review_after_gptpro'
  $lines += ''
  $lines += '## P0 Findings'
  $lines += ''
  $lines += '| id | severity | GPT Pro finding | affected artifact | traceability route | local evidence to inspect | Codex source verdict | patch target | status |'
  $lines += '|---|---|---|---|---|---|---|---|---|'
  $lines += '| GPTV65-001 | P0 | no blocking P0 after source check | 思维宝典_框架重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 12 Q0005 | QUESTION_COVERAGE_MATRIX.csv; MAIN_THINKING_LEDGER.csv; source-lock note | source_verified | none | ready_for_claude |'
  $lines += ''
  $lines += '## P1 Findings'
  $lines += ''
  $lines += '| GPTV65-002 | P1 | verify reasoning chapter wording before Claude | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 23 Q0010 | REASONING_FORM_LEDGER.csv; STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv | source_verified | none | ready_for_claude |'
  $lines += ''
  $lines += '## Source Verification Summary'
  $lines += ''
  $lines += '- source verdict: source_verified for all P0/P1 items.'
  $lines += '- traceability matrix used: STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv.'
  $lines += '- alias table used: STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv.'
  $lines += '- local ledgers checked: QUESTION_COVERAGE_MATRIX.csv, MAIN_THINKING_LEDGER.csv, REASONING_FORM_LEDGER.csv, CHOICE_TRAP_LEDGER.csv.'
  $lines += ''
  $lines += '## Claude V63 Gate'
  $lines += ''
  $lines += '- Claude V63 may run only after this triage is saved and all P0/P1 source-verified patches are applied or logged as blocked.'
  $lines += '- final pass, Word, PDF, Governor final, and Confucius final remain forbidden.'
  return ($lines -join "`r`n")
}

function New-TestRun {
  Remove-SafeTempRoot $tempRoot
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '05_gptpro_review') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '07_governor_confucius') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '06_claude_review') | Out-Null
  Copy-Item -LiteralPath $sourceIntake -Destination (Join-Path $tempRoot '05_gptpro_review\run_gptpro_v65_intake_check.ps1') -Force
  Copy-Item -LiteralPath $sourceResume -Destination (Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1') -Force
  if (Test-Path -LiteralPath $sourceValidator) {
    Copy-Item -LiteralPath $sourceValidator -Destination (Join-Path $tempRoot '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1') -Force
  }
  @(
    '$ErrorActionPreference = "Stop"',
    '$runDir = Split-Path -Parent $PSScriptRoot',
    'Set-Content -LiteralPath (Join-Path $PSScriptRoot "fake_claude_invoked.txt") -Value "called" -Encoding UTF8',
    'Set-Content -LiteralPath (Join-Path $PSScriptRoot "CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md") -Value "fake Claude V63 result" -Encoding UTF8',
    'exit 0'
  ) | Set-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\run_claude_external_review_v63.ps1') -Encoding UTF8
  New-CompleteGptResult | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
}

try {
  Assert-True (Test-Path -LiteralPath $sourceResume) 'Missing resume script.'
  Assert-True (Test-Path -LiteralPath $sourceIntake) 'Missing intake script.'
  Assert-True (Test-Path -LiteralPath $sourceValidator) 'Missing V83 triage validator script.'

  New-TestRun
  New-WeakTriage | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1') -ProjectRoot $tempRoot -RunClaude *> (Join-Path $tempRoot 'weak_resume_output.txt')
  Assert-Equal $LASTEXITCODE 3 'Weak triage should block before Claude.'
  $weakReport = Get-Content -LiteralPath (Join-Path $tempRoot '07_governor_confucius\POST_GPTPRO_RESUME_CHECK_V78.md') -Raw -Encoding UTF8
  Assert-True ($weakReport -match 'BLOCKED_INCOMPLETE_GPTPRO_TRIAGE') 'Weak triage should produce the V83 blocked status.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt'))) 'Weak triage must not invoke Claude.'

  New-TestRun
  New-BlockingP0Triage | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'blocking_validator_output.txt')
  Assert-Equal $LASTEXITCODE 3 'Structurally complete triage with blocking P0 pending should fail the standalone validator.'
  $blockingValidation = Get-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md') -Raw -Encoding UTF8
  Assert-True ($blockingValidation -match 'BLOCKED_GPTPRO_P0_SOURCE_PATCHES_PENDING') 'Blocking P0 triage should report the P0 source-patch blocker.'
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1') -ProjectRoot $tempRoot -RunClaude *> (Join-Path $tempRoot 'blocking_resume_output.txt')
  Assert-Equal $LASTEXITCODE 3 'Blocking P0 triage should block resume before Claude.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt'))) 'Blocking P0 triage must not invoke Claude.'

  New-TestRun
  New-StrongTriage | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'strong_validator_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Strong triage should pass the standalone validator.'
  $validation = Get-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md') -Raw -Encoding UTF8
  Assert-True ($validation -match 'READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE') 'Strong triage validator should report ready.'
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '07_governor_confucius\resume_after_gptpro_v65.ps1') -ProjectRoot $tempRoot -RunClaude *> (Join-Path $tempRoot 'strong_resume_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Strong triage should allow explicit Claude run in the fixture.'
  Assert-True (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\fake_claude_invoked.txt')) 'Strong triage should allow Claude runner invocation.'

  'PASS'
} finally {
  if ($env:KEEP_GPTPRO_TRIAGE_V83_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
