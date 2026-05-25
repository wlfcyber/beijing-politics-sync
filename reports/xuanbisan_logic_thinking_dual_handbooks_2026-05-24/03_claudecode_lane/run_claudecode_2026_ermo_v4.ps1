$ErrorActionPreference = 'Continue'

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom

$lane = $PSScriptRoot
$root = Split-Path -Parent $lane
$reportsDir = Split-Path -Parent $root
$projectRoot = Split-Path -Parent $reportsDir
$promptPath = Join-Path $lane 'CLAUDECODE_B_LINE_PROMPT_2026_ERMO_RERUN.md'
$stdoutPath = Join-Path $lane 'logs\claudecode_2026_ermo_rerun_stdout_v4.log'
$stderrPath = Join-Path $lane 'logs\claudecode_2026_ermo_rerun_stderr_v4.log'
$debugPath = Join-Path $lane 'logs\claudecode_debug_prompt_v4.log'
$returnPath = Join-Path $lane 'claudecode_2026_ermo_rerun_return_code_v4.txt'
$startedPath = Join-Path $lane 'claudecode_2026_ermo_rerun_started_v4.txt'
$finishedPath = Join-Path $lane 'claudecode_2026_ermo_rerun_finished_v4.txt'

Set-Content -LiteralPath $startedPath -Value (Get-Date -Format o) -Encoding utf8
Remove-Item -LiteralPath $stdoutPath, $stderrPath, $debugPath -Force -ErrorAction SilentlyContinue

$env:DEBUG = '*'
$env:CLAUDE_CODE_ENABLE_TELEMETRY = '0'

Push-Location $root
try {
    $prompt = Get-Content -LiteralPath $promptPath -Raw -Encoding utf8
    $prompt | claude -p --debug --model opus --effort max --permission-mode bypassPermissions --output-format text --add-dir $projectRoot 1> $stdoutPath 2> $debugPath
    $code = $LASTEXITCODE
    Set-Content -LiteralPath $returnPath -Value $code -Encoding ascii
}
catch {
    $_ | Out-String | Set-Content -LiteralPath $stderrPath -Encoding utf8
    Set-Content -LiteralPath $returnPath -Value 'powershell_exception' -Encoding ascii
}
finally {
    Pop-Location
    Set-Content -LiteralPath $finishedPath -Value (Get-Date -Format o) -Encoding utf8
}
