# Atom Mapping Patch Queue

- generated_at: 2026-05-19T15:05:00+08:00
- purpose: block final framework/handbook closure until misbound atoms and split records are corrected.
- status note: CC0229 is closed; CC0305/CC0373/CC0380 split patch records exist but still need canonical integration and final document regeneration.

## P0 `CC0229_2026_东城_一模_18`

- issue_type: bad_rubric_atom_mapping
- problem: Current rubric atoms include logic/economy/ecology fragments. Correct scoring exists in F0153 page 8 and F0146 slides 3-4.
- required_action: DONE: replaced bad R_CC0229 rows from F0153/F0146 and regenerated CC0229 handbook section; keep backup files for audit.
- source_locator: F0153:page 7-8 | F0146:slide 3-4
- status: closed_patched_atoms_and_baodian_section_20260519

## P0 `CC0094_2025_东城_期末_19_3`

- issue_type: split_required_bad_atoms
- problem: Whole small question is law+politics mixed, and current atoms point to新能源/欧盟/贸易保护.
- required_action: Create split legal-only pending unit for the 2-point adjacent-relation/legal layer; keep politics/democratic-procedure layer out of law framework.
- source_locator: F0129:slide 14
- status: open

## P1 `CC0305_2026_海淀_一模_18_3`

- issue_type: split_material_atoms_needed
- problem: Q18(3) legal scoring is clear, but parent question contains economic subquestions.
- required_action: DONE for patch records: split question/material/ask/rubric atom records created under 10_framework_validation; still integrate into canonical merged files and regenerate final handbook/docx.
- source_locator: F0165:lines 87-96
- status: patch_records_created_final_integration_pending

## P1 `CC0373_2026_顺义_一模_18`

- issue_type: canonical_id_and_atoms_needed
- problem: Original row was Q17 politics; Q18 labor-law scoring appears later.
- required_action: DONE for patch records: split question/material/ask/rubric atom records created under 10_framework_validation; still integrate into canonical merged files and regenerate final handbook/docx.
- source_locator: F0177:lines 302-327 | F0176:lines 35-47
- status: patch_records_created_final_integration_pending

## P1 `CC0380_2026_顺义_二模_18_2`

- issue_type: split_open_atoms_needed
- problem: Whole row atoms only captured logic part; legal subquestion has formal but mixed-module scoring.
- required_action: DONE for patch records: split question/material/ask/rubric atom records created under 10_framework_validation; still integrate into canonical merged files and regenerate final handbook/docx.
- source_locator: F0202:lines 53-55
- status: patch_records_created_final_integration_pending

## P1 `CC0259_2026_丰台_期中_19_LAW`

- issue_type: missing_legal_rubric
- problem: Question text appears to be遗赠扶养协议 but rubric atoms are unrelated.
- required_action: Re-source answer/评标; if no legal rubric found, keep missing and out of framework/handbook closure.
- source_locator: F0207:page 33
- status: open

## P2 `CC0118_2025_丰台_期末_18_2_LAW`

- issue_type: duplicate_or_reextract
- problem: Current row is economy; legal feedback may duplicate CC0119.
- required_action: Check if 尹某 labor-contract小问 is already represented by CC0119; avoid duplicate count.
- source_locator: F0131:slides 45-52 | F0132:pages 16-17
- status: open

