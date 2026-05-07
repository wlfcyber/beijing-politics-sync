# ClaudeCode P1 Recheck Relaunch

You are the real ClaudeCode CLI running inside the run directory for the
Xuanbisan two-lane closure job. This is a repair relaunch after two failed P1
attempts. Do not write final artifacts, Word, PDF, or delivery files.

Use relative paths from the current working directory.

Inputs:

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`
- `fusion/p1_recheck_sources/P1_SOURCE_TEXT_INDEX.csv`
- `fusion/p1_recheck_sources/`
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P0_PATCHED.md`
- `claudecode_lane/p1_recheck/SUPERVISOR_PATCH_01_FALSE_PROGRESS.md`
- `claudecode_lane/p1_recheck/SUPERVISOR_PATCH_02_REPAIR_STALL_AND_RELAUNCH.md`

Write outputs only under:

- `claudecode_lane/p1_recheck/`

Required output files, in this exact order:

1. `P1_RECHECK_DECISIONS.csv`
2. `P1_RECHECK_PATCHES.jsonl`
3. `P1_SOURCE_EVIDENCE.md`
4. `P1_RECHECK_ACCEPTANCE.md`
5. update `PROGRESS.md`

Do not write only progress. If a source is uncertain, still write the row with
`source_insufficient`; never leave the deliverable missing.

Scope:

- Filter the manifest to `priority=P1`.
- There must be exactly 11 decision rows.
- Do not add P0 or P2 rows.
- Do not use the student-facing phrase `固定分析流程`.

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

JSONL fields, one valid JSON object per P1 row:

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

Evidence rules:

- `A-formal`: formal scoring rubric, marking rule, evaluation report, or explicit
  scoring source matched to the suite and question.
- `A-support`: teacher/reference/lecture material with explicit answer language
  but not a formal scoring rubric.
- `B-choice-signal`: choice question only.
- Do not invent rubrics or promote an ordinary reference answer to `A-formal`.

Known P1 source hints to verify from files:

- `017_*评标docx.docx.txt` contains the Chaoyang Q18 scoring language for both
  Chuwang incomplete induction and Yanzi analogical reasoning.
- `046_*19（4）.pptx.txt` and/or `046_*26东城一模细则.pdf.txt` contain Dongcheng
  Q19(4) scoring language for innovation thinking, super-advanced thinking, and
  system/analysis-synthesis linkage.
- `040_*2025丰台期末细则.pptx.txt` contains Fengtai Q18(1) scoring language for
  necessary conditional judgment and conjunction judgment.
- `035_*2025顺义一模细则.docx.txt` contains Shunyi Q17(1) scoring language for
  sufficient conditional judgment, necessary conditional judgment, and compatible
  disjunctive judgment.

Acceptance report requirements:

- state `P1_RECHECK_ACCEPTANCE: NOT_FINAL`
- state exact row count and patch count
- state whether every manifest P1 key is resolved
- state that no Word/PDF/final artifact was produced
- list any `source_insufficient` or `can_enter_fusion=no` rows

Progress update requirements:

- explicitly say the earlier false progress is corrected
- list the five output files written in this relaunch
- do not mark final or Governor closure as passed

Begin by writing `P1_RECHECK_DECISIONS.csv`.
