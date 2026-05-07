# ClaudeCode P1 Repair: write the missing deliverables

你是真实 ClaudeCode CLI。上一轮 P1 只写了 `PROGRESS.md`，且在 `PROGRESS.md` 中错误勾选了已写 deliverables，但实际四个交付文件缺失。现在只做修补：补齐缺失文件，不做 Word/PDF，不做终稿。

## 运行目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\p1_recheck`

只写本目录。不要覆盖 P0、batches、fusion 主文件、delivery。

## 必须立即写出的文件

1. `P1_RECHECK_DECISIONS.csv`
2. `P1_RECHECK_PATCHES.jsonl`
3. `P1_SOURCE_EVIDENCE.md`
4. `P1_RECHECK_ACCEPTANCE.md`
5. 追加修正 `PROGRESS.md`，说明上一轮假进度已由本轮修复。

不要再只写 `PROGRESS.md`。

## 输入

- P1 manifest：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\RECHECK_MANIFEST_ENRICHED.csv`
- P1 source index：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p1_recheck_sources\P1_SOURCE_TEXT_INDEX.csv`
- P1 source texts：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p1_recheck_sources`
- 当前融合稿：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\FRAMEWORK_FIRST_FUSION_P0_PATCHED.md`
- 监督补丁：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\p1_recheck\SUPERVISOR_PATCH_01_FALSE_PROGRESS.md`

## 只处理 P1 的 11 行

从 `RECHECK_MANIFEST_ENRICHED.csv` 中筛选 `priority=P1`。必须正好 11 行，不能多也不能少。

## CSV 字段

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

`decision` 只能是：

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

`can_enter_fusion` 只能是 `yes/no`。

## JSONL 字段

每行 JSON 必须含：

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

## Evidence rules

- 正式评分细则、阅卷细则、评标中明确给分点：`A-formal`。
- 教师版参考答案、讲评但非明确评分细则：`A-support`。
- 选择题只可 `B-choice-signal`。
- 不确定就不要硬确认。

现在开始，先写 `P1_RECHECK_DECISIONS.csv`，再写 JSONL、evidence、acceptance，最后才修正 progress。
