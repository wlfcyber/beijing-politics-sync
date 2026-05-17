$ErrorActionPreference = 'Stop'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$claude = 'C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\claude.exe'
$promptPath = Join-Path $PSScriptRoot 'CLAUDECODE_FULL_RERUN_PROMPT.md'
$outDir = $PSScriptRoot
$logPath = Join-Path $outDir 'CLAUDECODE_FULL_RERUN_RUN_LOG.txt'
$stdoutPath = Join-Path $outDir 'CLAUDECODE_FULL_RERUN_STDOUT.txt'
$stderrPath = Join-Path $outDir 'CLAUDECODE_FULL_RERUN_STDERR.txt'

Set-Location $repo
$prompt = Get-Content -Encoding UTF8 -Raw $promptPath
"START $(Get-Date -Format o)" | Set-Content -Encoding UTF8 $logPath

try {
    & $claude -p --model opus --effort max --permission-mode bypassPermissions --dangerously-skip-permissions --allowedTools 'Read,Write,Edit,MultiEdit,Glob,Grep,LS,Bash' --output-format text $prompt > $stdoutPath 2> $stderrPath
    $code = $LASTEXITCODE
    "EXIT $code $(Get-Date -Format o)" | Add-Content -Encoding UTF8 $logPath
    exit $code
} catch {
    "ERROR $($_.Exception.Message) $(Get-Date -Format o)" | Add-Content -Encoding UTF8 $logPath
    throw
}
