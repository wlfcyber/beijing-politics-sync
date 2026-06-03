# Blocked / Boundary 说明

本文件配合 `COVERAGE_MATRIX.csv` 与 `framework_node_matrix.csv` 阅读。本 B 线本轮把不进 student body 的条目分为两类：

- `blocked`：要进 body，但缺关键证据（题面、答案、细则、OCR、页图、模块边界、选项或答案源）；
- `boundary / excluded`：本身不进 student body（思维选择题、B-compilation、B-choice-signal 索引、不在本书范围）。

## 一、blocked 条目(1 条)

### B01. Q0030 — 2024北京高考 19(2)

- 缺什么: 缺正式细则/评标/阅卷材料；本机 run 内没有官方评分来源。本 run `00_control/QUESTION_COVERAGE_MATRIX.csv` 标 `evidence_level=missing`。
- 不进 body 的原因: 按 hard-rule notebook 第二条与第二十二条，普通参考答案不得冒充正式细则；A-formal 等级仅限正式细则、评标、阅卷总结或用户确认可用的评分材料。
- 解锁条件: 用户提供 2024 北京高考 19(2) 的官方评分细则、阅卷总结或评标资料；或用户明确授权将某教师版答案/讲评作为 A-support。
- 暂行处理: B 线在 `COVERAGE_MATRIX.csv` 中标 `decision=blocked`，`handbook_target=excluded_or_boundary`，`blocked_reason=missing_official_rubric_for_2024_beijing_gaokao_q192`。

## 二、节点级 blocker(framework_node_matrix 已显式标出)

### B02. RE08 — 充要条件假言推理

- 缺什么: 本 run 题源池中没有发现独立的“充要条件假言推理”主题题。`RC-2024-DONGCHENG-1MO-Q8` 中有“当且仅当小孙选政治，小李选政治”的分支，但题目主问是复合假言推理链，不构成独立的充要条件假言主题题。
- 处理: framework_node_matrix 中 RE08 标 `required_status=blocked_no_question`，`body_count=0`，`representative_entries=N/A`。
- 解锁条件: 由 Codex 在融合阶段决定是否合并入“假言推理/复合”或单独保留 blocker；如需开题，应在源材料中找“当且仅当……才……”句式独立主题题。

### B03. RE04 — 联言判断与联言推理

- 缺什么: 本 run 题源池没有单纯的“联言判断与联言推理”主条目。`RC-2024-DONGCHENG-1MO-Q8` 等复合推理选择题中含联言段，但不构成独立主题题。
- 处理: framework_node_matrix 中 RE04 标 `required_status=blocked_no_question`，`body_count=0`，`index_count=1`(以 RC-2024-DONGCHENG-1MO-Q8 作辅助索引)。
- 解锁条件: 由 Codex 决定是否在概念/判断章节合并写入或单列 blocker；如需开题，可在源材料中找“……并且……”结构独立题。

## 三、boundary / excluded 汇总(共 33 条，含 30 excluded + 3 index)

详见 `suite_reports/_boundary_excluded.md`。简表：

- 30 excluded：22 思维选择题(user scope) + 2 通州期末 choice_trap + 1 B-compilation(Q0070) + 其余按节点理由排除。
- 3 index：Q0123/Q0137/Q0138 三条 B-choice-signal 推理选择题，作为 audit 字段保留但不进 student body；详 `entries/reasoning_choice.jsonl` 中带 `-INDEX` 后缀的三条。

## 四、低证据等级 body(已在 body 中显式标出 evidence_level，不算 blocker)

下列条目 evidence_level 低于 A-formal，但 B 线本轮判 body，标 evidence_level 提示 Codex 融合时再评估：

- Q0028 / `RC-2025-FENGTAI-FINAL-Q9` — B-choice-signal 占位 body：题面/选项以原卷为准，B 线本轮未补全选项原文，留 fusion_candidates 列 `append_choice_wrong_option_reason` 给 Codex。
- Q0033 / `RC-2026-SHUNYI-1MO-Q4` — B-choice-signal body：B 线已写完整选项与逐项错因。
- Q0065 — 2024石景山一模 19(3) A-support：思维主观题，B 线 COVERAGE 标 body，但保留 A-support 标记。
- Q0069 — 2024门头沟一模 20 B-compilation：本 run 上一轮已用页图锁定题面与答案，B 线 COVERAGE 标 body 但 evidence_level 保留 B-compilation；Codex 融合时若不接受 B-compilation 进入 student body，可降级为 boundary。

## 五、后续 B 线轮次的建议优先级

如果 Codex 在融合阶段需要请 B 线再补 entry，建议优先级：

1. P1：RE08 充要条件假言独立主题题（如能在源材料定位）。
2. P1：RE04 联言推理独立主题题。
3. P2：思维“迁移和想象”独立 entry（如需独立节点）。
4. P2：A-formal 等级的相容选言、不相容选言更多条目以加厚 RE05。
5. P3：B-choice-signal 推理选择题改写为完整选项+错因（Q0028/Q0033/Q0123/Q0137/Q0138）。
