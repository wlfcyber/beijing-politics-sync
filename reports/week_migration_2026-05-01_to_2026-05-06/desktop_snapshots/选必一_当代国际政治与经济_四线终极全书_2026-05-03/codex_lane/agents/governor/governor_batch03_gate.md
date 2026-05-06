# Codex A Governor Gate - Batch 03 2026西城期末 Q20

- Role: Governor / 条目级门禁
- Scope: Batch03, 2026西城期末 Q20
- Required files read: `02_extraction/codex_extraction_logs/batch03_source_locator_notes.md`; `codex_lane/agents/worker/worker_batch03_entries.md`; `codex_lane/agents/worker/worker_batch03_source_notes.csv`; `02_extraction/codex_evidence_cards/batch03_2026西城期末_Q20_evidence_card.md`; `fusion/scoring_atom_table_batch03_codex_prelim.csv`; `fusion/merge_register_batch03_codex_prelim.md`
- Local visual evidence additionally checked: `rubric_pdf_page_04.png`; `rubric_pdf_page_05.png`; `teacher_pdf_page_08.png`
- Conclusion: `PASS_WITH_FIXES`

## Gate Decision

Batch03 may enter `fusion/scoring_atom_table_batch03` main table and Batch03 merge-register update only after the fixes below are applied. This is not a release gate for student final text.

The P0 evidence boundary is valid: Q20 scoring points are visible in the formal scoring PDF pages 4-5, and the teacher-paper page 8 only supports prompt/material recovery. The teacher-version reference answer must not be used as scoring authority.

## Required Fixes

1. Split source references in fusion atoms. In `fusion/scoring_atom_table_batch03_codex_prelim.csv`, several `source_ledger_refs` include `TEACHER_PDF_CURRENT`. The main table must separate:
   - scoring source: formal scoring PDF visual pages 4-5, `P0_formal_scoring_rule_visual`;
   - prompt/material support: teacher PDF page 8, `P3_prompt_support`.
   Teacher PDF must not appear as the scoring-source ref for any atom.
2. Resolve bucket conflict in favor of the evidence card / prelim fusion:
   - `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 践行真正的多边主义 / 坚持互利共赢` enters the main bucket `中国`, with `政治多极化/联合国` as cross-reference only.
   - Do not keep it as a standalone `政治多极化` main-row from this question.
3. `促进全球可持续发展 / 建设清洁世界` may enter only as a P0 result/effect expression under global climate-governance practice. It is not an independent high-frequency core and must not be promoted as a standalone reusable theory/political-multipolarity core from this single question.
4. `坚持绿色发展 / 新发展理念，有为政府 + 有效市场` is P0 in the scoring rule, but for 选必一 cumulative framework it is cross-module practice support. It may be retained in a boundary/practice-support note and answer context, not in the main 选必一 core-term fusion table.
5. Clean two worker trigger phrases before any external-review or student-facing draft is built: `不能只写` and `要落到` appear in material-trigger prose. They do not contaminate answer sentences, but they are not acceptable final teaching prose.

## Atom-Level Ruling

| Atom | Ruling | Frequency / Merge Rule |
|---|---|---|
| ATOM-D01 `建设者 / 引领者 / 做负责任的大国` | 可进融合 | Merge under 中国责任/全球气候治理角色. Count only with climate-governance trigger, not generic slogan. |
| ATOM-D02 `坚持绿色发展 / 新发展理念，有为政府 + 有效市场` | 只做边界记录 | 不进选必一主链；不得计入选必一核心术语频次。 |
| ATOM-D03 `和平发展合作共赢是时代潮流 / 非传统安全威胁` | 可进融合 | Angle 2 is 4选3; record as optional reason-slot variant, not mandatory frequency. Do not split non-traditional security into a second frequency. |
| ATOM-D04 `共同利益` | 可进融合 | Merge with cooperation-basis theory; do not merge with `正确义利观`. 4选3 optional, not mandatory frequency. |
| ATOM-D05 `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 践行真正的多边主义 / 坚持互利共赢` | 可进融合但须改主桶为中国 | Six expressions are one same-slot variant group; do not split into six atoms or six frequencies. Cross-reference political multipolarity only. |
| ATOM-D06 `自觉履行国际义务 / 遵循国际法 / 承担国际责任` | 可进融合 | Merge under 中国责任/国际义务. 4选3 optional, not mandatory frequency. |
| ATOM-D07 `促进全球可持续发展 / 建设清洁世界` | 可进融合为效果表达 | 不得作为独立高频核心；不得单独计入核心术语频次 unless later P0 rubrics repeat it as a reusable scoring core. |
| ATOM-D08 `维护联合国的核心作用 / 完善全球治理体系` | 可进融合 | Merge under 联合国核心作用/全球治理体系. Do not flatten into generic `多边主义` or all-international-organization language. |
| ATOM-D09 `贡献中国智慧 / 中国力量` | 可进融合 | Merge with 中国智慧/中国方案/中国力量 contribution group as climate-governance variant; avoid duplicate effect frequency with D07. |

## Evidence Boundary Checks

- P0 formal scoring PDF visual: PASS. The rendered rubric pages show Q20 scoring structure: angle 1 role/practice, angle 2 4选3 reasons, angle 3 effects.
- Teacher-version reference answer: PASS_WITH_FIX. Worker and evidence card do not use it as `细则位置`; prelim fusion metadata must still remove ambiguity caused by `TEACHER_PDF_CURRENT` in scoring refs.
- Worker vs total-control conflict: PASS_WITH_FIX. Main bucket should follow the total-control/evidence-card decision where China global-governance concepts belong under `中国`, not a separate `政治多极化` main row.
- Green-development boundary: PASS_WITH_FIX. It is a scoring-rule practice point for this question, but it overlaps 必修二/经济治理 language and must remain boundary/practice support in the 选必一 framework.
- Coverage / final delivery: BLOCKED. This gate does not close coverage and does not authorize final artifacts.

## Still Forbidden

- Do not generate student final Markdown / Word / PDF.
- Do not mark coverage close.
- Do not write or imply `FINAL_ACCEPTANCE`.
- Do not promote teacher-paper reference answer into scoring authority.
- Do not count angle 2 4选3 alternatives as four mandatory frequencies.
- Do not split D05 same-slot variants into multiple independent frequency rows.
- Do not count D02 or D07 as independent main-core frequency rows under current evidence.
