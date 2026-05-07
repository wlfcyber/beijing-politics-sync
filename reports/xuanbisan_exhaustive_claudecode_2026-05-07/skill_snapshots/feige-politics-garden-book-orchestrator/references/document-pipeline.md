# Simplified Document Pipeline

Use this reference when a full-book run must produce Markdown, DOCX, optional PDF, and visual/Word validation.

## 2026-05-02 Local Tool Findings

- Microsoft Word is available and scriptable: `com.microsoft.Word`, version `16.108.2`.
- Bundled Codex Python is available at `/Users/wanglifei/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.
- Useful bundled Python packages: `python-docx`, `lxml`, `Pillow`, `pypdf`, `reportlab`.
- System tools available: `textutil`, `qlmanage`, `mdls`.
- Not currently in `PATH`: `pandoc`, `libreoffice`, `soffice`, standalone `openai`.

## Simpler Default Route

Keep Markdown as the canonical content source and make DOCX a generated artifact. Do not manually repair content in Word unless the user explicitly wants hand edits.

1. Normalize Markdown first:
   - Chinese quote style: use `“”` for material quotations.
   - Choice-question options: one option per line for `①②③④`.
   - Student-facing fields only: no audit labels, paths, `参考答案`, `评标`, `pass`, `filled`, or pipeline notes.
   - Stable image references for comics, scans, tables, and charts.
2. Generate DOCX from the normalized Markdown using a scripted builder with fixed styles:
   - body font and heading ladder set once;
   - restrained blue only for high-level headings, not whole TOC;
   - automatic page numbers;
   - clickable TOC/bookmarks where feasible;
   - watermark added through header/shape or section background logic;
   - all images embedded, not linked to fragile local paths.
3. Run an OOXML post-process for deterministic fixes:
   - TOC style cleanup;
   - quote and option-line audit;
   - image relationship audit;
   - header/footer/page-number check;
   - watermark presence check;
   - title color and body-color consistency check.
4. Use Microsoft Word only as the final renderer/validator:
   - open the DOCX;
   - update fields/TOC where possible;
   - save once;
   - export PDF or inspect quicklook/Word screenshots when practical.
5. Re-run structural checks after Word saves the file. Word may rewrite XML, so final checks must read the saved file, not only the pre-Word file.

## Avoided Complexity

- Do not depend on `pandoc` unless it is explicitly installed and tested.
- Do not depend on LibreOffice rendering on this Mac unless `soffice` is installed or provided by the Codex documents runtime.
- Do not use repeated manual Word tweaks as the main workflow. Manual Word is for final inspection and rare cosmetic fixes after the scripted pipeline has already done the mechanical work.
- Do not let GPT or Claude rewrite the final DOCX directly. They may advise on style, but Codex should apply deterministic transformations.

## Required Document Checks

Before final delivery, confirm:

- `rg` or equivalent text extraction finds zero forbidden audit terms in the student-facing document.
- Every choice question has four visible options when the source question has four options.
- Every `①②③④` option is split onto its own line in both Markdown and DOCX.
- Comic/image questions have embedded images and captions or nearby question text that make the image boundary clear.
- TOC is not globally blue; only intended headings use the accent color.
- Page numbers exist after Word save.
- Watermark is visible enough to deter casual removal but light enough not to interfere with reading.
- Final DOCX has been opened and saved in Microsoft Word when Word is available.

## Preferred Automation Shape

Create one small run-local script per book run, usually under `tools/document_pipeline/`, with these stages:

- `normalize_markdown.py`
- `build_docx.py`
- `postprocess_docx.py`
- `word_validate.applescript`
- `audit_docx.py`

Keep each script idempotent. The user should be able to run the whole document build again without changing the student-facing content.
