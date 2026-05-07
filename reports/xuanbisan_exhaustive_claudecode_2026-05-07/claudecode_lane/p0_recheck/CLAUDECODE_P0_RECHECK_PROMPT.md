# ClaudeCode P0 Recheck: 选必三硬样本回源复核

你是真实 ClaudeCode CLI 的回源复核工。当前任务不是终稿写作，不生成 Word/PDF，不写 PASS/终稿/最终版。

## 运行目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\p0_recheck`

只写本目录，不覆盖前面批次、fusion 主文件或 delivery。

## 必读规则

- `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\overall_batch_closure\OVERALL_CLOSURE_REPORT.md`

## 输入文件

- P0 复核清单：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\RECHECK_MANIFEST_ENRICHED.csv`
- 框架融合底稿：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\framework_first_fusion\FRAMEWORK_FIRST_FUSION_DRAFT.md`
- P0 source text index：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p0_recheck_sources\P0_SOURCE_TEXT_INDEX.csv`
- P0 source texts 目录：`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\fusion\p0_recheck_sources`

## 任务边界

只处理 `RECHECK_MANIFEST_ENRICHED.csv` 中 `priority=P0` 的 19 行。

每行必须回源核验：

1. 是否能在试卷题面或细则/讲评/答案源中找到对应题号、设问、材料、答案或细则依据。
2. 现有 entry 的 `framework_node` 是否能被来源支持。
3. 现有 `材料怎么看 / 为什么想到 / 卷面句` 是否有明显错挂、过度扩展、模板化、截断或后台话术。
4. 如果来源不足，不能硬确认；标为 `source_insufficient` 或 `needs_codex_manual_recheck`。

注意：

- 2026 丰台一模试卷 PDF 文本抽取为空，优先使用 `2026丰台一模细则.pptx.txt` 和已有源索引；如果仍不够，明确记录缺口，不要猜。
- 选择题只能做 `B-choice-signal`，不能冒充主观题评分链。
- A-support 不能写成 A-formal。
- 合成子题号必须写清 `parent_question_id`，例如 `Q-2024朝阳二模-19-1-动态性` 的母题是 `Q-2024朝阳二模-19-1`。

## 必交文件

1. `PROGRESS.md`
2. `P0_RECHECK_DECISIONS.csv`
3. `P0_RECHECK_PATCHES.jsonl`
4. `P0_SOURCE_EVIDENCE.md`
5. `P0_RECHECK_ACCEPTANCE.md`

### `P0_RECHECK_DECISIONS.csv` 字段

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

`decision` 只能是：

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

`can_enter_fusion` 只能是 `yes/no`。

### `P0_RECHECK_PATCHES.jsonl` 字段

每行 JSON 必须含：

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

如果不需要修补，也写一行，`decision=confirmed`，patched 字段可沿用当前内容但必须是干净中文。

### `P0_SOURCE_EVIDENCE.md`

按 source_id 分组，记录每个 P0 条目使用了哪份试卷/细则/讲评文本，引用短片段即可，不要大段复制。

### `P0_RECHECK_ACCEPTANCE.md`

写清：

- P0 rows 总数是否为 19。
- 每种 decision 的数量。
- 还有多少 `source_insufficient / wrong_framework / block_from_student_body`。
- 是否生成 Word/PDF：必须写 `no`。
- 是否授权终稿：必须写 `no`。

现在开始。先写 `PROGRESS.md` 启动段，然后逐条回源，最后再写 acceptance。
