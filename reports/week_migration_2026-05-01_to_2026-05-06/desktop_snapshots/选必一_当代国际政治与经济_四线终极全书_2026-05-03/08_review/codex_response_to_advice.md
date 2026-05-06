# Codex Response To Advice

## Phase 01 GPT-5.5 Pro Commander Advice Digest

Raw advice file: `08_review/gpt_phase_advice/phase_01_gpt.md`

Overall decision: partially accepted. GPT gave `条件 GO`, which matches Codex Governor Round 2: proceed to evidence locking, dual-lane first outputs, and merge-rule stress testing; do not proceed to student final, Word/PDF, final Governor, or Confucius yet.

| suggestion_id | raw_gpt_suggestion_summary | decision | reason | local_task_created | local_evidence_to_check | execution_status | affects_student_doc | follow_up_phase |
|---|---|---|---|---|---|---|---|---|
| GPT01-01 | Push 11 high-priority questions from candidate state into evidence-locked cards before expanding scope. | accepted | This matches current Governor condition and prevents false closure. | Create/complete worker evidence cards and source notes for priority questions. | Source ledger, worker source notes, current source files, visual/table evidence. | in_progress | no | Phase 2 |
| GPT01-02 | Do not enter student final or Word/PDF until Codex A worker, patcher, Governor, and ClaudeCode outputs are present. | accepted | Current worker appeared, patcher/Governor Batch 01 are running, ClaudeCode still writing entries. | Gate fusion on Patcher Batch 01, Governor Batch 01, and ClaudeCode lane B outputs. | `codex_lane/agents/*`, `claudecode_lane/*`, Governor gate. | in_progress | yes later | Phase 3 |
| GPT01-03 | Build evidence-card fields: source status, scoring-source boundary, core prompt, material trigger, student-eligible terms, blocked content, disputes, evidence level. | accepted | Strongly compatible with xuanbiyi protocol and solves cache-only risk. | Convert worker batch output into evidence-card/fusion-candidate structure after Governor pass. | Worker entries, source notes, P0/P1/P2 labels. | pending | yes later | Phase 3 |
| GPT01-04 | Separate six-bucket term learning from per-question answer reconstruction. | accepted | This directly addresses the user's concern that six-bucket indexing alone is not enough for students. | Ask Claude Opus for teaching layout; later create both six-bucket and by-question views. | Claude Opus advice, local verified entries. | in_progress | yes | Phase 5 |
| GPT01-05 | Add specific merge-risk checks for era theme, economic-globalization direction, China diplomacy terms, new-type international relations, and trade friction. | accepted | This matches latest skill updates and user corrections. | Patcher Batch 01 review and fusion merge register. | Patcher review, worker terms, ClaudeCode challenge entries. | in_progress | yes | Phase 3 |
| GPT01-06 | Treat non-text sources as needing visual/table recheck before promotion. | partially_accepted | Non-text sources can be promoted when directly visually verified or user-confirmed; not every non-text item must remain uncertain. | Keep visual read notes for 2025 Haidian images and P2/PPT boundary notes. | Embedded images, PPT slide labels, scanned render pages. | in_progress | yes later | Phase 2 |
| GPT01-07 | Run Confucius as transfer tests rather than just aesthetic review. | accepted | Matches Garden final acceptance rule. | Add Confucius transfer checks after student artifact exists. | Final Markdown/DOCX/PDF only. | pending | yes | Phase 7 |

Immediate Codex-owned tasks from GPT advice:

1. Finish Patcher Batch 01 and Governor Batch 01 on the worker output.
2. Wait for ClaudeCode `claudecode_entries.md`, `missing_blockers.md`, `conflicts_for_codex.md`, and suite report index, then create an A/B difference table before merging.
3. Keep 2025 Haidian embedded image scoring evidence separated from ordinary reference-answer text.
4. Do not generate student final until evidence lock and merge checks pass.
