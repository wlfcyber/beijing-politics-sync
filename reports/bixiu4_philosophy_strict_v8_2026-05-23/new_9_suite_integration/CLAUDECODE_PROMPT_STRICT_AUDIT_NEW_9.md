# ClaudeCode strict audit prompt: 必修四哲学 v8 新增9套并入

你是独立审计员，不要改文件，只输出审计结论。

请严格审计以下文件：

- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/必修四哲学材料-知识触发框架_v8_65套新增卷子并入版.md`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/new_9_suite_integration_audit.md`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/new_9_suite_main_entries.csv`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/new_9_suite_choice_entries.csv`
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/new_9_suite_boundary_exclusions.csv`
- 通州证据：`reports/bixiu4_philosophy_strict_v8_2026-05-23/tongzhou_yimo_extract/26 通州一模评标.txt`
- 通州题面渲染目录：`reports/bixiu4_philosophy_strict_v8_2026-05-23/tongzhou_yimo_extract/rendered_pages/`
- 二模审计源：`reports/bixiu4_philosophy_coverage_patch_2026-05-23/claudecode_second_mock_philosophy_review.md`

审计标准：

1. 新增9套是否都有处理结论：2026东城二模、丰台二模、房山二模、朝阳二模、海淀二模、石景山二模、西城二模、顺义二模、通州一模。
2. 正式进入学生正文的条目是否都有正式细则/评标支持，尤其是高风险词：辩证否定、量变质变、主次矛盾、矛盾主次方面、两点论重点论、主流支流、价值观导向。
3. 是否把《逻辑与思维》《政治与法治》《当代国际政治与经济》的题错误塞进必修四哲学正文。
4. 通州一模第18题和第21题的处理是否稳；第17(2)、16、19是否正确边界排除。
5. 选择题是否只作为选择题速记，没有反推成主观题评分链。
6. 学生版是否仍然存在“新增二模只放在末尾补丁”的问题。
7. 找出必须删除、必须改写、可以保留、需要补证据的项。

输出格式：

- 总结论：PASS / PASS_WITH_BOUNDARIES / FAIL，只能选一个。
- 必须修改项：逐条列出。
- 可保留项：逐条列出。
- 需要补证据项：逐条列出。
- 对通州一模的单独判断。
- 对8套二模的单独判断。

不要客套，直接给审计意见。
