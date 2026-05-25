# GPT Pro / Claude App P3 final review prompt

Please review the attached current final Markdown:

`选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md`

Current LF-normalized SHA256:

`3E4BF9D111AA91BE178699387C1FF6862B13C31B7B22A20015DC03D35E7D9EC5`

Context:

- This is a Beijing Gaokao politics 选择性必修一《当代国际政治与经济》 subjective-question student handbook.
- Target quality benchmark: the previously accepted 必修四哲学宝典.
- It must be framework-first, not paper-order-first.
- Each independent `###` example should correspond to one real question/example placement, not merge two different questions into one example.
- Frequency counts in `（出现N次）` should equal the number of independent `###` examples under that core point.
- Student body should not contain audit language, source paths, debug notes, TODOs, or unresolved markers.
- Known P3 repair: a false `2026顺义一模Q19(3)` example was removed because the real task belongs to `经济与社会` future-industry advice/reasoning, not the 选必一 main chain.
- P3 local audit says: 136 core points, 364 core examples, 372 total H3 headings, 0 frequency mismatches, 0 `2026顺义一模Q19(3)`, 0 `2026石景山期末`, 0 TODO/FIXME/待补/待核.
- ClaudeCode Opus 4.7 P3 production-lane recheck returned `PASS_WITH_RISKS`, no `must_fix_now`; external GPT Pro / Claude App final gate is still pending for this exact SHA.

Please output:

```
VERDICT: STRICT_FINAL_ACCEPTED / PASS_WITH_MINOR_PATCH / FAIL_MUST_PATCH

1. coverage_and_scope
2. false_merge_or_two_questions_in_one_example
3. wrong_module_or_wrong_bucket
4. frequency_and_numbering
5. student_teaching_quality_vs_bixiu4_benchmark
6. must_fix_items
7. should_fix_items
8. final_acceptance_sentence
```

Rules:

- Do not invent local source facts.
- If you find a substantive content problem, quote the exact heading or nearby wording and explain why it fails.
- Separate `must_fix_content` from style or readability suggestions.
- If the document is acceptable except for external workflow caveats, say so clearly.
