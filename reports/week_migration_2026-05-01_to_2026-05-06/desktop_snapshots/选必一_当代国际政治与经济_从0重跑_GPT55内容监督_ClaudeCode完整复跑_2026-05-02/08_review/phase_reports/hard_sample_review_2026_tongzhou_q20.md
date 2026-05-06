# Hard Sample Review: 2026通州期末 Q20

status: codex_current_run_checked
suite_id: `2026_通州_期末`
question: `Q20`
module: `选必一《当代国际政治与经济》`

## Local Sources

- paper_source_id: `SRC_b66cc2d35877`
- paper_file: `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf`
- scoring_source_id: `SRC_35ef9424281a`
- scoring_file: `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/细则/细则.pptx`
- extraction_text:
  - `02_extraction/codex_extraction_logs/2026通州期末_试卷_pdf_text.txt`
  - `02_extraction/codex_extraction_logs/2026通州期末_细则_pptx_text.txt`
- visual_check: rendered paper pages under `02_extraction/screenshots/2026通州期末_试卷/`

## Evidence Judgment

- question_in_scope: yes
- evidence_level: `P0_verified_scoring_rule` for scoring PPTX; `P3_paper_only` for original paper prompt/material
- old_final_quality_reference_used: no
- GPT_used_as_evidence: no
- ClaudeCode_merge_status: pending comparison only; no Claude entry is accepted without local recheck

## Six Scoring Items Checked

| item | scoring term | source status | Codex entry status | note |
|---|---|---|---|---|
| 1 | 共商共建共享全球治理观 | PPTX slide 15 scoring point; slide 14 answer layer | indexed | Fits 政治多极化/global governance. |
| 2 | 时代主题、经济全球化、顺应各国人民愿望 | PPTX slide 15 scoring point; slide 14 answer layer | indexed | Fits 时代背景; must not shrink to only “时代主题”. |
| 3 | 符合《联合国宪章》 | PPTX slide 15 scoring point; slide 14 answer layer | indexed | Fits 联合国; answer sentence uses 宪章宗旨和原则. |
| 4 | 推动构建国际新秩序、倡导国际关系民主化、践行多边主义、坚持正确义利观、兼顾利益 | PPTX slide 15 scoring point, 任意点共2分 | indexed | Kept as one grouped scoring function instead of over-splitting. |
| 5 | 人类命运共同体 | PPTX slide 15 scoring point; slide 14 answer layer | indexed | Must remain independent; do not collapse into “全球治理倡议”. |
| 6 | 贡献中国智慧、中国方案、勇于大国担当 | PPTX slide 15 scoring point; slide 14 answer layer | indexed | Fits 中国 / 智慧. |

## Prompt Wording Issue

- paper prompt uses: `全球治理倡议正逢其时、指引方向彰显担当`
- scoring PPTX prompt has extra punctuation before `彰显担当`
- decision: use the paper prompt as `完整设问`; use PPTX for scoring positions.

## Transfer Check

- material_trigger_present: yes
- answer_landing_present: yes
- forbidden_answer_meta_language: none found in Codex answer sentences
- student_doc_ready: no, not yet; this is a hard-sample evidence check, not final classroom prose.

## Remaining Risks

- Need ClaudeCode comparison after its Phase 02 restart produces a hard-sample review.
- Need later GPT content review only after a real `section_batch` or student-facing sample exists; current state remains G11 `not_triggered`.
