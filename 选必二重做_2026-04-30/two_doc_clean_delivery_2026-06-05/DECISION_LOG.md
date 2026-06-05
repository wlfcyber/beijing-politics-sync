# DECISION_LOG

## 2026-06-05 v17 control repair

- Decision: formal external review for this run must use visible web/app sessions only. CLI, pro-cli, Claude CLI, or simulated advisor outputs are invalid for final acceptance.
- Decision: v17 student-facing documents remain text-only; full-page source/rubric screenshots are retained as backend QA assets but are not embedded in the two student DOCX files.
- Decision: v16 GPT-5.5 Pro web/app `compilation-01` result is treated as FAIL for workflow purposes. Some findings were local false positives caused by long-chunk conflation, but it exposed real student-facing answer-point residue, repaired in v17.
- Boundary: E009 still lacks formal point-distribution rubric evidence. E057 is retained only as cross-module/background and still needs teacher or Claude final retention judgment.
- Status: do not claim final delivery or GitHub final closure until GPT-5.5 Pro web/app and Claude Opus 4.8 Max web/app reviews both close without blocking defects.

## 2026-06-05 v27 layout rebuild

- Decision: user rejected v26 presentation as too scattered and text-like; v27 becomes the current layout candidate while v26 remains a repaired-content checkpoint.
- Decision: student-facing layout should learn from the accepted 选必一/必修四宝典 family: blue hierarchy, clean source rows, boxed material/rubric blocks, and red answer-point bullets.
- Decision: table-like materials and rubrics should be reconstructed as Word tables when reliable; for high-risk table/image cases, embed a precise original-question image only where it improves student readability and verification.
- Boundary: v27 is a presentation rebuild and local-render pass, not a final external-review closure. GPT-5.5 Pro and Claude Opus 4.8 Max still must use web/app sessions only.

## 2026-06-05 v30 mother-style layout rebuild

- Decision: user rejected the v27/v28 database-card feeling; v30 supersedes v27/v28 as the current presentation candidate.
- Decision: latest 必修四、选必一、选必三宝典 share a lecture-handbook pattern: quiet cover, clean contents, natural tagged paragraphs, selective color callouts, and tables only where the source is truly tabular.
- Decision: v30 adopts that pattern: material/question/rubric/answer fields are no longer rendered as universal cards; table rows avoid cross-page splitting and repeat headers when a table continues.
- Boundary: v30 is still a layout candidate and local render pass. It does not close E009/E057 and does not count as GPT-5.5 Pro or Claude Opus 4.8 Max formal web/app acceptance.

## 2026-06-05 v31 E001 rubric source repair

- Decision: user correctly identified that v30 turned the first 2024东城一模细则 into an answer-like paragraph.
- Source finding: E001 source packet pointed to `思想政治答案(1).pdf`; the real scoring material for this item is in `2024东城一模/细则/细则.pptx`, slide 57.
- Decision: v31 supersedes v30. E001 now uses the PPTX scoring text with explicit 2+2+2 point structure; QA now lists rubric-source repairs and answer-PDF-as-rubric risk.
- Boundary: v31 fixes this local source error but remains NOT_FINAL until GPT-5.5 Pro and Claude Opus 4.8 Max web/app reviews pass.

## 2026-06-05 v32 rubric-source risk audit

- Decision: user feedback about answer text being treated as rubric must be expanded from the single E001 case into a source-risk audit, not handled as a local wording patch.
- Source repair: E002/E003 now point to the 2024东城二模 per-question `阅卷总结/19题/19（1）.docx` and `19（2）.docx` sources rather than the generic supplementary PDF path.
- Content repair: E018 now restores the 2025丰台一模第19题 `评分标准说明` table text, including error boundaries and substitute expressions; v31 had only an answer-style paragraph.
- Metadata repair: E024 and E031 no longer remain tagged as `answer_reference`; E024 uses the scanned rubric/marking PDF with score and no-score notes, and E031 uses the 海淀一模细则 DOCX embedded formal rubric image evidence.
- Boundary: E009、E043、E051 remain formal point-distribution rubric risks and must stay visible in QA; v32 remains NOT_FINAL until web/app GPT-5.5 Pro and Claude Opus 4.8 Max reviews pass.

## 2026-06-05 v33 Claude modification report repair

- Decision: apply the local Claude application review files `法律与生活_修改意见报告.docx` and `法律与生活_修改意见汇总表.xlsx` as a repair queue for the current v32 two-document candidate, not as final acceptance.
- Content repair: v33 fixes the 10 high-priority issues from the report: E007 扶养/赡养, E022/E023 昌平二模结构, E025 可撤销/无效混淆, E030 竞业限制8分结构, E031 解除/撤销权边界, E036/E044/E048 表格串栏, E039 第1问细则串入第2问.
- Source decision: for E022/E023, the report's proposed “每问6分” reading conflicts with the local original paper. The original paper shows `20.（6分）` and two blanks `(1)(2)` in the裁判理由 column, so v33 uses total 6分 with two 3分 blanks.
- Safety repair: v33 also absorbs source-safe medium/low edits such as E073 身体权/健康权, E005 原劳动和社会保障部, E006 公序良俗 and 7-8分, E008 承诺到达生效, E009 不可抗力/司法确认 wording, E012 赡养费, E013 食品安全法148条, E016 效力待定, E058 民法典293条, E066 外观设计专利权, E067 民法典497条, E072 不得过度处理.
- Verification: v33 local build and render passed; output bad-term scan and same-group self-reference scan passed. Boundary remains NOT_FINAL until valid GPT-5.5 Pro and Claude Opus 4.8 Max web/app reviews pass.

## 2026-06-05 v34 recheck and baodian repair

- Decision: apply `法律与生活v33_复核与宝典核对_报告.docx` and `法律与生活v33_复核与宝典核对_汇总表.xlsx` as a row-level repair queue for v33, not as final acceptance.
- Process decision: extract all 255 review rows into `qa/v33_recheck_and_baodian_raw_extract_20260605.tsv`, then produce row-level adjudication in `qa/v34_recheck_and_baodian_adjudication_20260605.tsv`; do not collapse “source-evidence risk” and “teacher taste” into “fixed”.
- Content repair: v34 hard-fixes the high-priority串栏/table items: 2024东城一模19诉讼时效资料卡, 2024海淀一模19虚拟数字人资料卡, 2026石景山一模18举证责任表, 2025丰台期末19劳动法/劳动合同法表, 2025海淀期中21(1)婚姻法/民法典表, 2026门头沟一模18(1)环境民事公益诉讼.
- Legal verification: 2025东城期末19(1) high-rise building fire-safety rule 第37条 was checked against the official Emergency Management Ministry page; 2026丰台二模生态环境法典 effective-date boundary was checked against the official Ecology and Environment Ministry page.
- Boundary: E009/E043/E051 remain formal point-distribution risks; v34 does not invent point values without formal rubric evidence. GPT-5.5 Pro and Claude Opus 4.8 Max final reviews still must be performed via web/app only, never CLI.

## 2026-06-05 v35 v34 recheck repair

- Decision: apply `法律与生活v34_复核报告.docx` and `法律与生活v34_复核汇总表.xlsx` as a repair queue for v34, not as final acceptance.
- Process decision: extract all 140 v34-review rows into `qa/v34_recheck_raw_extract_20260605.tsv`, then produce row-level handling in `qa/v35_recheck_adjudication_20260605.tsv`; keep “已实改”“保留回源风险”“编辑性建议暂缓” separate.
- Content repair: v35 hard-fixes legal/structure issues that do not require new source scoring evidence, including E016效力待定链条、E014本问2分与共有部分、E035小刘打赏责任口径、E062劳动法表述、E071竞业限制利益关联、E042内部阅卷抬头、E022 AI作者/著作权主体表述、E026共有部位安装摄像头与隐私权衔接。
- Baodian repair: v35 corrects clear AB-axis mismatches for E051 B5意义价值、E052 B1表格补链、E054 B5意义价值、E055 A1民事主体、E072含必修3国家治理/制度建设角度.
- Boundary: v35 does not invent point values or total scores for unresolved source-evidence items. E009/E043/E051 remain formal point-distribution risks, and 2026顺义一模18 remains a score-split source risk. GPT-5.5 Pro and Claude Opus 4.8 Max final reviews still must be web/app only, never CLI.
