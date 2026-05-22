# Boundary Patched Canonical Corpus Report

- generated_at: 2026-05-19T13:59:04+08:00
- run_root: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长`
- output_dir: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/boundary_patched_20260519`

## What This Step Did

This step creates a canonical boundary-patched corpus without overwriting the original `04_merge_audit/merged_*` files.

Rules applied:

1. Remove original rows whose after-GPT boundary status is `excluded`, `not_counted_parent_unit`, `pending_split_not_open`, `pending_missing_legal_rubric`, or `duplicate_or_reextract_pending` from the framework-ready corpus.
2. Append split legal subquestions from `10_framework_validation/split_*_patch.csv`:
   - `CC0305_2026_海淀_一模_18_3`
   - `CC0373_2026_顺义_一模_18`
   - `CC0380_2026_顺义_二模_18_2`
3. Keep `CC0229_2026_东城_一模_18` with the already-corrected F0153/F0146 rubric atoms.
4. Keep `CC0094_2025_东城_期末_19_3`, `CC0259_2026_丰台_期中_19`, and `CC0118_2025_丰台_期末_18_2` out of the framework-ready corpus until their pending split/re-source issues close.
5. Preserve all removals and pending cases in `boundary_patch_status_ledger.csv` and `boundary_patched_excluded_pending_ledger.csv`.

## Counts

| Item | Count |
| --- | ---: |
| Original merged question rows | 70 |
| Original question IDs removed from framework-ready corpus | 20 |
| Split legal question rows added | 3 |
| Boundary-patched framework-ready question rows | 53 |
| Original material atoms | 929 |
| Boundary-patched material atoms | 535 |
| Original ask atoms | 70 |
| Boundary-patched ask atoms | 53 |
| Original rubric atoms after CC0229 patch | 499 |
| Boundary-patched rubric atoms | 319 |

## Output Files

- `merged_subjective_law_questions_boundary_patched.csv`
- `merged_material_atoms_subjective_boundary_patched.csv`
- `merged_ask_atoms_subjective_boundary_patched.csv`
- `merged_rubric_atoms_subjective_boundary_patched.csv`
- `merged_subjective_law_questions_for_reasoners_boundary_patched.csv`
- `merged_material_atoms_subjective_for_reasoners_boundary_patched.csv`
- `merged_ask_atoms_subjective_for_reasoners_boundary_patched.csv`
- `merged_rubric_atoms_subjective_for_reasoners_boundary_patched.csv`
- `boundary_patch_status_ledger.csv`
- `boundary_patched_framework_eligible_ids.csv`
- `boundary_patched_excluded_pending_ledger.csv`
- `boundary_patched_counts.json`

## Additional Sanity Patch

After initial corpus generation, `CC0229_2026_东城_一模_18` still carried stale串页 text in `answer_text/rubric_text` even though its rubric atoms were already corrected. This report version records a second pass: those two question-level fields were replaced with the eight corrected F0153/F0146 legal rubric atoms.

## Still Blocked

- `CC0094_2025_东城_期末_19_3`: split pending. Only the adjacent-relation 2-point legal layer may be recovered later; the democratic-procedure layer stays out.
- `CC0259_2026_丰台_期中_19`: missing legal rubric. Not in framework-ready corpus.
- `CC0118_2025_丰台_期末_18_2`: duplicate/reextract pending; likely overlaps `CC0119`. Not in framework-ready corpus.
- DOCX visual QA remains blocked locally because `soffice` is unavailable.

## Decision

`STEP_19_CANONICAL_INTEGRATION` is complete for a patched framework-ready corpus. This is not yet full final classroom release, because visual Word/WPS QA and optional full-score sentence bank regeneration remain open.
