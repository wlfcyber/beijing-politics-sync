$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$reviewDir = $PSScriptRoot
$sourceValidator = Join-Path $reviewDir 'validate_claude_v63_triage_v84.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_claude_triage_v84_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_claude_triage_v84_test_*') {
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
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '06_claude_review') | Out-Null
  Copy-Item -LiteralPath $sourceValidator -Destination (Join-Path $tempRoot '06_claude_review\validate_claude_v63_triage_v84.ps1') -Force
}

function New-WeakTriage {
  return 'Claude triage filled. Source verified. Ready for final.'
}

function New-StrongTriage {
  $lines = @()
  $lines += '# Claude V63 Triage Filled'
  $lines += ''
  $lines += 'Verdict: not_final_source_patching_required_before_governor'
  $lines += ''
  $lines += '## P0 Findings'
  $lines += ''
  $lines += '| id | severity | Claude finding | Relation to GPT Pro V65 | affected artifact | traceability route | local evidence to inspect | Codex source verdict | patch target | status |'
  $lines += '|---|---|---|---|---|---|---|---|---|---|'
  $lines += '| CLV63-001 | P0 | no final pass before source patch ledger | agrees with GPTV65-001 | 思维宝典_框架重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 12 Q0005 | QUESTION_COVERAGE_MATRIX.csv; MAIN_THINKING_LEDGER.csv; source-lock note | source_verified | 04_fusion/POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md | blocked_until_patch_logged |'
  $lines += ''
  $lines += '## P1 Findings'
  $lines += ''
  $lines += '| CLV63-002 | P1 | reasoning same-form wording needs local check | conflicts with GPTV65-002 on severity only | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 23 Q0010 | REASONING_FORM_LEDGER.csv; STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv | source_verified | 08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md | patch_required |'
  $lines += ''
  $lines += '## Reconciliation With GPT Pro'
  $lines += ''
  $lines += '- Relation to GPT Pro V65: CLV63-001 agrees with GPTV65-001; CLV63-002 conflicts on priority but not on source evidence.'
  $lines += '- Conflicts are resolved by local evidence, not by model preference.'
  $lines += '- Local evidence checked: QUESTION_COVERAGE_MATRIX.csv, MAIN_THINKING_LEDGER.csv, REASONING_FORM_LEDGER.csv, CHOICE_TRAP_LEDGER.csv, source-lock notes.'
  $lines += '- source verdict: source_verified for P0/P1 rows; no unverifiable item is patched.'
  $lines += ''
  $lines += '## Final Gate'
  $lines += ''
  $lines += '- Final Governor, Confucius, Word, and PDF remain blocked until source-verified patches are applied or logged as blocked.'
  $lines += '- No final pass, complete, publish-ready, Word, or PDF claim is allowed from this triage alone.'
  return ($lines -join "`r`n")
}

function New-ClosedTriage {
  $lines = @()
  $lines += '# Claude V63 Triage Filled'
  $lines += ''
  $lines += 'Verdict: not_final_source_patches_applied_before_governor'
  $lines += ''
  $lines += '## P0 Findings'
  $lines += ''
  $lines += '| id | severity | Claude finding | Relation to GPT Pro V65 | affected artifact | traceability route | local evidence to inspect | Codex source verdict | patch target | status |'
  $lines += '|---|---|---|---|---|---|---|---|---|---|'
  $lines += '| CLV63-001 | P0 | no final pass before source patch ledger | agrees with GPTV65-001 | 思维宝典_框架重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 12 Q0005 | QUESTION_COVERAGE_MATRIX.csv; MAIN_THINKING_LEDGER.csv; source-lock note | source_verified | 04_fusion/POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md | patched |'
  $lines += ''
  $lines += '## P1 Findings'
  $lines += ''
  $lines += '| id | severity | Claude finding | Relation to GPT Pro V65 | affected artifact | traceability route | local evidence to inspect | Codex source verdict | patch target | status |'
  $lines += '|---|---|---|---|---|---|---|---|---|---|'
  $lines += '| CLV63-002 | P1 | reasoning same-form wording needs local check | conflicts with GPTV65-002 on severity only | 推理宝典_题型重排送审版.md | STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv section 23 Q0010 | REASONING_FORM_LEDGER.csv; STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv | source_verified | 08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md | patched |'
  $lines += ''
  $lines += '## Reconciliation With GPT Pro'
  $lines += ''
  $lines += '- Relation to GPT Pro V65: CLV63-001 agrees with GPTV65-001; CLV63-002 conflicts on priority but not on source evidence.'
  $lines += '- Conflicts are resolved by local evidence, not by model preference.'
  $lines += '- Local evidence checked: QUESTION_COVERAGE_MATRIX.csv, MAIN_THINKING_LEDGER.csv, REASONING_FORM_LEDGER.csv, CHOICE_TRAP_LEDGER.csv, source-lock notes.'
  $lines += '- source verdict: source_verified for P0/P1 rows; no unverifiable item is patched.'
  $lines += ''
  $lines += '## Final Gate'
  $lines += ''
  $lines += '- Final Governor, Confucius, Word, and PDF may begin only as local gates; this triage still does not prove final acceptance.'
  $lines += '- No final pass, complete, publish-ready, Word, or PDF claim is allowed from this triage alone.'
  return ($lines -join "`r`n")
}

try {
  Assert-True (Test-Path -LiteralPath $sourceValidator) 'Missing V84 Claude triage validator script.'

  New-TestRun
  New-WeakTriage | Set-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '06_claude_review\validate_claude_v63_triage_v84.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'weak_validator_output.txt')
  Assert-Equal $LASTEXITCODE 3 'Weak Claude triage should be blocked.'
  $weakReport = Get-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md') -Raw -Encoding UTF8
  Assert-True ($weakReport -match 'BLOCKED_INCOMPLETE_CLAUDE_TRIAGE') 'Weak Claude triage should report incomplete.'

  New-TestRun
  New-StrongTriage | Set-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '06_claude_review\validate_claude_v63_triage_v84.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'strong_validator_output.txt')
  Assert-Equal $LASTEXITCODE 3 'Strong but unresolved Claude triage should be blocked.'
  $strongReport = Get-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md') -Raw -Encoding UTF8
  Assert-True ($strongReport -match 'BLOCKED_CLAUDE_PATCHES_PENDING') 'Unresolved Claude triage should report patch blocker.'

  New-TestRun
  New-ClosedTriage | Set-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md') -Encoding UTF8
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '06_claude_review\validate_claude_v63_triage_v84.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'closed_validator_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Closed Claude triage should pass.'
  $strongReport = Get-Content -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md') -Raw -Encoding UTF8
  Assert-True ($strongReport -match 'READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE') 'Strong Claude triage should report ready for final local gates.'

  'PASS'
} finally {
  if ($env:KEEP_CLAUDE_TRIAGE_V84_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
