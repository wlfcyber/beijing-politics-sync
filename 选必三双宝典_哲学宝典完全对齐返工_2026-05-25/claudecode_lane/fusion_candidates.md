# Fusion Candidates — 给 Codex 的融合裁决入口

本文件按 11 号包 `OUTPUT_SCHEMA` 第 5 节硬规则，把 B 线本轮 entries 与 Codex A 线现有 Word/PDF + `05_candidate_md/` 候选稿之间的关系，按 7 类列出。每条都给：

- ClaudeCode entry id
- Codex 对应条目或缺口（候选 MD 行号或章节）
- 建议动作
- 证据理由
- 学生版清洗注意事项

> 文件路径都以本 run 根目录为参照。`A候选MD` = `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`；`B候选MD` = `05_candidate_md/选必三_逻辑与思维_推理宝典_哲学完全对齐候选稿.md`。

---

## 1. replace_codex_thin_entry

Codex 现稿是有效条目但偏薄/把多节点压成一段；建议用 B 线分节点条目替换。

### F1.1 — 2026顺义一模 Q19(2) 三节点替换

- ClaudeCode entry: `T-2026-SHUNYI-1MO-Q19-2-A` / `-B` / `-C`
- Codex 对应: `A候选MD` 56-64 行 “1. 2026顺义一模 Q19(2)” 单条目把客观性/预见性/可检验性压成一段
- 建议动作: 用 B 线三条按客观性/预见性/可检验性三节点分别挂载，替换 Codex 单条目
- 证据理由: 哲学宝典风格要求每个小方法节点单独配题；本题是科学思维三特征的硬样本，必须按节点拆开
- 学生版清洗: 三条 entries 中 `audit_note` 不进学生版；`source_lock` 不进学生版

### F1.2 — 2025海淀二模 Q20 四节点替换

- ClaudeCode entry: `T-2025-HAIDIAN-2MO-Q20-A` / `-B` / `-C` / `-D`
- Codex 对应: `A候选MD` 286-294 行单条目把分析综合/整体性/动态性质量互变/辩证否定全部压成一段
- 建议动作: 用 B 线四条分挂；学生版的“分析与综合 / 整体性 / 动态性与质量互变 / 辩证否定”四节点分别配该题
- 证据理由: hard sample；硬规则记事本第二十一条要求辩证思维下沉到子节点配题
- 学生版清洗: 四节点同题复挂时，每节点的 `material_trigger` 必须单独成段，不得复制

### F1.3 — 2026朝阳期中 Q21(2) 四节点替换

- ClaudeCode entry: `T-2026-CHAOYANG-MID-Q21-2-A` / `-B` / `-C` / `-D`
- Codex 对应: `A候选MD` 555-564 行 与 666-674 行同题双段写法
- 建议动作: 按超前/联想/逆向/发散聚合四节点分挂，替换 Codex 双段拼接
- 证据理由: hard sample；硬规则第二十一条要求创新思维下沉到具体方法
- 学生版清洗: 删除 `audit_note`、`source_lock`、`evidence_level` 等审计字段

### F1.4 — 2024海淀二模 Q17(1) 三节点替换

- ClaudeCode entry: `T-2024-HAIDIAN-2MO-Q17-1-A` / `-B` / `-C`
- Codex 对应: `A候选MD` 143-151 行（科学思维 复合方法）+ 230-238 行（探索性与方法更新）+ 257-265 行（整体安排）三段
- 建议动作: 用 B 线三条 entry 替换 Codex 三段；保留 B 线的单节点四要件写法，避免“三特征列举句”
- 证据理由: hard sample；hard-rule notebook 第十六/十八条 SCIENCE_ONLY_SOURCE_SUPPORTED；不得回流为三模块并列设问
- 学生版清洗: B 线 `audit_note` 显式提醒不得回流为三模块并列，融合时保留该约束但不进学生版

### F1.5 — 2025顺义一模 Q7 谬误名称纠错替换

- ClaudeCode entry: `RC-2025-SHUNYI-1MO-Q7`
- Codex 对应: `B候选MD` 425-439 行
- 建议动作: B 线 `tempting_wrong_options` 字段已逐项写 B/C/D 错因；用 B 线条目替换 Codex 现稿，保证字段对齐 OUTPUT_SCHEMA
- 证据理由: hard-rule notebook 第十九条；不得正向写为“小项不当扩大”
- 学生版清洗: B 线已锁定名称纠错方向；学生版只显示题面/选项/答案/正确理由/诱人错项+错因

---

## 2. append_missing_material_trigger

Codex 现稿已有正文但 `材料触发点` 仍偏摘抄或偏程序化；建议把 B 线 `material_trigger` 字段并入。

### F2.1 — 2024西城一模 Q19(2) 定义构成

- ClaudeCode entry: `RM-2024-XICHENG-1MO-Q19-2`
- Codex 对应: `B候选MD` 定义构成段落（约 195-210 行附近，candidate gate batch5 已处理过）
- 建议动作: 把 B 线 entry 的“被定义项=新质生产力；定义联项=是；种差=……；属概念=先进生产力”逐项分述并入材料触发
- 证据理由: 定义构成要求严格按四要素拆，B 线写法更便于学生记忆
- 学生版清洗: 学生版不写“定义联项”这一术语本身，而以“用是连结”表达

### F2.2 — 2024西城一模 Q19(3) 属种关系

- ClaudeCode entry: `RM-2024-XICHENG-1MO-Q19-3`
- Codex 对应: `B候选MD` 同一题目下一条
- 建议动作: 把“新型举国体制⊂举国体制”这一外延符号化表达从 B 线吸收（学生版可写为“包含关系”，不必符号）
- 证据理由: 加强“属种关系”概念外延表达准确性

### F2.3 — 多套类比推理评析

- ClaudeCode entries: `RM-2025-FENGTAI-2MO-Q16-2` / `RM-2026-CHAOYANG-2MO-Q19-1` / `RM-2024-CHAOYANG-MID-Q18` 等
- Codex 对应: `B候选MD` 各类比章节中的 “看到题目把前提和结论组织成…” 类程序化句仍可能存在残留
- 建议动作: 用 B 线的“两对象在 X、Y 属性上相似 → 推断 Z 属性也相似”这一具体材料触发替换泛化句
- 证据理由: 哲学宝典要求材料触发是“学生能圈出的具体动作或关系”，不是“归类句”

---

## 3. append_missing_answer_landing

Codex 现稿正文存在但 `答案落点` 偏短/偏抽象/混入制作说明；建议用 B 线 `answer_landing` 替换或并入。

### F3.1 — 2024东城一模 Q18(3) 辩证否定

- ClaudeCode entry: `T-2024-DONGCHENG-1MO-Q18-3`
- Codex 对应: `A候选MD` 中辩证否定节点对应题段
- 建议动作: 用 B 线写的卷面答案句“传统产业是未来产业的基础和起点，未来产业是对传统产业的扬弃改造和前瞻布局……”替换偏短结论
- 证据理由: 答案落点必须可直接写到答题纸；B 线版本结构 = 术语+本题事实+结论
- 学生版清洗: 不出现“先写”“要写”等制作说明语

### F3.2 — 2025海淀期末 Q18 改变条件与新联系

- ClaudeCode entry: `T-2025-HAIDIAN-FINAL-Q18`
- Codex 对应: 该节点本身在 Codex 现稿中可能是新建节点；B 线 entry 可作为基础
- 建议动作: 用 B 线 `answer_landing` 作为该节点的代表答案句

### F3.3 — 2026海淀二模 Q18(1) 多动作复挂

- ClaudeCode entry: `T-2026-HAIDIAN-2MO-Q18-1`
- Codex 对应: `A候选MD` 同题段
- 建议动作: 把 B 线“分析与综合 → 联想 → 实践检验”三段动作落到答案落点

---

## 4. append_choice_wrong_option_reason

Codex 现稿的选择题缺“诱人错项+错因”逐项写；建议用 B 线 `tempting_wrong_options` 补齐。

### F4.1 — 2025顺义一模 Q7

- ClaudeCode entry: `RC-2025-SHUNYI-1MO-Q7`
- Codex 对应: `B候选MD` 425-439 行
- 建议动作: 把 B/C/D 三个错项的“为什么诱人 + 为什么错（在该题中是‘三段论规则本身正确所以不选’）”从 B 线吸收
- 证据理由: hard sample；学生需要明白本题正向选 A 是因为 A 的名称错了，B/C/D 反而是“规则判断正确所以不选”

### F4.2 — 2024朝阳一模 Q6

- ClaudeCode entry: `RC-2024-CHAOYANG-1MO-Q6`
- Codex 对应: `B候选MD` 1270 附近
- 建议动作: 把 A 的“越级划分”、C 的“矛盾律违反”、D 的“四概念”从 B 线吸收

### F4.3 — 2026海淀二模 Q5/Q6/Q7

- ClaudeCode entries: `RC-2026-HAIDIAN-2MO-Q5` / `Q6` / `Q7`
- Codex 对应: `B候选MD` 230-247 行(Q5) + 294-314 行(Q6) + Q7 段
- 建议动作: B 线已逐项写完整 `tempting_wrong_options`，建议替换 Codex 现稿对应段落
- 学生版清洗: 不写“答案表锁定”“客观答案表”等审计语

### F4.4 — 2024东城一模 Q6 / Q7 / Q8

- ClaudeCode entries: `RC-2024-DONGCHENG-1MO-Q6` / `Q7` / `Q8`
- Codex 对应: `B候选MD` 1117-1132 行附近
- 建议动作: 用 B 线条目作为该套卷三条选择题的标准化模板

### F4.5 — Q0028 B-choice-signal 占位

- ClaudeCode entry: `RC-2025-FENGTAI-FINAL-Q9`
- Codex 对应: `B候选MD` 中 2025丰台期末 Q9 段
- 建议动作: B 线只提供占位 body；Codex 必须按本 run 客观答案表与原卷选项原文重写 `options`、`answer`、`correct_reason`、`tempting_wrong_options`
- 学生版清洗: 占位句 “(以原卷为准)” 严禁出现在学生版

---

## 5. add_framework_node_mount

Codex 现稿中该节点缺挂载或挂错节点；建议在思维/推理 framework 下新增/纠正挂载。

### F5.1 — 思维“认识发展历程”三段链

- ClaudeCode entry: `T-2024-HAIDIAN-2MO-Q17-2`
- Codex 对应: A候选MD 中“认识发展历程”章节如挂题不稳，可用本 entry 作为代表题
- 建议动作: 在“感性具体 → 思维抽象 → 思维具体”节点固定挂本题

### F5.2 — 思维“整体安排”作为科学思维内部节点

- ClaudeCode entry: `T-2024-HAIDIAN-2MO-Q17-1-C`
- Codex 对应: 若 A 候选 MD 把“整体安排”挂到辩证思维整体性，需纠正回科学思维内部
- 建议动作: 在“科学思维/整体安排”节点固定挂本题

### F5.3 — 推理“概念外延关系/属种”节点

- ClaudeCode entry: `RM-2024-XICHENG-1MO-Q19-3` / `RC-2024-HAIDIAN-2MO-Q6`
- Codex 对应: 推理册若该节点仅有 1 条挂题，建议把 B 线 2 条同时挂入
- 建议动作: 形成“属种判断主观+选择题双对照”

### F5.4 — 推理“逻辑三律/同一律”节点

- ClaudeCode entry: `RC-2024-XICHENG-1MO-Q11`
- Codex 对应: `2024西城一模 Q19(5)` 已回正为思维册超前思维，不能再作为同一律主观题融合；逻辑规律节点以 Q11 等选择题覆盖。

---

## 6. keep_as_index

不进 student body，但保留在 audit 字段或同类索引中。

### F6.1 — 2025海淀二模 Q20 推理册索引

- ClaudeCode entry: `RM-2025-HAIDIAN-2MO-CROSS`
- 建议动作: 仅作推理册的“同题不构成单一推理形式”索引；学生在推理册看到此索引时跳转思维册 `T-2025-HAIDIAN-2MO-Q20-A/B/C/D`

### F6.2 — Q0123 / Q0137 / Q0138 B-choice-signal 三条

- ClaudeCode entries: `RC-2026-HAIDIAN-2MO-Q4-INDEX` / `RC-2026-SHUNYI-2MO-Q6-INDEX` / `RC-2026-SHUNYI-2MO-Q7-INDEX`
- 建议动作: 保留在 audit 字段；不写入学生稿
- 证据理由: B-choice-signal 不能冒充 A-formal 主观题评分链

### F6.3 — Q0069 2024门头沟一模 Q20 B-compilation body

- 建议动作: 如 Codex 不接受 B-compilation 进 student body，可降级为 keep_as_index；如接受，必须在 audit 字段写明 `evidence_level=B-compilation`
- 学生版清洗: 不出现 “B-compilation” 字样

---

## 7. reject_or_block

证据不足或会污染学生版；必须拒绝进 student body 或 blocked 等条件解锁。

### F7.1 — 2024北京高考 19(2)

- 状态: blocked；缺正式细则
- 建议动作: 不进 student body；等待用户提供正式细则；不冒充 A-formal

### F7.2 — 2024房山一模 Q20(1) B-compilation

- 状态: excluded
- 建议动作: 不进 student body；保留在 audit 边界

### F7.3 — Codex 现稿任何把 2024海淀二模 Q17(1) 写成“三模块并列设问”的版本

- 建议动作: 直接 reject；按 D05 决议与 hard-rule notebook 第十八条，必须回到 SCIENCE_ONLY_SOURCE_SUPPORTED
- 学生版清洗: 三模块并列写法属硬失败

### F7.4 — Codex 现稿任何把 2025顺义一模 Q7 正向描述为“小项不当扩大”或“四概念”的版本

- 建议动作: 直接 reject；按 D06 决议
- 学生版清洗: 名称纠错方向不可反转

### F7.5 — Codex 现稿中所有被 B 线 COVERAGE 判 `excluded` 的思维选择题如出现在学生思维正文

- 建议动作: 全部移出思维册学生正文；可保留在“边界陷阱”附录或推理册（若具备稳定推理形式）

---

## 融合统计模板（建议 Codex 在 fusion 报告中按此口径填写）

- Codex 原有条目数（按 candidate MD body 条目计）: 思维 43 / 推理 79
- ClaudeCode 本轮 entries 数: thinking_main 31 / reasoning_main 31 / reasoning_choice 23 = 85
- ClaudeCode 独有导入数（B 线新增节点或新写法）: 待 Codex 比对填写
- ClaudeCode 替换 Codex 数（F1.x 类）: 至少 5 处（F1.1 / F1.2 / F1.3 / F1.4 / F1.5）
- Codex 覆盖保留数: 待填
- ClaudeCode rejected 数及原因: 0（B 线本轮无内部拒绝；如 Codex 在融合时回源后否决某条，应在此填写）
- 最终正文条目数: 由 Codex 在融合后统计
- 四字段缺失数: 由 Codex 在融合后扫描
- 学生禁词命中数: 由 Codex 在融合后扫描

## 学生版清洗共同注意事项

适用所有 entries：

- 删除 `entry_id`、`decision`、`evidence_level`、`source_suite`、`question_id`、`framework_type`、`framework_node`、`reasoning_family`、`logical_form`、`valid_or_invalid_form`、`source_lock`、`audit_note` 等审计字段。
- 学生正文只保留 `full_prompt`、`material_trigger`、`why_this_method`、`answer_landing`、`common_trap`（思维）；`logical_form` 可在推理章节作为“形式提示”出现，但不写英文字段名。
- 选择题学生正文显示 `question_stem`、四个完整 `options`、`answer`、`correct_reason`、按 A/B/C/D 列出的 `tempting_wrong_options`（用中文小标题，不写 `tempting_wrong_options` 这个字段名）。
- 任何包含 `/Users/`、`C:\`、`OCR`、`debug`、`line id`、`file id`、`question_id`、`A-formal`、`B-choice-signal`、`评标`、`参考答案`、`答案写`、`PASS`、`final`、`候选稿门禁` 的字符都必须从学生版剔除。
- 三模块并列写法、谬误名称反转写法、B-choice-signal 升级为主观评分链的写法，一律 reject。
