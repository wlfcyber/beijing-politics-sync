param(
    [Parameter(Mandatory=$true)]
    [string]$BatchId
)

$ErrorActionPreference = 'Stop'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$runRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$outDir = Join-Path $PSScriptRoot 'parts'
$logDir = Join-Path $PSScriptRoot 'batch_logs'
$claude = 'C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\claude.exe'

New-Item -ItemType Directory -Force -Path $outDir | Out-Null
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$reqPath = Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md'
$protocolPath = Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md'
$batchPath = Join-Path $runRoot ("03_fusion\BATCH_{0}_FINAL_AFTER_GPT_AND_CLAUDE.md" -f $BatchId)
$templatePath = Join-Path $PSScriptRoot 'CLAUDECODE_BATCH_TEMPLATE.md'

$req = Get-Content -Encoding UTF8 -Raw $reqPath
$protocol = Get-Content -Encoding UTF8 -Raw $protocolPath
$batch = Get-Content -Encoding UTF8 -Raw $batchPath
$template = Get-Content -Encoding UTF8 -Raw $templatePath

$prompt = $template.Replace('{BATCH_ID}', $BatchId).Replace('{REQ}', $req).Replace('{PROTOCOL}', $protocol).Replace('{BATCH}', $batch)

$outPath = Join-Path $outDir ("CLAUDECODE_BATCH_{0}.md" -f $BatchId)
$errPath = Join-Path $logDir ("CLAUDECODE_BATCH_{0}.stderr.txt" -f $BatchId)
$logPath = Join-Path $logDir ("CLAUDECODE_BATCH_{0}.log.txt" -f $BatchId)

"START $BatchId $(Get-Date -Format o)" | Set-Content -Encoding UTF8 $logPath
"MODEL opus; EFFORT max; NOTE Claude Opus 4.7 alias verified via minimal CLI check" | Add-Content -Encoding UTF8 $logPath
$prompt | & $claude -p --model opus --effort max --tools '' --output-format text 2> $errPath | Set-Content -Encoding UTF8 $outPath
$code = $LASTEXITCODE
"EXIT $BatchId $code $(Get-Date -Format o)" | Add-Content -Encoding UTF8 $logPath
exit $code
