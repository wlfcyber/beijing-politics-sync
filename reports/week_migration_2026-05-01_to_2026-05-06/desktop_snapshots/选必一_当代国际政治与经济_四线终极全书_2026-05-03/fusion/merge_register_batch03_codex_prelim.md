# Batch 03 Codex Prelim Merge Register

Status: `codex_local_pre_worker`

Input:

- `02_extraction/codex_extraction_logs/batch03_source_locator_notes.md`
- `02_extraction/codex_evidence_cards/batch03_2026西城期末_Q20_evidence_card.md`
- `fusion/scoring_atom_table_batch03_codex_prelim.csv`

This file is a Codex total-control pre-merge. Worker/Patcher/Governor review is still required before promotion into the main cumulative merge register.

## Updates Proposed

### M01 和平与发展仍是时代主题

Add variant:

- 2026西城期末 Q20: `和平发展合作共赢是时代潮流 / 非传统安全威胁`

Rule:

- It enters as one reason-slot variant from a 4-choose-3 scoring area.
- Do not count `非传统安全威胁` as a separate mandatory theory frequency from the same slot.

### M18 共同利益是国家合作的基础

Add source:

- 2026西城期末 Q20: `共同利益`, P0 visual scoring rule, one item inside angle-two 4-choose-3.

Non-merge:

- Still do not merge with `正确义利观`.

### M05 / M06 / M07 中国外交价值与贡献

Add same-slot variants:

- `命运共同体`
- `全人类共同价值`
- `正确义利观`
- `共商共建共享`
- `践行真正的多边主义`
- `坚持互利共赢`
- `贡献中国智慧 / 中国力量`

Counting rule:

- The first six expressions are variants inside one scoring-function slot in angle two, not six independent scoring points.
- `贡献中国智慧 / 中国力量` is a result point in angle three and may update China-contribution language.

### M04 / M19 联合国核心作用与全球治理体系

Add source:

- 2026西城期末 Q20: `维护联合国的核心作用 / 完善全球治理体系`, P0 visual scoring rule.

Rule:

- Preserve the phrase `维护联合国的核心作用`.
- Do not flatten it into generic `多边主义` or all-international-organization language.

### New Candidate: 全球气候治理中的中国责任与实践

Candidate core:

- `积极参与全球气候治理，做全球气候治理的建设者、引领者和负责任大国`

Related expressions:

- `自觉履行国际义务 / 遵循国际法 / 承担国际责任`
- `坚持绿色发展 / 新发展理念，有为政府 + 有效市场`

Boundary:

- This group is anchored in climate governance and NDC materials.
- `绿色发展 / 有为政府 + 有效市场` should be promoted with boundary wording because it overlaps non-选必一 content.

## Explicit Non-Merges

| non_merge_id | Do Not Merge | Reason |
|---|---|---|
| NM11 | `共同利益` with `正确义利观` | Cooperation basis vs China's value orientation. |
| NM12 | `共商共建共享` in Q20 climate governance with all previous `共商共建共享` occurrences | Same wording can serve different scoring functions; merge only with context note. |
| NM13 | `维护联合国核心作用` with generic `多边主义` | The scoring rule names the UN core role and global governance体系. |
| NM14 | `促进全球可持续发展 / 建设清洁世界` as a standalone high-frequency core | In this question it is an effect sentence; keep as result language unless additional rubrics support it. |
| NM15 | All six China-concept variants inside angle two as separate points | They are same scoring-slot alternatives. |

## Gate Needed

Before this can enter cumulative tables:

- Worker Batch03 output must be compared against this card.
- Patcher must check one-material-many-points and same-slot variant inflation.
- Governor must decide whether `绿色发展 / 有为政府 + 有效市场` can appear in student-facing 选必一 text and with what boundary wording.
