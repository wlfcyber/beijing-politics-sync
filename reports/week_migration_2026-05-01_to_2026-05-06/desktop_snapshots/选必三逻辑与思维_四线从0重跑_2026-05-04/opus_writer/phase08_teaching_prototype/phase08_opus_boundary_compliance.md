# Phase08 Opus Boundary Compliance (REVIEW ONLY)

- compliance_time: 2026-05-05 CST
- prototype_status: review_only
- student_permission: no
- word_pdf_permission: no
- final_pass_permission: no
- input_freeze_rows: 29
- hold_rows_excluded: 45
- L0_rows_excluded: 288

## 1. 文件存在自检

| 路径 | 必备 | 实际 |
|---|---|---|
| `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md` | yes | created |
| `07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv` | yes | created |
| `07_student_prototype/phase08_opus_change_log.md` | yes | created |
| `07_student_prototype/phase08_opus_change_log.csv` | yes | created |
| `opus_writer/phase08_teaching_prototype/phase08_opus_boundary_compliance.md` | yes | this file |
| `opus_writer/phase08_teaching_prototype/progress.md` | yes | being written |

不创建以下文件:
- 任何 Word/`.docx`、PDF、`outputs/`。
- 任何最终学生稿、最终 PASS 稿、宝典成品稿。
- 任何对 Phase07 输入的修改。

## 2. 行数自检

- 输入冻结行 (`05_coverage/phase08_opus_prototype_input_freeze.csv`):29 行(含表头实际 30 行)。
- 教学原型 CSV:29 行数据,7 列。
- 改动日志 CSV:29 行数据,10 列。
- 教学原型 Markdown:29 个 `### Q-...` 单题块。
- 模块分布:思维 13 / 推理 11 / 交叉 5。匹配冻结。
- 状态分布:L4 = 4(`Q-2025海淀二模-20`、`Q-2025西城二模-16-2`、`Q-2025西城二模-16-3`、`Q-2026丰台一模-18-2`),L3 = 25。匹配冻结。

(自检命令:
- `python3 -c "import csv; print(sum(1 for _ in csv.DictReader(open('phase08_opus_teaching_prototype_REVIEW_ONLY.csv', encoding='utf-8-sig'))))"` → 29
- `python3 -c "import csv; print(sum(1 for _ in csv.DictReader(open('phase08_opus_change_log.csv', encoding='utf-8-sig'))))"` → 29
- `grep -c '^### Q-' phase08_opus_teaching_prototype_REVIEW_ONLY.md` → 29 )

## 3. no-hold / no-L0 自检

- hold 行(`hold_answer_locator_risk = 25` + `hold_reasoning_form_risk = 20` 合计 45 行):全部不在 prototype 正文中出现。
- L0 行(288 行):全部不在 prototype 正文中出现。
- prototype 正文每一题的 question_id 均严格属于冻结 29 行。
- 同类题列表中可能出现的 hold / L0 ID(如 Q-2026顺义一模-3、Q-2024西城一模-11、Q-2025海淀二模-12 等)只作为 ID 引用,未展开任何答案/类型/挂载结论。

## 4. no-student / no-Word / no-PDF / no-final 自检

- 文件名与目录:不写入 `outputs/`,不写入 `07_student_doc/` 学生定稿目录,不写 `*.docx` / `*.pdf`。
- 文件头:`prototype_status: review_only`,`student_permission: no`,`word_pdf_permission: no`,`final_pass_permission: no`。
- 文中标注:阅读说明开头明确"本文件是 review-only 教学原型,不是学生稿,不是最终稿,不是 Word/PDF,不是宝典成品"。
- 不输出最终 PASS 语言;同类题不展开他题答案/类型;原型不进入交付通道。

## 5. 硬样本自检

- `Q-2024西城一模-11`(corrected pairing `B=①③`):
  - 不在冻结 29 行中,不进入正文。
  - 仅作为 `Q-2024朝阳期中-9` 的同类题 ID 出现。
  - 未在原型中陈述任何配对结论;旧的错误配对未作为正确结果出现。
- `Q-2025海淀二模-12`(answer = D):
  - 不在冻结 29 行中,不进入正文。
  - 仅作为 `Q-2025丰台期末-7` 的同类题 ID 出现。
  - 未在原型中陈述任何答案;答案 D 与定位限制不解耦。
- `Q-2025海淀二模-13`(answer = C):
  - 不在冻结 29 行中,不进入正文。
  - 不在任何同类题列表中出现。
  - 答案 C 与定位限制不解耦。
- `Q-2026顺义一模-3`(must not enter reasoning prototype):
  - 不在冻结 29 行中,不进入推理原型正文。
  - 仅作为思维同类题 ID 出现于 `Q-2025海淀二模-20`、`Q-2026朝阳期中-20`、`Q-2024朝阳一模-9` 的同类题列表。
  - 未在原型中陈述任何答案/挂载/题型。
- `Q-2026丰台一模-18-2`(answer/action/locator follow Phase07 patch freeze):
  - 在冻结 29 行中,推理 L4。
  - 解题动作严格沿用 patch freeze 表述:"先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误。"
  - answer locator 锁定为 `answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric`,不进入正文,只在审计行保留。
  - 不写演绎推理;大项/中项/小项识别顺序原文锁定保留为易错陷阱。

## 6. 禁用术语自检(prototype 正文)

- `source locator`、`lane`、`Governor`、`Confucius`、`packet`、`L3`、`L4`、`A-formal`、`A-support`、`B-choice-signal`、`/Users/`、`C:\` 等内部术语均未进入 prototype 正文(教学型 markdown body 与 CSV `generated_text` 字段)。
- 内部术语只出现在合规备注、change log 的 before/after 描述与 csv `opus_self_note` 字段中,这些字段属于审计。
- 未引用任何文件路径、行号、`@L...`、`Slide...`、`renders/page_...`、`.pdf::`、`.pptx::`、`.docx::`、`.rtf::` 等定位串于原型正文。

## 7. 正面合规清单

- 答案、配对、L3/L4 状态、来源定位均与 Phase08 输入冻结一致。
- 交叉双挂载五题(`Q-2024朝阳二模-19-1`、`Q-2024朝阳二模-19-2`、`Q-2024朝阳期中-9`、`Q-2026顺义一模-19-1`、`Q-2026顺义一模-19-2`)保留 thinking + reasoning 双挂载;主挂载推理、次挂载思维。
- 推理章节按"题型→规则口诀→常见陷阱→同类真题→解题动作"组织;未写推理总论。
- 思维章节按"材料信号→可写思维方法→为什么能想到→答题动作→答案落点→易错陷阱→同类题"组织。
- 改动日志全部为 `change_type ∈ {wording_only, structure_only}`;`answer_changed`、`status_changed`、`question_deleted`、`question_added`、`pairing_changed` 全部 `must_be_no`。
- 自检命令记录:
  - `python3 -c "import csv; rs=list(csv.DictReader(open('phase08_opus_change_log.csv', encoding='utf-8-sig'))); print(set(r['change_type'] for r in rs))"` → `{'wording_only', 'structure_only'}`。
  - `python3 -c "import csv; rs=list(csv.DictReader(open('phase08_opus_change_log.csv', encoding='utf-8-sig'))); print(all(r[k]=='must_be_no' for r in rs for k in ['answer_changed','status_changed','question_deleted','question_added','pairing_changed']))"` → True。

## 8. NEEDS_SOURCE_REPAIR 备注

- 无 `NEEDS_SOURCE_REPAIR` 行。所有 29 行原型 generated_text 均能基于 Phase08 输入冻结写出 review-only 教学原型;未对任何题写入 `NEEDS_SOURCE_REPAIR` 标记。
- `Q-2025顺义一模-7` 的原始 phase07 数据对正确选项 A 的解释存在概念性复杂(题干"逻辑分析错误"指向"分析"本身有误,而非谬误本身不存在);本原型保留原始解释,不重写;若后续 Codex A / Lane B 审核要求改写,需要明确证据级别提升后再行处理。
- `Q-2026顺义一模-19-2` 的原始 phase07 数据将 `primary_reasoning_type` 字段标为"三段论;判断;推理",但 `rule_slogan` 实际为"科学思维三特征"。本原型保留原始挂载与字段,不重新归类;若后续 Codex A / Lane B 复核认为应改归思维,需要单独 gate 决定。

## 9. 后续推进建议

- Lane B Phase08 原型审计已完成并报 WARN;Codex A 已清理正文中的文件编号式表述、阶段字段名式表述,补入两个选择题答案字母,并从清洗后的 Markdown + Phase08 freeze 重建 29 行 CSV。下一步进入 Governor / Confucius review-only gate + 新一轮 GPT commander packet。
- 任何升级到学生稿、Word/PDF、最终 PASS,必须先通过上述 gate 链;本阶段不授权。
