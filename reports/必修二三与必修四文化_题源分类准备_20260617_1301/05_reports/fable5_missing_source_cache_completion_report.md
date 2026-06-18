# Fable5 Missing Source Cache Completion

## Scope

- missing unique sha before completion: 23
- source rows represented in missing groups: 39
- cache rows after completion: 194
- unique sha after completion: 194

## Added Rows By Status

{'raw-extracted': 22, 'skipped-excluded': 1}

## Cache Status After Completion

{'raw-extracted': 44, 'cache-hit': 149, 'skipped-excluded': 1}

## Source Type Counts After Completion

{'paper': 71, 'module-classification': 7, 'rubric': 110, 'reference-answer': 1, 'marking-report': 5}

## OCR Repairs

- `5581e0237e861511...` 2026 西城一模 PDF paper: Apple Vision OCR.
- `54715a1e650d940e...` 2026 西城期末细则 PDF: Apple Vision OCR.

## Hard Exclusions

- 2026 石景山期末 remains `skipped-excluded`; it is visible in the cache ledger but is not an input source for the B2/B3/B4_CULTURE handoff.

## Bad Rows

- `empty-or-unsupported`: 0
