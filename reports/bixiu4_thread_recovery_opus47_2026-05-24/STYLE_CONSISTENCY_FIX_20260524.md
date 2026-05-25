# STYLE_CONSISTENCY_FIX_20260524

Status: `INSERTED_LABEL_STYLE_FIXED_AND_RERENDERED`

Timestamp: 2026-05-24 23:33 +08

## Problem Found

The reported visible mismatch was real. XML inspection showed:

- Existing body entries: label runs such as `【材料触发点】`, `【设问】`, `【为什么能想到】`, `【答案落点】` are bold, color `21574C`, with paragraph spacing after `80`.
- Newly inserted 36 entries: the same four label paragraphs were plain Normal runs with no label split, no bold green label, and no paragraph spacing after.

This affected 36 inserted entries x 4 label paragraphs = 144 student-facing paragraphs.

## Fix Applied

Script: `fix_inserted_label_styles_20260524.py`

Actions:

- Preserved DOCX backups before patching.
- Rebuilt only the inserted label paragraphs.
- Split each paragraph into:
  - label run: bold, color `21574C`
  - body run: normal inherited body text
- Set paragraph spacing after to `80`.
- Preserved existing heading style `5`; no content judgment or evidence level was changed by the style fix.

Initial implementation note: a first XML rewrite used a library that changed Word namespace prefixes and Word rejected the DOCX. That file was restored from the automatic backup, and the patch script was revised to preserve the original Word namespace map. The final DOCX opens through Word export and rendered successfully.

## Verification

| check | result |
|---|---|
| Inserted headings found | 36 / 36 |
| Inserted label paragraphs checked | 144 |
| Label style failures after final rerender | 0 |
| Current DOCX size | 348,234 bytes |
| Current PDF size | 3,489,735 bytes |
| Current PDF pages | 235 |
| Rendered page PNGs | 235 pages + contact sheet |
| Student-facing residue terms | 0 hits in DOCX/PDF for `评标`, `NEED_EVIDENCE`, `source_lane`, `correct_option_chain`, `参考答案`, `答案写`, `可从`, `/Users/`, `source_repair_basis` |
| Blank-like pages | only `page_002.png`, the sparse foreword page |
| Visual samples | contact sheet, pages 7, 13, 121, and 235 |

## Boundary

This closes the specific new-vs-old inserted label style mismatch found in XML and visible on rendered pages. It does not claim a full manual every-page typography audit or strict final acceptance.
