# Governor Gate - Batch04K 2026房山一模 Q19 预融合门禁

gate_file: `codex_lane/agents/governor/governor_gate_batch04K_fangshan2026.md`
gate_role: Codex A Governor
gate_scope: Batch04K 2026房山一模是否可进入候选融合门禁
final_gate: PASS_WITH_FIXES

## 读取文件

- `current requirements`
- `xuanbiyi protocol`
- `05_coverage/batch04K_fangshan2026_candidate_questions.csv`
- `02_extraction/codex_extraction_logs/batch04K_fangshan2026_manual_evidence_notes.md`
- `codex_lane/agents/worker/worker_batch04K_fangshan2026_triage.md`
- `fusion/scoring_atom_table_batch04K_fangshan2026_prelim.csv`
- `fusion/merge_register_batch04K_fangshan2026_updates.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`

## 总结论

Batch04K 可以进入候选融合门禁 / pre-A-B review，但只能以 `candidate_with_fixes` 或等价 guarded 状态推进；不得宣称 Batch04K 已闭合，不得放行学生稿、Word、PDF、final、FINAL_ACCEPTANCE 或 coverage close。

本轮不是 FAIL：Q19 的核心证据来自 `P0_formal_scoring_rule_docx`，原卷仅作为 `P3_visual_prompt_support` 用于完整设问与材料核读；未发现普通参考答案或试卷答案被冒充评分细则。Q16(1)、Q20 已保持边界记录，未暗中升入主链。

本轮不是无条件 PASS：P0 细则中存在一处分值结构解释待确认，即“四组候选机制”与细则备注中“1-5 每个2分、总分不超过6分”之间的关系仍需 Patcher/Governor 在 A/B closure 前显式闭合。该点不阻断候选融合，但阻断最终频次闭合与学生稿使用。

## 门禁检查

### 1. 参考/普通答案冒充细则

结论：未发现。

- Q19 使用来源为 `2026房山一模_Q19_SRC_7301f6d3c6e2`，在 source ledger 中标为 `P0_formal_scoring_rule_docx`。
- 原卷来源 `2026房山一模_Q19_SRC_0e98e571e5b0` 仅标为 `P3_visual_prompt_support`，用于确认题面、设问和材料，不承担评分细则身份。
- Q16(1)、Q20 即使出现开放、中国方案等表达，也分别保留为 `P0_mixed_module_boundary` 与 `P0_composite_boundary`，没有被拿来补强 Q19 评分频次。

### 2. Q19 分值结构

结论：可候选推进，但必须返修确认分值结构。

当前融合表列出的四个 atoms 有 P0 细则支撑：

- `ATOM-FS26-01`：超大规模市场优势、货物/服务贸易升级、要素自由流动、资源优化配置、贸易投资自由化便利化。
- `ATOM-FS26-02`：技术研发、企业竞争力、产业升级、融入全球产业分工和合作。
- `ATOM-FS26-03`：优化营商环境、吸引外商投资、引进来。
- `ATOM-FS26-04`：制度型开放、中国方案、国内国际两个市场两种资源联动效应。

但 manual notes 与 merge register 已共同记录一个未闭合点：细则备注中“1-5，每个2分，总分不超过6分”的范围需要复核。当前 Codex A 的解释是前三组机制最多6分，第四组中国方案侧另计2分，合计8分；该解释合理但尚不能当作最终闭合事实。

阻断项：在 A/B closure 或进入主融合表定频前，必须明确：

- 若 P0 细则确认为“前三组机制封顶6分 + 中国方案侧2分”，则 `FS26-01` 至 `FS26-04` 可继续按当前四组候选进入合并。
- 若 P0 细则实际表示全部候选点共同封顶6分，则必须调整 `FS26-04` 的计频身份或把四组关系改为同题内择点结构，不能按四个独立2分 atom 直接闭合。

### 3. 模块边界

结论：当前边界处理基本合格。

- Q16(1) 属经济与社会的因地制宜/地区发展题，虽然材料中可见开放相关语汇，但当前只作 boundary，不进入选必一主链。
- Q20 是综合探究/等级评分题，中国智慧、中国方案等表述只作世界意义示例，不构成独立选必一评分细则点。
- `ATOM-FS26-02` 的“产业升级”有必修二交叉风险，但当前落点绑定“全球产业分工和合作”，可作为经济全球化语境下候选，需在融合时保留边界说明。

### 4. 学生稿提前使用

结论：未发现放行。

- Coverage 对 Batch04K Q19 仍标记为 `batch04K_candidate_pre_ab_review`、`claudecode_pending`、`pending`，并注明“暂未入学生稿”。
- 本门禁继续阻断学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

### 5. 同类项过度抽象

结论：当前未过度抽象，但需继续 guard。

- 融合表保留了“货物/服务贸易升级、要素自由流动、贸易投资自由化便利化”等高信息量表述，未压缩成泛泛的“开放”。
- merge register 已说明不得与 Batch04H 门头沟同类项机械合并。Batch04K 的设问功能是“海南自贸港封关如何助力国际循环”，不同于 Batch04H 的“注入新动能/新活力”语境。
- `两个市场两种资源` 在本题中可作为“国内国际循环联动”语境下的中国方案侧表达，但不能脱离 Q19 scoring context 裸写为普适2分 atom。

## 可推进项

允许进入候选融合 / pre-A-B review 的 atom：

- `ATOM-FS26-01`：candidate_with_fixes
- `ATOM-FS26-02`：candidate_with_fixes
- `ATOM-FS26-03`：candidate_with_fixes
- `ATOM-FS26-04`：candidate_with_fixes，附分值结构 guard

仅保留边界记录：

- 2026房山一模 Q16(1)：经济与社会边界，不计入选必一主链频次。
- 2026房山一模 Q20：综合等级题边界，不计入独立选必一评分 atom。

不得计频 / 不得使用：

- 任何仅来自普通参考答案、试卷解析、模型意见的表述，不得升级为 P0 评分细则。
- 未闭合分值结构前，不得把四个 FS26 atoms 宣称为最终4个独立2分闭合点。
- 不得进入学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

## 必须返修项

1. 在 Patcher 或 A/B closure 前复核 P0 细则中“1-5 每个2分、总分不超过6分”的准确适用范围，并把结论写入 merge register 或冲突闭合文件。
2. 若复核后确认四组并非可独立计频，必须调整 `ATOM-FS26-04` 或全组结构的 promotion/status。
3. 保留 Q16(1)、Q20 boundary-only，不得用它们补足 Q19 或学生稿。
4. 继续标注 Batch04K 与 Batch04H 的同族不同功能关系，避免把“海南自贸港/开放”压成一个泛化模板。

## Governor 裁决

final_gate: PASS_WITH_FIXES

允许：Batch04K Q19 进入候选融合门禁 / pre-A-B review。

不允许：学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

硬性条件：分值结构歧义闭合前，Batch04K 不能进入最终频次闭合或学生版正文。
