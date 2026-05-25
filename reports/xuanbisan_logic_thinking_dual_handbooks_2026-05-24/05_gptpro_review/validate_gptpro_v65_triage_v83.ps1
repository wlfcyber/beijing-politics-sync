param(
  [string]$ProjectRoot = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$triageRel = '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md'
$reportRel = '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md'
$triagePath = Join-Path $ProjectRoot $triageRel
$reportPath = Join-Path $ProjectRoot $reportRel
$checkedAt = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss zzz')

function Write-TriageReport {
  param(
    [string]$Status,
    [string[]]$Findings,
    [string[]]$NextActions
  )

  $lines = @()
  $lines += '# GPT Pro V65 Triage Ready Check V83'
  $lines += ''
  $lines += "Status: ``$Status``"
  $lines += ''
  $lines += "- Checked at: $checkedAt"
  $lines += "- Filled triage: ``$triageRel``"
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
  $lines += '- This check does not count as GPT Pro review, Claude review, source patching, Governor final pass, Confucius final pass, or Word/PDF QA.'
  $lines += '- It only controls whether the filled GPT Pro triage is structured enough to allow the next gate.'
  $lines += ''
  Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
}

if (-not (Test-Path -LiteralPath $triagePath -PathType Leaf)) {
  Write-TriageReport `
    -Status 'BLOCKED_MISSING_GPTPRO_TRIAGE' `
    -Findings @('Filled GPT Pro triage file does not exist.') `
    -NextActions @('Fill 05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md from the real GPT Pro result.', 'Do not run Claude V63 yet.')
  exit 3
}

$item = Get-Item -LiteralPath $triagePath
if ($item.Length -eq 0) {
  Write-TriageReport `
    -Status 'BLOCKED_EMPTY_GPTPRO_TRIAGE' `
    -Findings @('Filled GPT Pro triage file exists but is empty.') `
    -NextActions @('Replace it with a source-routed GPT Pro triage table.', 'Do not run Claude V63 yet.')
  exit 3
}

$text = Get-Content -LiteralPath $triagePath -Raw -Encoding UTF8
$normalized = $text -replace "`r`n", "`n"
$checks = @(
  @{ Name = 'verdict'; Pattern = '(?is)\bVerdict\b' },
  @{ Name = 'P0 section'; Pattern = '(?is)\bP0\b' },
  @{ Name = 'P1 section'; Pattern = '(?is)\bP1\b' },
  @{ Name = 'triage finding id'; Pattern = '(?is)GPTV65-[0-9]{3}|GPTPRO.*[0-9]{3}' },
  @{ Name = 'traceability route'; Pattern = '(?is)STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79\.csv|traceability matrix|section\s+[0-9]+|Q[0-9]{4}' },
  @{ Name = 'local source evidence'; Pattern = '(?is)QUESTION_COVERAGE_MATRIX\.csv|MAIN_THINKING_LEDGER\.csv|REASONING_FORM_LEDGER\.csv|CHOICE_TRAP_LEDGER\.csv|source-lock|source verification|local evidence' },
  @{ Name = 'source verdict'; Pattern = '(?is)source_verified|rejected|unverifiable|blocked|Codex source verdict|source verdict' },
  @{ Name = 'patch or blocker status'; Pattern = '(?is)ready_for_claude|patched|blocked|pending|patch target|status' },
  @{ Name = 'Claude gate statement'; Pattern = '(?is)Claude V63|before Claude|RunClaude|Claude.*gate' },
  @{ Name = 'forbidden final claims'; Pattern = '(?is)final pass|Word|PDF|Governor final|Confucius final' }
)

$findings = @()
$missing = @()
foreach ($check in $checks) {
  if ($normalized -match $check.Pattern) {
    $findings += "Found required triage signal: $($check.Name)."
  } else {
    $missing += $check.Name
  }
}

if ($normalized.Length -lt 600) {
  $missing += 'triage body length >= 600 characters'
}

if ($missing.Count -gt 0) {
  $allFindings = @()
  $allFindings += $findings
  foreach ($m in $missing) {
    $allFindings += "Missing or too weak: $m."
  }
  Write-TriageReport `
    -Status 'BLOCKED_INCOMPLETE_GPTPRO_TRIAGE' `
    -Findings $allFindings `
    -NextActions @('Expand GPTPRO_V65_TRIAGE_FILLED.md with P0/P1/P2 findings, traceability routes, local evidence, source verdicts, patch/blocker status, and Claude-before-final gate notes.', 'Do not run Claude V63 yet.')
  exit 3
}

$blockingP0Patterns = @(
  '(?is)\|\s*GPTV65-[0-9]{3}\s*\|\s*P0\s*\|[^\n]*\|\s*(blocked|pending|unverifiable)\s*\|[^\n]*\|\s*(pending|blocked)',
  '(?is)source verdict:\s*(blocked|pending|unverifiable)[^.\n]*(P0|source patches are not complete)',
  '(?is)Claude V63 remains blocked before Claude because P0',
  '(?is)P0[^#\n]*(source patches|source patching)[^#\n]*(pending|blocked)'
)
$blockingP0Found = $false
foreach ($pattern in $blockingP0Patterns) {
  if ($normalized -match $pattern) {
    $blockingP0Found = $true
    break
  }
}

if ($blockingP0Found) {
  Write-TriageReport `
    -Status 'BLOCKED_GPTPRO_P0_SOURCE_PATCHES_PENDING' `
    -Findings ($findings + @('Found GPT Pro triage rows or summary text indicating P0 source verification/patches are still blocked or pending.')) `
    -NextActions @('Resolve or explicitly source-verify every GPT Pro P0 before Claude V63.', 'Update GPTPRO_V65_TRIAGE_FILLED.md so P0 rows are patched, rejected with local evidence, or otherwise closed before rerunning this validator.', 'Do not run Claude V63 yet.')
  exit 3
}

Write-TriageReport `
  -Status 'READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE' `
  -Findings $findings `
  -NextActions @('Run resume_after_gptpro_v65.ps1 again; use -RunClaude only when ready to invoke Claude V63.', 'Do not claim final acceptance until Claude triage, source patches, Governor, Confucius, and Word/PDF QA are complete.')

exit 0
