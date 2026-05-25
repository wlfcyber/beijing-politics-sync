$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$auditDir = $PSScriptRoot
$sourceBuilder = Join-Path $auditDir 'build_student_traceability_v79.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_traceability_v79_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_traceability_v79_test_*') {
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
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '07_governor_confucius') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '08_delivery') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '01_source_inventory') | Out-Null
  Copy-Item -LiteralPath $sourceBuilder -Destination (Join-Path $tempRoot '07_governor_confucius\build_student_traceability_v79.ps1') -Force

  @(
    '# thinking fixture',
    '',
    '## science thinking',
    '',
    '### objectivity and verification',
    '',
    '#### original section 65 trigger chain',
    '',
    'Source: 2026HaidianErmo Q18(1)',
    '',
    '### material action',
    '',
    'fixture text'
  ) | Set-Content -LiteralPath (Join-Path $tempRoot '08_delivery\thinking_fixture.md') -Encoding UTF8

  @(
    '# reasoning fixture',
    '',
    '## sufficient-condition reasoning',
    '',
    '#### original section 1 affirming consequent error',
    '',
    'Source: 2025XichengErmo Q16(2), 2026HaidianQimo Q20(1)',
    '',
    '#### original section 2 shorthand aliases',
    '',
    'Source: AliasA, AliasB, 2026DongchengQimo Q6',
    '',
    '### reasoning form',
    '',
    'fixture text'
  ) | Set-Content -LiteralPath (Join-Path $tempRoot '08_delivery\reasoning_fixture.md') -Encoding UTF8

  @(
    '"question_id","year","district","stage","suite_name","question_no","book_part","question_type","evidence_level","source_packet","status","decision_reason"',
    '"Q0001","2026","Haidian","Ermo","2026HaidianErmo","18(1)","thinking","main_question","A-formal","packet.md#q0001","source_locked","fixture"',
    '"Q0002","2025","Xicheng","Ermo","2025XichengErmo","16(2)","reasoning","main_question","A-formal","packet.md#q0002","source_locked","fixture"',
    '"Q0003","2026","Haidian","Qimo","2026HaidianQimo","20(1)","reasoning","main_question","A-formal","packet.md#q0003","source_locked","fixture"',
    '"Q0004","2026","Dongcheng","Qimo","2026DongchengQimo","17(2)","reasoning","main_question","A-formal","packet.md#q0004","source_locked","fixture"',
    '"Q0005","2026","Fengtai","Yimo","2026FengtaiYimo","18(2)","reasoning","main_question","A-formal","packet.md#q0005","source_locked","fixture"',
    '"Q0006","2026","Dongcheng","Qimo","2026DongchengQimo","6","reasoning","main_question","A-formal","packet.md#q0006","source_locked","fixture"'
  ) | Set-Content -LiteralPath (Join-Path $tempRoot '01_source_inventory\QUESTION_COVERAGE_MATRIX.csv') -Encoding UTF8

  @(
    '"alias_label","target_suite","target_question_no","note"',
    '"AliasA","2026DongchengQimo","17(2)","fixture shorthand for a claim inside the same reasoning section"',
    '"AliasB","2026FengtaiYimo","18(2)","fixture shorthand for a subclaim inside the same reasoning section"'
  ) | Set-Content -LiteralPath (Join-Path $tempRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_ALIASES_V80.csv') -Encoding UTF8
}

try {
  Assert-True (Test-Path -LiteralPath $sourceBuilder) 'Missing builder: build_student_traceability_v79.ps1'
  New-TestRun
  $thinkingPath = Join-Path $tempRoot '08_delivery\thinking_fixture.md'
  $reasoningPath = Join-Path $tempRoot '08_delivery\reasoning_fixture.md'
  & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '07_governor_confucius\build_student_traceability_v79.ps1') -ProjectRoot $tempRoot -ThinkingArtifactPath $thinkingPath -ReasoningArtifactPath $reasoningPath *> (Join-Path $tempRoot 'traceability_host_output.txt')
  Assert-Equal $LASTEXITCODE 0 'Traceability builder should exit 0 for complete fixture.'

  $csvPath = Join-Path $tempRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79.csv'
  $summaryPath = Join-Path $tempRoot '07_governor_confucius\STUDENT_ARTIFACT_TRACEABILITY_SUMMARY_V79.md'
  Assert-True (Test-Path -LiteralPath $csvPath) 'Traceability matrix CSV should be created.'
  Assert-True (Test-Path -LiteralPath $summaryPath) 'Traceability summary should be created.'

  $rows = @(Import-Csv -LiteralPath $csvPath)
  Assert-Equal $rows.Count 6 'Fixture should produce one row per source question, including alias-expanded rows.'
  Assert-Equal @($rows | Where-Object { $_.artifact -eq 'thinking_framework' }).Count 1 'Thinking artifact should have one trace row.'
  Assert-Equal @($rows | Where-Object { $_.artifact -eq 'reasoning_type' }).Count 5 'Reasoning artifact should split direct and alias source labels into five rows.'
  Assert-Equal @($rows | Where-Object { $_.coverage_status -eq 'matched' }).Count 6 'All fixture source labels should match coverage rows.'
  Assert-True (($rows | Where-Object { $_.source_label -eq '2026HaidianErmo Q18(1)' }).question_id -eq 'Q0001') 'Thinking source should map to Q0001.'
  Assert-True (($rows | Where-Object { $_.source_label -eq '2025XichengErmo Q16(2)' }).chapter_path -match 'sufficient-condition') 'Reasoning row should retain chapter path.'
  Assert-True (($rows | Where-Object { $_.source_label -eq 'AliasA' }).question_id -eq 'Q0004') 'AliasA should map through the alias table.'
  Assert-True (($rows | Where-Object { $_.source_label -eq 'AliasB' }).question_id -eq 'Q0005') 'AliasB should map through the alias table.'

  $summary = Get-Content -LiteralPath $summaryPath -Raw -Encoding UTF8
  Assert-True ($summary -match 'Status: `TRACEABILITY_READY_PRE_EXTERNAL`') 'Summary should report ready pre-external status.'
  Assert-True ($summary -match 'Unmatched source labels: `0`') 'Summary should report zero unmatched fixture labels.'
  Assert-True ($summary -match 'Unparsed source labels: `0`') 'Summary should report zero unparsed fixture labels after alias expansion.'

  'PASS'
} finally {
  if ($env:KEEP_TRACEABILITY_V79_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
