# Boundary Recovered Canonical Corpus Report

- generated_at: 2026-05-19T15:20:00+08:00
- source: `04_merge_audit/net17_serious_recheck_20260519.md`
- previous_dir: `04_merge_audit/boundary_patched_20260519/`
- output_dir: `04_merge_audit/boundary_recovered_20260519/`

## Decision

The 53-row boundary-patched corpus is superseded for source-exhaustion work by this 56-row boundary-recovered corpus. The old 53-row package remains useful as an earlier bounded artifact, but it is no longer the exhausted legal-subjective corpus.

## Recovered Questions

1. `RECOVER_2024_顺义_二模_17` - 财产制度助力经济社会发展. Evidence level: `reference_only`; do not use as standalone core support.
2. `RECOVER_2025_海淀_二模_18` - 模拟法庭、商标恶意抢注、程序法、证据. Evidence level: `formal`.
3. `RECOVER_2026_通州_一模_20` - 民法典自甘风险、安全保障义务、侵权责任. Evidence level: `formal`.

## Counts

| Item | Before | Added | After |
| --- | ---: | ---: | ---: |
| Question rows | 53 | 3 | 56 |
| Material atoms | 535 | 12 | 547 |
| Ask atoms | 53 | 3 | 56 |
| Rubric atoms | 319 | 18 | 337 |

Evidence level counts after recovery: `{"formal": 51, "reference_only": 5}`.

## Not Counted Yet

- `CC0094_2025_东城_期末_19_3`: pending split; possible legal layer not closed.
- `CC0118_2025_丰台_期末_18_2`: pending dedup/reextract; possible overlap with `CC0119`.
- `UNCERTAIN_2026_丰台_期末_18_MIXED`: newly flagged mixed law boundary row, saved in `uncertain_mixed_law_boundary_review.csv`, not counted in the 56 until reviewed.

## Required Downstream Work

1. Rerun framework validation and sidecar generation against the 56-row corpus.
2. Regenerate handbook sections for the three recovered questions.
3. Keep `RECOVER_2024_顺义_二模_17` as reference/open evidence unless a formal point rubric is found.
4. Do not claim final classroom closure until the recovered corpus is validated and Word/PDF outputs are regenerated.
