# TASK_BRIEF

run_id: raw_exam_subjective_compilation_2026-06-02
module: 选择性必修二《法律与生活》
task: 从桌面 2024-2026 原始试卷/答案/细则文件中从零抽取法律主观题，生成习题汇编。
requested_output: 选必二法律与生活_习题汇编_2024-2026.md

## User Requirements

- 从零重跑；不得读取、参考、复用已有汇编、题包、整理稿等成品文件。
- 唯一内容证据为桌面 2024、2025、2026 三年原始试卷及其答案、评分细则、评标、阅卷总结、讲评等原始评分来源。
- 逐套试卷、逐题、逐设问排查；以设问为最小单位判定选必二法律题。
- 只收录主观题；选择题不进入本汇编。
- 每道题只保留三个部分：材料、设问、细则。
- 材料、设问、细则必须原文照录，不改写、不缩写、不归纳、不加解析、不加点评。
- 若只有参考答案而无独立评分细则，使用参考答案充当细则，并在条目中标注【仅有参考答案，无独立细则】。
- 归属难以判定的设问标记【待确认】并保留一句判定理由。
- 输出文件开头放覆盖清单表，结尾放总计设问数与【待确认】清单。
- 增量写盘：每处理完一套试卷，更新主文件和进度日志。

## Source Boundary

Included roots:

- /Users/wanglifei/Desktop/2024模拟题
- /Users/wanglifei/Desktop/2025模拟题
- /Users/wanglifei/Desktop/2026模拟题
- Other Desktop files/folders whose paths indicate 2024, 2025, or 2026 exam papers, if discovered by the inventory scan.

Excluded as content evidence:

- Any existing compilation, handbook,题包,整理稿,汇编,最终版,框架,候选框架,old outputs, previous selected-module artifacts, or generated teaching documents.
- Any file under this run output directory except control and generated logs.
- Any old 选必二 conclusion, count, framework, or candidate list.

## Completion Criteria

- Candidate paper/source inventory is written and printed.
- Every scanned suite has coverage status: has_xuanbier, no_xuanbier, uncertain, or blocked_conversion.
- Every extracted legal subjective item has material, prompt, and rubric/reference-answer text.
- Final Markdown contains only material, prompt, rubric/reference-answer for each item plus required coverage/statistics sections.
- Governor and acceptance notes name blockers honestly; no false closure if OCR/conversion/rubric gaps remain.
