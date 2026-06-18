# Slice 027 Codex + ClaudeCode Merge

- timestamp: 2026-06-18T00:47:59+08:00
- scope: doc_order 131-135 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop_source_mutation: none
- ClaudeCode lane: real `claude -p --model opus --effort max`, stream init resolved to `claude-opus-4-8` for doc131-doc135.

## Result Summary

| doc_order | entry_id | source | merged result | required action |
|---:|---|---|---|---|
| 131 | Q0131 | 2024朝阳一模Q21 | PASS with UQ0005 book-level hold | No entry repair; later review UQ0005. |
| 132 | Q0132 | 2025西城二模Q19(2) | NEEDS_FIX | Restore 中国担当3分 as main answer layer; keep world-meaning points optional. |
| 133 | Q0133 | 2026石景山一模Q20 | NEEDS_FIX | Restore exact `五个共同` wording and source `结合材料` prompt phrase. |
| 134 | Q0134 | 2026通州期末Q20 | NEEDS_FIX | Separate material wording from inference and remove overbinding of 各国人民愿望. |
| 135 | Q0135 | 2025石景山一模Q17(2) | NEEDS_FIX | Replace altered answer sentence with the official 普惠包容经济全球化 point. |

## Source Evidence

- Q0131: exam `SRC_EXAM_2024_CHAOYANG_YIMO_Q21.txt:372-376`; DOCX rubric `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_DOCX.txt:88-99`; PPTX rubric `SRC_RUBRIC_2024_CHAOYANG_YIMO_Q21_PPTX.txt:1224-1317`. Codex additionally checked lines 1308-1317, which confirm the single-dimension cap noted by ClaudeCode as initially needing later evidence.
- Q0132: exam/reference `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-224,303-306`; rubric `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-71`.
- Q0133: exam/reference `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247,311-328`; rubric `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69`. Source line 244 is `共同促进普惠包容发展`, not `共同促进区域繁荣`.
- Q0134: exam/reference `SRC_EXAM_2026_TONGZHOU_QIMO_Q20.txt:209-222,303-309`; PPTX rubric `SRC_RUBRIC_2026_TONGZHOU_QIMO_Q20_PPTX.txt:125-145`. Rubric line 141 keeps `时代主题、经济全球化、顺应各国人民愿望等` as a broad `基本都给` point.
- Q0135: exam/reference `SRC_EXAM_2025_SHIJINGSHAN_YIMO_Q17_2.txt:211-237,361-369`; rubric `SRC_RUBRIC_2025_SHIJINGSHAN_YIMO_Q17_2.txt:28-43`.

## Merge Notes

- Q0131 is slice-level PASS. The formal sources support the prompt, the 4+5 structure, the economic-globalization branch, and the single-dimension cap. Its duplicate group UQ0005 remains unaccepted at book level.
- Q0132 is NEEDS_FIX because the desktop answer misses the main 中国担当3分 layer and treats the world-meaning optional items as a required chain.
- Q0133 is NEEDS_FIX. ClaudeCode marked the `五个共同` error; Codex is stricter and also marks the omitted `结合材料` in the prompt field as a fix because this run checks set-question text exactly.
- Q0134 is NEEDS_FIX because the answer overbinds `各国人民愿望` to `推进普惠包容经济全球化/共享发展成果`, while source/rubric keep those as broad or parallel points.
- Q0135 is NEEDS_FIX because `特别是发展中国家` is unsupported, `实现共同发展繁荣` is missing, and the field currently records a score requirement rather than the actual material trigger. Codex is stricter than ClaudeCode on the material-trigger field.

## Boundary

This merge accepts only doc_order 131-135 as reviewed. It does not repair the desktop DOCX and does not claim full-book completion. Continue from doc_order 136.
