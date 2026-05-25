$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$auditDir = $PSScriptRoot
$sourceAudit = Join-Path $auditDir 'audit_gptpro_v65_upload_package_v81.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_gptpro_upload_audit_v81_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_gptpro_upload_audit_v81_test_*') {
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

function Set-FixtureFile {
  param([string]$RelativePath, [string[]]$Lines)
  $path = Join-Path $tempRoot $RelativePath
  $parent = Split-Path -Parent $path
  New-Item -ItemType Directory -Force -Path $parent | Out-Null
  Set-Content -LiteralPath $path -Value $Lines -Encoding UTF8
}

function Copy-ToUploadSet {
  param([string]$SourceRelativePath, [string]$UploadName)
  Copy-Item -LiteralPath (Join-Path $tempRoot $SourceRelativePath) -Destination (Join-Path $tempRoot "05_gptpro_review\GPTPRO_V65_UPLOAD_SET\$UploadName") -Force
}

function New-TestRun {
  Remove-SafeTempRoot $tempRoot
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_SET') | Out-Null
  Copy-Item -LiteralPath $sourceAudit -Destination (Join-Path $tempRoot '05_gptpro_review\audit_gptpro_v65_upload_package_v81.ps1') -Force

  Set-FixtureFile 'PROGRESS.md' @('V80 traceability alias closure present.')
  Set-FixtureFile '00_control\GOVERNOR_GATES.md' @('V80 Traceability Alias Gate Update')
  Set-FixtureFile '01_source_inventory\COVERAGE_GAP_AUDIT_V86.md' @(
    'Status: `LOCAL_COVERAGE_AUDIT_COMPLETE_EXTERNAL_REVIEW_PENDING`',
    '- Coverage gap rows: `26`',
    '- Question coverage rows: `140`',
    '- `GAP007` remains source identified but original question not locked.',
    '- `B2026ERMO-016` remains open external review.'
  )
  Set-FixtureFile '01_source_inventory\SUITE_COVERAGE_AUDIT_V87.md' @(
    'Status: `SUITE_COVERAGE_AUDIT_UPDATED_EXTERNAL_REVIEW_PENDING`',
    '- Added coverage rows: `3`',
    '- Question coverage rows after V87: `143`',
    '- Added rows: `Q0141`, `Q0142`, `Q0143`',
    '- Remaining external hard gate: `B2026ERMO-016`.'
  )
  Set-FixtureFile '03_claudecode_lane\blockers_2026_ermo.csv' @(
    '"blocker_id","scope","question_id","severity","source_log","finding","required_action","status"',
    '"B2026ERMO-016","external_review_gate","GPTPRO_V65/CLAUDE_V63","P0","07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv;06_claude_review/validate_claude_v63_triage_v84.ps1;06_claude_review/test_claude_v63_triage_quality_v84.ps1;06_claude_review/CLAUDE_V63_TRIAGE_READY_CHECK_V84.md;05_gptpro_review/GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md","V88 refreshes traceability: 153 trace rows, 153 matched source labels, 0 unmatched labels, 0 unparsed labels. V84 adds a Claude V63 triage quality gate. V85 rechecked the Chrome extension channel.","Use STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv with the matrix. Require READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE before final gates. Use GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md as latest channel evidence.","open_external_review"'
  )
  Set-FixtureFile '05_gptpro_review\EXTERNAL_REVIEW_STATUS.md' @('V80 Traceability Alias Closure Note')
  Set-FixtureFile '05_gptpro_review\test_gptpro_v65_upload_package_audit_v81.ps1' @("'PASS'")
  Set-FixtureFile '05_gptpro_review\run_gptpro_v65_intake_check.ps1' @('# fixture V82 intake runner')
  Set-FixtureFile '05_gptpro_review\test_gptpro_v65_intake_placeholder_v82.ps1' @("'PASS'")
  Set-FixtureFile '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1' @('# fixture V83 triage validator')
  Set-FixtureFile '05_gptpro_review\test_gptpro_v65_triage_quality_v83.ps1' @("'PASS'")
  Set-FixtureFile '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md' @('Status: `BLOCKED_MISSING_GPTPRO_TRIAGE`')
  Set-FixtureFile '05_gptpro_review\GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md' @('Status: `CHROME_CHANNEL_RECHECKED_NO_EXTERNAL_RESULT`')
  Set-FixtureFile '05_gptpro_review\GPTPRO_V65_UPLOAD_MANIFEST.md' @('V80 traceability context')
  Set-FixtureFile '05_gptpro_review\GPTPRO_V65_UPLOAD_SET_REFRESH_V75.md' @('V80 Traceability Alias Closure Added')
  Set-FixtureFile '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md' @('Status: `BLOCKED_MISSING_GPTPRO_RESULT`')
  Set-FixtureFile '06_claude_review\EXTERNAL_REVIEW_STATUS.md' @('Claude V63 remains blocked by GPT-first order.')
  Set-FixtureFile '06_claude_review\run_claude_external_review_v63.ps1' @('# fixture Claude V63 runner')
  Set-FixtureFile '06_claude_review\test_claude_v63_gate.ps1' @("'PASS'")
  Set-FixtureFile '06_claude_review\validate_claude_v63_triage_v84.ps1' @('# fixture Claude V84 validator')
  Set-FixtureFile '06_claude_review\test_claude_v63_triage_quality_v84.ps1' @("'PASS'")
  Set-FixtureFile '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md' @('Status: `BLOCKED_MISSING_CLAUDE_TRIAGE`')
  Set-FixtureFile '07_governor_confucius\GOVERNOR_CHECKLIST.md' @('V80 traceability alias closure')
  Set-FixtureFile '07_governor_confucius\build_student_traceability_v79.ps1' @('# fixture builder')
  Set-FixtureFile '07_governor_confucius\test_student_traceability_v79.ps1' @("'PASS'")
  Set-FixtureFile '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md' @(
    'Status: `TRACEABILITY_READY_PRE_EXTERNAL`',
    '- Total trace rows: `153`',
    '- Matched source labels: `153`',
    '- Unmatched source labels: `0`',
    '- Unparsed source labels: `0`'
  )
  Set-FixtureFile '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv' @(
    '"alias_label","target_suite","target_question_no","note"',
    '"AliasA","SuiteA","1","fixture"',
    '"AliasB","SuiteB","2","fixture"'
  )
  Set-FixtureFile '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv' @(
    '"artifact","source_label","parse_status","coverage_status","question_id"',
    '"thinking_framework","direct1","parsed","matched","Q0001"',
    '"reasoning_type","AliasA","alias","matched","Q0005"',
    '"reasoning_type","AliasB","alias","matched","Q0010"'
  )
  Set-FixtureFile '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md' @(
    'Status: `TRACEABILITY_REFRESHED_PRE_EXTERNAL`',
    '- V87 added local source-locked rows `Q0141-Q0143`.',
    '- V88 moves those rows into the reasoning handbook body rather than leaving them only in audit ledgers.',
    '- Refreshed traceability counts: total `153`, thinking `73`, reasoning `80`, matched `153`, unmatched `0`, unparsed `0`, unique matched question ids `138`.',
    '- This delta does not count as GPT Pro review, Claude review, final Governor pass, final Confucius pass, Word QA, or PDF QA.'
  )
  Set-FixtureFile '08_delivery\DELIVERY_STATUS.md' @('Current delivery remains pre-external review.')

  $pairs = @(
    @('PROGRESS.md','PROGRESS.md'),
    @('00_control\GOVERNOR_GATES.md','00_control__GOVERNOR_GATES.md'),
    @('01_source_inventory\COVERAGE_GAP_AUDIT_V86.md','01_source_inventory__COVERAGE_GAP_AUDIT_V86.md'),
    @('01_source_inventory\SUITE_COVERAGE_AUDIT_V87.md','01_source_inventory__SUITE_COVERAGE_AUDIT_V87.md'),
    @('03_claudecode_lane\blockers_2026_ermo.csv','03_claudecode_lane__blockers_2026_ermo.csv'),
    @('05_gptpro_review\EXTERNAL_REVIEW_STATUS.md','05_gptpro_review__EXTERNAL_REVIEW_STATUS.md'),
    @('05_gptpro_review\audit_gptpro_v65_upload_package_v81.ps1','05_gptpro_review__audit_gptpro_v65_upload_package_v81.ps1'),
    @('05_gptpro_review\test_gptpro_v65_upload_package_audit_v81.ps1','05_gptpro_review__test_gptpro_v65_upload_package_audit_v81.ps1'),
    @('05_gptpro_review\run_gptpro_v65_intake_check.ps1','05_gptpro_review__run_gptpro_v65_intake_check.ps1'),
    @('05_gptpro_review\test_gptpro_v65_intake_placeholder_v82.ps1','05_gptpro_review__test_gptpro_v65_intake_placeholder_v82.ps1'),
    @('05_gptpro_review\validate_gptpro_v65_triage_v83.ps1','05_gptpro_review__validate_gptpro_v65_triage_v83.ps1'),
    @('05_gptpro_review\test_gptpro_v65_triage_quality_v83.ps1','05_gptpro_review__test_gptpro_v65_triage_quality_v83.ps1'),
    @('05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md','05_gptpro_review__GPTPRO_V65_TRIAGE_READY_CHECK_V83.md'),
    @('05_gptpro_review\GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md','05_gptpro_review__GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md'),
    @('05_gptpro_review\GPTPRO_V65_UPLOAD_MANIFEST.md','05_gptpro_review__GPTPRO_V65_UPLOAD_MANIFEST.md'),
    @('05_gptpro_review\GPTPRO_V65_UPLOAD_SET_REFRESH_V75.md','05_gptpro_review__GPTPRO_V65_UPLOAD_SET_REFRESH_V75.md'),
    @('05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md','05_gptpro_review__GPTPRO_V65_INTAKE_READY_CHECK.md'),
    @('06_claude_review\EXTERNAL_REVIEW_STATUS.md','06_claude_review__EXTERNAL_REVIEW_STATUS.md'),
    @('06_claude_review\run_claude_external_review_v63.ps1','06_claude_review__run_claude_external_review_v63.ps1'),
    @('06_claude_review\test_claude_v63_gate.ps1','06_claude_review__test_claude_v63_gate.ps1'),
    @('06_claude_review\validate_claude_v63_triage_v84.ps1','06_claude_review__validate_claude_v63_triage_v84.ps1'),
    @('06_claude_review\test_claude_v63_triage_quality_v84.ps1','06_claude_review__test_claude_v63_triage_quality_v84.ps1'),
    @('06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md','06_claude_review__CLAUDE_V63_TRIAGE_READY_CHECK_V84.md'),
    @('07_governor_confucius\GOVERNOR_CHECKLIST.md','07_governor_confucius__GOVERNOR_CHECKLIST.md'),
    @('07_governor_confucius\build_student_traceability_v79.ps1','07_governor_confucius__build_student_traceability_v79.ps1'),
    @('07_governor_confucius\test_student_traceability_v79.ps1','07_governor_confucius__test_student_traceability_v79.ps1'),
    @('07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv','07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv'),
    @('07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md','07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md'),
    @('07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv','07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv'),
    @('07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md','07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md'),
    @('08_delivery\DELIVERY_STATUS.md','08_delivery__DELIVERY_STATUS.md')
  )
  foreach ($pair in $pairs) {
    Copy-ToUploadSet -SourceRelativePath $pair[0] -UploadName $pair[1]
  }
  $uploadFiles = @(Get-ChildItem -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_SET') -File)
  Compress-Archive -LiteralPath ($uploadFiles | ForEach-Object { $_.FullName }) -DestinationPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_SET.zip') -Force
}

try {
  Assert-True (Test-Path -LiteralPath $sourceAudit) 'Missing audit script: audit_gptpro_v65_upload_package_v81.ps1'
  New-TestRun
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '05_gptpro_review\audit_gptpro_v65_upload_package_v81.ps1') -ProjectRoot $tempRoot *> (Join-Path $tempRoot 'audit_host_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Upload package audit should exit 0 for a synced pre-external package.'

  $reportPath = Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_PACKAGE_AUDIT_V81.md'
  Assert-True (Test-Path -LiteralPath $reportPath) 'Audit report should be created.'
  $report = Get-Content -LiteralPath $reportPath -Raw -Encoding UTF8
  Assert-True ($report -match 'Status: `UPLOAD_PACKAGE_READY_EXTERNAL_REVIEW_PENDING`') 'Report should mark package ready while external review is pending.'
  Assert-True ($report -match 'zip_entry_check: `PASS`') 'Report should verify zip entries.'
  Assert-True ($report -match 'hash_sync_check: `PASS`') 'Report should verify upload-set hashes.'
  Assert-True ($report -match 'audit_tool_check: `PASS`') 'Report should verify the V81 audit script and test are included.'
  Assert-True ($report -match 'traceability_check: `PASS`') 'Report should verify traceability counts.'
  Assert-True ($report -match 'chrome_v85_recheck_check: `PASS`') 'Report should verify the V85 Chrome recheck evidence is included.'
  Assert-True ($report -match 'coverage_v86_audit_check: `PASS`') 'Report should verify the V86 coverage-gap audit is included.'
  Assert-True ($report -match 'suite_v87_audit_check: `PASS`') 'Report should verify the V87 suite-coverage audit is included.'
  Assert-True ($report -match 'traceability_v88_delta_check: `PASS`') 'Report should verify the V88 traceability delta is included.'
  Assert-True ($report -match 'external_result_gate: `BLOCKED_MISSING_GPTPRO_RESULT`') 'Report should preserve the GPT result blocker.'
  Assert-True ($report -match 'blocker_status: `open_external_review`') 'Report should preserve B2026ERMO-016 open status.'
  Assert-True ($report -match 'blocker_v84_gate_check: `PASS`') 'Report should verify B2026ERMO-016 includes the V84 Claude triage gate.'
  Assert-True ($report -match 'blocker_v85_channel_check: `PASS`') 'Report should verify B2026ERMO-016 includes the V85 Chrome channel evidence.'

  'PASS'
} finally {
  if ($env:KEEP_UPLOAD_AUDIT_V81_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
