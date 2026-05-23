# Xuanbiyi Strict Final Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the strict final version of the Xuanbiyi subjective-question handbook from all 2024/2025/2026 desktop mock-exam materials.

**Architecture:** Use a staged evidence pipeline: source inventory, text extraction, subjective-question scope table, rubric-location table, current-handbook coverage diff, batch source packets, four-lane model production, final merge, and governor verification. Keep generated evidence and outputs under `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23`.

**Tech Stack:** PowerShell, Python 3, existing repository scripts, Office/PDF extraction helpers, Markdown/CSV/JSON outputs, Word generation with existing `build_xuanbiyi_docx.py`.

---

### Task 1: Build Full Source Inventory

**Files:**
- Create: `scripts/xuanbiyi_strict_inventory_sources.py`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/00_source_inventory.csv`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/00_source_inventory.md`

- [ ] Enumerate these roots exactly: `C:\Users\Administrator\Desktop\2024各区模拟题`, `C:\Users\Administrator\Desktop\2025各区模拟题`, `C:\Users\Administrator\Desktop\2026各区模拟题`.
- [ ] Classify each file as `paper`, `rubric`, `answer`, `lecture`, `ocr`, or `other` by filename and parent directory signals.
- [ ] Write a CSV with absolute path, year, district/suite guess, exam stage guess, file role, extension, size, and modified time.
- [ ] Write a Markdown summary grouped by year and folder.

### Task 2: Extract Text and Build Search Cache

**Files:**
- Create: `scripts/xuanbiyi_strict_extract_sources.py`
- Create directory: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/01_extracted_text`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/01_extraction_log.csv`

- [ ] Reuse extraction patterns from `scripts/cc_independent_extract.py` for docx, pdf, pptx, and old doc binary scans.
- [ ] For every source file, write one `.txt` cache file keyed by a stable short hash and original filename.
- [ ] Log extraction method, character count, success flag, and error message.
- [ ] Mark weak or short PDF/PPT extraction as `needs_ocr_or_render_review` rather than treating the source as absent.

### Task 3: Locate Subjective Questions and Rubric Evidence

**Files:**
- Create: `scripts/xuanbiyi_strict_scope_questions.py`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/02_subjective_question_scope.csv`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/02_subjective_question_scope.md`

- [ ] Identify subjective question candidates from extracted paper text and scoring text using question markers such as `16.`, `第16题`, `16（1）`, `20(2)`, and section headings.
- [ ] For each candidate, record suite, question id, paper text evidence, matched rubric/answer/lecture files, and current evidence status.
- [ ] Use `细则未定位` when evidence is not found after current pass; do not use `无细则`.
- [ ] Flag likely Xuanbiyi candidates using query terms from the skill protocol, including 国际政治与经济, 世界多极化, 经济全球化, 国家利益, 共同利益, 新型国际关系, 全球治理, 人类命运共同体, 中国方案, 联合国.

### Task 4: Compare Against Current Handbook

**Files:**
- Create: `scripts/xuanbiyi_strict_compare_coverage.py`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/03_coverage_diff.csv`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/03_coverage_diff.md`

- [ ] Parse sources from current student handbook, existing entry JSON, BATCH_014, the 12-item anti-merge audit, and 2026 second-mock scope table.
- [ ] Mark each scoped question as `already_in_main`, `needs_rebuild`, `must_backfill`, `candidate_review`, `strict_exclude`, or `evidence_not_located`.
- [ ] Force include the 12 anti-merge residuals and 2026二模 顺义Q20 / 丰台Q22 / 房山Q21 / 丰台Q20 in the review queue.

### Task 5: Produce Batch Source Packets

**Files:**
- Create: `scripts/xuanbiyi_strict_make_source_packets.py`
- Create directory: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/04_source_packets`

- [ ] Group review-queue questions into source packets by suite and topic, keeping each packet small enough for GPT Pro and Claude Opus review.
- [ ] Each packet must include exact source file paths, extracted text snippets, question prompt, rubric text, evidence status, and required output schema.
- [ ] Each packet must instruct models that question examples cannot be merged at the题例 layer.

### Task 6: Four-Lane Production and Review

**Files:**
- Create directories: `05_codex_drafts`, `06_claudecode_drafts`, `07_gpt_pro_fusion`, `08_claude_opus_review`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/MODEL_EVIDENCE_LEDGER.md`

- [ ] Generate Codex independent thick drafts from each source packet.
- [ ] Run ClaudeCode Opus 4.7 for independent thick drafts from the same source packets.
- [ ] Submit Codex and ClaudeCode drafts to GPT Pro for main fusion; save the captured output.
- [ ] Submit GPT Pro fusion output to Claude Opus 4.7 Adaptive for review and improvement; save the captured output.
- [ ] Record model, prompt path, output path, and any downgrade in `MODEL_EVIDENCE_LEDGER.md`.

### Task 7: Merge, Rebuild, and Verify Final Handbook

**Files:**
- Modify: `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_学生版.md`
- Modify: `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md`
- Modify: Word outputs with `scripts/build_xuanbiyi_docx.py`
- Create: `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/FINAL_STRICT_GOVERNOR_AUDIT.md`

- [ ] Merge only evidence-backed entries into the six-bucket handbook.
- [ ] Keep every example single-question; do not combine two source questions in one heading or one题例.
- [ ] Rebuild Word outputs.
- [ ] Run anti-merge search, field completeness checks, coverage checks, and current validator.
- [ ] Write final governor audit with pass/fail status and residual evidence gaps if any.
