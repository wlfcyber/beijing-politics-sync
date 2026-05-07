# ClaudeCode P2A Recheck

You are the real ClaudeCode CLI. This is the split P2A run after the full P2
run stalled without file output.

Use relative paths from the current working directory. Do not write Word, PDF,
delivery, or final artifacts.

Inputs:

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`
- `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv`
- `fusion/p2_recheck_sources/`
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P1_PATCHED.md`

Write outputs only under:

- `claudecode_lane/p2_recheck/`

Required output files:

1. `P2A_RECHECK_DECISIONS.csv`
2. `P2A_RECHECK_PATCHES.jsonl`
3. `P2A_SOURCE_EVIDENCE.md`
4. `P2A_RECHECK_ACCEPTANCE.md`
5. `P2A_PROGRESS.md`

Scope:

- Filter manifest rows to `priority=P2`.
- Include only these source_ids:
  - `017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf`
  - `003_Desktop_2026模拟题_2026各区期末和期中_2026朝阳期中_试卷_试卷.pdf`
  - `012_Desktop_2025模拟题_2025各区期末_2025东城期末_试卷_试卷.pdf`
  - `046_Desktop_2026模拟题_2026各区一模_2026东城一模_试卷_试卷.pdf`
  - `044_Desktop_2026模拟题_2026各区期末和期中_2026东城期末_试卷_试卷.pdf`
- There must be exactly 17 decision rows.
- Do not add P0, P1, or P2B rows.

CSV header:

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

Allowed `decision` values:

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

JSONL fields:

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

P2A emphasis:

- These are mostly choice traps. Verify stem/options and answer key before
  confirming.
- 2026 Dongcheng Yimo Q5 and Q7 have answers visible in the paper answer table;
  do not keep old answer-missing blocker without checking the source.
- Use `B-choice-signal` for choice rows.
- If a choice answer is not reliable after source checking, use
  `source_insufficient` and `can_enter_fusion=no`.

Acceptance:

- state `P2A_RECHECK_ACCEPTANCE: NOT_FINAL`
- state exact row count 17 and patch count 17
- list any no-fusion or insufficient rows
- state no Word/PDF/delivery artifact was produced

Begin by writing `P2A_RECHECK_DECISIONS.csv`.
