# FAIL4 External Cross Check

Claude Cowork and local source adjudication agree on all four v1.1 FAIL cases. This file records the integration decision before framework generation.

| question_id | local | Cowork | final resolution | core use |
|---|---|---|---|---|
| CC0143_2025_朝阳_一模_19 | candidate_core_pending_dual_model | revise_existing_code | revise_existing_code_after_atom_patch | yes_after_patch |
| CC0276_2026_房山_二模_17 | boundary_non_core_keep_audit | exclude_core | boundary_exclude_core | no |
| RECOVER_2026_西城_二模_18_2 | open_container_pending_dual_model | open_container_only | open_container_only | no |
| RECOVER_2026_西城_二模_18_3 | exclude_from_xuanbier_core | exclude_core | boundary_exclude_core | no |

Gate: framework_v2 remains blocked until the CC0143 atom patch and v1.2 codebook snapshot are written.
