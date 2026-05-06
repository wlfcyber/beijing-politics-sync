# Phase12 Source Recheck: 2024 海淀二模第17题第(1)问

Question ID: `Q-2024海淀二模-17-1`

Decision: `SCIENCE_ONLY_SOURCE_SUPPORTED`

## Sources Checked

- Paper: `02_extraction/priority_queue_sources/text/027_Desktop_2024模拟题_海淀二模_试卷_试卷.pdf.txt`, lines 202-224.
- Rubric: `02_extraction/priority_queue_sources/text/028_Desktop_2024模拟题_海淀二模_细则_细则.docx.txt`, lines 9-13.
- Supplemental answer: `02_extraction/priority_queue_sources/text/029_Desktop_2024模拟题_海淀二模_细则_补充材料_高三二模_政治答案_2_.docx.txt`, lines 12-14.

## Source Findings

The original prompt asks: `结合材料，说明此次时间利用调查是如何体现科学思维的。（7分）`

Therefore the original question is not a three-module prompt. It should not be rewritten as `科学思维、创新思维、辩证思维` in parallel.

The rubric and supplemental answer support three landing dimensions under the science-thinking prompt:

1. `全面、真实、准确` understanding of resident time use: pursuit of objectivity.
2. Compared with previous surveys, broader scope, more subjects, richer content, electronic/new tools: new thinking/method and exploratory scientific investigation.
3. Staged arrangement with clear tasks: overall arrangement of a complex investigation.

## Patch Decision

Keep the question stem as science-only.

Patch the body to explain that `探索性` and `整体安排` are source-supported landing points under the science-thinking prompt, not a rewritten innovation/dialectical three-angle prompt.

Status: `PATCH_REQUIRED_AND_APPLIED_TO_REVIEW_BODY`
