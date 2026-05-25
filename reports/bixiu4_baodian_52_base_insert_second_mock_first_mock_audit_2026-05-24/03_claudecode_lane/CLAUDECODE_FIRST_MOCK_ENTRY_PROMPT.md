# ClaudeCode B 补跑：一模疑似遗漏转成可插入学生版条目

你已经完成本轮 `claudecode_b_coverage_matrix.csv` 和 `claudecode_b_first_mock_omissions.md`。现在只做一个窄任务：把其中“强细则候选/疑似遗漏”的 2024-2026 一模哲学题，转成可进入最终宝典的厚内容候选 JSONL。

## 只读材料

- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_b_first_mock_omissions.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_b_coverage_matrix.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/`
- 母版文本：`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/accepted_base_docx_text.txt`

## 输出文件

只写入：

`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/claudecode_b_first_mock_insert_candidates.jsonl`

每行一个“题目 x 原理节点”。字段必须是：

```json
{
  "source_suite": "",
  "question_no": "",
  "framework_node": "",
  "material_trigger": "",
  "question_prompt": "",
  "why_trigger": "",
  "answer_landing": "",
  "evidence_level": "",
  "boundary_note": ""
}
```

## 质量要求

- 必须像原宝典一样厚，不能只写一句空泛话。
- `material_trigger` 要写清楚材料中什么情境/动作/关系触发该原理。
- `why_trigger` 要解释“学生为什么能从材料想到这个原理”，不能说“细则提到”。
- `answer_landing` 要是学生能写进答案的自然答题句。
- 一题多原理要拆成多行，尤其：主要矛盾/次要矛盾、矛盾主要方面/次要方面、两点论重点论/主流支流、量变质变、辩证否定、上层建筑适合经济基础等。
- 如果只是选必三边界、普通参考答案弱证据、或题干/细则缺失，不要生成正文条目，只能跳过。
- 不要生成 Word，不要改母版。
