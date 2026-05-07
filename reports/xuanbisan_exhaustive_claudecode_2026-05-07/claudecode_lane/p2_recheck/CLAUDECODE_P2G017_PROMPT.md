# ClaudeCode P2G017 P2 Source Group Recheck

You are the real ClaudeCode CLI. This is a small source_id-level P2 run after
larger P2 runs stalled without file output.

Use relative paths from the current working directory. Do not write Word, PDF,
delivery, or final artifacts.

Inputs:

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`
- `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv`
- `fusion/p2_recheck_sources/`
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P1_PATCHED.md`

Write outputs only under `claudecode_lane/p2_recheck/`.

Required output files:

1. `P2G017_RECHECK_DECISIONS.csv`
2. `P2G017_RECHECK_PATCHES.jsonl`
3. `P2G017_SOURCE_EVIDENCE.md`
4. `P2G017_RECHECK_ACCEPTANCE.md`
5. `P2G017_PROGRESS.md`

Scope:

- Filter manifest rows to `priority=P2`.
- Include only these source_id values:
  - `017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf`
- There must be exactly 3 decision rows.
- Do not add any other P2 rows.

CSV header:

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

Allowed decisions:

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

JSONL fields:

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

Rules:

- Verify stem/options and answer key before confirming choice-trap rows.
- Use the manifest evidence_level exactly unless the source genuinely proves the
  row is misclassified; explain any exception.
- Do not invent options, answers, rubrics, or source files.
- If answer evidence is unavailable, mark `source_insufficient` and
  `can_enter_fusion=no`.
- Acceptance must state `P2G017_RECHECK_ACCEPTANCE: NOT_FINAL`, exact row
  count 3, patch count 3, no Word/PDF/delivery.

Begin by writing `P2G017_RECHECK_DECISIONS.csv`.
