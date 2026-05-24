# Patch v6 P0-3 Duplicate Heading Hygiene

Edit only this file:
C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_revisions\选必一_当代国际政治与经济_主观题术语宝典_学生精简版_v6.md

Also read your previous review:
C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\03_claude_opus\CLAUDE_CODE_OPUS_V6_REVIEW_CAPTURE_20260524.md

Goal: fix P0-3 duplicate / near-duplicate core-answer-point bucket issues WITHOUT deleting any question examples.

Hard constraints:
- Preserve exactly 351 ### question-example entries.
- Preserve exactly 351 each of 【什么时候写】, 【设问】, 【为什么能想到】, 【卷面句】.
- Do not merge different questions into one example.
- Same source question with multiple answer points may stay as multiple ### entries and may use 【同题组】 cross references.
- Do not add backend/process/scoring/source language. Do not use 用户硬规则, hard rule, strict-final, 钉死, 分列, 评分, 细则, 参考答案, 来源：, Claude, GPT, Codex, PASS, FAIL.
- Keep the six-bucket framework. Do not move content across book/module boundaries unless the heading is clearly in the wrong bucket.

Patch strategy:
1. For exact duplicate headings within the same bucket, merge the later ### examples under the earlier same heading and delete only the duplicate ## heading and duplicate local boundary note if redundant. Do not delete the ### blocks.
   - United Nations duplicates are the clearest: merge short/long 联合国是当今世界最具普遍性... examples under one heading; merge 联合国对中国对外开放... variants under one heading.
2. For cross-bucket same wording that actually has different answer function, keep both examples but rename headings with clear function qualifiers so they no longer look like duplicated buckets.
   Examples:
   - Political bucket 推动构建人类命运共同体 = international order / global governance direction.
   - China bucket 中国推动构建人类命运共同体 = China proposal/action/contribution.
   - China 坚持正确义利观 variants must be distinguished by use case if not merged: development cooperation, sustainable development responsibility, external cultural/public-opinion environment, South-South cooperation substitution.
   - New型国际关系 variants must be distinguished by their exact rubric function: general relation direction, South-South cooperation,周边工作组合表达, broad global-governance package. If two are truly same function, merge headings and keep all examples under one heading.
3. After editing, scan the file and report:
   - counts for ###, fields, and forbidden terms
   - list of duplicate heading groups resolved
   - any remaining duplicate/near-duplicate heading groups and why they are intentionally distinct

Important: This is a student handbook. Prefer clean student-facing labels over editor notes. Do not write a review report into the student file; only edit the file and report in stdout.
