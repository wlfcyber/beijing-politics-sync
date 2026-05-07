# Governor / Confucius Precheck

Governor verdict: `GOVERNOR_P0_P2_EVIDENCE_GATE_OK_NOT_FINAL`
Confucius verdict: `CONFUCIUS_PRECHECK_NOT_STUDENT_DELIVERY`

## Evidence Gate

- overall: `OVERALL_BATCH_CLOSURE_OK_NOT_FINAL` expected `OVERALL_BATCH_CLOSURE_OK_NOT_FINAL`
- p0_recheck: `P0_RECHECK_QA_OK_NOT_FINAL` expected `P0_RECHECK_QA_OK_NOT_FINAL`
- p1_recheck: `P1_RECHECK_QA_OK_NOT_FINAL` expected `P1_RECHECK_QA_OK_NOT_FINAL`
- p2_recheck: `P2_RECHECK_QA_OK_NOT_FINAL` expected `P2_RECHECK_QA_OK_NOT_FINAL`
- p0_fusion: `P0_FUSION_PATCH_OK_NOT_FINAL` expected `P0_FUSION_PATCH_OK_NOT_FINAL`
- p1_fusion: `P1_FUSION_PATCH_OK_NOT_FINAL` expected `P1_FUSION_PATCH_OK_NOT_FINAL`
- p2_fusion: `P2_FUSION_PATCH_OK_NOT_FINAL` expected `P2_FUSION_PATCH_OK_NOT_FINAL`

## P2 Boundary

- P2 decision counts: `{'source_insufficient': 7, 'confirmed_with_patch': 24, 'confirmed': 4, 'block_from_student_body': 3, 'downgrade_to_index': 1}`
- P2 can-enter-fusion counts: `{'no': 10, 'yes': 29}`
- forbidden/recheck hits in fusion: `{'固定分析流程': 0, 'FINAL_PASS': 0, '终稿已通过': 0, '最终版': 0, '需 Codex 回源复核': 0}`
- running P2 ClaudeCode processes: `0`

## Confucius Note

- The current artifact is a framework-first fusion draft with audit evidence still visible.
- It is ready for a later student-facing cleanup pass, but it is not a student delivery, Word file, PDF, or final product.
- audit marker hits: `{'P0证据': 19, 'P1证据': 11, 'P2证据': 39, 'A-formal': 57, 'A-support': 12, 'B-choice-signal': 57, 'source_insufficient': 14}`

## Boundary

- Word/PDF/delivery authorization: `no`
- Four-line finalization authorization: `no`
