# 给 GPT-5.5 Pro：选必三《逻辑与思维》Phase12 全量扩容审查

你是本项目的 chief content reviewer / pressure tester。请不要批准当前 29 题候选稿为终稿；本轮请专门审“为什么题量不足、如何扩到全量、如何重排结构”。

## 项目背景

项目：北京高考政治 选必三《逻辑与思维》思维与推理宝典。

本地工作目录：

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

用户目标：

- 完全模仿已经成功的“哲学宝典”做法。
- 思维部分要像哲学原理方法论一样处理：材料信号、可写方法、触发逻辑、答案动作都要讲清楚。
- 推理部分要按题型分类：三段论、假言推理、选言推理、归纳推理、类比推理、概念/判断/逻辑规则等，同类题都放在对应题型下面。
- 不是做代表例题小册子，而是尽量穷尽约 60 套卷中所有有效的选必三思维/推理题。
- 最后交付学生可用 Word 文档，必须经过 Word/版式验收。

## 当前问题

当前候选 Word 只有 29 条。用户明确质疑：约 60 套卷不应该只有 29 题，预计应接近或超过 100 题。

本地证据显示用户质疑成立：

- `05_coverage/phase05_evidence_pool_74.csv` 有 74 条 locked evidence rows。
- 这 74 条中：选择题 47 条，主观题 27 条。
- 模块分布：推理 38 条，思维 23 条，交叉 13 条。
- `09_student_draft/phase10_5_pre_gpt_expansion_gap_inventory.csv` 显示：
  - 29 条进入正文 body；
  - 16 条只是同类题索引；
  - 29 条正文和索引都未体现；
  - 合计 45 条 non-body rows 仍未转为学生正文。
- `09_student_draft/phase10_5_pre_gpt_expansion_gap_summary.md` 显示 Phase07 permission：
  - 25 条 `hold_answer_locator_risk`;
  - 20 条 `hold_reasoning_form_risk`;
  - 4 条 `include`;
  - 25 条 `include_as_packet_candidate`.
- `05_coverage/phase04_control_base_status_after_batch03_cleaned.csv` 有 362 个控制底座行：
  - 231 选择题；
  - 129 主观题；
  - 2 suite visual blocker。
  这些不全是可入正文证据，但说明还应回扫 source/control base，排查是否有有效选必三题被过度保守排除。

因此：29 题只能算 controlled candidate packet，不是 final document。

## 用户刚刚新增的排序硬要求

最终学生文档顺序必须改成：

1. 主观题在前。
2. 选择题在后。
3. 每一类内部按区排序：海淀、西城、东城、朝阳、丰台、其他区。
4. 同一区内部按时间倒序：2026、2025、2024。
5. 同年同区再按考试阶段和题号稳定排序。

## 请你审查并输出

请严格按以下结构回复：

### 1. Verdict

在以下结论中选一个，并说明理由：

- `EXPAND_REQUIRED_29_INVALID_AS_FINAL`
- `EXPAND_TO_74_FIRST_THEN_RESCAN`
- `RESCAN_362_BEFORE_ANY_WORD`
- `OTHER`

### 2. Minimum Scope

请判断最终学生文档最低应包含多少题才算“没有偷懒”：

- 是否必须先把 74 条 locked evidence rows 中可修复者全部转正文？
- 45 条 non-body rows 中哪些应优先转正文，哪些可以只做索引，哪些必须继续 blocked？
- 是否必须回扫 362-row control base/source roots，争取补到 90-120 左右？

### 3. Expansion Policy For 45 Non-Body Rows

请给出处理策略：

- `hold_answer_locator_risk` 如何修源后入正文？
- `hold_reasoning_form_risk` 如何复核推理形式后入正文？
- “same-type index only” 是否应该多数转为正文？
- “not represented” 是否应该逐条给出入正文/排除理由？

### 4. 推理部分结构

请给出推理部分的分类框架，要求同类题都挂进去，不只放代表例：

- 三段论
- 充分条件假言推理
- 必要条件假言推理
- 选言推理
- 归纳推理
- 类比推理
- 概念、判断、逻辑规则、逻辑错误
- 其他你认为北京卷常考的类型

### 5. 思维部分结构

请给出思维部分如何模仿哲学宝典的正文结构。要求每个条目能让学生知道：

- 材料怎么看；
- 该写哪个思维方法；
- 为什么触发；
- 答案句怎么落；
- 易错项怎么避。

### 6. 最终排序规则

请确认或修正用户排序规则：

主观题先于选择题；每类内部海淀、西城、东城、朝阳、丰台、其他区；时间 2026 > 2025 > 2024。

### 7. 禁止项

请明确指出：

- 29 题候选稿能否叫终稿？
- 能否继续做 Word/PDF final？
- 如果不能，下一步最小闭环是什么？

### 8. 给 Codex 的下一步命令

请给出一组具体执行指令，让 Codex 后续照做，包括：

- 先补哪些 ledgers；
- 先修哪些源；
- 如何重建正文；
- 如何验收题量；
- 如何再做 Word。

请不要泛泛鼓励，要像项目总指挥一样给可执行方案。
