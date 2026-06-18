# Slice 025 Source Backcheck Notes

- timestamp: 2026-06-17T23:40:37+08:00
- scope: doc_order 121-125 only.
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- desktop original is read-only; no edits made to the `.docx`.

## Source Coverage

- Q0121 2026丰台二模Q20: reused teacher-version exam answer plus PPTX mismatch/absence evidence; do not promote to formal-rubric-backed unless a matching Q20 rubric is found.
- Q0122 2026房山二模Q20: reused teacher answer and formal rubric evidence for six 1-point directions plus material 2分.
- Q0123 2026通州一模Q19: reused visual prompt and formal rubric evidence for 4+4 structure.
- Q0124 2025朝阳二模Q21: reused exam and formal rubric evidence for 中国/区域/世界 3+3+2 structure.
- Q0125 2025昌平二模Q21: reused slice023 exam/rubric evidence, focusing on the more precise `更加开放、包容的全球经济格局` branch.

## Pre-Claude Codex Watchpoints

- Q0121: likely LOW_EVIDENCE for formal `细则位置`; source is teacher-answer-backed, but matching formal PPTX rubric is absent.
- Q0122: verify that the row points to `世界数据组织` rather than generic `中国智慧`, and that six 1-point directions plus material 2分 are not inflated.
- Q0123: verify the row does not make `多边贸易体制/经济全球化方向` the whole answer; formal rubric is 4分知识 + 4分材料作用.
- Q0124: verify the world-development 2分 branch only, not the entire 周边工作 question.
- Q0125: verify that the protectionism contrast in the desktop trigger is not sourced by the prompt/rubric; the open/inclusive global economic pattern branch itself is source-backed.
