# Slice 028 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T01:18:52+08:00
- scope: doc_order 136-140 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- ClaudeCode lane: real `claude -p --model opus --effort max`, stream init resolved to `claude-opus-4-8` for doc136-doc140.
- ClaudeCode exception trace: doc139 first attempt preserved `04_claudecode/slice_028_doc139_attempt1_stream.jsonl`; successful rerun used for merge.

## Result Summary

| doc_order | entry_id | source | merged result | required action |
|---:|---|---|---|---|
| 136 | Q0136 | 2025西城二模Q19(2) | PASS with UQ0020 book-level hold | No entry repair; optional redundancy between two world-meaning points can be cleaned later. |
| 137 | Q0137 | 2026石景山一模Q20 | NEEDS_FIX | Restore `结合材料` and exact `五个共同` source headings, especially `共同促进普惠包容发展`. |
| 138 | Q0138 | 2026朝阳期末Q20 | NEEDS_FIX | Repair same-question scoring notes: `互利共享` -> `互利共赢`; restore `主权、安全、发展利益是国家核心利益`. |
| 139 | Q0139 | 2026东城一模Q19(3) | PASS with UQ0021 book-level hold | No entry repair; later review UQ0021. |
| 140 | Q0140 | 2026西城二模Q19(2) | PASS with UQ0074 book-level hold | No entry repair; later review UQ0074 and related members 307/401. |

## Source Evidence

- Q0136: exam/reference `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-224,303-306`; rubric `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-71`.
- Q0137: exam/reference `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247,311-328`; rubric `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69`. Source line 244 is `共同促进普惠包容发展`, not `共同促进区域繁荣`.
- Q0138: exam OCR `SRC_EXAM_2026_CHAOYANG_QIMO_Q20_OCR.txt:273-286`; rubric visual `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_VISUAL.txt:4-16`; rubric cache `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_CACHE_FROM_SAME_SOURCE.txt:119-134`.
- Q0139: exam/reference `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:218-227,305-308`; rubric `SRC_RUBRIC_2026_DONGCHENG_YIMO_Q19_3.txt:16-28`.
- Q0140: exam/reference `SRC_EXAM_2026_XICHENG_ERMO_Q19_2.txt:138-143,165-176`; rubric OCR `SRC_RUBRIC_2026_XICHENG_ERMO_Q19_2_OCR.txt:211-220`.

## Merge Notes

- Q0136 is slice-level PASS. The formal sources support the prompt, zero-tariff/open-market trigger, and 5分=中国担当3分+世界意义2分 structure. The answer has a non-blocking redundancy because `建设开放型世界经济` and `促进贸易自由化` sit in the same optional world-meaning group.
- Q0137 is NEEDS_FIX. The core term is acceptable, but the desktop prompt omits `结合材料`, and the material-trigger block miscopies the exact `五个共同` labels. The fifth label must be `共同促进普惠包容发展`.
- Q0138 is NEEDS_FIX only in same-question scoring reproduction. The economic-angle core, prompt and answer pass, but scoring notes must restore `互利共赢` and the theory phrase `主权、安全、发展利益是国家核心利益`.
- Q0139 is slice-level PASS. The source/rubric support the high-level-opening and industrial-chain-resilience relationship; the broad core wording is acceptable as a focused open-economy entry, while the full 4+3+1 structure remains visible.
- Q0140 is slice-level PASS. `开放合作和包容普惠` is a valid two-suggestion angle. The material trigger has a soft precision caveat around 主权平等/网络主权 and 安全保障, but not a hard source contradiction.

## Boundary

This merge accepts only doc_order 136-140 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 141; 421 entries remain pending.
