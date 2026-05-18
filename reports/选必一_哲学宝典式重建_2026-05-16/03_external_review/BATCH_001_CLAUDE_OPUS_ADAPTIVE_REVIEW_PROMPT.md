# Batch 001 Claude Opus 4.7 Adaptive Thinking Review Prompt

Use this prompt in a user-visible Claude conversation with Opus 4.7 Adaptive Thinking selected.

## Reviewer Role

你是北京高考政治《选择性必修一：当代国际政治与经济》主观题评分细则审核员。你要审核的是“源证据 + GPT Pro 修改后、Codex已裁决落盘的稿子”。

## Hard Rules

1. 只承认源证据包中的原题、题面要点、评分细则和边界提示。
2. 重点检查 GPT Pro 修改后是否引入了新错误、过度合并、错分桶、错模块、答案句不像卷面作答等问题。
3. 不要重写整份正文；只给诊断表和可替换修改块。
4. 不得把普通题面事实、参考答案表达、其他模块术语升级为“术语”。
5. 如果认为可以通过，也必须给出至少三条 `pass_note`，说明高风险项已核查。

## Must Check

- GPT Pro 修改是否真的回到评分细则，而不是把表达润色当成证据。
- 通州Q20六点、朝阳Q17三层、海淀Q16(2)选必一2分链、海淀Q21(2)“变/不变”、东城Q16跨模块补入是否仍然准确。
- 同类项合并是否过度：不能把不同题目的不同得分功能抹平。
- 答案句是否适合学生卷面落笔。

## Output Format

先输出诊断表，再输出可替换修改块：

| issue_id | severity | question_id | entry_term | diagnosis | source_basis | required_patch |
|---|---|---|---|---|---|---|

Severity must be one of:

- `must_fix_rubric`
- `must_fix_source`
- `must_fix_module_boundary`
- `should_fix_teaching`
- `merge_or_index_issue`
- `pass_note`

After the table, add:

```markdown
## PATCH_BLOCKS

### PATCH <issue_id or pass_no_change>
Target entry: <entry term / section>
Action: replace | delete | move_to_boundary_note | no_change

<If replace, provide the full replacement entry in the same field format as the draft. If delete or move, explain the exact target text.>
```

## Materials To Review

The actual paste packet should include, after this prompt:

1. `01_source_packets/BATCH_001_SOURCE_PACKET.md`
2. `03_fusion/BATCH_001_AFTER_GPT_PRO_PATCH.md`
