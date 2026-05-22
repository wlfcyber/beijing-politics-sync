# Cowork Patch Apply Audit

Generated: 2026-05-19T16:58:32

Verdict: **PASS**

## Counts

- questions: 65
- material_atoms: 482
- ask_atoms: 65
- rubric_atoms: 350
- evidence_level: {'formal': 61, 'reference_only': 4}

## Hard Blocker Checks

- empty_asks: 0 []
- material_equals_rubric: 0 []
- broken_rubric_material_refs_count: 0
- logic_rubric_leaks: 0 []

## Remaining Review-Only Flags

- material_contains_answer_or_scoring_tokens_review: 0 []

These review-only flags are expected when the original material itself contains score text such as `8分`, or where weak reference-only rows remain. They are not automatic blockers after manual source recovery unless listed above.

## Applied Patch Summary

- CC0019_2024_朝阳_一模_19 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0015:paper page 7 lines 249-265; rendered/text source recovered after Cowork.)
- CC0092_2025_东城_期末_19_1 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0130:paper page 6 lines 199-227.)
- CC0131_2025_房山_一模_19 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0081:paper page 6 lines 227-236.)
- CC0180_2025_海淀_期末_20 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0139:paper text around Q20 and attached table.)
- CC0195_2025_西城_一模_20 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0094:paper page 7 lines 276-283.)
- CC0214_2025_门头沟_一模_20_2 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0096:paper pages 7-8 lines 305-344.)
- CC0245_2026_东城_期末_18_2 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0206:paper page 6 lines 234-241.)
- CC0276_2026_房山_二模_17 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0191:rendered paper page 6.)
- CC0277_2026_房山_二模_18 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0191:rendered paper page 7.)
- CC0317_2026_海淀_期末_18 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0217:rendered paper page 6.)
- CC0318_2026_海淀_期末_18_2 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0217:rendered paper page 6.)
- CC0319_2026_海淀_期末_19 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0217:rendered paper page 7.)
- CC0353_2026_西城_期末_17 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0221/F0399:rendered paper page 6; answer reference page 11.)
- CC0011_2024_丰台_二模_17 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0048:rendered paper page 5; F0047/F0270:rubric text.)
- CC0119_2025_丰台_期末_19 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0132:paper page 7 lines 255-280; F0131:rubric slides 45-47.)
- CC0251_2026_丰台_一模_20 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0157:rendered paper page 9; F0156:rubric slide 51.)
- CC0254_2026_丰台_二模_18 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0188:paper page 7 lines 308-336; F0187:rubric slides 29-34.)
- CC0283_2026_朝阳_一模_18 [question_row]: rebuilt full_question_text/material_text/ask_text from paper source (F0163:paper page 6 lines 269-295; F0162/F0373:rubric text.)
- CC0077_2025_东城_一模_19 [question_row]: filled ask_text (F0073:page 4 | F0074:page 5 | F0074:page 8 | F0292:page 4)
- CC0084_2025_东城_二模_19 [question_row]: filled ask_text (F0100:page 3 | F0101:page 5 | F0101:page 7 | F0317:page 3)
- CC0157_2025_朝阳_期末_20 [question_row]: filled ask_text (F0135:page 6 | F0135:page 9 | F0133:slides around Q20; F0343:teacher answer Q20)
- CC0189_2025_石景山_一模_20 [question_row]: filled ask_text (F0091:text | F0092:page 11 | F0092:page 8 | F0309:text)
- CC0213_2025_门头沟_一模_20 [question_row]: filled ask_text (F0096:page 10 | F0096:page 7 | F0095:text lines 38-55; F0096:text Q20)
- CC0325_2026_石景山_一模_18 [question_row]: filled ask_text (F0167:text | F0168:page 6 | F0168:page 9 | F0377:text)
- CC0019_2024_朝阳_一模_19 [material_atoms]: replaced old atoms with 7 source-material atoms (F0015:paper page 7 lines 249-265; rendered/text source recovered after Cowork.)
- CC0092_2025_东城_期末_19_1 [material_atoms]: replaced old atoms with 5 source-material atoms (F0130:paper page 6 lines 199-227.)
- CC0131_2025_房山_一模_19 [material_atoms]: replaced old atoms with 4 source-material atoms (F0081:paper page 6 lines 227-236.)
- CC0180_2025_海淀_期末_20 [material_atoms]: replaced old atoms with 4 source-material atoms (F0139:paper text around Q20 and attached table.)
- CC0195_2025_西城_一模_20 [material_atoms]: replaced old atoms with 3 source-material atoms (F0094:paper page 7 lines 276-283.)
- CC0214_2025_门头沟_一模_20_2 [material_atoms]: replaced old atoms with 14 source-material atoms (F0096:paper pages 7-8 lines 305-344.)
- CC0245_2026_东城_期末_18_2 [material_atoms]: replaced old atoms with 5 source-material atoms (F0206:paper page 6 lines 234-241.)
- CC0276_2026_房山_二模_17 [material_atoms]: replaced old atoms with 5 source-material atoms (F0191:rendered paper page 6.)
- CC0277_2026_房山_二模_18 [material_atoms]: replaced old atoms with 4 source-material atoms (F0191:rendered paper page 7.)
- CC0317_2026_海淀_期末_18 [material_atoms]: replaced old atoms with 4 source-material atoms (F0217:rendered paper page 6.)
- CC0318_2026_海淀_期末_18_2 [material_atoms]: replaced old atoms with 3 source-material atoms (F0217:rendered paper page 6.)
- CC0319_2026_海淀_期末_19 [material_atoms]: replaced old atoms with 7 source-material atoms (F0217:rendered paper page 7.)
- CC0353_2026_西城_期末_17 [material_atoms]: replaced old atoms with 5 source-material atoms (F0221/F0399:rendered paper page 6; answer reference page 11.)
- CC0011_2024_丰台_二模_17 [material_atoms]: replaced old atoms with 6 source-material atoms (F0048:rendered paper page 5; F0047/F0270:rubric text.)
- CC0119_2025_丰台_期末_19 [material_atoms]: replaced old atoms with 9 source-material atoms (F0132:paper page 7 lines 255-280; F0131:rubric slides 45-47.)
- CC0251_2026_丰台_一模_20 [material_atoms]: replaced old atoms with 7 source-material atoms (F0157:rendered paper page 9; F0156:rubric slide 51.)
- CC0254_2026_丰台_二模_18 [material_atoms]: replaced old atoms with 11 source-material atoms (F0188:paper page 7 lines 308-336; F0187:rubric slides 29-34.)
- CC0283_2026_朝阳_一模_18 [material_atoms]: replaced old atoms with 5 source-material atoms (F0163:paper page 6 lines 269-295; F0162/F0373:rubric text.)
- CC0092_2025_东城_期末_19_1 [ask_atom]: rewrote ask atom from repaired ask_text (F0130:paper page 6 lines 199-227.)
- CC0254_2026_丰台_二模_18 [ask_atom]: rewrote ask atom from repaired ask_text (F0188:paper page 7 lines 308-336; F0187:rubric slides 29-34.)
- CC0213_2025_门头沟_一模_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0096:page 10 | F0096:page 7 | F0095:text lines 38-55; F0096:text Q20)
- CC0283_2026_朝阳_一模_18 [ask_atom]: rewrote ask atom from repaired ask_text (F0163:paper page 6 lines 269-295; F0162/F0373:rubric text.)
- CC0319_2026_海淀_期末_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0217:rendered paper page 7.)
- CC0353_2026_西城_期末_17 [ask_atom]: rewrote ask atom from repaired ask_text (F0221/F0399:rendered paper page 6; answer reference page 11.)
- CC0251_2026_丰台_一模_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0157:rendered paper page 9; F0156:rubric slide 51.)
- CC0318_2026_海淀_期末_18_2 [ask_atom]: rewrote ask atom from repaired ask_text (F0217:rendered paper page 6.)
- CC0189_2025_石景山_一模_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0091:text | F0092:page 11 | F0092:page 8 | F0309:text)
- CC0131_2025_房山_一模_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0081:paper page 6 lines 227-236.)
- CC0195_2025_西城_一模_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0094:paper page 7 lines 276-283.)
- CC0011_2024_丰台_二模_17 [ask_atom]: rewrote ask atom from repaired ask_text (F0048:rendered paper page 5; F0047/F0270:rubric text.)
- CC0119_2025_丰台_期末_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0132:paper page 7 lines 255-280; F0131:rubric slides 45-47.)
- CC0077_2025_东城_一模_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0073:page 4 | F0074:page 5 | F0074:page 8 | F0292:page 4)
- CC0019_2024_朝阳_一模_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0015:paper page 7 lines 249-265; rendered/text source recovered after Cowork.)
- CC0084_2025_东城_二模_19 [ask_atom]: rewrote ask atom from repaired ask_text (F0100:page 3 | F0101:page 5 | F0101:page 7 | F0317:page 3)
- CC0214_2025_门头沟_一模_20_2 [ask_atom]: rewrote ask atom from repaired ask_text (F0096:paper pages 7-8 lines 305-344.)
- CC0157_2025_朝阳_期末_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0135:page 6 | F0135:page 9 | F0133:slides around Q20; F0343:teacher answer Q20)
- CC0276_2026_房山_二模_17 [ask_atom]: rewrote ask atom from repaired ask_text (F0191:rendered paper page 6.)
- CC0317_2026_海淀_期末_18 [ask_atom]: rewrote ask atom from repaired ask_text (F0217:rendered paper page 6.)
- CC0245_2026_东城_期末_18_2 [ask_atom]: rewrote ask atom from repaired ask_text (F0206:paper page 6 lines 234-241.)
- CC0180_2025_海淀_期末_20 [ask_atom]: rewrote ask atom from repaired ask_text (F0139:paper text around Q20 and attached table.)
- CC0325_2026_石景山_一模_18 [ask_atom]: rewrote ask atom from repaired ask_text (F0167:text | F0168:page 6 | F0168:page 9 | F0377:text)
- CC0277_2026_房山_二模_18 [ask_atom]: rewrote ask atom from repaired ask_text (F0191:rendered paper page 7.)
- CC0254_2026_丰台_二模_18 [rubric_atom]: removed stray non-source-review atom R_CC0254_2026_丰台_二模_18_09 (F0187:slide 29)
- CC0277_2026_房山_二模_18 [rubric_atom]: removed R_CC0277_2026_房山_二模_18_08 (F0189:text | F0190:text | F0191:page 10)
- CC0277_2026_房山_二模_18 [rubric_atom]: removed R_CC0277_2026_房山_二模_18_09 (F0189:text | F0190:text | F0191:page 10)
- CC0277_2026_房山_二模_18 [rubric_atom]: removed R_CC0277_2026_房山_二模_18_10 (F0189:text | F0190:text | F0191:page 10)
- CC0277_2026_房山_二模_18 [rubric_atom]: removed R_CC0277_2026_房山_二模_18_11 (F0189:text | F0190:text | F0191:page 10)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_02 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_03 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_04 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_05 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_06 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_07 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [rubric_atom]: removed R_CC0364_2026_通州_期末_19_1_08 (F0223:slide 11 | F0403:slide 11)
- CC0364_2026_通州_期末_19_1 [question/material/ask/rubric]: restored 19(1) law ask and removed 19(2) logic rubric atoms (F0224:paper page 7 lines 236-251; F0223/F0403:rubric slide 11.)
