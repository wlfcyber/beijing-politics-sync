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

$req = Get-Content -Encoding UTF8 -Raw (Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md')
$protocol = Get-Content -Encoding UTF8 -Raw (Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md')
$batch = Get-Content -Encoding UTF8 -Raw (Join-Path $runRoot ("03_fusion\BATCH_{0}_FINAL_AFTER_GPT_AND_CLAUDE.md" -f $BatchId))

$prompt = @"
You are ClaudeCode. The previous full output for BATCH $BatchId was truncated at the beginning. Regenerate ONLY the beginning part.

Output Markdown only.

Start with exactly:

# BATCH $BatchId 独立厚稿：补头

Then output the first 6 to 8 core nodes that should appear from the beginning of this batch draft, in six-bucket order:

## 时代背景
## 理论
## 经济全球化
## 政治多极化
## 中国
## 联合国

Use this unit:

### 核心答题点：...（出现N次）
【表述积累】
- ...
【本节点真题】
**题例A：...**
- 【细则术语】...
- 【材料触发点】...
- 【设问】...
- 【为什么能想到】...
- 【答案落点】...
- 【细则位置】...
- 【来源】...

Stop after 6 to 8 complete core nodes. Do not continue into later nodes. Do not mention Codex, GPT, Claude, prompt, review, local paths, or backstage workflow in the body.

Hard rules:
- 新型国际关系 belongs in 政治多极化, not 理论.
- Economic globalization merge requires close/substitutable rubric wording or explicit same-point alternatives.
- Do not collapse 开放型世界经济, 开放型经济, 创新型开放型世界经济, 全球经济治理, 贸易自由化, 多边贸易体系 into one node merely because they are related.

[CURRENT USER REQUIREMENTS]
$req

[TERM PROTOCOL]
$protocol

[SOURCE BATCH $BatchId]
$batch
"@

$outPath = Join-Path $outDir ("CLAUDECODE_BATCH_{0}_HEAD.md" -f $BatchId)
$errPath = Join-Path $logDir ("CLAUDECODE_BATCH_{0}_HEAD.stderr.txt" -f $BatchId)
$logPath = Join-Path $logDir ("CLAUDECODE_BATCH_{0}_HEAD.log.txt" -f $BatchId)

"START HEAD $BatchId $(Get-Date -Format o)" | Set-Content -Encoding UTF8 $logPath
"MODEL opus; EFFORT max; NOTE Claude Opus 4.7 alias verified via minimal CLI check" | Add-Content -Encoding UTF8 $logPath
$prompt | & $claude -p --model opus --effort max --tools '' --output-format text 2> $errPath | Set-Content -Encoding UTF8 $outPath
$code = $LASTEXITCODE
"EXIT HEAD $BatchId $code $(Get-Date -Format o)" | Add-Content -Encoding UTF8 $logPath
exit $code
