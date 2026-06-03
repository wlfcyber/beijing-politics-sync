# Low Evidence Choice Body Triage

time: `2026-05-26T05:31:30+08:00`

verdict: `CHOICE_BODY_TRIAGE_READY_NOT_YET_FUSED`

本文件处理 ClaudeCode B 线 `reasoning_choice.jsonl` 中低证据等级或占位选择题，防止占位内容进入推理宝典学生正文。

## 总规则

- `decision=index` 的选择题不得进入学生正文。
- `B-choice-signal` 可以保留为审计证据等级，但只有在候选正文或原卷已具备完整题干、完整选项、答案、正确理由、逐项错因时，才能作为候选正文继续保留。
- 任何含 `(以原卷为准)`、`(索引条目)`、`待按原卷`、占位选项或占位答案的内容，一律不得进入学生正文。

## RC-2026-SHUNYI-1MO-Q4 / Q0033

- B decision: `body`
- B evidence: `B-choice-signal`
- Codex triage: `conditional_keep_as_reasoning_choice_body`
- reason:
  - B 线条目已有完整题干、四个完整选项、答案 A、正确理由和 B/C/D 逐项错因；
  - 当前候选 MD `推理宝典` 中 `2026顺义一模 Q4` 已完整写入正文；
  - 证据等级仍低，不升级为 A-formal。
- fusion instruction:
  - 可继续保留在推理册类比推理选择题正文；
  - 学生正文不出现 `B-choice-signal`；
  - 外审时标注为低证据保留项，若外审或回源发现原卷/答案不一致，立即转 boundary。

## RC-2025-FENGTAI-FINAL-Q9 / Q0028

- B decision: `body`
- B evidence: `B-choice-signal`
- B issue:
  - B 条目仍是占位：题干、选项、答案和错因含 `(以原卷为准)`、`(同上)`、`待按原卷选项原文补齐错因`。
- Codex triage: `reject_bline_placeholder_keep_candidate_md_if_complete`
- reason:
  - 占位 B 条目不能进入学生正文；
  - 当前候选 MD 已有 `2025丰台期末 Q9` 完整题干、完整选项、答案 D、正确理由和逐项错因；
  - 融合时只能采用候选 MD 已完成版本，不能采用 B 线占位版本。
- fusion instruction:
  - 保留候选 MD 的完整 `2025丰台期末 Q9` 条目；
  - 不导入 B 线 `RC-2025-FENGTAI-FINAL-Q9` 的任何占位文本；
  - 审计字段标注：`bline_placeholder_rejected_candidate_complete_retained`。

## RC-2026-HAIDIAN-2MO-Q4-INDEX / Q0123

- B decision: `index`
- Codex triage: `keep_audit_index_only`
- fusion instruction: 不进学生正文；待回源或外审升级后再考虑补入。

## RC-2026-SHUNYI-2MO-Q6-INDEX / Q0137

- B decision: `index`
- Codex triage: `keep_audit_index_only`
- fusion instruction: 不进学生正文；待回源或外审升级后再考虑补入。

## RC-2026-SHUNYI-2MO-Q7-INDEX / Q0138

- B decision: `index`
- Codex triage: `keep_audit_index_only`
- fusion instruction: 不进学生正文；待回源或外审升级后再考虑补入。

## Gate Effect

After applying this triage:

- B 线低证据 choice body 不再直接污染推理册；
- 已完整的候选 MD 选择题可保留，但必须重新进入最终文本层和视觉 QA；
- 占位文本不得进入 DOCX/PDF。
