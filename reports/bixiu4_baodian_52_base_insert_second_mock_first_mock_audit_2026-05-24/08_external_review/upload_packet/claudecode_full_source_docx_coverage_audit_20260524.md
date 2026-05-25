# ClaudeCode Full Source vs DOCX Coverage Audit
**Lane:** ClaudeCode production lane B  
**Date:** 2026-05-24  
**Scope:** 2024–2026 first-mock and second-mock suite-name coverage in final DOCX

---

## 1. Desktop Source Inventory — Independent Verification

Independently enumerated from Desktop folders `2024各区模拟题/`, `2025各区模拟题/`, `2026各区模拟题/` (one/二模sub-folders only; 期中/期末/期末 excluded as out of scope).

| Year | Phase | Count | Suites |
|------|-------|------:|--------|
| 2024 | 一模 | 6 | 东城、丰台、朝阳、海淀、石景山、西城 |
| 2024 | 二模 | 6 | 东城、丰台、朝阳、海淀、西城、顺义思政 |
| 2025 | 一模 | 10 | 东城、丰台、延庆、房山、朝阳、海淀、石景山、西城、门头沟、顺义 |
| 2025 | 二模 | 6 | 东城、丰台、昌平、朝阳、海淀、西城 |
| 2026 | 一模 | 11 | 东城、丰台、延庆、房山、朝阳、海淀、石景山、西城、通州、门头沟、顺义 |
| 2026 | 二模 | 8 | 东城、丰台、房山、朝阳、海淀、石景山、西城、顺义 |
| **TOTAL** | | **47** | |

**Q1 VERDICT: CONFIRMED.** Desktop inventory = 47 suites, exactly matching governor report claim.

**Naming note (non-fatal):** The folder on disk is `2024顺义思政二模`; the governor audit normalizes it to `2024顺义二模`. The source_example path in the CSV correctly points to the `2024顺义思政二模` sub-path, confirming they are the same suite. No suite is lost.

---

## 2. Final DOCX Suite-Name Coverage

Per `FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv`, all 47 suites have `final_docx_mentions ≥ 1`. The two lowest-mention suites are:

| Suite | DOCX Mentions | Note |
|-------|-------------:|-------|
| 2026海淀二模 | 2 | Closure matrix shows 4 weak_evidence resolved, 1 module_boundary; still COVERED_OR_PATCHED |
| 2026通州一模 | 2 | 2 accepted_insertions in matrix; no other blockers |

All 47 suites appear at least twice. No suite has 0 mentions.

**Q2 VERDICT: CONFIRMED.** All 47 suite names present in final DOCX ≥ 1 time (per governor audit which this lane cannot independently re-verify by raw DOCX text extraction; this lane accepts the governor CSV as evidence).

---

## 3. Delta-vs-Base Coverage Split (35 / 12)

### Counting from CSV

**35 DELTA_OR_FIRST_MOCK_MATRIX_CLOSED (COVERED_OR_PATCHED):**
- 2024 一模: 6 suites (all in COVERAGE_CLOSURE_MATRIX_V2.csv)
- 2025 一模: 10 suites (all in closure matrix)
- 2026 一模: 11 suites (all in closure matrix)
- 2026 二模: 8 suites (all in closure matrix)
- Total: 6 + 10 + 11 + 8 = **35** ✓

**12 DOCX_BASE_COVERED_NOT_REOPENED_THIS_DELTA (inherited base):**
- 2024 二模: 6 (朝阳、东城、丰台、海淀、顺义、西城)
- 2025 二模: 6 (昌平、朝阳、东城、丰台、海淀、西城)
- Total: 6 + 6 = **12** ✓

35 + 12 = 47 ✓

**Q3 VERDICT: CONFIRMED.** The report's 35/12 split is internally consistent and independently verified from the source CSV rows.

---

## 4. 2026 Second-Mock Suites — DOCX and Matrix Check

Desktop shows 8 × 2026 二模 suites:

| Suite | DOCX Mentions | In Closure Matrix | Status |
|-------|-------------:|:-----------------:|--------|
| 2026东城二模 | 6 | ✓ | COVERED_OR_PATCHED |
| 2026丰台二模 | 5 | ✓ | COVERED_OR_PATCHED |
| 2026房山二模 | 4 | ✓ | COVERED_OR_PATCHED |
| 2026朝阳二模 | 6 | ✓ | COVERED_OR_PATCHED |
| 2026海淀二模 | 2 | ✓ | COVERED_OR_PATCHED |
| 2026石景山二模 | 3 | ✓ | COVERED_OR_PATCHED |
| 2026西城二模 | 3 | ✓ | COVERED_OR_PATCHED |
| 2026顺义二模 | 5 | ✓ | COVERED_OR_PATCHED |

**Q4 VERDICT: PASS.** All 8 × 2026 二模 suites present in DOCX and in closure matrix. None missing.

---

## 5. 2024–2026 First-Mock Suites — DOCX and Matrix Check

All 27 first-mock suites (6 × 2024 + 10 × 2025 + 11 × 2026) are listed as `COVERED_OR_PATCHED` in both the FULL_SOURCE audit and COVERAGE_CLOSURE_MATRIX_V2.csv. Minimum mentions among 一模 suites:

| Suite | DOCX Mentions |
|-------|-------------:|
| 2024石景山一模 | 4 |
| 2024朝阳一模 | 5 |
| 2026海淀一模 | 6 |

No 一模 suite is absent from either the DOCX mentions column or the closure matrix.

**Q5 VERDICT: PASS.** All 27 × 一模 suites (2024–2026) present in DOCX and closure matrix. None missing.

---

## 6. Inherited-Base Coverage Caveat

The 12 suites classified as `INHERITED_BASE_NOT_REOPENED_THIS_DELTA` (all 2024/2025 二模):

> These suites appear in the final DOCX because they were already present in the accepted handbook base. Their coverage is **suite-name coverage only** — the base rows were not re-extracted, re-scored, or re-inserted during the 2026 二模 / 一模 漏项补强 delta. No row-level re-scoring has been conducted for these 12 suites in this pass. Any concern about the quality or completeness of those rows requires a separate row-level audit pass against the original source files.

**Q6 VERDICT: DOCUMENTED.** Inherited coverage is suite-name-level only, not fresh row scoring.

---

## Summary Table

| Audit Question | Verdict |
|----------------|---------|
| Q1 — Desktop inventory = 47 suites | CONFIRMED |
| Q2 — All 47 suite names in final DOCX | CONFIRMED (governor CSV evidence accepted) |
| Q3 — 35 delta / 12 inherited base split correct | CONFIRMED |
| Q4 — No 2026 二模 suites missing | PASS |
| Q5 — No 2024–2026 一模 suites missing | PASS |
| Q6 — Inherited base = suite-name coverage only | DOCUMENTED |

**SCOPED_PASS** — coverage audit passes at suite-name level with the inherited-base caveat documented.  
Full final all-model PASS is NOT issued. GPTPro web review remains pending.
