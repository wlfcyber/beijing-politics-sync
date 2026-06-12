# Development Plan

1. Reproduce the `2026海淀二模 第18题第（1）问` source-boundary error.
2. Extract all current DOCX entries and all `【同题说明】` / detailed scoring claims.
3. Inventory local source candidates for each unique question group.
4. Classify high-risk claims as formal-rubric supported, answer-reference only, formal-rubric missing, or needs manual source inspection.
5. Patch the student-facing Word file to demote or remove unsupported `细则` wording.
6. Render to PDF/images and verify no layout/link/watermark regression.
