# Feynman 2025 Late Culture Worker Report

## Scope

- Run directory: `C:\bp_sync_visible\reports\culture_all_suites_rerun_2026-04-29`
- Assigned suites: S026-S037, covering 2025 二模与期中期末。
- Write scope used: `worker_outputs\feynman_2025_late_culture_entries.csv` and this report only.
- Final Word was not modified.

## Evidence Rules Applied

- Main questions enter the culture table only when the bundle contains a scoring rubric, marking rule, review/lecture rubric, or scan-rubric OCR that explicitly supports culture points.
- Reference answers were not treated as scoring rubrics unless the same bundle section exposed scoring/marking language.
- Choice questions enter only when both stem and reliable answer key or answer explanation are present in the bundle.
- Philosophy chains were kept separate. If a question used 《哲学与文化》 but the scoring point was philosophy-only, it was marked `MODULE_BOUNDARY`.

## Framework 0-7 Coverage

| Slot | Framework Node | Newly Used In This Batch |
|---:|---|---|
| 0 | 载体 | S027 Q9, S030 Q5/Q6, S031 Q16, S034 Q16(1), S035 Q16 |
| 1 | 特点 | S033 Q1, S035 Q4, S037 Q1 |
| 2 | 作用 | S026 Q17, S027 Q20, S029 Q16, S030 Q6, S034 Q1, S035 Q3, S036 Q4 |
| 3 | 横向 | S030 Q16(1), S034 Q3, S036 Q16 |
| 4 | 纵向 | S026 Q17, S029 Q16, S030 Q16(1), S031 Q3/Q16, S033 Q3/Q16, S034 Q16(1), S035 Q16, S036 Q4/Q16 |
| 5 | 文化强国/文化自信 | S027 Q20, S030 Q16(1), S031 Q16, S033 Q3, S034 Q16(1), S035 Q16, S036 Q16, S037 Q1 |
| 6 | 民族精神 | S027 Q1, S034 Q2, S031 Q16 |
| 7 | 习近平文化思想 | S033 Q16 |

## Suite Coverage

| Suite | Status | Main Culture Questions | Culture Choice Questions | Notes |
|---|---|---|---|---|
| S026 2025海淀二模 | PASS | Q17 | none confirmed | Q17 only has 1 分文化补点；choice coverage not forced because bundle did not expose full cultural objective stem+key set. |
| S027 2025西城二模 | PASS | Q20 | Q1, Q9 | Q20 has clear scoring split: cultural rights/supply/needs and talent/innovation. |
| S028 2025东城二模 | PASS | none | Q3, Q4 | Q16 is philosophy-only scoring; culture choice rows entered from reliable key. |
| S029 2025朝阳二模 | PASS | Q16 | Q3, Q4 | Q16 has culture传承、文化濡染、文化功能、文化创新 wording in scoring rules. |
| S030 2025丰台二模 | PASS | Q16(1) | Q5, Q6 | Q16(1) is mixed philosophy+culture; report keeps culture chain separate. |
| S031 2025昌平二模 | PASS | Q16 | Q3 | Main row uses PPT scoring support; choice Q3 is robot秧歌科技赋能文化创新. |
| S032 2025海淀期中 | MODULE_BOUNDARY | none | none | No confirmed culture module question found; objective candidates are economics/politics/legal. |
| S033 2025海淀期末 | PASS | Q16 | Q1, Q3 | Q16 excludes generic文化功能/中华文化特点 because local细则 lists them as typical non-scoring answers. |
| S034 2025西城期末 | PASS | Q16(1) | Q1, Q2, Q3 | Main row covers中轴线文物建筑活化利用. |
| S035 2025东城期末 | PASS | Q16 | Q3, Q4 | Q16 requires saying what the器物承载; only writing文化载体 is explicitly insufficient. |
| S036 2025朝阳期末 | PASS | Q16 | Q4 | Scan-rubric OCR gives culture 6 分 structure: 自信、弘扬、发展、传播. |
| S037 2025丰台期末 | PASS | none | Q1 | Main Q16 is philosophy-only; culture coverage comes from objective Q1 answer explanation. |

## Blockers And Boundaries

- No `BLOCKED` suite in S026-S037.
- S032 is `MODULE_BOUNDARY`, not blocked: local bundle has answer key and stems, but no question was judged to be a culture-module entry under the template.
- S026 choice questions were not expanded because the local bundle evidence used for this run did not expose a reliable full cultural objective stem+answer-key pair. The suite still passes through Q17 culture scoring support.

## Output Counts

- CSV data rows: 41
- Coverage rows: 12
- Subjective rows: 11
- Choice rows: 18
- PASS coverage suites: 11
- MODULE_BOUNDARY coverage suites: 1
- BLOCKED coverage suites: 0
