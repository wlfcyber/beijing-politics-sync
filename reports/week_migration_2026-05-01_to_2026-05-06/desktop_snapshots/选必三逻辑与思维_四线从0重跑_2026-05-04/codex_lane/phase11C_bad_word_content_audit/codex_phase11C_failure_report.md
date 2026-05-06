# Codex Phase11C Failure Report

## Verdict

`HARD_FAIL_BAD_WORD_CONTENT_GATE`

The bad Word/Markdown does not merely need polish. It fails the content standard the user wanted from the philosophy benchmark.

## Evidence

Generated matrix:

`codex_lane/phase11C_bad_word_content_audit/bad_word_four_element_failure_matrix_codex.csv`

Counts:

- 181 entries scanned.
- 101 entries have fake/template prompts such as `本题要求结合材料说明其体现的思维方法...`.
- 130 entries contain meta answer instructions such as `卷面要把...`, `先写...`, `要写...`, or generic choice-question process language.
- 0 entries passed the strict answer-sentence sufficiency heuristic, because the artifact usually gives instructions, labels, or trap summaries rather than a clean answer-sheet sentence.

## Main Failures

1. The four labels are present, but the four functions are not fulfilled.
2. `设问` frequently does not preserve the real prompt, so students cannot see the actual task they are answering.
3. `为什么能想到` often becomes a method list instead of a trigger chain.
4. `答案落点` often tells the writer what to do. It should tell the student what to write.
5. Multi-node mounting is mechanically duplicated. Same-question entries must be rewritten for each exact method node.
6. Choice-question entries do not consistently show all options, correct-option logic, tempting wrong-option logic, and trap type.
7. The artifact is much closer to an index than to a teaching document.

## Representative Bad Patterns

- `2024丰台一模 Q19(2)`: repeats across several nodes with the same broad method soup, instead of separating scientific thinking, analysis-synthesis, and发散聚合.
- `2025东城期末 Q18(2)`: answer landing says how to write, not what to write.
- `2026顺义一模 Q19(2)`: the stronger current Phase11A version is better than the bad Word because it at least maps 客观性 / 预见性 / 可检验性 to distinct material signals.
- `2026通州期末 Q11`: should be a choice-trap entry centered on `杂多现象 -> 抽出核心概念 -> 回到完整整体图景`; generic choice-process language is insufficient.

## Rebuild Rule

The next student Markdown must be rebuilt from locked evidence rows and source repair packets. It may use the bad Word only as a failure inventory, never as the base.

