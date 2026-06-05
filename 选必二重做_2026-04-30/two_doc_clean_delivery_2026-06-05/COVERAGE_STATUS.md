# COVERAGE_STATUS

## v35 student-document coverage snapshot

- Source base: `../raw_exam_subjective_compilation_2026-06-02/03_source_packets/source_packets_final.jsonl`
- Repair overlays:
  - `../raw_exam_subjective_compilation_2026-06-02/05_output/A_THEME_SOURCE_REPAIR_OVERRIDES_20260604.json`
  - `../raw_exam_subjective_compilation_2026-06-02/05_output/A_THEME_PENDING_BOUNDARY_RESOLUTIONS_20260604.json`
- Candidate QA: `qa/TWO_DOC_CLEAN_DRAFT_QA_v35_20260605.md`

| Item | Count / Status |
| --- | ---: |
| 分问总数 | 74 |
| 宝典核心轴分问数 | 73 |
| 跨模块背景题 | 1 |
| 同题组数量 | 64 |
| 教师复核条目 | 4 |
| answer_reference证据风险条目 | 0 |
| 正式点分布细则待深挖条目 | 3 |
| 学生版嵌入图片条目 | 3 |
| 后台保留原题图条目 | 20 |
| 后台保留细则图条目 | 22 |
| 表格优先重建条目 | 17 |

## Boundary

- This file is a run-level coverage snapshot for the two student documents, not a replacement for the upstream source packet ledger.
- v35 keeps the upstream 74-question coverage base, preserves the v30 mother-style presentation, extends v31/v32 source-risk repairs, applies the Claude local modification report, absorbs the v33复核与宝典核对 report/xlsx, and then applies the v34复核报告/汇总表 into the current two student documents.
- v35 repairs legal wording and structure items from the 140-row v34 recheck: E014/E016/E022/E026/E033/E035/E042/E062/E071, plus B-axis/A-axis fixes for E051/E052/E054/E055/E072 and placeholder/internal-heading cleanup.
- v35 row-level adjudication: `qa/v35_recheck_adjudication_20260605.tsv`; summary: `qa/v35_recheck_adjudication_summary_20260605.md`.
- E009、E043、E051 remain formal point-distribution rubric risks; 2026顺义一模18 remains a score-split source risk; E057 remains a cross-module/background item. None may be hidden in final acceptance.
