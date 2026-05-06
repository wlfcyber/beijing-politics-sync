# Phase06 Codex A Local Audit

Verdict: `PASS_LOCAL_PHASE06_STRUCTURE_AUDIT`

- checks: 16
- failures: 0

Internal audit only. No student稿, Claude Opus prose, Word/PDF, or final PASS is authorized.

## Checks

- PASS: G01 evidence_lock_register - rows=74
- PASS: G02 thinking_fusion - rows=36
- PASS: G03 reasoning_fusion - rows=51
- PASS: G04 cross_mount - rows=13
- PASS: G05 L0_retention - rows=288
- PASS: G06 cross_double_membership - missing=[]
- PASS: G07 Q11_lock - Q11 retains B=①③ and contains no retired wrong-pairing string
- PASS: G08 Q12_Q13_lock - Q12=answer_confirmed_D_from_supplemental_key; Q13=answer_confirmed_C_from_supplemental_key
- PASS: G09 L3_L4_separation - counts={'L3': 70, 'L4': 4}
- PASS: G10 student_permission - all phase06 rows keep student_permission=no
- PASS: C01 thinking_material_signal - all thinking rows have material signal
- PASS: C02 thinking_answer_action - all thinking rows have answer action
- PASS: C03 reasoning_logical_form - all reasoning rows have logical form
- PASS: C04 reasoning_rule_slogan - all reasoning rows have rule slogan
- PASS: C05 reasoning_common_trap - all reasoning rows have common trap
- PASS: C06 index_coverage - indexes generated separately; evidence ids stable
