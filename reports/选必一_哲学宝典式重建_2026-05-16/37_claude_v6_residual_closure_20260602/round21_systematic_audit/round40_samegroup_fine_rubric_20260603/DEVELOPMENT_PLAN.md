# DEVELOPMENT PLAN

## Root Cause

Round38/Round39 judged many same-question groups "OK" once they matched the main formal rubric layers. The user now correctly points out that this still misses fine-grained rubric information: per-angle scores, replacement terms, "任选/答出几点" rules, max-score limits, and non-scoring boundaries.

## Method

1. Re-extract the current DOCX same-question inventory.
2. Use `2025延庆一模Q20(2)` as a failing regression test: current group must fail because replacement alternatives are absent.
3. Build a fine-rubric audit table for all unique keys:
   - current same-group text;
   - formal source path;
   - formal fine points;
   - missing content;
   - student-facing replacement text if needed.
4. Split the 72 unique keys into independent slices for read-only agent audits.
5. Locally patch confirmed omissions into every duplicate same-question block.
6. Re-extract and render the final DOCX.

## Student-Facing Wording Rule

Use labels like `答题层次`, `角度`, `可替代`, `得分提醒`, `易错边界`. Do not use backend labels like `细则`, `评分`, `评标`, `采分`, `证据`.

## Verification

- Regression: `2025延庆一模Q20(2)` includes the replacement note and appears identically in all duplicate groups.
- Full inventory: 0 inconsistent duplicate groups.
- Forbidden terms: 0.
- Core headings: all deep red/bold/12 pt.
- Render: page images produced and spot checked.
