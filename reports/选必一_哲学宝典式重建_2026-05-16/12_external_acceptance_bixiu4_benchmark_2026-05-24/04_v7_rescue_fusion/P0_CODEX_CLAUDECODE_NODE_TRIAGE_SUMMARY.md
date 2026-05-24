# P0 Codex / ClaudeCode 节点差异审计摘要

生成时间：2026-05-24

- 本次重算使用索引：07_claudecode_full_rerun/CLAUDECODE_COMBINED_CORE_INDEX.csv 与 CODEX_CURRENT_CORE_INDEX.csv
- ClaudeCode 节点数：247
- Codex 当前节点数：94
- ClaudeCode -> Codex 精确覆盖：54
- ClaudeCode-only / split-out：193
- Codex -> ClaudeCode 精确背书：34
- Codex-only / merged：60

备注：GPT/Claude 审稿时引用的包内差异报告写的是 228 / 98 / 31 / 184 / 66；本表按当前索引文件重算，作为 v7 操作底表。差异本身不改变结论：v6 没有达到终稿。

## ClaudeCode 未被精确覆盖的桶分布

- 经济全球化：71
- 中国：56
- 政治多极化：25
- 理论：18
- 联合国：10
- 时代背景：9
- ：4

## Codex-only / 疑似合并桶分布

- 经济全球化：26
- 中国：17
- 政治多极化：9
- 联合国：3
- 理论：3
- 附：总说句 / 兜底加分表达：1
- 时代背景：1

## 使用规则

- exact_covered 只表示核心点字面规范化后相同，不等于题目级示例合格。
- claudecode_only_or_split_out 默认进入 P0 恢复池，除非回源证明属于边界或非选必一。
- codex_only_or_merged_node 默认进入 P0 反合并池，必须查明是否由两道以上题压缩而来。
- 分类修正必须服从用户六大顶层框架。
