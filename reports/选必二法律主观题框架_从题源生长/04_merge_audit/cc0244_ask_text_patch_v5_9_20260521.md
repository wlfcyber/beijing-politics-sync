# CC0244 Ask Text Patch V5.9

- question_id: `CC0244_2026_东城_期末_18`
- status: derived_v5_9_patch_not_overwriting_step29_canonical

## Old ask_text

运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。

## New ask_text

（1）运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。（2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？

## Reason

V5.9 core run trains CC0244 as a two-part question. The zero-baseline blind-test packet exposed that `merged_subjective_law_questions.csv` still only carried第（1）问, while the V5.9 core CSV and student handbook include第（2）问.

This patch writes a derived merged-questions copy for V5.9 use without overwriting STEP_29 canonical evidence. Promotion into canonical should be done only after source-card review.
