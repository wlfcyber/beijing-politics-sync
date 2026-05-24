# Word Rebuild QA - App Claude Patch

## Files

- Markdown source: `选必一_当代国际政治与经济_主观题术语宝典_学生版.md`
- Word output: `选必一_当代国际政治与经济_主观题术语宝典_学生版.docx`
- Previous backups:
  - `选必一_当代国际政治与经济_主观题术语宝典_学生版_backup_before_appclaude_20260524_1529.md`
  - `选必一_当代国际政治与经济_主观题术语宝典_学生版_backup_before_appclaude_20260524_1529.docx`

## Structural Checks

- Markdown core answer-point headings: 138
- Markdown question examples: 351
- `【什么时候写】`: 351
- `【设问】`: 351
- `【卷面句】`: 351
- Old slash-merged economic globalization wording: 0
- DOCX opened with python-docx.
- DOCX `Heading 3` count: 351
- DOCX paragraphs: 3464
- DOCX tables: 1

## Render Check

`render_docx.py` was attempted at:

`rendered_student_docx_appclaude_20260524/render.log`

It failed because the local LibreOffice/soffice executable is unavailable (`FileNotFoundError`). Therefore this rebuild is structurally checked, but not visually PNG/PDF rendered.
