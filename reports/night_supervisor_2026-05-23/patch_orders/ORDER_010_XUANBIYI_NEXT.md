# ORDER_010_XUANBIYI_NEXT

状态：`ACTIVE`  
对象：选必一《当代国际政治与经济》严格终稿闭合  
当前基线状态：`DELIVERED_WITH_GOVERNANCE_GAPS`  
目标状态：`STRICT_FINAL_ACCEPTED`

## 总禁令

1. 不覆盖旧终稿，不直接改写 `06_final_handbook` 的既有文件。
2. 所有新产物先进入新的闭环目录，建议命名为：`12_batch015_strict_closure_2026-05-24`。
3. 不把普通参考答案、学生答案、泛化讲评冒充评分细则。
4. 不把 ClaudeCode 本地审查冒充 Claude Opus 外部复审。
5. 不把旧 GPT Pro/Claude Opus 结论自动套用到最新补丁。
6. 未完成 GPT Pro、Claude Opus、Governor、Confucius、Word/PDF/渲染 QA 前，不得写 `STRICT_FINAL_ACCEPTED`。

## 补丁命令

### CMD-01 建立闭环目录和清单

新建目录：`...\选必一_哲学宝典式重建_2026-05-16\12_batch015_strict_closure_2026-05-24`

必须生成：
   - `00_CONTROL_CARD.md`
   - `01_source_reconciliation_matrix.csv`
   - `02_patch_apply_matrix.csv`
   - `03_batch015_source_packets.md`
   - `04_claudecode_thick_draft.md`
   - `05_codex_adjudication.md`
   - `06_gpt_pro_fusion_capture.md`
   - `07_claude_opus_review_capture.md`
   - `08_governor_final_audit.md`
   - `09_confucius_student_test.md`
   - `10_delivery_manifest.md`

通过标准：每个文件必须有来源路径、题号、证据等级、处理结论和下一步状态。

### CMD-02 合入最新 ClaudeCode 严格补丁前先做矩阵

来源文件：`11_strict_final_rebuild_2026-05-23\05_claudecode_opus47\CLAUDECODE_STRICT_PATCH_ENTRIES.md`

动作：
   - 抽取所有 `INCLUDE_STRICT_MAIN` / 可合入条目。
   - 将覆盖队列新增条目和反合并单题重写条目分开登记。
   - 对每条写入 `02_patch_apply_matrix.csv`，列为：`patch_id, source_file, source_line, paper, question_no, bucket, core_point, evidence_level, target_location, apply_decision, blocker`。
   - 对 9 条 `DOWNGRADED_REFERENCE_ONLY` 单列为“只可迁移参考/附录，不进主表”。

通过标准：补丁进入终稿前，必须逐条可追踪；不能只说“已吸收 ClaudeCode 建议”。

### CMD-03 闭合 BATCH_015 第一优先级：2026 顺义二模 Q20

来源线索：
   - 父级外审摘要：顺义 Q20 必须进入 BATCH_015。
   - `06_final_handbook\2026二模丰台顺义复查纠偏.md` 已指出顺义 Q20 证据位于 `26顺义二模评标.doc`。
   - 最新风险日志仍有顺义题号/证据风险，必须统一。

动作：
   - 找到原卷题号、评标/细则原文、答案角度和现有宝典位置。
   - 核定究竟是 Q19 还是 Q20；若原卷和学生宝典编号不一致，写清映射。
   - 独立生成顺义二模 Q20 源包，不得直接写入旧终稿。
   - 至少核查这些要点是否入主链：共商共建共享/新型国际关系，独立自主和平外交政策，让经济全球化更有活力/世界经济发展的重要推动者。

通过标准：`03_batch015_source_packets.md` 中有原题、原评分依据、题号映射和入桶位置。

### CMD-04 闭合 BATCH_015 第二优先级：2026 丰台二模 Q22

来源线索：
   - Claude Opus 外审将丰台 Q22 列为必须复核候选。
   - 外审提示其有选必一迁移评分点，但未完成四线流程。

动作：
   - 回到丰台二模原卷、阅卷细则和讲评源文件。
   - 判断 Q22 是否为选必一主链题、跨模块题还是参考迁移题。
   - 若入主链，写出材料触发词、评分术语、易误区和可直接背诵模板。
   - 若不入主链，写明排除证据，不得静默跳过。

通过标准：丰台 Q22 的 `include/exclude/reference_only` 结论有源文依据。

### CMD-05 处理 BATCH_015 低优先但必须登记项

对象：
   - 2026 房山二模 Q21
   - 2026 丰台二模 Q20

动作：
   - 房山 Q21：核是否有稳定选必一评分点，若证据弱则作为候选或边界题。
   - 丰台 Q20：若只有普通答案或参考性表述，维持 `reference_only`，不得升入主表。

通过标准：两题在矩阵中不再是“待定空洞项”。

### CMD-06 追索 12 条 NEEDS_EVIDENCE

来源文件：`11_strict_final_rebuild_2026-05-23\05_claudecode_opus47\CLAUDECODE_COVERAGE_RISK_LOG.md`

必须逐条处理：
   - 2024 丰台一模 Q21
   - 2024 海淀期中 Q20
   - 2024 石景山一模 Q20
   - 2024 顺义二模 Q18
   - 2025 东城一模 Q21
   - 2025 东城期末 Q21
   - 2025 丰台期末 Q21
   - 2025 延庆一模 Q21
   - 2026 东城期中 Q20
   - 2026 石景山期中 Q19
   - 2026 顺义二模 Q20
   - 风险日志另点名的 2024 东城一模 Q16 漏队列项

动作：
   - 每题先查现有 `01_extracted_text`、`04_source_packets`、父级二模回填目录和原始清单。
   - 找不到评分细则时，结论只能是 `BLOCKED_SOURCE_BOUNDARY` 或 `reference_only`，不能强行编术语。
   - 找到细则后，补写为独立源包，再由 ClaudeCode 厚稿和 Codex 复核。

通过标准：所有 `NEEDS_EVIDENCE` 被改成 `INCLUDE_STRICT_MAIN`、`EXCLUDE_OTHER_MODULE`、`DOWNGRADED_REFERENCE_ONLY` 或 `BLOCKED_SOURCE_BOUNDARY`，不能保留裸 `NEEDS_EVIDENCE`。

### CMD-07 修正题号和年份错配

必须核定：
   - 2026 顺义一模 Q19/Q20
   - 2026 延庆一模 Q19(2)/Q20
   - 2025 丰台二模 Q21 9 分版/6 分版
   - 2024/2025 海淀期中 Q16

动作：
   - 每个错配项写入 `01_source_reconciliation_matrix.csv`。
   - 明确“原卷题号、答案题号、学生宝典题号、最终采用题号”。
   - 旧宝典中若存在错误题号，新候选稿只能用注释迁移，不能直接覆盖旧文件。

通过标准：最终导航版和学生版没有同一题两个题号的混乱引用。

### CMD-08 生成 ClaudeCode 独立厚稿

输入：
   - `03_batch015_source_packets.md`
   - `02_patch_apply_matrix.csv`
   - `01_source_reconciliation_matrix.csv`

要求：
   - ClaudeCode 必须输出每题七字段：题型/材料触发/评分术语/入桶/答题模板/错因/边界。
   - 必须把“普通参考答案”和“评分细则”分开标注。
   - 必须给出是否进入主表的明确结论。

通过标准：`04_claudecode_thick_draft.md` 可逐题回指源文件，不出现无源扩写。

### CMD-09 Codex 二次裁决

动作：
   - 逐条审查 ClaudeCode 厚稿。
   - 对每题给出 `ACCEPT`、`REWRITE`、`DOWNGRADE`、`EXCLUDE`、`BLOCKED`。
   - 对跨模块题，必须写清为什么属于选必一或为什么排除。

通过标准：`05_codex_adjudication.md` 中没有“看起来可用”式判断，只有带证据的裁决。

### CMD-10 GPT Pro 融合审查

输入：
   - Codex 裁决稿
   - ClaudeCode 厚稿
   - 最新学生候选稿
   - 覆盖矩阵

要求：
   - 保存真实 GPT Pro 审查记录到 `06_gpt_pro_fusion_capture.md`。
   - 必须让 GPT Pro 明确回答：是否全题覆盖、是否达到哲学宝典同级、哪些题仍挡住 strict final。

通过标准：不能只有转述；必须有真实外部模型输出记录和结论。

### CMD-11 Claude Opus 复审

输入同 CMD-10，另加 GPT Pro 结论。

要求：
   - 保存真实 Claude Opus 审查记录到 `07_claude_opus_review_capture.md`。
   - 必须让 Claude Opus 专门检查“聪明高三学生能否直接上手全对”。

通过标准：若 Claude Opus 仍给 `PASS_WITH_B15_REQUIRED` 或同义结论，不得升级。

### CMD-12 生成新候选交付，不覆盖旧版

动作：
   - 生成时间戳后缀的新学生版 Markdown。
   - 生成时间戳后缀的新导航版 Markdown。
   - 生成对应 Word 和 PDF。
   - 所有文件先放入 `12_batch015_strict_closure_2026-05-24\delivery`。

通过标准：新旧版本可并存，任何旧文件未被覆盖。

### CMD-13 Governor 终审

Governor 必查：
   - 覆盖矩阵是否 368 行全部闭合。
   - 12 条 `NEEDS_EVIDENCE` 是否全部消失或有硬边界结论。
   - BATCH_015 顺义 Q20 和丰台 Q22 是否处理。
   - 题号年份错配是否清零。
   - GPT Pro 和 Claude Opus 是否真实复审最新候选稿。
   - Word/PDF/渲染 QA 是否完成。

通过标准：`08_governor_final_audit.md` 只能写 `STRICT_FINAL_ACCEPTED` 或明确降级理由，不允许写模糊通过。

### CMD-14 Confucius 零基础学生测试

测试对象：
   - 顺义二模 Q20
   - 丰台二模 Q22
   - 2024 东城一模 Q16
   - 一个国际组织题
   - 一个经济全球化题
   - 一个中国外交/全球治理题

要求：
   - 用宝典作答，不借外部材料。
   - 检查是否能定位桶、抽术语、拼答案、避错。

通过标准：`09_confucius_student_test.md` 必须给出每题是否能全对、卡点在哪里、修补是否已回写候选稿。

### CMD-15 渲染与交付 QA

动作：
   - 对新 Word/PDF 做页面渲染抽检。
   - 检查目录、表格、长段落、题号、脚注/来源、跨页断裂。
   - 记录截图路径和问题修复记录。

通过标准：`10_delivery_manifest.md` 记录 Markdown、Word、PDF、截图、页数、文件大小和最终状态。

## 升级条件

只有同时满足以下条件，才允许把选必一状态改为 `STRICT_FINAL_ACCEPTED`：

1. 覆盖矩阵 368 行全部有闭合结论。
2. BATCH_015 顺义 Q20 完成入主链或有硬排除证据。
3. 丰台 Q22、房山 Q21、丰台 Q20 均有源文等级结论。
4. 12 条 `NEEDS_EVIDENCE` 清零。
5. 2024 东城一模 Q16 已追索并处理。
6. 题号/年份错配全部清零。
7. 最新候选稿经过 GPT Pro 和 Claude Opus 真实复审。
8. Governor 写出严格通过。
9. Confucius 测试证明聪明高三学生可直接上手。
10. 新 Markdown、Word、PDF 和渲染 QA 交付完成。
