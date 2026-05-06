# Phase11D Seed Must-Fix: Q-2024海淀二模-17-1

Status: `SOURCE_SCOPE_REPAIRED_FOR_REVIEW_ONLY_NOT_BODY_AUTHORIZATION`

GPT Phase12 flagged this row as `MUST_FIX_SOURCE_OR_SCOPE`.

## Source Check

Paper source:

- `02_extraction/priority_queue_sources/text/027_Desktop_2024模拟题_海淀二模_试卷_试卷.pdf.txt`
- Lines 202-224 show the question material and the actual prompt.
- Actual prompt: `（1）结合材料，说明此次时间利用调查是如何体现科学思维的。（7 分）`

Rubric source:

- `02_extraction/priority_queue_sources/text/028_Desktop_2024模拟题_海淀二模_细则_细则.docx.txt`
- Lines 9-13 show Q17(1) answer and note.
- Rubric answer names: `全面、真实、准确` / `客观性`; `思路新、方法新` / `探索性`; `范围广、对象多、内容更丰富、敢用新手段、试用新工具、创造性地解决问题`; `整体性，分阶段实施，每个阶段主要任务明确`.
- Rubric note: if only one angle is written with good theory-material combination, give 3 points.

## Repair Decision

The original paper asks only `科学思维`, not a three-angle prompt explicitly asking scientific thinking, innovative thinking, and dialectical thinking. Therefore the seed should not be rewritten as if the original prompt named all three modules.

However, the formal rubric itself supports `探索性` and `整体性` under the answer to this science-thinking prompt. The repair should keep these source-backed rubric points but explain them as source/rubric-supported scoring angles inside the Q17(1) answer, not as an invented three-module prompt.

## Revised Review-Only Student Entry

### 2024 海淀二模第17题第(1)问

【材料触发点】

时间利用调查采集居民在“个人生理必需活动、有酬劳动、无酬劳动、个人自由支配活动”等方面的时间投入，目标是“全面、真实、准确”了解居民时间利用情况；与前两次调查相比，本次调查范围首次拓宽到全国，对象扩展至 6 周岁以上常住成员，首次全面使用电子化采集方式，活动分类更加细化，并按准备、组织实施、资料开发应用等阶段推进。

【设问】

结合材料，说明此次时间利用调查是如何体现科学思维的。

【为什么能想到】

本题设问只问科学思维，不能把设问改成科学思维、创新思维、辩证思维三模块并列。但细则在科学思维答案中明确支持三个落点：调查目标“全面、真实、准确”，触发科学思维追求客观性；调查范围、对象、采集方式和分类方式出现新变化，触发细则中的“思路新、方法新、探索性”；调查工作分阶段推进、任务明确，触发细则中的整体安排。

【答案落点】

此次时间利用调查以全面、真实、准确了解居民时间利用情况为目标，能够客观反映居民生活质量和生活模式变化，体现科学思维追求认识的客观性。与前两次调查相比，本次调查拓宽范围、扩展对象、使用电子化采集方式、细化活动分类，体现调查思路新、方法新和探索性。调查工作按准备、组织实施、资料开发应用等阶段推进，每个阶段任务明确，有利于把复杂调查作为整体安排并形成科学认识。

## Remaining Gate

This repair resolves the source/scope conflict for review purposes. It still does not authorize Word/PDF/final. It must be carried into Phase12 expanded body only through the 74-row decision matrix.
