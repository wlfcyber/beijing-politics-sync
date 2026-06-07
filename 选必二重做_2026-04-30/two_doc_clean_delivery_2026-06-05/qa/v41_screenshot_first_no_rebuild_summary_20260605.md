# v41 screenshot-first / no-rebuild summary

- candidate: `v41_screenshot-first_no-rebuild_candidate`
- generated_at: 2026-06-05 23:12 CST
- status: NOT_FINAL

## Outputs

- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v41.docx`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v41.docx`
- `outputs/选必二法律与生活_试题细则汇编_学生可发版_v41.md`
- `outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v41.md`
- `qa/TWO_DOC_CLEAN_DRAFT_QA_v41_20260605.md`
- `claude_cowork/CLAUDE_OPUS48_COWORK_REVIEW_PACKET_v41_20260605.md`

## User-requested repairs applied

- Removed old generic student-facing scaffolding source from the generator.
- Kept A-axis order as: `需要掌握的知识和踩分点` before `相关例题（2024-2026）`.
- Kept no fixed cap on rubric scoring points: 74 questions, 1036 scoring points, min=3, max=34.
- Changed image-backed entries to screenshot first: `原题图 -> 材料文字 -> 设问文字 -> 细则 -> 细则踩分点`.
- Prevented screenshot-backed rows from being rebuilt into Word tables.
- Replaced visible reconstruction language with `原题图` or `表格文字版`.

## Verification

- Markdown forbidden scan on `outputs/*v41*.md`: zero hits.
- DOCX XML forbidden scan: zero hits in both v41 DOCX files.
- Handbook DOCX structural scan: unzip OK; 2910 paragraphs; 4 tables; 23 inline images; required hits include 10 `需要掌握的知识和踩分点`, 10 `相关例题（2024-2026）`, 74 `细则踩分点`, 23 `原题图`.
- Compilation DOCX structural scan: unzip OK; 1762 paragraphs; 4 tables; 23 inline images; required hits include 75 `细则踩分点`, 25 `原题图`.
- Handbook Markdown structure: 10 related-example sections and 74 source-like example headings.
- Spot check `2025 · 东城 · 二模 · 第19题`: `原题图` appears before `材料文字`, `设问文字`, `细则`, and `细则踩分点`.

## Boundary

- `render_docx.py` failed with `[WinError 2]` because LibreOffice/soffice is unavailable on this machine, so visual render QA is not claimed.
- GPT-5.5 Pro web/app review and Claude Opus 4.8 Max web/app review are still pending for final closure.
- E009, E043, E051, E057, and the remaining source-recovery risks stay open.
