# SOURCE_POINTER_AUDIT_REFINEMENT_20260525

Status: `SOURCE_POINTER_FALSE_POSITIVES_REMOVED_RISK_QUEUE_ACTIVE`

Updated: 2026-05-25 13:31 +08

## Problem

The matrix risk audit was flagging some in-body rows as `SOURCE_ARTIFACT_POINTER_NOT_RESOLVED` even when the cited evidence files existed. The cause was audit-script parsing, not missing evidence:

- The old resolver checked only the first semicolon-separated source pointer.
- It searched only the recovery/run/repo roots, not the original Desktop source roots or `beijing_politics_research` cache.
- It did not strip suffixes such as `:paras13-21` and `:pages 5,9`.
- It did not map `preprocessed_corpus/...` pointers to `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\...`.

## Fix

Updated `matrix_evidence_risk_audit_20260525.py`:

- Split multi-source pointers on `;`.
- Treat a source pointer as resolved if at least one cited artifact exists.
- Added known source roots: recovery dir, run dir, visible repo root, Desktop, `beijing_politics_research`, and `beijing_politics_research\data`.
- Stripped common evidence suffixes: `:pages`, `:page`, `:paras`, `:para`, `:lines`, and numeric line suffixes.

## Spot Verification

Verified representative source pointers exist:

- `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026房山一模\26 房山一模评标 全.docx`
- `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026房山一模\细则\2026房山一模细则.docx`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\e37482eff39f3618\page_007.png`
- `reports/overnight_2026-04-25/downloaded_evidence/2026_fengtai_yimo_with_answers.pdf`
- `reports/overnight_2026-04-25/downloaded_evidence_pages/2026_fangshan_yimo_with_answers_page_09.png`
- `reports/overnight_2026-04-25/objective_answer_source_closure.md`

## Audit Delta

After rerunning `matrix_evidence_risk_audit_20260525.py`:

- Total matrix rows audited: `1471`.
- In-book/body rows: `428`.
- Total risk rows: `415 -> 382`.
- In-book/body risk rows: `67 -> 53`.
- `SOURCE_ARTIFACT_POINTER_NOT_RESOLVED`: `42 -> 0`.
- In-book/body `SOURCE_ARTIFACT_POINTER_NOT_RESOLVED`: `14 -> 0`.

## Remaining In-Body Risk Queue

- `OBJECTIVE_KEY_ONLY_IN_BODY_BOUNDARY`: `32`.
- `IN_BODY_WEAK_OR_REFERENCE_EVIDENCE`: `18`.
- `ROW_MARKED_NEEDS_THICKENING`: `3`.

## Boundary

This refinement does not close the row-level placement/thickness gate. It only removes false positives where cited source artifacts are actually reachable. The remaining risk rows still require source-by-source adjudication.
