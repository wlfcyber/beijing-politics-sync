# ClaudeCode V8 Decode Independent Run

You are ClaudeCode. Execute an independent V8 decode-version run for:

`飞哥正志讲堂：2026北京高考政治哲学宝典---三年模拟全触发全链条`

This run is named:

`v8_decode版`

Do not call it v6. Do not write "based on v6". Do not put v6 in output filenames or titles.

## Critical correction from the controller

`C:\Users\Administrator\Desktop\4.29凌晨跑完的结果v6` is a Codex-produced result. It is unrelated to this ClaudeCode run. You must run independently.

Forbidden as evidence and forbidden as baseline:

- `C:\Users\Administrator\Desktop\4.29凌晨跑完的结果v6\**`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_outputs\*_v6_*`
- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\worker_reports\*_v6.*`
- `C:\bp_sync_visible\reports\claudecode_v4_final_2026-04-28\final_artifacts\**`
- any old framework entry, old CSV judgment, old final document, old model summary, or old conclusion file.

Allowed control/index files:

- `C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29\SUITE_ROSTER.csv` only as the 56-suite roster.
- `C:\bp_sync_visible\reports\claudecode_v4_final_2026-04-28\compare\08_OCR-needed重跑控制清单.md` only as a gap checklist, not as evidence.
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\S001_2024东城一模.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_RESULTS.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_AUDIT.md`

Important mapping note: in the old OCR rerun package, `S001` means `2024东城一模`. In the 56-suite roster, `2024东城一模` is `S003`. Merge by suite name, not by the old suite id.

## UTF-8 decode guard

This Windows session has an encoding trap. ClaudeCode's built-in `Read` tool can decode UTF-8 Chinese files as system-default encoding and produce mojibake such as `鍚`, `瀛`, `涓`, `鎶`, `锛?`.

Rules:

1. Do not use the built-in `Read` tool for Chinese UTF-8 project files.
2. Use PowerShell or Python with explicit UTF-8 for all Chinese text:
   - PowerShell:
     `$OutputEncoding = [System.Text.UTF8Encoding]::new(); [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new(); Get-Content -Encoding UTF8 -Raw -Path "PATH"`
   - Python:
     `Path("PATH").read_text(encoding="utf-8", errors="replace")`
3. Prefer writing and running Python scripts in this run directory. All scripts must read with `encoding="utf-8-sig"` or `encoding="utf-8"` and write with `encoding="utf-8"`.
4. Before finishing, scan student-facing files for mojibake:
   `鍚|瀛|涓|鎶|锛\?|绛旀|璁鹃|鏉愭|鐭ヨ|摬瀛|鏈濋|娴锋|涓滃`
5. If mojibake exists in a student-facing file, regenerate it before creating DOCX.

## Evidence rules

1. Old conclusions cannot be used as evidence.
2. First-source cache must be read first:
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.jsonl`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_index.jsonl`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\*.md`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\*.md`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\*.txt`
   - `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\**\page_*.png`
3. Cache-first is not cache-only. If the cache is incomplete, unclear, or lacks the full question/material/answer key/rubric boundary, return to the original PDF/PPT/Word or rendered page image.
4. Do not blindly OCR every file. Repair the known gaps and any gap discovered during validation.
5. Do not invent answer keys, question text, scoring rubrics, or framework entries.

## Required OCR-needed and source-gap repair queue

Use the 56-suite roster IDs below.

### Whole-suite OCR/source repairs

- `S003 2024东城一模`: already repaired by ClaudeCode in `reports\ocr_rerun_claudecode_2026-04-28`; merge the valid recovered entries into V8. Recovered answer key: `1C 2B 3A 4A 5D 6D 7A 8D 9B 10C 11A 12B 13D 14C 15C`.
- `S012 2024丰台二模`: repair via cache, render pages, or original source. Recover "统筹发展和安全" and "你的步伐就是中国的步伐" only if the full prompt/material/scoring boundary is confirmed.
- `S042 2026丰台一模`: repair paper OCR if needed. Recover Q16 and "积极识变应变求变" only where complete evidence closes.
- `S044 2026房山一模`: repair paper OCR if needed. Recover Q16(2), Q18(1), Q20 where evidence closes; repair choice-question paper/key if possible.
- `S038 2026海淀一模`: repair paper OCR if needed. Check Q16 for "物质决定意识/一切从实际出发" and related nodes. Do not use old conclusions.
- `S054 2026丰台期末`: repair paper OCR if needed. Recover the "留白" main question with full prompt/material and four philosophy scoring points.
- `S053 2026朝阳期末`: repair paper and rubric OCR if needed. Judge from source whether there are 必修四哲学 entries and choice entries.
- `S049 2026海淀期末`: repair the first 8 paper pages if needed. Recover Q16/Q17/Q21 and affected choice questions where evidence closes.

### Misjudged file-present repair

- `S047 2026顺义一模`: do not treat as missing. Paper is readable and rubric PPTX contains Q16 scoring content. Redo Q16 "破窗效应" with full prompt, material trigger, and source-supported philosophy points such as 量变质变/适度、矛盾转化、联系/系统优化、价值观 where supported. Use answer key if reliable for choice rows.

### True source/answer-key missing boundaries

- `S039 2026西城一模`: main questions may be used if paper and rubric are present; choice questions without reliable 1-15 answer key must remain answer-key-missing unless a reliable key is found locally.
- `S050 2026西城期末`: do not invent question text if paper is missing. Search local source/cache folders; if still missing, mark source-missing in audit only.
- `S055 2026石景山期末`: if only answer/scoring PDF exists and no paper text exists, keep source-missing in audit only.

### Local OCR/image supplements

After the above, check and repair only if evidence can be confirmed:

- `S010 2024东城二模`
- `S005 2024丰台一模`
- `S018 2025东城一模`
- `S019 2025朝阳一模`
- `S026 2025海淀二模`
- `S036 2025朝阳期末`

## Final student artifact shape

The final student-facing document must:

- be titled `2026北京高考政治哲学宝典---三年模拟全触发全链条`;
- have a clean cover page with only the title and large signature `飞哥正志讲堂`;
- reserve page 2 as a foreword section for the user, without process logs;
- be organized by the user's principle/method framework nodes, not by suite order or question order;
- include full question prompts for main-question entries;
- include only key material trigger excerpts, not long pasted passages;
- explain why the material triggers the principle;
- write a concrete answer landing;
- keep source paths, file ids, line ids, slide ids, OCR/debug/process notes, `.pdf`, `.pptx`, `.docx`, `F04`, `L24`, hashes, and raw audit provenance out of student-facing files.

Audit/provenance must go to separate audit files.

## Required outputs

Create outputs under:

`C:\bp_sync_visible\reports\final_56_v8_decode_claudecode_2026-04-29`

Required files:

1. `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md`
2. `outputs\2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.docx`
3. `outputs\北京高考政治选择题错肢总结_v8_decode版.md`
4. `outputs\北京高考政治选择题错肢总结_v8_decode版.docx`
5. `audit\V8_DECODE_AUDIT.md`
6. `audit\V8_DECODE_COVERAGE_MATRIX.csv`
7. `audit\V8_DECODE_CLEANLINESS_SCAN.txt`
8. `BUILD_REPORT_V8_DECODE.md`

## Validation before finishing

Record these checks in `BUILD_REPORT_V8_DECODE.md`:

- `SUITE_ROSTER.csv` has 56 suites.
- No `v6` appears in student-facing filenames or document titles.
- The student-facing Markdown files have no engineering residue:
  `C:\\|source_path|hash|sha256|page_|OCR|debug|visible_runs|crops_|F\d{2}|L\d{2}|slide|pdf|pptx|docx|\.jsonl`
- The student-facing Markdown files have no mojibake residue:
  `鍚|瀛|涓|鎶|锛\?|绛旀|璁鹃|鏉愭|鐭ヨ|摬瀛|鏈濋|娴锋|涓滃`
- Every required repair suite is marked `merged`, `excluded-after-source-check`, or `blocked-with-explicit-reason` in the audit matrix.
- Any true source-missing or answer-key-missing suite remains out of the student final body and appears only in audit.

Now execute the V8 decode independent run.
