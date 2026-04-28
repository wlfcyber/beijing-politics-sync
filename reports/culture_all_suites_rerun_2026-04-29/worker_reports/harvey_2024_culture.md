# harvey 2024 culture worker report

## Scope

- Run directory: `C:\bp_sync_visible\reports\culture_all_suites_rerun_2026-04-29`
- Assignment: S001-S015, all 2024 suites.
- Write scope honored: only `worker_outputs\harvey_2024_culture_entries.csv` and this report.
- Rule applied: cache-first. I used each roster `bundle_path` first; when bundle text was scan-only or incomplete, I recorded the rendered-image/supplement boundary instead of upgrading weak evidence.

## Framework

Entries use the user culture framework:

0. 载体
1. 特点
2. 作用
3. 横向
4. 纵向
5. 建设文化强国，树立文化自信
6. 民族精神
7. 坚持习近平文化思想

Subjective rows were admitted only when the evidence was a formal rubric, marking summary, evaluation PPT, lecture scoring source, or the provided prior复核 table classified the item as A/B. Reference-only material is marked as a boundary or blocker.

## Suite Coverage

| suite_id | suite_name | status | culture handling |
| --- | --- | --- | --- |
| S001 | 2024海淀一模 | PASS | Choice 1/4 and subjective 16 processed. Subjective 16 is B-level rubric support, not逐点标分. |
| S002 | 2024西城一模 | PASS | Choice 4/10 and cross-module subjective 18(3) processed. |
| S003 | 2024东城一模 | PASS | Choice 1/2/3 processed from rendered paper/key; subjective 16 formal rubric processed. |
| S004 | 2024朝阳一模 | PASS | Choice 1/2/5 and subjective 18(2) processed; 18(2) is B-level support. |
| S005 | 2024丰台一模 | PASS | Choice 1/2 and subjective 21 B-level support processed. |
| S006 | 2024石景山一模 | BLOCKED | Culture signal exists in teacher-version answer, but current evidence is reference/level only, not a formal scoring source. |
| S007 | 2024门头沟一模 | BLOCKED | Roster marks classification-bundle-supplement; objective supplement exists, but subjective culture remains reference-only boundary. |
| S008 | 2024海淀二模 | PASS | Choice 15 and subjective 21 B-level support processed. |
| S009 | 2024西城二模 | PASS | Subjective 18(4)乡村文化振兴 B-level support processed. |
| S010 | 2024东城二模 | PASS | Choice 1/2 processed from rendered paper/key; subjective 16 formal rubric and 21 B-level support processed. |
| S011 | 2024朝阳二模 | PASS | Choice 4 and subjective 19(3) formal rubric processed. |
| S012 | 2024丰台二模 | BLOCKED | Paper is rendered-ocr-needed in bundle and no culture subjective rubric was verified. |
| S013 | 2024顺义思政二模 | PASS | Choice 3/4 processed from text bundle and answer key. |
| S014 | 2024海淀期中 | MODULE_BOUNDARY | Prior复核 excludes 2024海淀期中 subjective questions from 必修四文化. |
| S015 | 2024朝阳期中 | PASS | Subjective 17 formal rubric processed. |

## Evidence Notes

- S003 and S010 objective choices used cached rendered page images because the suite bundle records the question PDFs and answer PDFs as `rendered-ocr-needed`. The CSV marks these as `objective_key_rendered`.
- S007 remains a hard boundary because the roster source is a classification bundle plus supplement; the prior文化复核 explicitly says only objective answer source was supplemented and subjective reference/level descriptions must not be promoted.
- S006 and S012 are blocked rather than forced: S006 lacks formal scoring evidence for the culture chain, and S012 does not provide enough readable objective evidence to safely certify culture choice coverage.
- S014 is a module boundary, not a failure: the prior复核 says the subjective modules are 必修2、必修3、选择性必修1, so no 必修四文化主观链 is created.

## Counts

- Suites processed: 15
- CSV rows including header: 34
- Data entries: 33
- PASS suites: 11
- MODULE_BOUNDARY suites: 1
- BLOCKED suites: 3
