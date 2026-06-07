# COVERAGE_STATUS

## v45 student-document coverage snapshot

- Source base: `../raw_exam_subjective_compilation_2026-06-02/03_source_packets/source_packets_final.jsonl`
- Candidate QA: `qa/TWO_DOC_CLEAN_DRAFT_QA_v45_20260605.md`
- Current output:
  - `outputs/选必二法律与生活_试题细则汇编_学生可发版_v45.docx`
  - `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v45.docx`

| Item | Count / Status |
| --- | ---: |
| 分问总数 | 74 |
| 宝典核心轴分问数 | 73 |
| 跨模块背景题 | 1 |
| 不同大题数量 | 63 |
| 独立单问数量 | 54 |
| A轴章节 | 10 |
| 相关例题题源标题 | 74 |
| 学生版嵌入原题图 | 23 |
| 后台未嵌入原题图 | 0 |
| 后台保留细则图 | 22 |
| 正式点分布细则待深挖条目 | 3 |
| 细则踩分点总数 | 1027 |
| 单题踩分点最少/最多 | 3 / 34 |

## v45 Repair Scope

- The handbook follows the requested order: A1/A2/... -> rubric-derived knowledge and scoring points -> all related examples from 2024-2026.
- Rejected generic scaffolding remains removed from the student-facing handbook: old self-made prompt columns, opening AB rules, B-axis decision table, and quick-reference tables.
- Per-question scoring output uses `细则踩分点` and is sourced from rubric text first, with manual repair points only as deduped supplements.
- v45 keeps the no-fixed-cap scoring strategy: per-question scoring output has no fixed upper limit, and A-axis front-matter scoring points are not capped at three per question.
- Original-question screenshots are embedded for every available image/table-sensitive entry; screenshot-backed entries show `原题图` before `材料文字` and `设问文字`.
- Student-facing table/image wording no longer uses reconstruction language; screenshot-backed rows do not rebuild tables into Word tables.
- Handbook Markdown heading hierarchy is now explicit: A-axis `##`, knowledge and related-example blocks `###`, core example entries `####`, and entry fields `#####`.
- DOCX background-color audit passes for material, prompt, rubric, scoring-point, and A-axis knowledge/scoring-point categories.

## Boundary

- v45 is a repaired candidate, not final closure.
- E009, E043, and E051 remain formal point-distribution rubric risks.
- E057 remains a cross-module/background item pending external/teacher acceptance.
- Render QA is not passed for v45 because LibreOffice/soffice is unavailable; DOCX structural QA, color/background audit, heading hierarchy audit, and text regression scans passed.
- GPT-5.5 Pro web/app review and Claude Opus 4.8 Max web/app review are still required for final closure.
