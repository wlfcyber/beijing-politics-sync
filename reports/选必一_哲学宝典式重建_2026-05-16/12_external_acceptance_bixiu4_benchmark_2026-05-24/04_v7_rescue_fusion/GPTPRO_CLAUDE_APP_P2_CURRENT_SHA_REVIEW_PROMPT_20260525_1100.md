# External Review Prompt For Current P2 SHA

You are reviewing the current final of the Beijing Gaokao politics xuanbiyi subjective-question handbook. Do not rely on older acceptance notes.

Current final SHA256: CF5B597E3B05358F02F0A5B0FD61670A3419A8AC21CA62B94EBD71E00231B5AD
Current local status: local P2 baseline OK, external gates pending.

Attached / supplied files should include:
1. Current student final Markdown: `选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md`
2. `P2_FINAL_LOCAL_GOVERNOR_STATUS_20260525_105245.md`
3. `P2_CURRENT_FINAL_COVERAGE_AUDIT_SUMMARY_20260525_105150.md`
4. `P2_NOT_INDEPENDENT_CANDIDATE_ADJUDICATION_CLOSURE_SUMMARY_20260525_105218.md`
5. `CLAUDECODE_OPUS47_P2_RECHECK_RESULT_20260525_1053.md`
6. `EXTERNAL_GATE_BLOCKER_LOG_20260525_1058.md`

Review tasks:
- Verify the final no longer includes 2026 Shijingshan final / Q19(2) AI-governance examples.
- Verify duplicate core headings were merged without merging distinct question examples.
- Verify the statement `104/104 closed` is used only under the combined standard: independent heading OR explicit adjudication/alias/exclusion ledger. Reject wording that says every P0 candidate has an independent example.
- Check whether the student final can be accepted without in-body source fields if paired with the evidence index and audit files.
- Check concept placement, especially:
  - cooperation-win-win new international relations belongs to political multipolarity;
  - independent peaceful foreign policy and Five Principles belong to China;
  - economic globalization terms must be expression-sensitive, not over-merged unless the rubric phrasing is close/substitutable.
- Judge if the final is comparable to the philosophy handbook in student-facing thickness.

Return exactly:
1. VERDICT: PASS_CURRENT_SHA / PASS_WITH_MINOR_PATCH / FAIL_MUST_PATCH.
2. Required patches, if any, with exact section names.
3. Coverage wording that is allowed.
4. External-gate caveat wording.
5. One final Chinese paragraph telling the user whether this can be called the current final.
