# Slice 024 Codex + ClaudeCode Merge

- timestamp: 2026-06-17T23:34:42+08:00
- scope: doc_order 116-120 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- ClaudeCode: real `claude-opus-4-8` via `claude -p --model opus --effort max`; stream logs captured per doc.
- desktop DOCX mutation: none

## Summary

| doc_order | entry | question | merged status | reason |
|---:|---|---|---|---|
| 116 | Q0116 | 2026顺义二模Q20 | PASS + PENDING_BOOK_LEVEL | Source/rubric support the “今天的中国，明天的世界” structure; five-direction wording is broader than the formal rubric’s `普惠包容/更有活力` wording but not source-conflicting. UQ0013 still not group-reviewed. |
| 117 | Q0117 | 2024海淀一模Q18(1) | PASS + PENDING_BOOK_LEVEL | Formal rubric supports the substitute `开放、包容、普惠、共赢/互利共赢/国内国际双循环` under the factor-flow/two-markets layer; row’s five-word standard phrasing is acceptable. UQ0034 still not group-reviewed. |
| 118 | Q0118 | 2026朝阳一模Q20 | LOW_EVIDENCE on score/cap only; otherwise PASS + PENDING_BOOK_LEVEL | Content/rubric points are source-backed, but `本题8分/全题总分不超过8分` is not visible in the provided formal exam/rubric evidence. Visual render of page 7 also shows no `（8分）` after Q20. Keep score/cap as LOW_EVIDENCE until confirmed. |
| 119 | Q0119 | 2026石景山一模Q20 | NEEDS_FIX + PENDING_BOOK_LEVEL | Block 1409 invents/incorrectly labels `共同促进区域繁荣`; source line 244 says `共同促进普惠包容发展`. It also labels line 238 content as the second `共同` title instead of `共同营造开放型区域经济环境`. |
| 120 | Q0120 | 2025门头沟一模Q19 | PASS + PENDING_BOOK_LEVEL | Formal rubric supports the world-economic globalization branch and all four scoring/boundary layers. Minor wording softening does not block. UQ0039 still not group-reviewed. |

## Source Evidence

- Q0116: `SRC_EXAM_2026_SHUNYI_ERMO_Q20.txt:350-362`; `SRC_RUBRIC_2026_SHUNYI_ERMO_Q20.txt:71-88`; Claude finding `04_claudecode/slice_024_doc116_claudecode_findings.md`.
- Q0117: `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:251-262`; `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66`; Claude finding `04_claudecode/slice_024_doc117_claudecode_findings.md`.
- Q0118: `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230`; `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`; visual check `05_source_backcheck/slice_024/chaoyang_yimo_q20_page7.png`; Claude finding `04_claudecode/slice_024_doc118_claudecode_findings.md`.
- Q0119: `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247`; `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69`; Claude finding `04_claudecode/slice_024_doc119_claudecode_findings.md`.
- Q0120: `SRC_EXAM_2025_MENTOUGOU_YIMO_Q19.txt:218-245,274-276`; `SRC_RUBRIC_2025_MENTOUGOU_YIMO_Q19.txt:26-38`; Claude finding `04_claudecode/slice_024_doc120_claudecode_findings.md`.

## Required Repairs / Holds

- Q0118: Do not treat the 8分/overall cap statement as confirmed-current source truth until a formal scoring source line is found. The content points remain supported.
- Q0119: repair block 1409 to use the exact `五个共同` labels, especially `共同促进普惠包容发展`; preferably restore the second title as `共同营造开放型区域经济环境`.
- All five rows: `同类项合并` remains `PENDING_BOOK_LEVEL`; no normalized question group is accepted in this slice.
