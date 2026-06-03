# Claude Code B Independent Suite-Exhaustion Audit Prompt

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Code B：独立套卷穷尽审计者。

你不能默认相信 Codex 的 66 题核心包。你要独立读取 source manifest、原始题源、抽取文本和已渲染页面，审查是否仍然漏掉了选必二《法律与生活》主观题，是否误收了非法律题，是否把普通参考答案升级为评分细则，是否存在题号、页码、区县、考试阶段、细则匹配错误。

本轮任务非常窄：

- 只做套卷穷尽审计、查漏、查误收、查证据等级、查定位。
- 不写框架。
- 不总结规律。
- 不生成代码本。
- 不写宝典。
- 不分析选择题。
- 不沿用 Codex 的结论。

## 项目与输入路径

工作目录：

`/Users/wanglifei/Desktop/北京高考政治`

工程根目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长`

原始题源优先路径：

- `/Users/wanglifei/Desktop/2024模拟题`
- `/Users/wanglifei/Desktop/2025模拟题`
- `/Users/wanglifei/Desktop/2026模拟题`
- `/Users/wanglifei/GaokaoPolitics/2024各区模拟题`
- `/Users/wanglifei/GaokaoPolitics/2025各区模拟题`
- `/Users/wanglifei/GaokaoPolitics/2026各区模拟题`

当前 Codex 认为“套卷穷尽后”的核心包：

- `04_merge_audit/suite_exhaustive_20260519/merged_subjective_law_questions_suite_exhaustive.csv`
- `04_merge_audit/suite_exhaustive_20260519/merged_material_atoms_subjective_suite_exhaustive.csv`
- `04_merge_audit/suite_exhaustive_20260519/merged_ask_atoms_subjective_suite_exhaustive.csv`
- `04_merge_audit/suite_exhaustive_20260519/merged_rubric_atoms_subjective_suite_exhaustive.csv`
- `04_merge_audit/suite_exhaustive_20260519/suite_exhaustion_matrix.csv`
- `04_merge_audit/suite_exhaustive_20260519/boundary_mixed_or_blocked_cases.csv`
- `QUESTION_COVERAGE_MATRIX_SUITE_EXHAUSTIVE.csv`

基础 source manifest 与处理材料：

- `00_manifest/source_manifest.csv`
- `00_manifest/source_manifest.jsonl`
- `00_manifest/failed_files.csv`
- `00_manifest/processing_log.md`
- `00_manifest/extracted_text/`
- `00_manifest/rendered_pages/`

你要输出到：

`04_merge_audit/claudecode_suite_exhaustion_audit_20260519/`

## 用户当前质疑

用户明确质疑：

1. “为什么才 35 题，应该有六十多道题。”
2. “missing17 的都有哪些，期中考题可能没有法律题，别的应该都有。”
3. “你就不能确保你把每一套考题都吃干抹净了吗？然后再给 GPT Pro 和 Claude Opus 生成框架。”

Codex 后来声称已经从 53/56 修正到 66 个核心主观法律题，但这必须被你独立审计。你必须特别检查：

- 目前 66 题是否真的穷尽。
- 是否还存在非期中套卷无核心法律主观题但其实应有法律题。
- 是否有期中卷其实也有可入核心的法律主观题。
- 是否把 mixed/boundary 题排除过度。
- 是否把必修三、经济、哲学、逻辑题误收。
- 是否把 reference_only 当成 formal。

## 审计硬规则

1. 本工程只研究主观题，选择题不进入本次审计结论。
2. 不能因为题面出现“法律”“权利”“责任”“法治”就收为选必二。
3. 只有当设问、材料、答案或细则确实体现选必二《法律与生活》的法律规则/制度/权利义务/责任救济/程序/合同/侵权/婚姻家庭/继承/劳动争议/消费者权益/知识产权/诉讼仲裁调解等，才可判入核心或候选。
4. 如果题目主要是必修三法治建设、经济、哲学、逻辑，必须标排除或 mixed，不得强收。
5. 普通参考答案不得冒充评分细则。
6. formal 只给正式评分细则、阅卷细则、评标、阅卷报告、讲评中明确给分口径。
7. reference_only 只可辅助理解，不能单独支撑框架核心。
8. missing 不得进入 GPT/Claude 框架归纳。
9. 扫描 PDF、图片、无文本层、OCR 不确定，必须标 source_or_ocr_blocker，不得默认为没有法律题。
10. 审计结论必须给出原始文件、页码或定位、题号、小问号、理由。

## 独立审计任务

### A. 重建套卷清单

从 source_manifest 和原始题源目录重建 2024、2025、2026 北京各区政治套卷清单。

每套卷至少判定：

- year
- district
- exam_stage
- paper files
- answer/rubric/evaluation files
- lecture/report files if any
- source_file_ids
- whether paper and scoring source are readable

### B. 逐套卷审查是否有核心法律主观题

对每套卷判断：

- `core_law_question_present_and_in_66`
- `missed_core_law_question`
- `mixed_boundary_only`
- `confirmed_no_law_subjective`
- `source_blocked_or_ocr_gap`
- `stage_mapping_conflict`
- `false_positive_in_66`

你必须尤其列出“非期中且 Codex 当前没有核心法律主观题”的所有套卷，并逐套回源说明为什么确实没有、为什么 blocked、或为什么漏题。

### C. 审计 66 个核心题是否误收

读取：

`04_merge_audit/suite_exhaustive_20260519/merged_subjective_law_questions_suite_exhaustive.csv`

逐题审查：

- 是否真为主观题。
- 是否真为选必二《法律与生活》。
- question_no/sub_question_no 是否正确。
- year/district/exam_stage 是否正确。
- paper_page/source_locator 是否可信。
- answer_file/rubric_file 是否匹配该题。
- evidence_type/evidence_level 是否保守。
- 是否存在 reference_only 被升级为 formal。
- 是否存在答案串页、细则串题、材料串题。

### D. 复核 boundary/blocked 题

读取：

`04_merge_audit/suite_exhaustive_20260519/boundary_mixed_or_blocked_cases.csv`

逐项判断：

- 是否应拆分出法律小问进入核心。
- 是否应继续作为 mixed/reference/blocker。
- 是否应删除为非法律题。
- 是否存在用户明确排除导致不能纳入的 source restriction。

### E. 核查“只有期中可能没有法律题”

单独生成一节：

`User claim check: only midterms may lack law questions`

内容必须包括：

- 当前所有非期中无核心法律题套卷列表。
- 这些套卷是否其实有漏题。
- 若没有漏题，为什么可确认没有选必二法律主观题。
- 若不能确认，阻塞原因是什么。
- 当前所有期中无核心法律题套卷列表。
- 期中卷中是否有可入核心的法律题或只是 mixed/reference。

## 必须输出的文件

全部写到：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/claudecode_suite_exhaustion_audit_20260519/`

文件清单：

1. `claudecode_suite_exhaustion_audit_report.md`
2. `claudecode_suite_exhaustion_matrix_review.csv`
3. `claudecode_missed_core_candidates.csv`
4. `claudecode_false_positive_in_66.csv`
5. `claudecode_boundary_case_review.csv`
6. `claudecode_evidence_level_or_locator_disagreements.csv`
7. `claudecode_no_law_suites_confirmed.csv`
8. `claudecode_source_or_ocr_blockers.csv`

### claudecode_suite_exhaustion_matrix_review.csv 字段

- suite_audit_id
- year
- district
- exam_stage
- codex_suite_status
- claudecode_suite_status
- codex_core_question_ids
- claudecode_core_question_ids_confirmed
- missed_core_candidate_ids
- false_positive_question_ids
- boundary_case_ids
- source_file_ids_checked
- paper_files_checked
- rubric_files_checked
- non_midterm_without_core
- midterm_without_core
- user_claim_assessment
- source_or_ocr_blocker
- decision
- reason
- source_locator

### claudecode_missed_core_candidates.csv 字段

- missed_candidate_id
- year
- district
- exam_stage
- question_no
- sub_question_no
- paper_file
- paper_page_or_locator
- full_question_text
- material_text
- ask_text
- answer_or_rubric_file
- answer_or_rubric_locator
- answer_or_rubric_text
- evidence_type
- evidence_level
- why_core_law_subjective
- why_codex_may_have_missed
- module_boundary_risk
- confidence
- required_action

### claudecode_false_positive_in_66.csv 字段

- question_id
- year
- district
- exam_stage
- question_no
- reason_false_positive_or_overincluded
- likely_true_module
- evidence_issue
- recommended_action
- source_locator

### claudecode_boundary_case_review.csv 字段

- boundary_case_id
- codex_boundary_status
- claudecode_decision
- should_enter_core
- should_split_legal_subquestion
- evidence_level
- reason
- source_locator

### claudecode_evidence_level_or_locator_disagreements.csv 字段

- question_id
- issue_type
- codex_value
- claudecode_value
- conservative_decision
- reason
- source_locator

### claudecode_no_law_suites_confirmed.csv 字段

- suite_id
- year
- district
- exam_stage
- is_midterm
- files_checked
- subjectives_seen
- why_no_core_law_subjective
- remaining_risk
- source_locator

### claudecode_source_or_ocr_blockers.csv 字段

- blocker_id
- year
- district
- exam_stage
- file_path
- file_id_if_known
- blocker_type
- effect_on_exhaustion
- suggested_recovery_action

## 最终报告必须回答

`claudecode_suite_exhaustion_audit_report.md` 必须以以下裁决开头：

- `FINAL_JUDGMENT: PASS`：未发现漏题、误收或会影响 66 题核心包的证据问题；只剩可说明的边界/blocked。
- `FINAL_JUDGMENT: CONDITIONAL_PASS`：主体 66 题基本可用，但存在少量需回源/降级/拆分的条件项；不能直接交 GPT/Claude 生成最终框架，需先修补。
- `FINAL_JUDGMENT: FAIL`：发现明显漏题、误收、证据等级错误或套卷未穷尽；不得把当前 66 题包交给 GPT/Claude 生成框架。

报告必须具体回答：

1. 当前 66 核心题是否穷尽？
2. 是否仍有漏掉的核心法律主观题？若有，列出 exact suite/question。
3. 是否有误收？若有，列出 exact question_id。
4. 是否有 reference_only 被升级为 formal？
5. 哪些题必须降级、拆分或删除？
6. 哪些套卷确认为无选必二法律主观题？
7. 哪些套卷仍有 OCR/source 阻塞，不能宣称穷尽？
8. “只有期中可能没有法律题，别的应该都有”这句话在当前题源下是否成立？
9. 当前是否允许把修正后的包交给 GPT-5.5 Pro 和 Claude Opus 做开放归纳？如果不允许，必须列出修补清单。

请直接写文件，不要只在终端回答。终端最后只简要输出你的 FINAL_JUDGMENT 和文件路径。
