# Codex A Governor - Batch04A Haidian Prelim Fusion Gate

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

本轮性质：Batch04A 海淀预融合门禁。只判断 `E01-E04` 是否可进入 `candidate_with_fixes`，以及 `E-B01/B02/B03` 是否必须保持 boundary/reference。不得放行学生稿、Word/PDF、final、FINAL_ACCEPTANCE、coverage close。

## 读取文件

- `fusion/scoring_atom_table_batch04A_haidian_prelim.csv`
- `fusion/merge_register_batch04A_haidian_prelim.md`
- `codex_lane/agents/worker/worker_batch04A_haidian_entries.md`
- `codex_lane/agents/patcher/patcher_batch04A_source_triage_precheck.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`

## 结论

`PASS_WITH_GUARD`

允许：
- `ATOM-E01` 至 `ATOM-E04` 进入 `candidate_with_fixes`。
- 仅允许作为融合候选继续给 Patcher/Governor/coverage 复核。

继续阻断：
- 学生稿改写或学生版发布。
- Word/PDF/DOCX 生成。
- final / FINAL_ACCEPTANCE。
- coverage close。
- 把 boundary/reference 行计入 P0 高频或主链闭合。

## Atom 门禁判定

| atom | 判定 | Governor 裁决 |
|---|---|---|
| `ATOM-E01` | 可进 `candidate_with_fixes` | `2024海淀一模 Q18(1)` 有 `P0_formal_scoring_rule_text` 与题面支持，可并入贸易投资自由化便利化链；不得把同套 Q17 的松散开放表述并入本题。 |
| `ATOM-E02` | 可进 `candidate_with_fixes` | 同题 P0 细则可支撑“全球资源要素自由流动 / 两个市场两种资源”；必须保留“商品、服务、技术、资金、劳务”等高信息量表述，不压成空泛“开放”。 |
| `ATOM-E03` | 可进 `candidate_with_fixes`，但不得标 P0 | `2026海淀一模 Q20` 当前为 `P1_structured_answer_in_scoring_file_plus_P3_visual_prompt`；题面视觉支持已补，但来源仍不是纯正式分点评分细则。可作为制度型开放/两个市场两种资源的规则标准变体候选，证据标签必须保留。 |
| `ATOM-E04` | 可进 `candidate_with_fixes`，但不得标 P0 | 同题可作为“国际标准 / 标准共通 / 技术共享 -> 参与全球经济治理和规则制定”的材料特定变体候选；不得泛化成普通全球治理口号，也不得计为 P0 高频。 |

## Boundary / Reference 行

| atom | 必须状态 | Governor 裁决 |
|---|---|---|
| `ATOM-E-B01` | `boundary_only` | `2024海淀二模 Q18(1)` 只有开放述评宽泛答案角度，无详细评分子点；`时代主题 / 世界多极化 / 人类命运共同体 / 国际组织` 不得作为严格频次 atom。 |
| `ATOM-E-B02` | `reference_only` | `2025海淀一模 Q21(2)` 正向内容来自参考答案支持，P0 价值主要是负向评分警示；不得把开放战略、贸易自由化便利化、绿色/数字贸易等参考答案冒充正式细则。 |
| `ATOM-E-B03` | `reference_only` | `2026海淀期中 Q22` 未定位正式评分细则；全球治理倡议、联合国宪章、共商共建共享等只能作参考/迁移材料，找到正式给分口径前不得计频。 |

## 证据边界复核

- `SOURCE_LEDGER.csv` 与预融合表一致地保留了 `P0_formal_scoring_rule_text`、`P1_answer_in_scoring_file_needs_boundary`、`P1_reference_plus_P0_marking_caution`、`P1_structured_answer_in_scoring_file_plus_P3_visual_prompt`、`P3_paper_answer_doc_no_scoring_source` 等分层。
- `2024海淀一模 Q18(1)` 的细则源和题面源是同一题的不同证据层，只能计为一个题例。
- `2026海淀一模 Q20` 的结构化答案源和视觉题面源只能合并为一个候选题例；视觉题面不能把 P1 结构化答案升级成 P0 正式细则。
- `COVERAGE_MATRIX.csv` 中 Batch04A 行仍为 `not_started / not_started / not_started` 的下游状态，不得据本报告直接写成 coverage closed；后续若更新，只能更新到候选/复核中状态。

## 必须保留的修正条件

1. `ATOM-E01/E02` 进入融合时，`高水平对外开放 / 开放型经济` 只作背景或桥接，不作选必一主链独立频次。
2. `ATOM-E03/E04` 进入融合时，必须保留 `P1_structured_answer_in_scoring_file_plus_P3_visual_prompt`，不得改写为 `P0_formal_scoring_rule`。
3. `ATOM-E-B01/B02/B03` 只能留在 boundary/reference/transfer 池，不得进入主表频次。
4. `2024海淀一模 Q18` 与 `Q18(1)` 的题号写法需在后续 coverage 回填中统一，避免同题拆成两条。
5. 普通参考答案、纸面答案、开放述评答案、负向评分警示均不得冒充正式细则。

## 禁止动作

- 禁止编辑或生成学生稿。
- 禁止生成 Word/PDF/DOCX。
- 禁止宣布 final 或写 `FINAL_ACCEPTANCE`。
- 禁止关闭 coverage。
- 禁止把 `candidate_with_fixes` 解释为稳定主表或终稿闭合。

## Governor 最终判定

`ATOM-E01_TO_E04: PASS_TO_CANDIDATE_WITH_FIXES`

`ATOM-E-B01: BOUNDARY_ONLY`

`ATOM-E-B02: REFERENCE_ONLY`

`ATOM-E-B03: REFERENCE_ONLY`

`STUDENT_DRAFT: BLOCK`

`WORD_PDF_DELIVERY: BLOCK`

`FINAL_ACCEPTANCE: BLOCK`

`COVERAGE_CLOSE: BLOCK`
