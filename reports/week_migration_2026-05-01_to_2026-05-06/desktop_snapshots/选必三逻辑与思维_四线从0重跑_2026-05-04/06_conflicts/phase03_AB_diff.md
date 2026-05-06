# Phase 03 A/B Diff

Status: Codex-generated diff after ClaudeCode Lane B completed. This is not student-facing and does not authorize drafting.

## Headline Verdict

- Verdict: `NO_PASS_CONTINUE_EXTRACTION`.
- Lane B is useful as an independent candidate scan, but it does not yet satisfy the literal every-question coverage gate.
- Student稿、Claude Opus 成文化、Word/PDF、最终 PASS remain blocked.

## Counts

- Lane A question/subquestion rows: 528
- Lane A in-scope/cross keys: 122
- Lane B question/candidate rows: 59
- Common A/B keys: 46
- A-only in-scope/cross keys: 76
- B-only candidate keys: 7
- Diff summary CSV: `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04/06_conflicts/phase03_AB_diff_summary.csv`

## Critical Findings

### P1 B_LINE_NOT_FULL_EVERY_QUESTION_COVERAGE

Lane A has 528 question/subquestion rows including blockers; Lane B has 59 candidate rows. This is useful for candidate diff but does not satisfy GPT's literal every-question gate.

### P1 2026_FENGTAI_Q18_2_MISSED_BY_LANEB

Codex A visually recovered 2026丰台一模 Q18(2) and paired it with 043细则 lines on必要条件假言推理+三段论大项不当扩大; Lane B leaves S15 as scan blocked and says 043 only哲学/政治, so B missed a high-value推理题.

### P1 HS02_STILL_LOCKED

A visually confirmed 2025海淀二模 Q20 page 07, but Lane B did not independently confirm; keep locked_pending_laneB_visual_confirmation before student稿.

### P2 LANEB_UNREAD_SOURCES_REMAIN

Lane B report admits 14 unread sources and 4 pending suites; no final student artifact or GPT content review can proceed from this state.

### P2 A_MATRIX_HAS_NOISY_DUPLICATES_AND_REFERENCE_TEXT

Lane A has duplicate rows and some answer/reference text mixed into excerpts; before student fusion, run dedup and split paper prompt from answer/rubric excerpts.

### P2 2026_ERMO_MISSING

Both lanes report no confirmed 2026二模 within current source boundary. Record missing_or_blocked, do not claim nonexistence.

## A/B Common Keys Requiring Attention

- `2025西城二模 16(3)` | CLASSIFICATION_CONFLICT | A=推理 (pending_pairing) | B=思维部分_创新思维 (PARTIAL_READ) | A=推理 B=思维部分_创新思维
- `2024朝阳一模 20(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳一模 20(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳一模 21` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳一模 9` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳二模 16(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳二模 16(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳二模 19(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳二模 19(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳二模 19(3)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳期中 1` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳期中 5` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 14` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 16` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 17(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 17(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 4` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024海淀二模 8` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 11` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (blocked_until_options_visual_check) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 13` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(3)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(4)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(5)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024西城一模 19(6)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 1` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 16` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维;边界 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 18(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 2` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;思维;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 20` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维;边界 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 21` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 5` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 7` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 8` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025东城期末 9` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025丰台期末 16` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉;待判 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025丰台期末 18(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025丰台期末 18(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025丰台期末 18(3)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025海淀期末 17(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025海淀期末 22` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025西城二模 16(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025西城二模 17(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025西城二模 17(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025西城二模 7` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (blocked_until_options_visual_check) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 10` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 16` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维;边界 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 17(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 17(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 3` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2025顺义一模 4` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城一模 12` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城一模 19(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城一模 19(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城一模 19(3)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城一模 2` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 14` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 16(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 16(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 17(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 21` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 3` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 4` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 5` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026东城期末 6` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026丰台一模 18(2)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (locked_pending_laneB_visual_confirmation) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026朝阳期中 1` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026朝阳期中 18` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=待判;推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026朝阳期中 21(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026通州期末 19(1)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026通州期末 5` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026通州期末 8` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026顺义一模 19(3)` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=交叉 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026顺义一模 6` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026顺义一模 7` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=推理 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2026顺义一模 9` | A_ONLY_NEEDS_B_OR_SOURCE_RECHECK | A=思维 (pending_pairing) | B= () | A detected in-scope or cross candidate absent from Lane B
- `2024朝阳一模 主观题` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=思维部分_创新思维 (PENDING_READ) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2024西城一模 PENDING` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=PENDING (PENDING_READ) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2025海淀二模 12` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=推理部分 (LOCKED_PENDING_VISUAL) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2025海淀二模 13` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=推理部分 (LOCKED_PENDING_VISUAL) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2025顺义一模 主观题` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=PENDING (PENDING_READ) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2026东城期末 选择题` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=完整 () | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row
- `2026丰台一模 PENDING` | B_ONLY_NEEDS_A_OR_SOURCE_RECHECK | A= () | B=PENDING (SCAN_BLOCKED) | Lane B candidate absent from Lane A initial matrix or uses pending suite-level row

## Required Next Actions

1. Send a focused patch prompt to ClaudeCode for S15/2026丰台一模 Q18(2), forcing it to inspect 042 page_07 render and 043 lines around necessary-condition hypothetical reasoning and syllogism.
2. Keep HS02 locked but provide Lane B the A-line visual locator and ask for independent confirmation of 008 page_07.
3. Run Lane A dedup/split pass: separate paper question rows from answer/rubric/reference rows and remove duplicated Q rows before fusion.
4. Do not send Phase 03 to GPT as a pass packet; send it as a blocker/diff packet asking for commander advice after the focused patch.
