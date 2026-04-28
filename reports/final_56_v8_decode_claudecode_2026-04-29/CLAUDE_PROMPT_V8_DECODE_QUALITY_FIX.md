# ClaudeCode continuation: v8_decode版 quality fix

You are continuing the SAME run:

`C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29`

Do not rename this run. Do not call it v6, v7, or v9. The deliverables must remain `v8_decode版`.

## Why this continuation exists

Your previous run completed with exit_code=0 and produced all required files, but the independent controller rejected the student-facing markdown because it still contains audit/scoring/source-spill residues. This is a quality-fix continuation, not a new plan.

Independent scan result on:

`outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md`

- `v6`: 0
- engineering/path/mojibake residues: 0
- BUT student-facing audit/source-spill residues: 49 total
- terms found: `细则边界`, `阅卷前`, `评分细则`, `参考答案`, `政治与法治`

Examples of unacceptable content in the student version:

- headings named `细则边界`
- phrases such as `阅卷前制定的参考答案`
- `评分细则、答案变通说明`
- `评分细则：评分细则...具体采分点...优秀试卷...存在问题`
- non-philosophy module diagnosis such as `政治与法治` block text
- teacher/audit/process notes such as `学生问题及建议`, `复练试题`, `优秀试卷`, `存在问题`

These may remain in audit files if needed, but not in the student-facing final document.

## Evidence rules remain unchanged

- Do not use any v6 output or old final artifact as evidence.
- Do not use old framework entries, old CSV judgments, or old model summaries as evidence.
- Allowed inputs are only the current run extraction, cache/source bundles already used by this v8_decode run, SUITE_ROSTER as roster/index, OCR-needed control as repair queue, and the already-certified S003 ClaudeCode OCR rerun.
- Cache-first is still required, but cache-only is not required. If source evidence is incomplete, exclude from student body and explain only in audit.

## Required fix

1. Patch the generator or add a deterministic cleanup script in `scripts\` so this quality rule is reproducible.
2. Regenerate the student markdown and both DOCX files.
3. Regenerate audit/build report/cleanliness scan.
4. Keep output filenames exactly:
   - `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md`
   - `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.docx`
   - `outputs\北京高考政治选择题错肢总结_v8_decode版.md`
   - `outputs\北京高考政治选择题错肢总结_v8_decode版.docx`

## Student-version hard gate

Before ending, run an explicit UTF-8 scan over the two student-facing markdown files.

For the philosophy student version, all of these must be zero:

```text
C:\\
source_path
hash
sha256
page_
OCR
debug
visible_runs
crops_
F\d{2}
L\d{2}
slide
pdf
pptx
docx
\.jsonl
v6
鍚|瀛|涓|鎶|锛\?|绛旀|璁鹃|鏉愭|鐭ヨ|摬瀛|鏈濋|娴锋|涓滃
细则边界
阅卷前
阅卷中
评分细则
参考答案
政治与法治
法律与生活
逻辑与思维
优秀试卷
存在问题
学生问题及建议
复练试题
```

For the choice wrong-option markdown, engineering/mojibake/v6 must be zero. Choice-key and wrong-option teaching terms are allowed.

## Content shape after cleanup

The philosophy student version must remain organized by principle/method framework, not by paper order.

Each retained entry should contain only:

- full question prompt
- selected material trigger sentence(s)
- why the material triggers the principle
- concrete answer chain responding to the exact question

Do not include audit labels, score-boundary notes, source path/file names, OCR/debug words, teacher marking process text, or cross-module diagnosis blocks in the student body.

If removing residue causes an entry to lose a valid complete question or concrete answer chain, remove that entry from the student body and record the boundary in `audit\V8_DECODE_AUDIT.md` / `audit\V8_DECODE_COVERAGE_MATRIX.csv`.

## Final response

Report:

- files regenerated
- strict scan counts
- entry count after cleanup
- whether DOCX zip structure was verified

Do not claim PASS unless the hard gate above is zero.
