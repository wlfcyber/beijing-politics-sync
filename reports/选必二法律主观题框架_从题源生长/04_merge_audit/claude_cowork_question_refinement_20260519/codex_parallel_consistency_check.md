# Codex Parallel Consistency Check — Claude Cowork Refinement Lane
This local check runs while Claude Cowork audits the same corrected 65-question packet. It is mechanical only and does not replace Cowork source judgment.
## Counts
- questions: 65
- evidence levels: {'formal': 61, 'reference_only': 4}
- material atoms: 541
- ask atoms: 65
- rubric atoms: 362
- rubric to material refs parsed: 867
- broken rubric to material refs: 0
- suite matrix rows: 65
- boundary/blocked rows: 9
## Reference Only Rows
- CC0040_2024_海淀_一模_19: teacher_reference_answer / reference_only; locator=F0025:text | F0026:page 7 | F0249:text | F0251:page 7
- CC0162_2025_海淀_一模_18: teacher_reference_answer / reference_only; locator=F0089:page 2 | F0090:page 5 | F0090:page 8 | F0305:text lines 358-360; no formal scoring source located in F0088/F0307
- CC0311_2026_海淀_二模_18_2: teacher_reference_answer / reference_only; locator=F0197:text Q18(2)
- CC0353_2026_西城_期末_17: teacher_reference_answer / reference_only; locator=F0221:page 11
## Mechanical Issue Summary
- issue counts by severity: {'high': 20, 'medium': 1}
- high | missing_ask_text | CC0019_2024_朝阳_一模_19: ask_text is empty
- high | missing_ask_text | CC0077_2025_东城_一模_19: ask_text is empty
- high | missing_ask_text | CC0084_2025_东城_二模_19: ask_text is empty
- high | missing_ask_text | CC0092_2025_东城_期末_19_1: ask_text is empty
- high | missing_ask_text | CC0131_2025_房山_一模_19: ask_text is empty
- high | missing_ask_text | CC0157_2025_朝阳_期末_20: ask_text is empty
- high | missing_ask_text | CC0180_2025_海淀_期末_20: ask_text is empty
- high | missing_ask_text | CC0189_2025_石景山_一模_20: ask_text is empty
- high | missing_ask_text | CC0195_2025_西城_一模_20: ask_text is empty
- high | missing_ask_text | CC0213_2025_门头沟_一模_20: ask_text is empty
- high | missing_ask_text | CC0214_2025_门头沟_一模_20_2: ask_text is empty
- high | missing_ask_text | CC0245_2026_东城_期末_18_2: ask_text is empty
- high | missing_ask_text | CC0276_2026_房山_二模_17: ask_text is empty
- high | missing_ask_text | CC0277_2026_房山_二模_18: ask_text is empty
- high | missing_ask_text | CC0317_2026_海淀_期末_18: ask_text is empty
- high | missing_ask_text | CC0318_2026_海淀_期末_18_2: ask_text is empty
- high | missing_ask_text | CC0319_2026_海淀_期末_19: ask_text is empty
- high | missing_ask_text | CC0325_2026_石景山_一模_18: ask_text is empty
- high | missing_ask_text | CC0353_2026_西城_期末_17: ask_text is empty
- high | reference_only_set | questions: actual=['CC0040_2024_海淀_一模_19', 'CC0162_2025_海淀_一模_18', 'CC0311_2026_海淀_二模_18_2', 'CC0353_2026_西城_期末_17'] expected=['CC0040', 'CC0162', 'CC0311_2026_海淀_二模_18_2', 'CC0353_2026_西城_期末_17']
- medium | true_no_law_suite_status_not_confirmed | 2024-海淀-期中: status=midterm_boundary_no_core_after_claudecode_audit

## Gate Note
Cowork output is still required before deciding whether any must-fix patch blocks the GPT-5.5 Pro / Claude Opus open-observation rerun.
