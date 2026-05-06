# Batch 03 Merge Register Updates

Status: `candidate_with_fixes`

Inputs:

- `codex_lane/agents/worker/worker_batch03_entries.md`
- `codex_lane/agents/worker/worker_batch03_source_notes.csv`
- `02_extraction/codex_evidence_cards/batch03_2026西城期末_Q20_evidence_card.md`
- `fusion/scoring_atom_table_batch03.csv`
- `codex_lane/agents/patcher/patcher_batch03_review.md`
- `codex_lane/agents/governor/governor_batch03_gate.md`

## Gate Result

Batch03 may enter fusion as a candidate-with-fixes set. It is still not a student final, not Word/PDF, not coverage closed, and not FINAL_ACCEPTANCE.

The scoring source is the formal scoring PDF visual read only. Teacher-paper page 8 is prompt/material support and is intentionally excluded from `source_ledger_refs` in the main Batch03 atom table.

## New / Updated Merge Groups

### M01 和平与发展仍是时代主题

Add variant:

- 2026西城期末 Q20: `和平发展合作共赢是时代潮流 / 非传统安全威胁`

Counting rule:

- Angle 2 is `4选3`; this is an optional reason-slot variant, not mandatory frequency.
- `非传统安全威胁` is not split into a second frequency from this question.

### M18 共同利益是国家合作的基础

Add source:

- 2026西城期末 Q20: `共同利益`

Non-merge:

- Do not merge with `正确义利观`.
- Common interests explain why cooperation can happen; correct义利观 explains China's value orientation in cooperation.

### M22 中国全球治理理念与价值取向

Core wording:

- `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 践行真正的多边主义 / 坚持互利共赢`

Main bucket:

- `中国`

Cross-reference:

- `政治多极化`
- `联合国`

Counting rule:

- These six expressions are one same-slot scoring variant group in 2026西城期末 Q20.
- They may update expression accumulation under related China-concept groups, but the source counts once as one scoring slot.

### M23 中国参与全球治理的责任与义务

Add:

- `积极参与全球气候治理，做全球气候治理的建设者、引领者和负责任大国`
- `自觉履行国际义务 / 遵循国际法 / 承担国际责任`

Boundary:

- The first is climate-governance role language and needs NDC / global climate governance trigger.
- The second is international-duty language and remains separate from the China-concept slot.

### M04 / M19 联合国核心作用与全球治理体系

Add:

- `维护联合国的核心作用 / 完善全球治理体系`

Rule:

- Preserve `维护联合国的核心作用`.
- Do not flatten it into generic `多边主义` or ordinary international-organization language.

### M07 中国智慧、中国方案、中国力量

Add:

- 2026西城期末 Q20: `贡献中国智慧 / 中国力量`

Rule:

- This is an angle-three China-contribution result slot.
- It is not the same scoring slot as angle-two China concepts.

## Boundary-Only / Result-Only Items

### B03 绿色发展 / 新发展理念 / 有为政府 + 有效市场

Status: `boundary_practice_support_only`

- It is P0 in this question's scoring rule.
- It is cross-module practice support and does not enter 选必一 core-term frequency.
- Student-facing use is limited to this question's climate-governance answer sentence.

### R01 促进全球可持续发展 / 建设清洁世界

Status: `result_expression_only`

- It is P0 as an effect expression in this question.
- It does not become an independent high-frequency core from one occurrence.
- Keep it near China's climate-governance practice and result language.

## Explicit Non-Merges

| non_merge_id | Do Not Merge | Reason |
|---|---|---|
| NM11 | `共同利益` with `正确义利观` | Cooperation basis vs China's value orientation. |
| NM12 | `共商共建共享` in Q20 climate governance with all previous `共商共建共享` occurrences | Same wording can serve different scoring functions; this occurrence is inside one China-concept same slot. |
| NM13 | `维护联合国核心作用` with generic `多边主义` | The scoring rule names the UN core role and global governance体系. |
| NM14 | `促进全球可持续发展 / 建设清洁世界` as a standalone high-frequency core | In this question it is an effect sentence. |
| NM15 | Six China-concept variants inside angle two as separate points | They are same scoring-slot alternatives and count once. |
| NM16 | `绿色发展 / 有为政府 + 有效市场` with economic-globalization mechanism cores | It is climate-governance practice support, not trade/investment/factor-flow mechanism. |

## Still Forbidden

- Student final.
- Word/PDF.
- Coverage close.
- Frequency final.
- FINAL_ACCEPTANCE.
