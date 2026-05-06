# Phase11C Codex-ClaudeCode Fusion Decision

状态：`FUSION_DECISION_NO_STUDENT_MERGE`

## 输入

- Codex A 本地失败审计：
  - `08_review/phase11C_bad_word_four_element_failure_audit.md`
  - `codex_lane/phase11C_bad_word_content_audit/bad_word_four_element_failure_matrix_codex.csv`
  - `codex_lane/phase11C_bad_word_content_audit/codex_phase11C_source_verified_rewrite_samples.md`
- Terminal ClaudeCode T1 可见窗口输出：
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/bad_word_four_element_failure_matrix.csv`
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/bad_word_four_element_failure_report.md`
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/four_element_gold_contract.md`
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/rewrite_samples_10_entries.md`
  - `claudecode_lane/phase11C_bad_word_content_audit_visible/next_rebuild_plan.md`

## 一致结论

1. 坏 Word/Markdown 是内容失败，不是格式失败。
2. 坏稿中假设问、制作说明式答案落点、多节点复制、选择题缺错项分析、推理题模板收尾均为硬失败。
3. 坏稿不得作为 Word polish 基础。
4. Phase11D 必须从源核条目和小批次候选重建 Markdown。

## 分歧或需校正点

- T1 的部分样例沿用 `phase11A` 摘录或候选稿措辞，仍需 Codex 回到题面/细则核验。
- T1 把部分条目写成“示范”，但 Codex 判定：示范不等于正文，不得绕过 GPT/Opus/Governor。
- `2025海淀二模 Q20`、`2026丰台一模 Q18(2)` 等 T1 标注为 BLOCKED 的条目必须继续卡住。

## 融合裁决

- 采纳 T1 的失败审计与合同方向。
- 采纳 T1 的 Phase11D → 11E → 11F → 11G 顺序。
- 不采纳任何未经 Codex 源核的样例为正式学生正文。
- 下一批正文重建只从已核源条目开始，优先硬样本和 Phase11B Batch01 经 GPT 审稿后的候选。
