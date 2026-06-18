# Source Backcheck Slice 009 Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- scope: doc_order 41-45 only
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- backcheck_time: 2026-06-17T17:47:36+08:00

## Evidence Summary

| doc_order | question_ref | source status | evidence pointer | Codex source finding |
|---:|---|---|---|---|
| 41 | 2024海淀二模Q18(1) | source-backed formal rubric + exam prompt | `SRC_EXAM_2024_HAIDIAN_ERMO_Q18.txt:185-205`, `SRC_RUBRIC_2024_HAIDIAN_ERMO_Q18_DOCX.txt:51-53`, `SRC_ANSWER_2024_HAIDIAN_ERMO_Q18_SUPP.txt:15-26` | The source is an 8分时政述评等级题. Official scoring gives broad available angles, not an independent `共同利益` fixed score. The desktop row correctly warns about this but block506 still over-directs "先写共同利益". |
| 42 | 2026西城期末Q20 | source-backed formal rubric via same-source render | `SRC_RUBRIC_2026_XICHENG_QIMO_Q20_VISUAL.txt:3-14`, `SRC_EXAM_2026_XICHENG_QIMO_Q20.txt:80-97` | The 8分 structure is real: 角度1是什么2分, 角度2为什么3分4选3, 角度3效果3分. `共同利益` is a formal 1分 item under why, but the desktop row uses backstage wording "答题要求角度2" and includes cross-module terms without boundary labels. |
| 43 | 2026通州一模Q19 | source-backed formal rubric + visual exam prompt | `SRC_EXAM_2026_TONGZHOU_YIMO_Q19_VISUAL.txt:3-10`, `SRC_RUBRIC_2026_TONGZHOU_YIMO_Q19.txt:160-176` | The 8分 structure is knowledge/measures 4分 plus material function 4分. `共同利益是合作的基础` is one可采知识 in 镜头一, not the full answer. |
| 44 | 2025朝阳二模Q21 | source-backed formal rubric + exam prompt | `SRC_EXAM_2025_CHAOYANG_ERMO_Q21.txt:215-228`, `SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21.txt:283-310` | The 8分 structure is 中国发展需要3分, 区域发展需要3分, 世界发展需要2分. `共同的国家利益是国际合作基础` is a 1分 option inside the 区域发展需要 layer. |
| 45 | 2026房山二模Q20 | source-backed formal rubric + teacher answer | `SRC_EXAM_2026_FANGSHAN_ERMO_Q20.txt:106-118`, `SRC_RUBRIC_2026_FANGSHAN_ERMO_Q20.txt:134-146` | The 8分 structure is six 1分 directions plus material 2分. `共同利益/共同发展` is exactly one 1分 direction, not the whole answer. The desktop row should clarify subject wording because the prompt is about 世界数据组织的智慧, not generic 中国智慧. |

## Boundary

This backcheck verifies source evidence for five entries only. It does not repair the desktop DOCX and does not imply full-book completion.
