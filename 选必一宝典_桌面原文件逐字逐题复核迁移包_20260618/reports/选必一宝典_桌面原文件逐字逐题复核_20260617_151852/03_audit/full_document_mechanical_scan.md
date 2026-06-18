# Full Document Mechanical Scan

- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- scan_type: mechanical structure only; not a source-content final audit

## Counts

- extracted_blocks: 6699
- question_entry_candidates: 561
- normalized_unique_questions: 127
- seeded_field_checks: 4488
- slice_001_field_checks_reviewed_by_codex_and_claudecode: 40
- additional_mechanical_rows_marked_structure_needs_fix: 1112

## Duplicate Concentration

Top repeated normalized questions:

| normalized question | entry count |
|---|---:|
| 2025朝阳期末Q21 | 20 |
| 2026朝阳一模Q20 | 15 |
| 2026朝阳期中Q17 | 14 |
| 2025丰台二模Q20 | 13 |
| 2026通州期末Q20 | 12 |

Full inventory:

- `03_audit/UNIQUE_QUESTION_INVENTORY.csv`

## Mechanical Finding

The current document structure uses:

- bucket headings
- `核心答题点：...`
- numbered question entries
- 【材料触发点】
- 【设问】
- 【为什么能想到】
- 【答案落点】
- 【同题组】

This structure does not independently expose the two highest-priority hard-rule fields:

- 【术语】 as scoring-rule original phrase(s)
- 【细则位置】 as suite + question + scoring section + exact point + score/replacement/evidence level/source type

Therefore, after slice 001, the remaining 556 entries had their ledger rows for `术语/核心采分点` and `细则位置` marked:

`STRUCTURE_NEEDS_FIX_SOURCE_PENDING`

This does not mean every content sentence is wrong. It means the current document is not auditable enough under the 选必一 hard rules until the missing fields are repaired and each source/rubric is checked.

## Next Work

Continue source-level audit by normalized question group. Repeated entries for the same question must share one formal rubric layer map, then each bucket placement should be checked against that map.
