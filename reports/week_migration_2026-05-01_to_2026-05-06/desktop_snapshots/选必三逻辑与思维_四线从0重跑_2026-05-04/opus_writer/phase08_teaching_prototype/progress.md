# Phase08 Opus Teaching Prototype Progress (REVIEW ONLY)

- run_time: 2026-05-05 CST
- model: claude-opus-4-7 (max/adaptive thinking)
- prototype_status: review_only
- student_permission: no
- word_pdf_permission: no
- final_pass_permission: no
- input_freeze_rows: 29
- hold_rows_excluded: 45
- L0_rows_excluded: 288

## 已完成

1. 读取强制输入文件清单(共 10 项):
   - `MASTER_REQUIREMENTS.md`
   - `05_coverage/phase08_opus_prototype_input_freeze.csv`
   - `05_coverage/phase08_opus_prototype_input_freeze.md`
   - `05_coverage/phase07_opus_input_thinking_entries.csv` (+ `.md` 全文核对)
   - `05_coverage/phase07_opus_input_reasoning_entries.csv` (+ `.md` 全文核对)
   - `05_coverage/phase07_opus_input_cross_entries.csv`
   - `05_coverage/phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md`
   - `06_conflicts/phase07_laneB_warning_patch_freeze.md`
   - `08_review/gpt_phase_advice/phase_07_gpt55_digest.md`
   - `~/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`

2. 输出文件(全部按规范路径写入,review_only):
   - `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md`
   - `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv`
   - `07_student_prototype/phase08_opus_change_log.md`
   - `07_student_prototype/phase08_opus_change_log.csv`
   - `opus_writer/phase08_teaching_prototype/phase08_opus_boundary_compliance.md`
   - `opus_writer/phase08_teaching_prototype/progress.md` (本文件)

3. 行数 / 模块 / 状态自检全部通过:
   - 教学原型 CSV、change log CSV、教学原型 Markdown 三处均覆盖同一 29 行 question_id。
   - 模块分布:思维 13 / 推理 11 / 交叉 5,与冻结一致。
   - 状态分布:L4 = 4(`Q-2025海淀二模-20`、`Q-2025西城二模-16-2`、`Q-2025西城二模-16-3`、`Q-2026丰台一模-18-2`),L3_candidate = 25。
   - change log 全部 `change_type ∈ {wording_only, structure_only}`;sentinel 字段全部 `must_be_no`。

4. 硬样本自检全部通过(详见 `phase08_opus_boundary_compliance.md`):
   - `Q-2024西城一模-11`、`Q-2025海淀二模-12`、`Q-2025海淀二模-13` 均不在冻结 29 行,只作 ID 引用,不暴露答案。
   - `Q-2026顺义一模-3` 不进入推理原型,只在思维同类题列表里以 ID 出现。
   - `Q-2026丰台一模-18-2` 解题动作严格按 Phase07 patch freeze 表述保留;answer_locator `answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric` 不进入正文,只在审计行保留。

5. 禁用术语自检全部通过:
   - `source locator`、`lane`、`Governor`、`Confucius`、`packet`、`L3`、`L4`、`A-formal`、`A-support`、`B-choice-signal`、`/Users/`、`@L...`、`.pdf::`、`.pptx::`、`.docx::`、`.rtf::` 均未在 prototype 正文 / `generated_text` 字段中出现。

6. 双挂载自检全部通过:
   - 5 题交叉(`Q-2024朝阳二模-19-1`、`Q-2024朝阳二模-19-2`、`Q-2024朝阳期中-9`、`Q-2026顺义一模-19-1`、`Q-2026顺义一模-19-2`)主挂载推理 + 次挂载思维双段保留,未单挂。

## 未完成 / 不在本阶段授权

- 学生稿:blocked。
- Word/PDF:blocked。
- 最终 PASS、宝典成品:blocked。
- 全量 Lane B 重跑:不需要;但本原型完成后必须由 Lane B 审计。

## 下一步建议(交回总控)

- 由 Codex A 接收本 prototype,进行 verification。
- 由 Lane B 进行 prototype 审计(同源独立审核),交叉对比错位风险。
- 由 Governor / Confucius review-only gate 把关边界。
- 由 GPT-5.5 Pro 在 review-only 范围内做内容压力测试。
- 上述 gate 全部 PASS 之前,不进入学生稿、Word/PDF、最终 PASS。

## 本阶段未发起的动作(主动避免)

- 未新增任何题、未删除任何题。
- 未变更任何答案、配对、归类(包括 L3 升 L4)。
- 未将 hold 行(45 行)、L0 行(288 行)写入正文。
- 未读取 / 修改任何冻结输入文件。
- 未生成任何 `.docx`、`.pdf`、`outputs/` 文件。
- 未在 prototype 正文中暴露 lane / Governor / Confucius / packet / source locator / L3 / L4 / file path 等内部术语。
