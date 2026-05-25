# P3 unmatched-heading source reconciliation

This file reconciles the headings that P2 could not join to current strict P0 rows. The cause is mostly index coverage, not missing source evidence: several entries were source-locked through older batch ledgers or rendered-image sources. One false entry, `2026顺义一模Q19(3)`, was removed from the student body in P3.

## Reconciled current headings

| current line | final heading | reconciliation status | source ledger / evidence |
|---:|---|---|---|
| 239 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | `00_control/SOURCE_LEDGER_BATCH_013.csv`, `source_locked_image`, question render `renders/e1a49527cb4c175f/page_007.png`, rubric render `renders/487b2d15b3a3ac2b/page_003.png`, evidence `formal_rubric_image` |
| 487 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 2612 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 2627 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 2642 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 3820 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 4487 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 6102 | 2026朝阳期末Q20 | source locked; P2 join missed rendered-image source | same as above |
| 2907 | 2026西城期末Q20--参与全球气候治理中的中国实践 | user-pinned official inclusion; not strict P0 rubric | `00_control/SOURCE_LEDGER_BATCH_005.csv`, rendered question packet `01_source_packets/BATCH_005_2026_XICHENG_QIMO_Q20_PAGE_08.png`, official answer text `texts/efbc5507a38dbd4f_2026北京西城高三_上_期末政治_教师版.txt:67-84`, evidence `official_answer_reference_with_rendered_question` |
| 4172 | 2026西城期末Q20--参与全球气候治理中的中国实践 | user-pinned official inclusion; not strict P0 rubric | same as above |
| 5291 | 2026西城期末Q20 | user-pinned official inclusion; not strict P0 rubric | same as above |
| 5357 | 2026西城期末Q20 | user-pinned official inclusion; not strict P0 rubric | same as above |
| 5374 | 2026西城期末Q20 | user-pinned official inclusion; not strict P0 rubric | same as above |
| 4316 | 2025海淀二模Q21 | source locked; formal rubric with rendered question | `00_control/SOURCE_LEDGER_BATCH_002.csv`, question render `renders/7ff16fecb25f793f/page_008.png`, rubric `texts/fc56fdd304fde118_2025海淀二模细则.txt:77-97` plus lecture `texts/086cafc0d843cdfd_2025届二模考试讲评0510.txt:444-475`, evidence `formal_rubric_rendered_question` |
| 4933 | 2025海淀二模Q21 | source locked; formal rubric with rendered question | same as above |
| 5852 | 2025海淀二模Q21 | source locked; formal rubric with rendered question | same as above |
| 5929 | 2025海淀二模Q21 | source locked; formal rubric with rendered question | same as above |
| 5963 | 2025海淀二模Q21 | source locked; formal rubric with rendered question | same as above |
| 4889 | 2024东城二模Q20 | source locked through formal review summary | `00_control/SOURCE_LEDGER_BATCH_011.csv`, question render `renders/da9fdcae666d3412/page_010.png`, rubric/review `texts/4c98484a2246ecdd_20小题二模阅卷总结.txt:1-24`, evidence `formal_review_summary` |
| 5112 | 2024东城二模Q20 | source locked through formal review summary | same as above |
| 5159 | 2024东城二模Q20 | source locked through formal review summary | same as above |
| 5191 | 2024东城二模Q20 | source locked through formal review summary | same as above |
| 6220 | 2024东城一模Q16 | boundary cross-module source locked; not main-chain P0 | `00_control/SOURCE_LEDGER_BATCH_001.csv`, question render `renders/74cdfac9253763bf/page_006.png`, rubric `texts/4b2073bcc9e26f62_2024东城一模细则.txt:53-62`, evidence `formal_rubric_mixed_module`, boundary entry |

## Removed false positive

| removed heading | reason | action |
|---|---|---|
| 2026顺义一模Q19(3) | The rubric fragment about talent belongs to 顺义 Q19(3) `经济与社会` future-industry recommendation/reasoning. The student body had paired it with a wrong/non-source `当代国际政治与经济` prompt. | Removed from the final student Markdown and reduced the relevant core frequency to `出现1次`. |

Source-label note from ClaudeCode P3 recheck:

- The 顺义一模细则 text itself has a local numbering/label trap: near the transition from Q19 to Q20, the `科技小院/南南合作` rubric is marked in the extracted细则 as `19（3）评标`, while the paper text shows that `科技小院/南南合作` is Q20 and the Q19(3) task is `经济与社会` future-industry advice. Future automation should match by both question text and subject module, not by that local label alone.

## Remaining status

- Remaining previously unmatched headings after P3 are reconciled to batch ledgers or documented boundary/reference evidence.
- The evidence index itself should be regenerated in the next full automation pass so ledger-based and rendered-image sources join automatically.
- This file is audit-only and must not enter the student-facing document.
