# PHILOSOPHY_FORMAT_V5_PREFACE_AND_LEAK_PATCH_20260526

verdict: `PATCH_APPLIED_NOT_FINAL`

## Trigger

Claude Opus real review of the V4 external packet surfaced two credible alignment defects:

- V4 PDF page order placed `前言` on the same page as the cover title, while the philosophy benchmark PDF is `cover -> page 2 前言 -> page 3 目录`.
- 推理册正文 still contained the student-facing phrase `哲学宝典式的看法`, which is an internal alignment/editing trace and should not appear in the handbook.

Codex independently verified both points against the current PDF/Markdown before patching.

## Patch

- Updated `tools/build_handbook_docs.py` to insert a page break after the cover/title block, before emitting the preface.
- Shifted all manual TOC fallback page numbers by one page so the visible TOC remains stable after the new preface page.
- Rewrote the leaked 推理册 sentence from `哲学宝典式的看法是...` to the student-facing `判断时先看材料关系...`.
- Rebuilt both DOCX files and exported both PDFs through Microsoft Word.

## Current Evidence

- Benchmark philosophy PDF front matter:
  - page 1: title / subtitle / `飞哥正志讲堂`
  - page 2: `— 2 —` / `前言`
  - page 3: `— 3 —` / `目录`
- Current 思维 PDF front matter after patch:
  - page 1: title / subtitle / `飞哥正志讲堂`
  - page 2: `— 2 —` / `前言`
  - page 3: `— 3 —` / `目录`
- Current 推理 PDF front matter after patch:
  - page 1: title / subtitle / `飞哥正志讲堂`
  - page 2: `— 2 —` / `前言`
  - page 3: `— 3 —` / `目录`
- PDF text/backend scan after patch:
  - 思维册: 35 pages, forbidden/backend hits 0
  - 推理册: 51 pages, forbidden/backend hits 0
- DOCX XML scan after patch:
  - 思维册: `PAGEREF=19`, internal links 19, bookmarks 19, `哲学宝典=0`
  - 推理册: `PAGEREF=8`, internal links 8, bookmarks 8, `哲学宝典=0`

## Boundary

This patch addresses only the verified V4 front-matter and backend-leak defects. It does not close the full external review gate. Because the first Claude review was run on the pre-patch V4 external packet, the updated V5 files still require refreshed review status before any final claim.
