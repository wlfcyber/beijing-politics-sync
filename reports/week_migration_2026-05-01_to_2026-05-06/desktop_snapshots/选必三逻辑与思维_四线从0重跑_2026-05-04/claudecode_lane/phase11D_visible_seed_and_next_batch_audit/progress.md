# Phase 11D Visible-Window ClaudeCode Progress (T1)

模式：T1 Terminal ClaudeCode 可见窗口；Opus 4.7；非 `claude -p` 后台。
日期：2026-05-05。
工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`。

## 任务来源

`08_review/claudecode_phase11D_visible_seed_next_batch_prompt.md` 派发的四项任务（Task A 种子审稿；Task B 下一批候选；Task C 可选样本改写；Task D 进度与状态）。

## 已读文件（按 prompt 13 项 Reading）

1. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. `00_control/CLAUDECODE_THREAD_ROUTING_2026-05-05.md`
6. `claudecode_lane/phase11C_bad_word_content_audit_visible/four_element_gold_contract.md`
7. `claudecode_lane/phase11C_bad_word_content_audit_visible/next_rebuild_plan.md`
8. `09_student_draft/phase11D_seed_source_verified_04_REVIEW_ONLY.md`
9. `08_review/phase11D_seed_source_ledger.csv`
10. `08_review/phase11D_four_element_gate/phase11D_seed_source_verified_04_REVIEW_ONLY_four_element_gate.md`
11. `09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`
12. `09_student_draft/phase10_5_source_repair_priority_queue.md`
13. `09_student_draft/phase11B_batch01_student_body_30_REVIEW_ONLY.md`

## 量化扫描

- 8 条种子稿全文 grep 禁止短语集（`卷面要把|先写|要写|本题要求|采分点|细则要求|落到|v7漏了|关键词最稳|因此做选择题时先圈材料|先翻译逻辑结构|A-formal|B-choice-signal|参考答案|评标|可从.{0,15}角度作答|本题需要|设问要求|pass|yes|filled|correct_option_chain`）→ 命中 0 处。
- 8 条种子稿的设问字段没有出现 Phase11C 三类模板假设问。
- 多节点同题：本批种子稿 8 条均为单节点首发，没有同题复制。

## 已写文件

`claudecode_lane/phase11D_visible_seed_and_next_batch_audit/`

| 文件 | 性质 | 主要内容 |
|---|---|---|
| `phase11D_seed_audit_matrix.csv` | 矩阵 | 8 行；列 entry_title, entry_type, material_trigger, question_prompt, why_logic, answer_landing, choice_trap, boundary, student_cleanliness, verdict, must_fix, should_fix；verdict 全员 `PASS_FOR_GPT_REVIEW_ONLY` |
| `phase11D_seed_audit_report.md` | 中文报告 | 总裁定 `PASS_SEED_FOR_GPT_REVIEW_ONLY`；逐条 should_fix；学生稿干净度 + 模块边界 + Phase11A/11B 关系 + 下一步建议 |
| `phase11D_next_batch_candidate_queue.csv` | 队列 | 10 个晋级候选 + 7 个 do_not_promote；列 rank, question_id, title, type, priority_reason, source_stability, expected_four_element_risk, do_not_promote_reason_if_any |
| `phase11D_next_batch_rewrite_plan.md` | 计划 | 10 行改写顺序 + 不晋级清单 + 工序 + 风险提示 + VSCode lane 隔离提示 |
| `phase11D_next_batch_sample_rewrites_REVIEW_ONLY.md` | 样本 | 5 个 review-only 四要件样本（Rank 1/2/3/7/9）；设问字段全部 `BLOCKED_NEEDS_SOURCE_FULL_PROMPT` 等 Codex 源核回填 |
| `phase11D_visible_status.md` | 状态 | 模式、Routing、闸口、Hard Compliance |
| `progress.md` | 进度 | 本文件 |

## 未做的事（合规边界）

- 没有改 `09_student_draft/`、`outputs/`、`09_delivery/`、`codex_lane/`、`claudecode_lane/vscode_lane_phase11C/`。
- 没有生成 `.docx` / `.pdf`。
- 没有写 `final` / `终稿` / `最终稿` / `PASS` / `宝典成品`。
- 没有触动 P0 PROTECTED HOLD（Q-2026顺义一模-3、Q-2025海淀二模-12、Q-2024西城一模-11、Q-2025海淀二模-13）；
- 没有触动 HS02 / Q-2025海淀二模-20 视觉锁；
- 没有触动 P4 / P5 reasoning-form recheck pending 条目；
- 没有把 2026 石景山期末整套引入。

## 闸口

- `phase11D_seed_audit_t1_visible_window_done = TRUE`
- `phase11D_seed_merge_to_student_draft = NOT_AUTHORIZED`
- `phase11D_next_batch_proposed = AWAITING_USER_OR_CODEX_SOURCE_VERIFICATION_AND_GPT_REVIEW`
- `gpt55_content_review = NOT_RUN`
- `opus47_text_pass = NOT_RUN`
- `word_generation = BLOCKED_UNTIL_PHASE11F_PASS`

## 与 phase11C 的衔接

- 本 phase 严格沿用 `four_element_gold_contract.md` 与 `next_rebuild_plan.md`。
- 本 phase 输出本身**不构成** Phase11D 学生稿正文；正文化由 Codex 在源核 + GPT v1 + Opus + GPT v2 + Governor + Confucius 全员 PASS 后自行落盘。
