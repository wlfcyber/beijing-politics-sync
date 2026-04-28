# ClaudeCode task: 56-suite OCR-repaired final document

You are continuing the Beijing politics philosophy project. This is not a planning task. Execute, write files, and leave an audit trail.

## Goal

Generate the final student-facing document for:

`飞哥正志讲堂：2026北京高考政治哲学宝典---三年模拟全触发全链条`

The previous final/v4/v6 versions are not sufficient because some `ocr-needed` suites were not included or were left as partial evidence. Your job is to use the existing 56-suite run as the baseline, repair OCR-needed/source gaps where possible, merge the repaired entries, and produce a new final document.

## Hard source rules

1. Old framework entries, old CSV judgments, old model summaries, old "final" files, and old Claude/Codex conclusions are not evidence.
2. First-source cache is preferred evidence: raw-paper/answer/rubric converted text, suite bundles, manifest rows, rendered page images, and verified OCR/crops.
3. Cache-first is not cache-only. If the cache is incomplete, unclear, missing the full prompt/material/answer key/rubric boundary, go back to the original PDF/PPT/Word or the rendered page image.
4. Do not blind-OCR everything. Only repair the suites/gaps below and any additional gap discovered while validating the 56-suite final.
5. The final student-facing document must not contain source paths, file ids, line ids, slide ids, OCR logs, debug logs, `F04`, `L24`, `.pdf`, `.pptx`, `.docx`, `source path`, hashes, or process notes.
6. Keep all provenance, path evidence, OCR notes, and blocker notes in a separate audit file.
7. The final student-facing document must be organized by the user's original principle/method framework nodes, not by suite order or question order.
8. For every main-question entry included in the final student-facing document:
   - copy the full question prompt;
   - include only the material trigger excerpt needed for the principle;
   - explain why the material triggers the principle;
   - write a concrete answer landing, not a meta-instruction;
   - state rubric/scoring correspondence in student-readable wording without engineering provenance.
9. For choice questions, include only stable correct-option or wrong-option patterns with a reliable answer key and enough question/material signal.
10. Do not hide source-missing or answer-key-missing cases as completed.

## Primary inputs

Read these first:

- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\SUITE_ROSTER.csv`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_outputs\*_v6_student_entries.md`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_outputs\*_v6_audit_entries.csv`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_outputs\*_v6_choice_review.md`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_reports\*_v6.md`
- `C:\Users\Administrator\Desktop\4.29凌晨跑完的结果v6\01_学生版Word\必修四哲学材料-知识触发框架_v6.md`
- `C:\Users\Administrator\Desktop\4.29凌晨跑完的结果v6\03_结构化CSV\v6_entries_merged.csv`
- `C:\bp_sync_visible\reports\claudecode_v4_final_2026-04-28\compare\08_OCR-needed重跑控制清单.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\S001_2024东城一模.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_RESULTS.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_AUDIT.md`

Important mapping note: in the old OCR rerun package, `S001` means `2024东城一模`. In the new 56-suite roster, `2024东城一模` is `S003`. Merge by suite name, not by old suite id.

## Required repair queue

Use the 56-suite roster IDs below when writing the new coverage/audit matrix.

### A. Whole-suite OCR/source repairs

- `S003 2024东城一模`: already repaired in `reports\ocr_rerun_claudecode_2026-04-28`; merge this result into the final. Its recovered key is `1C 2B 3A 4A 5D 6D 7A 8D 9B 10C 11A 12B 13D 14C 15C`. Include only the valid 必修四 philosophy/culture/choice items; keep module-boundary exclusions out of the final body.
- `S012 2024丰台二模`: repair by reading cache first, then rendered pages/original paper if needed. Recover "统筹发展和安全" and "你的步伐就是中国的步伐" only if the full prompt/material and scoring boundary can be confirmed.
- `S042 2026丰台一模`: repair paper OCR if needed; recover Q16 and "积极识变应变求变" only where complete prompt/material/scoring loop exists.
- `S044 2026房山一模`: repair paper OCR if needed; recover Q16(2), Q18(1), Q20 where they can be closed with scoring evidence; repair choice-question paper/key if possible.
- `S038 2026海淀一模`: repair paper OCR if needed; check Q16 for "物质决定意识/一切从实际出发" and related framework nodes. Do not rely on old conclusions.
- `S054 2026丰台期末`: repair paper OCR if needed; recover the "留白" main question with full prompt/material and four philosophy scoring points.
- `S053 2026朝阳期末`: repair paper and rubric OCR if needed; judge from zero whether there are 必修四 philosophy entries and choice entries.
- `S049 2026海淀期末`: repair the first 8 paper pages if needed; recover Q16/Q17/Q21 and affected choice questions where evidence closes.

### B. Misjudged file-present repair

- `S047 2026顺义一模`: do not treat this as missing. The paper is readable and the rubric PPTX contains Q16 scoring content. Redo Q16 "破窗效应" with full prompt, material trigger, and source-supported philosophy points such as 量变质变/适度、矛盾转化、联系/系统优化、价值观 where actually supported. Use answer key if reliable for choice rows.

### C. True source/answer-key missing boundaries

- `S039 2026西城一模`: main questions can be used if paper and rubric are present; choice questions without a reliable 1-15 key must remain answer-key-missing unless a reliable key is found locally.
- `S050 2026西城期末`: do not invent question text if the paper is missing. Search local cache/source folders; if still missing, mark source-missing in audit only.
- `S055 2026石景山期末`: if only answer/scoring PDF exists and no paper text exists, keep source-missing in audit only.

### D. Local OCR/image supplements

After A/B/C, check and repair only if evidence can be confirmed:

- `S010 2024东城二模`
- `S005 2024丰台一模`
- `S018 2025东城一模`
- `S019 2025朝阳一模`
- `S026 2025海淀二模`
- `S036 2025朝阳期末`

## Image safety

Do not place many >2000px images into a single model message. Before reading page images, inspect dimensions. Prefer text cache, suite bundles, small rendered pages, or cropped/downscaled derived images. If you must use images, keep each image within the many-image dimension limit and limit the batch.

## Required outputs

Create these files under:

`C:\bp_sync_visible\reports\final_56_ocr_repaired_claudecode_2026-04-29`

1. `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md`
2. `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.docx`
3. `outputs\北京高考政治选择题错肢总结_56套OCR补齐版.md`
4. `outputs\北京高考政治选择题错肢总结_56套OCR补齐版.docx`
5. `audit\FINAL_56_OCR_REPAIRED_AUDIT.md`
6. `audit\COVERAGE_REPAIR_MATRIX.csv`
7. `audit\STUDENT_CLEANLINESS_SCAN.txt`
8. `BUILD_REPORT.md`

The student Markdown and Word files must be clean student-facing artifacts. Audit files may contain paths, OCR notes, and source boundaries.

## Validation before finishing

Before final response, run and record checks:

- Count `SUITE_ROSTER.csv`: must be 56.
- State whether every A/B repair suite is `merged`, `excluded-after-source-check`, or `blocked-with-explicit-reason`.
- Run a text scan on student-facing Markdown files for forbidden engineering residues:
  `C:\\|source_path|hash|sha256|page_|OCR|debug|visible_runs|crops_|F\d{2}|L\d{2}|slide|pdf|pptx|docx|\.jsonl`
- If any forbidden residue remains in student-facing files, fix it before finishing.
- Ensure page 1 of the DOCX is a clean cover with only the title and large signature `飞哥正志讲堂`; page 2 reserves a foreword section for the user and does not contain process logs.
- Write `BUILD_REPORT.md` summarizing what changed from v6, which OCR-needed items were recovered, and which source-missing items remain out.

Now execute the task.
