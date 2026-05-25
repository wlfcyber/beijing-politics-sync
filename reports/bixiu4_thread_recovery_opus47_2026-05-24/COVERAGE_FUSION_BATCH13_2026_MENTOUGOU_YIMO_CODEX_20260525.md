# Coverage Fusion Batch13 - 2026门头沟一模

timestamp: 20260525_042738
operator: Codex recovery thread
suite: 2026门头沟一模
status: CODEX_BATCH13_SOURCE_COVERAGE_APPLIED

## Applied To DOCX / Ledger / Accepted

- 17. 2026门头沟一模 第4题（选择题）
- 16. 2026门头沟一模 第5题（选择题）
- 28. 2026门头沟一模 第7题（选择题）
- 16. 2026门头沟一模 第16题（主观题）
- 6. 2026门头沟一模 第16题（主观题）
- 18. 2026门头沟一模 第16题（主观题）
- 12. 2026门头沟一模 第16题（主观题）
- 22. 2026门头沟一模 第16题（主观题）
- 14. 2026门头沟一模 第21题（主观题）
- 15. 2026门头沟一模 第21题（主观题）

## Matrix Disposition

- Existing Q4, Q5, Q16 x5, and Q21 x2 DOCX rows were registered in `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Q7 was newly inserted under `实践是认识的基础`.
- Missing boundary rows were added for Q3, Q6, and Q10.
- Q1, Q2, Q8-Q15, Q17-Q20, and Qunknown were closed as source-supported module-boundary or extraction-residue decisions.
- Q18 was excluded because Q18(1) is 《法律与生活》 and Q18(2) is explicitly 《逻辑与思维》; broad near-neighbor terms were not used to force a 必修四 placement.
- Suite-level rows were closed after per-question rows were updated.

## Boundary

No Sonnet/Haiku/model-unknown output was used. Q21 is labeled as comprehensive angle support, not a point-by-point detailed scoring rule.
