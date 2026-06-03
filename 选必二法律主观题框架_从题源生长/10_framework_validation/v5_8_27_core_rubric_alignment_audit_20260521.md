# V5.8 27 核心题细则对账留痕

生成时间：2026-05-21 04:25 CST

## 结论

- 对账对象：27 道核心题。
- 核心题 clean rubric atom 总数：133。
- clean rubric atom ID 在 merged_rubric_atoms 中缺失：0 题。
- 审计残留命中：0 题。
- 机械追踪结论分布：{'PASS_WITH_MANUAL_CHECK': 17, 'PASS_TRACE': 10}。

说明：本表用于补 Claude V5.8 P2-2 的“27 核心全量细则对账留痕”。它是机械追踪，不替代最终阅卷判断；凡 `PASS_WITH_MANUAL_CHECK` 的行，需要在 Word/PDF 成稿前由 Codex/GPTPro/Claude 结合细则语义确认。

## 特别风险

- CC0150 clean atoms 数：9；底座中未纳入 clean 的 rubric atoms 数：15。Claude 已指出其中 R_12-R_24 为《当代国际政治与经济》串入原子，V5.8 学生稿当前未引用，但后续应清理底座。

## 输出文件

- `10_framework_validation/v5_8_27_core_rubric_alignment_audit_20260521.csv`
- `10_framework_validation/v5_8_27_core_rubric_atom_trace_20260521.csv`

## 27 核心题汇总

| # | question_id | clean atoms | weak trace | residue | verdict |
|---|---|---:|---:|---|---|
| 1 | CC0002_2024_丰台_一模_17 | 6 | 2 | 无 | PASS_WITH_MANUAL_CHECK |
| 2 | CC0025_2024_朝阳_二模_17 | 16 | 12 | 无 | PASS_WITH_MANUAL_CHECK |
| 3 | CC0045_2024_海淀_二模_19 | 1 | 1 | 无 | PASS_WITH_MANUAL_CHECK |
| 4 | CC0054_2024_石景山_一模_17 | 6 | 4 | 无 | PASS_WITH_MANUAL_CHECK |
| 5 | CC0063_2024_西城_二模_16 | 1 | 0 | 无 | PASS_TRACE |
| 6 | CC0103_2025_丰台_一模_19 | 1 | 0 | 无 | PASS_TRACE |
| 7 | CC0125_2025_延庆_一模_19 | 5 | 3 | 无 | PASS_WITH_MANUAL_CHECK |
| 8 | CC0143_2025_朝阳_一模_19 | 9 | 4 | 无 | PASS_WITH_MANUAL_CHECK |
| 9 | CC0150_2025_朝阳_二模_20 | 9 | 4 | 无 | PASS_WITH_MANUAL_CHECK |
| 10 | CC0181_2025_海淀_期末_21 | 5 | 4 | 无 | PASS_WITH_MANUAL_CHECK |
| 11 | CC0200_2025_西城_二模_18 | 1 | 0 | 无 | PASS_TRACE |
| 12 | CC0206_2025_西城_期末_19 | 1 | 0 | 无 | PASS_TRACE |
| 13 | CC0223_2025_顺义_一模_19 | 6 | 2 | 无 | PASS_WITH_MANUAL_CHECK |
| 14 | CC0229_2026_东城_一模_18 | 8 | 0 | 无 | PASS_TRACE |
| 15 | CC0238_2026_东城_二模_19 | 6 | 4 | 无 | PASS_WITH_MANUAL_CHECK |
| 16 | CC0244_2026_东城_期末_18 | 4 | 1 | 无 | PASS_WITH_MANUAL_CHECK |
| 17 | CC0373_2026_顺义_一模_18 | 7 | 3 | 无 | PASS_WITH_MANUAL_CHECK |
| 18 | RECOVER_2025_海淀_二模_18 | 9 | 2 | 无 | PASS_WITH_MANUAL_CHECK |
| 19 | RECOVER_2026_通州_一模_20 | 6 | 0 | 无 | PASS_TRACE |
| 20 | RECOVER_2024_东城_二模_19_1 | 3 | 0 | 无 | PASS_TRACE |
| 21 | RECOVER_2024_东城_二模_19_2 | 2 | 2 | 无 | PASS_WITH_MANUAL_CHECK |
| 22 | RECOVER_2025_丰台_二模_19_2 | 4 | 3 | 无 | PASS_WITH_MANUAL_CHECK |
| 23 | RECOVER_2026_延庆_一模_18_1 | 3 | 0 | 无 | PASS_TRACE |
| 24 | RECOVER_2026_房山_一模_17_1 | 3 | 2 | 无 | PASS_WITH_MANUAL_CHECK |
| 25 | RECOVER_2026_西城_二模_18_1 | 3 | 1 | 无 | PASS_WITH_MANUAL_CHECK |
| 26 | RECOVER_2026_门头沟_一模_18_1 | 3 | 0 | 无 | PASS_TRACE |
| 27 | RECOVER_2026_朝阳_期末_18_1 | 5 | 0 | 无 | PASS_TRACE |
