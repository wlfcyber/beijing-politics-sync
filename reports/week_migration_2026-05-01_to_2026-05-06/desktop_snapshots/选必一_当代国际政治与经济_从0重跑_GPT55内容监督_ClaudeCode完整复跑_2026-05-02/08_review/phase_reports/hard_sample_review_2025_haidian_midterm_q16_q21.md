# Hard Sample Review: 2025海淀期中 Q16(2) / Q21(2)

status: codex_current_run_checked
suite_id: `2025_海淀_期中`
questions: `Q16(2)`, `Q21(2)`
module: `选必一《当代国际政治与经济》`

## Local Sources

- paper_source_id: `SRC_e3da1b6b45ca`
- paper_file: `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中/试卷/试卷.pdf`
- scoring_source_id: `SRC_cda046c2d36d`
- scoring_file: `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中/细则/细则.docx`
- extraction_text:
  - `02_extraction/codex_extraction_logs/2025海淀期中/试卷_pdf_text.txt`
  - `02_extraction/codex_extraction_logs/2025海淀期中/细则_docx_text.txt`
- extracted_media:
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png`
  - `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image8.png`

## Evidence Judgment

- question_in_scope: yes
- evidence_level: `P0_verified_rubric` for embedded scoring images/tables in the DOCX; `P3_paper_only` for original paper prompt/material
- old_final_quality_reference_used: no
- GPT_used_as_evidence: no
- DOCX media check: 8 embedded images, 7 tables; this confirms the user's notebook warning that image/table scoring material exists.

## Q16(2) Checked Item

| item | scoring term | source status | Codex entry status | note |
|---|---|---|---|---|
| Q16(2)-1 | 利用国际组织赋予的权利；积极参与全球经济治理和规则制定 | DOCX embedded `image2.png`, 第3点“贸易摩擦”，2分 | indexed | Only this 选必一 point is included; ordinary business strategy/cost-policy language is not forced into the 选必一 table. |

## Q21(2) Checked Items

| item | scoring term | source status | Codex entry status | note |
|---|---|---|---|---|
| Q21(2)-1 | 新中国外交的时代背景不断变化；政治多极化、经济全球化深入发展；和平与发展成为时代主题 | DOCX embedded `image8.png`, “变”第1层，2分 | indexed | Fits 时代背景. |
| Q21(2)-2 | 中国的综合国力不断增强；国际地位不断提升；承担越来越多的国际责任；国际影响力话语权不断提升；人类命运共同体 | DOCX embedded `image8.png`, “变”第2层实力/备注 | indexed | Fits 中国 / 地位与责任. |
| Q21(2)-3 | 外交指导思想与时俱进；习近平外交思想为新时代中国特色大国外交提供了根本遵循和行动指南 | DOCX embedded `image8.png`, “变”第2层思想，1分 | indexed | Fits 中国 / 指导思想. |
| Q21(2)-4 | 新中国外交始终服务于我国人民民主专政的国家性质；坚持党对外交统一集中领导；国家利益 | DOCX embedded `image8.png`, “不变”第1层及备注 | indexed | Fits 中国 / 政策; later final wording must avoid turning state-form language into vague slogan. |
| Q21(2)-5 | 坚持独立自主的基本立场；贯彻维护世界和平、促进共同发展的宗旨；促进世界的和平与发展为基本目标；坚持以和平共处五项原则作为我国对外关系基本准则；独立自主的和平外交政策；反对霸权主义强权政治 | DOCX embedded `image8.png`, “不变”第2层及备注 | indexed | Kept as one grouped scoring function. |

## Transfer Check

- material_trigger_present: yes
- answer_landing_present: yes
- forbidden_answer_meta_language_in_answer_sentence: none found in Codex answer sentences
- student_doc_ready: no, not yet; this is evidence-lock work.

## Remaining Risks

- Need ClaudeCode independent comparison after its Phase 02 restart.
- Need final fusion to decide whether Q21(2) grouped policy terms remain one entry or split into classroom subcards without breaking scoring provenance.
