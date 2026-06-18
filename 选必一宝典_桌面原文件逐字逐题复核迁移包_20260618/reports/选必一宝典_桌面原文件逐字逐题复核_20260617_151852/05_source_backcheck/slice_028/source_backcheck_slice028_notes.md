# Slice 028 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 136-140 only
- backcheck_time: 2026-06-18T01:01:49+08:00

## Source Routing

| doc_order | question | source evidence | routing note |
|---:|---|---|---|
| 136 | 2025西城二模Q19(2) | `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-224,303-306`; `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-71` | Reused slice027 formal exam/rubric for the same source question. |
| 137 | 2026石景山一模Q20 | `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247,311-328`; `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69` | Reused slice027 formal exam/rubric; watch exact fifth 五个共同 and `结合材料`. |
| 138 | 2026朝阳期末Q20 | `SRC_EXAM_2026_CHAOYANG_QIMO_Q20_OCR.txt:273-286`; `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_VISUAL.txt:4-16`; `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_CACHE_FROM_SAME_SOURCE.txt:119-134` | Used OCR cache for the scanned exam and visual/OCR rubric because the direct PDF text layer is sparse. |
| 139 | 2026东城一模Q19(3) | `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:218-227,305-308`; `SRC_RUBRIC_2026_DONGCHENG_YIMO_Q19_3.txt:16-28` | Reused slice015 formal exam/rubric. |
| 140 | 2026西城二模Q19(2) | `SRC_EXAM_2026_XICHENG_ERMO_Q19_2.txt:138-143,165-176`; `SRC_RUBRIC_2026_XICHENG_ERMO_Q19_2_OCR.txt:211-220` | Desktop rubric PDF has no text layer; rendered pages were OCRed with RapidOCR, with page 13 carrying Q19(2) rules. |

## Watchpoints

- Q0136: Same official 5分 frame as Q0132, but this row's core is `建设开放型世界经济`; distinguish 中国担当3分 from 世界意义2分 optional points.
- Q0137: Same source as Q0133; check whether `共同促进区域繁荣` and omitted `结合材料` recur.
- Q0138: 朝阳期末 Q20 is a four-angle 8分 question; this entry is only the economic angle, not the whole answer.
- Q0139: 东城一模 Q19(3) is 4+3+1 about 高水平开放 and 产业链韧性; verify whether `建设开放型世界经济` is a source-backed core or too broad.
- Q0140: 西城二模 Q19(2) asks for 2 suggestions, 2分 each; examples/angles include 主权平等、开放合作、包容普惠、安全保障.
