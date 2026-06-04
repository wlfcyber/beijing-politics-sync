# DOCX_STYLE_CONSISTENCY_AUDIT_20260525

Status: `PASS`
Updated: 2026-05-26 02:27:16 +08

## Scope

- DOCX bytes: `476243`.
- PDF bytes: `4693630`.
- Question entries audited: `721`.
- Entries matched to insertion ledger: `415`.
- Legacy or inherited entries: `306`.
- Unique ledger headings: `158`.

## Structural Style Checks

- Heading paragraph property variants: `1`.
- Heading run property variants: `1`.
- Inserted heading pPr/rPr variants: `1`/`1`.
- Legacy heading pPr/rPr variants: `1`/`1`.
- Missing label blocks: `0`.
- Duplicate label blocks: `0`.
- Ledger headings missing from current DOCX: `0`.

## Label Style Variants

- `【材料触发点】` first-run style variants: `1`; count: `721`.
- `【设问】` first-run style variants: `1`; count: `721`.
- `【为什么能想到】` first-run style variants: `1`; count: `721`.
- `【答案落点】` first-run style variants: `1`; count: `721`.

## Render Cross-Check

- Latest retained render: `309/309 pages, labels 2890/2890, blank-like pages 0`.

## Boundary

- This audit proves structural heading/label style consistency inside the DOCX and checks it against the latest retained PDF render manifest.
- It does not replace full every-page human visual review or the required GPTPro/Claude Opus external content-thickness review.
