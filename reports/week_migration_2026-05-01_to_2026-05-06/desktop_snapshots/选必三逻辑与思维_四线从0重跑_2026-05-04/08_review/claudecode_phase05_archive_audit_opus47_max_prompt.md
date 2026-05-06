# Opus 4.7 / Max Thinking: Phase05 Evidence Archive Audit

You are ClaudeCode Lane B for Feige Politics Garden 选必三《逻辑与思维》.

This task must run as real ClaudeCode with Opus 4.7 / maximum thinking controls:

```text
--model opus
--effort max
```

Do not use any old Sonnet output as evidence. If you find files from old ClaudeCode/Sonnet lanes, treat them only as inputs already merged by Codex A, not as your own audit conclusion.

## Mission

Independently audit Codex A Phase05 archive outputs. This is an archive/evidence gate only. You must not write a student draft, polished prose, Word/PDF, final PASS, or Claude/Opus teaching text.

Core run folder:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## Highest-Priority Rules

Read and obey:

1. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. `MASTER_REQUIREMENTS.md`
6. `00_control/NOTEBOOK_DIGEST.md`
7. `08_review/gpt_phase_advice/phase_04_batch03_gpt55_digest.md`
8. `05_coverage/phase04_batch03_cleaned_status_freeze.md`
9. `06_conflicts/phase04_batch03_choice_count_discrepancy_audit.md`
10. `06_conflicts/phase04_2024_xicheng_yimo_Q11_pairing_lock.md`
11. `06_conflicts/phase04_2025_haidian_ermo_Q12_Q13_answer_locator_lock.md`
12. `06_conflicts/phase05_archive_backcheck_report.md`

## Files To Audit

Audit these Phase05 files:

1. `05_coverage/phase05_evidence_pool_74.csv`
2. `05_coverage/phase05_evidence_pool_74.md`
3. `05_coverage/phase05_thinking_signal_archive.csv`
4. `05_coverage/phase05_thinking_signal_archive.md`
5. `05_coverage/phase05_reasoning_typology_archive.csv`
6. `05_coverage/phase05_reasoning_typology_archive.md`
7. `05_coverage/phase05_cross_question_split_matrix.csv`
8. `05_coverage/phase05_reasoning_same_type_index.md`
9. `05_coverage/phase05_L0_blocker_reason_summary.md`

Use the source tables and already-produced lane evidence when needed:

- `05_coverage/phase04_control_base_status_after_batch03_cleaned.csv`
- `claudecode_lane/phase04_laneB_targeted_verification_results.csv`
- `claudecode_lane/phase04_Aonly_76_review_batch01.csv`
- `05_coverage/phase03_codex_local_patch_addendum.csv`
- `claudecode_lane/phase03_laneB_patch_addendum.csv`
- `claudecode_lane/phase04_batch02_laneB_results_normalized.csv`
- `claudecode_lane/opus47_batch03_subjective/phase04_batch03_A_subjective_results.csv`
- `claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv`

If a locator looks weak, return to the original extracted/renders/raw source files listed by the row. Do not silently accept a weak locator.

## Required Checks

You must check:

1. The evidence pool has exactly 74 data rows and every row has stable `question_id`, `suite_id`, `source_locator`, `answer_locator`, status, and no student permission.
2. The frozen control base remains 362 rows with L4=4, L3=70, L0=288, L1=0.
3. L4 and L3 remain separated; no L3 row is described as locked/final.
4. All four L4 rows are preserved and correctly routed:
   - `Q-2025海淀二模-20`
   - `Q-2025西城二模-16-2`
   - `Q-2025西城二模-16-3`
   - `Q-2026丰台一模-18-2`
5. `2024西城一模 Q11` is locked as correct answer B with pairing B=①③. Any trace of B=①④ as the final pairing must be marked as hard failure.
6. `2025海淀二模 Q12/Q13` retain the answer locators:
   - render page 04 / original paper visible locator for question text.
   - supplemental answer source page/table locator.
   - Q12 answer D; Q13 answer C.
7. The 13 cross rows are present in `phase05_cross_question_split_matrix.csv`, and each cross row is appropriately visible in both thinking/reasoning archive context or explicitly justified if one side is boundary-only.
8. Thinking archive has 36 rows: 23 thinking rows plus 13 cross rows.
9. Reasoning archive has 51 rows: 38 reasoning rows plus 13 cross rows.
10. At least 30 percent of L3 thinking/archive rows are spot-audited against their source locator. Include all L4 thinking rows.
11. At least 30 percent of L3 reasoning/archive rows are spot-audited against their source locator. Include all L4 reasoning rows.
12. The three Batch03 count-discrepancy marginal rows retain locator, answer source, marginal/cross risk note, and no student draft:
   - `Q-2024朝阳二模-6`
   - `Q-2025丰台期末-7`
   - `Q-2026通州期末-9`
13. The 288 L0 rows remain preserved by blocker reason in `phase05_L0_blocker_reason_summary.md`; do not delete or hide blocked rows.
14. No Phase05 file authorizes student稿, Claude/Opus 成文化, Word/PDF, or final PASS.
15. No audit/debug/source-path wording is being converted into student content. Phase05 archive files may contain source locators because they are not student artifacts.

## Output Directory

Write only inside:

`claudecode_lane/opus47_phase05_archive_audit/`

Required outputs:

1. `claudecode_lane/opus47_phase05_archive_audit/phase05_laneB_archive_audit.csv`
2. `claudecode_lane/opus47_phase05_archive_audit/phase05_laneB_archive_audit.md`
3. `claudecode_lane/opus47_phase05_archive_audit/phase05_laneB_archive_audit_findings.csv`
4. `claudecode_lane/opus47_phase05_archive_audit/phase05_laneB_archive_audit_blockers.md`
5. `claudecode_lane/opus47_phase05_archive_audit/progress.md`

## CSV Schema

Use this exact header for `phase05_laneB_archive_audit.csv`:

```csv
check_id,scope,question_id,check_item,result,severity,evidence_seen,source_locator_checked,action_required,notes
```

`result` must be one of:

- `PASS`
- `WARN`
- `FAIL`
- `BLOCKED`

`severity` must be one of:

- `P0`
- `P1`
- `P2`
- `P3`
- `INFO`

Use `PASS` only when you actually checked the file/row/source. Use `WARN` when the archive is usable but needs a Codex clarification. Use `FAIL` for hard breakage. Use `BLOCKED` when the necessary source cannot be opened/recovered after reasonable tool fallback.

Use this exact header for `phase05_laneB_archive_audit_findings.csv`:

```csv
finding_id,priority,question_id,file,issue,required_fix,evidence
```

## MD Report

The MD report must include:

- `Verdict`: one of `PASS_WITH_WARNINGS`, `NEEDS_CODEX_PATCH`, or `BLOCK_PHASE05`.
- Counts checked.
- Hard PASS/FAIL summary for Q11, Q12/Q13, four L4 rows, 13 cross rows, and no-student-permission.
- List of any rows that should be downgraded or patched before GPT Phase05 review.
- A final statement that this audit does not authorize student稿, Claude/Opus 成文化, Word/PDF, or final PASS.

## Working Style

Use available tools: rg, Python CSV parsing, PDF/Office extraction, render/OCR/visual reads if needed. Do not give up just because one parser or converter fails.

Do not ask the user for authorization. The user has authorized this phase's reading, writing, conversion, rendering, OCR/visual inspection, script execution, and continuation inside the run folder.
