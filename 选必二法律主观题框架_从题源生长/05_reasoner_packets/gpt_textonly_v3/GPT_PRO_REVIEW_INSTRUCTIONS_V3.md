# GPT Pro review instructions V3

This is the v3 text-only fallback packet after Codex patched the Claude V2 findings. Review the current v3 files only. Do not inherit older V2 verdicts except as a checklist for regression.

Key v3 regression targets:

- `2026丰台二模 Q8` must now be the brain-computer-interface choice question, not 长三角政务服务.
- `2026丰台二模 Q9` must now be the flower-tea truth-telling choice question, not 城市治理.
- `2024丰台一模 Q7` must not leak `Answer key`.
- `2024朝阳二模 Q7` must include option D.
- `2026石景山一模 Q6` must split C and D.
- `2026海淀二模 Q6` must include the table conditions in text form.
- `2024石景山一模 Q7` must include a text reconstruction of 图甲/乙/丙/丁; `image2.png` is the source image extracted from the original DOCX.
- `2026石景山二模 Q7` must no longer be truncated.
- `2024西城一模 Q11` must no longer repeat blocks.
- `2026顺义一模 Q2/Q4` must no longer contain OCR PUA glyphs.
- `CHOICE_OPTION_RECOVERY_AUDIT.csv` and `PROMPT_RECOVERY_AUDIT.csv` should have headers and 0 rows.
- `LOCAL_QA_REPORT.md` should show no banned backend terms.

Output exactly one verdict: `PASS`, `CONDITIONAL_PASS`, `NOT_PASS`, or `BLOCKED`, followed by P0/P1/P2 findings with concrete file/question evidence. Any patch advice remains advisory until Codex verifies against local sources.
