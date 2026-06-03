# DEVELOPMENT PLAN

## 2026-06-03 Round36 Continuation

User correction: `2025朝阳二模` still has a wrong 同题组. This proves the previous round did not fully solve all comparable failures. The document is student-facing, so words such as `证据卡`, `证据边界`, `工程痕迹`, `回源`, `待复核`, `可锁定`, and similar backend/audit language must not appear in the正文交付版.

## Root Cause Hypothesis

1. 同题组仍有一部分是由正文条目、框架桶位或旧风险矩阵推导出来的，而不是由正式评分细则/评标层次直接生成。
2. Some fallback text correctly protected source boundaries, but it used backend language. That belongs in audit/control files, not in the student DOCX.
3. The verifier overchecked obvious six-bucket residue, but did not prove that every high-risk 同题组 follows its own rubric scoring layers.

## Required Fix

1. Lock `2025朝阳二模` against the real source/rubric material and replace all same-question blocks for that question with a student-facing rubric-layer 同题组.
2. Run a full document scan for:
   - six-bucket same-group residue;
   - backend words and audit phrases;
   - fallback same-group prose that exposes source/evidence boundaries;
   - repeated-risk same-question titles still using non-rubric structures.
3. Replace backend fallback wording with student-facing study wording, such as `本题暂不作为同题组归纳` or `本题只保留正文答题点，不展开同题组`.
4. Preserve all existing visual requirements: watermark, red/bold `核心答题点：`, answer-highlight boxes, and the user's six-element framework.

## Verification

Before delivery, prove the following from current DOCX state:

- `2025朝阳二模` extracted 同题组 no longer contains framework-bucket expansion or backend evidence language.
- Forbidden student-facing engineering words count is zero for the final DOCX.
- Old same-group bucket residues count is zero.
- `核心答题点：` remains deep red and bold.
- Final DOCX renders to page images for visual QA.
