# Batch04L 2026石景山一模 Patcher Review

time: 2026-05-04 CST
role: Codex A Patcher
cross_thread_guard: active
external_lane_outputs_used: no
student_doc_touched: no
fusion_files_touched: no
verdict: PASS_WITH_FIXES

## 读取范围

- `05_coverage/batch04L_shijingshan2026_candidate_questions.csv`
- `02_extraction/codex_extraction_logs/batch04L_shijingshan2026_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04L_shijingshan2026_prelim.csv`
- `fusion/merge_register_batch04L_shijingshan2026_updates.md`
- `SOURCE_LEDGER.csv` 中 2026石景山一模行
- `COVERAGE_MATRIX.csv` 中 2026石景山一模行
- 选必一 skill、`current-user-requirements.md`、`xuanbiyi-term-protocol.md`

## 总结论

Batch04L Q20 可以作为 guarded 候选进入下一门槛。证据来自官方答案及评分参考，规则是“任选两个关键词；每个关键词使用1个学科用语并合理分析得4分”，并带等级评分表；不是逐点细则。因此 `P0_scoring_reference_level_guarded` 和 `candidate_with_guard` 是必要边界，不能升级为稳定逐点频次。

当前 SJS26-01 至 SJS26-05 基本覆盖 `共同 / 开放 / 包容` 三个关键词下的可用学科角度，没有把人类命运共同体当万能帽，也没有把 Q21 的中国方案误收进 Q20 主链。但有两个下游修正点：`共商共建共享` 进入学生侧时必须绑定全球治理语境，且所有 Q20 条目必须保留 guarded level-scoring 边界。

## 必须修的点

1. SJS26-02 后缀与桶位 guard：当前 fusion core 写作 `共商共建共享`，merge register 说并入 global-governance-view core。下游学生稿或总表继承时，必须写成 `共商共建共享的全球治理观` 或明确标注为全球治理取向表达；不得写成裸 `共商共建共享理念`，更不得混成发展理念、发展格局或国内治理口号。

2. Q20 证据 guard：该题只能作为 `keyword/level-scoring guarded candidate`。下游不得把 SJS26-01 至 SJS26-05 写成五个固定逐点得分项，也不得把 HMC 写成每个关键词通用的收尾帽。

## 逐项复查

### 1. 共同 / 开放 / 包容的拆分

PASS。三类关键词与核心拆分基本清楚：

- `共同`：SJS26-01 落到 `维护共同利益`，解释亚太各方为何能合作；SJS26-02 落到 `共商共建共享`，解释如何把共同利益转化为治理行动。
- `开放`：SJS26-03 落到 `贸易和投资自由化便利化 / 区域经济一体化 / 开放型经济格局`，不是泛泛写开放。
- `包容`：SJS26-04 落到 `推动经济全球化更加包容、更可持续，更好惠及地区全体人民`，保留包容与可持续的题目写法。

SJS26-05 属角度列表中的可选升华，不应视为第四个关键词本体。

### 2. 共同利益与共商共建共享

PASS_WITH_SUFFIX_FIX。二者没有被混并成一个 atom：SJS26-01 放在 `理论`，SJS26-02 放在 `政治多极化`，功能不同。风险在于 SJS26-02 当前核心名偏短，若学生稿直接继承，容易变成裸口号。最小修法是下游统一用 `共商共建共享的全球治理观`，或在表述积累中写明它是全球治理取向，不是共同利益理论点。

### 3. 包容可持续与完整五词核心

PASS。SJS26-04 的 `boundary_note` 已写明“本批只给包容可持续表达，不改写成完整五词核心名称”。这符合合并规则：可以并入经济全球化方向家族，但本题新增表达应保留为 `更加包容、更可持续，更好惠及地区全体人民`，不能被改写成完整五词，也不能只剩 `经济全球化正确方向`。

### 4. 人类命运共同体

PASS。SJS26-05 标为 guarded optional expression，merge register 也写明“不能成为 universal hat”。当前没有把 HMC 强行套到共同、开放、包容每个关键词上。后续只可作为所选关键词分析完成后的可选升华，不可替代共同利益、自由化便利化、包容可持续等具体点。

### 5. Q21 中国方案边界

PASS。candidate 表、SOURCE_LEDGER、COVERAGE_MATRIX 均把 Q21 标为 composite boundary：生态环境法典综合等级题虽有中国智慧、中国方案示例，但不是选必一逐点细则。当前未入 fusion 原子，边界正确。

## 证据与边界

- Q20：`P0_scoring_reference_level_guarded`，官方答案及评分参考加等级表，不是逐点 rubric。
- Q16/Q17/Q18/Q19：均为非选必一模块边界，未进入主链。
- Q21：综合等级题边界，仅源穷尽记录，不提升频次。

## 学生稿污染风险

PASS_WITH_GUARD。fusion CSV 中存在 `evidence_level`、`source_boundary`、`promotion_status`、`source_ledger_refs` 等后台字段，merge register 也有 `candidate_with_guard` 等过程语；这些不得进入学生稿。当前答案句本身可读，但学生侧继承时需要去掉 `评分参考`、`level-scoring`、`candidate`、`guard`、source id、路径等审计语言。

## 后续继承提醒

- 学生版应呈现为“从共同、开放、包容中任选两个关键词，每个关键词用一个学科术语加材料分析”的结构。
- `共同利益` 和 `共商共建共享的全球治理观` 可同属“共同”关键词下的两个可选角度，但不能合并成一个核心。
- `包容、更可持续` 是本题高信息表达，只作经济全球化方向家族的表述积累。
- HMC 只作 guarded optional 升华，不作万能帽。
