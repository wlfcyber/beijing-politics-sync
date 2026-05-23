# ClaudeCode / Opus 4.7 Final Review Task

You are the final reviewer for the 2026 Beijing district second-mock backfill into the Xuanbiyi handbook.

Read these files:

- `../05_gpt_pro_packet/GPT_PRO_OUTPUT_NORMALIZED_FOR_CLAUDE.md`
- `../05_gpt_pro_packet/GPT_PRO_OUTPUT_CAPTURE.md`
- `../04_diff_and_fusion/CODEX_CLAUDECODE_DIFF.md`
- `../04_diff_and_fusion/FUSION_DRAFT_FOR_GPT_PRO.md`
- `../02_claudecode_independent/CLAUDECODE_ORIGINALS_THICK_DRAFT.md`
- `../03_codex_independent/CODEX_INDEPENDENT_THICK_DRAFT.md`

Review the normalized GPT Pro output against the original source extraction and the user's hard rules:

1. Only formal rubrics, evaluation criteria, marking rules, or explicit scored lecture materials enter the main table.
2. Fengtai Q20 and Shunyi Q20 must remain outside the main table.
3. New型国际关系 / 国际新秩序 / cooperation-win in international order or global governance must be under 政治多极化, not 理论.
4. 正确义利观 in this round must remain 中国 because the context is China action, development cooperation, and responsibility.
5. Economic-globalization nodes must not be over-merged. Keep non-substitutable terms separate; same rubric-position alternatives may still be separate if useful, but mark their shared score layer clearly.
6. No answer sentence may contain backend language such as 采分点, 要落到, 本题需要, 细则要求, 设问要求, v7.

Output:

- `PASS` if the normalized GPT Pro output is safe to put into `03_fusion/BATCH_014_FINAL_AFTER_GPT_AND_CLAUDE.md`.
- Otherwise output `PATCH REQUIRED`, then list exact edits by bucket, term, and replacement text. Keep this concise and actionable.

Do not rewrite the whole document unless a patch is required.
