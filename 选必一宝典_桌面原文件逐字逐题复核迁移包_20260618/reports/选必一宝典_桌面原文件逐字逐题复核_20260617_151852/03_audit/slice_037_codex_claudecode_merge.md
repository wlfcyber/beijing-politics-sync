# Slice 037 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T05:43:30+08:00
- scope: doc_order 181-185 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc. doc185 first attempt hung after the prompt accidentally included full Q20 source context and was preserved as `04_claudecode/slice_037_doc185_attempt1_hung_*`; doc185 was rerun after trimming the exam/rubric excerpts and the rerun finding is the accepted finding.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 181 | Q0181 | 2024丰台一模Q20供应链如何成为“共赢链” | PASS | Infrastructure branch supports resource-allocation/global-flow point; formal 7分 level rule is preserved. UQ0085 is singleton; no row-level repair. |
| 182 | Q0182 | 2024石景山一模Q19(2)新能源车企“扎下根” | NEEDS_FIX | Block 2141 imports the coffee/supply-chain raw-material-cost sentence, which is absent from the NEV/Hungary source. Scoring detail remains source-limited because the PPTX gives answer text but no full scoring breakdown. |
| 183 | Q0183 | 2025西城一模Q18 | NEEDS_FIX + PENDING_BOOK_LEVEL | Block 2150 says the question asks “利用国内外资源/开拓海外市场/提升国际循环质量”, but those are answer/rubric terms, not the actual prompt; UQ0038 remains pending. |
| 184 | Q0184 | 2026房山一模Q19海南“一线放开”自由便利 | NEEDS_FIX + PENDING_BOOK_LEVEL | Block 2160 repeats the one-line/two-line error: 一线放开 is international-facing, while 进出岛 belongs to 二线/岛内外; UQ0049 remains pending. |
| 185 | Q0185 | 2025丰台一模Q20北京“两区”通关创新 | NEEDS_FIX + PENDING_BOOK_LEVEL | Block 2179 omits the copy-material 1-2分 cap and the 《经济与社会》政府与市场知识 no-credit boundary; UQ0064 remains pending. |

## Source Evidence

- Q0181: `SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt`; `SRC_RUBRIC_2024_FENGTAI_YIMO_Q20.txt`; exam lines 242-253,370-373; rubric lines 110-116; Claude finding `04_claudecode/slice_037_doc181_claudecode_findings.md`.
- Q0182: `SRC_EXAM_2024_SHIJINGSHAN_YIMO_Q19_2.txt`; corrected `SRC_RUBRIC_2024_SHIJINGSHAN_YIMO_Q19_2.txt`; exam lines 161-164; rubric/PPTX lines 539-544 with answer line 543; Claude finding `04_claudecode/slice_037_doc182_claudecode_findings.md`.
- Q0183: `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt`; `SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt`; exam lines 221-234,342-345; rubric lines 65-78; Claude finding `04_claudecode/slice_037_doc183_claudecode_findings.md`.
- Q0184: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt`; `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt`; exam lines 300-342; rubric lines 58-64; Claude finding `04_claudecode/slice_037_doc184_claudecode_findings.md`.
- Q0185: trimmed `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt`; trimmed `SRC_RUBRIC_2025_FENGTAI_YIMO_Q20.txt`; exam lines 206-220,287-289; rubric lines 13-14; Claude finding `04_claudecode/slice_037_doc185_claudecode_findings.md`.

## Required Repairs / Holds

- Q0182: repair block 2141 so the “why” explanation uses NEV/Hungary facts: domestic tech/industrial-chain/product strengths plus Hungary transport hub/industrial base, not coffee supply-chain/raw-material-cost facts.
- Q0183: repair block 2150 so the actual prompt remains “中国经济增长新空间如何拓展”; treat 开拓海外市场/国际循环质量 as answer/rubric cues, not question wording. Keep UQ0038 pending.
- Q0184: repair block 2160 so 一线放开 is tied to one-line international-facing freedom/convenience, and 进出岛/internal-market chain is tied to 二线口岸. Keep UQ0049 pending.
- Q0185: repair block 2179 by restoring copy-material 1-2分 cap and 《经济与社会》政府与市场知识 no-credit boundary. Keep UQ0064 pending; the macro 双循环 point is a fallback 1-3分 frame, not the main 8分 answer spine.
- Q0181: no hard repair; optional precision only (`提高资源配置效率`, and adding `推动全球供应链高质量发展`).

## Boundary

This merge accepts only doc_order 181-185 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 186; 376 entries remain pending.
