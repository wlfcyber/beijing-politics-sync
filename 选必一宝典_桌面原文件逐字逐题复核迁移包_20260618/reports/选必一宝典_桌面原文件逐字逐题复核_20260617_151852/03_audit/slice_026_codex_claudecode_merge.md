# Slice 026 Codex + ClaudeCode Merge

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- timestamp: 2026-06-18T00:23:41+08:00
- scope: doc_order 126-130 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- source_docx_mutation: none
- ClaudeCode lane: real `claude -p --model opus --effort max`, resolved in debug logs to `claude-opus-4-8`; doc126-doc130 streams all ended with success.

## Result Summary

| doc_order | entry_id | source question | merged status | key reason |
|---:|---|---|---|---|
| 126 | Q0126 | 2026顺义二模Q20 | PASS + PENDING_BOOK_LEVEL | Prompt/material/rubric align with 顺义二模Q20; `普惠包容经济全球化` is line-87 backed; UQ0013 not group-accepted. |
| 127 | Q0127 | 2025朝阳期末Q21 | NEEDS_FIX | `材料触发点` uses the overall peace/development branch instead of the economic branch; visible score parts sum to 7 while Q21 is 8分. |
| 128 | Q0128 | 2025石景山一模Q17(2) | PASS | Exam and formal rubric literally support prompt, material, four 2分中国主张 points, and the `推进普惠包容的经济全球化` answer sentence. |
| 129 | Q0129 | 2026门头沟一模Q20 | PASS + PENDING_BOOK_LEVEL | 7分 reason/China/world/logic frame is source-backed; this entry is correctly narrowed to the world-meaning branch; UQ0015 pending. |
| 130 | Q0130 | 2026房山一模Q19 | NEEDS_FIX | `材料触发点` confuses 一线口岸面向国际/进出境 with 二线口岸进出岛; other fields align at slice level. |

## Source Evidence Used

- Q0126: `05_source_backcheck/slice_026/SRC_EXAM_2026_SHUNYI_ERMO_Q20.txt:350-362`; `SRC_RUBRIC_2026_SHUNYI_ERMO_Q20.txt:71-88`.
- Q0127: `SRC_EXAM_2025_CHAOYANG_QIMO_Q21.txt:229-237`; `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1314-1355,1420-1490`; formal PDF text extract is registered but unreadable.
- Q0128: `SRC_EXAM_2025_SHIJINGSHAN_YIMO_Q17_2.txt:211-237,361-369`; `SRC_RUBRIC_2025_SHIJINGSHAN_YIMO_Q17_2.txt:28-43`.
- Q0129: `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356`; `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131`.
- Q0130: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342`; `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:58-64`.

## Required Repairs / Holds

- Q0127 block 1513 must be retargeted from 总体外部环境/和平发展 to the economic branch: 逆全球化、保护主义、脱钩断链 -> 普惠包容经济全球化.
- Q0127 blocks 1518-1522 must reconcile the 8分 total. Visible PPTX evidence proves the desktop 1+1+2+2+1=7 frame is wrong; exact ②/③ split should be checked against the missing PPTX gap before final rewrite.
- Q0130 block 1551 must separate 一线放开 (international/entry-exit convenience) from 二线口岸进出岛.
- UQ0013, UQ0001, UQ0015 and UQ0049 remain book-level pending; no group-level acceptance is claimed here.

## Ledger Update

- Updated `03_audit/QUESTION_AUDIT_LEDGER.csv` rows A01001-A01040.
- Reviewed field rows through doc_order 130: 1040 / 4488.
- Remaining question entries after this slice: 431.
