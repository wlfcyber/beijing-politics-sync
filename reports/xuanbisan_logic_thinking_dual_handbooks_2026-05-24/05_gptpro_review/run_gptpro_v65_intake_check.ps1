param(
    [string]$ProjectRoot = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = Split-Path -Parent $PSScriptRoot
}

$resultRel = "05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md"
$checkRel = "05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md"
$triageRel = "05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md"

$resultPath = Join-Path $ProjectRoot $resultRel
$checkPath = Join-Path $ProjectRoot $checkRel
$checkedAt = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss zzz")

function Write-CheckReport {
    param(
        [string]$Status,
        [string[]]$Findings,
        [string[]]$NextActions
    )

    $lines = @()
    $lines += "# GPT Pro V65 Intake Ready Check"
    $lines += ""
    $lines += "Status: ``$Status``"
    $lines += ""
    $lines += "- Checked at: $checkedAt"
    $lines += "- Required result: ``$resultRel``"
    $lines += "- Filled triage target: ``$triageRel``"
    $lines += ""
    $lines += "## Findings"
    $lines += ""
    foreach ($finding in $Findings) {
        $lines += "- $finding"
    }
    $lines += ""
    $lines += "## Next Actions"
    $lines += ""
    foreach ($action in $NextActions) {
        $lines += "- $action"
    }
    $lines += ""
    Set-Content -LiteralPath $checkPath -Value $lines -Encoding UTF8
}

if (-not (Test-Path -LiteralPath $resultPath)) {
    Write-CheckReport `
        -Status "BLOCKED_MISSING_GPTPRO_RESULT" `
        -Findings @("GPT Pro V65 result file does not exist.") `
        -NextActions @("Save the real GPT Pro response to ``$resultRel``.", "Do not run Claude V63 or final delivery gates yet.")
    exit 2
}

$item = Get-Item -LiteralPath $resultPath
if ($item.Length -eq 0) {
    Write-CheckReport `
        -Status "BLOCKED_EMPTY_GPTPRO_RESULT" `
        -Findings @("GPT Pro V65 result file exists but is empty.") `
        -NextActions @("Replace it with the full real GPT Pro response.", "Do not run Claude V63 or final delivery gates yet.")
    exit 2
}

$text = Get-Content -LiteralPath $resultPath -Raw
$normalized = $text -replace "`r`n", "`n"
$placeholderChecks = @(
    @{ Name = "TODO marker"; Pattern = "(?is)\bTODO\b" },
    @{ Name = "placeholder marker"; Pattern = "(?is)\bplaceholder\b|\btemplate\b" },
    @{ Name = "paste-result instruction"; Pattern = "(?is)paste\s+(the\s+)?real\s+GPT\s+Pro\s+response" },
    @{ Name = "not actual review marker"; Pattern = "(?is)not\s+(the\s+)?actual\s+external\s+review|not\s+treat\s+this\s+template" }
)
$placeholderSignals = @()
foreach ($check in $placeholderChecks) {
    if ($normalized -match $check.Pattern) {
        $placeholderSignals += $check.Name
    }
}
if ($placeholderSignals.Count -gt 0) {
    Write-CheckReport `
        -Status "BLOCKED_PLACEHOLDER_GPTPRO_RESULT" `
        -Findings @("GPT Pro V65 result file contains placeholder/template signals: $($placeholderSignals -join ', ').", "The file must be the full real GPT Pro response, not a handoff template, TODO note, or save instructions.") `
        -NextActions @("Replace ``$resultRel`` with the full real GPT Pro response.", "Do not fill ``$triageRel`` from a placeholder.", "Do not run Claude V63 yet.")
    exit 2
}

$checks = @(
    @{ Name = "verdict"; Pattern = "(?is)\b(verdict|结论|判定)\b.*?(not_final|ready_for_claude_review_after_gptpro|reject|不终稿|退回|拒绝)" },
    @{ Name = "P0 findings"; Pattern = "(?is)\bP0\b|严重问题|一级问题|必须先修" },
    @{ Name = "P1 findings"; Pattern = "(?is)\bP1\b|重要问题|二级问题" },
    @{ Name = "thinking handbook structure judgment"; Pattern = "(?is)思维宝典|thinking handbook|framework|触发链|材料.*方法.*答案" },
    @{ Name = "reasoning handbook structure judgment"; Pattern = "(?is)推理宝典|reasoning handbook|推理形式|同形|题型" },
    @{ Name = "must-fix-before-Claude list"; Pattern = "(?is)Claude V63|Claude.*前|before Claude|必须.*回源|must[- ]fix" },
    @{ Name = "forbidden claims"; Pattern = "(?is)禁止声明|forbidden claims|final pass|终稿|可发布|已通过" },
    @{ Name = "source verification request"; Pattern = "(?is)回源|source verification|source-verified|原题|评分细则|答案表|ledger|source-lock" }
)

$findings = @()
$missing = @()
foreach ($check in $checks) {
    if ($normalized -match $check.Pattern) {
        $findings += "Found required section/signal: $($check.Name)."
    } else {
        $missing += $check.Name
    }
}

if ($normalized.Length -lt 800) {
    $missing += "result body length >= 800 characters"
}

if ($missing.Count -gt 0) {
    $allFindings = @()
    $allFindings += $findings
    foreach ($m in $missing) {
        $allFindings += "Missing or too weak: $m."
    }
    Write-CheckReport `
        -Status "BLOCKED_INCOMPLETE_GPTPRO_RESULT" `
        -Findings $allFindings `
        -NextActions @("Replace or expand ``$resultRel`` with the full GPT Pro response.", "Only after this check passes may Codex fill ``$triageRel``.", "Do not run Claude V63 yet.")
    exit 2
}

Write-CheckReport `
    -Status "READY_FOR_GPTPRO_TRIAGE" `
    -Findings $findings `
    -NextActions @("Read ``$resultRel`` and fill ``$triageRel``.", "Apply only source-verified P0/P1 patches under ``04_fusion\POST_EXTERNAL_REVIEW_SOURCE_PATCH_PROTOCOL_V70.md``.", "Run Claude V63 only after GPT Pro triage and required source-verified patches are complete.")

exit 0
