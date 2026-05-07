# ClaudeCode P2 Recheck

You are the real ClaudeCode CLI running inside the run directory for the
Xuanbisan two-lane closure job. This phase verifies the remaining P2 rows after
P0 and P1 have passed Codex QA.

Use relative paths from the current working directory. Do not write Word, PDF,
delivery, or any final artifact.

Inputs:

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`
- `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv`
- `fusion/p2_recheck_sources/`
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P1_PATCHED.md`
- `claudecode_lane/p0_recheck/P0_RECHECK_QA.json`
- `claudecode_lane/p1_recheck/P1_RECHECK_QA.json`

Write outputs only under:

- `claudecode_lane/p2_recheck/`

Required output files, in this exact order:

1. `P2_RECHECK_DECISIONS.csv`
2. `P2_RECHECK_PATCHES.jsonl`
3. `P2_SOURCE_EVIDENCE.md`
4. `P2_RECHECK_ACCEPTANCE.md`
5. `PROGRESS.md`

Scope:

- Filter the manifest to `priority=P2`.
- There must be exactly 39 decision rows.
- Do not add P0 or P1 rows.
- Do not use banned student-facing workflow wording from the Garden rules.

CSV header:

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

Allowed `decision` values:

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

Allowed `can_enter_fusion` values:

- `yes`
- `no`

JSONL fields, one valid JSON object per P2 row:

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

P2-specific rules:

- Most P2 rows are choice-trap signals. For these, verify the stem/options and
  answer key from the extracted paper/answer source. Use `B-choice-signal`, not
  main-question rubric language.
- If a choice row lacks a reliable answer key after checking extracted sources,
  mark `source_insufficient` and `can_enter_fusion=no`.
- `2025丰台期末 Q16` is A-support but mainly philosophy/boundary material. Do
  not force it into the Xuanbisan student body. Use `block_from_student_body` or
  `downgrade_to_index` if that is the correct evidence decision.
- Do not invent options, answers, rubrics, or source files.
- For each choice-trap patch, include the correct answer/trap logic in
  `patched_trigger_logic` or `patched_answer_sentence` when the source supports it.

Acceptance report requirements:

- state `P2_RECHECK_ACCEPTANCE: NOT_FINAL`
- state exact row count and patch count
- state whether every manifest P2 key is resolved
- list all `source_insufficient`, `wrong_framework`,
  `block_from_student_body`, and `can_enter_fusion=no` rows
- state that no Word/PDF/delivery artifact was produced

Begin by writing `P2_RECHECK_DECISIONS.csv`.
