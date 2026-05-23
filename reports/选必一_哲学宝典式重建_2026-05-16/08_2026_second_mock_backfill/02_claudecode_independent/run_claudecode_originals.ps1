$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()

$outDir = $PSScriptRoot
$batchDir = Split-Path -Parent $outDir
$runDir = Split-Path -Parent $batchDir
$reportsDir = Split-Path -Parent $runDir
$repo = Split-Path -Parent $reportsDir
$task = Join-Path $batchDir '01_source_packet\CLAUDECODE_ORIGINALS_TASK.md'
$rawDir = $env:CLAUDE_RAW_DIR
if (-not $rawDir) {
  throw 'CLAUDE_RAW_DIR is not set.'
}
$stdout = Join-Path $outDir 'claudecode_run_stdout.txt'
$stderr = Join-Path $outDir 'claudecode_run_stderr.txt'
$debug = Join-Path $outDir 'claudecode_debug.log'

Remove-Item -LiteralPath $stdout, $stderr, $debug -Force -ErrorAction SilentlyContinue
Set-Location -LiteralPath $repo

Get-Content -LiteralPath $task -Encoding UTF8 -Raw |
  claude -p `
    --model opus `
    --effort max `
    --ide `
    --permission-mode bypassPermissions `
    --add-dir $rawDir `
    --debug-file $debug `
    --output-format text `
    1> $stdout `
    2> $stderr

exit $LASTEXITCODE
