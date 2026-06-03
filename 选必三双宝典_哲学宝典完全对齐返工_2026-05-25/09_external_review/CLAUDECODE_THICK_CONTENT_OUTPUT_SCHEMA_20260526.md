# CLAUDECODE_THICK_CONTENT_OUTPUT_SCHEMA_20260526

status: `prepared_not_run`

## 1. JSONL Entry Schema

每一行是一个 JSON object。字段名保持英文，字段值用中文。

### thinking_main.jsonl

```json
{
  "entry_id": "T-YYYY-DISTRICT-STAGE-Q",
  "decision": "body",
  "evidence_level": "A-formal",
  "source_suite": "2026顺义一模",
  "question_id": "Q19(2)",
  "framework_type": "科学思维",
  "framework_node": "客观性",
  "full_prompt": "真实设问原句",
  "material_trigger": "学生能圈出的材料动作或关系",
  "why_this_method": "材料动作为什么触发这个小方法",
  "answer_landing": "思维方法/术语 + 本题事实 + 因果/作用/结论",
  "common_trap": "本节点易误判点",
  "same_type_notes": "可选：同类题提示",
  "source_lock": "题面/答案/细则/页图位置",
  "audit_note": "只放审计版，不进学生正文"
}
```

### reasoning_main.jsonl

```json
{
  "entry_id": "RM-YYYY-DISTRICT-STAGE-Q",
  "decision": "body",
  "evidence_level": "A-formal",
  "source_suite": "2024朝阳一模",
  "question_id": "Q20(1)",
  "reasoning_family": "充分条件假言推理",
  "logical_form": "如果 p 那么 q；肯定前件推出肯定后件",
  "valid_or_invalid_form": "有效式",
  "full_prompt": "真实设问原句",
  "material_trigger": "题干怎样组织前提和结论",
  "why_this_form": "为什么判为此推理形式",
  "answer_landing": "可直接写出的卷面理由",
  "common_trap": "易错式或误判原因",
  "source_lock": "题面/答案/细则/页图位置",
  "audit_note": "只放审计版，不进学生正文"
}
```

### reasoning_choice.jsonl

```json
{
  "entry_id": "RC-YYYY-DISTRICT-STAGE-Q",
  "decision": "body",
  "evidence_level": "B-choice-signal",
  "source_suite": "2025顺义一模",
  "question_id": "Q7",
  "reasoning_family": "三段论结构题与谬误题",
  "question_stem": "完整题干",
  "options": {
    "A": "完整选项 A",
    "B": "完整选项 B",
    "C": "完整选项 C",
    "D": "完整选项 D"
  },
  "answer": "正确选项",
  "correct_reason": "正确项为什么成立",
  "tempting_wrong_options": {
    "A": "为什么诱人，为什么错",
    "B": "为什么诱人，为什么错",
    "C": "为什么诱人，为什么错"
  },
  "logical_form": "若适用，写出形式或错误式",
  "trap_type": "大项不当扩大/小项不当扩大误称/中项不周延等",
  "source_lock": "题面/答案表/页图位置",
  "audit_note": "只放审计版，不进学生正文"
}
```

## 2. Coverage Matrix Fields

`claudecode_lane/COVERAGE_MATRIX.csv` 至少包含：

```csv
coverage_id,source_suite,question_id,question_type,module_decision,handbook_target,decision,evidence_level,framework_node_or_reasoning_family,source_lock,blocked_reason,fusion_priority
```

`decision` 只能是：

- `body`
- `index`
- `blocked`
- `excluded`

`handbook_target` 只能是：

- `thinking_main`
- `reasoning_main`
- `reasoning_choice`
- `excluded_or_boundary`

## 3. Framework Node Matrix Fields

`claudecode_lane/framework_node_matrix.csv` 至少包含：

```csv
node_id,book,framework_parent,framework_node,required_status,body_count,index_count,blocked_count,representative_entries,hard_sample_status,notes
```

`required_status` 只能是：

- `covered`
- `covered_by_support`
- `blocked_no_source`
- `blocked_no_question`
- `blocked_boundary`
- `not_found_in_current_source_pool`

## 4. Suite Report Template

每个 `suite_reports/*.md` 至少包含：

```markdown
# <suite name>

- status:
- source files:
- question candidates:
- body entries:
- index entries:
- blocked:
- excluded:

## Decisions

| Question | Target | Decision | Evidence | Reason |
| --- | --- | --- | --- | --- |

## Thick Content Notes

本套卷比 Codex 现有稿可补厚的地方：

## Blockers

必须写清缺哪一类证据，以及下一步怎么补。
```

## 5. Fusion Candidates

`claudecode_lane/fusion_candidates.md` 必须按以下类别组织：

- `replace_codex_thin_entry`
- `append_missing_material_trigger`
- `append_missing_answer_landing`
- `append_choice_wrong_option_reason`
- `add_framework_node_mount`
- `keep_as_index`
- `reject_or_block`

每条都要写：

- ClaudeCode entry id；
- Codex 对应条目或缺口；
- 建议动作；
- 证据理由；
- 学生版清洗注意事项。
