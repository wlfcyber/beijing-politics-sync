# PROMPT FOR CLAUDE COWORK — 选必二法律主观题全题完善审查

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Cowork E：全题完善审查者。

你的任务不是写框架，不是总结规律，不是生成代码本。你的任务是在已经通过 ClaudeCode patch verification 的 65 道核心主观题包上，继续做“证据完善、题目完善、原子完善、定位风险审查”。

## 最高规则

1. 只研究主观题，选择题全部忽略。
2. 本轮禁止输出框架、口诀、总图、宝典目录、候选框架。
3. 不得按教材目录重排题目。
4. 不得使用任何预设结构，包括“一核二线三问四步五域”“动作库”“故事卡”“法律关系路由”。
5. 不得把参考答案冒充评分细则。
6. 不得因为材料出现“法律”“法治”“权利”“责任”等词，就把必修三、经济、哲学、逻辑题强收进选必二。
7. 对 reference_only 题只能做辅助审查，不得升级为 formal，除非你在原始文件中找到明确评分细则、评标、阅卷报告或讲评明确给分口径。
8. 对 OCR、页码、题号、阶段、区县、证据等级有疑问的地方，一律写成风险项或待核查项，不要猜。
9. 如能直接调用桌面文件，请读取下面列出的本地路径；如不能直接读取，请基于上传/粘贴给你的同名文件工作，并在报告中标明限制。

## 本轮唯一有效输入包

项目根目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长`

修正后语料包：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/`

修正后 reasoner packet：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/`

可上传压缩包：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/reasoner_packet_suite_exhaustive_claudecode_corrected_20260519.zip`

ClaudeCode patch verification：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/claudecode_suite_exhaustion_audit_20260519/claudecode_patch_verification_report.md`

关键输入文件：

1. `merged_subjective_law_questions_for_reasoners_claudecode_corrected.csv`
2. `merged_material_atoms_subjective_for_reasoners_claudecode_corrected.csv`
3. `merged_ask_atoms_subjective_for_reasoners_claudecode_corrected.csv`
4. `merged_rubric_atoms_subjective_for_reasoners_claudecode_corrected.csv`
5. `suite_exhaustion_matrix_for_reasoners_claudecode_corrected.csv`
6. `boundary_mixed_or_blocked_cases_for_reasoners_claudecode_corrected.csv`
7. `REASONER_INPUT_PACKET_CLAUDECODE_CORRECTED.md`
8. `claudecode_suite_exhaustion_audit_report_for_reasoners.md`

## 当前已验证状态

ClaudeCode patch verification 已给出 `PATCH_VERIFICATION: PASS`。

当前语料统计：

- 核心主观题：65 道
- formal：61 道
- reference_only：4 道
- missing：0 道
- material atoms：541 条
- ask atoms：65 条
- rubric atoms：362 条
- rubric → material 反向引用断链：0
- 当前不允许再使用旧 53/56/66 行包；旧开放观察输出全部作废。

需要重点盯住的特殊项：

1. reference_only 四题：
   - `CC0040`
   - `CC0162`
   - `CC0311_2026_海淀_二模_18_2`
   - `CC0353_2026_西城_期末_17`
2. OCR/render 补回题：
   - `RECOVER_2026_朝阳_期末_18_1`
3. 期中/期末阶段修正过的题：
   - `CC0244_2026_东城_期末_18`
   - `CC0245_2026_东城_期末_18_2`
   - `CC0317_2026_海淀_期末_18`
   - `CC0318_2026_海淀_期末_18_2`
   - `CC0319_2026_海淀_期末_19`
   - `CC0353_2026_西城_期末_17`
   - `CC0364_2026_通州_期末_19_1`
4. 已从核心移出的边界题不得重新混入核心，除非你找到直接证据：
   - `CC0051_2024_海淀_期中_21_1`
   - `RECOVER_2024_顺义_二模_17`
5. 真正无选必二法律主观题的期中：
   - `2024-朝阳-期中`
   - `2024-海淀-期中`
   - `2026-朝阳-期中`
   - `2026-海淀-期中`

## 你的具体任务

请对 65 道核心主观题逐题做完善审查。不要只抽样。

### 一、题目层审查

对每道题检查：

1. `question_id` 是否稳定、无旧错名、无期中/期末错挂。
2. `year / district / exam_stage / question_no / sub_question_no` 是否自洽。
3. `full_question_text` 是否包含题干、材料、设问，不要缺关键句。
4. `material_text` 是否混入参考答案或细则。
5. `ask_text` 是否是主观设问，且是否明确要求《法律与生活》。
6. `answer_text / rubric_text` 是否匹配对应题号和小问。
7. `evidence_type / evidence_level` 是否保守准确。
8. `module_boundary_risk` 是否准确标注。
9. `source_locator` 是否足够让人回源。

### 二、材料原子审查

对所有 material atoms 检查：

1. 是否遗漏会触发细则得分的关键材料事实。
2. 是否把多个不同事实压成过粗的一条。
3. 是否把无关背景当成核心法律触发点。
4. 是否把答案、细则、解释混进材料原子。
5. `legal_signal_if_any` 是否能帮助学生把材料转成法律语言。
6. `possible_relevance_to_answer` 是否过度推断。

### 三、设问原子审查

对所有 ask atoms 检查：

1. `ask_function_plain` 是否准确。
2. 是否需要结合材料。
3. 是否要求行为评价、建议、意义、理由、程序路径或价值讨论。
4. `student_task_plain` 是否能让学生知道第一步该干什么。

### 四、细则原子审查

对所有 rubric atoms 检查：

1. 是否一句一拆，过长的要建议拆分。
2. 是否有漏拆的给分点。
3. `related_material_atom_ids` 是否准确，是否过度牵连无关材料。
4. `what_expression_is_rewarded` 是否贴近细则原文。
5. `what_judgment_student_must_make_before_writing` 是否具体。
6. `legal_knowledge_or_rule_if_explicit` 是否来自细则/答案文本，而不是你的法学常识。
7. `knowledge_material_value_type` 是否准确区分 knowledge / material / value / 混合。
8. `can_be_written_without_material` 是否准确。
9. reference_only 的 rubric atoms 是否被误写成 formal。

### 五、全套穷尽性复核

请基于 suite matrix 和 boundary 表确认：

1. 65 道核心题是否覆盖了应进入选必二法律主观题库的所有题。
2. 非核心套卷是否有明确理由。
3. 期中无题是否只限于真正无法律主观题的期中，不要扩大到其他套卷。
4. 是否仍存在可能漏掉的题、漏掉的小问、漏掉的细则页。
5. 是否需要回源 OCR 的高风险文件有哪些。

## 输出文件要求

请把结果写成以下文件内容。若你不能直接写本地文件，就在回答中按文件名分节输出，供 Codex 保存。

目标输出目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/claude_cowork_question_refinement_20260519/`

请输出：

1. `claude_cowork_question_refinement_report.md`
2. `claude_cowork_question_patch_suggestions.csv`
3. `claude_cowork_material_atom_patch_suggestions.csv`
4. `claude_cowork_ask_atom_patch_suggestions.csv`
5. `claude_cowork_rubric_atom_patch_suggestions.csv`
6. `claude_cowork_locator_evidence_risks.csv`
7. `claude_cowork_reference_only_review.csv`
8. `claude_cowork_ready_for_reasoner_decision.md`

### patch suggestion CSV 字段

`patch_id, target_file, target_id, question_id, patch_type, current_value, suggested_value, reason, evidence_level_impact, source_locator, must_fix_before_reasoner`

`patch_type` 只能使用：

- keep
- add
- delete
- update
- split
- merge
- downgrade
- promote_if_source_verified
- source_check_needed
- no_action

`must_fix_before_reasoner` 只能使用：

- yes
- no
- uncertain

### locator/evidence risk CSV 字段

`risk_id, question_id, risk_type, risk_description, affected_files_or_atoms, current_evidence_level, recommended_action, blocks_reasoner, source_locator`

`blocks_reasoner` 只能使用 `yes / no / uncertain`。

### reference_only review CSV 字段

`question_id, current_evidence_type, current_evidence_level, reason_for_reference_only, possible_upgrade_source, should_remain_reference_only, can_enter_weak_observation, cannot_support_core_framework_alone, notes`

## 最终判定

在 `claude_cowork_ready_for_reasoner_decision.md` 中必须给出：

`COWORK_VERDICT: PASS / CONDITIONAL_PASS / FAIL`

并回答：

1. 当前 65 题是否可以作为“全题完善后”的开放观察输入？
2. 哪些 patch 是送 GPT-5.5 Pro / Claude Opus 前必须修的？
3. 哪些 patch 是质量提升项，可以边归纳边保留风险？
4. 是否发现还可能漏掉的选必二法律主观题？
5. 是否发现 reference_only 被误升 formal？
6. 是否发现 formal 需要降级？
7. 是否发现期中/期末、区县、题号、小问错挂？
8. 是否允许 Codex 继续生成双模型开放观察输入包？

再次强调：本轮不许写框架。
