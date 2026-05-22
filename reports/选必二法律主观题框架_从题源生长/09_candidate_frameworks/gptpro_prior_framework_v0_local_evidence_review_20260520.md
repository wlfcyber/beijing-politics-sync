# GPTPro Prior-Framework v0 Local Evidence Review

## Verdict

`CONDITIONAL_PASS_FOR_CANDIDATE_FRAMEWORK`

GPTPro 已按用户要求学习桌面先前框架的结构表达，并基于 STEP_29 65 题底座生成法律主观题框架 v0。该稿可进入本地压测，但不能直接升为最终框架或宝典。

## Evidence Baseline Checked

- Canonical question file: `04_merge_audit/merged_subjective_law_questions.csv`
- Rows: 65
- Evidence levels: 61 formal, 4 reference_only
- Missing: 0
- GPTPro output: `09_candidate_frameworks/gptpro_prior_framework_learned_legal_framework_v0_20260520.md`

## Capture Integrity

- 正确稿首行：`# 总结论`
- 正确稿大小：41782 bytes
- 旧误复制稿已备份：`tool_outputs/gptpro_wrong_previous_quality_review_clipboard_20260520.md`
- 旧误复制稿首行：`# 总判断`

## Positive Findings

1. 输出明确把先前框架限定为结构、表达、学生可启动性样本，没有把旧框架当法律证据。
2. 输出明确回到 `current_65_legal_evidence_compact.csv` 的 65 题，写明 61 formal、4 reference_only。
3. 输出明确说“本版 v0 先做框架，不做最终宝典”。
4. 输出把 reference_only 四题锁为参考区，不单独支撑核心节点。
5. 输出提出七个学生动作节点：一格一答、先判后证、切责成链、护创新、走救济、划边界、补价值。
6. 本地扫描显示 65 个 question_id 均至少以完整 ID 或短 ID 被覆盖；未发现 GPTPro 引入未知 CC 编号。

## Risks And Required Checks

1. GPTPro v0 是单边候选，不满足四线最终框架 gate；若继续严格流程，需要 Claude Opus 独立审查或交叉审查。
2. GPTPro v0 使用动作节点重组旧“一核二线三问四步五域”的精神，需压测确认没有退回旧脚手架。
3. N02“先判后证”和 N03“切责成链”存在交叉，必须逐题压测是否会导致学生只写表态、漏责任链。
4. N06“划边界”容易把 AI/治理类综合题误吸进核心，需重点压测 CC0276、CC0380、RECOVER_2026_西城_二模_18_3。
5. N07“补价值”需压测是否会必修三化，尤其意义题和典型案例价值题。
6. reference_only 四题 CC0040、CC0162、CC0311、CC0353 不得在后续宝典中写成核心证据。

## Next Gate

`STEP_65_LOCAL_PRESSURE_TEST_GPTPRO_V0`

用该 v0 回到 65 题逐题测试：每题是否能从动作节点启动，是否能匹配 rubric atoms，是否生成高三学生可写的答案句，是否避免必修三化和法考化。
