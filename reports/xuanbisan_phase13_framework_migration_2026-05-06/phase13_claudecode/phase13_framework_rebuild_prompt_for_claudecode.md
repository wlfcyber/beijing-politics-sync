# ClaudeCode Phase13 Framework Rebuild Prompt

你是 ClaudeCode 生产线。当前任务不是继续美化已经交付的按题排序版，而是按用户新纠偏重写选必三《逻辑与思维》学生宝典结构。

## 工作目录

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## 必读规则

1. `00_飞哥选必三逻辑与思维硬性要求记事本.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
3. 特别执行 2026-05-06 框架版结构硬规则。

## 可用输入

- 原 77 条学生正文：`09_student_draft/phase12_student_clean_candidate.md`
- 思维方法索引：`09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md`
- 推理题型索引：`09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md`
- 最终输出旧版：`outputs/2026北京高考政治选必三逻辑与思维宝典---思维与推理全触发全链条_学生版.md`
- 哲学宝典模板结构：`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04/01_extract/philosophy_template_structure.md`
- 哲学宝典最终 Markdown：`/Users/wanglifei/Desktop/北京高考政治/必修四终极融合版_2026-05-02/outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_终极融合版.md`

## 用户指出的问题

当前版本正文结构错了：前面只是罗列题目来源或索引，后面仍按大题单位展开。用户要求像哲学宝典一样，以框架为单位：

`思维类型 -> 思维特点/小方法 -> 固定分析流程 -> 对应模拟题`

例：科学思维下面必须有客观性、预见性、可检验性等；创新思维下面必须有三新、联想、发散聚合、逆向、超前等；辩证思维下面必须有整体性、动态性、分析与综合等。每个节点下面配模拟题，而不是把题目按地区时间排成流水账。

推理部分也一样：按题型树组织，每个题型下面挂全部同类题。

## 输出要求

只写到以下目录，不要覆盖 outputs 里的旧终稿：

`claudecode_lane/phase13_framework_rebuild/`

必须生成：

1. `phase13_framework_rebuild_claudecode_draft.md`
2. `phase13_framework_mount_matrix.csv`
3. `phase13_framework_rebuild_review.md`

## 结构要求

学生正文必须是：

1. 使用方法
2. 第一部分：思维方法框架
   - 科学思维
     - 客观性
     - 预见性
     - 可检验性
     - 探索性与方法更新（仅题源支持时）
     - 整体安排（仅题源支持时）
   - 辩证思维
     - 整体性
     - 动态性
     - 分析与综合
     - 质量互变
     - 辩证否定
   - 创新思维
     - 思路新/方法新/结果新
     - 联想思维
     - 发散思维与聚合思维
     - 逆向思维
     - 超前思维
     - 改变条件/建立新联系
   - 认识发展历程
     - 感性具体
     - 思维抽象
     - 思维具体
   - 系统观念
   - 边界陷阱与易混选择题
3. 第二部分：推理题型框架
   - 概念与定义 / 概念外延关系
   - 联言判断与联言推理
   - 相容/不相容选言推理
   - 充分条件假言推理
   - 必要条件假言推理
   - 三段论结构与周延谬误
   - 归纳推理
   - 类比推理
   - 逻辑三律
   - 复合推理与易混题

每个节点必须先写固定分析流程：

- 材料怎么看
- 该写哪个方法/规则
- 为什么触发
- 答案句怎么落
- 易错项怎么避

然后挂模拟题。题目条目沿用哲学宝典四要件和当前 Phase12 内容：

- `材料触发点` 或 `题干信号`
- `设问`
- `为什么能想到`
- `答案落点` / `正确项` / `错项陷阱`
- `考场动作`
- `同类题索引`

## 禁止

- 不准把最终正文继续写成 `主观题 -> 选择题 -> 地区时间 -> 大题`。
- 不准只列题目来源清单，不展开模拟题。
- 不准删掉 77 条已清洁内容；如果某题只适合相关检索或边界陷阱，必须说明。
- 不准把审计词、路径、英文内部字段写进学生正文。
- 不准称最终版、终稿、PASS；这是 ClaudeCode 重写草稿，供 Codex 融合。

## 审计矩阵字段

`phase13_framework_mount_matrix.csv` 至少包含：

- title
- source_section
- framework_part
- framework_node
- sub_node
- tag
- included_as
- reason

## 自查重点

1. 科学思维三性是否都有题。
2. 创新思维三新、联想、发散聚合、逆向、超前是否都有题。
3. 辩证思维整体性、动态性、分析综合是否都有题。
4. 推理题型是否不是流水账。
5. 是否保留完整选择题选项、正确项和错项陷阱。
6. 是否没有审计/路径/REVIEW_ONLY/question_id 等学生版污染。
