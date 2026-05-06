# Phase 01 Framework And Candidate Inventory Summary

phase_name: `phase_01_framework_inventory`

phase_goal: absorb the user's two PDF frameworks and build a first-pass candidate inventory for 选必三《逻辑与思维》 split into 思维部分 and 推理部分.

completed_actions:

- Created the run folder and control files for the 2026-05-04 four-lane run.
- Copied the two user-uploaded PDFs into `00_source_pdfs/`.
- Extracted PDF text and rendered first pages with PyMuPDF because Poppler tools were unavailable.
- Wrote `MASTER_REQUIREMENTS.md` and `USER_FRAMEWORK.md`.
- Scanned 282 local readable text/cache files.
- Generated candidate ledgers:
  - `01_source_inventory/logic_candidate_hits.csv`
  - `01_source_inventory/logic_candidate_hits_enriched.csv`
  - `01_source_inventory/thinking_candidate_hits.md`
  - `01_source_inventory/reasoning_candidate_hits.md`
  - `01_source_inventory/candidate_suite_summary.md`
  - `03_entries/thinking_formal_candidate_shortlist.csv`
  - `03_entries/reasoning_formal_candidate_shortlist.csv`

unfinished_actions:

- Original-source recheck for every promoted candidate.
- Pairing paper question text, four options/objective answers where needed, and formal scoring source.
- ClaudeCode production lane B is running.
- GPT-5.5 Pro and Claude Opus real external review/writer gates are not yet satisfied.
- No final student-facing draft has been produced yet.

changed_artifacts:

- Framework/control files in the run folder.
- PDF extraction/rendering files.
- Candidate scan scripts under `tools/`.
- Candidate ledgers under `01_source_inventory/` and `03_entries/`.

source_coverage_summary:

- Text/cache files scanned: 282.
- Total raw hits: 3947.
- Thinking hits: 2236.
- Reasoning hits: 1711.
- Enriched rows mapped back to source/suite metadata: 3223.
- Formal/support shortlist rows:
  - 思维部分: 929.
  - 推理部分: 776.

non_text_material_summary:

- User PDFs were rendered and extracted.
- Raw district PDF/Word/PPT sources are not fully re-rendered yet in this phase; that is the next evidence-lock step.

evidence_level_counts_P0_P1_P2_P3_P4:

- Current phase uses candidate-level labels only, not final evidence levels.
- Formal/rubric-like and lecture-support hits were separated from paper/answer/index hits.
- Old 选必三 artifacts are marked as index-only, not evidence.

missing_suites_questions_or_file_types:

- Need original-source verification for all high-value candidates.
- Need special handling for choice questions: question stem + four options + reliable answer key.
- Need explicit exclusion or boundary notes for cross-module hits and 2026石景山期末.

codex_vs_claudecode_differences:

- Pending. ClaudeCode B lane has been launched and will write independent matrices under `claudecode_lane/`.

conflict_summary:

- Current noise risks:
  - "或者" and generic logic wording create false 选言推理 hits.
  - Negative/rubric-warning lines can look like positive method support.
  - 必修四哲学 and general system-thinking rubrics can be mistaken for 选必三思维.
  - Some cache rows lack precise question anchors.

blockers:

- No hard blocker for local evidence work.
- Final promotion is blocked until real GPT-5.5 Pro review, Claude Opus teaching pass, Governor, Confucius, and Word/PDF verification.

governor_gate_status:

- Phase 01 local inventory gate: provisional OK.
- Final gates: not run.

three_uncertainties:

1. Which 2026 二模/后续 materials are present in all source roots beyond the existing caches.
2. Whether every high-priority cache hit has a complete original paper/scoring pair available.
3. Whether some "系统观念" rows should be treated as 选必三思维, 必修四哲学, or broader cross-module boundary.

most_likely_missing_material_types:

- Scanned PDF rubrics whose text extraction is partial.
- PPT讲评 slides with scoring tables.
- Choice-question answer keys and option images/tables.

most_likely_evidence_level_mislabels:

- Lecture-support rows mislabeled as formal scoring.
- Ordinary answer/reference rows that mention thinking terms but are not rubrics.
- Negative-warning rubric lines counted as positive support.

most_likely_student_misleading_phrases:

- "可从……角度作答"
- "参考答案"
- "评标/细则"
- "A-formal/B-choice-signal"
- "source/path/line id/OCR"

do_not_enter_student_doc_list:

- Local paths, source ids, cache ids, OCR/debug notes.
- Evidence status fields.
- Old artifact conclusions not rechecked against original sources.
- 2026石景山期末 unless new scoring source appears.

questions_for_gpt_commander:

1. Is the split design right: 思维部分 as philosophy-style trigger chains, 推理部分 as type-family solution protocols?
2. Which formal/support candidate clusters should be promoted first for source recheck?
3. What mistakes are most likely if we turn the current candidate shortlists into a student-facing artifact?
4. What should ClaudeCode B prioritize so it complements Codex A rather than duplicating it?
5. What acceptance checks would you require before final Word/PDF delivery?

candidate_next_tasks:

- Codex A: verify high-value thinking clusters from formal scoring sources first.
- ClaudeCode B: independent matrices and blocker/conflict list.
- GPT-5.5 Pro: phase commander recommendation.
- Claude Opus: wait until evidence pack is locked before teaching-text rewrite.
