$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$reviewDir = $PSScriptRoot
$runDir = Split-Path -Parent $reviewDir
$sourceRunner = Join-Path $reviewDir 'run_claude_external_review_v63.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("xuanbisan_claude_v63_gate_test_{0}" -f $PID)

function Remove-SafeTempRoot {
  param([string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  $resolved = (Resolve-Path -LiteralPath $Path).Path
  $tempResolved = (Resolve-Path -LiteralPath ([IO.Path]::GetTempPath())).Path.TrimEnd('\')
  if (-not $resolved.StartsWith($tempResolved, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to delete outside temp: $resolved"
  }
  if ((Split-Path -Leaf $resolved) -notlike 'xuanbisan_claude_v63_gate_test_*') {
    throw "Refusing to delete unexpected temp path: $resolved"
  }
  Remove-Item -LiteralPath $resolved -Recurse -Force
}

function Assert-Equal {
  param(
    [object]$Actual,
    [object]$Expected,
    [string]$Message
  )
  if ($Actual -ne $Expected) {
    throw "$Message Expected=[$Expected] Actual=[$Actual]"
  }
}

function Assert-True {
  param(
    [bool]$Condition,
    [string]$Message
  )
  if (-not $Condition) {
    throw $Message
  }
}

function New-TestRun {
  Remove-SafeTempRoot $tempRoot
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '06_claude_review') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '05_gptpro_review') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot '10_packets') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $tempRoot 'bin') | Out-Null
  Copy-Item -LiteralPath $sourceRunner -Destination (Join-Path $tempRoot '06_claude_review\run_claude_external_review_v63.ps1') -Force
  'packet for gate test' | Set-Content -LiteralPath (Join-Path $tempRoot '10_packets\CLAUDE_REVIEW_PACKET_V63.md') -Encoding UTF8

  $fakeClaude = @'
@echo off
echo fake-claude-called %*>>"%FAKE_CLAUDE_MARKER%"
if "%1"=="--version" (
  echo claude-fake 0.0.0
) else (
  echo fake claude review body
)
exit /b 0
'@
  $fakeClaude | Set-Content -LiteralPath (Join-Path $tempRoot 'bin\claude.cmd') -Encoding ASCII
}

function Invoke-TestRunner {
  $env:FAKE_CLAUDE_MARKER = Join-Path $tempRoot 'fake_claude_called.txt'
  $oldPath = $env:PATH
  $oldPreference = $ErrorActionPreference
  $env:PATH = (Join-Path $tempRoot 'bin') + ';' + $oldPath
  $ErrorActionPreference = 'Continue'
  try {
    & powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $tempRoot '06_claude_review\run_claude_external_review_v63.ps1') *> (Join-Path $tempRoot 'runner_host_output.txt')
  } finally {
    $env:PATH = $oldPath
    $ErrorActionPreference = $oldPreference
  }
}

try {
  New-TestRun
  Invoke-TestRunner
  $returnCodePath = Join-Path $tempRoot '06_claude_review\claude_external_review_v63_return_code.txt'
  Assert-Equal ((Get-Content -LiteralPath $returnCodePath -Raw).Trim()) '2' 'Missing GPT result should write gate return code 2.'

  New-TestRun
  'real gpt pro result body with enough local text' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  Invoke-TestRunner
  Assert-Equal ((Get-Content -LiteralPath $returnCodePath -Raw).Trim()) '2' 'GPT result without ready intake should be blocked.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot 'fake_claude_called.txt'))) 'Claude command must not run before intake is ready.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'))) 'Claude result must not be produced before intake is ready.'

  New-TestRun
  'real gpt pro result body with enough local text' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  'Status: `READY_FOR_GPTPRO_TRIAGE`' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md') -Encoding UTF8
  Invoke-TestRunner
  Assert-Equal ((Get-Content -LiteralPath $returnCodePath -Raw).Trim()) '2' 'Ready intake without filled GPT triage should be blocked.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot 'fake_claude_called.txt'))) 'Claude command must not run before GPT triage exists.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'))) 'Claude result must not be produced before GPT triage exists.'

  New-TestRun
  'real gpt pro result body with enough local text' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  'Status: `READY_FOR_GPTPRO_TRIAGE`' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md') -Encoding UTF8
  'filled gpt pro triage' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  Invoke-TestRunner
  Assert-Equal ((Get-Content -LiteralPath $returnCodePath -Raw).Trim()) '2' 'Ready intake plus weak GPT triage without V83 status should be blocked.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot 'fake_claude_called.txt'))) 'Claude command must not run before V83 GPT triage quality gate is ready.'
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md'))) 'Claude result must not be produced before V83 GPT triage quality gate is ready.'

  New-TestRun
  'real gpt pro result body with enough local text' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md') -Encoding UTF8
  'Status: `READY_FOR_GPTPRO_TRIAGE`' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_INTAKE_READY_CHECK.md') -Encoding UTF8
  'filled source-routed gpt pro triage' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_FILLED.md') -Encoding UTF8
  'Status: `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`' | Set-Content -LiteralPath (Join-Path $tempRoot '05_gptpro_review\GPTPRO_V65_TRIAGE_READY_CHECK_V83.md') -Encoding UTF8
  Invoke-TestRunner
  Assert-Equal ((Get-Content -LiteralPath $returnCodePath -Raw).Trim()) '0' 'Ready intake plus V83-ready GPT triage should allow Claude runner.'
  Assert-True (Test-Path -LiteralPath (Join-Path $tempRoot '06_claude_review\CLAUDE_EXTERNAL_REVIEW_RESULT_V63.md')) 'Allowed runner should preserve Claude output as the V63 result.'

  'PASS'
} finally {
  if ($env:KEEP_GATE_TEST_TEMP -ne '1') {
    Remove-SafeTempRoot $tempRoot
  }
}
