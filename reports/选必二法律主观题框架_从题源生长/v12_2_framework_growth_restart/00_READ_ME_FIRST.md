# v12.2 framework growth restart

本目录用于把选必二拉回最初的正确轨道：Codex 只做题源清洗、批次组织、证据裁决和门禁记录；GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive 必须基于处理后的题源批次独立生长框架，再互相批判，最后由 Codex 按题源证据裁决是否接受框架变化。

## 当前事实底座

- 上一阶段入口：`v12_1_reference_cleanup_and_stage_integration/`
- 当前可用正文题链：42 道 source-locked / recovered-locked。
- 参考运行：5 道 `OPEN_OR_REFERENCE`，只能作为开放容器或边界参考，不能支撑核心框架。
- 下一版回填候选：6 道，已经有源寻线索，但尚未纳入 v12.1 正文。
- 当前不得宣称：最终宝典、DOCX/PDF、TASK_COMPLETE、53/65/70 全闭合。

## 本轮目标

1. 让 GPT 和 Claude 先读处理后的题源批次，而不是读一个已经写好的终稿。
2. GPT 独立提出高频主干、覆盖缺口、风险和版本变更标准。
3. Claude 独立提出学生可启动结构、迁移语言、低频容器和过抽象风险。
4. 第二轮必须交叉批判：GPT 看 Claude 原方案，Claude 看 GPT 原方案。
5. Codex 只在双模型输出和本地证据都到位后，写 `codex_adjudication/`，决定哪些框架变化进入候选版本。

## 输入文件

- `evidence_pack/batch_01_priority_district_core_cards.md`
- `evidence_pack/batch_02_remaining_core_cards.md`
- `evidence_pack/batch_03_boundary_reference_and_next_backfill_cards.md`
- `evidence_pack/core_42_v12_1.csv`
- `evidence_pack/true_coverage_matrix_v12_1.csv`
- `evidence_pack/reference_5_appendix.md`
- `evidence_pack/next_backfill_6_summary.csv`

## 输出门禁

- `model_outputs/gpt_round01_independent_framework.md`
- `model_outputs/claude_round01_independent_framework.md`
- `cross_critiques/gpt_critiques_claude_round01.md`
- `cross_critiques/claude_critiques_gpt_round01.md`
- `codex_adjudication/round01_convergence_and_evidence_adjudication.md`

缺任一文件，不得写新版框架 PASS。

