# ClaudeCode P1 Recheck: 选必三二线闭合中优先样本复核

你是真实 ClaudeCode CLI 的 P1 回源复核工。当前任务不是终稿写作，不生成 Word/PDF，不写 PASS/最终版/终稿。

## 运行目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\p1_recheck`

只写本目录，不覆盖 P0、batches、fusion 主文件或 delivery。

## 必读规则

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\P0_FUSION_PATCH_REPORT.md`

## 输入文件

- P1 清单：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\RECHECK_MANIFEST_ENRICHED.csv`
- P1 source index：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p1_recheck_sources\P1_SOURCE_TEXT_INDEX.csv`
- P1 source texts 目录：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p1_recheck_sources`
- 当前融合稿：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\FRAMEWORK_FIRST_FUSION_P0_PATCHED.md`

## 任务边界

只处理 `RECHECK_MANIFEST_ENRICHED.csv` 中 `priority=P1` 的 11 行：

- Q-2024朝阳期中-18-晏子推理
- Q-2024朝阳期中-18-楚王推理
- Q-2026东城一模-19-4 x4
- Q-2025丰台期末-18-1 x2
- Q-2025顺义一模-17-1 x3

每行必须回源核验：

1. 是否能在试卷题面或细则/评标/讲评/答案源中找到对应题号、设问、材料、答案或细则依据。
2. `framework_node` 是否被来源支持，尤其区分类比推理、归纳推理、发散聚合、超前思维、假言判断、联言/选言判断。
3. 当前条目的材料信号、触发逻辑、卷面句是否需要修补。
4. 如果来源不足，不能硬确认，必须标明 `source_insufficient` 或 `block_from_student_body`。

注意：

- 选择题只能做 `B-choice-signal`，不能冒充主观题评分链。
- 讲评、评标、教师版答案与正式细则要分清；有明确评分点/细则的才能判 A-formal。
- A-support 不能写成 A-formal。
- 不要使用学生面对面的“固定分析流程”这个说法。

## 必交文件

1. `PROGRESS.md`
2. `P1_RECHECK_DECISIONS.csv`
3. `P1_RECHECK_PATCHES.jsonl`
4. `P1_SOURCE_EVIDENCE.md`
5. `P1_RECHECK_ACCEPTANCE.md`

### `P1_RECHECK_DECISIONS.csv` 字段

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

`decision` 只能是：

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

`can_enter_fusion` 只能是 `yes/no`。

### `P1_RECHECK_PATCHES.jsonl` 字段

每行 JSON 必须含：

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

如果不需要修补，也写一行，`decision=confirmed`，patched 字段可沿用当前内容但必须是干净中文。

### `P1_SOURCE_EVIDENCE.md`

按 source_id 分组，记录每个 P1 条目使用哪份试卷/细则/评标文本，引用短片段即可，不要大段复制。

### `P1_RECHECK_ACCEPTANCE.md`

写清：

- P1 rows 总数是否为 11。
- 每种 decision 的数量。
- 还有多少 `source_insufficient / wrong_framework / block_from_student_body`。
- 是否生成 Word/PDF：必须写 `no`。
- 是否授权终稿：必须写 `no`。

现在开始。先写 `PROGRESS.md` 启动段，然后逐条回源，最后再写 acceptance。
