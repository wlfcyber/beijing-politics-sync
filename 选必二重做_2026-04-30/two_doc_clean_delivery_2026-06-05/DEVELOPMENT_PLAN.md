# DEVELOPMENT_PLAN

created_at: 2026-06-05

## Current Boundary

This run only produces two clean student-facing documents for 选必二《法律与生活》:

- 试题和细则汇编
- AB 双轴学生宝典

Do not count any GPT-5.5 Pro or Claude Opus 4.8 Max result produced through CLI as a formal external review. Formal external review must use a visible web or desktop app session.

## Minimal Step For v10

1. Repair the four blocking defects reported by the valid GPT-5.5 Pro web review of `compilation-01` in v9.
2. Regenerate both student-facing documents as v10.
3. Run local checks for the repaired entries, hidden paths, and empty rubric markers.
4. Rebuild the web/app external-review package for v10.
5. Restart GPT-5.5 Pro web review from `compilation-01`.

## Do Not Claim

- Do not claim final delivery before GPT-5.5 Pro web review and Claude Opus 4.8 Max web/app review both close without blocking defects.
- Do not push as final GitHub closure before the external-review record is complete.
