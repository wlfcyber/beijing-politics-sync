# CODEX_BLINE_FUSION_BATCH2_REASONING_HARDSAMPLES_20260526

timestamp: `2026-05-26T05:52:00+08:00`

verdict: `BATCH2_REASONING_HARDSAMPLES_PARTIAL_FUSION_MARKDOWN_NOT_YET_REBUILT`

## Scope

本批只处理推理宝典的 B 线差异融合第一小批，重点是选择题完整错因与前台后台残留清理。

## Applied Changes

### 1. `2026海淀二模 Q5`

发现推理候选 Markdown 中残留“答案表锁定的保真结论”一类后台口径。

已改为学生可读表达：

- 原：`不是本题答案表锁定的保真结论`
- 新：`不是本题能够推出的保真结论`

### 2. `2024朝阳一模 Q6`

按 B 线 `RC-2024-CHAOYANG-1MO-Q6` 加厚完整错项分析。

已改写：

- `材料触发点`：由短标签扩成 A/B/C/D 四项具体错误来源；
- `为什么能想到`：从“逐项找规则”扩成划分层级、矛盾律、四概念与反对判断同假之间的比较；
- `诱人错项和错因`：补成“为什么诱人 + 为什么错”的学生版表达。

### 3. `2025顺义一模 Q7`

抽查确认当前候选稿已与 B 线硬规则一致：

- 正向选 A；
- 错误名称应为“大项不当扩大”，不是“小项不当扩大”；
- B/C/D 已说明为什么是“规则判断正确所以不选”。

本批未追加改写。

### 4. `2024东城一模 Q6`

抽查确认当前候选稿已存在 B 线同构写法：

- D 项为正确答案；
- A/B/C 逐项错因已写明；
- 未发现需要本批替换的硬错误。

## Verification

已扫描推理候选 Markdown，未命中以下后台残留：

- `答案表`
- `客观答案表`
- `制作`
- `审计`
- `source`
- `B线`
- `A-formal`
- `run_question`
- `候选`
- `以原卷为准`
- `本题规则要点是`

保留的 `待处理` 属于原题/正文自然语义，不是后台门禁。

## Remaining Gates

- 本批只完成推理册小批差异融合，尚未处理全部 `fusion_candidates.md`；
- DOCX/PDF 尚未基于本批重新生成；
- 推理册仍需继续检查 F2/F3/F4/F5 类差异；
- GPT Pro / Claude 真实审查、fresh-context 盲测和最终 Governor / Confucius 仍未通过。
