# Batch04M Remaining Prelim Patcher Review

time: 2026-05-04
role: Codex A Patcher
student_doc_touched: no
fusion_csv_touched: no
coverage_or_source_ledger_touched: no

verdict: PASS_WITH_FIXES

## Read Scope

- `05_coverage/batch04M_remaining_candidates.csv`
- `02_extraction/codex_extraction_logs/batch04M_remaining_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04M_remaining_prelim.csv`
- `fusion/merge_register_batch04M_remaining_updates.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`

## Overall Judgment

Batch04M remaining prelim can continue, but only with guard fixes. The main scoring atoms generally preserve one-material-multiple-point structure, especially:

- 2024丰台一模 Q20: four guarded supply-chain/globalization chains are all present.
- 2025丰台期末 Q20: theory logic and value-meaning layers are separated.
- 2025延庆一模 Q20(2): era theme, globalization direction, multipolarity/national-interest chain, HMC chain are separated.
- 2025房山一模 Q18(2): open world economy chain and UN/HMC/global-governance chain are separated.
- 2025昌平二模 Q21: four significance chains are present.
- 2025石景山一模 Q17(2): four China/global-governance proposals are present.
- 2025顺义一模 Q20: project features, local value, China-side idea/image, world contribution are kept as capped groups.

No evidence supports promoting 2026丰台期末 Q20. It must remain blocked until a real scoring source is found.

## Required Fixes

### 1. 2026丰台期末 Q20 must remain hard blocked

Current candidate/manual/coverage correctly mark 2026丰台期末 Q20 as `blocked_prompt_only` / `prompt_found_current_scoring_missing`, and no atom is created in the prelim CSV. That is the right decision.

Risk: `SOURCE_LEDGER.csv` rows `2026丰台期末_Q20_SRC_SRC_45c50fff4444` and `2026丰台期末_Q20_SRC_SRC_371641aaa3a7` still show broad candidate labels such as `P0_candidate_scoring` / `P3_candidate_paper`, while the note says no current formal scoring rubric was found. Downstream must not read the `P0_candidate_scoring` label as permission to promote. The next ledger pass should retag or hard-override this as prompt-only/support-only until scoring is found.

### 2. Reference-answer / answer-chain guarded rows need stronger source labels

Several prelim rows are correctly guarded in substance, but their source labels can still mislead later merging:

- `2024石景山一模 Q19(2)` uses `P1_pptx_reference_answer_guarded`; keep it as expression accumulation only. It must not become P0 point frequency.
- `2024顺义二模 Q19(2)` uses `P0_answer_only_mixed_module_guarded`; because it is answer-only and mixed-module, it should remain guarded expression accumulation, not formal scoring.
- `2024丰台一模 Q20` uses level/aspect guidance and answer chains; the four chains can be retained, but not as fixed 2-point rubric rows.

Required downstream action: retain these as guarded candidates and avoid using them as independent high-confidence frequency evidence.

### 3. 2025昌平二模 Q21 is admissible only as no-explicit-book guarded

The guarded inclusion is acceptable. The prompt does not explicitly name《当代国际政治与经济》, but the scoring source contains recognizable 选必一 economic-globalization terms:

- `国内国际两个市场两种资源`
- `全球经济治理中的话语权和影响力`
- `更加开放、包容的全球经济格局`
- `经贸合作 / 营商环境`

Required boundary: all four `M-CP25EM-*` rows must keep `no_explicit_book_but_xuanbiyi_scoring_terms` or equivalent guard. They can support expression accumulation for 经济全球化 / 中国参与全球经济治理, but should not be counted as clean book-explicit P0 frequency.

### 4. Mixed-book practical-measure rows need boundary notes before student merge

`2025丰台一模 Q20` is a mixed `经济与社会 + 当代国际政治与经济` prompt. The four rows are supported by a formal scoring source, but several expressions are practical or domestic-policy measures:

- `优化营商环境`
- `国际职业资格认可 / 双向互认`
- `税费优惠 / 高新技术企业`

They may stay as answer-chain material for this question, but should not become standalone 选必一 textbook core rows. Downstream should keep them under trade/investment facilitation, service trade, talent opening, or open-economy support expressions.

### 5. Normalize `国际竞争的实质` bucket/cross-reference

The prelim CSV places `M-SY24EM-01` under `政治多极化`, while the merge register lists `国际竞争的实质` under `时代背景`. This is not blocking, but the global merge should choose one main bucket and use the other only as cross-reference. Recommended main bucket: `政治多极化`, with `时代背景` as context where needed.

## Same-Core Merge Check

Pass with the above fixes.

- Full globalization direction is preserved in `M-YQ25YM-02`; shorter variants such as `开放包容普惠`, `普惠包容`, and `更加开放、包容的全球经济格局` are not used to overwrite the full five-word core.
- `共商共建共享` is preserved as `共商共建共享的全球治理观` in `M-FT25QM-04` and `M-SJS25YM-01`; domestic `共建共治共享` is not mixed in.
- Full `相互尊重、公平正义、合作共赢的新型国际关系` is retained in `M-FT25QM-05`; bare `新型国际关系` is treated as weaker/partial where the source says so.
- `人类命运共同体` is not used as a universal hat; it appears in bounded source roles such as 中非命运共同体、区域合作、供应链合作, or capped choice groups.

## One-Material-Multiple-Point Check

No material-to-multiple-point leakage requiring block was found. The only caution is capped-choice handling:

- `M-SY25YM-03` and `M-SY25YM-04` should remain capped groups, because the source says 任意点给分/不超过上限. Do not split their internal options into separate frequency rows.
- `M-FT24YM-01..04` should remain four guarded aspects, not four fixed scoring frequencies.
- `M-CP25EM-01..04` can remain four guarded significance expressions, not a clean book-explicit rubric set.

## Blocked / Boundary Confirmation

- 2026丰台期末 Q20: BLOCKED until formal scoring is found.
- 2026海淀期末: no Xuanbiyi subjective promotion in this pass.
- 2024模块分类汇编: source-bundle boundary only.
- 2026石景山期末: remains excluded per user-confirmed boundary.

## Final Gate

`PASS_WITH_FIXES`: batch can proceed to B comparison / governor only if the guarded-source labels above are kept visible and 2026丰台期末 Q20 remains out of the atom table.

