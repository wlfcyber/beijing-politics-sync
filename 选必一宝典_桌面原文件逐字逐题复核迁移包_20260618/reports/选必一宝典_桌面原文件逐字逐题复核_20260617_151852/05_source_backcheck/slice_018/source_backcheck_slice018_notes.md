# Slice 018 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 86-90 only
- backcheck_time: 2026-06-17T20:20:17+08:00

## Overall Finding

Slice 018 has local source evidence for all five entries. Q0086 is content-pass at this slice angle with source-field repair still needed. Q0087-Q0090 need field repairs before student-facing use:

- Q0087 must reconcile the 8-point short-essay scoring display and stop presenting `推进贸易自由化便利化` as the whole short essay's main axis.
- Q0088 must correct the original `五个共同` wording; `共同推进贸易投资自由化便利化` is not one of the five headings, and `共同促进区域繁荣` is not the source wording.
- Q0089 must remove a copied/template trigger chain and record that the original prompt uses 《经济与社会》, not 《当代国际政治与经济》.
- Q0090 must restore two omitted effect points from the reference answer: `提高资源配置效率` and `推动全球供应链高质量发展`.

## Q0086 doc_order=86

- desktop blocks: 1022-1030
- question: 2025西城二模Q19(2)
- source evidence:
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-224` confirms the zero-tariff material and prompt.
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:303-306` confirms the teacher-answer summary.
  - `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-71` confirms the 3-point China-responsibility layer and 2-point world-significance layer.

Codex judgment:

- `术语/核心采分点`: PASS. The row's trade-facilitation slice is supported by the world-significance line `促进贸易自由化`; however `投资` should be weakened if the text is later repaired because the source is a zero-tariff/trade case.
- `完整设问`: PASS.
- `细则位置`: PASS. Blocks 1028-1030 preserve the 3 + 2 scoring structure.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry still lacks formal source identity.
- `材料触发`: PASS, with tightening suggestion: do not let lower trade cost replace the 3-point `共享发展新机遇、惠民生增福祉、互利共赢` China-responsibility layer in a whole-answer version.
- `答案句`: PASS as this slice's trade-facilitation answer sentence, while a full-answer repair should add the 2-point shared-opportunity layer.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0020 still needs group-level reconciliation.
- `模块边界`: PASS.

## Q0087 doc_order=87

- desktop blocks: 1031-1041
- question: 2025东城期末Q20
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:192-201` confirms the NEV anti-subsidy-tax material and short-essay prompt.
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:645-657` confirms the teacher-answer angle list.
  - `SRC_RUBRIC_2025_DONGCHENG_QIMO_Q20_PDF.txt:127-142` confirms the title/paragraph/scoring layers and the `推动贸易自由便利` attitude/doings option.

Codex judgment:

- `术语/核心采分点`: PASS. `推动贸易自由便利` appears as a source-backed third-layer attitude/doings option at line 141.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. The desktop keeps `本题8分` but lists sublayers that add to 10 unless the source's display inconsistency is explicitly capped or reconciled.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: NEEDS_FIX. Blocks 1032 and 1034 mix the `维护本国利益` trigger and a generic cross-border-flow template with a trade-facilitation core; the term is only one option in the third layer, not the whole short essay.
- `答案句`: PASS as a slice answer sentence, with the caution that it cannot stand in for the full short essay.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0014 still needs group-level reconciliation.
- `模块边界`: PASS.

## Q0088 doc_order=88

- desktop blocks: 1042-1054
- question: 2026石景山一模Q20
- source evidence:
  - `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:232-247` confirms the APEC `五个共同` material and prompt.
  - `SRC_EXAM_2026_SHIJINGSHAN_YIMO_Q20.txt:311-328` confirms teacher-answer examples for `共同/开放/包容`.
  - `SRC_RUBRIC_2026_SHIJINGSHAN_YIMO_Q20.txt:49-69` confirms the level/keyword scoring and examples.

Codex judgment:

- `术语/核心采分点`: PASS. Trade/investment facilitation is explicitly present under the `开放` angle at source lines 238, 315 and 324.
- `完整设问`: PASS. The desktop prompt is compressed but keeps the task core.
- `细则位置`: PASS. The same-group notes preserve the 1-keyword/2-keyword level scoring.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: NEEDS_FIX. The desktop misnames the second `共同` heading and invents `共同促进区域繁荣`; the source says `共同营造开放型区域经济环境` and `共同促进普惠包容发展`.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0012 still needs group-level reconciliation.
- `模块边界`: PASS.

## Q0089 doc_order=89

- desktop blocks: 1055-1064
- question: 2025西城一模Q18
- source evidence:
  - `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt:221-234` confirms the `两条鱼循环` material and 《经济与社会》 prompt.
  - `SRC_EXAM_2025_XICHENG_YIMO_Q18.txt:342-345` confirms the answer summary.
  - `SRC_RUBRIC_2025_XICHENG_YIMO_Q18.txt:65-78` confirms the 7-point 产业优势/物质条件/市场 rubric and no-credit warnings.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source supports `贸易便利化` as a 1-point material-condition phrase, but not the full 选必一-style `推进贸易和投资自由化便利化` core.
- `完整设问`: PASS.
- `细则位置`: PASS. The three-layer 7-point structure is accurately preserved.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: NEEDS_FIX. Blocks 1056 and 1058 misstate the prompt and import unsupported facts (`通关、准入、协议、人员往来`).
- `答案句`: PASS. Block 1059 maps to the source's material-condition layer.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0038 still needs group-level reconciliation.
- `模块边界`: NEEDS_FIX. The original prompt explicitly uses 《经济与社会》, so this row cannot be treated as a clean 选必一主链 item without a boundary note.

## Q0090 doc_order=90

- desktop blocks: 1067-1076
- question: 2024丰台一模Q20
- source evidence:
  - `SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt:242-253` confirms the supply-chain expo material and prompt.
  - `SRC_EXAM_2024_FENGTAI_YIMO_Q20.txt:369-373` confirms the reference answer.
  - `SRC_RUBRIC_2024_FENGTAI_YIMO_Q20.txt:110-116` confirms the formal rubric and level rule.

Codex judgment:

- `术语/核心采分点`: PASS. `打造国际经济合作交流平台，推进贸易投资自由化便利化` is source-backed.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Block 1076 omits `提高资源配置效率` and `推动全球供应链高质量发展` while summarizing the source answer aspects.
- `来源`: NEEDS_FIX. The desktop entry still lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL. UQ0061 still needs group-level reconciliation.
- `模块边界`: PASS.
