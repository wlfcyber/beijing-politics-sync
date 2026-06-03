# Framework v1 Partial Cluster Source Check

- Formal PARTIAL rows: 45
- Reference-only PARTIAL rows: 4

## Cluster Counts
- PC01 `意义::FWV1_N02+FWV1_N03+FWV1_N04`: 4
- PC02 `综合::FWV1_N01+FWV1_N02+FWV1_N03`: 4
- PC03 `论证::FWV1_N02+FWV1_N03+FWV1_N04`: 2
- PC04 `综合::FWV1_N07`: 2
- PC05 `原因::FWV1_N02+FWV1_N04+FWV1_N07`: 2
- PC06 `论证::FWV1_N02+FWV1_N03+FWV1_N05`: 2
- PC07 `说明::FWV1_N02+FWV1_N07`: 2
- PC08 `综合::FWV1_N02+FWV1_N05+FWV1_N07`: 2
- PC09 `论证::FWV1_N02+FWV1_N04+FWV1_N05`: 2
- PC10 `评析::FWV1_N02+FWV1_N04+FWV1_N06`: 2
- PC11 `说明::FWV1_N02+FWV1_N03+FWV1_N04`: 2
- PC12 `论证::FWV1_N02+FWV1_N03+FWV1_N06`: 1
- PC13 `综合::FWV1_N02+FWV1_N04+FWV1_N06`: 1
- PC14 `意义::FWV1_N02+FWV1_N03+FWV1_N06`: 1
- PC15 `原因::FWV1_N01+FWV1_N02+FWV1_N03`: 1
- PC16 `原因::FWV1_N02+FWV1_N04+FWV1_N05`: 1
- PC17 `原因::FWV1_N02+FWV1_N04+FWV1_N06`: 1
- PC18 `说明::FWV1_N06`: 1
- PC19 `说明::FWV1_N02+FWV1_N04+FWV1_N05`: 1
- PC20 `评析::FWV1_N04+FWV1_N06`: 1
- PC21 `综合::FWV1_N02+FWV1_N03+FWV1_N04`: 1
- PC22 `论证::FWV1_N02+FWV1_N07`: 1
- PC23 `建议::FWV1_N02+FWV1_N04+FWV1_N07`: 1
- PC24 `综合::FWV1_N01+FWV1_N02+FWV1_N05`: 1
- PC25 `论证::FWV1_N03+FWV1_N04+FWV1_N06`: 1
- PC26 `说明::FWV1_N05+FWV1_N07`: 1
- PC27 `开放::FWV1_N06+FWV1_N07`: 1
- PC28 `建议::FWV1_N06+FWV1_N07`: 1
- PC29 `说明::FWV1_N02+FWV1_N05+FWV1_N07`: 1
- PC30 `说明::FWV1_N02+FWV1_N06+FWV1_N05`: 1

## Rule

These clusters are not new framework nodes. They are evidence-search targets. A cluster can become a new codebook observation only if formal rubric atoms repeatedly reward the same student judgment, material trigger, legal rule, and answer sentence pattern with question_id/rubric_atom_id/material_atom_id traceability.

## Cluster-Key Method

Cluster key = ask_function_plain plus the full transfer-test node combination. This avoids hiding multi-node entry patterns behind the first matched node.

## Files For Next Model Round

- `partial_formal_rows_for_codebook_expansion.csv`
- `reference_only_rows_not_for_core.csv`
- `framework_v1_question_by_question_test.csv`
- `provisional_codebook_v0_cowork_refined.csv`
- `framework_v1.md`
- `framework_v1_evidence_map.csv`
