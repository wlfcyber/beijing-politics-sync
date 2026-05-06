# Phase04 Batch03 B-Choice — Lane B (Opus 4.7) Blockers

## Run / Lane Identity

- Lane: ClaudeCode Lane B (Opus 4.7 — Adaptive Thinking / Max Effort）
- Batch: phase04 batch03 选择题 verification
- Queue: `05_coverage/phase04_batch03_B_choice_queue.csv` (56 rows)
- Output dir: `claudecode_lane/opus47_batch03_choice/`
- This is a parallel re-run launched separately from any prior Sonnet run; the prior Sonnet run is treated as terminated and its output is not used as evidence here.

## Hard blockers (rows that could not be resolved without further evidence)

None. All 56 rows reached a terminal `B_TARGET_*` decision (no row left as `B_TARGET_BLOCKED` in this Lane B run). For each row we have at least one reliable answer source paired (rubric, embedded answer table in 试卷 PDF, or supplementary teacher version).

## Soft blockers / partial coverage notes

The following rows have non-blocking caveats worth recording for fusion review. They were still answered, but the evidence chain has a partial weakness:

1. **Q-2026东城一模-6 (S-2026东城一模 / Q6)**
   - Authoritative answer key: `046_Desktop_..._试卷.pdf::Page9 参考答案表` shows Q6 = **D**.
   - Codex Lane A precheck reported `detected_answer = B` for this row (`CODEX_A_CHOICE_ANSWER_OPTIONS_CANDIDATE`), which Lane B rejects as a precheck error — see `phase04_batch03_B_choice_conflicts.csv`.
   - Supplementary rubric `048_Desktop_..._细则.pdf` is image-only (text extraction empty) and the分题细则 PowerPoints (049-056) cover 主观题 only; they do not contradict the embedded answer table but they also do not independently re-confirm Q6=D. Treat the embedded answer table as authoritative, but flag this as a single-source confirmation pending a second visual recheck on the 046 PDF answer-table page.

2. **Q-2026顺义一模-5 / Q-2026顺义一模-6 / Q-2026顺义一模-7 / Q-2026顺义一模-9**
   - The local `02_extraction/priority_queue_sources/text/002_..._细则.pptx.txt` (this run's extraction) contains only 主观题 rubric; choice answers 1–15 were NOT carried in this extraction.
   - Choice answer table is recovered from the alternate extraction at `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维双线四线终极跑_2026-05-04/02_extraction/priority_source_texts/002_..._细则.pptx.txt` (Slide 1 prints the 1–15 letter table).
   - Lane B aligns with this alternate extraction (Q3=C, Q4=A, Q5=D, Q6=A, Q7=D, Q8=A, Q9=B, …). Recommend cross-running the local 002 .pptx through a richer pptx-to-text pass to cache Slide 1's answer table inside this run's extraction tree.

3. **Q-2026东城一模-12 (脑机接口产业链)**
   - Stem includes a 产业链构成 figure not captured in text extraction. Answer = B is confirmed by the embedded answer table, but the option-D distractor analysis depends on the unseen figure (上游/中游/下游 占比 distribution). Marked `scope_out` and `paired_candidate` for visual_status — fusion does not rely on it for 选必三 student稿.

4. **Q-2024西城一模 Q11 contamination guard**
   - Q11 is NOT in the 56-row queue, so Lane B does not produce a row for it. However the contamination guard from the base prompt requires verifying that no source in this batch propagates `B = ①④` for Q11.
   - Authoritative source `025_..._细则.docx` shows Q11 = B (letter only; no option-pair text). The 024 试卷 docx Q11 stem references option statements as ①②③④ in figure form; the figure was not text-extractable, so Lane B cannot independently verify the ①③ pairing claim from text alone.
   - Lane B did not propagate either pairing in any output for Q11 (it is out of the 56-row queue). The contamination guard is satisfied for this batch's outputs by absence; downstream fusion should still ensure that any later pairing of Q-2024西城一模-11 uses B = ①③ as authoritative.

5. **2025海淀二模 Q12 / Q13 answer-source locator**
   - Neither Q-2025海淀二模-12 nor Q-2025海淀二模-13 appears in this 56-row queue, so no row was authored for either. Therefore the explicit-locator requirement from the base prompt is moot for this batch's output. If a downstream batch references either question, the answer source is `009_Desktop_2025模拟题_2025各区二模_2025海淀二模_细则_细则.docx` and `010_Desktop_..._补充材料_2025年海淀二模评标实录.docx` (and `011_..._讲评0510.pdf`); both `009` and `010` survived text extraction in `02_extraction/priority_queue_sources/text/`.

## Sources of authoritative answer keys (per suite)

| suite_id | authoritative answer source | location | choice answers Q1–Q15 |
|---|---|---|---|
| S-2025西城二模 | 038 细则.docx | `02_extraction/priority_queue_sources/text/038_*.txt` | A,D,A,C,B,C,C,D,D,C,A,B,A,D,B |
| S-2026东城一模 | 046 试卷 embedded | same path 046_*.txt p9 | B,A,C,A,B,D,D,A,D,C,C,B,C,B,A |
| S-2026顺义一模 | 002 细则.pptx (alt extraction Slide 1) | `选必三逻辑与思维双线四线终极跑_2026-05-04/02_extraction/priority_source_texts/002_*.txt` | B,C,C,A,D,A,D,A,B,B,D,B,C,D,C |
| S-2024朝阳期中 | 020 细则.rtf textutil | `02_extraction/priority_queue_sources/text/020_*.textutil.txt` | B,D,D,C,A,C,B,D,B,D,C,C,C,A,B |
| S-2024海淀二模 | 028 细则.docx | `02_extraction/priority_queue_sources/text/028_*.txt` line 3 | C,D,C,B,A,C,D,B,D,B,A,B,A,C,D |
| S-2024西城一模 | 025 细则.docx | `02_extraction/priority_queue_sources/text/025_*.txt` lines 4-6 | C,A,D,B,B,C,A,D,D,A,B,C,B,A,C |
| S-2025东城期末 | 012 试卷 embedded "故选" lines | `02_extraction/priority_queue_sources/text/012_*.txt` | D,D,B,A,C,C,B,B,A,C,C,A,B,D,B |
| S-2025丰台期末 | 040 试卷 embedded "【答案】" | `02_extraction/priority_queue_sources/text/040_*.txt` | B,D,B,A,A,A,C,D,D,B,D,B,C,C,A |
| S-2025顺义一模 | 036 顺义参考答案 | `02_extraction/priority_queue_sources/text/036_*.txt` lines 5-7 | A,C,B,D,B,C,A,C,B,A,D,C,B,D,A |
| S-2026东城期末 | 044 试卷 embedded vertical answer table | `02_extraction/priority_queue_sources/text/044_*.txt` p8 | D,C,B,D,A,B,A,B,A,D,C,B,C,D,C |
| S-2026朝阳期中 | 003 试卷 embedded vertical answer table | `02_extraction/priority_queue_sources/text/003_*.txt` p8 | A,C,C,A,B,B,D,D,C,C,A,B,D,B,D |
| S-2026通州期末 | 006 试卷 embedded vertical answer table | `02_extraction/priority_queue_sources/text/006_*.txt` p9 | A,D,B,D,C,A,B,D,D,B,C,A,C,A,B |
| S-2024朝阳一模 | 031/032 细则.pptx slide-by-slide answer letter | `02_extraction/priority_queue_sources/text/031_*.txt` and 032 | (Q7=C slide15; Q9=D slide17) — full table not in one slide, partial pieced from per-question slides |
| S-2024朝阳二模 | 023 细则.docx Table 1 | `02_extraction/priority_queue_sources/text/023_*.txt` | B,C,B,A,D,C,D,A,D,C,B,C,B,D,D |
| S-2025海淀期末 | 015 试卷.docx Table 7 | `02_extraction/priority_queue_sources/text/015_*.txt` lines 175-177 | A,C,B,C,D,B,A,D,B,C,D,A,B,C,D |

## Things that did NOT block but are worth surfacing

- Multiple queue rows are mis-classified at the section_scope/knowledge_node level (queue says `推理` or `思维`, but the actual stem is 政治 / 经济 / 文化 / 法律). Lane B has overridden these to `B_TARGET_SCOPE_OUT` in the results CSV and reported in the conflicts CSV. The queue's `excerpt` field for several rows (notably 2025东城期末-1, 2025东城期末-2) appears to have grabbed text from elsewhere in the PDF (textbook entries) rather than the actual question stem. The actual stems (改革开放, 邓小平理论) confirm scope_out.
- 048 (2026东城一模 细则.pdf) and 047 (2026东城一模 原卷扫描版.pdf) are both image-only / empty text. Choice answers for 2026东城一模 rely on the embedded answer table inside 046 (the typeset 试卷). Recommend a render+OCR pass on 048 if a richer 选择题分题细则 is required.

## Lane gate

- `can_enter_student_draft = no` for all 56 rows.
- B-choice signal can support choice-trap or evidence-archive material only; it cannot, by itself, authorize 学生稿 / Word / PDF / final PASS.
- No 学生稿 / 成文化 was produced or attempted in this lane.
