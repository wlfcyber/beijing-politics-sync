# Phase12 Batch01 Source Excerpt Status

Status: `BATCH01_SOURCE_REPAIR_REVIEW_ONLY`

Created: 2026-05-05 17:58 CST

Purpose: repair the first 12 non-body rows from the 74-row evidence pool before any broader正文扩容. This file is an audit/source-control file, not a student artifact.

Hard gate remains:

- no Word
- no PDF
- no final PASS
- no 终稿
- no 宝典成品

## Summary

- Batch rows checked: 12
- Source/prompt visible: 12
- Answer/rubric visible: 12
- Ready for review-only body drafting: 12
- Still blocked in this batch: 0

## Row Status

| question_id | source status | answer/rubric status | repair decision | note |
|---|---|---|---|---|
| Q-2024朝阳二模-7 | paper lines 109-128 show full Q7 options | answer table in 023 shows Q7=D | `READY_FOR_REVIEW_BODY` | Logical form: D states invalid structure blocks guaranteed conclusion; A/B/C are traps. |
| Q-2025东城期末-18-2 | paper lines 199-203 show登月服 material and prompt | inline answer lines 696-698 supports联想、思路新/方法新/结果新、聚合/发散 | `READY_FOR_REVIEW_BODY` | Innovation-thinking subjective entry. |
| Q-2026通州期末-9 | paper lines 126-132 show医保+商保 question and options | answer table lines 319-330 shows Q9=D | `READY_FOR_REVIEW_BODY` | System/digital integration choice signal. |
| Q-2024朝阳期中-18 | paper lines 225-232 show楚王/晏子 prompt | formal rubric lines 57-78 supports不完全归纳、轻率概括、类比推理 | `READY_FOR_REVIEW_BODY` | Two-part reasoning subjective entry. |
| Q-2025丰台期末-18-1 | paper lines 239-251 show prompt | inline answer lines 569-571 supports必要条件假言判断、联言判断 and保真条件 | `READY_FOR_REVIEW_BODY` | Judgment-type and truth-condition entry. |
| Q-2025顺义一模-17-1 | paper lines 246-255 show甲乙丙 statements and prompt | rubric lines 25-29 supports充分条件假言判断、必要条件假言判断、相容选言判断 | `READY_FOR_REVIEW_BODY` | Composite-judgment true-condition entry. |
| Q-2026东城期末-17-2 | paper lines 221-239 show three claims and prompt | rubric slides lines 332-342 support矛盾律、联言判断、充分条件假言推理 traps | `READY_FOR_REVIEW_BODY` | Formal-logic主观题, not思维主链. |
| Q-2026东城一模-6 | paper lines 64-72 show画马 question | paper answer table lines 324-331 shows Q6=D | `READY_FOR_REVIEW_BODY` | Cross row:联想/形象思维/换质位 trap. |
| Q-2026丰台一模-4 | supplemental source lines 79-94 show凹曲屋面 question | supplemental answer table line 418 shows Q4=A | `READY_FOR_REVIEW_BODY` | 思维 choice:实践积淀 + 综合思维. |
| Q-2026丰台一模-7 | supplemental source lines 135-154 show四诊法 question | supplemental answer table line 418 shows Q7=B | `READY_FOR_REVIEW_BODY` | Scientific-thinking/medical reasoning choice. |
| Q-2026朝阳期中-13 | paper lines 148-158 show石榴籽 question | paper answer table lines 313-326 shows Q13=D | `READY_FOR_REVIEW_BODY` | 思维抽象 + 联想思维 choice. |
| Q-2026顺义一模-6 | paper lines 82-93 show人机认知边界 question | raw pptx XML slide 1 extracted answer table shows Q6=A | `READY_FOR_REVIEW_BODY` | Source repaired from raw pptx XML, not inherited from old text artifact. |

## Direct Repair Notes

1. `Q-2024朝阳二模-7`: A is not simply "中项不周延"; the tighter trap is小项不当周延/小项扩大. This correction must follow into any student正文.
2. `Q-2025东城期末-18-2`: must write at least联想思维 plus思路新、方法新、结果新 and发散/聚合, not just "创新思维".
3. `Q-2026通州期末-9`: D is a choice-question signal about系统化、数字化模式整合保障资源形成机制; do not promote it into a subjective思维主链 without a scoring source.
4. `Q-2026东城期末-17-2`: this belongs under推理/形式逻辑; do not mix it into思维方法主链.
5. `Q-2026顺义一模-6`: answer source is repaired by re-extracting raw `细则.pptx` slide 1 XML: Q1-5 = B/C/C/A/D, Q6-10 = A/D/A/B/B, Q11-15 = D/B/C/D/C.
