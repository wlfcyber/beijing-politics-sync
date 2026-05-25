param(
  [string]$ProjectRoot = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $ProjectRoot = Split-Path -Parent $PSScriptRoot
}
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path

$uploadDir = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_SET'
$zipPath = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_SET.zip'
$reportPath = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_UPLOAD_PACKAGE_AUDIT_V81.md'
$checkedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')

function Get-PropertyValue {
  param(
    [object]$Object,
    [string]$Name
  )
  if ($null -eq $Object) { return '' }
  $property = $Object.PSObject.Properties | Where-Object { $_.Name -eq $Name } | Select-Object -First 1
  if ($null -eq $property) { return '' }
  return [string]$property.Value
}

function Test-NonEmptyFile {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $false }
  return ((Get-Item -LiteralPath $Path).Length -gt 0)
}

function Read-TextIfExists {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return '' }
  return Get-Content -LiteralPath $Path -Raw -Encoding UTF8
}

$requiredMappings = @(
  [pscustomobject]@{ source = 'PROGRESS.md'; upload = 'PROGRESS.md' },
  [pscustomobject]@{ source = '00_control\GOVERNOR_GATES.md'; upload = '00_control__GOVERNOR_GATES.md' },
  [pscustomobject]@{ source = '01_source_inventory\COVERAGE_GAP_AUDIT_V86.md'; upload = '01_source_inventory__COVERAGE_GAP_AUDIT_V86.md' },
  [pscustomobject]@{ source = '01_source_inventory\SUITE_COVERAGE_AUDIT_V87.md'; upload = '01_source_inventory__SUITE_COVERAGE_AUDIT_V87.md' },
  [pscustomobject]@{ source = '03_claudecode_lane\blockers_2026_ermo.csv'; upload = '03_claudecode_lane__blockers_2026_ermo.csv' },
  [pscustomobject]@{ source = '05_gptpro_review\EXTERNAL_REVIEW_STATUS.md'; upload = '05_gptpro_review__EXTERNAL_REVIEW_STATUS.md' },
  [pscustomobject]@{ source = '05_gptpro_review\audit_gptpro_v65_upload_package_v81.ps1'; upload = '05_gptpro_review__audit_gptpro_v65_upload_package_v81.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\test_gptpro_v65_upload_package_audit_v81.ps1'; upload = '05_gptpro_review__test_gptpro_v65_upload_package_audit_v81.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\run_gptpro_v65_intake_check.ps1'; upload = '05_gptpro_review__run_gptpro_v65_intake_check.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\test_gptpro_v65_intake_placeholder_v82.ps1'; upload = '05_gptpro_review__test_gptpro_v65_intake_placeholder_v82.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\validate_gptpro_v65_triage_v83.ps1'; upload = '05_gptpro_review__validate_gptpro_v65_triage_v83.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\test_gptpro_v65_triage_quality_v83.ps1'; upload = '05_gptpro_review__test_gptpro_v65_triage_quality_v83.ps1' },
  [pscustomobject]@{ source = '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md'; upload = '05_gptpro_review__GPTPRO_V65_TRIAGE_READY_CHECK_V83.md' },
  [pscustomobject]@{ source = '05_gptpro_review\GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md'; upload = '05_gptpro_review__GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md' },
  [pscustomobject]@{ source = '05_gptpro_review\GPTPRO_V65_UPLOAD_MANIFEST.md'; upload = '05_gptpro_review__GPTPRO_V65_UPLOAD_MANIFEST.md' },
  [pscustomobject]@{ source = '05_gptpro_review\GPTPRO_V65_UPLOAD_SET_REFRESH_V75.md'; upload = '05_gptpro_review__GPTPRO_V65_UPLOAD_SET_REFRESH_V75.md' },
  [pscustomobject]@{ source = '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md'; upload = '05_gptpro_review__GPTPRO_V65_INTAKE_READY_CHECK.md' },
  [pscustomobject]@{ source = '06_claude_review\EXTERNAL_REVIEW_STATUS.md'; upload = '06_claude_review__EXTERNAL_REVIEW_STATUS.md' },
  [pscustomobject]@{ source = '06_claude_review\run_claude_external_review_v63.ps1'; upload = '06_claude_review__run_claude_external_review_v63.ps1' },
  [pscustomobject]@{ source = '06_claude_review\test_claude_v63_gate.ps1'; upload = '06_claude_review__test_claude_v63_gate.ps1' },
  [pscustomobject]@{ source = '06_claude_review\validate_claude_v63_triage_v84.ps1'; upload = '06_claude_review__validate_claude_v63_triage_v84.ps1' },
  [pscustomobject]@{ source = '06_claude_review\test_claude_v63_triage_quality_v84.ps1'; upload = '06_claude_review__test_claude_v63_triage_quality_v84.ps1' },
  [pscustomobject]@{ source = '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md'; upload = '06_claude_review__CLAUDE_V63_TRIAGE_READY_CHECK_V84.md' },
  [pscustomobject]@{ source = '07_governor_confucius\GOVERNOR_CHECKLIST.md'; upload = '07_governor_confucius__GOVERNOR_CHECKLIST.md' },
  [pscustomobject]@{ source = '07_governor_confucius\build_student_traceability_v79.ps1'; upload = '07_governor_confucius__build_student_traceability_v79.ps1' },
  [pscustomobject]@{ source = '07_governor_confucius\test_student_traceability_v79.ps1'; upload = '07_governor_confucius__test_student_traceability_v79.ps1' },
  [pscustomobject]@{ source = '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv'; upload = '07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv' },
  [pscustomobject]@{ source = '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md'; upload = '07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md' },
  [pscustomobject]@{ source = '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv'; upload = '07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv' },
  [pscustomobject]@{ source = '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md'; upload = '07_governor_confucius__STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md' },
  [pscustomobject]@{ source = '08_delivery\DELIVERY_STATUS.md'; upload = '08_delivery__DELIVERY_STATUS.md' }
)

$failures = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]

if (-not (Test-Path -LiteralPath $uploadDir -PathType Container)) {
  $failures.Add("Missing upload set directory: 05_gptpro_review\GPTPRO_V65_UPLOAD_SET") | Out-Null
}
if (-not (Test-Path -LiteralPath $zipPath -PathType Leaf)) {
  $failures.Add("Missing upload zip: 05_gptpro_review\GPTPRO_V65_UPLOAD_SET.zip") | Out-Null
}

$missingSource = New-Object System.Collections.Generic.List[string]
$missingUpload = New-Object System.Collections.Generic.List[string]
$hashMismatch = New-Object System.Collections.Generic.List[string]

foreach ($mapping in $requiredMappings) {
  $sourcePath = Join-Path $ProjectRoot $mapping.source
  $uploadPath = Join-Path $uploadDir $mapping.upload
  if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
    $missingSource.Add($mapping.source) | Out-Null
    continue
  }
  if (-not (Test-Path -LiteralPath $uploadPath -PathType Leaf)) {
    $missingUpload.Add($mapping.upload) | Out-Null
    continue
  }
  $sourceHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
  $uploadHash = (Get-FileHash -LiteralPath $uploadPath -Algorithm SHA256).Hash
  if ($sourceHash -ne $uploadHash) {
    $hashMismatch.Add($mapping.upload) | Out-Null
  }
}

if ($missingSource.Count -gt 0) {
  $failures.Add("Missing source files: $($missingSource.ToArray() -join '; ')") | Out-Null
}
if ($missingUpload.Count -gt 0) {
  $failures.Add("Missing upload-set files: $($missingUpload.ToArray() -join '; ')") | Out-Null
}
if ($hashMismatch.Count -gt 0) {
  $failures.Add("Upload-set hash mismatches: $($hashMismatch.ToArray() -join '; ')") | Out-Null
}

$zipMissing = New-Object System.Collections.Generic.List[string]
$zipEntryCheck = 'SKIPPED'
if (Test-Path -LiteralPath $zipPath -PathType Leaf) {
  Add-Type -AssemblyName System.IO.Compression.FileSystem
  $zip = [IO.Compression.ZipFile]::OpenRead($zipPath)
  try {
    $zipEntries = @($zip.Entries | Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) } | Select-Object -ExpandProperty FullName)
  } finally {
    $zip.Dispose()
  }
  foreach ($mapping in $requiredMappings) {
    if ($zipEntries -notcontains $mapping.upload) {
      $zipMissing.Add($mapping.upload) | Out-Null
    }
  }
  if ($zipMissing.Count -eq 0) {
    $zipEntryCheck = 'PASS'
  } else {
    $zipEntryCheck = 'FAIL'
    $failures.Add("Missing zip entries: $($zipMissing.ToArray() -join '; ')") | Out-Null
  }
}

$traceMatrixPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv'
$traceSummaryPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md'
$traceRows = @()
if (Test-Path -LiteralPath $traceMatrixPath -PathType Leaf) {
  $traceRows = @(Import-Csv -LiteralPath $traceMatrixPath)
}
$traceTotal = $traceRows.Count
$traceMatched = @($traceRows | Where-Object { (Get-PropertyValue $_ 'coverage_status') -eq 'matched' }).Count
$traceUnmatched = @($traceRows | Where-Object { (Get-PropertyValue $_ 'coverage_status') -eq 'unmatched' }).Count
$traceUnparsed = @($traceRows | Where-Object { (Get-PropertyValue $_ 'coverage_status') -eq 'unparsed' }).Count
$traceAlias = @($traceRows | Where-Object { (Get-PropertyValue $_ 'parse_status') -eq 'alias' }).Count
$traceSummary = Read-TextIfExists $traceSummaryPath
$traceabilityCheck = 'FAIL'
if ($traceTotal -gt 0 -and $traceMatched -eq $traceTotal -and $traceUnmatched -eq 0 -and $traceUnparsed -eq 0 -and $traceSummary -match 'TRACEABILITY_READY_PRE_EXTERNAL') {
  $traceabilityCheck = 'PASS'
} else {
  $failures.Add("Traceability is not clean: total=$traceTotal matched=$traceMatched unmatched=$traceUnmatched unparsed=$traceUnparsed") | Out-Null
}

$aliasPath = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv'
$aliasCheck = if (Test-Path -LiteralPath $aliasPath -PathType Leaf) { 'PASS' } else { 'FAIL' }
if ($aliasCheck -eq 'FAIL') {
  $failures.Add('Missing V80 traceability alias table.') | Out-Null
}

$chromeV85Path = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85.md'
$chromeV85Text = Read-TextIfExists $chromeV85Path
$chromeV85Check = if ($chromeV85Text -match 'Status:\s*`?CHROME_CHANNEL_RECHECKED_NO_EXTERNAL_RESULT`?') { 'PASS' } else { 'FAIL' }
if ($chromeV85Check -eq 'FAIL') {
  $failures.Add('Missing or invalid V85 Chrome external-review channel recheck evidence.') | Out-Null
}

$blockerPath = Join-Path $ProjectRoot '03_claudecode_lane\blockers_2026_ermo.csv'
$blockerStatus = 'missing'
$blockerCheck = 'FAIL'
$blockerV84Check = 'FAIL'
$blockerV85Check = 'FAIL'
if (Test-Path -LiteralPath $blockerPath -PathType Leaf) {
  $blocker = @(Import-Csv -LiteralPath $blockerPath | Where-Object { (Get-PropertyValue $_ 'blocker_id') -eq 'B2026ERMO-016' } | Select-Object -First 1)
  if ($blocker.Count -gt 0) {
    $blockerStatus = Get-PropertyValue $blocker[0] 'status'
    $blockerSource = Get-PropertyValue $blocker[0] 'source_log'
    $blockerFinding = Get-PropertyValue $blocker[0] 'finding'
    $blockerRequiredAction = Get-PropertyValue $blocker[0] 'required_action'
    if ($blockerStatus -eq 'open_external_review' -and $blockerSource -match 'STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80\.csv' -and $blockerFinding -match '153 trace rows|153 matched source labels|0 unparsed') {
      $blockerCheck = 'PASS'
    }
    if (
      $blockerStatus -eq 'open_external_review' -and
      $blockerSource -match 'validate_claude_v63_triage_v84\.ps1' -and
      $blockerSource -match 'test_claude_v63_triage_quality_v84\.ps1' -and
      $blockerSource -match 'CLAUDE_V63_TRIAGE_READY_CHECK_V84\.md' -and
      $blockerFinding -match 'V84 adds a Claude V63 triage quality gate' -and
      $blockerRequiredAction -match 'READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE'
    ) {
      $blockerV84Check = 'PASS'
    }
    if (
      $blockerStatus -eq 'open_external_review' -and
      $blockerSource -match 'GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85\.md' -and
      $blockerFinding -match 'V85 rechecked the Chrome extension channel' -and
      $blockerRequiredAction -match 'GPTPRO_V65_CHROME_EXTENSION_RECHECK_V85\.md'
    ) {
      $blockerV85Check = 'PASS'
    }
  }
}
if ($blockerCheck -eq 'FAIL') {
  $failures.Add("B2026ERMO-016 is not aligned with the V80 external-review gate.") | Out-Null
}
if ($blockerV84Check -eq 'FAIL') {
  $failures.Add("B2026ERMO-016 is not aligned with the V84 Claude triage gate.") | Out-Null
}
if ($blockerV85Check -eq 'FAIL') {
  $failures.Add("B2026ERMO-016 is not aligned with the V85 Chrome channel recheck.") | Out-Null
}

$coverageV86Path = Join-Path $ProjectRoot '01_source_inventory\COVERAGE_GAP_AUDIT_V86.md'
$coverageV86Text = Read-TextIfExists $coverageV86Path
$coverageV86Check = if (
  $coverageV86Text -match 'Status:\s*`?LOCAL_COVERAGE_AUDIT_COMPLETE_EXTERNAL_REVIEW_PENDING`?' -and
  $coverageV86Text -match 'Coverage gap rows:\s*`26`' -and
  $coverageV86Text -match 'Question coverage rows:\s*`140`' -and
  $coverageV86Text -match 'GAP007' -and
  $coverageV86Text -match 'B2026ERMO-016'
) { 'PASS' } else { 'FAIL' }
if ($coverageV86Check -eq 'FAIL') {
  $failures.Add('Missing or invalid V86 coverage-gap audit.') | Out-Null
}

$suiteV87Path = Join-Path $ProjectRoot '01_source_inventory\SUITE_COVERAGE_AUDIT_V87.md'
$suiteV87Text = Read-TextIfExists $suiteV87Path
$suiteV87Check = if (
  $suiteV87Text -match 'Status:\s*`?SUITE_COVERAGE_AUDIT_UPDATED_EXTERNAL_REVIEW_PENDING`?' -and
  $suiteV87Text -match 'Added coverage rows:\s*`3`' -and
  $suiteV87Text -match 'Question coverage rows after V87:\s*`143`' -and
  $suiteV87Text -match 'Q0141' -and
  $suiteV87Text -match 'Q0142' -and
  $suiteV87Text -match 'Q0143' -and
  $suiteV87Text -match 'B2026ERMO-016'
) { 'PASS' } else { 'FAIL' }
if ($suiteV87Check -eq 'FAIL') {
  $failures.Add('Missing or invalid V87 suite-coverage audit.') | Out-Null
}

$traceDeltaV88Path = Join-Path $ProjectRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md'
$traceDeltaV88Text = Read-TextIfExists $traceDeltaV88Path
$traceDeltaV88Check = if (
  $traceDeltaV88Text -match 'Status:\s*`?TRACEABILITY_REFRESHED_PRE_EXTERNAL`?' -and
  $traceDeltaV88Text -match 'Q0141-Q0143' -and
  $traceDeltaV88Text -match 'reasoning handbook body' -and
  $traceDeltaV88Text -match 'total `153`' -and
  $traceDeltaV88Text -match 'matched `153`' -and
  $traceDeltaV88Text -match 'unparsed `0`' -and
  $traceDeltaV88Text -match 'does not count as GPT Pro review, Claude review'
) { 'PASS' } else { 'FAIL' }
if ($traceDeltaV88Check -eq 'FAIL') {
  $failures.Add('Missing or invalid V88 student traceability delta.') | Out-Null
}

$gptResultPath = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md'
$claudeResultPath = Join-Path $ProjectRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'
$intakePath = Join-Path $ProjectRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md'
$intakeText = Read-TextIfExists $intakePath

$externalResultGate = 'UNKNOWN'
if (Test-NonEmptyFile $gptResultPath) {
  $externalResultGate = 'GPTPRO_RESULT_PRESENT'
} elseif ($intakeText -match 'BLOCKED_MISSING_GPTPRO_RESULT') {
  $externalResultGate = 'BLOCKED_MISSING_GPTPRO_RESULT'
} else {
  $externalResultGate = 'MISSING_GPTPRO_RESULT_WITHOUT_CURRENT_INTAKE_BLOCK'
  $failures.Add('GPT Pro result is missing and intake file does not report BLOCKED_MISSING_GPTPRO_RESULT.') | Out-Null
}
$claudeResultGate = if (Test-NonEmptyFile $claudeResultPath) { 'CLAUDE_RESULT_PRESENT' } else { 'MISSING_CLAUDE_RESULT' }

$sourceFileCheck = if ($missingSource.Count -eq 0) { 'PASS' } else { 'FAIL' }
$uploadFileCheck = if ($missingUpload.Count -eq 0) { 'PASS' } else { 'FAIL' }
$hashSyncCheck = if ($hashMismatch.Count -eq 0 -and $missingSource.Count -eq 0 -and $missingUpload.Count -eq 0) { 'PASS' } else { 'FAIL' }
$auditToolCheck = if (
  $sourceFileCheck -eq 'PASS' -and
  $uploadFileCheck -eq 'PASS' -and
  $hashSyncCheck -eq 'PASS' -and
  (Test-Path -LiteralPath (Join-Path $uploadDir '05_gptpro_review__audit_gptpro_v65_upload_package_v81.ps1') -PathType Leaf) -and
  (Test-Path -LiteralPath (Join-Path $uploadDir '05_gptpro_review__test_gptpro_v65_upload_package_audit_v81.ps1') -PathType Leaf)
) { 'PASS' } else { 'FAIL' }
$uploadSetFiles = if (Test-Path -LiteralPath $uploadDir -PathType Container) { @(Get-ChildItem -LiteralPath $uploadDir -File).Count } else { 0 }
$zipBytes = if (Test-Path -LiteralPath $zipPath -PathType Leaf) { (Get-Item -LiteralPath $zipPath).Length } else { 0 }

if ($failures.Count -eq 0 -and $externalResultGate -eq 'BLOCKED_MISSING_GPTPRO_RESULT') {
  $status = 'UPLOAD_PACKAGE_READY_EXTERNAL_REVIEW_PENDING'
} elseif ($failures.Count -eq 0) {
  $status = 'UPLOAD_PACKAGE_SYNCED'
} else {
  $status = 'UPLOAD_PACKAGE_AUDIT_FAILED'
}

$report = @()
$report += '# GPT Pro V65 Upload Package Audit V81'
$report += ''
$report += "Status: ``$status``"
$report += ''
$report += "- Checked at: $checkedAt"
$report += "- Upload folder: ``05_gptpro_review\GPTPRO_V65_UPLOAD_SET``"
$report += "- Upload zip: ``05_gptpro_review\GPTPRO_V65_UPLOAD_SET.zip``"
$report += "- Upload-set file count: ``$uploadSetFiles``"
$report += "- Zip size bytes: ``$zipBytes``"
$report += ''
$report += '## Gate Checks'
$report += ''
$report += "- source_file_check: ``$sourceFileCheck``"
$report += "- upload_file_check: ``$uploadFileCheck``"
$report += "- hash_sync_check: ``$hashSyncCheck``"
$report += "- audit_tool_check: ``$auditToolCheck``"
$report += "- zip_entry_check: ``$zipEntryCheck``"
$report += "- traceability_check: ``$traceabilityCheck``"
$report += "- alias_table_check: ``$aliasCheck``"
$report += "- chrome_v85_recheck_check: ``$chromeV85Check``"
$report += "- coverage_v86_audit_check: ``$coverageV86Check``"
$report += "- suite_v87_audit_check: ``$suiteV87Check``"
$report += "- traceability_v88_delta_check: ``$traceDeltaV88Check``"
$report += "- blocker_status: ``$blockerStatus``"
$report += "- blocker_check: ``$blockerCheck``"
$report += "- blocker_v84_gate_check: ``$blockerV84Check``"
$report += "- blocker_v85_channel_check: ``$blockerV85Check``"
$report += "- external_result_gate: ``$externalResultGate``"
$report += "- claude_result_gate: ``$claudeResultGate``"
$report += ''
$report += '## Traceability Snapshot'
$report += ''
$report += "- total_trace_rows: ``$traceTotal``"
$report += "- matched_source_labels: ``$traceMatched``"
$report += "- unmatched_source_labels: ``$traceUnmatched``"
$report += "- unparsed_source_labels: ``$traceUnparsed``"
$report += "- alias_expanded_rows: ``$traceAlias``"
$report += ''
$report += '## Guardrail'
$report += ''
$report += '- This audit only proves that the local GPT Pro upload package is synchronized and ready to submit.'
$report += '- It does not count as GPT Pro review, Claude review, Governor final pass, Confucius final pass, or Word/PDF QA.'
$report += ''

if ($failures.Count -gt 0) {
  $report += '## Failures'
  $report += ''
  foreach ($failure in $failures) {
    $report += "- $failure"
  }
  $report += ''
}

if ($warnings.Count -gt 0) {
  $report += '## Warnings'
  $report += ''
  foreach ($warning in $warnings) {
    $report += "- $warning"
  }
  $report += ''
}

Set-Content -LiteralPath $reportPath -Value $report -Encoding UTF8

if ($failures.Count -gt 0) {
  exit 2
}
exit 0
