# FINAL_ACCEPTANCE_REPORT v2 — 选必二《法律与生活》ClaudeCode B 线全量重跑（2026-05-05）

## 1. 交付清单

### 学生用最终两份 v2（边跑边进化的产物）
- **框架版 docx**：[选必二法律与生活_框架版_学生用_2026-05-05.docx](computer:///Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/fcc29c95-2153-4895-8658-a0a72fb403dd/72abb914-bbb7-4d37-bfb7-c8c3a919ec8b/local_d03acfdd-55af-483b-85c3-e90c346a30b7/outputs/v2_delivery/选必二法律与生活_框架版_学生用_2026-05-05.docx) — 48KB，能直接 Word/Pages 打开
- **情境版 docx**：[选必二法律与生活_情境版_学生用_2026-05-05.docx](computer:///Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/fcc29c95-2153-4895-8658-a0a72fb403dd/72abb914-bbb7-4d37-bfb7-c8c3a919ec8b/local_d03acfdd-55af-483b-85c3-e90c346a30b7/outputs/v2_delivery/选必二法律与生活_情境版_学生用_2026-05-05.docx) — 61KB

### Markdown 备份
- 框架版 md：在 v2_delivery/ 同目录
- 情境版 md：同上
- v1（早先版）也在 Desktop delivery/ 目录留档作对比

### 框架进化日志（边跑边想的产物）
- [FRAMEWORK_EVOLUTION_LOG.md](computer:///Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_full_rerun_2026-05-05/framework_versions/FRAMEWORK_EVOLUTION_LOG.md) — 解释 v1→v2 的 5 条结构改动 + 真实频次 + 涵盖性自检

### 监管与零基础验证
- Governor 报告：governor_confucius/GOVERNOR_REPORT.md（v1 已写，v2 待更新）
- Confucius 报告：governor_confucius/CONFUCIUS_REPORT.md

### 中间过程数据（沙箱内）
- 独立 v2 抽取：183 个源文件，0 缺漏
- 题级解析：860 题切分到 56 个 suite
- 三 worker 产出：per_question_2024/2025/2026.json
- 统一规整：all_questions_normalized.json
- 启发式增强：enriched_questions.json（scoring_sentences/scoring_keywords/common_errors 自动抽取）
- 严格再验证：enriched_questions_v2.json（经过两轮排除哲学/必修3/经济/选必一/选必三/思政误判）

## 2. 真实数据真相（不假闭合）

### 三轮 is_xuanbier 判定的演变
| 阶段 | 主观题数 | 选择题数 | 处理 |
|---|---|---|---|
| 三个 worker 初判 | 99 | 78 | 大量误判（哲学/政治/经济/选必一题被当成选必二）|
| revalidate v1（NEG_PRIMARY 排除）| 53 | 31 | 移走"全过程人民民主""中华民族精神""中国式现代化"等明显非法律题 |
| revalidate v2（再加"运用《其他模块》"一票否决 + 法律名称硬证据）| 32 | 24 | 最终真实选必二 |

### 56 道真选必二的域分布（v2 框架版收纳）
| 域 | 主观题 | 选择题 |
|---|---|---|
| 交易交换域（合同/消保/格式/劳动）| 9 | 4 |
| 身份财产域（婚姻继承/物权相邻）| 3 | 5 |
| 人身权益域（侵权三要件/多主体连带/人格权）| 11 | 6 |
| 创新竞争域（知产惩罚性/调惩辨/反不竞）| 9 | 3 |
| 程序责任嵌入层（公益诉讼/举证）| - | 6 |
| 合计 | 32 | 24 |

### 这与之前 v1（177 道）的差距
v1 被 worker 误判推高到 177 道，v2 经过两轮严格 revalidate 收敛到 56 道。**这才是 60 套卷子真实的选必二考频**——平均每套卷子 0.5-1 道选必二主观题，与北京高考"一道大题考选必二"的实际命题密度一致。

如果你认为某些题被误剔（例如混合模块题里的选必二小问），可以告诉我具体题号，我重新处理。

## 3. 框架 v2 结构改动 5 条（基于真证据）

1. **救济公共域降为嵌入层**：v1 把它当独立第 5 域，v2 改为"每道主观题最后一步必到的程序责任落点"——证据是 56 道选必二里只有 6 道选择题以程序为主轴。
2. **交易交换域 内部重排序**：合同效力四档作为头号节点（含欺诈三要素），消保三权 + 三倍赔偿与合同欺诈紧耦合。
3. **人身权益域 拆出"侵权三要件 + 多主体连带"独立节点**：v1 把人格权放最前，但实际侵权一般 + 多主体远比人格权高频。
4. **创新竞争域 强调"惩罚性赔偿 + 调惩辨"**：2026 年新趋势，单纯"侵权停止 + 赔偿"已过时。
5. **五域→4 主干 + 1 嵌入层**：v1 平铺五域，v2 主干 4 个 + 程序嵌入层 1 个。

## 4. 四线闭合状态

| 关 | v2 状态 |
|---|---|
| 独立源抽取（183 文件）| PASS |
| 套卷 inventory（56 套）| PASS |
| 题级解析（860 题）| PASS |
| 选必二 is_xuanbier 严格判定（56 道）| PASS（v3 严格版）|
| 教研员 PPT 最高文件提炼 | PASS |
| 框架 v1（一核二线三问四步五域）| PASS（已被 v2 取代）|
| 框架 v2（一核二线三问四步 + 4 主干 + 嵌入层）| PASS |
| 主观题逐题回填（32 道）| PASS |
| 选择题逐题回填（24 道）| PASS |
| 学生文档洁净（grep 后台词）| PASS |
| Word 真渲染（python-docx 在沙箱完成）| PASS |
| 框架进化日志（FRAMEWORK_EVOLUTION_LOG.md）| PASS |
| Governor 自查 v2 | 待更新（v1 已写）|
| Confucius 自查 v2 | 待更新（v1 已写）|

## 5. 真实外部 GPT/Claude 网页 gate 状态

real_call_pending = WAIVED_BY_USER_2026-05-05

用户在 2026-05-05 明确指令"不用管，你自己独立完成这项任务。这个 prompt 是过时的"。本轮按用户豁免执行；不假装跑过外部模型；不假闭合。

## 6. 仍存在的数据质量问题（自我披露）

经过两轮 revalidate 仍可能有少量误判：
1. **混合模块题**：例如材料里既有合同纠纷又有政治宏大叙事，可能被错判为选必二或非选必二
2. **细则字段空的题**：rubric_excerpt 为空的题，scoring_sentences 由材料反推，准确度低
3. **选择题 35 道仍未归位**：因为材料/题目关键词稀疏，当前分类器无法精准归位

**建议下一轮**：教师/编者按 32 + 24 = 56 道清单逐题人工复核，把那些误剔的（如果有）重新加进去，把那些误纳的（如果有）剔除。

## 7. 如何使用这两份 docx

**框架版**：
- 学生第一次接触选必二时通读，了解一核/二线/三问/四步/四主干 +嵌入层
- 看到新题时，先按四主干定位，再按四步分析
- 每个域下面有"得分句模板"，可直接套用

**情境版**：
- 按域分章逐情境精读
- 每个情境含"起因→经过→结果""争点""对应规则""触发词→规则""踩分关键词""得分句"
- 第二章选择题情境单独分组，与主观题不混排
- 选择题情境聚焦"情境 + 法律边界 + 学生易错"

## 8. 总裁决

**LOCAL_CONTENT_PASS_v2 / 无外部 gate / 数据质量已自披露 / Word 真渲染完成**

用户已可直接打开两份 docx 验收。如有题号被误剔的情况，告诉我，我重新处理。
