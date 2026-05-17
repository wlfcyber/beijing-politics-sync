param()

$ErrorActionPreference = 'Stop'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$claude = 'C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Packages\Anthropic.ClaudeCode_Microsoft.Winget.Source_8wekyb3d8bbwe\claude.exe'

$req = Get-Content -Encoding UTF8 -Raw (Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md')
$protocol = Get-Content -Encoding UTF8 -Raw (Join-Path $repo 'skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md')
$claudeIndex = Get-Content -Encoding UTF8 -Raw (Join-Path $PSScriptRoot 'CLAUDECODE_COMBINED_CORE_INDEX.csv')
$codexIndex = Get-Content -Encoding UTF8 -Raw (Join-Path $PSScriptRoot 'CODEX_CURRENT_CORE_INDEX.csv')

$prompt = @"
You are ClaudeCode. Compare two core indexes for the Selective Compulsory 1 politics handbook and produce fusion recommendations.

Output Markdown only to help the next fusion step.

Required sections:

1. 总体判断
2. 必须采用 ClaudeCode 拆分的节点
3. 必须保留 Codex 合并的节点
4. Codex 归桶可疑或应改的节点
5. ClaudeCode 过度拆分、需要回并的节点
6. 经济全球化重点复查
7. 新型国际关系 / 合作共赢 重点复查
8. 最终融合执行清单

Hard criteria:

- Merge only when rubric wording is close, answer-sheet wording is substitutable, or the rubric explicitly lists alternatives in the same scoring point.
- Do not merge terms merely because their abstract essence is similar.
- 新型国际关系 belongs in 政治多极化, not 理论.
- Economic globalization must not collapse 开放型世界经济, 开放型经济, 创新型开放型世界经济, 全球经济治理, 多边贸易体系, 普惠包容的经济全球化, 贸易自由化 into one node.
- Be concrete. Name exact core nodes.

[CURRENT USER REQUIREMENTS]
$req

[TERM PROTOCOL]
$protocol

[CLAUDECODE CORE INDEX]
$claudeIndex

[CURRENT CODEX CORE INDEX]
$codexIndex
"@

$outPath = Join-Path $PSScriptRoot 'CLAUDECODE_INDEX_FUSION_RECOMMENDATIONS.md'
$errPath = Join-Path $PSScriptRoot 'CLAUDECODE_INDEX_FUSION_RECOMMENDATIONS.stderr.txt'
$prompt | & $claude -p --model opus --effort max --tools '' --output-format text 2> $errPath | Set-Content -Encoding UTF8 $outPath
exit $LASTEXITCODE
