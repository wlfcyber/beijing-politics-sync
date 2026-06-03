# Boundary-Patched Sidecar Regeneration Report

- generated_at: 2026-05-19T14:02:34+08:00
- patched_corpus: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/boundary_patched_20260519`

## Outputs

- `question_by_question_framework_runs_boundary_patched.csv`: 53 rows
- `material_trigger_bank_boundary_patched.csv`: 53 rows
- `full_score_sentence_bank.csv`: regenerated to 53 rows
- `full_score_sentence_bank_boundary_patched.csv`: same regenerated content
- backup of previous sentence bank: `full_score_sentence_bank.pre_boundary_canonical_regen_20260519.csv`

## Pass Status Counts

{
  "PASS": 37,
  "OPEN_OR_REFERENCE": 5,
  "PASS_RECOVERED": 11
}

## Notes

The 70-row tracking files remain available for audit, but the new `_boundary_patched.csv` sidecars align with the 53-row framework-ready corpus. Open/reference rows are labelled as `OPEN_OR_REFERENCE`; they must not be used as standalone core evidence.

## Sidecar Status Normalization

After initial filtering, the 53-row boundary sidecars still carried older `PARTIAL/FAIL/OPEN_FORMAL` labels for recovered cases. They have now been normalized against `boundary_patched_framework_eligible_ids.csv`: recovered core rows are `PASS_RECOVERED`, and open/reference/composite rows are `OPEN_OR_REFERENCE`.

```json
{
  "question_by_question_framework_runs_boundary_patched.csv": {
    "PASS": 37,
    "OPEN_OR_REFERENCE": 5,
    "PASS_RECOVERED": 11
  },
  "material_trigger_bank_boundary_patched.csv": {
    "PASS": 37,
    "OPEN_OR_REFERENCE": 5,
    "PASS_RECOVERED": 11
  },
  "full_score_sentence_bank.csv": {
    "PASS": 37,
    "OPEN_OR_REFERENCE": 5,
    "PASS_RECOVERED": 11
  }
}
```
