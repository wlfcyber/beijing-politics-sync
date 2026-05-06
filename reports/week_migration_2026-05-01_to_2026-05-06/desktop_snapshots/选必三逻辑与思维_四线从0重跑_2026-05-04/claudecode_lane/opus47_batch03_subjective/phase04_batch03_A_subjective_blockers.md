# Phase 04 Batch03 A-only Subjective — Lane B (Opus 4.7) Blockers

Run owner: ClaudeCode Lane B (Opus 4.7 max-effort thinking).
Output base: `claudecode_lane/opus47_batch03_subjective/`.
Date: 2026-05-04.

## Hard Blockers

None at the source-evidence layer.

All 56 subjective rows in `05_coverage/phase04_batch03_A_subjective_queue.csv` were resolved against:

- the cached extracted text in `02_extraction/priority_queue_sources/text/` (sources 001-056), and
- the corresponding 试卷 + 细则/补充材料 pairs (paper + rubric) for each suite.

Every row has either:

- a verifiable formal scoring rubric (`A-formal`) confirming the 选必三 module-line attach (思维 / 推理), or
- a verifiable formal scoring rubric for a non-target module (`C-boundary`) showing the row is genuinely out of 选必三 scope.

No row required PDF re-render, OCR, image vision, or DOCX XML textbox recovery beyond the cached text. No row produced `B_TARGET_NEEDS_VISUAL`.

## Soft Blockers / Cautions

These are documented to protect downstream batches and the eventual fusion stage. They are not source-evidence blockers; they are queue-meta integrity issues that must be cleaned before any student-doc work.

### S-1 — Queue split-error: 2026东城期末 Q16

The queue lists `Q-2026东城期末-16-1` and `Q-2026东城期末-16-2` as separate rows. In the original paper (`044_...试卷.pdf`) and the official rubric (`044@L335-347`), Q16 is a single 7-point question (单题, 哲学与文化, "白，不止于白" understanding-type item). The two queue rows must be merged into a single Q16 row before any aggregation. Both rows are SCOPE_OUT regardless.

### S-2 — Queue omission: 2025西城二模 Q16(2) is missing

The queue lists `Q-2025西城二模-16-1` (which is the 哲学智慧 stem) but does NOT list `Q-2025西城二模-16-2`, even though Q16(2) is the actual 选必三 充分条件假言推理 item ("条件①勺鸡和雕鸮不会同时出现在同一饮水点；条件②若发现岩松鼠的活动痕迹则一定能找到红嘴蓝鹊；问题：工作人员在某雨水收集池同时观察到雕鸮和红嘴蓝鹊，能否确定此时一定有岩松鼠活动？解释推理过程", 4 分). The rubric is at `038@L18-19` and explicitly says "条件②是一个充分条件假言判断,看到了红嘴蓝鹊后件为真,无法确定前件的真假,无法确定一定有岩松鼠行动".

Lane B did not synthesize a row for Q16(2) because the base prompt said "Verify exactly the first Batch03 queue ... 56 rows". Q16(2) must be added to a follow-on queue. It is the most important 选必三 推理 row in the entire 2025西城二模 paper and would otherwise be lost.

### S-3 — Queue auto-tag noise

A large fraction of Batch03 rows (≈18 of 33 SCOPE_OUT rows) carry queue auto-tag values (`section_scope=in_scope`, `knowledge_node` containing terms like "概念", "假言", "辩证否定", "创新思维", etc.) that DO NOT match the actual paper task. The auto-tagger appears to trigger on string-level matches in adjacent text (e.g., the 算力 paper happens to contain "概念" somewhere in the option-stems but the actual subjective task is "运用《经济与社会》知识"). The conflicts CSV (`phase04_batch03_A_subjective_conflicts.csv`) lists each occurrence individually as `scope_misclassification`. Future batches should NOT trust queue `section_scope` and `knowledge_node` columns without re-verification against the actual rubric module clause.

### S-4 — Cross / boundary rows with selectable 选必三 attach

Three rows are SCOPE_OUT as a primary task but have a verifiable 选必三 attachment that may be useful in evidence fusion:

- `Q-2025丰台期末-16` (哲学思考 主 + 量变质变规律 attach for 选必三 辩证思维 动态性)
- `Q-2025海淀期末-22` (综合短文 主 + 质量互变规律 attach as one of 7 angle-options)
- `Q-2026东城期末-21` (综合所学 主 + 系统观念 attach as one of 4 angle-options)

These rows are marked `can_enter_fusion=yes` for the boundary attach only; `can_enter_student_draft=no` (per hard rule, no student稿 in this run).

### S-5 — Hard contamination guard reaffirmation

Per the base prompt and `phase04_batch02_status_freeze.md`:

- `2024西城一模 Q11` correct pairing remains `B=①③`. Lane B did not re-touch this row in Batch03 (it is a choice row not a subjective row), but the contamination guard remains active and any future re-tagging back to `B=①④` must be flagged.
- `2025海淀二模 Q12/Q13` answer-source locators must be retained. Lane B did not re-touch these rows in Batch03 (also choice rows).
- Archive skeletons remain internal evidence-pool only. No student稿, no Word/PDF, no final PASS in this Lane B Opus output.

## What is NOT in this output

- No student-facing prose, draft, or 教学 content.
- No Word/Markdown student doc, no PDF.
- No final PASS gate.
- No re-touching of choice-question rows (Batch03 has a sibling A-only choice queue handled separately under `claudecode_lane/opus47_batch03_choice/`).
- No mutation of Codex Lane A files outside the explicit Lane B Opus write set.
