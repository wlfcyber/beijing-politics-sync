param(
  [string]$ProjectRoot = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$triageRel = '06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md'
$reportRel = '06_claude_review\CLAUDE_V63_TRIAGE_READY_CHECK_V84.md'
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
  $lines += '# Claude V63 Triage Ready Check V84'
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
  $lines += '- This check does not count as Claude review, source patching, Governor final pass, Confucius final pass, or Word/PDF QA.'
  $lines += '- It only controls whether the filled Claude triage is structured enough to allow final local gates to begin.'
  $lines += ''
  Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
}

if (-not (Test-Path -LiteralPath $triagePath -PathType Leaf)) {
  Write-TriageReport `
    -Status 'BLOCKED_MISSING_CLAUDE_TRIAGE' `
    -Findings @('Filled Claude V63 triage file does not exist.') `
    -NextActions @('Fill 06_claude_review\CLAUDE_V63_TRIAGE_FILLED.md from the real Claude V63 result.', 'Do not run final Governor, Confucius, Word, or PDF gates yet.')
  exit 3
}

$item = Get-Item -LiteralPath $triagePath
if ($item.Length -eq 0) {
  Write-TriageReport `
    -Status 'BLOCKED_EMPTY_CLAUDE_TRIAGE' `
    -Findings @('Filled Claude V63 triage file exists but is empty.') `
    -NextActions @('Replace it with a source-routed Claude triage table.', 'Do not run final Governor, Confucius, Word, or PDF gates yet.')
  exit 3
}

$text = Get-Content -LiteralPath $triagePath -Raw -Encoding UTF8
$normalized = $text -replace "`r`n", "`n"
$checks = @(
  @{ Name = 'verdict'; Pattern = '(?is)\bVerdict\b' },
  @{ Name = 'P0 section'; Pattern = '(?is)\bP0\b' },
  @{ Name = 'P1 section'; Pattern = '(?is)\bP1\b' },
  @{ Name = 'Claude finding id'; Pattern = '(?is)CLV63-[0-9]{3}|Claude.*[0-9]{3}' },
  @{ Name = 'relation to GPT Pro'; Pattern = '(?is)Relation to GPT Pro V65|GPTV65-[0-9]{3}|agrees|conflicts|new' },
  @{ Name = 'traceability route'; Pattern = '(?is)STUDENT_ARTIFACT_TRACEABILITY_MATRIX_V79\.csv|traceability matrix|section\s+[0-9]+|Q[0-9]{4}' },
  @{ Name = 'local source evidence'; Pattern = '(?is)QUESTION_COVERAGE_MATRIX\.csv|MAIN_THINKING_LEDGER\.csv|REASONING_FORM_LEDGER\.csv|CHOICE_TRAP_LEDGER\.csv|source-lock|source verification|local evidence' },
  @{ Name = 'source verdict'; Pattern = '(?is)source_verified|rejected|unverifiable|blocked|Codex source verdict|source verdict' },
  @{ Name = 'patch or blocker status'; Pattern = '(?is)patch_required|blocked_until_patch_logged|patched|blocked|pending|patch target|status' },
  @{ Name = 'final local gate statement'; Pattern = '(?is)Final Governor|Confucius|Word|PDF|final local gates' },
  @{ Name = 'forbidden final claims'; Pattern = '(?is)final pass|publish-ready|complete|Word|PDF' }
)

$findings = @()
$missing = @()
foreach ($check in $checks) {
  if ($normalized -match $check.Pattern) {
    $findings += "Found required Claude triage signal: $($check.Name)."
  } else {
    $missing += $check.Name
  }
}

if ($normalized.Length -lt 700) {
  $missing += 'triage body length >= 700 characters'
}

if ($missing.Count -gt 0) {
  $allFindings = @()
  $allFindings += $findings
  foreach ($m in $missing) {
    $allFindings += "Missing or too weak: $m."
  }
  Write-TriageReport `
    -Status 'BLOCKED_INCOMPLETE_CLAUDE_TRIAGE' `
    -Findings $allFindings `
    -NextActions @('Expand CLAUDE_V63_TRIAGE_FILLED.md with P0/P1/P2 findings, relation to GPT Pro, traceability routes, local evidence, source verdicts, patch/blocker status, and final gate notes.', 'Do not run final Governor, Confucius, Word, or PDF gates yet.')
  exit 3
}

$openBlockingRows = @()
$lineNumber = 0
foreach ($line in ($normalized -split "`n")) {
  $lineNumber += 1
  if ($line -notmatch '^\|\s*CLV63-[0-9]{3}\s*\|\s*(P0|P1)\s*\|') {
    continue
  }

  $cells = $line -split '\|'
  if ($cells.Count -lt 11) {
    $openBlockingRows += "Malformed Claude P0/P1 triage row at line $lineNumber."
    continue
  }

  $id = $cells[1].Trim()
  $severity = $cells[2].Trim()
  $sourceVerdict = $cells[$cells.Count - 4].Trim()
  $status = $cells[$cells.Count - 2].Trim()

  $sourceStillOpen = $sourceVerdict -match '(?i)^(blocked|pending|unverifiable)$'
  $statusStillOpen = $status -match '(?i)^(patch_required|blocked_until_patch_logged|blocked|pending|unverifiable)$'
  if ($sourceStillOpen -or $statusStillOpen) {
    $openBlockingRows += "$id $severity remains open: source verdict=[$sourceVerdict], status=[$status]."
  }
}

if ($openBlockingRows.Count -gt 0) {
  Write-TriageReport `
    -Status 'BLOCKED_CLAUDE_PATCHES_PENDING' `
    -Findings ($findings + $openBlockingRows) `
    -NextActions @('Patch or explicitly close every Claude V63 P0/P1 row through local evidence before final local gates.', 'Update CLAUDE_V63_TRIAGE_FILLED.md so each P0/P1 row has a closed source verdict and a closed status such as patched or rejected_with_evidence.', 'Do not run final Governor, Confucius, Word, or PDF gates yet.')
  exit 3
}

Write-TriageReport `
  -Status 'READY_FOR_FINAL_LOCAL_GATES_AFTER_CLAUDE_TRIAGE' `
  -Findings $findings `
  -NextActions @('Run source-verified patch ledger checks before final Governor.', 'Do not claim final acceptance until final Governor, Confucius, and Word/PDF QA are complete.')

exit 0
