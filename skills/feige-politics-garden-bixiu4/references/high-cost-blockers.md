# High-Cost Blockers And Fast Paths

Use this reference before long corpus runs and when any step takes more than one failed attempt.

## 1. DOCX Tables Rendered As Vertical Strips

Symptom: Word output looked fine structurally, but artifact-tool rendered tables as a narrow column with vertical Chinese text.

Wasted path:

- Tried to force table widths in python-docx and rendered multiple times.

Fast path:

- For dense Chinese research notes, default to paragraph-block layout, not wide tables.
- Use bold field labels: `来源：`、`材料信息：`、`触发知识：`、`触发逻辑：`.
- Only use tables for very small 2-3 column data.

Trigger to switch:

- If first render shows vertical/narrow table text, stop table work immediately and convert to blocks.

## 2. PowerShell Treated Unix Here-Docs As Syntax Errors

Symptom: `python - <<'PY'` failed in PowerShell.

Fast path:

```powershell
@'
print("hello")
'@ | python -
```

Or write a script file with `apply_patch` when it will be reused.

## 3. Unicode Paths And Backslash Escaping Broke Python

Symptom: raw string/path manipulation created unterminated strings or mojibake paths.

Fast path:

- Use `Path.home() / "Desktop"` and `glob()` to discover Chinese folder names.
- Set `$env:PYTHONUTF8='1'`.
- Avoid manual `.replace("\\", "\")` and avoid hardcoded long Chinese paths inside Python when discovery is possible.

## 4. Partial Download Looked Like A PDF

Symptom: `Invoke-WebRequest` timed out after writing a partial file; PyMuPDF reported `pages 0`.

Fast path:

- Prefer `curl.exe -L --fail --connect-timeout 30 --max-time 600 -o file url` for large CDN PDFs.
- After download, verify file size and page count before parsing.
- If page count is `0`, delete/re-download; do not debug extraction logic first.

## 5. Local-Only Search Created False Blockers

Symptom: a worker marked objective answer keys missing after checking local folders; public answer PDFs later solved it quickly.

Fast path:

- Before final blocker, run the escalation ladder:
  1. local canonical folder,
  2. duplicate folders,
  3. zip archives,
  4. rendered/OCR pages,
  5. approved web source search.
- Record exactly which rung solved the problem.

## 6. Reference Answer Was Useful But Not A Rubric

Symptom: answer PDFs solved objective keys and source existence but could not legitimately produce main-question scoring chains.

Fast path:

- Split source use immediately:
  - objective key: usable for choice-answer closure,
  - main-question reference answer: `reference-only`,
  - scoring chain: only rubric/评标/阅卷报告/讲评评分口径/user-confirmed source.

## 7. Agent Role Findings Did Not Automatically Become Work

Symptom: subagents produced good findings, but the main thread still had to discover, merge, and verify each one.

Fast path:

- Require each role to output a `Merge candidates` table.
- Main thread creates `ROLE_FINDING_DISPOSITION.md` before final:
  - finding,
  - source role,
  - status: merged/rejected/blocked/superseded,
  - artifact location,
  - reviewer.

## 8. Long Runs Need A Stop-Loss Rule

If the same subproblem fails twice:

- write the failure to `DECISION_LOG.md`,
- switch method,
- ask whether a deterministic tool or external source is more appropriate,
- do not spend a third attempt on the same tactic without new evidence.

Examples:

- Word table width failed twice -> switch to block layout.
- Web download timed out once and produced invalid PDF -> switch to `curl`.
- local source search failed -> escalate to zip/web/OCR, not another identical `rg`.
