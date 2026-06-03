# RUBRIC_FORMALITY_RECHECK

Completed: 2026-06-02T16:40:00+08:00

## User Correction

User pointed out that multiple `细则图片` were actually ordinary reference answers, especially the first two entries. This pass removes those reference-answer substitutions from the image-only Word packet.

## Replaced With Formal Scoring Sources

| Entry | Action | Source |
| --- | --- | --- |
| E001 2024 东城一模 第19题 | Replaced reference-answer PDF with formal PPT scoring points and point distribution. | `/Users/wanglifei/Desktop/2024模拟题/2024东城一模/细则/细则.pptx` |
| E002 2024 东城二模 第19题第1问 | Replaced reference answer with per-question `阅卷细则`, including 2/2/3 point distribution. | `/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/19题/19（1）.docx` |
| E003 2024 东城二模 第19题第2问 | Replaced reference answer with per-question `阅卷细则`, including 2/1/no-score rules. | `/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/19题/19（2）.docx` |
| E006 2024 海淀一模 第19题 | Added the formal scoring table after the answer text. | `/Users/wanglifei/Desktop/2024模拟题/2024海淀一模/细则/细则.docx` |
| E007 2024 海淀二模 第19题 | Replaced text fallback with original embedded rubric image. | `/Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/细则.docx` |
| E018 2025 丰台一模 第19题 | Replaced reference answer with formal `评分标准说明`. | `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025丰台一模/细则/细则.docx` |
| E028 2025 海淀期中 第21题第1问 | Replaced reference answer with original embedded rubric image. | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中/细则/细则.docx` |
| E031 2025 海淀一模 第18题 | Replaced placeholder with original embedded formal scoring rubric image: contract validity 2 points, case analysis 3 points, judgment significance 2 points. | `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025海淀一模/细则/细则.docx` |
| E033 2025 石景山一模 第20题 | Replaced title-only rubric with formal scoring table. | `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025石景山一模/细则/细则.doc` |
| E034 2025 西城期末 第19题 | Replaced answer-only 西城 PDF text with same-question formal scoring rubric located in raw term-exam PPT. | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末/细则/细则.pptx` |
| E051 2026 海淀二模 第18题第2问 | Confirmed manual original-PDF rubric crop contains point distribution. | `/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/细则/26海淀高三政治二模讲评.pdf` |

## Formal Rubric Not Found In Raw Source

The following entries no longer use reference answers as rubric images. They now show a `未找到正式评分细则` placeholder image until the official marking rubric can be supplied.

| Entry | Raw source checked | Result |
| --- | --- | --- |
| E009 2024 石景山一模 第18题第2问 | `/Users/wanglifei/Desktop/2024模拟题/石景山一模/细则/细则.pptx` | Only answer-style text located; no point-distribution rubric found. |
| E043 2026 丰台一模 第20题 | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx` | Only answer-style text located; no point-distribution rubric found. |

## Structural Check

- Report rows: 60.
- Missing question image rows: 0.
- Missing rubric image rows: 0.
- Question image assets: 62.
- Rubric image assets: 72.
- Total inline image assets in report: 134.
- DOCX inline drawings: 134.
- DOCX anchored/floating drawings: 0.
- DOCX text-form section markers absent: `【材料】`, `【设问】`, `【细则】`, `分数分布`.

## Render Check

Packaged LibreOffice render remains blocked by a local missing dynamic library:
`/opt/homebrew/opt/little-cms2/lib/liblcms2.2.dylib`.

Fallback checks completed:

- DOCX package integrity check: 128 media files embedded.
- macOS Quick Look thumbnail generated successfully.
- Representative rubric image contact sheet checked at `05_output/image_packet_assets/rubric_audit_contact.jpg`.

## Deep Source Recheck

Completed: 2026-06-02T16:45:00+08:00

- Re-searched raw source text for E009, E031, E034, and E043 across included Desktop source roots.
- Extracted embedded media contact sheets from the remaining unresolved raw files:
  - `05_output/rubric_deep_media/E009_ppt_contact.jpg`
  - `05_output/rubric_deep_media/E031_docx_contact.jpg`
  - `05_output/rubric_deep_media/E043_ppt_contact.jpg`
- E034 formal scoring rubric was found in same-question raw PPT and inserted into the rebuilt Word.
- E031 embedded images were rechecked at original resolution; `word/media/image12.png` is the formal theme-park annual-card rubric and has been inserted into the rebuilt Word.
- E043 embedded images were checked and are mainly student-answer examples and score tags, not a formal scoring rubric.
- Current unresolved formal-rubric placeholders: E009, E043.

## Hidden Text / Relationship Recheck

Completed: 2026-06-02T16:50:00+08:00

- Unzipped the remaining unresolved source files and extracted all XML text, including slides, notes, document text, properties, comments/footnote-like parts where present:
  - `05_output/hidden_text_audit/E009_all_xml_text.txt`
  - `05_output/hidden_text_audit/E031_all_xml_text.txt`
  - `05_output/hidden_text_audit/E043_all_xml_text.txt`
- E009 target slide 37 contains only the answer-style paragraph and has no media relationship other than slide layout.
- E043 target slide 51 contains only the answer-style paragraph and has no media relationship other than slide layout; following slides 52-54 contain student examples, not formal scoring rules.
- E043 scoring-rule text found elsewhere in the PPT belongs to other topics/slides and was not used for this law question.
- Current unresolved formal-rubric placeholders after this pass: E009, E043.

## Final Raw-Root Search

Completed: 2026-06-02T16:52:00+08:00

- Searched raw `/Users/wanglifei/Desktop/2024模拟题` file names for `细则/阅卷/评标/18/石景山`; no additional E009 formal marking file was found beyond `/Users/wanglifei/Desktop/2024模拟题/石景山一模/细则/细则.pptx`.
- Searched raw `/Users/wanglifei/Desktop/2026模拟题` file names for `细则/阅卷/评标/20/丰台`; no additional E043 formal marking file was found beyond `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx`.
- Searched raw source text for E009 distinctive phrases including `天灾`, `不可抗力`, `暴雨前气象`, `物业公司理应`, and `未全面履行服务义务`; no new formal scoring rubric hit was found.
- Searched raw source text for E043 distinctive phrases including `郭某.*餐厅`, `低头看手机`, `安全保障义务.*合理限度`, `自我负责的安全责任意识`, and `台阶区域`; no new formal scoring rubric hit was found.
- Current unresolved formal-rubric placeholders: E009, E043.
