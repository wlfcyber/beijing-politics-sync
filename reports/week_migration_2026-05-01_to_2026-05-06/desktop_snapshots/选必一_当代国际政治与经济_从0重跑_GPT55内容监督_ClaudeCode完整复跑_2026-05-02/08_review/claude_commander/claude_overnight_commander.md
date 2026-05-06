# Claude Overnight Commander Packet
# 选必一《当代国际政治与经济》 — 2026-05-03 夜间交付督工

Generated: 2026-05-03
Authority boundary: This is advisory output only. Codex digests into local tasks, verifies all source/content claims against original files, and retains final artifact authority. This document is not evidence.

---

## 1. Stop / Go Judgment

**CONDITIONAL GO — overnight final-delivery mode can proceed under the following constraints.**

What permits go:
- Phase 02 hard-sample work is substantively complete for the four user-required sample suites (2026通州期末 Q20, 2026朝阳期中 Q17, 2025海淀期中 Q16(2)/Q21(2)).
- ClaudeCode restart screen `xuanbiyi_claudecode_phase02_restart_20260502` is active and has produced `phase02_restart_status.md`, `claudecode_source_inventory_phase02.csv`, `claudecode_evidence_level_recheck.csv`, and `claudecode_xuanbiyi_subjective_index.csv`.
- Evidence conflict `C-2025HDQZ-evidence-level` is locally resolved in Codex's favor (P0 image/table evidence extracted and indexed). ClaudeCode must acknowledge before fusion.
- User has explicitly authorized overnight unattended continuation.

What blocks final delivery (do not promote to final Markdown/DOCX/PDF until resolved):
- G2.5 / G4: ~94 sources still `pending_content_recheck`; must-check suites 2025海淀期末 Q22, 2024东城一模 Q16/Q20, 2026西城期末 Q20 are not yet formally closed with correct evidence levels.
- G6: conflict `C-2025HDQZ-evidence-level` is `codex_resolved_pending_claudecode_ack` — ClaudeCode acknowledgement required before fusion.
- G7/G11: no student-facing outline, section batch, or final Markdown exists yet; all G11 triggers are `not_triggered`.
- 2026西城期末 Q20: hard blocker — scanned PDF, empty paper folder; must not be included unless OCR succeeds or user provides alternative source.

---

## 2. Ordered Tasks for ClaudeCode (8–12 steps)

Execute in this sequence. After each task write the relevant output file before proceeding to the next.

### Task 1 — Resolve conflict C-2025HDQZ-evidence-level

Read the two extracted images locally:
- `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png`
- `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image8.png`

Confirm whether image2.png is the Q16(2) scoring detail and image8.png is the Q21(2) scoring table. If confirmed, upgrade `2025海淀期中_细则` in `claudecode_lane/claudecode_evidence_level_recheck.csv` from `P1_reference_answer` to `P0_verified_rubric`. Update the four Q16(2)/Q21(2) rows in `claudecode_lane/claudecode_xuanbiyi_subjective_index.csv` from `provisional_P1` to `closed_P0`. Write a one-line finding to `claudecode_lane/claudecode_conflicts_suspected.md` acknowledging resolution.

Do not re-read large DOCX binary payloads. Use only the already-extracted image files and the Codex hard-sample review at `08_review/phase_reports/hard_sample_review_2025_haidian_midterm_q16_q21.md`.

### Task 2 — Close 2025海淀期末 Q22

`phase02_restart_status.md` already confirms slide 61 is labeled "22.细则" and slide 62 lists 选必一 acceptable knowledge (人类命运共同体; 中国智慧中国方案). These are not fixed scoring points; they are listed as optional usable knowledge (可选非必答). Evidence level is P2.

User requirement (`current-user-requirements.md`): "2025海淀期末 Q22 可正常补入." Include at P2 with explicit notation.

Write entry in `claudecode_lane/claudecode_xuanbiyi_subjective_index.csv`. Set `evidence_level=P2_teaching_or_lecture`. Set `status=closed_P2`. Write suite report `claudecode_lane/claudecode_suite_reports_phase02/2025海淀期末.md` recording slide numbers, P2 classification, and the exact slide-62 term list.

### Task 3 — Close 2024东城一模 Q16

`phase02_restart_status.md` confirms slide 26 of `细则.pptx` contains "16题阅卷细则" with: 国际关系民主化, 推进构建新型国际关系, 推动构建人类命运共同体. File header on slide 1 is "高三政治 试题分析", so this is P2_teaching_or_lecture, not P0.

User requirement: "2024东城一模 Q16 必须补入." Include at P2 with explicit notation.

Write entry. Set `evidence_level=P2_teaching_or_lecture`. Set `status=closed_P2`. Write suite report `claudecode_lane/claudecode_suite_reports_phase02/2024东城一模.md` with slide reference.

Note module boundary: Q16 is a philosophy/culture mixed question. Record `module_boundary_notes` and do not force philosophy-module terms into the 选必一 main table.

### Task 4 — Close 2024东城一模 Q20

`phase02_restart_status.md` confirms slide 64 contains Q20 scoring with: 经济全球化, 两个市场两种资源, 推进制度型开放. Same file, same P2 classification.

User requirement: "2024东城一模 Q20 必须补入." Include at P2.

Add entries to Q16 suite report already started in Task 3. Check module boundary: "高水平对外开放" is 必修二 — exclude from 选必一 main table; record in `module_boundary_notes`. "深入融入经济全球化" and "两个市场两种资源联动" are 选必一 经济全球化链 — include.

### Task 5 — Log 2026西城期末 Q20 as hard blocker

Do NOT create a Q20 entry with inferred wording. The confirmed facts are:
- 细则.pdf is a scanned image PDF; pdfminer extracted only 5 chars — unreadable.
- 试卷/ folder is empty — no exam paper file.
- 西城高三期末评标.pptx has 12 slides but does not show Q20 选必一 scoring rubric.
- 高三思想政治参考答案.pdf confirms Q20 topic is China's climate governance (巴黎协定/碳市场/绿色转型) at P1 reference-answer level only.

Decision path:
- If an OCR tool (e.g., `tesseract`, `ocrmypdf`, or system Preview/Vision OCR) is available locally, attempt OCR of `细则.pdf` and record the result in `claudecode_lane/claudecode_blockers_phase02.md`.
- If OCR succeeds and extracts readable scoring text for Q20, upgrade to appropriate evidence level and create provisional entry.
- If OCR fails or is unavailable, record the blocker as `UNRESOLVED — requires user decision`. The P1 reference answer text may be noted as fallback but must not be promoted to 细则位置.

Write finding to `claudecode_lane/claudecode_blockers_phase02.md`.

### Task 6 — Sweep next-priority P0-candidate suites

From `claudecode_lane/claudecode_evidence_level_recheck.csv`, the following sources are `P0_candidate` with named 评标/细则 files that have not yet been extracted:

Priority order (highest expected 选必一 yield first):
1. `2026东城一模` — `细则/分题细则/东城一模评标细则（勿传）/` contains PPTX files per-question. Extract slides for Q16–Q20. Check for 选必一 terms.
2. `2025丰台二模` — `细则/分题细则/2025丰台二模评标细则/` contains doc/docx files. Extract Q20/Q21 area.
3. `2024朝阳期中` — `细则/补充材料/2024.11期中政治朝阳评标2.docx` file name contains 评标. Extract and classify.
4. `2025朝阳一模` — `细则/补充材料/` contains 3 阅卷总结 doc files. Extract each.
5. `2025海淀二模` — `细则/补充材料/2025年海淀二模评标实录.docx`. File name contains 评标实录 — high-priority P0 candidate.

For each: use short text extraction (max ~600 chars per paragraph/slide). Identify 选必一 subjective questions by question number cross-referenced against exam paper. Record: verified evidence level, question numbers, 选必一 terms found, module boundary notes. Write suite report under `claudecode_lane/claudecode_suite_reports_phase02/`.

Do not read full PDFs or large images. If a file is scanned or image-based, record `needs_ocr` and skip.

### Task 7 — Sweep remaining suites at batch level

For all remaining `not_started` suites in `03_entries/suite_question_matrix.csv` that have P0_candidate 细则 DOCX/PPTX files (not scanned PDFs):

Use a consistent triage pass: extract file, check for 政治/国际/联合国/全球化 key terms in scoring text, identify question numbers, and record one of: `no_xuanbiyi_entry`, `provisional_entry_needs_verification`, or `blocked_needs_ocr`.

Do not attempt to produce full entries in this pass — only determine which suites have 选必一 subjective scoring content and which do not. Update `claudecode_lane/claudecode_evidence_level_recheck.csv` after each batch of 10 suites.

### Task 8 — Update matrices and write entries JSONL

After Tasks 1–7, write or update:
- `claudecode_lane/claudecode_xuanbiyi_subjective_index.csv` — all closed and provisional entries
- `claudecode_lane/claudecode_entries_phase02.jsonl` — one JSON object per entry, including entry_id, source_id, scoring_term, term_function, evidence_level, bucket, question_full_text, 细则位置, answer_sentence
- `claudecode_lane/claudecode_evidence_level_recheck.csv` — all processed sources with final or provisional evidence level

### Task 9 — Produce six-bucket student draft

Write `claudecode_lane/claudecode_student_draft_phase03.md`.

Structure: six top-level sections (时代背景 / 理论 / 经济全球化 / 政治多极化 / 中国 / 联合国). Under each section, group entries by scoring term. Each entry uses the exact format from `xuanbiyi-term-protocol.md`:

```
**术语：<rubric original phrase(s)>**（出现N次）

- 完整设问：<full question prompt>
- 细则位置：<suite + question + scoring point + score + evidence level>
- 来源：<year district exam + question>
- 材料触发：<why this material relation triggers this term>
- 答案句：<candidate answer sentence>
```

Rules for this draft:
- Include all `closed_P0` entries without qualification.
- Include `closed_P2` entries with evidence level shown in 细则位置, e.g.: "2024东城一模 Q16 slide26阅卷细则 — P2证据级别".
- Include `provisional_P1` entries only if Codex has confirmed the source in `03_entries/xuanbiyi_subjective_index.csv`; mark as `[P1待融合确认]`.
- Exclude `provisional_blocker` entries (e.g. 2026西城期末 Q20 unless OCR succeeded in Task 5).
- Do NOT include: local paths, source_ids, audit/debug language, model chatter, backstage scoring language (`采分点`, `要落到`, `细则要求`, `v7`, `材料中`, `评标`).
- Mark the document header: `DRAFT — PENDING CODEX FUSION AND GOVERNOR REVIEW. NOT FINAL.`

### Task 10 — Write completion report

Write `claudecode_lane/claudecode_phase03_completion_report.md` listing:
- Total suites processed and closed
- Total entries by evidence level (P0 / P2 / P1 / blocked)
- Open blockers (especially 2026西城期末 Q20)
- P2 entries pending Codex evidence review
- Suspected conflicts with Codex entries (reference `06_conflicts/conflict_register.md`)
- G11 trigger objects produced: outline (yes/no), section_batch (yes/no), final_markdown (yes/no), word_pdf (yes/no)
- Any 413/payload risk encountered and how it was avoided

---

## 3. Small-Context ClaudeCode Restart Prompt

Codex: paste this into a new ClaudeCode screen session if `xuanbiyi_claudecode_phase02_restart_20260502` stops. Adjust task numbers to reflect what is already done.

---

```
You are ClaudeCode running the independent production lane for 选必一《当代国际政治与经济》主观题 from-zero rerun.

Run folder: /Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_从0重跑_GPT55内容监督_ClaudeCode完整复跑_2026-05-02
Your output directory: claudecode_lane/

FIRST: Read these files before doing any other work. Read them one at a time with short targeted reads.
1. MASTER_REQUIREMENTS.md
2. 00_control/GOVERNOR_GATES.md
3. claudecode_lane/phase02_restart_status.md
4. claudecode_lane/claudecode_evidence_level_recheck.csv (first 20 rows)
5. claudecode_lane/claudecode_xuanbiyi_subjective_index.csv (first 20 rows)
6. 06_conflicts/conflict_register.md
7. 08_review/claude_commander/claude_overnight_commander.md (Tasks section)

HARD CONSTRAINTS:
- Never read a full PDF, DOCX, PPTX, or image file as a single payload. Use pdfminer/python-docx/python-pptx to extract max ~600 chars per paragraph or slide.
- Never invent question wording when the original paper file is missing. Record as blocker.
- Never copy entries from Codex lane files (03_entries/) or from old run folders.
- Never include paths, source_ids, audit language, model chatter, or backstage scoring language in student-facing text.
- Never mark a suite as complete without a written suite report file in claudecode_lane/claudecode_suite_reports_phase02/.
- Do not exceed ~20MB of total file reads per session. If you are about to read a large binary, extract a short snippet instead.

PRIMARY TASKS (ordered):
1. Resolve conflict C-2025HDQZ: read 02_extraction/codex_extraction_logs/2025海淀期中/docx_media/image2.png and image8.png; confirm Q16(2) and Q21(2) scoring details; update claudecode_evidence_level_recheck.csv and claudecode_xuanbiyi_subjective_index.csv for these entries.
2. Close 2025海淀期末 Q22 at P2 (slides 61-62 of 细则.pptx confirmed by prior extraction).
3. Close 2024东城一模 Q16 at P2 (slide 26 of 细则.pptx confirmed).
4. Close 2024东城一模 Q20 at P2 (slide 64 of 细则.pptx confirmed). Check module boundary for 高水平对外开放 (必修二 — exclude).
5. Log 2026西城期末 Q20 as HARD BLOCKER. Attempt OCR of 细则.pdf if tool available. Do NOT invent wording.
6. Sweep P0-candidate suites: 2026东城一模, 2025丰台二模, 2024朝阳期中, 2025朝阳一模, 2025海淀二模 — extract scoring files and classify.
7. Write claudecode_entries_phase02.jsonl with all closed entries.
8. Write claudecode_student_draft_phase03.md in six-bucket format using only closed_P0 and closed_P2 entries. Header must say DRAFT — PENDING CODEX FUSION AND GOVERNOR REVIEW.
9. Write claudecode_phase03_completion_report.md.

Report any blocker in claudecode_blockers_phase02.md. Do not stop silently.
```

---

## 4. Risks That Would Create False Completion

These conditions would produce a file that looks done but contains fabricated or unverifiable content:

| Risk | Specific Failure Mode |
|---|---|
| Inferred question wording | 2026西城期末 Q20 — paper folder is empty. If ClaudeCode writes 完整设问 using inferred text from the reference answer, the entry is invalid. |
| P2 promoted to P0 | 2025海淀期末 Q22 and 2024东城一模 Q16/Q20 are P2 (teacher training / trial analysis PPTs). If 细则位置 is written as if these are formal scoring rubrics, entries are inflated. |
| Image scoring skipped again | 2025海淀期中 Q16(2)/Q21(2) — the embedded-image scoring detail was missed in the first ClaudeCode run. If ClaudeCode skips the image check in Task 1 and keeps P1 classification, the conflict is unresolved and entries are underclassified. |
| Module boundary violation | 2024东城一模 Q20 contains `高水平对外开放` (必修二) alongside 选必一 terms. If both are listed as 选必一 entries, the artifact violates module boundary. Same risk for any suite containing dual-module questions. |
| Backstage language in student text | 答案句 or 材料触发 containing `采分点`, `细则要求`, `v7`, `评标`, paths, source_ids, or model chatter would fail G7. |
| Early completion claim | ClaudeCode writing a final student document before Codex fusion and before G5 question-level matrix is verified. |
| Large-payload 413 recurrence | Loading a full scanned PDF or large PPTX as a single payload will terminate the session. Particularly at risk: 2026东城一模 分题细则 PPTXs and any PDF in 2025/2026 期末 folders. |

---

## 5. Governor Checks Before Final Markdown, DOCX, and PDF Promotion

Codex must confirm each gate passes before promoting artifacts. Partial PASS on individual gates is not total PASS.

| Gate | Required Evidence Before Promotion |
|---|---|
| G2.5 source eligibility | Every source in the final student artifact's entries must have a verified evidence level row in `03_entries/evidence_level_recheck.csv`. No `pending_content_recheck` entries allowed in included content. |
| G3 non-text handling | Every entry that originated from a PDF, PPTX, or embedded image must record how the non-text content was handled (extracted snippet, rendered slide, OCR, or blocked). No silent assumptions about scanned content. |
| G4 evidence levels | Confirm: P0 entries have explicit scoring source locators (file + slide/section + point). P2 entries are labeled P2 in 细则位置. P1 entries are not in 细则位置 position. Blocked entries are not in the student artifact. |
| G5 coverage | Question-level matrix must exist for all suites that contributed entries. Confirm `suite_question_matrix.csv` has rows for each included suite with `contains_xuanbiyi_subjective=yes`. |
| G6 conflicts | Conflict register must show `resolved` or `codex_decided` for all registered conflicts, including `C-2025HDQZ-evidence-level`. Unresolved conflicts block final Markdown. |
| G7 student transfer | Final Markdown must pass a residue check: no local paths, no source_ids (SRC_xxx), no `采分点`, `细则要求`, `v7`, `评标`, `设问要求`, `debug`, `OCR`, `model`, `status`, or `phase` chatter. Run a grep/search pass before promotion. |
| G8 Word/PDF visual QA | After DOCX/PDF generation, visually check: six-bucket headings render, term entries are formatted as expected, no raw CSV/JSONL artifacts leaked into document, no Chinese encoding artifacts. If Microsoft Word is unavailable, record this explicitly and perform the strongest available local check. |
| G9 Confucius | Artifact-only learning verification: read final Markdown as if you are a student; confirm every entry teaches something usable for 选必一 exam; flag any entry that reads as meta-instruction or production note. |
| G11 outline | Send sanitized outline to GPT-5.5 Pro via clipboard paste into open Safari ChatGPT Pro thread. Save raw response. Digest corrections. If GPT unavailable, log fallback — late review required before PASS. |
| G11 section_batch | Send each six-bucket section to GPT for content review. Save review per batch. Patch any `must_fix_content` items verified against local source. |
| G11 final_markdown | Send final Markdown in chunks to GPT. Record full correction log in `08_review/gpt_content_review/content_correction_log.md`. Markdown PASS and Word/PDF PASS are separate. |
| G12 overnight delivery | All above gates PASS or logged with explicit fallback/waiver. `FINAL_ACCEPTANCE_REPORT.md` written with: gate-by-gate status, remaining blockers, ClaudeCode comparison record, GPT review log record. |

---

## 6. ClaudeCode Outputs Required Under claudecode_lane/ Before Codex Fusion

Codex must not begin fusion until all of the following exist and are readable:

| File | Required Content |
|---|---|
| `claudecode_lane/claudecode_source_inventory_phase02.csv` | All sources ClaudeCode reviewed with file path, file type, evidence level classification, xuanbiyi status |
| `claudecode_lane/claudecode_evidence_level_recheck.csv` | Updated with Task 1 P0 upgrade for 2025海淀期中; P2 closure for 2025海淀期末 Q22 and 2024东城一模 Q16/Q20; blocker status for 2026西城期末 Q20 |
| `claudecode_lane/claudecode_xuanbiyi_subjective_index.csv` | All closed and provisional entries with correct evidence levels |
| `claudecode_lane/claudecode_entries_phase02.jsonl` | One line per entry; required fields: entry_id, source_id, scoring_term, evidence_level, bucket, 完整设问, 细则位置, answer_sentence |
| `claudecode_lane/claudecode_suite_reports_phase02/` | One `.md` file per processed suite |
| `claudecode_lane/claudecode_hard_sample_tongzhou_q20.md` | Hard sample verification report for 2026通州期末 Q20 |
| `claudecode_lane/claudecode_hard_sample_chaoyang_q17.md` | Hard sample verification report for 2026朝阳期中 Q17 |
| `claudecode_lane/claudecode_blockers_phase02.md` | All unresolved blockers, especially 2026西城期末 Q20 OCR status |
| `claudecode_lane/claudecode_conflicts_suspected.md` | Any entries where ClaudeCode result differs from Codex result in scoring term or evidence level |
| `claudecode_lane/claudecode_student_draft_phase03.md` | Six-bucket student draft; marked DRAFT; no backstage language; P2 entries labeled |
| `claudecode_lane/claudecode_phase03_completion_report.md` | Final summary with suite counts, entry counts by level, open blockers, G11 trigger status |

Fusion precondition: Codex reads `claudecode_conflicts_suspected.md` and `06_conflicts/conflict_register.md` together and resolves every discrepancy against local source evidence before writing any merged entry into the main artifact.

---

## 7. Codex Verification Requirement

**Codex must verify all content against local evidence before final inclusion.**

This applies without exception to:
- Every scoring term in the final student artifact — verify the exact phrase appears in a local source file (scoring rubric, 评标, or marking report), not only in a ClaudeCode output.
- Every P2 entry — verify the slide or section reference is real; do not accept "slide 62 says X" without confirming ClaudeCode's extraction matches the actual slide content.
- Every 答案句 — verify it contains no backstage language and that the material fact cited exists in the question material.
- Every 细则位置 — verify the suite, question number, and scoring point reference is internally consistent and does not cite a source that Codex has not itself confirmed.
- All module boundary decisions — verify that no 必修二/选必二/选必三 term appears in the 选必一 main table without an explicit user-confirmed cross-module note.

ClaudeCode's `claudecode_student_draft_phase03.md` is a candidate draft, not a final artifact. Codex owns the merge, the correction log, and the final student Markdown.

---

*End of commander packet.*
