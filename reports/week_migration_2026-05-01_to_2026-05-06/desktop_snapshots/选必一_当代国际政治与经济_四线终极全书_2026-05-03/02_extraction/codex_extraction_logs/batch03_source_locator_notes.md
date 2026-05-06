# Batch 03 Source Locator Notes

Scope: 2026西城期末 Q20.

## Source Files Checked

| source | local file | method | result |
|---|---|---|---|
| teacher paper | `/Users/wanglifei/GaokaoPolitics/2026各区模拟题/2026各区期末和期中/2026西城期末/2026北京西城高三（上）期末政治（教师版）.pdf` | PyMuPDF render + visual read | Q20 prompt recovered on page 8 |
| rubric | `/Users/wanglifei/GaokaoPolitics/2026各区模拟题/2026各区期末和期中/2026西城期末/2026西城期末细则.pdf` | PyMuPDF render + visual read | Q20 scoring rule recovered across pages 4-5 |
| rubric text extraction | `02_extraction/ocr_outputs/batch03_2026西城期末_Q20/rubric_pdf_all_pages.txt` | text extraction | blank; visual read required |
| answer text | `02_extraction/ocr_outputs/batch03_2026西城期末_Q20/teacher_pdf_all_pages.txt` | text extraction | answer reference text readable on answer pages; cannot replace scoring rule |

## Rendered Evidence

- Prompt image: `02_extraction/screenshots/batch03_2026西城期末_Q20/teacher_pdf_page_08.png`
- Rubric images: `02_extraction/screenshots/batch03_2026西城期末_Q20/rubric_pdf_page_04.png`; `02_extraction/screenshots/batch03_2026西城期末_Q20/rubric_pdf_page_05.png`

## Full Prompt

2026西城期末 Q20: `2025年11月，中国政府正式向联合国提交《中国2035年国家自主贡献（NDC）目标》。该文件全面总结了过去工作的显著进展，设定了未来的气候行动目标。` The table compares `中国NDC进展与目标概况` across energy structure, forest carbon sink, greenhouse-gas reduction, green transport, market mechanism, and climate adaptation. The note says NDC is the core of the Paris Agreement and parties submit national climate action targets every five years. Prompt: `结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。`

## Scoring Rule Read

Evidence status: P0 formal scoring rule by visual read of `2026西城期末细则.pdf`, pages 4-5.

Q20 scoring structure:

- Reference answer paragraph: China is an active builder and leader of global climate governance; contributes Chinese strength to global ecological civilization and global climate governance; adheres to green development; independently proposes climate-governance action goals; promotes low-carbon transformation in energy, industry, market and other fields; consciously fulfills international obligations and assumes major-country responsibility; adheres to consultation, joint contribution and shared benefits; implements the Paris Agreement; uses multilateral cooperation to address climate change; maintains the UN core role in international affairs; promotes global sustainable development; promotes building a community with a shared future for mankind.
- Angle 1 `中国实践是什么`, 2 points:
  - China's role in global climate governance: `建设者 / 引领者 / 做负责任的大国`, 1 point.
  - Specific practice: `坚持绿色发展 / 新发展理念，有为政府 + 有效市场（用知识来概括）`, 1 point.
- Angle 2 `中国为什么要参与该实践`, 3 points, `4选3`:
  - International background: `和平发展合作共赢是时代潮流 / 非传统安全威胁`, 1 point.
  - `共同利益`, 1 point.
  - China concepts: `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 践行真正的多边主义 / 坚持互利共赢`, 1 point.
  - `自觉履行国际义务 / 遵循国际法 / 承担国际责任`, 1 point.
- Angle 3 `实践的效果怎么样`, 3 points:
  - International effect: `促进全球可持续发展 / 建设清洁世界`, 1 point.
  - Governance effect: `维护联合国的核心作用 / 完善全球治理体系`, 1 point.
  - China contribution: `贡献中国智慧 / 中国力量`, 1 point.

## Boundary Decisions

- P0 promotion is allowed because the formal scoring PDF has been visually checked in this run.
- The answer-reference text from the teacher paper is useful for material-trigger wording, but not the authority for scoring atoms.
- Angle 2 is `4选3`; in frequency/必答统计, these four alternatives cannot all be counted as independent mandatory points from this one question.
- `坚持绿色发展 / 新发展理念，有为政府 + 有效市场` is cross-module/material-practice support. It can be recorded as source context but should not become a central 选必一 six-bucket scoring core unless framed through global climate governance.
