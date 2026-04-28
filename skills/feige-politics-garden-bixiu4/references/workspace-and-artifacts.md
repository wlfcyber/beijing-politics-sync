# Workspace And Artifacts

## Default Paths

- source root 1: `C:\Users\Administrator\Desktop\2025各区模拟题`
- source root 2: `C:\Users\Administrator\Desktop\2026各区模拟题`
- research repo: `C:\Users\Administrator\Desktop\beijing_politics_research`

## Organizer Outputs

These are created by `scripts/prepare_analyst_workspace.py`:

- `data/reports/exam_suite_inventory.csv`
- `data/reports/cleanup_candidates.csv`
- `data/reports/analyst_workspace_status.md`

## Persistent Knowledge Files

- `data/knowledge/book_method_registry.md`
  - leader-owned
  - stores the seven-book method registry and phase decomposition
- `data/knowledge/master_rubric_summary.md`
  - summarizer-owned
  - cumulative, append-forward summary of confirmed findings

## Governor File

- `data/reports/governor_board.md`
  - governor-owned
  - tracks pass/fail status, reruns, and blockers

## Repo Pipeline Outputs

High-value files after `python -m scripts.pipeline`:

- `data/index/questions.csv`
- `data/index/rubric_matches.jsonl`
- `data/reviews/manual_rubric_review.csv`
- `data/reviews/manual_rubric_review.md`
- `data/reports/final_rubric_coverage.md`
- `data/reports/final_unresolved_questions.csv`
- `data/reports/full_coverage_matrix.csv`

## File Selection Heuristics

When deciding whether a rubric file is canonical:

- prefer files with terms such as `细则`, `评分细则`, `评分标准`, `评标`, `阅卷细则`, `参考答案及评标细则`
- prefer full or final markers such as `全`, `完整`, `定稿`, `最终`
- downgrade files that look like `报告`, `总结`, `讲评`, `实录`, `研修`
- downgrade scan or temporary markers such as `扫描全能王`, `chat_file`, `勿传`
- keep exactly one canonical rubric per suite in the active view

## Governor Minimum Standard

The governor should reject the run if any of the following remains true:

- a suite is missing year, district, or stage without being explicitly marked ambiguous
- no canonical rubric was chosen when clear candidates exist
- a logic chain states conclusions without the trigger and transmission path
- the cumulative summary was rewritten instead of extended
- unresolved items were omitted from the final report
