# 双线生产记录

## Codex 线

- 任务：锁定最新宝典，抽取 Heading 3 条目，和 V3 题源候选逐题比对。
- 产出：
  - `01_codex_lane/latest_handbook_entry_index.csv`
  - `01_codex_lane/v3_inventory_vs_latest_docx.csv`
  - `01_codex_lane/high_risk_contradiction_keyword_scan.csv`
  - `01_codex_lane/CODEX_FULL_COVERAGE_SCAN_REPORT.md`
- 结论：旧最新版有 533 个 Heading 3；V3 候选口径下，主观 A/B 缺口 14 条，选择 C 缺口 140 条；主要矛盾、矛盾主要方面、主流支流虽有正文词频，但缺少独立可检索节点。

## ClaudeCode 线

- 任务：作为生产线独立读扫描表，提出补入条目、矛盾专项升节方案和选择题补覆盖策略。
- 产出：
  - `02_claudecode_lane/CLAUDECODE_PRODUCTION_PROMPT.md`
  - `02_claudecode_lane/claudecode_production_candidates.md`
- 结论：ClaudeCode 独立确认必须升为独立节点的四类内容：主要矛盾和次要矛盾、矛盾的主要方面和次要方面、两点论和重点论、主流和支流；并给出主观题补入清单与选择题优先补入方案。

## 融合线

- 任务：保留用户认可的 2026 二模补题版为底稿，不重做整本文档，只做框架内补丁和全题索引。
- 产出：
  - 桌面 Word：`C:\Users\Administrator\Desktop\哲学宝典最终版-飞哥正志讲堂_主次矛盾全覆盖补丁v7_2026-05-23.docx`
  - 桌面 PDF：`C:\Users\Administrator\Desktop\哲学宝典最终版-飞哥正志讲堂_主次矛盾全覆盖补丁v7_2026-05-23.pdf`
  - 仓库备份：`04_delivery/`

