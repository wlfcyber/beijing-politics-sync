# GPT-5.5 Pro Phase04 Batch02 Fast Review Prompt

你是本项目的 GPT-5.5 Pro chief content reviewer / commander。请只评审当前 Phase04 Batch02，不要提前放行学生稿。

## 项目背景

- 项目：北京高考政治 选择性必修三《逻辑与思维》四线从0重跑。
- 工作目录：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`
- 目标形态：
  - 思维部分最终要完全模仿已成功的哲学宝典：`材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题`。
  - 推理部分最终要按题型归档：`题型 -> 规则口令 -> 常见陷阱 -> 同类真题 -> 解题动作`，并且所有题都要放入对应题型下面。
- 当前仍禁止：学生稿、Claude/Opus 成文化、Word/PDF、最终 PASS。

## 你上次给出的 Batch02 要求

你要求先执行：

1. 拆分 `L0_BLOCKED=236` 的真实类型。
2. formal patch `2026朝阳期中 Q12`。
3. full visual scan `2026丰台一模 042`。
4. answer-source recheck `2025海淀二模 Q12/Q13`，不得逻辑猜答案。
5. Lane B recheck `2024西城一模 Q11` XML textbox recovery。
6. scope decision `2025海淀期末 Q2`。
7. 然后才处理 Q14/Q15 和剩余 A-only batches。

## Batch02 已完成的文件

Codex A:

- `05_coverage/phase04_blocked_type_split.csv/md`
- `05_coverage/phase04_2026_chaoyang_q12_formal_patch.csv`
- `05_coverage/phase04_2026_fengtai_yimo_visual_suite_scan.csv`
- `05_coverage/phase04_2025_haidian_ermo_Q12_Q13_status.csv`
- `05_coverage/phase04_2024_xicheng_yimo_Q11_B_recheck.csv`
- `05_coverage/phase04_2025_haidian_qimo_Q2_scope_decision.md`
- `05_coverage/phase04_Aonly_batch02_queue.csv`
- `05_coverage/phase04_batch02_codex_visual_scope_repair_addendum.csv`

ClaudeCode Lane B:

- `claudecode_lane/phase04_batch02_laneB_results.csv`
- `claudecode_lane/phase04_batch02_laneB_results_normalized.csv`
- `claudecode_lane/phase04_batch02_fengtai_visual_recheck.csv/md`
- `claudecode_lane/phase04_batch02_haidian_q12q13_recheck.csv/md`
- `claudecode_lane/phase04_batch02_xicheng_q11_recheck.csv/md`
- `claudecode_lane/phase04_batch02_scope_and_upgrade_decisions.csv`
- `04_suite_reports/claudecode_suite_reports/phase04_batch02_visual_scope_repair_report.md`

Codex merge:

- `05_coverage/phase04_control_base_status_after_batch02.csv`
- `06_conflicts/phase04_batch02_codexA_laneB_reconciliation.csv/md`

## 结构自检

- ClaudeCode raw CSV 有 3 行列位偏移：Q14/Q15/Q4 的 `yes` 被写入前一字段，导致机械读取时误成 `can_enter_fusion=no`。
- Codex 保留 raw CSV，并根据 Lane B 报告、专项 CSV、stdout summary 生成 `phase04_batch02_laneB_results_normalized.csv`，只做字段归位，不改证据结论。
- normalized CSV 后：11 行全部 `can_enter_fusion=yes`，11 行全部 `can_enter_student_draft=no`。

## Batch02 合并结果

`phase04_control_base_status_after_batch02.csv`：

- total rows: 364
- `L4_LOCKED_FOR_FUSION`: 4
- `L3_A_PLUS_B_TARGET_CONFIRMED`: 13
- `L1_A_ONLY_PENDING_B_TARGET`: 112
- `L0_BLOCKED`: 235
- student-facing permission: still blocked for all rows

Batch02 新确认/升级 11 行到 L3 evidence fusion pool：

1. `Q-2026朝阳期中-12`：推理，B-choice-signal，answer B，相容选言判断/分类规则/矛盾律。
2. `Q-2026朝阳期中-14`：推理，B-choice-signal，answer B，不完全归纳/或然性。
3. `Q-2026朝阳期中-15`：推理，B-choice-signal，answer D，联言判断否定。
4. `Q-2026丰台一模-4`：思维，B-choice-signal，answer A，综合思维。
5. `Q-2026丰台一模-7`：思维，B-choice-signal，answer B，发散聚合 + 超前思维。
6. `Q-2026丰台一模-8`：推理，B-choice-signal，answer C，充分条件假言推理。
7. `Q-2026丰台一模-9`：推理，B-choice-signal，answer D，概念外延关系 + 联言判断。
8. `Q-2025海淀二模-12`：思维，B-choice-signal，answer D，超前思维/风险收益平衡。
9. `Q-2025海淀二模-13`：推理，B-choice-signal，answer C，三段论/选言判断。
10. `Q-2024西城一模-11`：推理，B-choice-signal，answer B，完全归纳推理。
11. `Q-2025海淀期末-2`：思维，B-choice-signal，answer C=②③，②场景迁移/联想思维，③辩证思维整体性；①扬弃是哲学诱惑项但为错误选项，不污染 scope。

## 唯一显式冲突

`Q-2024西城一模-11`：

- Codex A 早先写成 B=①④。
- ClaudeCode Lane B 从 `/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx` 的 DOCX XML textbox 独立恢复四个选项，确认：
  - A=①②
  - B=①③
  - C=②④
  - D=③④
- 025/026 两份答案/细则均确认 answer B。
- 所以正确 pairing 是 B=①③。后续 fusion 必须用 B=①③，并把 Codex A 原错误作为纠错记录保留。

## 本轮请你裁决

请给出明确 verdict，优先使用以下之一：

- `REPAIR_BATCH02`: Batch02 仍有硬伤，必须先补。
- `GO_TO_BATCH03_AONLY_QUEUE`: Batch02 可以作为 targeted visual/scope repair 通过，允许进入剩余 A-only / L1 队列分批复核，但仍禁止学生稿、Opus、Word/PDF、PASS。
- `GO_TO_EVIDENCE_FUSION_ARCHIVE_ONLY`: 可以开始把 L3/L4 证据池写入同类题型 archive，但仍不得学生稿。

请重点检查：

1. 你是否接受 normalized CSV 作为机械合并输入？如果不接受，要怎么修。
2. 11 个 L3 新确认是否有哪个不该进 evidence fusion pool。
3. `2024西城一模 Q11` 是否应保留为 “can_enter_fusion=yes but with corrected pairing B=①③”。
4. 下一步应先做 remaining A-only queue，还是先把现在 17 个 L3/L4 evidence rows 写成 archive skeleton。
5. 任何会影响最终宝典质量的硬性风险。

请用短而明确的审稿意见返回：verdict、must_fix、allowed_next、blocked、notes。
