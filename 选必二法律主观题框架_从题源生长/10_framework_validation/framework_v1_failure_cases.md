# Framework v1 Failure Cases

- Test policy: entry matching used only question text, ask atoms, material text, and material atoms. It did not use answer_text or rubric_text.

- Total questions: 65
- PASS: 16
- PARTIAL: 49
- FAIL: 0

## FAIL Rows
- None under entry-only matching; all non-direct formal rows at least trigger a transfer-test entry, but they remain non-closed.

## PARTIAL Rows Needing Source Check
- `CC0011_2024_丰台_二模_17` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0019_2024_朝阳_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0025_2024_朝阳_二模_17` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0040_2024_海淀_一模_19` status=REFERENCE_ONLY:FWV1_N02+FWV1_N05+FWV1_N07 evidence=reference_only patch_type=证据不足
- `CC0045_2024_海淀_二模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0054_2024_石景山_一模_17` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0061_2024_西城_一模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0063_2024_西城_二模_16` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0092_2025_东城_期末_19_1` status=TRANSFER_TEST:FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0103_2025_丰台_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0125_2025_延庆_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0131_2025_房山_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0137_2025_昌平_二模_20` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N03 evidence=formal patch_type=材料触发不清
- `CC0143_2025_朝阳_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0162_2025_海淀_一模_18` status=REFERENCE_ONLY:FWV1_N02+FWV1_N04+FWV1_N06 evidence=reference_only patch_type=证据不足
- `CC0181_2025_海淀_期末_21` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0189_2025_石景山_一模_20` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N03 evidence=formal patch_type=材料触发不清
- `CC0195_2025_西城_一模_20` status=TRANSFER_TEST:FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0200_2025_西城_二模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0206_2025_西城_期末_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0213_2025_门头沟_一模_20` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N03 evidence=formal patch_type=材料触发不清
- `CC0214_2025_门头沟_一模_20_2` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N03 evidence=formal patch_type=材料触发不清
- `CC0223_2025_顺义_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0229_2026_东城_一模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N05+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0238_2026_东城_二模_19` status=TRANSFER_TEST:FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0254_2026_丰台_二模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `CC0276_2026_房山_二模_17` status=TRANSFER_TEST:FWV1_N02+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0277_2026_房山_二模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0283_2026_朝阳_一模_18` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0289_2026_朝阳_二模_18` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0311_2026_海淀_二模_18_2` status=REFERENCE_ONLY:FWV1_N03+FWV1_N05+FWV1_N07 evidence=reference_only patch_type=证据不足
- `CC0318_2026_海淀_期末_18_2` status=TRANSFER_TEST:FWV1_N03+FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0319_2026_海淀_期末_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N05 evidence=formal patch_type=材料触发不清
- `CC0332_2026_石景山_二模_19` status=TRANSFER_TEST:FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0340_2026_西城_一模_17` status=TRANSFER_TEST:FWV1_N05+FWV1_N07 evidence=formal patch_type=材料触发不清
- `CC0353_2026_西城_期末_17` status=REFERENCE_ONLY:FWV1_N02+FWV1_N04+FWV1_N05 evidence=reference_only patch_type=证据不足
- `CC0364_2026_通州_期末_19_1` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `CC0380_2026_顺义_二模_18_2` status=TRANSFER_TEST:FWV1_N02+FWV1_N05+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2025_海淀_二模_18` status=TRANSFER_TEST:FWV1_N01+FWV1_N02+FWV1_N03 evidence=formal patch_type=材料触发不清
- `RECOVER_2024_东城_一模_19` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2024_东城_二模_19_1` status=TRANSFER_TEST:FWV1_N06+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2024_东城_二模_19_2` status=TRANSFER_TEST:FWV1_N06+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2025_丰台_二模_19_2` status=TRANSFER_TEST:FWV1_N02+FWV1_N05+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_延庆_一模_18_1` status=TRANSFER_TEST:FWV1_N02+FWV1_N07 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_房山_一模_17_1` status=TRANSFER_TEST:FWV1_N02+FWV1_N04+FWV1_N06 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_西城_二模_18_1` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_西城_二模_18_2` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_西城_二模_18_3` status=TRANSFER_TEST:FWV1_N02+FWV1_N03+FWV1_N04 evidence=formal patch_type=材料触发不清
- `RECOVER_2026_门头沟_一模_18_1` status=TRANSFER_TEST:FWV1_N02+FWV1_N06+FWV1_N05 evidence=formal patch_type=材料触发不清
