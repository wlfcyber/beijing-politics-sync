# Claude Opus 4.7 V5.8 Final Gate Review Prompt

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Opus 4.7 终审复核者。

请只按本次 V5.8 输入包复核，不要沿用旧会话里 V5.2/V5.4/V5.7 的结论。旧结论只能作为对比背景，不能替代本次文件核查。

## 工作目录

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长`

## 本次输入包

目录：

`05_reasoner_packets/v5_8_gptpro_final_gate_packet_20260521`

压缩包：

`05_reasoner_packets/v5_8_gptpro_final_gate_packet_20260521.zip`

请优先读取：

1. `PACKET_README.md`
2. `00_prompt/PROMPT_FOR_GPTPRO_V5_8_FINAL_GATE_REVIEW_20260521.md`
3. `01_student_handbook/student_handbook_v5_8_candidate.md`
4. `02_review_history/claude_opus_v5_7_review.md`
5. `03_validation/question_by_question_framework_runs_v5_8_27core65guard.csv`
6. `03_validation/non_core_guardrails_v5_8.csv`
7. `03_validation/v5_8_candidate_preflight_check.md`
8. `03_validation/v5_8_claude_guarded_patch_report.md`
9. `04_evidence_baseline/merged_subjective_law_questions.csv`
10. `04_evidence_baseline/merged_material_atoms_subjective.csv`
11. `04_evidence_baseline/merged_ask_atoms_subjective.csv`
12. `04_evidence_baseline/merged_rubric_atoms_subjective.csv`
13. `04_evidence_baseline/candidate70_to_current65_delta_ledger.csv`
14. `04_evidence_baseline/candidate70_to_current65_delta_summary.md`

## 复核任务

请重点判断：

1. V5.8 是否真正修复你在 V5.7 终审中提出的 P1：核心题入口过宽，未遵守“一题一主卡，最多一辅卡”。
2. V5.8 是否仍有 P0：学生正文混入审计话、评分说明、题干设问、reference answer 标签、rubric atom 脏文本。
3. 27 道核心题是否能让聪明但零基础高三学生按“入口、材料触发、最小判断、必踩硬词、考场答案、易错刹车、迁移限制”接近满分。
4. 38 道非核心题是否被诚实降级为保分/边界/回源索引，且不会误导学生当作核心满分模板。
5. 4 道 reference_only 是否绝对没有支撑核心节点。
6. source-check / boundary / transfer / excluded_logic_boundary 的红线是否足够醒目。
7. 是否仍有必修三化、法考化、教材目录化风险。
8. 是否允许进入 Word/PDF 候选成稿阶段。

请抽测至少 12 题：

- 至少 7 道 27 核心题。
- 至少 5 道 38 非核心题，覆盖 source-check、low-frequency、reference-only、boundary、excluded logic。

## 输出要求

请把最终报告写入：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/06_open_observations/claude_opus_v5_8_final_gate_review_20260521.md`

报告必须包含：

1. 总裁定：PASS / CONDITIONAL_PASS / FAIL。
2. Word/PDF 候选门禁：YES / YES_WITH_GUARDS / NO。
3. P0/P1/P2 问题表。
4. 12 题抽测表，含 question_id、核心/非核心类型、得分风险、是否误升核心。
5. 对 V5.8 相比 V5.7 的修复确认。
6. 如果仍不允许成稿，列出必须修补的具体 question_id 和修补动作。
7. 如果允许成稿，列出成稿必须保留的封面限制、红线和教师提示。

请不要只在聊天里总结，必须写入指定文件。
