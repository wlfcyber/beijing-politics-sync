param(
    [Parameter(Mandatory = $true)]
    [int]$StartId,

    [Parameter(Mandatory = $true)]
    [int]$EndId,

    [Parameter(Mandatory = $true)]
    [string]$Slug
)

$ErrorActionPreference = 'Stop'

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom

$lane = $PSScriptRoot
$root = Split-Path -Parent $lane
$reportsDir = Split-Path -Parent $root
$projectRoot = Split-Path -Parent $reportsDir

$logDir = Join-Path $lane 'logs'
$promptDir = Join-Path $lane 'prompts'
New-Item -ItemType Directory -Force -Path $logDir, $promptDir | Out-Null

$qcmPath = Join-Path $root '01_source_inventory\QUESTION_COVERAGE_MATRIX.csv'
$rows = Import-Csv -LiteralPath $qcmPath | Where-Object {
    $id = [int]$_.question_id.Substring(1)
    $id -ge $StartId -and $id -le $EndId
}

if (-not $rows) {
    throw "No rows found for Q range $StartId-$EndId"
}

$suiteNames = $rows | Select-Object -ExpandProperty suite_name -Unique
$sourceFiles = $rows | ForEach-Object { ($_.source_packet -split '#')[0] } | Select-Object -Unique
$rowLines = $rows | ForEach-Object {
    "- $($_.question_id) | suite=$($_.suite_name) | question_no=$($_.question_no) | book_part=$($_.book_part) | type=$($_.question_type) | evidence=$($_.evidence_level) | source=$($_.source_packet)"
}
$sourceLines = $sourceFiles | ForEach-Object { "- `$_" }

$prompt = @"
# ClaudeCode B-line suite-slice rerun: $Slug

You are the independent ClaudeCode B-line reviewer for the Xuanbisan double-baodian run.

Scope:
- Only audit the question rows listed below.
- Do not audit other rows or suites.
- Do not write or modify files.
- Output Markdown to stdout only.
- Do not claim final, pass, complete, publishable, Word, or PDF readiness.

Suite names:
$($suiteNames -join ', ')

Rows:
$($rowLines -join [Environment]::NewLine)

Read these local files first:
- `00_飞哥选必三逻辑与思维硬性要求记事本.md`
- `01_source_inventory/2026_ERMO_SUITE_CLOSURE_REPORT.md`
$($sourceLines -join [Environment]::NewLine)
- `QUESTION_COVERAGE_MATRIX.csv`
- `SOURCE_PACKET_QUEUE.csv`
- `MAIN_THINKING_LEDGER.csv`
- `REASONING_FORM_LEDGER.csv`
- `CHOICE_TRAP_LEDGER.csv`
- `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md`
- `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`
- `04_fusion/PROMOTION_QUALITY_CHECK.md`

Audit requirements:
1. Verify whether A-line classification is supported by local source-lock evidence.
2. Separate thinking-trigger audit from reasoning-form audit.
3. For thinking items, judge whether the material-to-knowledge trigger chain is concrete enough for the philosophy Bixiu 4 baodian quality benchmark.
4. For reasoning items, judge whether the form grouping is correct and whether the same-form aggregation rule is followed.
5. Check current body draft placement if the question appears in either body file.
6. Mark every uncertainty as a blocker instead of smoothing it into prose.
7. Give fusion candidates only where there is enough evidence to merge into the main ledgers or body.

Output format:

## B-line suite-slice rerun: $Slug

### Per-question audit
Use one block for each listed question:
- Verdict:
- Evidence read:
- Thinking trigger:
- Reasoning form:
- Body placement:
- Trap or boundary issue:
- B-line correction:
- Fusion decision:
- Blocker:

### Slice implications
List implications for 2026 ERMO suite closure.

### Machine summary
Use this exact CSV-like table:
``question_id,verdict,body_status,fusion_decision,blocker_required``
"@

$promptPath = Join-Path $promptDir ("claudecode_2026_ermo_{0}_prompt.md" -f $Slug)
$stdoutPath = Join-Path $logDir ("claudecode_2026_ermo_{0}_stdout.log" -f $Slug)
$stderrPath = Join-Path $logDir ("claudecode_2026_ermo_{0}_stderr.log" -f $Slug)
$returnPath = Join-Path $lane ("claudecode_2026_ermo_{0}_return_code.txt" -f $Slug)

Set-Content -LiteralPath $promptPath -Value $prompt -Encoding utf8

Push-Location $root
try {
    $prompt | claude -p --model opus --effort max --permission-mode bypassPermissions --output-format text --add-dir $projectRoot 1> $stdoutPath 2> $stderrPath
    $code = $LASTEXITCODE
    Set-Content -LiteralPath $returnPath -Value $code -Encoding ascii
    "return_code=$code"
}
finally {
    Pop-Location
}
