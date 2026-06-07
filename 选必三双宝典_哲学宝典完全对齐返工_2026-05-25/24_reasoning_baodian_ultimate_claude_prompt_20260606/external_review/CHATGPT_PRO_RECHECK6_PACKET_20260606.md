# ChatGPT Pro Sixth Recheck Packet

Please run an external recheck after the latest local repair pass. The local artifact has been regenerated and QA/PDF checks rerun after repairing the latest review findings.

Specific retest targets:

1. Confirm the fifth-recheck REVISE items are closed: the scientificity line break, the missing left quote before definition-narrowness, missing-source process wording, and revision-title residue.
2. Confirm expanded G13 currently reports zero visible text break hits for these newest patterns.
3. Re-sample prior fourth-recheck material repairs: city OCR, AT1/GS3 material OCR, AI-analysis table flow, and the two-conclusion AI answer layer.
4. Re-sample prior material-layer repairs, the two neutral missing-source entries, and answer-layer completeness.
5. Re-check language for template tone, backend traces, broken punctuation, and answer-layer incompleteness.

Use the same output shape as the review prompt. Verdict must be ACCEPT / REVISE / BLOCK. Treat external review as advisory only; do not invent original paper material or scoring rules.

---

## WEB_MODEL_REVIEW_PROMPT

Source file: external_review\WEB_MODEL_REVIEW_PROMPT_20260606.md

# Web Model Review Prompt

请作为外部审核员审核这份北京高考政治选必三《逻辑与思维》推理部分宝典。你不是原卷/细则证据源，只负责挑错、审逻辑、审学生可用性和语言。

请阅读我上传的文件：

- 《选必三逻辑与思维_推理宝典_终极版_20260606.docx》或同名 PDF
- `QA_GATES_V24_20260606.json`
- `QA_REPORT_V24_20260606.md`
- `DEFECT_LEDGER_V24_20260606.csv`
- `FINAL_ACCEPTANCE_REPORT.md`

目标标准：

1. 做成一个推理宝典，简单、高效、全面、准确。
2. 83 道题必须保留完整，不得遗漏、重复或暗删。
3. 按推理类型分类，每一类要穷尽对应考题。
4. 同一类题要有题型总结和方法总结，但不能有无意义废话、工程痕迹、后台词、AI 模板腔。
5. 每题六层必须有效：这道题考什么 / 题目材料 / 设问 / 怎么想到的 / 满分作答示范 / 采分点对照。
6. “满分作答示范”必须像考生卷面答案，不得是“本题应围绕……”这类元说明，不得照搬“怎么想到的”，也不得照搬“采分点对照”。
7. 两条缺陷台账项（2026海淀期末20(1)、2026朝阳二模19(1)）是原始题面缺失/错位问题；请检查正文是否中性处理、没有伪造题干。

请按以下格式输出：

## VERDICT
`ACCEPT` / `REVISE` / `BLOCK` 三选一。

## Critical Findings
如果有阻断问题，逐条写清题目锚点、问题、为什么影响交付。没有就写 `None`。

## Patch Suggestions
只写可执行修改建议。每条都要说明 Codex 需要回到哪个本地证据检查后才能采纳。

## Language / Student-Use Findings
指出是否还有模板腔、废话、后台痕迹、答题不可抄写的问题。

## Sampled Evidence
列出你抽查的题号/页码/类型，以及通过或失败的原因。

## Boundary
明确说明：你的意见是外部审核建议，不能替代原卷、答案、评分细则和本地 QA。

不要编造原卷材料、评分细则或未上传文件内容；如果需要原始试卷或细则验证，请标注“需本地源证据复核”。


---

## CLAUDE_CODE_COWORK_RECHECK_RESULT

Source file: external_review\CLAUDE_CODE_COWORK_RECHECK_RESULT_20260606.md

# Claude Code Cowork Recheck Result

Run time: 2026-06-06

Lane: real Claude Code CLI, model usage reported as `claude-opus-4-7`, effort max.

Session id: `2d28ae30-fa6a-4574-9fe4-0d881a01d3ee`

Verdict: `ACCEPT`

## Prior Findings Status

1. `2024.11朝阳期中 第18题` under `五、类比推理`: closed. The full-mark answer now directly answers 晏子类比推理, including 橘/枳 -> 人/社会环境, shared external-environment attribute, and analogical rebuttal force. The previous 楚王轻率概括 answer is no longer in this class-5 entry.

2. `2024朝阳一模 第20题第（1）问`: closed. The full-mark answer now begins `推理一属于充分条件假言推理，推理成立。`, so the type-identification point is explicit.

3. New G11: closed. `QA_GATES_V24_20260606.json` reports `G11_type_answer_label: true` and `type_answer_missing: []`.

## New Critical Findings

None.

## Boundary

This recheck is advisory. Local source files, official scoring rubrics, and QA gate outputs remain authoritative.


---

## GPT_PRO_INITIAL_BLOCK_RESULT

Source file: external_review\CHATGPT_PRO_REVIEW_RESULT_20260606.md

# ChatGPT Pro Web Review Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `ask_6862efe4-d6cd-49a6-bb9f-87bd6b93b835`

Verdict: `BLOCK`

## Critical Findings Reported By GPT Pro

1. `2026顺义一模 第19题第（1）问`: material stops after `据此，某同学得出以下推论:` but does not show the actual inference being judged.
2. `2024西城二模 第18题第（1）问`: material asks readers to inspect a table, but the table is absent while answers depend on 352 high-sorghum samples and AT1 variation.
3. `2024西城一模 第19题第（2）问`: material lacks the definition diagram or full definition text while answers use the definition components.
4. `2026海淀期末 第20题第（1）问` and `2026朝阳二模 第19题第（1）问`: material is neutral missing-source text, but the thinking/answer/rubric fields still state determinate content.
5. `2025海淀一模 第21题第（1）问`: full-mark answer appears to force a non-exclusive disjunctive inference and may use an untrue premise.

## Codex Handling Rule

These findings are advisory. Each item must be checked against local paper/rubric/source evidence before adoption. Source-material defects should be moved to the defect ledger or neutralized; do not fabricate missing question text.


---

## GPT_PRO_FIRST_RECHECK_BLOCK_RESULT

Source file: external_review\CHATGPT_PRO_RECHECK_RESULT_20260606.md

# ChatGPT Pro Recheck Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `ask_40c6c793-3f7c-493a-b7e1-7303f141da2c`

## VERDICT

`BLOCK`

## Critical Findings

1. `2025丰台二模 第19题第（1）问`

问题：正文【题目材料】明显混入一段与 AI 版权雷达、盗版资源网站、司法保护主题不匹配的消费促进表格内容，例如工资性收入、医疗养老保障、假冒伪劣、商业设施物流配送、消费场景等。该材料与本题设问“只要给 AI 装上版权雷达，提前扫描问题指令，就能防止点击盗版资源网站”之间缺少可解释的材料链条。

为什么影响交付：该题属于主观题，设问要求结合材料评析观点。当前材料层不可靠，会导致学生无法判断答案中的法律治理、平台治理、技术措施等是否来自原题材料，属于新的题面错位风险。此前台账只保留两条缺源项，但本条也应回本地源证据复核。

2. `2024朝阳一模 第20题第（1）问`

问题：【这道题考什么】末尾出现未完成句：“需要判断能否由……。”

为什么影响交付：这不是来源缺失，但属于学生版可见残句。它会削弱六层结构中第一层的有效性，且说明 QA 的“focus_truncation_hits: 0”没有覆盖该类残句。

3. `2024东城一模 第7题`

问题：【怎么想到的】出现未完成句：“从形式看，‘所有鸟都会飞。” 后文直接进入满分答案。

为什么影响交付：这是明显断句残留。该层用于解释解题路径，残句会影响学生理解，也说明文本完整性仍需人工抽检。

## Patch Suggestions

1. 对 `2025丰台二模 第19题第（1）问`，Codex 需回到本地原卷 PDF/DOCX 或人工校对后的题库源，核对该题完整材料。若当前消费表格确为错粘，应替换为原题中关于 AI 版权雷达、盗版资源、司法建议或平台治理的材料；若本地确无原题材料，应加入缺陷台账，正文按中性缺源方式处理，不能继续保留不相干材料。

2. 对 `2024朝阳一模 第20题第（1）问`，Codex 需回看本地 Markdown 段落，补全为类似：“需要判断能否由否定后件推出否定前件。” 修改后重新跑 focus truncation scan，建议增加对 “由……。” “看，‘……。” 等中文省略残句的规则。

3. 对 `2024东城一模 第7题`，Codex 需回看本地正文，补全【怎么想到的】。建议改为：“从形式看，它是‘所有 M 是 P，S 是 M，所以 S 是 P’；从内容看，大前提‘所有鸟都会飞’不真实，因此形式有效不等于结论真实。”

4. 对 `2024丰台一模 第19题第（1）问`，Codex 需回看本地 Markdown 的【采分点对照】。当前引号被拆成两条项目符号，建议合并为一条完整采分点，避免出现单独以右引号开头的 bullet。

5. 对 `2026通州期末 第19题第（2）问` 推理①，Codex 需回看满分作答示范，“作为，推出”语病应改为“把‘范某阻碍加装电梯’作为推出‘侵犯相关业主合法权益’的充分条件”。

## Language / Student-Use Findings

 prior GPT Pro 五条阻断项中，前四类材料缺失问题看起来已经闭合：`2026顺义一模 第19题第（1）问` 已恢复待判断推论；`2024西城二模 第18题第（1）问` 已恢复 352 种高粱样本和 AT1 变化信息；`2024西城一模 第19题第（2）问` 已恢复定义句和结构提示；两条真实缺源项已中性处理，没有继续给确定答案。

`2025海淀一模 第21题第（1）问` 已避开此前“不相容选言推理”强行套用现实前提的问题。现在用 `P 或 非 P，否定非 P，推出 P` 构造演绎推理，形式有效，但学生使用价值偏弱。若本地评分细则允许换质推理，该条可保留；若细则要求结合材料构造更有内容的演绎推理，仍需回源确认。

语言层仍存在少量可见残句、错粘、语病和断裂标点。它们不属于后台痕迹，但会影响学生直接使用。尤其是 `2025丰台二模 第19题第（1）问` 的题目材料错位风险，已经超过普通润色问题。

## Sampled Evidence

- `2026顺义一模 第19题第（1）问`，三段论类，修复通过。正文已经呈现三段推论，答案区能区分“形式看似三段论”与“大前提不可靠”。

- `2024西城二模 第18题第（1）问`，归纳推理类，修复通过。材料层包含 352 种高粱、AT1 基因定位、转入后耐碱减弱、剪切后耐碱增强，足以支撑不完全归纳、共变法和求异法分析。

- `2024西城一模 第19题第（2）问`，定义结构类，修复通过。材料层给出“举国体制是利用国家力量动员规模性资源、实现国家目标的一种任务组织方式和体制机制安排”，答案能对应被定义项、定义联项、种差、属概念。

- `2026海淀期末 第20题第（1）问`，缺源项，通过。正文保持“原题材料缺失，待补”，没有伪造题干或确定答案。

- `2026朝阳二模 第19题第（1）问`，缺源项，通过。正文保持中性缺源，没有继续给“生产性服务业”定义类确定答案。

- `2025丰台二模 第19题第（1）问`，充分条件判断类，失败。材料层出现消费促进表格，与 AI 版权雷达设问不匹配，需本地源证据复核。

- `2024朝阳一模 第20题第（1）问`，充分条件假言推理类，失败于语言完整性。【这道题考什么】有残句。

- `2024东城一模 第7题`，三段论类，失败于解题路径完整性。【怎么想到的】有残句。

## Boundary

以上意见是外部审核建议，不能替代原卷、官方答案、评分细则、本地 QA 和人工源文件复核。涉及题面错位或原始材料缺失的判断，必须以本地原卷和评分依据为准；不得凭本次外审意见直接补写原题材料。


---

## GPT_PRO_SECOND_RECHECK_BLOCK_RESULT

Source file: external_review\CHATGPT_PRO_RECHECK2_RESULT_20260606.md

# ChatGPT Pro Second Recheck Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `ask_6564217a-6c4d-4164-bf7c-051e3e0d7cb3`

## VERDICT

`BLOCK`

## Critical Findings

1. `2025丰台期末 第9题`

问题：正文【这道题考什么】出现可见残句：`正好暴露选言推理缺少否定另一……。`

为什么影响交付：这是学生版正文残留断句，且位置在六层第一层。该层应帮助学生快速识别考点，现在句子没有完成，直接破坏可读性。当前 QA 的 G13 可见文本完整性未覆盖这一类 `另一……。` 残句。

2. `2024东城一模 第8题`

问题：【满分作答示范】只推到 `小赵未选地理`，没有继续完成关键推理链：由小赵未选地理推出小王未选政治，再由小李或小王选政治推出小李选政治。

为什么影响交付：题目问的是哪项信息能必然推出“小李选政治”。满分答案层没有完成最终结论的推出，学生抄写会少核心推理步骤。虽然【采分点对照】里有完整链条，但“满分作答示范”本身不达标。

3. `2026丰台二模 第9题`

问题：【满分作答示范】仅写出 `D 项正确` 和两条硬约束：每人恰好喜欢两种、不喜欢一种；四人中只有一人说假话。没有说明为什么②乙喜欢珠兰花茶、④丁不喜欢白兰花茶必然为真。

为什么影响交付：该题属于真假话约束推理，满分答案需要给出约束代入后的必然结论。当前答案层更像解题提示，不能作为考生卷面答案，违反六层中“满分作答示范”必须有效的要求。

## Patch Suggestions

1. 对 `2025丰台期末 第9题`，Codex 需回到本地 Markdown 正文，补全【这道题考什么】末句。建议改为：`正好暴露选言推理缺少否定另一选言支就不能直接肯定其中一支。`  
采纳前需检查本地正文是否还有 `……。`、`由……。`、`另一……。`、`先，` 等残句模式，并重跑 visible text integrity gate。

2. 对 `2024东城一模 第8题`，Codex 需回看本地题面四个条件，确认条件①②④的链条。建议【满分作答示范】改为：`D 项正确。由“只有小徐选物理，小赵才选地理”可知，小徐选物理是小赵选地理的必要条件；小徐未选物理，可推出小赵未选地理。再由“如果小王选政治，那么小赵选地理”否定后件，推出小王未选政治。最后由“小李或者小王选政治”排除小王，必然推出小李选政治。`

3. 对 `2026丰台二模 第9题`，Codex 需回到本地答案或人工验算记录，补出真假话推理过程。至少要说明唯一假话分布下稳定推出②④，且①③不能稳定推出。若本地没有验算记录，应新增一个小脚本或人工真值表复核，避免只凭当前文字补写。

4. 建议新增 QA 规则：检查【满分作答示范】是否只停留在“题型名、硬约束、方法句”，却没有回答设问。可先对选择题答案层扫描 `D 项正确。题面同时给出`、`应选 X。` 后不足两句且没有选项结论解释的短答案。

## Language / Student-Use Findings

材料错位类问题目前看已明显收敛。`2025丰台二模 第19题第（1）问`已经恢复 AI 版权雷达材料；两条真缺源项保持中性，没有伪造题干或给出确定答案；前两轮提到的 `2024朝阳一模 第20题第（1）问`、`2024东城一模 第7题`、`2024丰台一模 第19题第（1）问`、`2026通州期末 第19题第（2）问`均已按当前正文闭合。

仍有少量学生可见表达问题。除上述阻断项外，还建议修正这些非阻断瑕疵：

- `2025朝阳期末 第19题` 三段论条目中，【满分作答示范】出现 `大题面`、`小题面`、`结语`，更像误写，应改成 `大前提`、`小前提`、`结论`。
- `2024海淀一模 第6题` 中【满分作答示范】有 `先，形成多个可选支项`，语病明显，建议改成 `先形成多个可选支项`。
- `2026石景山一模 第5题` 中【满分作答示范】引用判断时出现句号割裂：`实物和场所。适用文物保护法`，建议合并成完整判断。
- `2024朝阳一模 第20题第（2）问` 中【满分作答示范】把 `只有 A 区域古代气候温暖，A 区域古代才有可能广泛生长竹子`拆成两个句号，影响卷面自然度，建议改成一个完整必要条件判断。

整体语言已基本摆脱后台词和模板腔，但个别答案层仍有“只写方法、不写推导终点”的问题。当前不建议直接终版交付。

## Sampled Evidence

- `2025丰台二模 第19题第（1）问`，充分条件判断类，通过。材料已恢复 AI 产品、盗版资源网站、版权方 H 公司、法院建议等链条，答案能支撑“版权雷达只是治理条件之一”的评析。
- `2026海淀期末 第20题第（1）问`，缺源项，通过。正文仅保留原题材料缺失、待补，没有伪造题干或确定采分点。
- `2026朝阳二模 第19题第（1）问`，缺源项，通过。正文中性处理，没有继续给“生产性服务业”定义类确定答案。
- `2024朝阳一模 第20题第（1）问`，充分条件假言推理类，通过。焦点句已补为由否定后件推出否定前件，满分答案明确写出推理类型。
- `2024东城一模 第7题`，三段论类，通过。已补出形式有效与前提不真的区分。
- `2025丰台期末 第9题`，选言推理类，失败。考点层残句 `否定另一……。` 未清除。
- `2024东城一模 第8题`，复合假言与选言推理链，失败。满分答案未推出最终结论“小李选政治”。
- `2026丰台二模 第9题`，真假话约束推理，失败。满分答案没有展示必然推出②④的过程，学生不可直接作为卷面答案使用。

## Boundary

以上意见是外部审核建议，不能替代原卷、官方答案、评分细则、本地 QA 和人工源文件复核。涉及题面错位、答案采分、缺源修复的判断，仍必须以本地原卷、答案和评分依据为准；不得凭本次外审意见补写原题材料。


---

## GPT_PRO_THIRD_RECHECK_REVISE_RESULT

Source file: external_review\CHATGPT_PRO_RECHECK3_RESULT_20260606.md

# ChatGPT Pro Third Recheck Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `
ask_6715c63f-09aa-4065-bbdb-2ff4a4eae403
`


## VERDICT

`REVISE`

## Critical Findings

None.

三项第二次复核阻断点均已闭合，未发现需要继续判 `BLOCK` 的新问题。但正文仍有少量学生可见的材料层 OCR 残留和采分层断裂标点，建议小修后再终交。

## Patch Suggestions

1. `2025东城二模 第18题第（2）问`  
   需回到本地 Markdown 的【采分点对照】检查。当前采分点把一个充分条件推理式拆成三条 bullet，且首条引号未闭合：  
   `采用“如果有良好创新生态，就能实现创新发展`  
   建议合并成完整表述：  
   `该推理形式上采用充分条件假言推理的肯定前件式：如果有良好创新生态，就能实现创新发展；当前我国有良好创新生态；所以我国一定能实现创新发展。`  
   采纳前需核对本地答案依据，避免改动题目结论判断。

2. `2024东城一模 第7题`、`2026门头沟一模 第6题`、`2024西城一模 第11题`、`2026海淀二模 第6题`、`2024石景山一模 第7题`  
   需回本地原卷或人工校对题库核对【题目材料】。这些条目的【设问】层大多已补成可读版本，但【题目材料】仍有可见 OCR 或图表残留，例如孤立选项字母、`13/14/24/34`、尾部多余数字、`见下图`但同层没有图示说明、`以下情况`后未列出情况。建议用已核准的干净题面替换材料层，不能凭外审直接补写原题。

3. 建议新增 QA 规则  
   需在本地可见文本完整性 gate 中加入：  
   ① bullet 内有左引号但本 bullet 无右引号；  
   ② 选择题材料中出现孤立 `A.`、`C.`、`2)`、尾部单独数字；  
   ③ 出现 `见下图` 但该字段既无图片也无文字化图示说明；  
   ④ 出现 `以下情况。` 后直接进入设问语，未列举情况。

4. `2026丰台二模 第9题`  
   当前已能说明②④必然、①③不稳定。若要进一步增强学生可用性，Codex 可回本地真值表或验算脚本，把一句 `所有满足条件的安排都保留两点` 补成更明确的两行可行情形摘要。采纳前必须以本地枚举结果为准。

## Language / Student-Use Findings

整体语言已明显收敛。未见明显后台词、工程痕迹、模板腔，`本题应围绕`、`本题考查`式答案层表达未出现。三项第二次复核阻断点的答案层均已能直接抄写或改写成卷面答案。

仍建议返修的主要问题是可见层面的局部破碎：个别【题目材料】保留 OCR 选项残片，个别【采分点对照】有断裂引号和跨 bullet 句子。这些问题不影响 83 题数量和主要修复目标，但会影响学生阅读体验和终版质感。

## Sampled Evidence

1. `2025丰台期末 第9题`，选言推理类，通过。  
   【这道题考什么】已改为完整句：B 项只有 `小张或者去甘肃游学，或者去湖南游学` 为真，未否定湖南支，不能直接肯定甘肃支。此前 `否定另一……。` 残句已消失。

2. `2024东城一模 第8题`，复合假言与选言推理链，通过。  
   【满分作答示范】已完整走到最终结论：由小徐未选物理推出小赵未选地理，再推出小王未选政治，最后由小李或小王选政治推出小李选政治。

3. `2026丰台二模 第9题`，真假话约束推理，通过。  
   【满分作答示范】和【采分点对照】已说明在全部可成立情形中②乙喜欢珠兰花茶、④丁不喜欢白兰花茶稳定成立，①③只在部分情形成立，不能作为必然项。

4. `2025丰台二模 第19题第（1）问`，充分条件判断类，通过。  
   材料层已恢复 AI 产品、盗版资源网站、版权方 H 公司、法院建议、版权雷达、数字巡警、安全体检等链条，未见消费促进表格错粘。

5. `2024朝阳一模 第20题第（1）问`，充分条件假言推理类，通过。  
   焦点句已补全为由否定后件推出否定前件；【满分作答示范】明确写出推理类型和成立理由。

6. `2024东城一模 第7题`，三段论类，部分通过。  
   【怎么想到的】已补全形式有效与前提不真的区分，第二次复核阻断点闭合。但【题目材料】中的选项仍有明显 OCR 残片，需本地源证据复核后替换。

7. `2024西城二模 第18题第（1）问`，归纳推理类，通过。  
   材料层包含 352 种高粱、AT1 基因定位、转入后耐碱减弱、剪切后耐碱增强，足以支撑不完全归纳、共变法和求异法分析。

8. `2024西城一模 第19题第（2）问`，定义结构类，通过。  
   材料层给出举国体制定义句，并在答案中对应被定义项、定义联项、种差、属概念。

9. `2026海淀期末 第20题第（1）问`，缺源项，通过。  
   正文保持 `原题材料缺失，待补`，思路、示范答案和采分点均中性处理，未伪造题干或给确定答案。

10. `2026朝阳二模 第19题第（1）问`，缺源项，通过。  
    正文同样保持中性缺源处理，没有继续给生产性服务业定义类确定答案。

11. `2025东城二模 第18题第（2）问`，采分层需修。  
    【满分作答示范】完整，但【采分点对照】存在断裂引号和拆行推理式，建议返修。

## Boundary

本轮意见是外部审核建议，只依据本次提供的正文、QA 摘录和修复说明作判断，不能替代原卷、官方答案、评分细则、本地 QA、DOCX/PDF 实渲染检查和人工源文件复核。涉及题面错位、原始材料缺失、答案采分规则的判断，仍须以本地原卷和评分依据为准。


---

## GPT_PRO_FOURTH_RECHECK_REVISE_RESULT

Source file: external_review\CHATGPT_PRO_RECHECK4_RESULT_20260606.md

# ChatGPT Pro Fourth Recheck Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `
ask_b64ebf66-d6a3-4e4c-a5ef-08e380dd70f2
`


## VERDICT

`REVISE`

## Critical Findings

None.

## Patch Suggestions

1. `2026东城期末 第17题第（2）问`：材料层出现 `菜市发布老城区`，疑似 OCR 错字。Codex 需回本地原卷或人工校对题库，核对是否应为 `某市` 或其他原文。

2. `2024东城二模 第17题第（2）问`：材料层与解析层存在 `ATI / AT1` 不一致，并有 `科研院所十基地十公司`、`转化力“金山银山”` 等疑似 OCR 残留。Codex 需回本地原卷核对基因名、连接符和原句。

3. `2026顺义二模 第18题第（1）问`：材料层的 AI 分析表格仍有列流断裂：`违` 与 `反思维的确定性要求` 被拆开，中间插入 `结论二`。Codex 需回本地原卷或清洁题库重建该段材料。

4. 建议 G13 增补：`菜市发布`、`转化力`、`ATI/AT1` 同题不一致、`科研院所十基地十公司`、单字 `违` 后直接换标题、`反思维` 等模式。

## Language / Student-Use Findings

第三次 REVISE 的两项核心修复已闭合：`2025东城二模 第18题第（2）问` 采分链已合并，未见断裂引号；第三次列出的材料层 OCR 碎片条目已明显清理。两条缺源项仍保持中性，没有伪造题干或确定答案。

答案层整体可用，未见明显后台词、模板腔、`本题应围绕` 式表达或采分层照搬。主要剩余问题集中在少数材料层 OCR/列流残留，G13 虽报告 `visible_text_break_hits: 0`，但仍未覆盖上述语义型 OCR 残片。

## Sampled Evidence

- `2025东城二模 第18题第（2）问`：通过。采分点已完整写出充分条件假言推理链。
- `2024东城一模 第7题`、`2026门头沟一模 第6题`、`2024西城一模 第11题`、`2026海淀二模 第6题`、`2024石景山一模 第7题`：第三次点名 OCR 材料层通过。
- `2026海淀期末 第20题第（1）问`、`2026朝阳二模 第19题第（1）问`：通过。缺源处理中性。
- `2024东城一模 第8题`、`2026丰台二模 第9题`：通过。满分答案已完成关键推理链。
- `2026东城期末 第17题第（2）问`：失败于疑似 OCR 字 `菜市`。
- `2024东城二模 第17题第（2）问`：失败于 `ATI/AT1` 不一致及材料层 OCR 残留。
- `2026顺义二模 第18题第（1）问`：失败于材料层表格列流断裂。

## Boundary

以上是外部审核建议，不能替代原卷、官方答案、评分细则、本地 QA、DOCX/PDF 实渲染检查和人工源文件复核。涉及题面错位、OCR 修复和采分规则的判断，仍须以本地原始证据为准。


---

## GPT_PRO_FIFTH_RECHECK_REVISE_RESULT

Source file: external_review\CHATGPT_PRO_RECHECK5_RESULT_20260606.md

# ChatGPT Pro Fifth Recheck Result

Run time: 2026-06-06

Lane: `pro-cli` through live ChatGPT web session.

Model: `gpt-5-5-pro`

Reasoning: `extended`

Job id: `
ask_31abdeee-3d4f-4a49-9840-419bd5d75779
`


## VERDICT

`REVISE`

## Critical Findings

None.

第四次复核的三项 `REVISE` 目标已闭合，未发现需要判 `BLOCK` 的新问题。但本轮仍抽到少量学生可见的断裂标点和生产过程措辞，建议小修后再终交。

## Patch Suggestions

1. `2026海淀一模 第17题第（1）问`  
   需回本地原卷或人工校对题库核对【题目材料】。当前正文两处出现 `为提高调研活动的科学, 性,提出具体可行的建议` 一类断裂，疑似应为 `科学性，提出具体可行的建议`。建议修正文内两处同源材料，并把 G13 增补为可识别 `科学,\n性`、`科学, 性` 这类中文词内断裂模式。

2. `2026石景山一模 第5题`  
   需回本地原卷核对选项 C 标点。当前【题目材料】和【设问】中均有 `犯了定义过窄”的错误`，左引号缺失，疑似应为 `犯了“定义过窄”的错误`。采纳前以本地题源为准，并建议 G13 增补中文术语引号不成对模式。

3. `2026海淀期末 第20题第（1）问`、`2026朝阳二模 第19题第（1）问`  
   两条缺源项处理方向正确，没有伪造题干或确定答案。但【满分作答示范】中的 `待补入原始题面和细则后补齐`、【采分点对照】中的 `采分点暂不进入学生版；待人工补源后重建` 仍偏生产过程措辞。建议改成更中性的学生可见表达，例如：`原题材料缺失，暂不提供示范答案；补入原卷题面后再完善。`、`原始题面缺失，暂不列采分点；补入原卷材料后再补充。` 采纳前需与 defect ledger 的两条 `needs_manual_source` 保持一致。

4. 标题页短语 `终极返修版`  
   若定位为学生终交版，建议改为 `终极版` 或 `推理题型树`。这不是来源问题，但能减少返修过程痕迹。

## Language / Student-Use Findings

整体语言已明显接近可交付状态。未见 `本题应围绕`、`本题考查` 式模板答案，也未见答案层只写方法、不走到结论的明显问题。答案层和采分层已经分开，前几轮提到的关键推理链均已补齐。

仍需小修的是三类可见问题：一是个别材料层有词内断裂标点，二是个别选项引号不成对，三是两条缺源项虽然中性，但仍带有 `学生版`、`人工补源`、`细则`、`重建` 等编辑流程感词语。它们不影响 83 题数量、分类结构和主要修复目标，但会影响终版质感。

## Sampled Evidence

1. `2026东城期末 第17题第（2）问`，通过。  
   第四次复核指出的 `菜市发布老城区` 已修为 `某市发布老城区`。同题在充分条件、三段论、矛盾律三个相关条目中材料一致，未见 `菜市发布` 残留。

2. `2024东城二模 第17题第（2）问`，通过。  
   材料层现为 `AT1` 与 `GS3`，未见 `ATI / AT1` 混用。`科研院所+基地+公司`、`龙头企业+基地+农户`、`转化为“金山银山”` 已清理为正常表达，AT1/GS3 因果与类比链条可读。

3. `2026顺义二模 第18题第（1）问`，通过。  
   AI 分析材料已由断裂表格重建为两段清晰结论。未见 `违` 单字断裂、`反思维` 残留或列流错位。

4. `2026顺义二模 第18题第（1）问` 答案层，通过。  
   【满分作答示范】同时覆盖 AI 结论一和结论二：结论一指出车企前后判断冲突，并修正为矛盾律的一致性要求；结论二指出车企回避系统缺陷，不符合科学思维追求认识客观性的要求。不是只处理矛盾律部分。

5. G13，通过但覆盖仍可扩展。  
   `QA_GATES_V24_20260606.json` 报告 `visible_text_break_hits: []`，`G13_visible_text_integrity: true`；`QA_REPORT` 报告 visible text break hits 为 0；`CHANGELOG` 和 `FINAL_ACCEPTANCE_REPORT` 说明 G13 已增补 `菜市发布`、`转化力`、`ATI`、`科研院所十基地十公司`、`龙头企业十基地十农户`、拆分 `违/结论`、`反思维` 等模式。外审抽样仍发现 `科学, 性` 和 `定义过窄”` 这类未覆盖模式，所以建议继续扩展，不建议仅凭 G13 零命中直接终交。

6. `2026顺义一模 第19题第（1）问`，通过。  
   材料已呈现完整三段推论，答案能区分三段论形式有效与大前提不真，初始缺失推论问题闭合。

7. `2024西城二模 第18题第（1）问`，通过。  
   材料包含 352 种高粱样本、AT1 基因定位、转入后耐碱减弱、剪切后耐碱增强，足以支撑不完全归纳、共变法和求异法分析。

8. `2024西城一模 第19题第（2）问`，通过。  
   材料层给出举国体制定义句，答案能对应被定义项、定义联项、种差、属概念，前期定义材料缺失问题闭合。

9. `2025丰台二模 第19题第（1）问`，通过。  
   材料已恢复 AI 产品、盗版资源网站、版权方 H 公司、法院建议、版权雷达、数字巡警、安全体检等链条，未见消费促进表格错粘。

10. `2026海淀期末 第20题第（1）问`、`2026朝阳二模 第19题第（1）问`，部分通过。  
   正文保持缺源中性处理，没有伪造题干或确定答案。需小修的是可见措辞，避免 `学生版`、`人工补源`、`细则` 这类过程词。

11. `2024东城一模 第8题`，通过。  
   【满分作答示范】已完整走到最终结论：小徐未选物理，推出小赵未选地理，再推出小王未选政治，最后由小李或小王选政治推出小李选政治。

12. `2026丰台二模 第9题`，通过。  
   答案说明在所有可成立情形中②乙喜欢珠兰花茶、④丁不喜欢白兰花茶稳定成立，①③不稳定，已满足答案层完整性要求。

13. `2026海淀一模 第17题第（1）问`，失败于可见材料断裂。  
   同源材料中 `科学, 性` 影响阅读质感，建议本地源证据复核后清理。

14. `2026石景山一模 第5题`，失败于断裂引号。  
   `犯了定义过窄”的错误` 有明显左引号缺失风险，需本地题源复核后修正。

## Boundary

以上意见是外部审核建议，不能替代原卷、官方答案、评分细则、本地 QA、DOCX/PDF 实渲染检查和人工源文件复核。涉及题面错位、OCR 修复、缺源处理和采分规则的判断，仍须以本地原始证据为准；不得凭本次外审意见补写原题材料。


---

## FINAL_ACCEPTANCE_REPORT

Source file: FINAL_ACCEPTANCE_REPORT.md

# FINAL ACCEPTANCE REPORT

## Deliverables

- Markdown: `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.md`
- DOCX: `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.docx`
- PDF: `delivery/选必三逻辑与思维_推理宝典_终极版_20260606.pdf`
- QA report: `qa/QA_REPORT_V24_20260606.md`
- Defect ledger: `qa/DEFECT_LEDGER_V24_20260606.csv`
- Changelog: `qa/CHANGELOG_V24_20260606.md`

## What Changed

- Reworked v23 into the Claude prompt schema: `这道题考什么 / 题目材料 / 设问 / 怎么想到的 / 满分作答示范 / 采分点对照`.
- Removed backstage wording from the student-facing book.
- Regenerated the answer layer so it is no longer a copy of the采分层 or the thinking layer.
- Collapsed 62 repeated method blocks into 8 major-class `本类怎么做` blocks and 8 `本类常见坑` blocks.
- Added an updated contents section and final `考场速查`.
- Patched GPT Pro material-layer findings: restored the missing inference in `2026顺义一模 第19题第（1）问`, restored the 352-sample/AT1 table substance in `2024西城二模 第18题第（1）问`, and restored the definition sentence/structure hints in `2024西城一模 第19题第（2）问`.
- Neutralized the answer, thinking, and rubric fields for the two true missing-source entries instead of presenting determinate answers without original materials.
- Rewrote `2025海淀一模 第21题第（1）问` to avoid the disputed `国内大循环` premise while keeping a valid 不相容选言推理 construction.
- Patched GPT Pro recheck findings: restored the correct AI版权雷达材料 for `2025丰台二模 第19题第（1）问`, completed the visible residual sentence in `2024朝阳一模 第20题第（1）问`, completed the thinking sentence in `2024东城一模 第7题`, merged the broken quote bullet in `2024丰台一模 第19题第（1）问`, and repaired the wording in `2026通州期末 第19题第（2）问`.
- Patched GPT Pro second-recheck findings: completed the `2025丰台期末 第9题` focus sentence, expanded `2024东城一模 第8题` to the full chain ending in `小李选政治`, and added a truth-table-backed explanation for why `2026丰台二模 第9题` must choose ②④.
- Cleaned second-recheck language issues in `2025朝阳期末 第19题`, `2024海淀一模 第6题`, `2026石景山一模 第5题`, and `2024朝阳一模 第20题第（2）问`.
- Patched GPT Pro third-recheck `REVISE` findings: merged the broken `2025东城二模 第18题第（2）问` rubric chain; replaced OCR-fragment material layers with clean question text for `2024东城一模 第7题`, `2026门头沟一模 第6题`, `2024西城一模 第11题`, `2026海淀二模 第6题`, `2024石景山一模 第7题`, plus additional G13-caught fragments in `2024朝阳二模 第7题`, `2026海淀二模 第7题`, `2024海淀一模 第6题`, and `2024东城一模 第6题`.
- Expanded G13 to catch unclosed quote bullets, isolated option/OCR fragments, raw `A.12`-style option pairs, unrendered figure references, and missing listed cases after `以下情况。`.
- Patched GPT Pro fourth-recheck `REVISE` findings: corrected the `2026东城期末 第17题第（2）问` material from OCR `菜市` to source-supported `某市`; cleaned the `2024东城二模 第17题第（2）问` AT1/GS3 material and OCR `十/力` errors; rebuilt the `2026顺义二模 第18题第（1）问` AI analysis material to remove column-flow breaks and expanded the answer layer to cover both AI conclusions.
- Expanded G13 again for `菜市发布`, `转化力`, `ATI`, `科研院所十基地十公司`, `龙头企业十基地十农户`, split `违/结论` flows, and stray `反思维`.
- Patched GPT Pro fifth-recheck `REVISE` findings: cleaned the `2026海淀一模 第17题` visible scientificity line break, repaired the missing left quote in `2026石景山一模 第5题` option C, neutralized missing-source process wording, and removed old revision-title wording from the title page.
- Expanded G13 for scientificity line breaks, unpaired definition-narrowness quote tails, missing-source process wording, and old revision-title residue.

## Verification

- G1-G13 local gates: PASS.
- Source DOCX input snapshot: PASS; old source labels each count 83.
- Entries: 83/83.
- Major classes: 8.
- Subtypes: 62.
- Field counts in Markdown: 83 each for all 6 required per-entry fields.
- Anti-copy gate: 0 violations.
- Backstage word scan: 0 hits.
- Page/footer/OCR-dot residue scan: 0 hits.
- Word export PDF: PASS.
- PDF QA: 99 pages, 0 blank pages, all 6 required field labels count 83, forbidden backend/path hits 0.
- Visual QA: all-page contact sheet plus first/middle/final page samples checked.
- Extra DOCX/PDF residue scan: 本题应围绕/本题考查/高三政治/高三年级/成沟/化元/消赞/环搅/高梁/从高中提取/扫描水印/评分细则/变通说明 all 0.
- Orphan punctuation bullet scan: 0.
- Material integrity gate: 0 issues after targeted repair.
- Visible text integrity gate: 0 issues after targeted repair.
- Claude Code cowork recheck: ACCEPT after prior findings were patched.
- GPT Pro review: initial BLOCK findings, first-recheck BLOCK findings, and second-recheck BLOCK findings have all been locally repaired.
- GPT Pro third recheck: REVISE with no Critical Findings; all listed local repair items have been patched and G1-G13 rerun.
- GPT Pro fourth recheck: REVISE with no Critical Findings; all listed local repair items have been patched and G1-G13 rerun.
- GPT Pro fifth recheck: REVISE with no Critical Findings; all listed local repair items have been patched and G1-G13 rerun.
- GPT Pro sixth recheck: pending.
- Claude Chat Opus application/web lane: pending; Claude Code cowork ACCEPT does not substitute for this required lane.

## Residual Boundary

- `2026海淀期末 第20题第（1）问（主观题）` remains in the defect ledger as `needs_manual_source`: the input material block appears to be answer/example text rather than the original question material. The final book does not fabricate a replacement question stem.
- `2026朝阳二模 第19题第（1）问（主观题）` remains in the defect ledger as `needs_manual_source`: the local input contains scoring rules and variation notes, not the original 材料一. The final book does not fabricate a replacement question stem.
- The two missing-source entries are intentionally neutral in the student-facing body until original materials are provided.
- Final closure still requires GPT Pro sixth recheck and the user-required Claude Chat Opus lane.

LOCAL_PASS_WITH_2_MANUAL_SOURCE_DEFECTS_PENDING_GPT_RECHECK6_AND_CLAUDE_CHAT


---

## QA_REPORT

Source file: qa\QA_REPORT_V24_20260606.md

# QA REPORT V24

- Verdict: PASS
- Entries: 83
- Major classes: 8
- Subtypes: 62
- Type-level method blocks: 8
- Type-level pit blocks: 8
- Defect ledger rows: 2
- Answer-vs-rubric copy violations: 0
- Answer-vs-thinking copy violations: 0
- Banned answer templates: 0
- Half-width score parentheses: 0
- OCR/page header residue: {'高三政治': 0, '成沟': 0, '化元': 0, '消赞': 0, '环搅': 0, '高梁': 0, '从高中提取': 0, '扫描全能王': 0, '3亿人都在用': 0, '思想政治 第': 0, '高三年级(思想政治)': 0, '高三年级（思想政治）': 0, '评分细则': 0, '变通说明': 0}
- Focus truncation hits: 0
- Type-name omissions in full-mark answers: 0
- Material integrity issues: 0
- Visible text break hits: 0

## Gates

- G1_count: PASS
- G2_structure: PASS
- G3_anti_copy: PASS
- G3b_answer_vs_thinking: PASS
- G4_anti_backstage: PASS
- G5_anti_footer_ocr_noise: PASS
- G6_punctuation_spot: PASS
- G7_toc: PASS
- G8_logic_spot: PASS
- G9_terms: PASS
- G10_focus_sentence_complete: PASS
- G11_type_answer_label: PASS
- G12_material_integrity: PASS
- G13_visible_text_integrity: PASS

## Notes

- V24 keeps all 83 source anchors and changes the student-facing schema.
- The old repeated per-subtype method blocks were collapsed into 8 major-class method/pit blocks.
- G3 checks 满分作答示范 vs 采分点对照; G3b checks 满分作答示范 vs 怎么想到的 and bans template openings.
- G12 checks targeted material completeness, neutral handling for true missing-source entries, and the repaired 2025海淀一模推理 construction.
- G13 checks visible residual text breaks such as unfinished ellipses, orphan quote bullets, isolated option/OCR fragments, unrendered figure references, and known grammar fractures from external review.
- Suspected source-material misalignment is kept out of the student-facing body and recorded in the defect ledger.

---

## QA_GATES_JSON

Source file: qa\QA_GATES_V24_20260606.json

{
  "entries": 83,
  "major_count": 8,
  "subtype_count": 62,
  "method_blocks": 8,
  "pit_blocks": 8,
  "toc_major": 8,
  "toc_subtype": 62,
  "defect_count": 2,
  "defects": [
    {
      "index": "5",
      "anchor": "2026海淀期末 第20题第（1）问（主观题）",
      "severity": "needs_manual_source",
      "reason": "题目材料栏出现答案/示例/评分语特征，不能当作完整真题材料。",
      "suggested_action": "补入原卷题面后再替换本条题目材料；当前不伪造题干。"
    },
    {
      "index": "62",
      "anchor": "2026朝阳二模 第19题第（1）问（主观题）",
      "severity": "needs_manual_source",
      "reason": "题目材料栏粘贴的是评分细则和变通说明，缺少界定“生产性服务业”的材料一原文。",
      "suggested_action": "补入2026朝阳二模原卷材料一后再替换本条题目材料；当前不伪造题干。"
    }
  ],
  "per_entry_missing": [],
  "copy_violations": [],
  "answer_thinking_violations": [],
  "template_answer_hits": [],
  "focus_truncation_hits": [],
  "type_answer_missing": [],
  "material_integrity_issues": [],
  "visible_text_break_hits": [],
  "answer_template_total": 0,
  "backstage_hits": {
    "回源": 0,
    "底座": 0,
    "汇编": 0,
    "答案落点": 0,
    "学生化": 0,
    "细则要点": 0,
    "材料触发点": 0,
    "旧学生化": 0,
    "后台": 0,
    "供训练使用": 0,
    "材料栏": 0,
    "不作为完整真题": 0
  },
  "footer_hits": {
    "footer_pattern_1": 0,
    "footer_pattern_2": 0
  },
  "ascii_dot_residue": 0,
  "ocr_noise_hits": {
    "高三政治": 0,
    "成沟": 0,
    "化元": 0,
    "消赞": 0,
    "环搅": 0,
    "高梁": 0,
    "从高中提取": 0,
    "扫描全能王": 0,
    "3亿人都在用": 0,
    "思想政治 第": 0,
    "高三年级(思想政治)": 0,
    "高三年级（思想政治）": 0,
    "评分细则": 0,
    "变通说明": 0
  },
  "half_score_parentheses": 0,
  "full_score_parentheses": 140,
  "blank_placeholder_issues": 0,
  "orphan_rubric_punctuation": 0,
  "term_hits": {
    "充分条件命题": 0,
    "必要条件命题": 0,
    "形式逻辑推断法": 0,
    "逆条件推理法": 0,
    "推理路线图": 0
  },
  "line_label_counts": {
    "【这道题考什么】": 83,
    "【题目材料】": 83,
    "【设问】": 83,
    "【怎么想到的】": 83,
    "【满分作答示范】": 83,
    "【采分点对照】": 83
  },
  "gates": {
    "G1_count": true,
    "G2_structure": true,
    "G3_anti_copy": true,
    "G3b_answer_vs_thinking": true,
    "G4_anti_backstage": true,
    "G5_anti_footer_ocr_noise": true,
    "G6_punctuation_spot": true,
    "G7_toc": true,
    "G8_logic_spot": true,
    "G9_terms": true,
    "G10_focus_sentence_complete": true,
    "G11_type_answer_label": true,
    "G12_material_integrity": true,
    "G13_visible_text_integrity": true
  },
  "pass": true
}

---

## PDF_RENDER_QA_JSON

Source file: qa\PDF_RENDER_QA_V24_20260606.json

{
  "pdf": "delivery\\选必三逻辑与思维_推理宝典_终极版_20260606.pdf",
  "page_count": 99,
  "marker_counts": {
    "【这道题考什么】": 83,
    "【题目材料】": 83,
    "【设问】": 83,
    "【怎么想到的】": 83,
    "【满分作答示范】": 83,
    "【采分点对照】": 83
  },
  "forbidden_counts": {
    "回源": 0,
    "底座": 0,
    "汇编": 0,
    "答案落点": 0,
    "学生化": 0,
    "细则要点": 0,
    "材料触发点": 0,
    "/Users": 0,
    "C:\\": 0,
    "source_extracted": 0,
    "OCR": 0,
    "**• **": 0,
    "本题应围绕": 0,
    "本题考查": 0,
    "本题应": 0,
    "高三政治": 0,
    "成沟": 0,
    "供训练使用": 0,
    "材料栏": 0,
    "不作为完整真题": 0
  },
  "blank_pages": [],
  "min_text_chars_on_page": 179,
  "min_nonwhite_ratio": 0.03853,
  "sample_outputs": [
    "qa\\pdf_render_qa\\sample_page_001.png",
    "qa\\pdf_render_qa\\sample_page_049.png",
    "qa\\pdf_render_qa\\sample_page_099.png"
  ],
  "contact_sheet": "qa\\pdf_render_qa\\all_pages_contact_sheet.png",
  "pass": true,
  "page_stats": [
    {
      "page": 1,
      "text_chars": 179,
      "nonwhite_ratio": 0.03853
    },
    {
      "page": 2,
      "text_chars": 855,
      "nonwhite_ratio": 0.2897
    },
    {
      "page": 3,
      "text_chars": 932,
      "nonwhite_ratio": 0.37677
    },
    {
      "page": 4,
      "text_chars": 1093,
      "nonwhite_ratio": 0.36958
    },
    {
      "page": 5,
      "text_chars": 875,
      "nonwhite_ratio": 0.37854
    },
    {
      "page": 6,
      "text_chars": 792,
      "nonwhite_ratio": 0.19279
    },
    {
      "page": 7,
      "text_chars": 882,
      "nonwhite_ratio": 0.37831
    },
    {
      "page": 8,
      "text_chars": 1049,
      "nonwhite_ratio": 0.31388
    },
    {
      "page": 9,
      "text_chars": 968,
      "nonwhite_ratio": 0.48784
    },
    {
      "page": 10,
      "text_chars": 1037,
      "nonwhite_ratio": 0.33739
    },
    {
      "page": 11,
      "text_chars": 791,
      "nonwhite_ratio": 0.18909
    },
    {
      "page": 12,
      "text_chars": 830,
      "nonwhite_ratio": 0.39562
    },
    {
      "page": 13,
      "text_chars": 799,
      "nonwhite_ratio": 0.52614
    },
    {
      "page": 14,
      "text_chars": 1071,
      "nonwhite_ratio": 0.41336
    },
    {
      "page": 15,
      "text_chars": 993,
      "nonwhite_ratio": 0.39202
    },
    {
      "page": 16,
      "text_chars": 1043,
      "nonwhite_ratio": 0.27719
    },
    {
      "page": 17,
      "text_chars": 922,
      "nonwhite_ratio": 0.19481
    },
    {
      "page": 18,
      "text_chars": 999,
      "nonwhite_ratio": 0.25008
    },
    {
      "page": 19,
      "text_chars": 994,
      "nonwhite_ratio": 0.25528
    },
    {
      "page": 20,
      "text_chars": 782,
      "nonwhite_ratio": 0.28696
    },
    {
      "page": 21,
      "text_chars": 982,
      "nonwhite_ratio": 0.24973
    },
    {
      "page": 22,
      "text_chars": 829,
      "nonwhite_ratio": 0.14541
    },
    {
      "page": 23,
      "text_chars": 958,
      "nonwhite_ratio": 0.32646
    },
    {
      "page": 24,
      "text_chars": 923,
      "nonwhite_ratio": 0.26102
    },
    {
      "page": 25,
      "text_chars": 754,
      "nonwhite_ratio": 0.12791
    },
    {
      "page": 26,
      "text_chars": 1106,
      "nonwhite_ratio": 0.40191
    },
    {
      "page": 27,
      "text_chars": 642,
      "nonwhite_ratio": 0.57806
    },
    {
      "page": 28,
      "text_chars": 947,
      "nonwhite_ratio": 0.32839
    },
    {
      "page": 29,
      "text_chars": 944,
      "nonwhite_ratio": 0.28617
    },
    {
      "page": 30,
      "text_chars": 908,
      "nonwhite_ratio": 0.22278
    },
    {
      "page": 31,
      "text_chars": 1051,
      "nonwhite_ratio": 0.35195
    },
    {
      "page": 32,
      "text_chars": 999,
      "nonwhite_ratio": 0.30575
    },
    {
      "page": 33,
      "text_chars": 940,
      "nonwhite_ratio": 0.2449
    },
    {
      "page": 34,
      "text_chars": 1090,
      "nonwhite_ratio": 0.3795
    },
    {
      "page": 35,
      "text_chars": 1071,
      "nonwhite_ratio": 0.3934
    },
    {
      "page": 36,
      "text_chars": 874,
      "nonwhite_ratio": 0.36345
    },
    {
      "page": 37,
      "text_chars": 786,
      "nonwhite_ratio": 0.27804
    },
    {
      "page": 38,
      "text_chars": 761,
      "nonwhite_ratio": 0.17707
    },
    {
      "page": 39,
      "text_chars": 710,
      "nonwhite_ratio": 0.19115
    },
    {
      "page": 40,
      "text_chars": 936,
      "nonwhite_ratio": 0.26444
    },
    {
      "page": 41,
      "text_chars": 951,
      "nonwhite_ratio": 0.3034
    },
    {
      "page": 42,
      "text_chars": 954,
      "nonwhite_ratio": 0.31266
    },
    {
      "page": 43,
      "text_chars": 937,
      "nonwhite_ratio": 0.16252
    },
    {
      "page": 44,
      "text_chars": 1061,
      "nonwhite_ratio": 0.41046
    },
    {
      "page": 45,
      "text_chars": 1075,
      "nonwhite_ratio": 0.34942
    },
    {
      "page": 46,
      "text_chars": 1020,
      "nonwhite_ratio": 0.4713
    },
    {
      "page": 47,
      "text_chars": 900,
      "nonwhite_ratio": 0.36162
    },
    {
      "page": 48,
      "text_chars": 799,
      "nonwhite_ratio": 0.13832
    },
    {
      "page": 49,
      "text_chars": 961,
      "nonwhite_ratio": 0.24674
    },
    {
      "page": 50,
      "text_chars": 823,
      "nonwhite_ratio": 0.39189
    },
    {
      "page": 51,
      "text_chars": 1063,
      "nonwhite_ratio": 0.29052
    },
    {
      "page": 52,
      "text_chars": 964,
      "nonwhite_ratio": 0.25065
    },
    {
      "page": 53,
      "text_chars": 911,
      "nonwhite_ratio": 0.31991
    },
    {
      "page": 54,
      "text_chars": 923,
      "nonwhite_ratio": 0.26403
    },
    {
      "page": 55,
      "text_chars": 1103,
      "nonwhite_ratio": 0.39736
    },
    {
      "page": 56,
      "text_chars": 792,
      "nonwhite_ratio": 0.38194
    },
    {
      "page": 57,
      "text_chars": 949,
      "nonwhite_ratio": 0.36656
    },
    {
      "page": 58,
      "text_chars": 1002,
      "nonwhite_ratio": 0.32834
    },
    {
      "page": 59,
      "text_chars": 943,
      "nonwhite_ratio": 0.29403
    },
    {
      "page": 60,
      "text_chars": 984,
      "nonwhite_ratio": 0.27886
    },
    {
      "page": 61,
      "text_chars": 794,
      "nonwhite_ratio": 0.20196
    },
    {
      "page": 62,
      "text_chars": 927,
      "nonwhite_ratio": 0.26759
    },
    {
      "page": 63,
      "text_chars": 995,
      "nonwhite_ratio": 0.2561
    },
    {
      "page": 64,
      "text_chars": 1015,
      "nonwhite_ratio": 0.42686
    },
    {
      "page": 65,
      "text_chars": 835,
      "nonwhite_ratio": 0.20842
    },
    {
      "page": 66,
      "text_chars": 686,
      "nonwhite_ratio": 0.37597
    },
    {
      "page": 67,
      "text_chars": 1078,
      "nonwhite_ratio": 0.36543
    },
    {
      "page": 68,
      "text_chars": 923,
      "nonwhite_ratio": 0.24054
    },
    {
      "page": 69,
      "text_chars": 941,
      "nonwhite_ratio": 0.26593
    },
    {
      "page": 70,
      "text_chars": 1105,
      "nonwhite_ratio": 0.44972
    },
    {
      "page": 71,
      "text_chars": 1202,
      "nonwhite_ratio": 0.36477
    },
    {
      "page": 72,
      "text_chars": 754,
      "nonwhite_ratio": 0.24546
    },
    {
      "page": 73,
      "text_chars": 815,
      "nonwhite_ratio": 0.24071
    },
    {
      "page": 74,
      "text_chars": 723,
      "nonwhite_ratio": 0.12237
    },
    {
      "page": 75,
      "text_chars": 764,
      "nonwhite_ratio": 0.39241
    },
    {
      "page": 76,
      "text_chars": 996,
      "nonwhite_ratio": 0.35734
    },
    {
      "page": 77,
      "text_chars": 977,
      "nonwhite_ratio": 0.3065
    },
    {
      "page": 78,
      "text_chars": 910,
      "nonwhite_ratio": 0.25474
    },
    {
      "page": 79,
      "text_chars": 823,
      "nonwhite_ratio": 0.2233
    },
    {
      "page": 80,
      "text_chars": 785,
      "nonwhite_ratio": 0.1647
    },
    {
      "page": 81,
      "text_chars": 839,
      "nonwhite_ratio": 0.28734
    },
    {
      "page": 82,
      "text_chars": 786,
      "nonwhite_ratio": 0.23042
    },
    {
      "page": 83,
      "text_chars": 852,
      "nonwhite_ratio": 0.37132
    },
    {
      "page": 84,
      "text_chars": 1054,
      "nonwhite_ratio": 0.29221
    },
    {
      "page": 85,
      "text_chars": 850,
      "nonwhite_ratio": 0.14597
    },
    {
      "page": 86,
      "text_chars": 1022,
      "nonwhite_ratio": 0.3837
    },
    {
      "page": 87,
      "text_chars": 898,
      "nonwhite_ratio": 0.29044
    },
    {
      "page": 88,
      "text_chars": 937,
      "nonwhite_ratio": 0.218
    },
    {
      "page": 89,
      "text_chars": 941,
      "nonwhite_ratio": 0.19288
    },
    {
      "page": 90,
      "text_chars": 1115,
      "nonwhite_ratio": 0.28088
    },
    {
      "page": 91,
      "text_chars": 845,
      "nonwhite_ratio": 0.14562
    },
    {
      "page": 92,
      "text_chars": 945,
      "nonwhite_ratio": 0.34612
    },
    {
      "page": 93,
      "text_chars": 930,
      "nonwhite_ratio": 0.22088
    },
    {
      "page": 94,
      "text_chars": 854,
      "nonwhite_ratio": 0.32599
    },
    {
      "page": 95,
      "text_chars": 930,
      "nonwhite_ratio": 0.15577
    },
    {
      "page": 96,
      "text_chars": 616,
      "nonwhite_ratio": 0.34799
    },
    {
      "page": 97,
      "text_chars": 868,
      "nonwhite_ratio": 0.20908
    },
    {
      "page": 98,
      "text_chars": 1169,
      "nonwhite_ratio": 0.39144
    },
    {
      "page": 99,
      "text_chars": 604,
      "nonwhite_ratio": 0.10084
    }
  ]
}

---

## DEFECT_LEDGER_CSV

Source file: qa\DEFECT_LEDGER_V24_20260606.csv

index,anchor,severity,reason,suggested_action
5,2026海淀期末 第20题第（1）问（主观题）,needs_manual_source,题目材料栏出现答案/示例/评分语特征，不能当作完整真题材料。,补入原卷题面后再替换本条题目材料；当前不伪造题干。
62,2026朝阳二模 第19题第（1）问（主观题）,needs_manual_source,题目材料栏粘贴的是评分细则和变通说明，缺少界定“生产性服务业”的材料一原文。,补入2026朝阳二模原卷材料一后再替换本条题目材料；当前不伪造题干。


---

## CHANGELOG

Source file: qa\CHANGELOG_V24_20260606.md

# CHANGELOG V24

- Rewrote front matter as a student-facing usage guide.
- Replaced old labels with Claude-prompt schema: 这道题考什么 / 题目材料 / 设问 / 怎么想到的 / 满分作答示范 / 采分点对照.
- Regenerated the answer layer from scoring substance instead of the thinking layer; banned 本题应围绕 / 本题考查 / 本题应 templates.
- Added G3b: 满分作答示范 vs 怎么想到的 exact/normalized/LCS guard.
- Moved rubric substance into 采分点对照.
- Collapsed 62 repeated 做题方法 blocks into 8 major-class 本类怎么做 blocks and 8 本类常见坑 blocks.
- Added 目录 and 考场速查.
- Cleaned obvious OCR dot residue, page-footer patterns, 高三政治 page headers, 成沟 OCR error, and half-width score parentheses in question material.
- Applied audit-report OCR fixes for 化元/消赞/环搅/高梁/从高中提取 and scanner-watermark residue.
- Recovered source material for 2026顺义一模第4题, 2026朝阳一模第5题, and 2026朝阳一模第17(1) from verified local question text.
- Added 2026朝阳二模第19(1) to the defect ledger because the local source only contains scoring rules, not 材料一.
- Patched real Claude Code cowork findings: fixed the 2024.11朝阳期中第18题类比推理 answer-layer mismatch and added explicit type naming for 2024朝阳一模第20(1).
- Added G11 to catch full-mark answers that omit the reasoning type when the question explicitly asks for 推理类型.
- Recovered material-layer gaps flagged by GPT Pro for 2026顺义一模第19(1), 2024西城二模第18(1), and 2024西城一模第19(2).
- Neutralized the answer/thinking/rubric fields for the two true missing-source entries so the student-facing body no longer presents determined answers without original material.
- Rewrote 2025海淀一模第21(1) to a cleaner 不相容选言推理 construction and removed the disputed 国内大循环 premise.
- Added G12 material-integrity gate for the above targeted repairs.
- Patched GPT Pro recheck findings: recovered 2025丰台二模第19(1) original AI版权雷达材料, completed 2024朝阳一模第20(1) focus sentence, completed 2024东城一模第7题 thinking sentence, merged 2024丰台一模第19(1) broken rubric bullet, and fixed 2026通州期末第19(2) wording.
- Added G13 visible-text-integrity gate for unfinished ellipses, orphan quote bullets, and known grammar fractures.
- Rebuilt 2024丰台一模第19(1) visible blanks as 划线①/划线② standard underlines.
- Moved the 2026海淀期末第20(1) source-misalignment detail out of the body; the body now keeps only a neutral missing-source note.
- Added defect ledger for entries that cannot be safely auto-repaired.
- Patched GPT Pro second-recheck blockers: completed the 2025丰台期末第9题 focus sentence, expanded 2024东城一模第8题 to the final 小李选政治 conclusion, and added a truth-table-backed explanation for 2026丰台二模第9题 selecting ②④.
- Cleaned second-recheck wording issues in 2025朝阳期末第19题, 2024海淀一模第6题, 2026石景山一模第5题, and 2024朝阳一模第20(2).
- Patched GPT Pro third-recheck REVISE findings: merged 2025东城二模第18(2) broken rubric bullets and replaced OCR-fragment material layers with clean question text for 2024东城一模第7题, 2026门头沟一模第6题, 2024西城一模第11题, 2026海淀二模第6题, 2024石景山一模第7题, 2024朝阳二模第7题, 2026海淀二模第7题, 2024海淀一模第6题, and 2024东城一模第6题.
- Expanded G13 visible-text gate for unclosed quote bullets, isolated option/OCR fragments, raw A.12-style option pairs, unrendered figure references, and missing listed cases after 以下情况。
- Patched GPT Pro fourth-recheck REVISE findings: corrected 2026东城期末第17(2) material OCR to 某市, cleaned 2024东城二模第17(2) AT1/GS3 material and OCR 十/力 errors, rebuilt 2026顺义二模第18(1) AI analysis material, and expanded that answer layer to cover both AI conclusions.
- Expanded G13 again for 菜市发布, 转化力, ATI, OCR plus-as-ten strings, split 违/结论 flows, and stray 反思维。
- Patched GPT Pro fifth-recheck REVISE findings: cleaned the 2026海淀一模第17题 visible scientificity line break, repaired the missing left quote in 2026石景山一模第5题 option C, neutralized missing-source process wording, and removed old revision-title wording from the title page.
- Expanded G13 for scientificity line breaks, unpaired definition-narrowness quote tails, missing-source process wording, and old revision-title residue.

---

## FINAL_MARKDOWN_ARTIFACT

Source file: delivery\选必三逻辑与思维_推理宝典_终极版_20260606.md

# 2026北京高考政治选必三《逻辑与思维》推理宝典

推理题型树·终极版｜2026-06-06

飞哥正志讲堂

## 使用方法

这本书按推理类型整理。先看本类怎么做，再看同类题：用“这道题考什么”快速认类型，用“怎么想到的”学转弯路径，用“满分作答示范”练卷面表达，最后用“采分点对照”自检有没有漏点。

## 目录

- 一、充分条件假言推理与判断（9题）
  - 有效式：肯定前件或否定后件，方向要走对（2题）
  - 陷阱：后件为真不能倒推前件（3题）
  - 判断构造：把条件补成能推出结果的前件（1题）
  - 陷阱一：重要条件不等于充分条件（2题）
  - 陷阱二：形式像对，前提未必真（1题）
- 二、必要条件假言推理与判断（11题）
  - 有效式：少了它不行，结果成立就要回找它（2题）
  - 陷阱：有了必要条件不等于结果必然成（2题）
  - 必要条件的文字信号（1题）
  - 必要条件与结论边界（2题）
  - 必要条件与定义边界（1题）
  - 除非、否则与双重否定（1题）
  - 必要条件与选言边界（1题）
  - 相容选言里不要误排斥（1题）
- 三、三段论、性质判断周延与换质位（20题）
  - 先看三项：大项、小项、中项（2题）
  - 三段论形式正确，前提仍要真实（1题）
  - 补大前提：把省略规则说出来（1题）
  - 四概念：同一个词前后换了对象（1题）
  - 大项扩大：结论说得比前提更满（1题）
  - 小项扩大：主语范围被偷偷放大（1题）
  - 构造三段论：先定中项桥梁（2题）
  - 有效结构：形式有效还要看前提（1题）
  - 有效形式与真实前提要分开（1题）
  - 周延性：看概念有没有被说尽（1题）
  - 换位边界：不是每句话都能倒过来（1题）
  - 类比与换位换质不要混判（1题）
  - 换质位：变形不能变意思（1题）
  - 构建论证：让结论从共同前提长出来（3题）
  - 综合辨析：换位、三段论、外延分开看（1题）
  - 省略前提：把隐藏的大前提补回来（1题）
- 四、归纳推理与探求因果联系（11题）
  - 不完全归纳推理（4题）
  - 不完全归纳推理可靠程度（4题）
  - 科学归纳推理与不完全归纳推理（1题）
  - 探求因果联系中的求异法（1题）
  - 科学归纳、求异法与类比推理（1题）
- 五、类比推理（4题）
  - 类比推理（4题）
- 六、概念、定义、外延关系与划分（8题）
  - 概念划分规则（1题）
  - 同一律与偷换概念（1题）
  - 概念外延关系错项辨析（1题）
  - 定义构成与属加种差定义（1题）
  - 概念外延中的相容关系与属种关系（1题）
  - 概念外延关系图示辨析（1题）
  - 定义方法与种差加属概念（1题）
  - 同一律与概念确定性（1题）
- 七、选言推理、联言判断与复合判断（9题）
  - 选言判断（1题）
  - 反对关系与联言判断（1题）
  - 不相容选言推理（有效式）（1题）
  - 不相容选言推理无效式辨析（1题）
  - 复合假言与选言推理链（1题）
  - 选言推理与逆向思维复合辨析（1题）
  - 联言判断类型识别（1题）
  - 联言判断真值条件（1题）
  - 复合判断识别与逻辑规则辨析（1题）
- 八、真假关系、逻辑规律与关系判断（11题）
  - 矛盾律（1题）
  - 矛盾关系与真假判断（1题）
  - 形式逻辑综合选择题（1题）
  - 关系判断与非传递关系（2题）
  - 排中律与两不可错误（1题）
  - 矛盾律与自相矛盾错误（1题）
  - 逻辑规则综合选择（1题）
  - 枚举概括与同一对象替换（1题）
  - 真假话约束推理（1题）
  - 矛盾律与一致性要求（1题）

## 一、充分条件假言推理与判断

【本类怎么做】
- 先把条件句写成“P -> Q”，分清前件 P 和后件 Q。
- 只认两个有效方向：肯定前件推出后件，否定后件推出否定前件。
- 看到“结果已经出现”时，不能倒推唯一条件；先判断题目有没有犯方向倒置。

【本类常见坑】
- 后件为真不能推出前件必真。
- 某个条件很重要，不等于它就是充分条件。
- 形式像条件推理，但前提本身若不真实，结论仍不能成立。

### 有效式：肯定前件或否定后件，方向要走对

#### 1. 2024朝阳一模 第20题第（1）问（主观题）

【这道题考什么】 考充分条件假言推理。抓手是：推理一设定“如果 A 区域古代没有广泛生长竹子，就不可能有大量炭化竹节”，材料又给出已发现大量炭化竹节，需要判断能否由否定后件推出否定前件。

【题目材料】

```text
20.（9分）学会正确地运用推理，对于科学研究具有重要意义。
材料一 有科学家对我国古代气候及其变化进行了一系列考古研究和调查论证，其中
之一是关于A区域古代气候较为温暖的论证。科学家的论证过程包含了两个推理。
推理一:
如果A区域古代没有广泛生长竹子，就不可能有大量的炭化竹节，
考古发掘中已发掘出地底下有大量炭化竹节，
所以，A区域古代广泛生长着竹子。
(1)推理一属于哪种推理类型? 其成立的理由是什么? （5分）
材料二 科学家进而又根据竹子适宜生长在温暖的地方以及A区域当时广泛生长着竹
子，运用不同于推理一的另一种演绎推理形式，推断出A区域古代气候较为温暖。
(2)根据材料二，补充完整推理二。（4分）
```

【设问】 推理一属于哪种推理类型？其成立的理由是什么？（5分）

【怎么想到的】 前提说“如果没有广泛生长竹子，就不可能有大量炭化竹节”，后面又给出“大量炭化竹节”这一事实。既然后件中的“不可能有大量炭化竹节”被事实否定，就可以反过来否定“没有广泛生长竹子”这个前件，推出古代广泛生长竹子。

【满分作答示范】 推理一属于充分条件假言推理，推理成立。题面设定：没有广泛生长竹子，就不会出现大量炭化竹节；现在发现了炭化竹节，等于否定结果项，可反推并非没有竹子，即 A 区域古代曾广泛生长竹子。

【采分点对照】
- 推理一属于充分条件假言推理
- 前提把“古代没有广泛生长竹子”设为推出“不可能有大量炭化竹节”的充分条件
- 材料已经发现大量炭化竹节，即否定后件，因此可以否定前件，推出 A 区域古代广泛生长竹子，推理成立

#### 2. 2026通州期末 第19题第（2）问（主观题）

【这道题考什么】 考充分条件假言推理。抓手是：推理①先建立“阻碍加装电梯就会侵犯相关业主合法权益”的充分条件关系，又确认范某实施了阻碍行为，再推出其行为侵犯相关业主合法权益。

【题目材料】

```text
19. 【案件事实】
某小区3 号楼2 单元全体业主一致签字同意增设电梯,并于小区主要出入口张贴意见征集单、公示、
承诺及图纸等相关材料,公示期间未收到异议。随后,该项目取得了主管部门的审批手续并正式开工。居
住于相邻楼的业主范某认为,电梯安装位置影响其采光,侵犯其合法权益,遂多次在现场阻碍施工,导致
项目停工。2 单元全体业主向人民法院起诉,请求判令范某停止对加装电梯工程的妨害行为。法院经现场
勘查,案涉加装电梯采用全玻璃设计,未对相邻楼采光造成影响,遂判决范某停止对电梯加装工程的阻挠
行为。同时,法院明确,若电梯投入使用后,确在采光、通风等方面对部分业主造成较大影响,相关权利
人可就补偿事宜另行协商或通过法律途径解决。
【法律依据】
(1)结合材料,运用《法律与生活》知识,分析判决结果并说明理由。
(2)根据材料,判断推理1和2的逻辑正误,并结合《逻辑与思维》知识说明理由。
推理
判断逻辑正误并说明理由
1如果阻碍加装电梯,就会侵犯相关业主的合法权益。
范某阻碍加装电梯,所以范某侵犯了相关业主的合法权益。
2只有公示期间未收到异议,加装电梯才符合要求。
公示期内未收到异议,所以加装电梯符合要求。
```

【设问】 根据材料，判断推理①和②的逻辑正误，并结合《逻辑与思维》知识说明理由。

【怎么想到的】 材料先建立“阻碍加装电梯就会侵犯相关业主合法权益”的条件关系，又明确范某确实阻碍加装电梯。条件方向要先固定住：阻碍行为是前件，权益受侵是后件。

【满分作答示范】 推理①属于充分条件假言推理，结构有效。可整理为：若阻碍加装电梯，就侵犯相关业主合法权益；范某实施了阻碍行为；因此可推出其行为侵犯相关业主合法权益。这里是肯定前件推出后件，没有把方向倒过来。

【采分点对照】
- 推理①属于充分条件假言推理
- 材料把“范某阻碍加装电梯”作为推出“侵犯相关业主合法权益”的充分条件，现在已经肯定前件，就可以推出后件，符合“肯定前件式”
- 该推理方向是从阻碍行为到权利受侵，结构有效

### 陷阱：后件为真不能倒推前件

#### 3. 2026东城期末 第17题第（2）问（主观题）

【这道题考什么】 考充分条件假言推理的边界。抓手是：只建立“引入智能垃圾箱可以提升垃圾分类效率”的条件关系，前件是引入设备，后件是效率提升。

【题目材料】

```text
17. 人形机器人“入职”汽车生产线，安防机器人智能巡逻，科研机器人在实验室“上岗”……场景作为系统性验证新技术、新产品、新业态的具体情境，赋能新质生产力发展。
材料一 推动场景创新，制度性障碍亟待破解。
障碍1：高价值数据产权界定模糊、缺乏开放机制。政府、央企等掌握核心场景和数据资源，民营企业在特定领域面临较高的市场准入门槛，各地各部门场景建设存在孤岛化问题。
障碍2：场景业主方与技术供给方之间信息不对称、信任成本高、交易效率低。大量场景富集地区“有场景、缺技术”，而科技企业集聚地方“有技术、缺场景”。
障碍3：场景数据价值、利益分配规则不清楚。新技术新产品首试首用的政策保险、容错机制尚未普及，缺乏有效的社会分担机制，抑制企业创新活力。
（1）在上述障碍中任选两个，分别提出政策性建议，并运用《经济与社会》知识，说明理由。
材料二 某市发布老城区“微更新+智慧场景”需求。以下是关于更新方案的一些主张。
主张1：我们既要完整保留历史街巷的一砖一瓦，也要对其中无法适应现代需要的部分进行必要的拆除和改造。
主张2：要提升垃圾分类效率，必须引入智能垃圾箱。因为，智能垃圾箱含有无接触投放和自动积分奖励功能，如果引入智能垃圾箱，垃圾分类效率就能得到提升。
主张3：有些科学民主的更新方案是采用“居民提案—AI智能模拟—多轮投票”模式制定的。“立体花园+口袋公园”复合型公共空间方案是通过此模式制定的。因此，“立体花园+口袋公园”复合型公共空间方案是科学民主的更新方案。
（2）运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）
```

【设问】 运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）

【怎么想到的】 材料先说“引入智能垃圾箱”会带来“垃圾分类效率提升”，这只是条件能够推出结果。主张2却倒过来，由效率提升推出“必须引入智能垃圾箱”，等于把结果当成唯一原因。

【满分作答示范】 主张2不合逻辑。智能垃圾箱能提升分类效率，不代表效率提升只能靠它实现；由结果反推唯一条件，是把充分条件倒过来用。

【采分点对照】
- 主张2不符合逻辑
- 题干只能说明引入智能垃圾箱有助于提升垃圾分类效率，不能由效率提升这一结果倒推出“必须引入智能垃圾箱”这一唯一条件
- 该主张把后件真误当成前件必真，属于充分条件假言推理方向倒置

#### 4. 2025西城二模 第16题第（2）问（主观题）

【这道题考什么】 考充分条件假言推理的边界。抓手是：条件句只保证“发现岩松鼠活动痕迹”能够推出“找到红嘴蓝鹊”。

【题目材料】

```text
16.（14分）
京郊的鹿叫村遗址,生物资源丰富,是各种野生动植物的栖息地。
上世纪80年代,因为取水问题鹿叫村整体搬迁,村落遗址内保留着较
多废弃水井和地窖,时常有动物掉入,对区域野生动物造成极大威胁。
2024 年,延庆区自然保护地管理处在水井内建造了攀爬台阶,并营造了5
处雨水收集池,便于不同体型的动物们自由取水。 近日,工作人员在饮水
设施周边发现了多种野生动物活动痕迹,经分析采集到的影像资料,确认
有勺鸡、貉、雕鸮、狍子、野猪、岩松鼠、红嘴蓝鹊等十余种野生动物在
此饮水觅食,这里已经成为多个物种的栖息地。
(1)废弃水井变成了动物乐园,请说明背后的哲学智慧。（6分）
(2)已知以下条件:
1勺鸡和雕鸮不会同时出现在同一饮水点。
2若发现岩松鼠的活动痕迹,则一定能找到红嘴蓝鹊。
问题:
工作人员在某雨水收集池同时观察到雕鸮和红嘴蓝鹊,能否确定此时一定有岩松鼠活动?解释推理过
程。（4分）
(3)假定出现了如下情形:改造之后,野生动物的活动增加,导致周边的农田和果园被啃食,村民
要求拆除水源池。请运用所学,针对村民诉求提出解决办法。（4分）
```

【设问】 工作人员在某雨水收集池同时观察到雕鸮和红嘴蓝鹊，能否确定此时一定有岩松鼠活动？解释推理过程。（4分）

【怎么想到的】 “发现岩松鼠活动痕迹”能够推出“找到红嘴蓝鹊”，前件是岩松鼠活动痕迹，后件是红嘴蓝鹊出现；材料现在只给出后件为真，即观察到了红嘴蓝鹊。

【满分作答示范】 不能判定一定有岩松鼠。原条件只保证“有活动痕迹→可能找到红嘴蓝鹊”；现在只是见到红嘴蓝鹊，结果成立不能反推唯一原因，仍可能由别的因素造成。

【采分点对照】
- 不能确定此时一定有岩松鼠活动
- 题干只说明“发现岩松鼠活动痕迹”可以推出“找到红嘴蓝鹊”，这是从前件到后件的充分条件关系
- 观察到红嘴蓝鹊只是后件为真，不能倒推出前件必真，因为红嘴蓝鹊出现还可能由其他原因造成，所以岩松鼠是否活动仍不能确定

#### 5. 2026海淀期末 第20题第（1）问（主观题）

【这道题考什么】 原题材料缺失，暂不判定题型。

【题目材料】

```text
本题原始材料缺失，待补。
```

【设问】 原题设问缺失或与材料错位，待补。

【怎么想到的】 原题材料缺失，不能判断材料中的逻辑抓手；待补入原始题面后再分析。

【满分作答示范】 原题材料缺失，暂不提供示范答案；补入原卷题面后再完善。

【采分点对照】
- 原始题面缺失，暂不列采分点；补入原卷材料后再补充。

### 判断构造：把条件补成能推出结果的前件

#### 6. 2024丰台一模 第19题第（1）问（主观题）

【这道题考什么】 考充分条件假言推理。抓手是：题干要补全划线处，使后面的“就能方便人们正确进行垃圾分类”成为可靠结果。

【题目材料】

```text
19.（8分）北京市某校学生在参加模拟政协活动时,围绕垃圾分类问题进行了如下探讨。
目前,垃圾分类已在全国各地广泛开展。从现实来看,垃圾分类意识
已经深入人心,但垃圾分类知识宣传还有不足,分类错误现象依旧存在,
商品包装上的垃圾分类标识率仍然不高……我建议可以选择其中一个小
切入点来研究。
我们对食品、日用品、生鲜等不同类别的219件商品进行调研,发现其
中仅39件商品包装上有明确的垃圾分类标识,而且极少商品标记出商品内
包装、外包装以及商品的具体分类类别。我们认为:
划线①：__________
就能方便人们正确进行垃圾分类。
我同意你的想法。我们可以以此为主题进行研究,撰写一份模拟政协
提案。我觉得要撰写这个提案,需要查找我国关于垃圾分类标准的法律条
文、部分城市垃圾分类标准,以及常见商品外包装印刷标识情况等相关资
料。此外,我们还可以采取以下研究方法:
划线②：__________
(1)根据上下文,将划线①处补充完整,使其成为一个符合逻辑规则的真判断。（2分）
(2)在划线②处补全两种具体研究方法,并运用科学思维知识分别说明理由。（6分）
```

【设问】 根据上下文，将划线①处补充完整，使其成为一个符合逻辑规则的真判断。（2分）

【怎么想到的】 横线后面已经给出结果“就能方便人们正确进行垃圾分类”，要补的是能保证这个结果出现的前件。材料前面说的是商品包装缺少明确垃圾分类标识，所以关键条件不是泛泛说“加强宣传”，而是把标识印到商品外包装上。

【满分作答示范】 划线①可补：只要在商品外包装上清楚标注垃圾类别，就能方便人们正确进行分类。前件直接回应包装标识不足，后件对应分类便利，构成上下文中成立的充分条件判断。

【采分点对照】
- 符合逻辑规则的真判断是：如果或只要能够在商品外包装上印上垃圾分类标识，就能方便人们正确进行垃圾分类
- 前件对应商品包装标识缺失这一材料问题，后件对应方便正确分类这一结果，构成符合上下文的充分条件假言判断

### 陷阱一：重要条件不等于充分条件

#### 7. 2025丰台二模 第19题第（1）问（主观题）

【这道题考什么】 考充分条件假言推理的边界。抓手是：原观点结构为：只要给 AI 装上版权雷达并提前扫描问题指令，就能防止点击盗版资源网站。

【题目材料】

```text
19.（13分）数智时代，司法“把脉开方”解保护与创新之困。
案例：某互联网企业开发了一款 AI 产品，用户输入“我要看某某热播剧”后，AI 生成的链接中多数指向盗版资源网站。版权方 H 公司在检测数据时发现其热播剧日均被盗版链接点击超万次，遂向法院提起诉讼，请求开发这款 AI 产品的互联网企业承担侵权责任。
调研：法院在深入调研后，发现 AI 产品拥有千亿级参数规模的通用大模型，生成的具体内容具有高度的不可预测性。该互联网企业已经从语料输入、模型运行到内容输出等各个环节进行了定期跟踪和核查，尽到了相应的义务。
建议：法院遂开出具有前瞻性、可操作性的司法建议：给 AI 装上“版权雷达”，提前扫描问题指令；在输出端部署“数字巡警”，实时扫描可疑链接；定期开展“安全体检”，关注 AI 健康。
（1）有人认为：只要给 AI 装上“版权雷达”，提前扫描问题指令，就能防止点击盗版资源网站。判断该观点是否正确，并运用《逻辑与思维》知识说明理由。（5分）
（2）一纸司法建议，既为当下划定了红线，防止技术滥用，又为未来创新发展预留了空间。运用《法律与生活》知识，谈谈你对这句话的理解。（8分）
```

【设问】 有人认为：只要给 AI 装上“版权雷达”，提前扫描问题指令，就能防止点击盗版资源网站。判断该观点是否正确，并运用《逻辑与思维》知识说明理由。（5分）

【怎么想到的】 设问直接把观点写成“只要装上版权雷达，就能防止点击盗版资源网站”，触发的是充分条件判断真假辨析。判断时要问：这个技术措施是不是足以保证结果？

【满分作答示范】 观点片面。版权雷达能提前识别和提醒，是治理盗版的技术环节；要防止点击盗版网站，还离不开追责、平台治理、资源屏蔽和用户规范等条件，单一工具不足以保证结果。

【采分点对照】
- 该观点是片面的
- 给 AI 装上版权雷达并提前扫描问题指令，只能说明技术上增加了识别和提醒环节，是防止点击盗版资源网站的重要条件
- 但盗版治理还需要法律追责、平台审核、资源屏蔽和用户规范使用等多重条件共同作用，不能把单一技术措施当成足以保证结果的充分条件

#### 8. 2024丰台二模 第18题第（2）问（主观题）

【这道题考什么】 考充分条件假言推理的边界。抓手是：观点说“只要能够准确预测冰雪经济的发展前景，就能推动冰雪经济高质量发展”，把准确预测说成足以推出高质量发展的条件。

【题目材料】

```text
18.（19分）“冷资源”生成“热经济”,推动冰雪经济高质量发展。
火热的冰雪经济激发了同学们探究的热情,同学们查阅资料如下:
• 为推动冰雪经济发展,我国陆续出台《冰雪运动发展规划(2016—2025年)》
《关于释放旅游消费潜力推动旅游业高质量发展的若干措施》等相关政策。
• 依据相关报告显示,2022-2023冰雪季我国冰雪休闲旅游人数为3.12亿人次,冰
雪休闲旅游收入为3490亿元;2023-2024 冰雪季我国冰雪休闲旅游人数突破4亿
人次,冰雪休闲旅游收入超过5000亿元。
• 第七届雪博会共有来自9个国家27个省份近3000 名嘉宾和参展商现场参会,冰
雪装备、冰雪旅游、冰雪文化、冰雪体育、冰雪商贸等五大领域 455 家参展商参
展,累计参展观众达到14.04万人次,现场交易额达2.83亿元,创历届新高。
• 我国冰雪资源丰富,但由于地理气候等差异,目前国内比较好的室外场地往往局
限于一地或者一个区域,难以实现全季运营。我国冰雪装备制造企业以中小企业为主,产业链不健全、行业标准亟须完善;研发人才不足、研发投入较少、核心
技术欠缺,一些高端冰雪装备市场仍被国外品牌占据。
围绕如何推动冰雪经济高质量发展,同学们结合以上材料进行探究。
(1)结合材料,同学们构建了一个符合逻辑规则的三段论,请你补充完整。（5分）
大前提:
小前提:
结论:
可以推动冰雪经济高质量发展。
(2) 有同学认为,只要我们能够准确预测冰雪经济的发展前景,就能推动冰雪经济高
质量发展。结合材料,运用科学思维对该观点进行评析。（6分）
(3)经过探究,同学们从《经济与社会》角度,对如何利用“冷资源”撬动“热经
济”形成以下共识:
-。（8分）
```

【设问】 有同学认为，只要我们能够准确预测冰雪经济的发展前景，就能推动冰雪经济高质量发展。结合材料，运用科学思维对该观点进行评析。（6分）

【怎么想到的】 先抓“只要……就……”：这句话把“准确预测发展前景”放在充分条件位置，好像只要预测准，高质量发展就自然发生。再看材料，冰雪经济还受场地布局、产业链、标准、人才、核心技术、高端装备等条件制约，所以准确预测只能说明发展必须有科学预判，不能推出结果必然实现。

【满分作答示范】 观点片面。准确预判能帮助把握冰雪经济趋势，是重要支撑而非充分保证；高质量发展还取决于产业链、标准、人才、技术和装备等条件，也要结合优势短板作具体分析。

【采分点对照】
- 该观点是片面的
- 准确预测冰雪经济发展前景有助于把握趋势，是推动冰雪经济高质量发展的必要条件或重要条件，但不是充分条件
- 不能由“预测准确”直接推出“高质量发展必然实现”
- 还要补足产业链、标准、人才、技术、装备等条件，并结合辩证思维具体分析优势和短板

### 陷阱二：形式像对，前提未必真

#### 9. 2025东城二模 第18题第（2）问（主观题）

【这道题考什么】 考充分条件假言推理的边界。抓手是：学生推理把“良好的创新生态”设为“实现创新发展”的充分条件，并且用当前已有创新生态这一事实肯定前件，再推出一定实现创新发展。

【题目材料】

```text
18.（12分）
今天的中国成为全球瞩目的创新“孵化器”,创新的种子处处萌发。嫦娥六号实现人类首次月球背面采样返
回;人工智能方兴未艾,深度求索等“杭州六小龙”的科技创新备受瞩目;《哪吒2》横空出世,释放巨大文
化能量与市场潜力;无人化垂直植物工厂采用多层立体无土栽培技术,减少耕地依赖;我国集齐造船业的
“三颗明珠”:航空母舰、大型液化天然气运输船和大型邮轮,从造船大国走向造船强国……今天的中国,
正在形成充满生机、如热带雨林般的创新生态。
有人总结创新生态的“热带雨林”法则:需要大企业、高校、科研机构等“乔木层”,也需要中小企业等“灌木
层”,还需要政策、市场、基础设施、产业体系等“土壤层”。
(1)结合材料,运用《经济与社会》知识,说明我国形成“热带雨林”创新生态的“秘诀”。 （8分）
创新发展需要良好的创新生态。据此,某同学做出如下推理:
有良好的创新生态,就会实现创新发展。
当前我国有良好的创新生态,所以,我国一定能实现创新发展。
(2) 写出该推理的类型,判断正确与否,并说明理由。（4分）
```

【设问】 写出该推理的类型，判断正确与否，并说明理由。（4分）

【怎么想到的】 误判风险在于：“有良好创新生态，所以能实现创新发展”看起来像肯定前件式。判断时先看材料关系：热带雨林般的创新生态能支持创新，但并不等于只要有生态就必然实现创新发展。

【满分作答示范】 这一推理形式上像肯定前件，但前提把良好创新生态说成足以保证创新发展，这个判断并不真实。创新生态重要，却不能单独保证创新结果，所以结论不能必然推出。

【采分点对照】
- 该推理形式上是充分条件假言推理的肯定前件式：如果有良好创新生态，就会实现创新发展；当前我国有良好的创新生态；所以，我国一定能实现创新发展
- 但良好创新生态只是创新发展的重要条件，不足以单独保证创新发展
- 前提判断不真实，因此不能推出“我国一定能实现创新发展”的必然结论

## 二、必要条件假言推理与判断

【本类怎么做】
- 把“只有 P 才 Q”“没有 P 就没有 Q”先翻译成 Q -> P。
- 有效方向是肯定后件推出前件，否定前件推出否定后件。
- 遇到“除非、否则、才”等字眼，先把日常表达还原成条件关系。

【本类常见坑】
- 有了必要条件，不等于结果一定发生。
- 把相容选言当成不相容选言，会误排除其他可能。
- 定义边界和条件边界要分开，不能把概念解释直接当推理结论。

### 有效式：少了它不行，结果成立就要回找它

#### 1. 2024朝阳一模 第20题第（2）问（主观题）

【这道题考什么】 考必要条件假言推理。抓手是：只有A区域古代气候温暖，A区域古代才有可能生长竹子。

【题目材料】

```text
20.（9分）学会正确地运用推理，对于科学研究具有重要意义。
材料一 有科学家对我国古代气候及其变化进行了一系列考古研究和调查论证，其中
之一是关于A区域古代气候较为温暖的论证。科学家的论证过程包含了两个推理。
推理一:
如果A区域古代没有广泛生长竹子，就不可能有大量的炭化竹节，
考古发掘中已发掘出地底下有大量炭化竹节，
所以，A区域古代广泛生长着竹子。
(1)推理一属于哪种推理类型? 其成立的理由是什么? （5分）
材料二 科学家进而又根据竹子适宜生长在温暖的地方以及A区域当时广泛生长着竹
子，运用不同于推理一的另一种演绎推理形式，推断出A区域古代气候较为温暖。
(2)根据材料二，补充完整推理二。（4分）
```

【设问】 根据材料二，补充完整推理二。（4分）

【怎么想到的】 “只有气候温暖，才有可能生长竹子”把气候温暖放在必要条件的位置。必要条件推理的关键口令是：少了它不行，结果已经成立就要回找它。

【满分作答示范】 推理二属于必要条件假言推理。可表述为：广泛生长竹子离不开温暖气候；材料确认 A 区域古代曾有大量竹子，就应肯定这一必要条件，即 A 区域古代气候温暖。

【采分点对照】
- 推理二为：只有 A 区域古代气候温暖，A 区域古代才有可能广泛生长竹子
- 材料已经确认该区域古代广泛生长竹子，即后件成立，可以根据必要条件假言推理的肯定后件式推出必要条件成立：A 区域古代气候温暖

#### 2. 2026丰台一模 第18题第（2）问（主观题）

【这道题考什么】 考必要条件假言推理。抓手是：甲的推理使用“只有具备某必要条件，后件结果才成立”的条件关系。

【题目材料】

```text
18.（14分）
2026年《政府工作报告》提出,深入实施提振消费专项行动。某班同学在时事
学习中,查阅到以下资料,展开讨论。
用好“加减乘除”推动消费持续增长
“加法”,重在强基固本。制
定实施城乡居民增收计划,促进低
收入群体增收、扩大居民财产性收
入;同时推进消费新业态新模式新场景试点,大力培育文旅、体育
赛事和演艺经济等消费场景,增加
优质产品和服务供给。
“减法”,重在解除后顾之忧。
加大在医疗、养老和生育养育等方
面的保障力度:提高医保补助标准,
提高城乡居民基础养老金月最低标
准,发展普惠托育服务、探索育儿
补贴等。
“乘法”,重在发挥财政资金
乘数效应。今年政府将安排超长期
特别国债2500亿元支持消费品以旧
换新、进一步加大对线下实体零售
的支持力度,集中支持汽车、冰箱
和智能眼镜等重点消费品以旧换新,
换出新赛道和新动能。
“除法”,重在破壁清障,进
一步清理各类消费限制性措施。比如,
针对消费市场中存在的隐性壁垒进
行分类施策,简化促销活动的审批
流程;在一些城市进一步放宽车辆
购买限制、增发购车指标等。
(1)运用《经济与社会》知识,分析“加减乘除”在推动消费持续增长的过程
中是怎样发挥作用的。（8分）
在讨论过程中,两位同学作出如下推理。
甲:只有各项提振消费的举措扎实落地,才能有效释放消费潜力。如果消费潜力
得到有效释放,那么各项提振消费的举措已经扎实落地了。
乙:产品质量的提升能够带动居民消费,改善消费环境不能提升产品质量。所
以,改善消费环境不能带动居民消费。
(2)分别写出上述推理的类型,判断是否正确,并说明理由。（6分）
```

【设问】 分别写出上述推理的类型，判断是否正确，并说明理由。（6分）

【怎么想到的】 甲的推理把某个条件放在“只有……才……”的必要条件位置，又从后件成立回到必要条件成立。这里不能按充分条件去想成“有了条件必然有结果”，而要按必要条件的方向判断：既然结果已经出现，就说明它离不开的那个条件也必须存在。

【满分作答示范】 甲的推理可按必要条件假言推理处理。必要条件判断中，结果项成立能够推出必要条件成立。甲由结果成立回推其不可缺少的条件存在，满足肯定结果项式。只要材料中的必要条件关系和结果项事实都真实，这一推理就是正确的。

【采分点对照】
- 甲的推理属于必要条件假言推理
- 必要条件判断中，后件成立可以推出必要条件成立
- 甲由结果成立回推其不可缺少的条件存在，符合肯定后件式
- 只要材料中的必要条件关系和后件事实都真实，该推理就是正确的

### 陷阱：有了必要条件不等于结果必然成

#### 3. 2025朝阳一模 第17题第（1）问（主观题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：原判断表达“实现虚拟与现实深度融合，离不开人工智能拥有智能硬件载体”。

【题目材料】

```text
17. （12分）2025 年国务院政府工作报告提出,培育壮大新兴产业、未来产业。
材料一 具身智能,是指有身体并支持与物理世界进行交互的智能体。目前,人工智能正在迈向通用
智能的路上,大模型展示出满足人类需求的交互能力。然而,这种交互仍局限于数字世界,它能够回答问
题、画画,却不能帮助我们做家务或是盖房子。我们想要实现虚拟和现实的深度融合,就必须要让人工智
能拥有一个智能硬件载体,让它们像人类一样具备感知和行动能力。
据此,有人作出如下推理:
我们想要实现虚拟与现实的深度融合,就必须要让人工智能拥有一个智能硬件载体。
所以,让人工智能拥有一个智能载体,就能实现虚拟与现实的深度融合。
(1)运用《逻辑与思维》知识,判断该推理正确与否,并说明理由。（5分）
材料二 人形机器人又称类人机器人、仿生机器人等,通常具有头部、躯干、双臂双腿等,在结构和
功能上尽可能接近人类,具备一定的运动能力和感知能力。从商用服务到智能制造,从陪伴老人到理货看
店……人形机器人制造在“加速跑”。
与此同时,市场上主流的人形机器人价格甚至超50 万元。人形机器人产业链高度复杂,人形机器人
产品呈现出高度的定制化倾向,缺乏真正通用的零部件,导致成本居高不下。
在工厂环节,只有少部分先进工厂开始探索在某些工作流程中使用人形机器人,更多走进生产线可能
在未来三到五年实现;而真正走进人们的生活,需要更高的精确度和安全性,所需时间会更长。
人形机器人的应用首先要保证可靠性和稳定性,由于目前这方面尚未完全成熟,人形机器人更适合那些容
错率较高的场合。专家建议要尽快完善人形机器人的相关标准,不断开放应用场景,让人形机器人“先应
用起来”。
(2)结合材料二,运用《经济与社会》知识,说明如何加快人形机器人服务于生产生活的进程。（7分）
```

【设问】 运用《逻辑与思维》知识，判断该推理正确与否，并说明理由。（5分）

【怎么想到的】 材料里的“离不开智能硬件载体”是在说必要条件：没有智能硬件载体，就无法实现虚拟与现实深度融合。推理却倒过来，把“有智能硬件载体”当成“一定实现深度融合”的充分条件。

【满分作答示范】 推理不成立。智能硬件是虚实融合不可缺的载体，但具备载体不代表内容、交互、技术和场景都成熟；肯定必要条件，推不出深度融合一定实现。

【采分点对照】
- 该推理不正确
- 智能硬件载体只是实现虚拟与现实深度融合的必要条件，没有硬件载体不行，但有了硬件载体并不等于内容设计、交互体验、技术支撑和应用场景都已成熟
- 肯定必要条件前件不能推出后件成立，所以不能仅凭智能载体就断定一定实现深度融合

#### 4. 2026通州期末 第19题第（2）问（主观题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：推理②把“只有公示期间未收到异议，加装电梯才符合要求”理解成一个必要条件判断。

【题目材料】

```text
19. 【案件事实】
某小区3 号楼2 单元全体业主一致签字同意增设电梯,并于小区主要出入口张贴意见征集单、公示、
承诺及图纸等相关材料,公示期间未收到异议。随后,该项目取得了主管部门的审批手续并正式开工。居
住于相邻楼的业主范某认为,电梯安装位置影响其采光,侵犯其合法权益,遂多次在现场阻碍施工,导致
项目停工。2 单元全体业主向人民法院起诉,请求判令范某停止对加装电梯工程的妨害行为。法院经现场
勘查,案涉加装电梯采用全玻璃设计,未对相邻楼采光造成影响,遂判决范某停止对电梯加装工程的阻挠
行为。同时,法院明确,若电梯投入使用后,确在采光、通风等方面对部分业主造成较大影响,相关权利
人可就补偿事宜另行协商或通过法律途径解决。
【法律依据】
(1)结合材料,运用《法律与生活》知识,分析判决结果并说明理由。
(2)根据材料,判断推理1和2的逻辑正误,并结合《逻辑与思维》知识说明理由。
推理
判断逻辑正误并说明理由
1如果阻碍加装电梯,就会侵犯相关业主的合法权益。
范某阻碍加装电梯,所以范某侵犯了相关业主的合法权益。
2只有公示期间未收到异议,加装电梯才符合要求。
公示期内未收到异议,所以加装电梯符合要求。
```

【设问】 根据材料，判断推理①和②的逻辑正误，并结合《逻辑与思维》知识说明理由。

【怎么想到的】 “公示期间未收到异议”只是加装电梯符合要求的必要条件，不是全部条件。即使这一项满足，也还可能存在设计、审批、施工等其他要求未满足，所以不能只凭“未收到异议”就推出“符合要求”。

【满分作答示范】 推理②应判为必要条件假言推理，但结论不能成立。没有公示异议只说明程序中的一个前置条件具备，并不代表设计、安全、审批、施工等全部要求都满足；肯定必要条件不能推出结果必然成立，所以不能只凭这一点断定加装电梯符合要求。

【采分点对照】
- 推理②属于必要条件假言推理，但结构错误
- “公示期间未收到异议”只是加装电梯符合要求的必要条件，说明缺少该条件就不能认定程序符合要求
- 但肯定这一前件并不能推出设计、安全、审批、程序等全部要求都已满足，因此不能仅凭未收到异议就断定加装电梯符合要求

### 必要条件的文字信号

#### 5. 2024顺义二模 第7题（选择题）

【这道题考什么】 考必要条件假言推理。抓手是：只有不断加深对数字劳动的认识、把握基本特征并构建相关法律法规，才能确保数字劳动受到监管和保护并保证数字经济稳定快速发展。

【题目材料】

```text
7.随着科技进步和数字化转型的加速,数字经济成为了我国经济发展的重要动力。数字劳动是数字经济发展的重要因素,是依托于互联网、大数据、云计算、人工智能等新型技术载体,以智力、创造力为主导,创造数字化产品的非物质劳动。只有不断加深对于数字劳动的认识,把握数字劳动的基本特征,并以此为基础构建起相关法律法规,才能确保数字劳动受到监管和保护,保证我国数字经济稳定和快速发展。如果上述结论皆为真,下列逻辑分析正确的是
A.“数字劳动是数字经济发展的重要因素”是运用“种差加属概念”的方法下的定义
B.数字劳动和非物质劳动是交叉关系
C.构建起相关法律法规是保证我国数字经济稳定和快速发展的必要条件
D.材料中假言判断的真假取决于前后件本身的真假
```

【设问】 7.随着科技进步和数字化转型的加速，数字经济成为了我国经济发展的重要动力。数字劳动是数字经济发展的重要因素，是依托于互联网、大数据、云计算、人工智能等新型技术载体，以智力、创造力为主导，创造数字化产品的非物质劳动。只有不断加深对于数字劳动的认识，把握数字劳动的基本特征，并以此为基础构建起相关法律法规，才能确保数字劳动受到监管和保护，保证我国数字经济稳定和快速发展。如果上述结论皆为真，下列逻辑分析正确的是
A.“数字劳动是数字经济发展的重要因素”是运用“种差加属概念”的方法下的定义
B.数字劳动和非物质劳动是交叉关系
C.构建起相关法律法规是保证我国数字经济稳定和快速发展的必要条件
D.材料中假言判断的真假取决于前后件本身的真假

【怎么想到的】 先抓住最后那句“只有不断加深认识、把握特征，并构建起相关法律法规，才能确保监管和保护，保证数字经济稳定和快速发展”。“只有……才……”说明前面这组条件少了不行，其中“构建起相关法律法规”就是保证数字经济稳定快速发展的必要条件。

【满分作答示范】 C 项正确。“只有……才……”说明认识、特征把握和法规构建是不可少的条件；缺少相关法律法规，数字劳动监管保护和数字经济稳定发展就没有制度支撑。

【采分点对照】
- 答案选C
- 句式“只有……才……”先把“加深认识、把握特征、构建法律法规”放在必要条件位置
- 其中构建相关法律法规少了，就不能确保数字劳动受监管和保护，也不能保证数字经济稳定快速发展，所以 C 抓住了必要条件关系
- 错项分析：A 项诱人，因为材料确实解释了数字劳动
- 错在“数字劳动是数字经济发展的重要因素”只是地位说明，不是用种差加属概念下定义
- B 项诱人，因为数字劳动和非物质劳动都在同一句定义里
- 错在材料把数字劳动说成“创造数字化产品的非物质劳动”，更像被包含在非物质劳动范围内，不是交叉关系
- D 项诱人，因为前后件本身真假也会影响假言判断
- 错在假言判断还要看前后件的条件联系，不能停在前后件各自真假

### 必要条件与结论边界

#### 6. 2024丰台一模 第11题（选择题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：题干先说河流是生命宜居的必要条件，又只说火星陨坑结构“很可能”是远古河床遗迹。

【题目材料】

```text
11.在地球上,河流对生命、化学、营养物质、沉积物的循环非常重要,是生命宜居的必要条
件。科学家首次通过训练计算模型,结合卫星数据、火星车勘测图像和地球岩层的3D扫
描,绘制出远古火星土壤的侵蚀情况,而后发现一种被称为“滩鼻地貌”的陨坑结构,很可
能是远古河床的遗迹。该研究表明火星可能在远古时期存在过生命宜居的河流。基于
上述材料,下列说法正确的是
A. 火星上存在的陨坑结构可能是远古河床,可以推论远古时期火星上遍布各种河流
B.火星在远古时期存在过生命宜居的河流,可以得出远古时期火星上存在生命的结论
C.“火星上的陨坑结构很可能是远古河床的遗迹”是一个非对称性关系判断
D. 河流是地球生命宜居的必要条件,没有河流就不会有生命产生
```

【设问】 11.在地球上，河流对生命、化学、营养物质、沉积物的循环非常重要，是生命宜居的必要条件。科学家首次通过训练计算模型，结合卫星数据、火星车勘测图像和地球岩层的3D扫描，绘制出远古火星土壤的侵蚀情况，而后发现一种被称为“滩鼻地貌”的陨坑结构，很可能是远古河床的遗迹。该研究表明火星可能在远古时期存在过生命宜居的河流。基于上述材料，下列说法正确的是
A.火星上存在的陨坑结构可能是远古河床，可以推论远古时期火星上遍布各种河流
B.火星在远古时期存在过生命宜居的河流，可以得出远古时期火星上存在生命的结论
C.“火星上的陨坑结构很可能是远古河床的遗迹”是一个非对称性关系判断
D.河流是地球生命宜居的必要条件，没有河流就不会有生命产生

【怎么想到的】 题干最硬的逻辑句是“河流……是生命宜居的必要条件”。必要条件只能推出“没有河流就没有生命产生”。

【满分作答示范】 D 项正确。河流是生命宜居的必要条件，稳妥推理只能说没有河流便不具备生命宜居条件；可能有远古河床，不能推出遍布河流或已有生命。

【采分点对照】
- 答案选D
- 材料明说“河流是生命宜居的必要条件”，可保真的推理只能是否定必要条件：没有河流，就没有生命产生的宜居条件
- 由“可能有远古河床”不能扩展成遍布河流或已经有生命，D 的边界最稳
- 错项分析：A 项诱人，因为材料确实说陨坑结构“很可能是远古河床的遗迹”
- 错在从一个可能遗迹推到“遍布各种河流”，范围被夸大
- B 项诱人，因为河流和生命宜居有关
- 错在必要条件存在不等于结果已经存在，不能由“可能有河流”推出“存在生命”
- C 项诱人，因为句子里有“火星上的陨坑结构”和“远古河床的遗迹”两个表达
- 错在该句是在作可能性判断，不是在判断两个对象之间是否具有非对称关系

#### 7. 2026海淀二模 第5题（选择题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：题干用“只有这些数据被拆解成词元，人工智能才能分析运算”建立必要条件关系，把“数据被拆解成词元”放在不可缺少的位置。

【题目材料】

```text
5.词元,是人工智能大模型处理信息的最小信息单元,具有可计量、可定价、可交易的特征。人们每一次向人工智能提问、使用人工智能生成内容,都是在调用词元。无论是用户的提问,还是输入的代码,只有这些数据被拆解成词元,人工智能才能分析运算。对此分析正确的是
A.“词元”与“人工智能大模型处理信息的最小信息单元”在外延上是交叉关系
B.“输入的代码”和“词元”是属种关系
C.“这些数据被拆解成词元”,此处“被拆解成”关系为非对称关系
D.用户的提问没有被拆解成词元,则人工智能无法分析运算
```

【设问】 5．词元，是人工智能大模型处理信息的最小信息单元，具有可计量、可定价、可交易的特征。人们每一次向人工智能提问、使用人工智能生成内容，都是在调用词元。无论是用户的提问，还是输入的代码，只有这些数据被拆解成词元，人工智能才能分析运算。对此分析正确的是
A.“词元”与“人工智能大模型处理信息的最小信息单元”在外延上是交叉关系
B.“输入的代码”和“词元”是属种关系
C.“这些数据被拆解成词元”，此处“被拆解成”关系为非对称关系
D.用户的提问没有被拆解成词元，则人工智能无法分析运算

【怎么想到的】 一眼先抓“只有这些数据被拆解成词元，人工智能才能分析运算”。“只有……才……”把“被拆解成词元”放成必要条件。

【满分作答示范】 应选 D。题干说数据要先拆成词元，人工智能才有办法继续分析运算；现在用户提问没有被拆成词元，就是缺少必要条件，因而不能进行分析运算。A、B、C 都把词元说明误读成概念外延或充分条件方向，不能选。

【采分点对照】
- 答案选D
- 题干“只有这些数据被拆解成词元，人工智能才能分析运算”把“拆解成词元”设为必要条件
- 用户提问没有被拆解成词元，就是否定必要条件，可推出人工智能无法分析运算，不能转去判断概念外延关系
- 错项分析：A 项诱人，因为“词元”和后面一长串解释看起来像两个概念
- 错在二者是同一对象的名称与定义，外延相同，不是交叉关系
- B 项诱人，因为“输入的代码”会被拆成词元
- 错在“代码”是待处理的数据，“词元”是拆解后的信息单元，不是大类和小类
- C 项诱人，因为“被拆解成”确实有方向
- 错在它强调方向不可倒置，更接近反对称关系，不是该题能够推出的保真结论

### 必要条件与定义边界

#### 8. 2026石景山一模 第6题（选择题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：具身智能是具有身体的人工智能，但并非所有具有身体的人工智能都是具身智能。

【题目材料】

```text
6. 具身智能是指智能体通过身体与环境的互动产生的智能行为。从字面上理解,具身智能是指具有身体
的人工智能,但并非所有具有身体的人工智能都是具身智能,只有那些能像人一样感知、学习的人工智能,
才能称之为具身智能。如果材料内容为真,下列推断必然正确的是()
1具有身体的人工智能不是非具身智能
2有些具有身体的人工智能是能像人一样感知、学习的人工智能
3如果不能称之为具身智能,则是不能像人一样感知、学习的人工智能
4除非是能像人一样感知、学习的人工智能,否则不能称之为具身智能
A. 13
B. 14
C. 23
D. 24
```

【设问】 6.具身智能是指智能体通过身体与环境的互动产生的智能行为。从字面上理解，具身智能是指具有身体的人工智能，但并非所有具有身体的人工智能都是具身智能，只有那些能像人一样感知、学习的人工智能，才能称之为具身智能。如果材料内容为真，下列推断必然正确的是
①具有身体的人工智能不是非具身智能
②有些具有身体的人工智能是能像人一样感知、学习的人工智能
③如果不能称之为具身智能，则是不能像人一样感知、学习的人工智能
④除非是能像人一样感知、学习的人工智能，否则不能称之为具身智能
A.①③
B.①④
C.②③
D.②④

【怎么想到的】 先把“具身智能”的范围分清：它一定是“具有身体的人工智能”，但题干又明说“并非所有具有身体的人工智能都是具身智能”，所以大范围和小范围不能直接等同。再看“只有能像人一样感知、学习，才能称之为具身智能”，这里把“能感知、学习”放成必要条件。

【满分作答示范】 D 项正确。像人一样感知、学习只是具身智能成立的必要门槛；某对象不能称为具身智能，并不等于它一定没有感知学习能力，否定结果不能倒推否定必要条件。

【采分点对照】
- 答案选D
- 能像人一样感知、学习是称为具身智能的必要条件
- “不能称为具身智能”并不等于“不能感知学习”，否定后件不能反推否定必要条件
- 错项分析：①诱人，因为具身智能确实“具有身体”
- 错在题干说并非所有具有身体的人工智能都是具身智能，“有身体”仍覆盖具身与非具身两种可能
- ③诱人，因为它抓住了“只有能感知、学习，才能称为具身智能”
- 错在由“不能称为具身智能”反推“不能感知、学习”，是否定结果反推出否定必要条件，方向错

### 除非、否则与双重否定

#### 9. 2026朝阳二模 第6题（选择题）

【这道题考什么】 考必要条件假言推理。抓手是：题干说没有未来产业为载体，先进技术就无法形成现实生产能力，锁定未来产业是先进技术形成现实生产能力的必要条件。

【题目材料】

```text
6.未来产业是由前沿技术驱动,处于萌发阶段或产业化初期,具有显著战略性、引领性、颠覆性和不确定性的前瞻性产业。没有未来产业为载体,颠覆性技术就缺乏土壤,先进技术就无法形成现实的生产能力。未来产业涉及新业态,如果监管过严,会错失发展窗口期;如果完全放任自流,可能破坏市场秩序。从以上事实可以推出
A.除非对未来产业适度监管,否则就会破坏市场秩序
B.如果以未来产业为载体,先进技术就能形成现实的生产能力
C.未来产业没有高质量发展,不是缘于监管过严,就是缘于完全放任自流
D.有些具有显著战略性、引领性、颠覆性和不确定性的前瞻性产业不是非未来产业
```

【设问】 6．未来产业是由前沿技术驱动，处于萌发阶段或产业化初期，具有显著战略性、引领性、颠覆性和不确定性的前瞻性产业。没有未来产业为载体，颠覆性技术就缺乏土壤，先进技术就无法形成现实的生产能力。未来产业涉及新业态，如果监管过严，会错失发展窗口期；如果完全放任自流，可能破坏市场秩序。从以上事实可以推出
A.除非对未来产业适度监管，否则就会破坏市场秩序
B.如果以未来产业为载体，先进技术就能形成现实的生产能力
C.未来产业没有高质量发展，不是缘于监管过严，就是缘于完全放任自流
D.有些具有显著战略性、引领性、颠覆性和不确定性的前瞻性产业不是非未来产业

【怎么想到的】 题干里起支配作用的条件句是“没有未来产业为载体，先进技术就无法形成现实的生产能力”。这只能说明未来产业是先进技术形成现实生产能力的必要条件，不能倒过来说“只要以未来产业为载体，先进技术就一定能变成现实生产能力”。

【满分作答示范】 D 项正确。未来产业确有战略性、引领性、颠覆性和不确定性，所以可以推出部分前瞻性产业并非非未来产业；但以未来产业为载体不等于先进技术必然转化为现实生产能力。

【采分点对照】
- 答案选D
- 未来产业具有显著战略性、引领性、颠覆性和不确定性，所以有些具有这些特征的前瞻性产业不是非未来产业
- 但不能说只要以未来产业为载体，先进技术就一定形成现实生产能力
- 错项分析：A 项诱人，因为题干说“完全放任自流，可能破坏市场秩序”
- 错在“可能破坏”不能扩张成“不适度监管就会破坏”
- B 项诱人，因为题干说没有未来产业载体就不行
- 错在必要条件不是充分条件，有载体不等于一定形成现实生产能力
- C 项诱人，因为材料提到监管过严和完全放任两种风险
- 错在未来产业没有高质量发展的原因不一定只有这两种，选项把原因说窄了、说满了

### 必要条件与选言边界

#### 10. 2026海淀二模 第6题（选择题）

【这道题考什么】 考必要条件假言推理的边界。抓手是：广交会材料给出三条行文条件：有的未达最低出口额但有发展潜力的中小企业获得参展资格。

【题目材料】

```text
6. 第139届中国进出口商品交易会（广交会）于2026年4月在广州开幕，参展企业超3.2万家。记者在现场观察到以下情况：未达到最低出口额要求但具有发展潜力的中小企业获得了参展资格；只有参展企业拥有相关产品的自主知识产权，才能参加新品首发活动；参加新品首发活动的产品，须是全球市场或广交会首次发布的新产品。运用演绎推理方法，据此推出下列结论为真的是
①有的获得参展资格的企业是具有发展潜力的中小企业
②如果甲公司参加了新品首发活动，那么甲公司一定拥有相关产品的自主知识产权
③参展企业乙公司没能获批参加新品首发活动，可断定乙公司缺少相关产品的自主知识产权
④丙公司参加了新品首发活动，且其产品为广交会首次发布，那么该产品不是全球市场首次发布
A.①②
B.①③
C.②④
D.③④
```

【设问】 6.第139届中国进出口商品交易会（广交会）于2026年4月在广州开幕，参展企业超3.2万家。记者在现场观察到以下情况：未达到最低出口额要求但具有发展潜力的中小企业获得了参展资格；只有参展企业拥有相关产品的自主知识产权，才能参加新品首发活动；参加新品首发活动的产品，须是全球市场或广交会首次发布的新产品。运用演绎推理方法，据此推出下列结论为真的是
①有的获得参展资格的企业是具有发展潜力的中小企业
②如果甲公司参加了新品首发活动，那么甲公司一定拥有相关产品的自主知识产权
③参展企业乙公司没能获批参加新品首发活动，可断定乙公司缺少相关产品的自主知识产权
④丙公司参加了新品首发活动，且其产品为广交会首次发布，那么该产品不是全球市场首次发布
A.①②
B.①③
C.②④
D.③④

【怎么想到的】 广交会材料不要先看组合答案，先把三条观察分开。第一条直接给出“未达到最低出口额要求但具有发展潜力的中小企业获得了参展资格”，所以能推出①。

【满分作答示范】 A 项正确。①由材料中的存在事实直接支持；②依据“参加新品首发→拥有自主知识产权”这一必要条件关系成立。③把结果被否定倒推条件缺失，④误把相容选择当排斥选择。

【采分点对照】
- 答案选A
- ①直接来自“未达最低出口额但有发展潜力的中小企业获得参展资格”这个存在判断
- ②来自“只有拥有自主知识产权，才能参加新品首发活动”，肯定参加首发就必须肯定拥有知识产权
- ③是否定后件倒推条件，④把相容选言误排斥
- 错项分析：B 项把①和③放在一起，诱人是①确实成立
- 错在③由“没获批参加首发”反推“缺少自主知识产权”，必要条件推理方向反了
- C 项把②和④放在一起，诱人是②确实成立
- 错在④把“全球市场或广交会首次发布”看成互相排斥，实际材料只说至少满足其一
- D 项由③④组成，两个都错：一个是必要条件反推，一个是相容选言误读

### 相容选言里不要误排斥

#### 11. 2026西城二模 第5题（选择题）

【这道题考什么】 考选言推理或复合判断。抓手是：题干条件表达：该社区若参与竞选绿色宜居示范小区，就要解决餐饮油烟扰民问题或固定设备噪声扰民问题。

【题目材料】

```text
5.生态环境法典将“绿色低碳发展”单独成编,对噪声、油烟等群众“家门口”的顽疾作出专门规定。某社区落实法典精神,通过大家商量着办,制定了如下规则:
只有解决了餐饮油烟扰民问题,或解决了固定设备噪声扰民问题,该社区才能参与竞选绿色宜居示范小区。
据此,要必然推出“该社区解决了餐饮油烟扰民问题”,需要以下哪项作为前提
A.该社区解决了设备噪声扰民问题,但未入选示范社区
B.该社区未解决设备噪声扰民问题,但入选了示范社区
C.该社区解决了设备噪声扰民问题,且入选了示范社区
D.该社区未解决设备噪声扰民问题,且未入选示范社区
```

【设问】 5．生态环境法典将“绿色低碳发展”单独成编，对噪声、油烟等群众“家门口”的顽疾作出专门规定。某社区落实法典精神，通过大家商量着办，制定了如下规则：
只有解决了餐饮油烟扰民问题，或解决了固定设备噪声扰民问题，该社区才能参与竞选绿色宜居示范小区。
据此，要必然推出“该社区解决了餐饮油烟扰民问题”，需要以下哪项作为前提
A.该社区解决了设备噪声扰民问题，但未入选示范社区
B.该社区未解决设备噪声扰民问题，但入选了示范社区
C.该社区解决了设备噪声扰民问题，且入选了示范社区
D.该社区未解决设备噪声扰民问题，且未入选示范社区

【怎么想到的】 先把社区规则翻译成一句话：能参选或入选示范小区，至少要解决“油烟扰民”或“设备噪声扰民”中的一个。题目要推出“解决油烟扰民”，就必须同时看到两件事：一是社区已经入选，说明两个治理条件至少满足一个。

【满分作答示范】 B 项正确。规则可译为：入选示范社区要在油烟和噪声治理中至少解决一项。已入选又未解决噪声，就只能推出餐饮油烟已解决。

【采分点对照】
- 答案选B
- 规则可译为：入选示范社区必须至少解决油烟或噪声中的一个
- B 同时给出“入选”和“未解决噪声”，先触发必要条件中的选言支，再排除噪声支，剩下只能推出已解决餐饮油烟扰民问题
- 错项分析：A 项给出“解决设备噪声”且“未入选”，既不能说明示范条件被触发，也不能排除油烟项
- C 项给出“解决设备噪声”且“入选”，只说明至少一个条件已满足，不能推出另一个油烟问题也解决
- D 项给出“未解决设备噪声”但“未入选”，没有入选这个结果，就不能反推出必须解决油烟扰民

## 三、三段论、性质判断周延与换质位

【本类怎么做】
- 先找大项、小项、中项，再看中项有没有真正把两个前提接起来。
- 检查周延：结论里说尽的项，前提里也必须说尽。
- 换质、换位、换质位只能改形式，不能改原判断的意思。

【本类常见坑】
- 同一个词前后换对象，就是四概念错误。
- 大项或小项被结论偷偷扩大，三段论就无效。
- 省略前提题要补出隐藏大前提，不能只凭直觉连结。

### 先看三项：大项、小项、中项

#### 1. 2026东城期末 第17题第（2）问（主观题）

【这道题考什么】 考三段论。抓手是：有些采用居民提案-AI模拟-多轮投票模式的方案是科学民主方案。

【题目材料】

```text
17. 人形机器人“入职”汽车生产线，安防机器人智能巡逻，科研机器人在实验室“上岗”……场景作为系统性验证新技术、新产品、新业态的具体情境，赋能新质生产力发展。
材料一 推动场景创新，制度性障碍亟待破解。
障碍1：高价值数据产权界定模糊、缺乏开放机制。政府、央企等掌握核心场景和数据资源，民营企业在特定领域面临较高的市场准入门槛，各地各部门场景建设存在孤岛化问题。
障碍2：场景业主方与技术供给方之间信息不对称、信任成本高、交易效率低。大量场景富集地区“有场景、缺技术”，而科技企业集聚地方“有技术、缺场景”。
障碍3：场景数据价值、利益分配规则不清楚。新技术新产品首试首用的政策保险、容错机制尚未普及，缺乏有效的社会分担机制，抑制企业创新活力。
（1）在上述障碍中任选两个，分别提出政策性建议，并运用《经济与社会》知识，说明理由。
材料二 某市发布老城区“微更新+智慧场景”需求。以下是关于更新方案的一些主张。
主张1：我们既要完整保留历史街巷的一砖一瓦，也要对其中无法适应现代需要的部分进行必要的拆除和改造。
主张2：要提升垃圾分类效率，必须引入智能垃圾箱。因为，智能垃圾箱含有无接触投放和自动积分奖励功能，如果引入智能垃圾箱，垃圾分类效率就能得到提升。
主张3：有些科学民主的更新方案是采用“居民提案—AI智能模拟—多轮投票”模式制定的。“立体花园+口袋公园”复合型公共空间方案是通过此模式制定的。因此，“立体花园+口袋公园”复合型公共空间方案是科学民主的更新方案。
（2）运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）
```

【设问】 运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）

【怎么想到的】 两条前提都围绕“采用居民提案-AI模拟-多轮投票模式”这个中项展开，但大前提只是说“有些采用该模式的方案是科学民主方案”，并没有断定所有采用该模式的方案都属于科学民主方案。特称前提不能把中项覆盖充分，立体花园+口袋公园方案即使采用该模式，也不能必然推出它是科学民主方案。

【满分作答示范】 主张3不成立。中项在两个前提中都没有周延，只是分别同大项、小项有部分联系，不能把二者可靠连接；三段论要求中项至少周延一次。

【采分点对照】
- 主张3不符合逻辑
- 该三段论中，中项在大前提和小前提里都没有覆盖其全部外延，只是分别同大项、小项发生了部分联系，不能保证大项和小项之间一定建立联系
- 三段论要求中项至少周延一次，否则中项不能起到桥梁作用，因此该推理犯中项不周延错误，结论不能成立

#### 2. 2026丰台一模 第18题第（2）问（主观题）

【这道题考什么】 考三段论。抓手是：乙的推理把“带动居民消费”放在大项位置。

【题目材料】

```text
18.（14分）
2026年《政府工作报告》提出,深入实施提振消费专项行动。某班同学在时事
学习中,查阅到以下资料,展开讨论。
用好“加减乘除”推动消费持续增长
“加法”,重在强基固本。制
定实施城乡居民增收计划,促进低
收入群体增收、扩大居民财产性收
入;同时推进消费新业态新模式新场景试点,大力培育文旅、体育
赛事和演艺经济等消费场景,增加
优质产品和服务供给。
“减法”,重在解除后顾之忧。
加大在医疗、养老和生育养育等方
面的保障力度:提高医保补助标准,
提高城乡居民基础养老金月最低标
准,发展普惠托育服务、探索育儿
补贴等。
“乘法”,重在发挥财政资金
乘数效应。今年政府将安排超长期
特别国债2500亿元支持消费品以旧
换新、进一步加大对线下实体零售
的支持力度,集中支持汽车、冰箱
和智能眼镜等重点消费品以旧换新,
换出新赛道和新动能。
“除法”,重在破壁清障,进
一步清理各类消费限制性措施。比如,
针对消费市场中存在的隐性壁垒进
行分类施策,简化促销活动的审批
流程;在一些城市进一步放宽车辆
购买限制、增发购车指标等。
(1)运用《经济与社会》知识,分析“加减乘除”在推动消费持续增长的过程
中是怎样发挥作用的。（8分）
在讨论过程中,两位同学作出如下推理。
甲:只有各项提振消费的举措扎实落地,才能有效释放消费潜力。如果消费潜力
得到有效释放,那么各项提振消费的举措已经扎实落地了。
乙:产品质量的提升能够带动居民消费,改善消费环境不能提升产品质量。所
以,改善消费环境不能带动居民消费。
(2)分别写出上述推理的类型,判断是否正确,并说明理由。（6分）
```

【设问】 分别写出上述推理的类型，判断是否正确，并说明理由。（6分）

【怎么想到的】 乙的结论把“带动居民消费”说得很满，但这个大项在前提里并没有被充分覆盖。判断三段论不能停在生活结论是否顺耳，而要看项的周延范围有没有变化：前提只是把某类对象同居民消费建立联系，结论却把“带动居民消费”的外延扩大为更满的判断。

【满分作答示范】 乙推理错误，犯大项不当扩大。前提没有把“带动居民消费”的范围说尽，结论却把它扩大成确定判断，超出前提保证。

【采分点对照】
- 乙的推理属于三段论，错误在于大项不当扩大
- 大项“带动居民消费”在前提中只是作为某类情况的部分属性被使用，并没有被周延断定
- 结论却把这一属性扩大为确定判断，超出了前提允许的范围，所以大小项之间没有被前提可靠连接，结论不合逻辑

### 三段论形式正确，前提仍要真实

#### 3. 2026顺义一模 第19题第（1）问（主观题）

【这道题考什么】 考三段论。抓手是：推理先把“所有由前沿技术驱动，具有前瞻性、战略性、颠覆性特点的产业都是未来产业”当作大前提，再把量子科技归入这个前提，推出“量子科技是未来产业”。

【题目材料】

```text
19.（15分）“十五五”开局之年，我国将加快培育和发展未来产业，以现代化产业新优势把握未来发展主动权。
材料一 未来产业由前沿技术驱动，具有前瞻性、战略性、颠覆性等特点。“十五五”规划建议提出，推动量子科技、生物制造、氢能和核聚变能、脑机接口、具身智能、第六代移动通信等成为新的经济增长点，这些领域正是未来产业的典型代表。
据此，某同学得出以下推论：
所有由前沿技术驱动，具有前瞻性、战略性、颠覆性特点的产业都是未来产业。
量子科技是由前沿技术驱动，具有前瞻性、战略性、颠覆性特点的产业。
量子科技是未来产业。
（1）判断上述推理是否正确，并说明理由。（3分）
```

【设问】 判断上述推理是否正确，并说明理由。（3分）

【怎么想到的】 关键不只是三段论格式是否成立，而是演绎推理能否保真：既要推理结构正确，也要前提真实。这个推理形式上符合三段论规则，但材料只说未来产业具有这些特点，不能反过来必然推出“所有具有这些特点的产业都是未来产业”。

【满分作答示范】 结论不能成立。这个论证形式上可整理为三段论，但隐藏的大前提把所有具备前瞻、战略、颠覆特征的产业都归为未来产业，材料并不能保证这一点；前提不真，结论就不能保真。

【采分点对照】
- 该推理错误
- 它虽然可以整理成三段论形式，大小项和中项的连接结构也看似符合规则，但大前提“所有具有前瞻性、战略性、颠覆性特点的产业都是未来产业”不能由材料必然推出，不是真实可靠的判断
- 演绎推理要保证结论可靠，不仅形式要有效，前提也必须真实，因此不能据此断定量子科技必然属于未来产业

### 补大前提：把省略规则说出来

#### 4. 2026东城期末 第6题（选择题）

【这道题考什么】 考三段论。抓手是：题干已经给出小前提“乌毛蕨形成的镧独居石是纯净无辐射的独居石”，结论却要推出“乌毛蕨形成的镧独居石具有绿色提取前景”。

【题目材料】

```text
6. 独居石是工业上重要的稀土矿石,但天然独居石中常伴生放射性元素。我国科研人员发现稀土元素在乌
毛蕨植物体内可生物成矿,形成一种名为“镧独居石”的矿物,这种独居石纯净无辐射。若具备下述哪个
前提,“乌毛蕨形成的镧独居石具有绿色提取前景”的结论必然成立( )
A. 只有纯净无辐射的独居石,才有绿色提取前景
B. 只有具有绿色提取前景的,才是纯净无辐射的独居石
C. 有的纯净无辐射的独居石具有绿色提取前景
D. 部分生物成矿形成的矿物具有绿色提取前景
```

【设问】 6. 独居石是工业上重要的稀土矿石，但天然独居石中常伴生放射性元素。我国科研人员发现稀土元素在乌毛蕨植物体内可生物成矿，形成一种名为“镧独居石”的矿物，这种独居石纯净无辐射。若具备下述哪个前提，“乌毛蕨形成的镧独居石具有绿色提取前景”的结论必然成立（ ）
A.只有纯净无辐射的独居石，才有绿色提取前景
B.只有具有绿色提取前景的，才是纯净无辐射的独居石
C.有的纯净无辐射的独居石具有绿色提取前景
D.部分生物成矿形成的矿物具有绿色提取前景

【怎么想到的】 这里不是问独居石知识，而是给三段论补一块能保真的桥。先抓已知小前提：乌毛蕨形成的镧独居石属于纯净无辐射的独居石。

【满分作答示范】 B 项正确。题面已给出乌毛蕨生成的是干净且无辐射的镧独居石，结论要落到绿色提取前景；B 项补上的桥梁是：凡属这类独居石，就具备绿色提取前景。

【采分点对照】
- 答案选B
- 题干小前提已经有“乌毛蕨形成的镧独居石是纯净无辐射的独居石”，结论要得到“有绿色提取前景”
- B 的“只有具有绿色提取前景的，才是纯净无辐射的独居石”可译为纯净无辐射的独居石必有绿色提取前景，正好补上大前提
- 错项分析：A 项诱人，因为也出现了“纯净无辐射”和“绿色提取前景”
- 错在它说的是有绿色提取前景才纯净无辐射，不能由“纯净无辐射”推出“有绿色提取前景”
- C 项诱人，因为它直接把纯净无辐射和绿色前景放在一起
- 错在“有的”不能保证乌毛蕨形成的这块镧独居石就在其中
- D 项诱人，因为题干提到生物成矿
- 错在“部分生物成矿形成的矿物”范围太散，不能作为连接当前小项和大项的大前提

### 四概念：同一个词前后换了对象

#### 5. 2026西城一模 第19题第（3）问（主观题）

【这道题考什么】 考概念、定义或划分规则。抓手是：甲把“补偿问题”和“公共利益”处理成只能二选一的关系，又把公共利益理解得过窄，忽略了集体决策中个人利益与公共利益可能同时被协调的空间。

【题目材料】

```text
19.（12分）推进美丽乡村建设、完善乡村公共服务。
材料一 某村规划建设集休闲健身、生态绿化、文化展示于一体的文化生态公园,却在推进中却遭遇一连串难题:
乡镇政府:必须严守项目预算、建设标准、生态红线
村“两委”、村干部:担心规划与民意脱节、项目推进受阻
邻村及本村土地被占用村民:担心个人利益受损,有一定抵触情绪
外出务工村民:无法回村参与,担心自己的诉求被忽略
材料二 面对多方意见,村党支部创新推行“云端+院落夜话”议事机制(右图):一方面,线上议事群实时发布议题、收集意见,组织视频连线让外出村民全程参与讨论;另一方面,在院落、广场组织大家面对面商量,直接回应涉地村民的实际诉求。同时,联动政府、村干部与村民代表,在村规划、生态保护和群众利益之间找到平衡点,最终形成方案,推动实施。
(1)遵循民主程序要求,将右图最后一环节补充完整。（1分）
(2)结合材料,运用《政治与法治》知识,谈谈“云端+院落夜话”议事机制是如何破解“一连串难题”的。（7分）
(3)任选两位村民的观点,运用形式逻辑知识,说明其理解是否正确。（4分）
甲:议事协商应维护公共利益,个人补偿诉求不是公共利益,所以个人补偿诉求不应纳入议事协商。
乙:对于村务公开,我既不同意“所有村务必须公开”,也不同意“所有村务都不必公开”。
丙:只要涉及村民切身利益,就应由村民会议讨论决定。村委会没有讨论这件事,说明这件事不涉及村民切身利益。
```

【设问】 任选两位村民的观点，运用形式逻辑知识，说明其理解是否正确。（4分）

【怎么想到的】 甲的说法把“个人补偿诉求”和“公共利益”说成非此即彼，好像只要村民提出个人补偿，就不能再被放进公共利益的讨论中。这里要先看中项有没有保持同一：公共利益本来指整体、可共享的利益，并不排斥正当个人利益。

【满分作答示范】 甲观点错误。个人补偿诉求并不必然排斥公共利益；甲又把公共利益的范围压窄，导致前后使用的“公共利益”不是同一概念，犯四概念错误，不能排除村民正当补偿诉求。

【采分点对照】
- 甲观点错误
- 甲把个人补偿诉求与公共利益处理成非此即彼，前提并不真实
- 同时又把公共利益的外延窄化，使推理前后“公共利益”的概念范围不一致，造成四概念错误，不能据此排除村民正当补偿诉求进入集体协商

### 大项扩大：结论说得比前提更满

#### 6. 2025顺义一模 第7题（选择题）

【这道题考什么】 考三段论。抓手是：A 项把结论中被周延的“青年”错误归名为“小项不当扩大”。

【题目材料】

```text
7．下列三段论的逻辑分析错误的是（ ）
A．凡共青团员都是青年，并非所有的青年工人都是共青团员，所以并非所有的青年工人都是青年。
不正确，一个形式结构正确的三段论前提中不周延的项在结论中不得周延，该三段论犯了“小项不当扩大”的逻辑错误。
B．调查报告不是文学作品，这篇文稿不是调查报告，所以这篇文稿不是文学作品。
不正确，一个形式结构正确的三段论，两个否定的前提不能必然推出结论，结论为否定当且仅当前提中有一否定。
C．物质是不灭的，这支钢笔是物质，所以这支钢笔是不灭的。
不正确，一个形式结构正确的三段论只能有三个不同的项，该三段论犯了“四概念”的逻辑错误。
D．有些农民是劳动模范，有些农民是党员，所以有些党员是劳动模范。
不正确，一个形式结构正确的三段论中项在前提中至少周延一次，该三段论犯了“中项不周延”的逻辑错误。
A．A
B．B
C．C
D．D
```

【设问】 7. 下列三段论的逻辑分析错误的是（ ）
A. 凡共青团员都是青年，并非所有的青年工人都是共青团员，所以并非所有的青年工人都是青年。不正确，一个形式结构正确的三段论前提中不周延的项在结论中不得周延，该三段论犯了“小项不当扩大”的逻辑错误。
B. 调查报告不是文学作品，这篇文稿不是调查报告，所以这篇文稿不是文学作品。不正确，一个形式结构正确的三段论，两个否定的前提不能必然推出结论，结论为否定当且仅当前提中有一否定。
C. 物质是不灭的，这支钢笔是物质，所以这支钢笔是不灭的。不正确，一个形式结构正确的三段论只能有三个不同的项，该三段论犯了“四概念”的逻辑错误。
D. 有些农民是劳动模范，有些农民是党员，所以有些党员是劳动模范。不正确，一个形式结构正确的三段论中项在前提中至少周延一次，该三段论犯了“中项不周延”的逻辑错误。

【怎么想到的】 判断三段论错误时，不能停在选项有没有说出一条规则，而要先按结论定大项、小项。结论否定的是“青年工人”和“青年”之间的关系，“青年”在结论中作谓项，是大项。

【满分作答示范】 A 项正确。该三段论确有项扩大，但扩大的是结论谓项“大项”青年，不是主项“小项”青年工人；选项把错误名称说反。

【采分点对照】
- 答案选A
- A 项要求选“逻辑分析错误”
- 它的三段论确实有“前提不周延、结论周延”的项扩大问题，但被扩大的项是结论中的大项“青年”，不是小项“青年工人”，所以错误名称写错，应判为大项不当扩大
- 错项分析：B 项诱人，因为它也说“不正确”，但两个否定前提不能必然推出结论，这一分析是对的
- C 项诱人，因为推理句式很短
- 错因分析也对，前一个“物质”是哲学意义上的物质，后一个“物质”指具体物体，犯四概念错误
- D 项诱人，因为两个前提都有“农民”
- 但中项“农民”在两个特称肯定判断中都不周延，所以“中项不周延”的分析也是对的

### 小项扩大：主语范围被偷偷放大

#### 7. 2024朝阳二模 第7题（选择题）

【这道题考什么】 考三段论。抓手是：自媒体是思想政治教育的工具。

【题目材料】

```text
7. 科学思维离不开逻辑。下列表述中，合乎逻辑的是
A.自媒体是思想政治教育的工具，自媒体也是娱乐的工具，所以，娱乐工具都是思想政治教育的工具。
B.归纳推理是从个别性前提推出一般性结论的推理。我学过归纳推理，所以，我能推出一般性结论和新知识体系。
C.只有既弄清对象的性质，又了解对象之间的关系，才能对对象有较为全面的把握。我善于弄清对象的性质，所以，我特别善于进行关系判断。
D.如果推理结构不正确，也就是说，前提和结论的逻辑联系方式是错误的，那么，尽管前提真实，也不能保证推出正确的结论。
```

【设问】 7.科学思维离不开逻辑。下列表述中，合乎逻辑的是
A.自媒体是思想政治教育的工具，自媒体也是娱乐的工具，所以，娱乐工具都是思想政治教育的工具。
B.归纳推理是从个别性前提推出一般性结论的推理。我学过归纳推理，所以，我能推出一般性结论和新知识体系。
C.只有既弄清对象的性质，又了解对象之间的关系，才能对对象有较为全面的把握。我善于弄清对象的性质，所以，我特别善于进行关系判断。
D.如果推理结构不正确，也就是说，前提和结论的逻辑联系方式是错误的，那么，尽管前提真实，也不能保证推出正确的结论。

【怎么想到的】 四个选项里只有 D 是在讲一个稳妥的推理要求：结构不对，即使前提真，也不能保证结论真。A 项最像三段论，但要小心它把“自媒体也是娱乐的工具”里的“娱乐工具”从谓项位置，直接放到结论里说成“娱乐工具都是思想政治教育的工具”，范围被突然放大了。

【满分作答示范】 D 项正确。形式逻辑要求结构有效；A 项虽像三段论，但“娱乐工具”在前提中没有周延，结论中却周延，犯小项不当扩大。

【采分点对照】
- 答案选D
- D 说的是形式逻辑的底线：推理结构不正确，即使前提真实，也不能保证推出正确结论
- A 项作为干扰最像三段论，但“娱乐工具”在前提中不周延、结论中周延，犯小项不当扩大
- B、C 也都越过了前提能保证的范围
- 错项分析：A 项诱人，因为它看起来有两个前提和一个结论
- 错在“娱乐工具”在前提里没有被整体断定，结论却断定所有娱乐工具都是思想政治教育工具，犯小项不当扩大
- B 项诱人，因为归纳推理确实能从个别推出一般
- 错在学过概念不等于已经具备推出一般结论和新知识体系的能力
- C 项诱人，因为题干有“只有……才……”
- 错在只具备弄清性质这一项，不能推出对关系判断特别擅长

### 构造三段论：先定中项桥梁

#### 8. 2025房山一模 第16题第（2）问（主观题）

【这道题考什么】 考三段论。抓手是：大项=保护和传承人类文明的重要殿堂。

【题目材料】

```text
16. 阅读材料,回答问题。
博物馆是保护和传承人类文明的重要殿堂,是连接过去、现在、未来的桥梁。打卡博物馆成为假期
“顶流”,某班同学畅谈活动体验。
同学甲北京古代建筑博物馆的天宫藻井冰箱贴成为文创界“顶流”。我五天蹲点抢号终于成功购买,
这不仅仅是“跟风”,而是希望能通过文创产品,了解其背后的藻井、星宿图等文物及其背后的历史故事。
同学乙走进殷墟博物馆新馆,很震撼。博物馆运用了裸眼3D 技术,将跪坐玉人、亚长牛尊等20 多件商代
珍贵文物,在同一空间生动呈现。同时,文物展柜采用了数字虚拟影像技术,与静态文物进行叠加,能立
体化感受文物魅力,有很多游客前去参观。
同学丙有的博物馆门可罗雀,有的一票难求,有的人头攒动、展厅嘈杂,有的显示屏在闪、在发出声
音。也有一种比较浮躁的现象,比如有相当一部分人直奔盖章处集章,或者只在几个明星文物前拍照打卡。
(1)综合材料,运用《哲学与文化》知识,谈谈如何看待“博物馆热”。
(2)请以“博物馆是保护和传承人类文明的重要殿堂”为结论,编写一个合乎规则的三段论。
有人说,逛北京,一定要来房山看看,因为这里有一座勾勒三千年前北京城样貌的北京考古遗址博物
馆——琉璃河遗址。琉璃河遗址出土的青铜罍(léi)上的斑驳铭文沉淀着三千年时光,两重城垣见证着
北京最早的建城印记。考古成果从不同角度证实了北京自西周时期开始的城市建设史,是首都北京三千余
年赓续不断建城史的开端,具有极为重要的学术价值。
(3)结合材料,运用创新思维知识,就“如何让琉璃河遗址‘热’起来”提两条建议。
```

【设问】 请以“博物馆是保护和传承人类文明的重要殿堂”为结论，编写一个合乎规则的三段论。

【怎么想到的】 题目已经把结论给死：“博物馆是保护和传承人类文明的重要殿堂”。先抓结论里的两个端点：小项是“博物馆”，大项是“保护和传承人类文明的重要殿堂”。

【满分作答示范】 可写成三段论：凡具有教育功能的场所，都属于保护和传承人类文明的重要殿堂；博物馆具有教育功能；因此，博物馆属于保护和传承人类文明的重要殿堂。中项是“具有教育功能的场所”。

【采分点对照】
- 可构造三段论：具有教育功能的场所是保护和传承人类文明的重要殿堂
- 博物馆是具有教育功能的场所
- 博物馆是保护和传承人类文明的重要殿堂
- 中项“具有教育功能的场所”在两个前提中连接大项和小项，使结论从共同前提中推出

#### 9. 2024丰台二模 第18题第（1）问（主观题）

【这道题考什么】 考三段论。抓手是：中项是“搭建对外交流合作平台”，大项是“推动冰雪经济高质量发展”，小项是“第七届雪博会”。

【题目材料】

```text
18.（19分）“冷资源”生成“热经济”,推动冰雪经济高质量发展。
火热的冰雪经济激发了同学们探究的热情,同学们查阅资料如下:
• 为推动冰雪经济发展,我国陆续出台《冰雪运动发展规划(2016—2025年)》
《关于释放旅游消费潜力推动旅游业高质量发展的若干措施》等相关政策。
• 依据相关报告显示,2022-2023冰雪季我国冰雪休闲旅游人数为3.12亿人次,冰
雪休闲旅游收入为3490亿元;2023-2024 冰雪季我国冰雪休闲旅游人数突破4亿
人次,冰雪休闲旅游收入超过5000亿元。
• 第七届雪博会共有来自9个国家27个省份近3000 名嘉宾和参展商现场参会,冰
雪装备、冰雪旅游、冰雪文化、冰雪体育、冰雪商贸等五大领域 455 家参展商参
展,累计参展观众达到14.04万人次,现场交易额达2.83亿元,创历届新高。
• 我国冰雪资源丰富,但由于地理气候等差异,目前国内比较好的室外场地往往局
限于一地或者一个区域,难以实现全季运营。我国冰雪装备制造企业以中小企业为主,产业链不健全、行业标准亟须完善;研发人才不足、研发投入较少、核心
技术欠缺,一些高端冰雪装备市场仍被国外品牌占据。
围绕如何推动冰雪经济高质量发展,同学们结合以上材料进行探究。
(1)结合材料,同学们构建了一个符合逻辑规则的三段论,请你补充完整。（5分）
大前提:
小前提:
结论:
可以推动冰雪经济高质量发展。
(2) 有同学认为,只要我们能够准确预测冰雪经济的发展前景,就能推动冰雪经济高
质量发展。结合材料,运用科学思维对该观点进行评析。（6分）
(3)经过探究,同学们从《经济与社会》角度,对如何利用“冷资源”撬动“热经
济”形成以下共识:
-。（8分）
```

【设问】 结合材料，同学们构建了一个符合逻辑规则的三段论，请你补充完整。（5分）

【怎么想到的】 这里不是评价冰雪经济，而是把材料里的关系搭成三段论。结论是“第七届雪博会可以推动冰雪经济高质量发展”，所以小项是“第七届雪博会”，大项是“推动冰雪经济高质量发展”。

【满分作答示范】 可写成三段论：凡能搭建对外交流合作平台的活动，都有助于冰雪经济高质量发展；第七届雪博会搭建了此类平台；所以，第七届雪博会有助于推动冰雪经济高质量发展。

【采分点对照】
- 可构造三段论：搭建对外交流合作平台能够推动冰雪经济高质量发展
- 第七届雪博会是对外交流合作平台
- 第七届雪博会可以推动冰雪经济高质量发展
- 中项“对外交流合作平台”把雪博会和冰雪经济高质量发展连接起来

### 有效结构：形式有效还要看前提

#### 10. 2025朝阳期末 第19题（主观题）

【这道题考什么】 考三段论。抓手是：所有为维护小区美好环境付出辛勤劳动的行为都是值得赞扬的。

【题目材料】

```text
19.（7分）
某小区居民讨论冬季应该如何开展扫雪工作。
甲:我不同意使用融雪剂,但是我也不同意禁止使用融雪剂。
乙:扫雪工作既要快速完成方便居民出行,又要慢慢清扫以免遗漏任何一处积雪。
丙:所有为维护小区美好环境付出辛勤劳动的行为都是值得赞扬的。居民在小区扫雪是为维护小区美
好环境付出辛勤劳动的行为。所以,居民在小区扫雪是值得赞扬的。
结合材料,运用《逻辑与思维》知识,分析上述居民的话是否合乎逻辑,说明理由。
```

【设问】 结合材料，运用《逻辑与思维》知识，分析上述居民的话是否合乎逻辑，说明理由。

【怎么想到的】 丙的话已经是一个完整三段论：大前提说“为维护小区美好环境付出辛勤劳动的行为”都值得赞扬，小前提说“居民在小区扫雪”属于这种行为，结论说“居民在小区扫雪值得赞扬”。触发点不只是扫雪话题，而是三个项有没有固定下来、前提是否真实、结构是否把小项经由中项连到大项。

【满分作答示范】 丙的推理可按三段论处理：大前提把一类对象同某属性联系起来，小前提把当前对象归入这一类，结论再把该属性推出到当前对象上。只要前提真实，中项能连接大小项，且大小项外延没有被不当扩大，结论就能从前提中推出。

【采分点对照】
- 丙的推理属于三段论
- 大前提把一类对象与属性建立联系，小前提把当前对象归入该类，结论再把该属性推出到当前对象上
- 只要两个前提真实，中项在前提中能够连接大项和小项，且没有扩大项的外延，结论就能从前提中必然推出，所以结构符合三段论规则

### 有效形式与真实前提要分开

#### 11. 2024东城一模 第7题（选择题）

【这道题考什么】 考三段论。抓手是：推理的三项结构很完整：大前提说“所有鸟都会飞”，小前提说“鸵鸟是鸟”，结论推出“鸵鸟会飞”。

【题目材料】

```text
7. “所有鸟都是会飞的，鸵鸟是鸟，所以，鸵鸟是会飞的。”对此推理分析正确的是
①符合三段论推理规则，其推理形式有效
②大前提是假的，其推理的结论不正确
③该三段论推理属于必然性推理，其推理的结论是正确的
④违背三段论只能有三个不同项的规则，犯了“四概念”的错误
A.①②
B.①③
C.②④
D.③④
```

【设问】 7.“所有鸟都是会飞的，鸵鸟是鸟，所以，鸵鸟是会飞的。”对此推理分析正确的是
①符合三段论推理规则，其推理形式有效
②大前提是假的，其推理的结论不正确
③该三段论推理属于必然性推理，其推理的结论是正确的
④违背三段论只能有三个不同项的规则，犯了“四概念”的错误
A.①②
B.①③
C.②④
D.③④

【怎么想到的】 材料容易被“鸵鸟不会飞”带跑。判断时要同时看形式和前提：从形式看，它是“所有 M 是 P，S 是 M，所以 S 是 P”；从内容看，大前提“所有鸟都会飞”不真实，因此形式有效不等于结论真实。

【满分作答示范】 A 项正确。它的结构可写成：凡 M 为 P，S 归入 M，故 S 归入 P；三项未偷换，形式有效。但“所有鸟都会飞”这个前提不真，所以鸵鸟会飞的结论为假。

【采分点对照】
- 答案选A
- 这个推理的形式是“所有 M 是 P，S 是 M，所以 S 是 P”，三项位置没有偷换，结构有效，故①成立
- 但大前提“所有鸟都是会飞的”不符合事实，前提为假导致结论“鸵鸟会飞”不正确，故②成立
- 形式有效不等于结论真实
- 错项分析：③诱人，因为这是演绎推理，形式上有必然性
- 错在演绎推理要前提真实且形式有效，才保证结论真实
- ④诱人，因为结论错了，常见误区是以为形式犯规
- 错在这个推理只有“鸟、会飞的、鸵鸟”三个项，没有偷换成第四个概念，问题在大前提不真

### 周延性：看概念有没有被说尽

#### 12. 2024丰台一模 第7题（选择题）

【这道题考什么】 考性质判断的周延性。抓手是：文段连续使用“法是维持社会秩序、调整社会关系的一种社会规范”“法是由国家制定或认可的社会规范”等肯定性质判断，其中“社会规范”反复作为谓项出现。

【题目材料】

```text
7.
“法者,治之端也。”法是维持社会秩序、调整社会关系的一种社会规
范。法是由国家制定或认可的社会规范。法是由国家强制力保证实施的
具有普遍约束力的社会规范。
对上述文段的分析正确的是
A. 上述文段存在假言判断
B. 法律和社会规范是属种关系
C.“社会规范”在文中是不周延的
D.“法者,治之端也。”是特称肯定判断
```

【设问】 7.“法者，治之端也。”法是维持社会秩序、调整社会关系的一种社会规范。法是由国家制定或认可的社会规范。法是由国家强制力保证实施的具有普遍约束力的社会规范。对上述文段的分析正确的是
A.上述文段存在假言判断。
B.法律和社会规范是属种关系。
C.“社会规范”在文中是不周延的。
D.“法者，治之端也”是特称肯定判断。

【怎么想到的】 这段话反复说“法是……社会规范”。要盯住这个句式：它不是“如果……那么……”的假言判断，而是在作肯定性质判断。

【满分作答示范】 C 项正确。文段中的“法是……社会规范”是肯定性质判断，谓项“社会规范”没有被说尽，只表明法归入这一范围，并未断定所有社会规范都是法。

【采分点对照】
- 答案选C
- 文段反复使用“法是……社会规范”的肯定性质判断
- 肯定判断的谓项通常不周延，所以“社会规范”只是被用来说明法所属的范围，并没有断定全部社会规范
- A、D误判判断类型，B没有抓住周延性
- 错项分析：A 项诱人，因为文段有多个判断
- 错在没有“如果……那么……”这类条件结构
- B 项诱人，因为法确实属于社会规范
- 错在选项没有抓住题干反复出现的肯定判断谓项不周延，且把“法是社会规范的一种”的方向说得不够严格
- D 项诱人，因为“法者，治之端也”看起来像一句判断
- 错在它不是“有的……”这种特称肯定判断

### 换位边界：不是每句话都能倒过来

#### 13. 2024海淀二模 第6题（选择题）

【这道题考什么】 考三段论的边界。抓手是：特别国债是国债分类中的一种。

【题目材料】

```text
6.我国发行的国债,按照发行对象和资金用途,可分为普通国债、定向国债、专项国债和特别国
债。其中,特别国债具有专款专用、用途灵活、不列入财政赤字等特点,可为财政有效开源
增支,是助力经济增长的增量工具。超长期特别国债是指发行期限10 年以上的特别国债。基
于上述内容,下列说法正确的是
A.“专项国债”与“特别国债”的外延是矛盾关系
B.“特别国债”与“超长期特别国债”的外延是种属关系
C.“发行期限10 年以上”反映了超长期特别国债的属性
D.经换位推理可得出“助力经济增长的增量工具是特别国债”
```

【设问】 6. 我国发行的国债，按照发行对象和资金用途，可分为普通国债、定向国债、专项国债和特别国债。其中，特别国债具有专款专用、用途灵活、不列入财政赤字等特点，可为财政有效开源增支，是助力经济增长的增量工具。超长期特别国债是指发行期限10年以上的特别国债。基于上述内容，下列说法正确的是
A.“专项国债”与“特别国债”的外延是矛盾关系
B.“特别国债”与“超长期特别国债”的外延是种属关系
C.“发行期限10年以上”反映了超长期特别国债的属性
D.经换位推理可得出“助力经济增长的增量工具是特别国债”

【怎么想到的】 把材料里的两个层次分开：普通、定向、专项、特别国债是国债下面的不同类别；超长期特别国债则是在特别国债里面再按发行期限划出的更小范围。

【满分作答示范】 C 项正确。定义里“发行期限十年以上”用于区分超长期特别国债；材料只说明特别国债是一种增量工具，不能把主谓位置倒转为所有增量工具都是特别国债。

【采分点对照】
- 答案选C
- “超长期特别国债是指发行期限10年以上的特别国债”中，“发行期限10年以上”就是区别于其他特别国债的属性
- 材料只说特别国债可作为助力经济增长的增量工具，不能简单换位成所有增量工具都是特别国债
- 错项分析：A 项诱人，因为专项国债和特别国债同属国债分类
- 错在同一分类下的两个类别不是“非此即彼且合起来穷尽全部”的矛盾关系
- B 项诱人，因为超长期特别国债确实属于特别国债
- 错在选项把两个概念的属种方向说得不严
- D 项诱人，因为“特别国债是增量工具”看起来能倒过来说
- 错在肯定判断不能随手把主谓倒置，否则会把增量工具的范围不当地缩成特别国债

### 类比与换位换质不要混判

#### 14. 2026门头沟一模 第6题（选择题）

【这道题考什么】 考类比推理与换质位法。抓手是：EAST因模拟太阳内部核聚变反应而被称为人造太阳。

【题目材料】

```text
6. EAST 装置被称为“人造太阳”，模拟太阳内部的核聚变反应。中国科学院磁约束核聚变大科学工程团队成功实现了超过1亿度、1066秒稳态长脉冲高约束模等离子体运行，再次创造了托卡马克装置高约束模运行新的世界纪录。据此，下列判断或推理正确的是
①将 EAST 装置称作“人造太阳”，是根据其与太阳核聚变的相似性进行的类比推理
②“EAST 装置”与“模拟太阳核聚变的装置”两个概念的外延关系，属于属种关系
③有些模拟太阳核聚变的装置是 EAST 装置，因此，有些 EAST 装置不是非模拟太阳核聚变的装置
④托卡马克装置是开展核聚变研究的装置，EAST 装置是托卡马克装置，开展核聚变研究的装置是 EAST 装置
A.①③
B.①④
C.②③
D.②④
```

【设问】 6.EAST 装置被称为“人造太阳”，模拟太阳内部的核聚变反应。中国科学院磁约束核聚变大科学工程团队成功实现了超过1亿度、1066秒稳态长脉冲高约束模等离子体运行，再次创造了托卡马克装置高约束模运行新的世界纪录。据此，下列判断或推理正确的是
①将EAST 装置称作“人造太阳” ，是根据其与太阳核聚变的相似性进行的类比推理
②“EAST 装置”与“模拟太阳核聚变的装置”两个概念的外延关系，属于属种关系
③有些模拟太阳核聚变的装置是EAST 装置，因此，有些EAST 装置不是非模拟太阳核
聚变的装置
④托卡马克装置是开展核聚变研究的装置，EAST 装置是托卡马克装置，开展核聚变研
究的装置是EAST 装置
A.①③ B.①④ C.②③ D.②④

【怎么想到的】 材料有两个入口。“人造太阳”不是给 EAST 下定义，而是抓住它与太阳都涉及核聚变反应这一相似属性，由太阳类推 EAST 的功能特征，触发类比推理。

【满分作答示范】 A 项正确。①把 EAST 与太阳在核聚变上的相似点迁移到“人造太阳”称谓，属于类比。③由“有些模拟太阳核聚变的装置是 EAST”换位再换质，形式可以保真。

【采分点对照】
- 答案选A
- ①抓住 EAST 与太阳都涉及核聚变反应的相似性，由相似属性推出称作“人造太阳”，属于类比推理
- ③从“有些模拟太阳核聚变的装置是 EAST”出发，换位后再换质，形式保真
- ④把大范围谓项倒过来，属于不当换位
- 错项分析：B 项含①④，①正确但④把“托卡马克装置”与“开展核聚变研究的装置”的范围倒置，推理无效
- C 项含②③，③正确但②把单个装置与一类装置误判为属种关系
- D 项含②④，两个判断都不成立

### 换质位：变形不能变意思

#### 15. 2026石景山一模 第5题（选择题）

【这道题考什么】 考换质法、换位法或换质位法。抓手是：题干把非物质文化遗产的传统表现形式、实践以及相关实物和场所分层列出，再说其中有些实物和场所适用文物保护法。

【题目材料】

```text
5. 非物质文化遗产是中华优秀传统文化的重要组成部分。
《中华人民共和国非物质文化遗产法》第二条规定，本法所称非物质文化遗产，是指各族人民世代相传并视为其文化遗产组成部分的各种传统文化表现形式和实践，以及相关的实物和场所。包括：
（一）传统口头文学以及作为其载体的语言；
（二）传统美术、书法、音乐、舞蹈、戏剧、曲艺和杂技；
……
属于非物质文化遗产组成部分的实物和场所，凡属文物的，适用《中华人民共和国文物保护法》的有关规定。
据此，下列选项正确的是（ ）
A.“传统口头文学”与“传统美术”，从概念外延看属于矛盾关系
B.“各种传统文化表现形式和实践，以及相关的实物和场所”是非物质文化遗产的定义项
C.“非物质文化遗产包括传统美术、书法、音乐和杂技”犯了“定义过窄”的错误
D.“有些属于非物质文化遗产组成部分的实物和场所，适用文物保护法”该判断无法进行换质位推理
```

【设问】 5.非物质文化遗产是中华优秀传统文化的重要组成部分。对非物质文化遗产法第二条关于非遗范围的规定及相关判断，下列推理正确的是（   ）
A.“传统美术、书法、音乐、舞蹈、戏剧、曲艺和杂技是非物质文化遗产”可换位为“非物质文化遗产是传统美术、书法、音乐、舞蹈、戏剧、曲艺和杂技”
B.“非物质文化遗产包括相关的实物和场所”可推出“所有相关的实物和场所都是非物质文化遗产”
C.“非物质文化遗产包括传统美术、书法、音乐和杂技”犯了“定义过窄”的错误
D.“有些非物质文化遗产的组成部分中的实物和场所适用《中华人民共和国文物保护法》”不能有效进行换质位推理

【怎么想到的】 题干最后一句给了一个“有些……适用文物保护法”的特称肯定判断。单独换位可以做，但题目问的是“换质位推理”：先换质会变成“有些……不是不适用文物保护法”，这已经是特称否定判断。

【满分作答示范】 D 项正确。题干给的是一个特称肯定判断：部分非遗组成部分中的实物、场所受文物保护法调整。若硬要先换质，只能得到“有些对象不是不受调整”这类特称否定式；特称否定判断不能再换位，因此不能有效完成换质位推理。

【采分点对照】
- 答案选D
- 原句“有些属于非遗组成部分的实物和场所，适用文物保护法”是特称肯定判断
- 若先换质，会变成“有些……不是不适用文物保护法”的特称否定判断
- 特称否定判断不能再换位，所以无法完成有效的换质位推理
- 错项分析：A 项诱人，因为传统口头文学与传统美术是并列项目
- 错在并列不等于矛盾关系，二者并不能穷尽非遗全部外延
- B 项诱人，因为它摘了定义句后半部分
- 错在定义项还包括“各族人民世代相传并视为其文化遗产组成部分”等限定，不能只截取一段
- C 项诱人，因为它只列举了若干非遗类型
- 错在这不是在下定义，也不能说成定义过窄

### 构建论证：让结论从共同前提长出来

#### 16. 2025丰台二模 第16题第（2）问（主观题）

【这道题考什么】 考三段论。抓手是：大项是“有利于培养时代新人”，小项是“大思政课”，中项是“能够帮助青年学子树立正确价值观的教育活动”。

【题目材料】

```text
16. （10分）“大思政课”大有可为。
古丝绸之路上,西安、敦煌和喀什串起一条横贯东西的文明珠链。
西安:丝路起点 ·文脉赓续
“春风得意马蹄疾,一日看尽长安花。”长安深植周礼秦制,畅行丝路驼铃。设专项资 金,令铜瓷点金、面
花塑彩等古艺重焕生机。易俗大剧院中,秦腔激昂传唱岁月故事;大 唐不夜城里,唐风盛景引人沉醉。传
统与新潮交织,绘就华夏文明的绚丽新卷。
敦煌:丝路瑰宝 ·文化交融
“羌笛何须怨杨柳,春风不度玉门关。”敦煌拥有大量壁画、石窟、藏经,是一座艺术 宝库。唐代的一纸文
献记录了来自印度的甘蔗制糖法;粟特商人用波斯银币购买过四川的 茶叶;莫高窟第285 窟的日神形象有
着古希腊-罗马艺术的元素……敦煌壁画的一笔一画、 文献的一字一句,成为人类文明打破隔阂的永恒丰
碑。
喀什:丝路门户 ·文启新业
“疏勒城边水一湾,龙蟠虎踞阵云闲。”喀什自汉代起,外邦商队与维吾尔手工艺人聚 居,形成多民族共生
的社区生态。中国(新疆)自由贸易试验区喀什片区设立,化身联通 中亚物流枢纽。喀什古城融合传统生
土建筑与新兴业态,古韵新声交织,点亮城市文旅之 光。
(1)某校以“寻迹丝路明珠,领略古今风华”为主题开展“大思政课”,请你从以上三个 地点中推荐一处,并运用
《哲学与文化》知识阐述推荐理由。（6分）
(2)“大思政课”有利于激发青年学子爱国情、强国志、报国行,为新时代青年学子打好 成长底色,培养担当
民族复兴大任的时代新人。以“‘大思政课’有利于培养时代新 人”为结论,构建一个三段论推理。（4分）
```

【设问】 “大思政课”有利于激发青年学子爱国情、强国志、报国行，为新时代青年学子打好成长底色，培养担当民族复兴大任的时代新人。以“‘大思政课’有利于培养时代新人”为结论，构建一个三段论推理。（4分）

【怎么想到的】 设问已经给出结论：“大思政课”有利于培养时代新人。先把结论拆开，小项是“大思政课”，大项是“有利于培养时代新人”。

【满分作答示范】 可构造为：凡能帮助青年学子形成正确价值观的教育活动，都有利于培养时代新人；大思政课正具有这种教育功能；所以，大思政课有利于培养时代新人。中项负责连接两端。

【采分点对照】
- 可以构造三段论：所有能够帮助青年学子树立正确价值观的教育活动都有利于培养时代新人
- 大思政课是能够帮助青年学子树立正确价值观的教育活动
- 大思政课有利于培养时代新人
- 中项“帮助青年学子树立正确价值观的教育活动”把大思政课和培养时代新人连接起来，结论从共同前提中推出

#### 17. 2026海淀二模 第20题第（1）问（主观题）

【这道题考什么】 考三段论。抓手是：大前提：符合和平与发展主题的举措是应对全球发展各种新挑战的正确选择。

【题目材料】

```text
20.（9分）
2026年是全球发展倡议提出五周年。五年来,在各方推动下,全球发展倡议已从中国主张扩大到国际共识,从合作理念拓展到丰富实践。
当前全球发展面临各种新的挑战,同球共济、团结合作才是正确选择。五年来,已经有80多个国家加入“全球发展倡议之友小组”,近百个国家、地区和国际组织同中方签署倡议合作文件,并且共建全球发展促进中心网络。中方发起的创新培训基地、全球发展青年领袖之家、全球妇女能力建设中心等平台陆续投入运作,不断提升发展中国家可持续造血能力。中方还与非洲国家和联合国机构共同建设合作示范中心,开辟了三方发展合作新局面。
2026年4月,全球共享发展行动论坛第三届高级别会议在北京开幕。本届会议的主题为“坚持行动导向 推动构建全球发展命运共同体”。本次会议发布《共创未来行动计划成果清单》,提出50项重要举措,积极行动,深化合作。
(1)“同球共济、团结合作是应对全球发展各种新挑战的正确选择”,以此为结论写出一个合乎逻辑的三段论推理。（2分）
(2)结合材料,运用《当代国际政治与经济》知识,围绕“全球发展倡议从合作理念到丰富实践”这一主题,撰写一篇短评。（7分）
要求:观点明确;知识运用准确、贴切;论述合乎逻辑,条理清晰。
```

【设问】 “同球共济、团结合作是应对全球发展各种新挑战的正确选择”，以此为结论写出一个合乎逻辑的三段论推理。（2分）

【怎么想到的】 题目给出的结论是“同球共济、团结合作是应对全球发展各种新挑战的正确选择”。要补的不是国际政治短评，而是能把“同球共济、团结合作”和“正确选择”连起来的中项。

【满分作答示范】 可以这样构造：凡符合和平与发展主题的做法，都是应对全球发展挑战的正确选择；同球共济、团结合作符合和平与发展主题；所以，同球共济、团结合作是正确选择。中项应放在两个前提中作桥梁，结论才从前提中推出。

【采分点对照】
- 可以构造三段论：符合和平与发展主题的举措是应对全球发展各种新挑战的正确选择
- 同球共济、团结合作是符合和平与发展主题的举措
- 同球共济、团结合作是应对全球发展各种新挑战的正确选择
- 中项“符合和平与发展主题的举措”在两个前提中起连接作用，使结论从共同前提中推出

#### 18. 2025西城期末 第17题第（2）问（主观题）

【这道题考什么】 考三段论。抓手是：小前提固定为“工业固废是放错了地方的资源”。

【题目材料】

```text
17.（10分）
资料包
.
当前,全国大宗固体废弃物综合利用率约为59%,废钢铁、废有色金属等10 种主要再生资源利用量每
年都在大幅增长,废钢铁每年利用量约2.6 亿吨。
.
据测算,2023 年我国约4300 万吨废塑料被焚烧或填埋,如果其中50%能够实现化学循环,就相当于
开发了一个超过6000 万吨的油田。
.
新能源产业快速发展,早期投入使用的电动汽车动力电池和太阳能光伏板、发电风机等清洁能源发电
装备将陆续退役,不断增加的废动力电池、废光伏组件及风机叶片等“新三样”固废问题日益突出。
以风机叶片为例,主要由环氧树脂和纤维复合材料构成,长度可达140 多米,处置回收难度大。
.
我国的环保企业普遍规模较小,业务多围绕“资源回收”或单纯的“收废品”展开,管理水平参差不
齐。
2024 年10 月18 日,我国资源循环利用产业首支“国家队”——中国资源循环集团有限公司(中国资环
集团)成立,集团股东成员包括中国石化、中国宝武、中国五矿、华润集团、中铝集团等多家中央企业。
按照党中央、国务院决策部署,中国资环集团专门从事资源循环利用,业务涵盖线下资源回收网络建设和
废钢回收、电子产品等耐用消费品回收和以旧换新、新能源汽车和电动自行车废旧电池业务、退役风电和
光伏组件等重大装备产品的回收业务等。
(1)有同学关注到上面的新闻,提出疑问:资源循环利用产业已有不少企业参与其中,为什么还要专门
组建一支“国家队”?参考资料包的内容,运用所学,为这位同学答疑解惑。（6分）
(2)请以“工业固废是放错了地方的资源”为小前提,编写一个合乎规则的三段论。（4分）
```

【设问】 请以“工业固废是放错了地方的资源”为小前提，编写一个合乎规则的三段论。（4分）

【怎么想到的】 设问指定小前提是“工业固废是放错了地方的资源”，中项就要稳定保持为“放错了地方的资源”，不能另外换成“所有资源”或“工业固废资源”来制造四概念。大前提负责连接中项和结论属性：凡是放错了地方的资源，都可以通过适当方式被重新利用。

【满分作答示范】 可构造为：放错位置的资源，经过适当方式能够再利用；工业固废就是这类资源；所以，工业固废可以通过适当方式重新利用。中项是“放错位置的资源”。

【采分点对照】
- 可构造三段论：放错了地方的资源可以通过适当方式被重新利用
- 工业固废是放错了地方的资源
- 工业固废可以通过适当方式被重新利用
- 中项“放错了地方的资源”把工业固废与可重新利用这一属性连接起来，使结论具有推出根据

### 综合辨析：换位、三段论、外延分开看

#### 19. 2026丰台二模 第8题（选择题）

【这道题考什么】 考三段论。抓手是：题干定义脑机接口使用方，并分为终端使用者和试验操作者。

【题目材料】

```text
8.脑机接口使用方是指直接与脑机接口系统进行交互或操作的个体。使用方分为终端使
用者和试验操作者。终端使用者是指以脑机接口系统为工具,实现控制交互、状态感
知或神经调控等目的的系统直接使用者,包括患者、康复者、受试者等。试验操作者
是指负责脑机接口系统的试验组织、配置管理、数据采集、数据分析等工作的人员,
包括研究人员、临床操作者等。据此,下列说法正确的是
1“脑机接口使用方是指直接与脑机接口系统进行交互的个体”,犯了“定义过宽”的
错误
2“有的终端使用者是受试者”,通过换位推理可得出“有的受试者是终端使用者”
3 “所有试验操作者都是进行数据分析的工作人员,某人是试验操作者。所以,某人
是进行数据分析的工作人员”,该三段论犯了“中项不周延”的错误
4 “终端使用者”“试验操作者”二者在外延上属于矛盾关系
A. 12
B. 13
C. 24
D. 34
```

【设问】 8.脑机接口使用方是指直接与脑机接口系统进行交互或操作的个体。使用方分为终端使用者和试验操作者。终端使用者是指以脑机接口系统为工具，实现控制交互、状态感知或神经调控等目的的系统直接使用者，包括患者、康复者、受试者等。试验操作者是指负责脑机接口系统的试验组织、配置管理、数据采集、数据分析等工作的人员，包括研究人员、临床操作者等。据此，下列说法正确的是
①“脑机接口使用方是指直接与脑机接口系统进行交互的个体”，犯了“定义过宽”的错误
②“有的终端使用者是受试者”，通过换位推理可得出“有的受试者是终端使用者”
③“所有试验操作者都是进行数据分析的工作人员，某人是试验操作者，所以某人是进行数据分析的工作人员”，该三段论犯了“中项不周延”的错误
④“终端使用者”“试验操作者”二者在外延上属于矛盾关系
A.①②
B.①③
C.②④
D.③④

【怎么想到的】 ②的形式是“有的终端使用者是受试者”，这是特称肯定判断，可以换位为“有的受试者是终端使用者”。③给出的三段论中，“试验操作者”在全称前提中作主项，已经周延，不能说它犯中项不周延。

【满分作答示范】 应选 C。②可由“部分终端使用者是受试者”换成“部分受试者是终端使用者”；④中终端使用者和试验操作者在同一使用方范围内互相排斥并穷尽分类，可看作矛盾关系。①③不能被题干稳定推出，不能一起选。

【采分点对照】
- 答案选C，即②④
- ②中“有的终端使用者是受试者”是特称肯定判断，可以换位为“有的受试者是终端使用者”
- ④中，题干把脑机接口使用方分为终端使用者和试验操作者，在“使用方”这一同一属概念范围内，二者互相排斥并穷尽题干分类，可判为矛盾关系
- 错项分析：A 项诱人，因为②确实是特称肯定判断换位
- 错在①省去了定义中的“或操作”，方向不是定义过宽
- B 项把①和③绑在一起，两个都不能成立，尤其③中的中项“试验操作者”在全称前提中已经周延，不犯中项不周延
- D 项诱人，因为④正确
- 错在③误把形式有效的三段论说成中项不周延

### 省略前提：把隐藏的大前提补回来

#### 20. 2026东城二模 第12题（选择题）

【这道题考什么】 考三段论。抓手是：题干比较“春日意象”相关判断与推理。

【题目材料】

```text
12.春日意象承载着丰富的自然意趣与人文内涵。蚕破茧、鸭知暖、柳含春,尽显生机;春耕劳作、秋千嬉戏,蕴含生活哲思。古人以笔墨绘春,于静景中藏动势,于时序中明事理,留下“春江水暖鸭先知”“人误地一时,地误人一年”等传世之语。下列判断与推理正确的是
A.“蚕”“鸭”“柳”“春耕”“秋千”与“春日意象”是种属关系
B.“于静景中藏动势,于时序中明事理”这一判断属于关系判断
C.“鸭子是水禽”,所以“春江水暖鸭先知”,该三段论省略了小前提
D.“人误地一时,地误人一年”的否定论断与其不能同真,也不能同假
```

【设问】 12．春日意象承载着丰富的自然意趣与人文内涵。蚕破茧、鸭知暖、柳含春，尽显生机；春耕劳作、秋千嬉戏，蕴含生活哲思。古人以笔墨绘春，于静景中藏动势，于时序中明事理，留下“春江水暖鸭先知”“人误地一时，地误人一年”等传世之语。下列判断与推理正确的是
A.“蚕”“鸭”“柳”“春耕”“秋千”与“春日意象”是种属关系
B.“于静景中藏动势，于时序中明事理”这一判断属于关系判断
C.“鸭子是水禽”，所以“春江水暖鸭先知”，该三段论省略了小前提
D.“人误地一时，地误人一年”的否定论断与其不能同真，也不能同假

【怎么想到的】 D 项直接考一个判断和它的否定论断：原判断与否定判断构成矛盾关系，不能同真，也不能同假。C 项容易误选，因为“鸭子是水禽”确实是三段论中的一个前提，但它不是被省略的前提。

【满分作答示范】 D 项正确。“人误地一时，地误人一年”的否定命题同原判断不能同真、也不能同假；“鸭子是水禽，所以鸭先知”隐藏的是“水禽先知”的大前提。

【采分点对照】
- 答案选D
- “人误地一时，地误人一年”的否定论断与原判断不能同真，也不能同假
- “鸭子是水禽，所以鸭先知”省略的是大前提而非小前提
- 错项分析：A 项错在把“蚕、鸭、柳、春耕、秋千”等具体意象与“春日意象”的关系说成种属关系
- B 项错在“于静景中藏动势，于时序中明事理”不是关系判断
- C 项错在省略的是大前提，不是小前提

## 四、归纳推理与探求因果联系

【本类怎么做】
- 先判断是完全归纳还是不完全归纳，不完全归纳只给或然结论。
- 看样本数量、范围和代表性，再判断结论可靠程度。
- 因果题先找变化项和不变项，再对应求同、求异、共变、剩余等方法。

【本类常见坑】
- 几个例子反复出现，不等于结论必然成立。
- 样本太少、范围太窄，不能推出过满结论。
- 把类比、归纳和求因果混在一起，会错判推理类型。

### 不完全归纳推理

#### 1. 2026朝阳一模 第17题第（1）问前半（主观题）

【这道题考什么】 考归纳推理。抓手是：AI 任务指令先从若干文创产品样本中提取共同特征，再把这些特征概括成设计任务的一般要求，材料动作是由部分样本上升到一般判断。

【题目材料】

```text
17. 博物馆作为城市的文化名片，承载着历史记忆与文明薪火。
《北京博物馆之城建设发展规划（2024-2035）》提出，支持朝阳区等地建设博物馆之城示范区。某校同学聚焦“朝阳区全力打造馆城相融的博物馆之城”话题，开展学习实践活动。
【学习理论】
馆城融合发展是指推动博物馆与城市空间、历史文化、公共服务、产业经济深度融合，将博物馆嵌入社区、公园、交通场站、商圈及历史街区，让博物馆成为城市功能、市民生活与城市风貌的有机组成部分，实现以文兴城、以城载馆、馆城共生。
【参与实践】
在馆城融合发展政策引领下，中国铁路博物馆开展“快闪博物馆”进校园活动，并向同学们征集博物馆文创产品设计方案，以增强文创产品的市场竞争力。某小组同学拟借助生成式人工智能大模型为文创设计提供思路。
AI 任务指令：
请依据爆款文创产品受好评的高频词汇：设计、手工、做工、礼物、材质、包装、博物馆等，概括爆款博物馆文创产品的三个特点。
AI 结论：
1. 有辨识度，设计精美。
2. 材质优良，做工精致。
3. 有纪念意义，承载文化价值。
（1）识别设计 AI 任务指令所运用的推理类型。运用联想思维的具体方法提出一份“中国铁路博物馆文创产品”的设计方案。
```

【设问】 识别设计 AI 任务指令所运用的推理类型。运用联想思维的具体方法提出一份“中国铁路博物馆文创产品”的设计方案。

【怎么想到的】 识别 AI 任务指令所用的推理类型时，要看 AI 是怎样从若干文创产品特点中概括出“有辨识度、设计精美、材质优良、有纪念意义、承载文化价值”等一般结论。这里不是从定义推出结论，也不是类比一个对象到另一个对象，而是由部分样本特征上升到一般判断，所以触发不完全归纳推理。

【满分作答示范】 AI 任务指令从有限文创样本概括一般设计特点，是不完全归纳；样本有限，结论只具或然性，需要更多样本和实践检验。

【采分点对照】
- AI 任务指令是从若干文创产品样本中概括出一般特点，再据此形成设计任务，属于由部分对象推出一般结论的不完全归纳推理
- 由于样本数量有限，该结论具有或然性，其可靠性还需要更多样本和实践检验来增强

#### 2. 2024.11朝阳期中 第18题（主观题）

【这道题考什么】 考归纳推理。抓手是：楚王根据“一个齐国人在楚国盗窃”这个个别事实，就推出“齐人固善盗”的整体评价，个例范围和全体结论之间明显不匹配。

【题目材料】

```text
18. （8分）
晏子将使楚。楚王闻之,谓左右曰:“晏婴,齐之习辞者也。今方来,吾欲辱之,何以
也?”左右对曰:“为其来也,臣请缚一人,过王而行,王曰:‘何为者也?’ 对曰:‘齐人也。’
王曰:‘何坐?’曰:‘坐盗。’”
晏子至,楚王赐晏子酒,酒酣,吏二缚一人诣王。王曰:“缚者曷为者也?”对曰:“齐人
也,坐盗。”王视晏子曰:“齐人固善盗乎?”晏子避席对曰:“婴闻之,橘生淮南则为橘,生于
淮北则为枳,叶徒相似,其实味不同。所以然者何? 水土异也。今民生长于齐不盗,入楚
则盗,得无楚之水土使民善盗耶?”王笑曰:“圣人非所与熙也,寡人反取病焉。”
阅读材料,运用《逻辑与思维》相关知识,分别评析楚王和晏子的推理。
```

【设问】 阅读材料，运用《逻辑与思维》相关知识，分别评析楚王和晏子的推理。

【怎么想到的】 楚王根据“一个齐国盗贼”，就推出“齐人固善盗”。推理从一个个体行为上升到整个国家的人群评价，样本数量极少、对象范围极宽，“一个”与“齐人”的范围落差很大，因此要想到不完全归纳中的轻率概括。

【满分作答示范】 楚王由一个齐国盗贼概括“齐人善盗”，样本过少，属于轻率概括。若要增强归纳可靠性，应扩大考察对象，并分析盗窃行为同地域、环境、个体因素的真实关系。

【采分点对照】
- 楚王只根据一个齐国盗贼就推出“齐人固善盗”，样本数量太少且不具代表性，属于轻率概括
- 要提高这种归纳推理的可靠性，应扩大考察对象，分析盗窃行为与地域、环境、个体因素之间是否存在真实因果联系

#### 3. 2026石景山一模 第7题（选择题）

【这道题考什么】 考归纳推理。抓手是：茶道从观茶芽卷舒、察茶汤黏稠、闻茶香持久等有限经验迹象出发，识别嫩度、发酵水平和烘焙工艺。

【题目材料】

```text
7.煮茶之风,古已有之。茶道推崇“见微知著”。观茶芽卷舒程度辨其嫩度,紧细多芽是嫩茶,粗松展
叶是老茶;察茶汤黏稠度识其发酵水平,清透不黏发酵轻,琥珀黏稠发酵重;闻茶香持久度知其烘焙工艺,
清香飘是轻火,沉香浓是重火。此“观、察、闻”的认知路径( )
A.通过必要条件假言判断建立“茶芽越卷曲则嫩度越高”的条件关系
B.运用求同法从“茶汤黏稠程度渐进变化”推理出其发酵水平
C.通过不完全归纳推理识别茶的香气持久与烘焙工艺之间的内在关联
D.运用辩证思维,立足细节,领悟茶道整体之妙,实现“见微知著”
```

【设问】 7．煮茶之风，古已有之。茶道推崇 “见微知著”。观茶芽卷舒程度辨其嫩度，紧细多芽是嫩茶，粗松展
叶是老茶；察茶汤黏稠度识其发酵水平，清透不黏发酵轻，琥珀黏稠发酵重；闻茶香持久度知其烘焙工艺，
清香飘是轻火，沉香浓是重火。此“观、察、闻”的认知路径（ ）
A.通过必要条件假言判断建立“茶芽越卷曲则嫩度越高”的条件关系
B.运用求同法从“茶汤黏稠程度渐进变化”推理出其发酵水平
C.通过不完全归纳推理识别茶的香气持久与烘焙工艺之间的内在关联
D.运用辩证思维，立足细节，领悟茶道整体之妙，实现“见微知著”

【怎么想到的】 “观、察、闻”都来自有限经验迹象：看茶芽卷舒、看茶汤黏稠、闻茶香持久，再据此判断嫩度、发酵水平和烘焙工艺。这不是从定义演绎，也不是在多个场合找唯一共同因素，而是由部分经验材料识别对象内部关联，触发不完全归纳推理。

【满分作答示范】 C 项正确。“观、察、闻”都是从有限经验线索判断茶的嫩度、发酵和烘焙状况，由若干迹象概括对象内在关联，属于不完全归纳，而不是条件演绎或求同法。

【采分点对照】
- 答案选C
- 题干的“观、察、闻”都是从有限经验迹象出发：卷舒、黏稠、香气持久分别指向嫩度、发酵和烘焙工艺
- 这不是条件演绎，也不是求同法，而是由部分经验材料概括对象内在关联，属于不完全归纳推理
- 错项分析：A 项错在把经验识别误写成必要条件假言判断
- B 项错在求同法要求比较多个场合的共同因素，题干不是这个结构
- D 项说法有迷惑性，但题目考的是由有限迹象推出内在关联的归纳推理，不是泛泛谈辩证思维

#### 4. 2026海淀二模 第7题（选择题）

【这道题考什么】 考归纳推理。抓手是：对多个城市桥下空间改造项目进行跟踪调查，由部分对象的共同情况推出一般结论：桥下空间改造是提升城市活力的有效途径。

【题目材料】

```text
7. 桥下空间改造项目正在全国多个城市展开。某团队对其中多个城市桥下空间改造项目进行跟踪调查，发现这些城市桥下空间改造后，周边社区活力显著提升，据此得出“桥下空间改造是提升城市活力的有效途径”这一结论。关于这一研究，下列说法正确的是
①前提中只涉及部分认识对象，运用了不完全归纳推理
②增加考察对象的数量，有利于提高结论的可靠程度
③由个别前提推出一般结论，所得结论具有必然性
④研究团队得出结论的过程体现了分析是综合的先导
A.①②
B.①③
C.②④
D.③④
```

【设问】 7．桥下空间改造项目正在全国多个城市展开。某团队对其中多个城市桥下空间改造项目进行跟踪调查，发现这些城市桥下空间改造后，周边社区活力显著提升，据此得出“桥下空间改造是提升城市活力的有效途径”这一结论。关于这一研究，下列说法正确的是
①前提中只涉及部分认识对象，运用了不完全归纳推理
②增加考察对象的数量，有利于提高结论的可靠程度
③由个别前提推出一般结论，所得结论具有必然性
④研究团队得出结论的过程体现了分析是综合的先导
A.①② B.①③ C.②④ D.③④

【怎么想到的】 抓住“多个城市”不等于“所有城市”。团队只是跟踪部分桥下空间改造项目，再推出“桥下空间改造是提升城市活力的有效途径”，这就是从部分对象推出一般结论的不完全归纳。

【满分作答示范】 应选 A。研究只考察部分城市的桥下空间改造，却推广到“桥下空间改造能提升城市活力”这一一般判断，属于不完全归纳；样本越充分，结论可靠性越高，但由于没有穷尽全部对象，结论仍不是必然的。

【采分点对照】
- 答案选A
- 研究只跟踪“多个城市”的部分桥下空间改造项目，却推出“桥下空间改造是提升城市活力的有效途径”这一一般结论，属于不完全归纳
- 因为没有穷尽全部对象，所以增加样本数量能提高可靠程度，但不可将结论说成必然
- 错项分析：B 项诱人，因为①成立
- 错在③把不完全归纳的或然结论说成必然结论
- C 项诱人，因为②成立
- 错在④把“形成一般结论”的过程误判为分析与综合关系，题干核心是归纳可靠性，不是先分析再综合
- D 项由③④组成，两个都错：一个把或然写成必然，一个错判为分析与综合

### 不完全归纳推理可靠程度

#### 5. 2025朝阳二模 第17题（主观题）

【这道题考什么】 考归纳推理。抓手是：研究小组只考察部分客运量位居前列线路，发现这些线路沿线景点多，就推出沿线景点数量是影响北京地铁客运量的决定性因素。

【题目材料】

```text
17.（5分）某校研究性学习小组探究影响北京地铁客运量的决定性因素。
该组同学比较了不同线路客运量数据,分析2024 年全年日均客运量位居前列的线路,发现这些线路的沿
线分布着很多著名景点,如10 号线沿线有元大都城垣遗址公园、潘家园古玩市场、玉渊潭公园、中央电视
塔等;4 号线大兴线沿线有颐和园、圆明园遗址公园、北京动物园、陶然亭公园等;1 号线八通线沿线有石景
山游乐园、故宫博物院、北京环球影城等;6 号线沿线有什刹海、北海公园、南锣鼓巷等景点;14 号线沿线
有北京园博园、朝阳公园等。
据此,该组同学得出结论:沿线景点数量是影响北京地铁客运量的决定性因素。
分析材料,运用《逻辑与思维》知识,识别该组同学所运用的推理类型,谈谈如何更好发挥该推理类型的
思维功能。
```

【设问】 分析材料，运用《逻辑与思维》知识，识别该组同学所运用的推理类型，谈谈如何更好发挥该推理类型的思维功能。

【怎么想到的】 材料只考察了日均客运量位居前列的部分线路，并发现这些线路沿线景点较多，就推出“沿线景点数量是影响客运量的决定性因素”。触发点在“由部分线路推出一般结论”和“决定性因素”这两个地方：前者说明这是不完全归纳，后者提醒结论不能写得过满。

【满分作答示范】 该组使用不完全归纳。要增强可靠性，应扩大线路、站点、时段和客流类型的样本，比较差异，并考察客运量同景点数量、人口密度、换乘条件之间是否有稳定因果联系。

【采分点对照】
- 该组同学运用不完全归纳推理
- 要更好发挥该推理功能，应扩大考察线路和区域范围，比较不同站点、不同时间段和不同客流结构下的数据，并探究客运量与景点数量、人口密度、换乘条件等因素之间是否存在稳定因果联系，从而提高前提与结论的相关程度，增强推理可靠性

#### 6. 2024海淀一模 第18题第（2）问（主观题）

【这道题考什么】 考归纳推理。抓手是：从部分外国朋友在中国使用移动支付时遇到“不能用”“不好用”等个别体验出发，概括出支付不便利会导致“不想用”的一般结论。

【题目材料】

```text
18.（10分）便利中外人员往来,服务高水平对外开放。
【免签时代】
为便利中外人员往来、服务高水平对外开放,我国决定试行扩大单方面免签国家范围。截至
2024 年1 月底,我国已与157 个国家缔结涵盖不同护照的互免签证协定,与44 个国家达成简化
签证手续协定或安排,同包括泰国、新加坡、马尔代夫、阿联酋在内的23 个国家实现全面互免签
证,同时放宽来华外籍人员申办口岸签证条件。对急需来华从事商贸合作、访问交流、投资创业、
探望亲属及处理私人事务等非外交、公务活动的外籍人员,来不及在境外办妥签证的,可凭邀请
函件等相关证明材料向口岸签证机关申办口岸签证入境。短期来华从事商贸合作、访问交流、投
资创业、探望亲属、观光旅游及处理私人事务等非外交、公务活动的外籍人员,有正当合理事由
需继续在华停留的可就近就便向停留地公安机关出入境管理机构申请签证延期换发补发。
(1)结合材料,运用《当代国际政治与经济》知识,预测上述举措对服务高水平对外开放的
积极影响。（6分）
【便利支付】
外国朋友来华进行旅游、拜访、商务等活动,遇到移动支付困难的问题。经过认真调查分
析,问题主要为:“不能用”,有的外国朋友绑不了境外的银行卡;“不好用”,有的外国朋友消费
超出一定金额,付不成账,觉得不好用。遇到问题多了,支付不便利了,自然就“不想用”了。
针对这些问题,中国人民银行指导支付机构推出一系列便利措施。
(2)指出材料中得出“不想用”这一结论的过程运用了什么推理方法,并说明如何提高这种
推理的可靠性。（4分）
```

【设问】 指出材料中得出“不想用”这一结论的过程运用了什么推理方法，并说明如何提高这种推理的可靠性。（4分）

【怎么想到的】 材料说的是一些外国朋友在移动支付中遇到“不能用”“不好用”，于是形成“不想用”的结论。先抓住“部分外国朋友的经历”这一材料信号：它能提示支付便利性问题，但还不足以保真地推出所有外国朋友都会“不想用”。

【满分作答示范】 由部分外国朋友的支付困难概括出“不便利会降低使用意愿”，属于不完全归纳。要提高可信度，应增加对象、范围和角度，并用求同、求异、共变等方法考察支付体验与使用意愿的因果联系。

【采分点对照】
- 由部分外国朋友在支付中遇到“不能用”“不好用”等问题，推出支付不便利会导致“不想用”，运用了不完全归纳推理
- 要提高可靠性，应考察更多认识对象，扩大研究范围、增加样本数量和归纳角度，并分析支付不便利与“不想用”之间的因果关系，可运用求同法、求异法、共变法等方法

#### 7. 2026海淀一模 第17题第（2）问（主观题）

【这道题考什么】 考归纳推理。抓手是：调研方案需要改进，原因之一是样本、角度或因果链不足。

【题目材料】

```text
17.（6分）
调查研究要讲求科学方法。某校“模拟政协”社团同学准备围绕本市无障碍环境建设情况展开调研。以下是同学们设计的调查问卷（节选）。
调查问卷（节选）
问题1. 您的身份（单选）：
□老年人（60岁及以上） □残障人士
□普通在职职工
□离退休人员
□相关行业从业者（如城市管理、物业等）
□其他
□儿童（14岁以下）
问题2. 您认为本市无障碍设施存在的主要问题是（可多选）：
□设计不合理
□标识不清
□相关部门维护不到位
运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）
为提高调研活动的科学性，提出具体可行的建议。（4分）
```

【设问】 结合调研活动，运用《逻辑与思维》知识提出两条具体可行的改进建议。

【怎么想到的】 调研结论如果只来自有限样本、单一角度或预设原因，就属于不完全归纳可靠性不足。提高结论可靠性，关键不只是增加调查数量，还要扩大认识对象、增加归纳角度，并在不同片区、不同群体、不同机制之间比较效果，寻找无障碍设施问题与真实原因之间的因果联系。

【满分作答示范】 调研改进应扩大样本和视角，覆盖更多区域、年龄、场景和反馈渠道；再比较现象差异，寻找问题表现与真实原因之间的因果联系，避免少量样本轻率概括。

【采分点对照】
- 改进调研时，应扩大样本范围和调查角度，覆盖不同区域、不同年龄群体、不同使用场景和不同反馈渠道，比较各种现象背后的差异，并寻找问题表现与真实原因之间的因果联系
- 这样才能避免由少量样本轻率概括，提高不完全归纳推理结论的可靠程度

#### 8. 2025石景山一模 第19题（主观题）

【这道题考什么】 考归纳推理。抓手是：获奖建议不是只凭个别灵感形成，而是通过文献查阅、问卷调研、访谈和实验数据等多种方法增强研究的广度和深度，并寻找因果联系。

【题目材料】

```text
19. （5分）
自2009 年开始,北京市教委在本市中小学生中设立“科学建议奖”,鼓励中小学生为首都经济社会发展献
计献策。迄今为止,共有6 万多名中小学生参与活动,318 项获得科学建议奖和科学建议提名奖。获奖建
议具有以下特点。
●关注社会发展和人民生活改善,具有强烈的问题意识和一定的操作性,有些建议已经转化为惠及民生的
具体措施。
●采用了文献查阅法、问卷调研法、访谈法等多元化方法,增强研究的覆盖面和深度,通过实验获取大量
数据,进而发现问题及其成因。
●从亲身经历中捕捉灵感和创意,将生活中的奇思妙想与城市发展建设相“碰撞”,擦出新颖独特的智慧火
花。
提出优秀的科学建议不仅要有公共参与意识,还要树立科学思维观念。结合材料,运用《逻辑与思维》所
学,简析获奖同学的建议是如何体现科学思维的。
```

【设问】 提出优秀的科学建议不仅要有公共参与意识，还要树立科学思维观念。结合材料，运用《逻辑与思维》所学，简析获奖同学的建议是如何体现科学思维的。

【怎么想到的】 该设问虽然从科学思维切入，但研究方法这一层非常清楚：文献、问卷、访谈、实验数据不是材料装饰，而是在扩大证据面，避免从少数经验轻率概括。学生看到多种材料来源共同支撑建议，就要追问归纳结论是否可靠。

【满分作答示范】 获奖同学通过文献、问卷、访谈、实验等方式扩大证据来源，避免只凭个别经验下结论；再结合定性与定量分析寻找现实需求、社会问题和建议方案之间的因果联系。

【采分点对照】
- 获奖同学通过文献查阅、问卷调研、访谈和实验数据等方法扩大研究范围，避免只凭个别经验概括公共问题
- 同时结合定性分析和定量分析寻找社会问题、现实需求与建议方案之间的因果联系，提高归纳推理结论的可靠程度，使科学建议更有事实依据和操作价值

### 科学归纳推理与不完全归纳推理

#### 9. 2024西城二模 第18题第（1）问（主观题）

【这道题考什么】 考归纳推理。抓手是：由352种不同品系高粱的AT1基因与耐盐碱表现，推出缺失AT1基因的高粱更耐碱的一般性结论。

【题目材料】

```text
18.（33分）推进乡村全面振兴，加快农业农村现代化建设。
【盐碱地有望变良田】
我国盐碱地面积达1亿公顷，占世界盐碱地总面积的近1/10。我国研究人员以耐盐碱作物高粱等为材料，发现主效耐碱基因AT1可显著提升高粱、水稻、小麦、玉米和谷子等作物在盐碱地的产量。
（1）阅读下表，按提示在空栏处填写。（8分）
研究过程（部分）：
研究人员收集了全球各地352种不同品系的高粱，分析它们对盐碱的耐受程度。
通过全基因组关联分析技术，研究人员定位克隆到一个与高粱耐碱性显著相关的基因位点，命名为AT1。
他们将AT1基因从高粱中提取出来再转到高粱中，高粱耐盐碱能力减弱；而将该基因“剪切”后，高粱的耐盐碱能力增强。这说明AT1基因在高粱盐碱胁迫的响应过程中起负调控作用，也就是说，缺失AT1基因的高粱更耐盐碱。
表格空栏要求：在研究过程中找出一个推理类型；解释推理过程，以及探求因果联系的方法。
```

【设问】 根据表格，在研究过程中找出一个推理类型，解释推理过程，以及探求因果联系的方法。

【怎么想到的】 表格里有两组材料信号：研究人员收集全球 352 种不同品系高粱，由这些样本与耐碱表现推出“缺失 AT1 基因的高粱更耐碱”，这是由部分样本到一般结论，触发不完全归纳推理；AT1 基因增加时耐碱能力减弱、剪切后耐碱能力增强，因素变化和结果变化相伴出现，触发共变法，同时能借助有无 AT1 变化理解求异法。

【满分作答示范】 研究人员先从 352 种高粱样本的表现概括出耐碱判断，属于不完全归纳推理；又比较 AT1 基因变化与耐碱能力变化之间的对应关系，借助共变和求异思路探求因果联系，从而提高结论可靠性。

【采分点对照】
- 研究人员运用不完全归纳推理，考察352种不同品系高粱，推出缺失AT1基因的高粱更耐碱
- 又比较AT1基因增加时耐碱能力减弱、剪切后耐碱能力增强等不同条件下的变化，运用共变法和求异法探求AT1基因与耐碱能力之间的因果联系，使结论更可靠

### 探求因果联系中的求异法

#### 10. 2024海淀二模 第5题（选择题）

【这道题考什么】 考探求因果联系的方法。抓手是：同样是棉质新毛巾、同样用超纯水多次洗涤，只改变干燥环境：有阳光的室外、阳光被遮挡的室外、室内。

【题目材料】

```text
5.清洗后在阳光下自然晒干的衣服上似乎有种格外好闻的气味。研究者为探究这一现象背后的
原因,找来棉质新毛巾,用超纯水多次洗涤,然后将湿毛巾分别放在有阳光的室外、阳光被
遮挡的室外以及室内环境中自然干燥。结果,在室外阳光下晒干的毛巾上发现一系列独特的
“香气分子”,这些气味分子大多是含有5-9 个碳原子的小分子醛与酮。这个实验中,研究者
探求因果联系运用的方法是
A.求异法
B.求同法
C.共变法
D.剩余法
```

【设问】 5．清洗后在阳光下自然晒干的衣服上似乎有种格外好闻的气味。研究者为探究这一现象背后的原因，找来棉质新毛巾，用超纯水多次洗涤，然后将湿毛巾分别放在有阳光的室外、阳光被遮挡的室外以及室内环境中自然干燥。结果，在室外阳光下晒干的毛巾上发现一系列独特的“香气分子”，这些气味分子大多是含有5-9个碳原子的小分子醛与酮。这个实验中，研究者探求因果联系运用的方法是
A.求异法
B.求同法
C.共变法
D.剩余法

【怎么想到的】 题干把三组实验条件控制得很清楚：毛巾材质相同，洗涤方式相同，差别只在干燥环境，尤其是有没有阳光照射；结果也跟着变化，只有室外阳光下晒干的毛巾出现独特香气分子。

【满分作答示范】 A 项正确。几组实验中材质、洗涤等条件基本一致，关键差别在是否接受阳光照射；结果也随之改变，只有室外晒干的毛巾出现香气分子，这符合求异法。

【采分点对照】
- 答案选A
- 三组实验中毛巾材质、洗涤方式等条件基本相同，关键差异是有没有阳光
- 结果也随之不同，只有室外阳光下晒干的毛巾出现香气分子
- 其他情况相同而某因素有无不同、结果有无不同，就是求异法
- 错项分析：B 项求同法要求从多个场合中找共同因素，题干不是这个结构
- C 项共变法看两个现象是否随量变同步变化，题干只是在比较有无阳光
- D 项剩余法要从复合原因中扣除已知部分，题干没有这种剩余推断

### 科学归纳、求异法与类比推理

#### 11. 2024东城二模 第17题第（2）问（主观题）

【这道题考什么】 考归纳推理。抓手是：科学团队先比较高粱 AT1 基因与耐碱能力的因果关系，再根据高粱 AT1 基因与水稻 GS3 基因的相似属性迁移推断水稻耐碱密码。

【题目材料】

```text
17.（12分）盐碱地上播种新希望。
近年来，在盐碱地治理中，某地探索出“盐碱荒滩”转化为“金山银山”的科学路径。
该地坚持人与自然和谐共生理念，利用理论、技术、产业创新，宜粮则粮、宜林则林、宜湿则湿，采用“林、水、土”盐碱化综合治理措施，改良盐碱地土壤结构，提高盐碱地土壤肥力，改善植物生长环境，构筑“大良田”，打造“生态绿洲”。
该地充分发挥盐碱地生态修复累积效益，以土地资源优化配置为核心，通过“科研院所+基地+公司”“龙头企业+基地+农户”等多种形式，流转农村土地3.2万亩，吸引企业参与规模化经营，打造盐碱地治理产业项目10余个，发展盐碱地特色农业、旅游业，真正实现政府、企业与农民的“共赢”。
（1）运用《经济与社会》知识，分析该地探索“盐碱荒滩”转化为“金山银山”的路径。（7分）
我国科学家以耐碱作物高粱为突破口，试图揭开其耐碱奥秘。他们收集全球各地352种不同品系的高粱，通过全基因组大数据关联分析耐碱差异大的高粱资源，发现了主效耐碱基因AT1。将该基因从高粱中提取出来再转到高粱中，高粱耐碱能力减弱；而将该基因进行“剪切”后，高粱的耐碱能力增强。
如果高粱有这个基因，那么其他作物是否也会有类似的基因？团队利用AT1基因的同源体，即影响稻米粒长的粒形调控基因GS3，进行水稻GS3基因的耐碱性研究，结果发现，缺失了GS3基因的水稻也更耐碱。作物耐碱“密码”被找到了。
（2）结合材料，从推理的角度，谈谈科学团队是如何找到作物耐碱“密码”的。（5分）
```

【设问】 结合材料，从推理的角度，谈谈科学团队是如何找到作物耐碱“密码”的。

【怎么想到的】 设问问“如何找到作物耐碱密码”，材料不是只要求说一个推理名称，而是要按科研路径写。团队通过高粱 AT1 基因有无、增减与耐碱能力变化，寻找基因和耐碱之间的因果联系，触发科学归纳推理中的求异法、共变法。

【满分作答示范】 研究团队先用科学归纳和求异思路，比较 AT1 变化同高粱耐碱能力的联系；再依据高粱 AT1 与水稻 GS3 的相似性进行类比，推测水稻相关基因也影响耐碱性。

【采分点对照】
- 科学团队运用科学归纳推理，利用求异法探求 AT1 与高粱耐碱能力的因果联系
- 又根据高粱 AT1 基因与水稻 GS3 基因的相似属性进行类比推理，找到水稻 GS3 基因与耐碱属性的关系

## 五、类比推理

【本类怎么做】
- 先找两个对象在哪些方面相同或相似，再看能不能迁移到新的属性。
- 类比只能增强可能性，不能直接给必然结论。
- 答价值题时，要写清“从哪个领域类比到哪个领域”。

【本类常见坑】
- 只说“很像”不够，必须写出相似点和迁移点。
- 相似点不相关，类比可靠性就低。
- 类比推理不能被写成换位、归纳或联想口号。

### 类比推理

#### 1. 2024.11朝阳期中 第18题（主观题）

【这道题考什么】 考类比推理。抓手是：晏子把“橘因水土不同而性状变化”与“人因社会环境不同而行为表现变化”放在一起比较，由橘的变化类推人的变化。

【题目材料】

```text
18. （8分）
晏子将使楚。楚王闻之,谓左右曰:“晏婴,齐之习辞者也。今方来,吾欲辱之,何以
也?”左右对曰:“为其来也,臣请缚一人,过王而行,王曰:‘何为者也?’ 对曰:‘齐人也。’
王曰:‘何坐?’曰:‘坐盗。’”
晏子至,楚王赐晏子酒,酒酣,吏二缚一人诣王。王曰:“缚者曷为者也?”对曰:“齐人
也,坐盗。”王视晏子曰:“齐人固善盗乎?”晏子避席对曰:“婴闻之,橘生淮南则为橘,生于
淮北则为枳,叶徒相似,其实味不同。所以然者何? 水土异也。今民生长于齐不盗,入楚
则盗,得无楚之水土使民善盗耶?”王笑曰:“圣人非所与熙也,寡人反取病焉。”
阅读材料,运用《逻辑与思维》相关知识,分别评析楚王和晏子的推理。
```

【设问】 阅读材料，运用《逻辑与思维》相关知识，分别评析楚王和晏子的推理。

【怎么想到的】 晏子不是从一个个例推广所有人，而是拿“橘在不同水土中性质变化”去比照“人在不同社会环境中行为变化”。已知相似点是两者都受环境影响。

【满分作答示范】 晏子把“橘生淮南为橘、生于淮北为枳”这一受水土影响的现象，迁移到人在不同社会环境中行为表现会变化，抓住二者都受外部环境影响这一相似点进行类推。这属于类比推理，结论具有或然性，但能反驳楚王把个别人盗窃概括成“齐人善盗”的轻率说法。

【采分点对照】
- 晏子把橘受水土影响与人受社会环境影响作类比，由“对象会受环境影响”这一相似属性，推出楚地环境也可能影响人的行为表现
- 该推理属于类比推理，结论具有或然性，但它抓住楚王论证中的环境变量，能反驳楚王由个别盗贼污名化齐人的错误推断

#### 2. 2026顺义一模 第4题（选择题）

【这道题考什么】 考类比推理。抓手是：题干把《论持久战》中分析持久战、阶段性推进和战略主动的思想经验，拿来启迪当前科技创新、乡村振兴等中长期问题。

【题目材料】

```text
4.在民族危难时期，《论持久战》横空出世，总结全国抗战经验，系统阐明党的抗日持久战战略总方针，有力批驳当时流行的“亡国论”和“速胜论”等种种错误观点，立起了一座指导全民族抗战走向胜利的思想灯塔。重温《论持久战》，对解决当前我国科技创新、乡村振兴等中长期问题提供思想启迪。《论持久战》
A.对解决当前我国很多中长期问题提供思想启迪，这运用了类比推理
B.有力批驳错误观点，对全民族抗日战争走向胜利起到了决定性作用
C.是指导全民族抗战走向胜利的思想灯塔，这运用了比喻的定义方法
D.运用了完全归纳推理把握抗日战争的规律，因而其结论具有可靠性
```

【设问】 4.在民族危难时期，《论持久战》横空出世，总结全国抗战经验，系统阐明党的抗日持久战战略总方针，有力批驳当时流行的“亡国论”和“速胜论”等种种错误观点，立起了一座指导全民族抗战走向胜利的思想灯塔。重温《论持久战》，对解决当前我国科技创新、乡村振兴等中长期问题提供思想启迪。《论持久战》
A.对解决当前我国很多中长期问题提供思想启迪，这运用了类比推理
B.有力批驳错误观点，对全民族抗日战争走向胜利起到了决定性作用
C.是指导全民族抗战走向胜利的思想灯塔，这运用了比喻的定义方法
D.运用了完全归纳推理把握抗日战争的规律，因而其结论具有可靠性

【怎么想到的】 题干说《论持久战》解决的是抗战中的长期复杂问题，又说它对当前科技创新、乡村振兴等中长期问题提供启迪。两个时代、两个领域并不相同，但都面对长期性、复杂性、战略耐心和路径选择问题。

【满分作答示范】 A 项正确。《论持久战》处理长期复杂斗争，科技创新、乡村振兴也具有长期性和复杂性；二者在战略耐心和系统推进上相似，可由历史经验类比启发现实工作。

【采分点对照】
- 答案选A
- 《论持久战》面对的是抗战中的长期复杂问题，当前科技创新、乡村振兴等也是中长期问题
- 二者领域不同，但在长期性、复杂性、战略耐心上有相似结构
- 由历史经验迁移启发现实问题，是类比推理，不是完全归纳或定义
- 错项分析：B 项把“思想灯塔”的指导作用夸大成决定性作用
- C 项把比喻表达误说成定义方法，定义要揭示概念内涵，不能只靠比喻
- D 项把总结抗战经验误说成完全归纳，材料没有穷尽所有对象，也不能推出必然结论

#### 3. 2024朝阳二模 第19题第（1）问（主观题）

【这道题考什么】 考类比推理。抓手是：人效法天地之德：材料把天地生育万物不息、广阔博大的德性作为源对象，再迁移到人的修身实践，类推出人应自强不息、厚德载物。

【题目材料】

```text
19. （16分）
中华文明拥有五千多年不间断的历史,积淀形成辉煌灿烂的中华优秀传统文化,中
华优秀传统文化的特质赋予中国式现代化深厚底蕴,给予其精神和思想力量。
生生之宇宙观
宇宙处于生生不息的变化之中。“天地之大德曰生”“富有之谓大业,日新之谓盛德,
生生之谓易”。宇宙永久的变易包含永远的革新,是生命的不断充实、成长、更新和展开。
一体之天人观
人类与天地为一体。天地的交合生成了世界,赋予了人的身体和本性,所有人都是
天地生育的子女;不仅如此,万物和人类一样,也是天地所生。因此,他人都是自己的同
胞,万物都是自己的朋友。
法天地之人生观
人应该效法天地之德。“夫大人者,与天地合其德,与日月合其明,与四时合其序。”天
之德在生育万物而不息,地之德在广阔博大,君子应学习天地之德,自强不息、厚德载物。
(1)生生之宇宙观体现了辩证思维的 1 特征。人效法天地之德体现的推理
类型是 2 推理。（4分）
(2)“夫大人者,与天地合其德,与日月合其明,与四时合其序。”是哪种复合判断? 该
复合判断为真的条件是什么? （5分）
(3)“中华优秀传统文化的特质赋予中国式现代化以深厚底蕴”。结合材料,综合运
用所学,谈谈你对这句话的理解。（7分）
```

【设问】 生生之宇宙观体现了辩证思维的①特征。人效法天地之德体现的推理类型是②推理。（4分）

【怎么想到的】 题干说“人应该效法天地之德”，不是从一般规则推出个案，也不是列举许多个案归纳结论，而是把天地“生育万物而不息、广阔博大”的德性迁移到人的修身实践中，推出人应自强不息、厚德载物。材料的关键词是“效法”：看到一个对象借另一个对象的相似特征来启发自身行动，就应想到类比推理。

【满分作答示范】 “人效法天地之德”是把天地生生不息、包容运行等特点迁移到人的修身实践中，依据的是天地与人的价值相通性。这属于类比推理，能启发行动，但结论仍需实践检验。

【采分点对照】
- “人效法天地之德”是把天地运行所体现的生生不息、广阔包容等德性类推到人的修身实践中
- 该推理依据天地与人的价值相通性进行由此及彼的迁移，属于类比推理
- 它能提供启发，但不是演绎必然结论，仍需要在人的实践中进一步印证

#### 4. 2026东城二模 第18题（主观题）

【这道题考什么】 考类比推理。抓手是：把人体健康体检中的“检测指标、预判风险、主动干预”迁移到治理领域，形成治理体检的思路。

【题目材料】

```text
18.（6分）体检是通过检测人体生理指标、预判健康风险的常规方式,核心是“提前预判、主动干预”,以实现高效健康管理。如今,这种体检思维不断延伸。
明者图之于未萌,智者虑之于未有。体检思维在多个领域的运用,体现了一种治理智慧。
体检思维从人体健康领域延伸到治理领域,运用了哪种推理类型?结合材料,运用《逻辑与思维》知识,谈谈在治理领域运用这种推理的价值。
```

【设问】 体检思维从人体健康领域延伸到治理领域，运用了哪种推理类型？结合材料，运用《逻辑与思维》知识，谈谈在治理领域运用这种推理的价值。

【怎么想到的】 材料先讲人体体检：检测指标、预判风险、主动干预；再讲这种“体检思维”延伸到治理领域。

【满分作答示范】 这是类比推理。人体体检与基层治理都强调提前发现风险、诊断原因、持续跟踪；二者结构相似，所以治理中可以借用体检的预先排查、原因判断和持续处置思路。

【采分点对照】
- 体检思维从人体健康领域延伸到治理领域，运用了类比推理
- 人体体检和基层治理都强调提前发现隐患、及时诊断问题、持续干预跟踪，二者在“发现问题—判断原因—采取措施—跟踪效果”的结构上相似，因此可把体检中的预判、诊断、干预方法迁移到治理中，用来创新治理思路、提高治理效能

## 六、概念、定义、外延关系与划分

【本类怎么做】
- 概念题先看内涵是否明确、外延是否清楚。
- 定义题按“种差 + 属概念”检查，划分题按同一标准和穷尽互斥检查。
- 外延关系题要分清全同、属种、交叉和全异。

【本类常见坑】
- 划分标准前后不一，会造成子项混乱。
- 定义过宽、过窄或循环定义，都会影响判断。
- 偷换概念会破坏同一律，不能只看字面相近。

### 概念划分规则

#### 1. 2026海淀一模 第17题第（1）问（主观题）

【这道题考什么】 考概念、定义或划分规则。抓手是：调查问卷的问题1要求“您的身份（单选）”，却把老年人、残障人士、儿童、普通在职职工、离退休人员、相关行业从业者和其他并列为同一组选项。

【题目材料】

```text
17.（6分）
调查研究要讲求科学方法。某校“模拟政协”社团同学准备围绕本市无障碍环境建设情况展开调研。以下是同学们设计的调查问卷（节选）。
调查问卷（节选）
问题1. 您的身份（单选）：
□老年人（60岁及以上） □残障人士
□普通在职职工
□离退休人员
□相关行业从业者（如城市管理、物业等）
□其他
□儿童（14岁以下）
问题2. 您认为本市无障碍设施存在的主要问题是（可多选）：
□设计不合理
□标识不清
□相关部门维护不到位
运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）
为提高调研活动的科学性，提出具体可行的建议。（4分）
```

【设问】 运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）

【怎么想到的】 题目让指出问卷中的逻辑错误，先看选项是不是按同一个标准划分。问题1名义上问“身份”，但同一层级里同时出现年龄、身体状况、就业状态和行业角色：老年人、残障人士、上班族、物业人员并不是同一划分标准下的并列种类。

【满分作答示范】 问题1犯了划分标准混杂的错误。它把年龄层次、健康状况、职业状态和行业身份放进同一组，老年人、残障人士、在职职工、行业从业者可能互相交叉，不能作为单选身份项。

【采分点对照】
- 问题1存在划分标准不一的逻辑错误：同一组选项同时按年龄、身体状况、就业状态和行业角色分类，导致“老年人、残障人士、在职职工、相关行业从业者”等选项可能交叉，不能作为同一标准下的单选身份项

### 同一律与偷换概念

#### 2. 2026西城一模 第19题第（3）问（主观题）

【这道题考什么】 考概念、定义或划分规则。抓手是：丙的前提讨论的是“村民会议讨论通过”这一主体和程序，结论却转成“村委会有决定权”。

【题目材料】

```text
19.（12分）推进美丽乡村建设、完善乡村公共服务。
材料一 某村规划建设集休闲健身、生态绿化、文化展示于一体的文化生态公园,却在推进中却遭遇一连串难题:
乡镇政府:必须严守项目预算、建设标准、生态红线
村“两委”、村干部:担心规划与民意脱节、项目推进受阻
邻村及本村土地被占用村民:担心个人利益受损,有一定抵触情绪
外出务工村民:无法回村参与,担心自己的诉求被忽略
材料二 面对多方意见,村党支部创新推行“云端+院落夜话”议事机制(右图):一方面,线上议事群实时发布议题、收集意见,组织视频连线让外出村民全程参与讨论;另一方面,在院落、广场组织大家面对面商量,直接回应涉地村民的实际诉求。同时,联动政府、村干部与村民代表,在村规划、生态保护和群众利益之间找到平衡点,最终形成方案,推动实施。
(1)遵循民主程序要求,将右图最后一环节补充完整。（1分）
(2)结合材料,运用《政治与法治》知识,谈谈“云端+院落夜话”议事机制是如何破解“一连串难题”的。（7分）
(3)任选两位村民的观点,运用形式逻辑知识,说明其理解是否正确。（4分）
甲:议事协商应维护公共利益,个人补偿诉求不是公共利益,所以个人补偿诉求不应纳入议事协商。
乙:对于村务公开,我既不同意“所有村务必须公开”,也不同意“所有村务都不必公开”。
丙:只要涉及村民切身利益,就应由村民会议讨论决定。村委会没有讨论这件事,说明这件事不涉及村民切身利益。
```

【设问】 任选两位村民的观点，运用形式逻辑知识，说明其理解是否正确。（4分）

【怎么想到的】 丙前面讨论的是“村民会议”，结论却转成“村委会”。这两个主体不是同一个概念：村民会议是村民参与讨论决定的会议形式，村委会是基层群众性自治组织。

【满分作答示范】 丙观点错误。前提说村民会议是否讨论通过，结论却谈村委会有没有决定权；主体和权力来源变了，核心概念未保持同一，违背同一律。

【采分点对照】
- 丙观点错误
- 推理前提讨论的是“村民会议是否讨论通过”，结论却换成“村委会是否有决定权”，两个主体和权力来源并不相同
- 同一推理中核心概念由“村民会议的讨论通过”转换为“村委会的决定权”，概念没有保持同一，违反同一律，属于偷换概念

### 概念外延关系错项辨析

#### 3. 2026顺义一模 第2题（选择题）

【这道题考什么】 考概念、定义或划分规则。抓手是：A项把剧目个性、北京题材共性和概念外延包含混在一起。

【题目材料】

```text
2.2025年底，多台专注挖掘北京题材的新戏大戏接连上演，杂技剧场«屋顶上的北平»用现
代舞台语言演绎古都风云，话剧«金中都»，深入挖掘了一段鲜为人知的建都历史，曲剧
«城南旧事»，清淡隽永的展开上世纪20年代末北京城南的风土人情。这说明
A.«城南旧事»等剧目的个性特征包含于“北京题材”这一共性之中
B.话剧«金中都»通过创新文化呈现方式重构和延伸了北京的建都历史
C.杂技剧场«屋顶上的北平»在内容与形式的统一中体现意识的能动性
D.“上世纪20年代末北京城南风土人情”与“北京题材”在外延上是交叉关系
```

【设问】 2.2025年底，多台专注挖掘北京题材的新戏大戏接连上演，杂技剧场《屋顶上的北平》用现代舞台语言演绎古都风云，话剧《金中都》深入挖掘了一段鲜为人知的建都历史，曲剧《城南旧事》清淡隽永地展开上世纪20年代末北京城南的风土人情。这说明
A.《城南旧事》等剧目的个性特征包含于“北京题材”这一共性之中
B.话剧《金中都》通过创新文化呈现方式重构和延伸了北京的建都历史
C.杂技剧场《屋顶上的北平》在内容与形式的统一中体现意识的能动性
D.“上世纪20年代末北京城南风土人情”与“北京题材”在外延上是交叉关系

【怎么想到的】 “北京题材”四个字容易带偏判断。A 项把剧目的个性特征和“北京题材”的共性直接说成外延包含，混淆了共性个性关系和概念外延关系。

【满分作答示范】 C 项正确。A 混淆个性、北京题材共性和外延包含；B 把“深入挖掘”误推成“重构和延伸”；D 把具体风土人情误判为同北京题材交叉。

【采分点对照】
- 答案选C
- 整题答案为C
- A错在把个性特征、北京题材共性和外延包含混在一起，B错在把“深入挖掘”过度推出“重构和延伸”，D错在把具体风土人情误判为与北京题材交叉
- 错项分析：A 项错在混淆个性、共性和外延包含
- B 项错在把“深入挖掘”偷换成“重构和延伸”
- D 项错在下位具体内容通常属于北京题材范围内的内容，不能判为与北京题材交叉

### 定义构成与属加种差定义

#### 4. 2024西城一模 第19题第（2）问（主观题）

【这道题考什么】 考概念、定义或划分规则。抓手是：定义句把“举国体制”作为被说明对象，用“是”连接后面的定义项。

【题目材料】

```text
19.（31分）
我国新型举国体制不断完善，为国民经济和社会发展主要领域提供支撑、保障和引领。
新型举国体制的适用范围：
方向包括面向世界科技前沿、面向经济主战场、面向国家重大需求、面向人民生命健康。
领域包括战略性技术、前瞻性技术、“卡脖子”技术和防御性技术等。
举国体制是利用国家力量动员规模性资源、实现国家目标的一种任务组织方式和体制机制安排。
“两弹一星”、高速铁路、载人航天、大飞机、新冠疫苗攻关等都是运用举国体制实现国家目标的具体表现。
（2）有研究者给“举国体制”下了一个定义。阅读文本信息，按定义结构图中的序号写出其构成。（2分）
定义结构图提示：①被定义项，②定义联项，③种差，④属概念。
```

【设问】 有研究者给“举国体制”下了一个定义。阅读文本信息，按下图中的序号写出其构成。（2分）

【怎么想到的】 题目已经给出定义结构图，真正要做的是把定义句拆回对应位置。读到“举国体制是……一种任务组织方式和体制机制安排”，先抓“举国体制”这个被说明对象，再抓连接词“是”。

【满分作答示范】 可补：①举国体制；②是；③由国家力量统筹大规模资源并服务国家目标；④一种任务组织方式和体制机制安排。其中“是”是定义联项，④是属概念，③说明种差。

【采分点对照】
- 可补为：①举国体制，②是，③利用国家力量动员规模性资源、实现国家目标，④一种任务组织方式和体制机制安排
- 这个定义用“是”作定义联项，用“任务组织方式和体制机制安排”作属概念，再用国家力量、规模性资源和国家目标说明种差

### 概念外延中的相容关系与属种关系

#### 5. 2024西城一模 第19题第（3）问（主观题）

【这道题考什么】 考概念、定义或划分规则。抓手是：新型举国体制仍然属于举国体制的大范围，只是在社会主义市场经济条件、关键核心技术攻关等方面增加了新的条件和特征。

【题目材料】

```text
19.（31分）
未来产业由前沿技术驱动,是具有显著战略性、引领性、颠覆性和不确定性的前瞻性新兴产业,当前处于孕育萌发阶段或产业化初期。
2022年度全球未来产业发展指数排名前6位国家六大产业情况
(1)读上图,分析我国未来产业发展的状况。（3分）
我国新型举国体制不断完善,为国民经济和社会发展主要领域提供支撑、保障和引领。
(2)有研究者给“举国体制”下了一个定义。阅读文本信息,按下图中的序号写出其构成。（2分）
(3)“举国体制”与“新型举国体制”的外延是 关系。（1分）
党的十九届四中、五中全会均提出构建社会主义市场经济条件下关键核心技术攻关新型举国体制。党的二十大报告强调健全新型举国体制,提出加快实施创新驱动发展战略,强化企业科技创新主体地位,发挥科技型骨干企业引领支撑作用,营造有利于科技型中小微企业成长的良好环境,推动创新链产业链资金链人才链深度融合。
从中央到地方都在加大对未来产业的布局。从2024年各地政府工作报告看,过半数省份在部署工作时提出前瞻布局未来产业。
(4)根据前四问的材料,综合运用所学,说明我国新型举国体制的主要特点。（9分）
前瞻布局未来产业是构建我国现代化产业体系的重要一环,其前提是要判断哪些产业属于未来产业。未来产业在技术路线、应用场景、大规模产业化的时间等方面具有高度的不确定性,这就造成准确选择未来产业的难度较大。
(5)运用《逻辑与思维》的知识,说明应怎样研判我国未来产业发展的方向。（6分）
面对新一轮前沿科技发展浪潮,全球各主要经济体都在加强国家顶层科技战略布局和科技战略力量部署。
(6)结合材料,从经济角度分析我国未来产业发展的机遇和挑战,以及攻克“卡脖子”难题对经济开放发展的助推作用。（10分）
新型举国体制的适用范围 | 新型举国体制的适用范围 | 新型举国体制的适用范围 | 新型举国体制的适用范围 | 新型举国体制的适用范围
方向 | 面向世界科技前沿 | 面向经济主战场 | 面向国家重大需求 | 面向人民生命健康
领域 | 战略性技术:关系国家安全和民生安全的重大战略性领域 | 战略性技术:关系国家安全和民生安全的重大战略性领域 | 战略性技术:关系国家安全和民生安全的重大战略性领域 | 战略性技术:关系国家安全和民生安全的重大战略性领域
领域 | 前瞻性技术:关系国家核心竞争力的未来科技前沿领域 | 前瞻性技术:关系国家核心竞争力的未来科技前沿领域 | 前瞻性技术:关系国家核心竞争力的未来科技前沿领域 | 前瞻性技术:关系国家核心竞争力的未来科技前沿领域
领域 | “卡脖子”技术:关系国家主导或先导产业共性关键技术短板领域 | “卡脖子”技术:关系国家主导或先导产业共性关键技术短板领域 | “卡脖子”技术:关系国家主导或先导产业共性关键技术短板领域 | “卡脖子”技术:关系国家主导或先导产业共性关键技术短板领域
领域 | 防御性技术:关系国家产业链供应链安全的非普适性小众领域 | 防御性技术:关系国家产业链供应链安全的非普适性小众领域 | 防御性技术:关系国家产业链供应链安全的非普适性小众领域 | 防御性技术:关系国家产业链供应链安全的非普适性小众领域
```

【设问】 “举国体制”与“新型举国体制”的外延是____关系。（1分）

【怎么想到的】 这类题不能凭“新型”二字直接写全同或全异，要问“新型举国体制还是不是举国体制的一种”。材料说它是在社会主义市场经济条件下、面向关键核心技术攻关的新形态，说明它没有跳出“举国体制”的大范围，只是在原概念下增加了新的条件和特征。

【满分作答示范】 新型举国体制仍在举国体制范围内，只是在新时代条件下形成的新形态。二者不是并列、全异或矛盾关系，而是大概念包含小概念，属于相容关系中的真包含。

【采分点对照】
- “新型举国体制”的外延包含在“举国体制”的外延之中，是种概念与属概念之间的真包含关系
- 新型举国体制不是同举国体制并列的另一个概念，也不是与其互不相容，而是举国体制在新时代条件下的一种新形态，因此二者属于属种关系，也属于相容关系中的真包含关系

### 概念外延关系图示辨析

#### 6. 2024石景山一模 第7题（选择题）

【这道题考什么】 考概念、定义或划分规则。抓手是：题干要求把概念外延关系与图示对应起来：①财产权与物权之间存在上位概念和下位概念关系，可按图甲描述。

【题目材料】

```text
7. 概念的外延是指具有概念所反映的本质属性的事物的范围，人们经常用图来表示概念外延之间的关系。图示说明：图甲表示 P 真包含于 S；图乙表示 S 与 P 交叉；图丙表示 Q 被 S 与 P 二分；图丁表示 S、P 都真包含于 Q，且 S 与 P 不交叉、不穷尽 Q。对此，下列说法正确的是
①图甲，可以用来描述财产权和物权的关系
②图乙，可以用来描述国体和政体的关系
③图丙，如果 Q 是社会主要矛盾，S 是生产力，P 是生产关系
④图丁，如果 Q 是领土，S 可以是领陆，P 可以是领空
A.①③
B.①④
C.②③
D.②④
```

【设问】 7.概念的外延是指具有概念所反映的本质属性的事物的范围，人们经常用图来表示概念外延之间的关系。图示说明：图甲表示 P 真包含于 S；图乙表示 S 与 P 交叉；图丙表示 Q 被 S 与 P 二分；图丁表示 S、P 都真包含于 Q，且 S 与 P 不交叉、不穷尽 Q。对此，下列说法正确的是
①图甲，可以用来描述财产权和物权的关系
②图乙，可以用来描述国体和政体的关系
③图丙，如果 Q 是社会主要矛盾，S 是生产力，P 是生产关系
④图丁，如果 Q 是领土，S 可以是领陆，P 可以是领空
A.①③
B.①④
C.②③
D.②④

【怎么想到的】 先将文字关系翻译成图示关系。①中物权属于财产权的一种，财产权范围大，物权范围小，符合图甲的包含关系。

【满分作答示范】 B 项正确。①财产权范围大、物权范围小，对应包含图；④领陆和领空互不交叉，也不能穷尽领土，因为还包括领水等，对应丁图。

【采分点对照】
- 答案选B
- ①中财产权是大范围，物权属于财产权的一种，符合图甲“P 真包含于 S”的包含关系
- ④中领陆、领空都属于领土组成部分，二者不交叉，又不能穷尽领土，因为还有领水等范围，符合图丁
- 错项分析：A 项含①③，①正确但③把社会主要矛盾误拆为生产力和生产关系
- C 项含②③，二者都不符合图示
- D 项含②④，④正确但②把相关关系误作交叉外延关系

### 定义方法与种差加属概念

#### 7. 2026朝阳二模 第19题第（1）问（主观题）

【这道题考什么】 原题材料缺失，暂不判定题型。

【题目材料】

```text
本题原始材料缺失，待补。
```

【设问】 原题设问缺失或与材料错位，待补。

【怎么想到的】 原题材料缺失，不能判断材料中的逻辑抓手；待补入原始题面后再分析。

【满分作答示范】 原题材料缺失，暂不提供示范答案；补入原卷题面后再完善。

【采分点对照】
- 原始题面缺失，暂不列采分点；补入原卷材料后再补充。

### 同一律与概念确定性

#### 8. 2026石景山二模 第7题（选择题）

【这道题考什么】 考概念、定义或划分规则。抓手是：食品标签中的“0”“100%”等符号被突出为商标或宣传点，容易让消费者把商标、比例、纯度、零添加等不同概念混同。

【题目材料】

```text
7.“某某0”酱油因商标中“0”被放大宣传,易误导消费者认为是零添加产品;“某某100%”将百分比作为商标突出使用,易让公众误认产品纯度……针对此类现象,国家卫健委、国家市场监管总局公布 59 项食品安全国家标准及修改单,明确新版预包装食品标签通则实施后,禁止使用“零添加”等易误导用语。食品安全国家标准及修改
A.防止“偷换概念”,是思维的一致性要求
B.符合同一律,避免误导消费者
C.符合矛盾律,是思维的明确性要求
D.防止在“是”与“非”之间骑墙居中
```

【设问】 7.“某某0”酱油因商标中“0”被放大宣传，易误导消费者认为是零添加产品；“某某100%”将百分比作为商标突出使用，易让公众误认产品纯度。针对此类现象，国家卫健委、国家市场监管总局公布59项食品安全国家标准及修改单，明确新版预包装食品标签通则实施后，禁止使用“零添加”等易误导用语。食品安全国家标准及修改单的出台
A.防止“偷换概念”，是思维的一致性要求
B.符合同一律，避免误导消费者
C.符合矛盾律，是思维的明确性要求
D.防止在“是”与“非”之间骑墙居中

【怎么想到的】 “0”“100%”本来可以是商标或比例符号，但被放大宣传后容易让消费者误以为是“零添加”或“纯度百分百”，问题就在于同一思维过程中概念意义被混同、变得不确定。新版标准禁止“零添加”等易误导用语，是为了让标签概念前后一致、意义明确，触发同一律。

【满分作答示范】 B 项正确。标签里的“0”“100%”被醒目呈现，会让人把商标、比例、纯度、零添加等概念混同。新规排除这类误导表达，是要求同一思维过程中，概念前后一致、含义确定，满足“同一律”，不是矛盾律或排中律。

【采分点对照】
- 答案选B
- 食品标签中“0”“100%”被突出使用，容易把商标、比例、纯度、零添加等概念混在一起
- 新版标准禁止易误导用语，是要求同一思维过程中概念前后一致、含义确定，符合“同一律”，不是矛盾律或排中律
- 错项分析：A 项诱人，因为它抓到了概念混同，但“思维的一致性要求”对应矛盾律，不是同一律
- C 项错在没有出现同一对象同一方面既肯定又否定的自相矛盾
- D 项错在题干不是在“是”与“非”之间骑墙，而是概念使用不确定

## 七、选言推理、联言判断与复合判断

【本类怎么做】
- 先判断选言是相容还是不相容，再选推理规则。
- 联言判断要看各个联言支是否都成立。
- 复合判断题先拆成简单判断，再按真值条件核对。

【本类常见坑】
- 相容选言不能用不相容选言的排除规则。
- 一个联言支不成立，整个联言判断就不能成立。
- 把反对关系、矛盾关系和选言关系混用，会直接错判真假。

### 选言判断

#### 1. 2026海淀一模 第17题第（1）问（主观题）

【这道题考什么】 考选言推理或复合判断。抓手是：调查问卷的问题2问“本市无障碍设施存在的主要问题”，多选项只列“设计不合理、标识不清、相关部门维护不到位”，没有“其他”或补充说明。

【题目材料】

```text
17.（6分）
调查研究要讲求科学方法。某校“模拟政协”社团同学准备围绕本市无障碍环境建设情况展开调研。以下是同学们设计的调查问卷（节选）。
调查问卷（节选）
问题1. 您的身份（单选）：
□老年人（60岁及以上） □残障人士
□普通在职职工
□离退休人员
□相关行业从业者（如城市管理、物业等）
□其他
□儿童（14岁以下）
问题2. 您认为本市无障碍设施存在的主要问题是（可多选）：
□设计不合理
□标识不清
□相关部门维护不到位
运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）
为提高调研活动的科学性，提出具体可行的建议。（4分）
```

【设问】 运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）

【怎么想到的】 题目让指出问卷中的逻辑错误，问题2又是多选题，就要检查选言支是否覆盖有选择价值的情况。无障碍设施问题可能还包括坡道缺失、通行被占用、设施损坏、信息无障碍不足等，问卷只列三类原因，且没有“其他”或补充说明，容易把真实问题排除在选项外。

【满分作答示范】 问题2遗漏选言支。设施问题不能只列设计、标识、维护三类，还应允许其他情况或补充说明；选项不穷尽会排除真实意见。

【采分点对照】
- 问题2存在选言判断遗漏的逻辑错误：设施问题选项只列设计、标识和维护三类，缺少“其他”或补充说明，不能覆盖可能具有选择价值的其他情况
- 调查选项没有穷尽合理可能，就会把受访者的真实意见排除在外，导致收集到的信息不完整，影响后续判断和建议的可靠性

### 反对关系与联言判断

#### 2. 2026西城一模 第19题第（3）问（主观题）

【这道题考什么】 考联言判断或联言推理。抓手是：乙同时否定“所有村务必须公开”和“所有村务都不必公开”两个极端全称判断，材料信号不是自相矛盾，而是在两个极端之间保留“有些公开、有些不公开”的空间。

【题目材料】

```text
19.（12分）推进美丽乡村建设、完善乡村公共服务。
材料一 某村规划建设集休闲健身、生态绿化、文化展示于一体的文化生态公园,却在推进中却遭遇一连串难题:
乡镇政府:必须严守项目预算、建设标准、生态红线
村“两委”、村干部:担心规划与民意脱节、项目推进受阻
邻村及本村土地被占用村民:担心个人利益受损,有一定抵触情绪
外出务工村民:无法回村参与,担心自己的诉求被忽略
材料二 面对多方意见,村党支部创新推行“云端+院落夜话”议事机制(右图):一方面,线上议事群实时发布议题、收集意见,组织视频连线让外出村民全程参与讨论;另一方面,在院落、广场组织大家面对面商量,直接回应涉地村民的实际诉求。同时,联动政府、村干部与村民代表,在村规划、生态保护和群众利益之间找到平衡点,最终形成方案,推动实施。
(1)遵循民主程序要求,将右图最后一环节补充完整。（1分）
(2)结合材料,运用《政治与法治》知识,谈谈“云端+院落夜话”议事机制是如何破解“一连串难题”的。（7分）
(3)任选两位村民的观点,运用形式逻辑知识,说明其理解是否正确。（4分）
甲:议事协商应维护公共利益,个人补偿诉求不是公共利益,所以个人补偿诉求不应纳入议事协商。
乙:对于村务公开,我既不同意“所有村务必须公开”,也不同意“所有村务都不必公开”。
丙:只要涉及村民切身利益,就应由村民会议讨论决定。村委会没有讨论这件事,说明这件事不涉及村民切身利益。
```

【设问】 任选两位村民的观点，运用形式逻辑知识，说明其理解是否正确。（4分）

【怎么想到的】 乙同时反对“所有村务必须公开”和“所有村务都不必公开”，其实是在拒绝两个极端全称判断。形式逻辑中，两个全称判断如果一个肯定、一个否定，针对同一对象范围时构成反对关系：它们不能同真，但可以同假。

【满分作答示范】 乙的判断正确。两个极端说法分别是“全都公开”和“全都不公开”，二者不能同时为真，但可以同时为假；排除这两个极端以后，仍然可以保留“有的应公开、有的不必公开”的中间情形，所以它们是反对关系而不是矛盾关系。

【采分点对照】
- 乙观点正确
- “所有村务必须公开”和“所有村务都不必公开”是两个极端全称命题，二者不能同真，但可以同假，属于反对关系而不是矛盾关系
- 否定这两个极端，只是排除“全部公开”和“全部不公开”两种绝对说法，并不排除“有些应公开、有些不必公开”的中间情形，因此不违反逻辑规则

### 不相容选言推理（有效式）

#### 3. 2025海淀一模 第21题第（1）问（主观题）

【这道题考什么】 考不相容选言推理的否定肯定式。抓手是：设问要求以指定判断为结论，构造一个结构正确的演绎推理。

【题目材料】

```text
21.（8分）
外贸进出口是拉动经济增长的重要引擎。2024 年,我国外贸总量连续跨过42、43 两个万亿级台阶,
全年进出口总值达到43.85 万亿元人民币,再创历史新高。这一成绩的取得,离不开新动能的巨大推动力。
·绿色贸易领跑全球。我国绿色产品不仅丰富了全球供给,也为全球应对气候变化和绿色低碳转型作
出了巨大贡献。
·数字贸易蓬勃发展。2024 年我国跨境电商进出口2.63 万亿元,增长10.8%。
·高水平开放平台带动作用明显。综合保税区是我国开放程度最高、优惠政策最集中、功能最齐全的
海关特殊监管区域。我国现有167 个综合保税区,分布在全国各地,在产业转型升级方面发挥了重要作用。
·我国市场潜力不仅在于人口规模庞大,更在于消费增长迅速、需求层次丰富,不断为全球贸易注入
新的活力。
(1)以“外贸进出口是拉动经济增长的重要引擎”为结论,写出一个正确的演绎推理。（2分）
(2)结合材料,运用《当代国际政治与经济》知识,说明我国外贸为何能连上两个万亿级台阶。（6分）
```

【设问】 以“外贸进出口是拉动经济增长的重要引擎”为结论，写出一个正确的演绎推理。（2分）

【怎么想到的】 这题不要硬从材料里找被否定的现实前提。设问要的是形式正确的演绎推理，可以先构造“P或非P”的不相容选言判断，再否定后一种情况，推出指定结论。

【满分作答示范】 可写为：外贸进出口要么属于拉动经济增长的重要引擎，要么不属于这一类；现在后一种说法被否定；所以，外贸进出口是拉动经济增长的重要引擎。它是不相容选言推理的否定肯定式，结构有效。

【采分点对照】
- 构造不相容选言判断：外贸进出口要么属于拉动经济增长的重要引擎，要么不属于这一类
- 否定后一种情况，即否定“外贸进出口不属于这一类”
- 由否定一个选言支推出另一个选言支，得到结论：外贸进出口是拉动经济增长的重要引擎
- 也可按细则使用换质推理：由“外贸进出口不是非拉动经济增长的重要引擎”推出该结论

### 不相容选言推理无效式辨析

#### 4. 2025丰台期末 第9题（选择题）

【这道题考什么】 考选言推理或复合判断。抓手是：B 项只给出“小张或者去甘肃游学，或者去湖南游学”为真，却没有否定湖南这一支，不能直接肯定小张去甘肃。

【题目材料】

```text
9. 某中学以“赓续红色血脉传承红色基因”为主题,精心策划并组织了陕西、贵州、甘肃、湖南等几条研
学路线,每个学生都选择了一条研学路线。据此,下列说法逻辑正确的是( )
A. 由“小李既没报陕西研学,也没报贵州研学”为真,能推出“小李报湖南研学”为真
B. 由“小张或者去甘肃游学,或者去湖南游学”为真,能推出“小张去甘肃游学”为真
C. 由“王同学在研学中有所收获”为真,能推出“王同学主动将研学中的所见所闻与学科知识建立联系”
为真
D. 由“赵同学主动将研学中的所见所闻与学科知识建立联系”为真,能推出“赵同学在研学中有所收获”
为真
```

【设问】 9. 某中学以“赓续红色血脉传承红色基因”为主题，精心策划并组织了陕西、贵州、甘肃、湖南等几条研
学路线，每个学生都选择了一条研学路线。据此，下列说法逻辑正确的是（ ）
A.由“小李既没报陕西研学，也没报贵州研学”为真，能推出“小李报湖南研学”为真
B.由“小张或者去甘肃游学，或者去湖南游学”为真，能推出“小张去甘肃游学”为真
C.由“王同学在研学中有所收获”为真，能推出“王同学主动将研学中的所见所闻与学科知识建立联系”
为真
D.由“赵同学主动将研学中的所见所闻与学科知识建立联系”为真，能推出“赵同学在研学中有所收获”
为真

【怎么想到的】 B 项的迷惑性在“或者去甘肃，或者去湖南”已经为真，但它没有告诉我们湖南被排除，也没有给出甘肃被单独锁定的条件。不相容选言判断为真，只能说明两个选言支中恰有一个成立，不能在没有否定另一支时直接指定“去甘肃”。

【满分作答示范】 D 项正确。主动把研学见闻同学科知识联系起来，足以推出“有所收获”。B 项不能选，因为“小张去甘肃或湖南”为真时，若没有排除湖南，不能直接断定去甘肃。

【采分点对照】
- 答案选D
- 整题答案为 D
- D 把“主动将研学中的所见所闻与学科知识建立联系”作为获得研学收获的充分条件，肯定前件可以推出后件
- B 项不能选，因为“小张或者去甘肃，或者去湖南”为真，只说明选言判断成立，在没有否定湖南这一支时，不能直接推出小张去甘肃
- 错项分析：A 项错在排除陕西、贵州以后，还可能报甘肃或湖南，不能直接推出湖南
- B 项错在只知道“甘肃或湖南”这一选言判断为真，没有否定湖南，不能直接指定甘肃
- C 项错在“有所收获”范围很宽，可能来自体验、见闻、情感认同等，不能倒推出一定主动把所见所闻与学科知识建立联系

### 复合假言与选言推理链

#### 5. 2024东城一模 第8题（选择题）

【这道题考什么】 考选言推理或复合判断。抓手是：先由小徐未选物理推出小赵未选地理，再推出小王未选政治。

【题目材料】

```text
8.某班主任欲了解四位同学的选科情况。现已得知:
1只有小徐选物理,小赵才选地理;2或者小李选政治,或者小王选政治;
3当且仅当小孙选政治,小李选政治;4如果小王选政治,那么小赵选地理。
随后,班主任又得知了某一信息,他据此必然得出“小李选政治”的结论。该信息是
A. 小孙未选政治
B. 小赵选地理
C. 小王选政治
D. 小徐未选物理
```

【设问】 8.某班主任欲了解四位同学的选科情况。现已得知：①只有小徐选物理，小赵才选地理；②或者小李选政治，或者小王选政治；③当且仅当小孙选政治，小李选政治；④如果小王选政治，那么小赵选地理。随后，班主任又得知了某一信息，他据此必然得出“小李选政治”的结论。该信息是
A.小孙未选政治
B.小赵选地理
C.小王选政治
D.小徐未选物理

【怎么想到的】 D 项“小徐未选物理”一进来，整条链就能跑通。①“只有小徐选物理，小赵才选地理”说明小徐选物理是小赵选地理的必要条件，否定小徐选物理，就能否定小赵选地理。

【满分作答示范】 D 项正确。补充“小徐未选物理”后，①可推出小赵不选地理；再用④的否定后件式，可推出小王不选政治。②给出小李与小王至少一人选政治，排除小王后，只能肯定小李选政治。A 会推出相反结果，B 不能排除小王，C 肯定一个选言支不能推出另一个支。

【采分点对照】
- 答案选D
- 由“只有小徐选物理，小赵才选地理”可知，小徐选物理是小赵选地理的必要条件
- 现在小徐未选物理，可推出小赵未选地理
- 再由“如果小王选政治，那么小赵选地理”推出小王未选政治，最后用“小李或小王选政治”排除小王，必然推出小李选政治
- 错项分析：A 项“小孙未选政治”会由③推出小李未选政治，方向相反
- B 项“小赵选地理”不能推出小王是否选政治，更不能排除小王
- C 项“小王选政治”与“小李或小王选政治”相容，不能必然推出小李也选政治

### 选言推理与逆向思维复合辨析

#### 6. 2024海淀一模 第6题（选择题）

【这道题考什么】 考选言推理或复合判断。抓手是：围棋一步棋存在多种可选走法，可用选言推理在备选方案中分析取舍。

【题目材料】

```text
6. 围棋是体育、文娱和逻辑思维三位一体的活动，正确运用推理方法是提高棋艺的重要手段。从开盘布局、中盘拼杀，到收官阶段中的每一手棋的推敲、计算，通常都表现为各种形式的判断推理。围棋实战中
①一步棋有多种走法，运用选言推理可以从中选择最优的解决方案
②断定不同走法与结果之间的必然联系，应运用必要条件假言判断
③选点落子犹豫不决时，运用完全归纳推理方法才能取得最终胜利
④一步棋与双方都有关联，采用逆向思维有助于作出正确判断推理
A.①②
B.①④
C.②③
D.③④
```

【设问】 6.围棋是体育、文娱和逻辑思维三位一体的活动，正确运用推理方法是提高棋艺的重要手段。从开盘布局、中盘拼杀，到收官阶段中的每一手棋的推敲、计算，通常都表现为各种形式的判断推理。围棋实战中
①一步棋有多种走法，运用选言推理可以从中选择最优的解决方案
②断定不同走法与结果之间的必然联系，应运用必要条件假言判断
③选点落子犹豫不决时，运用完全归纳推理方法才能取得最终胜利
④一步棋与双方都有关联，采用逆向思维有助于作出正确判断推理
A.①②
B.①④
C.②③
D.③④

【怎么想到的】 围棋“一步棋有多种走法”，先触发选言判断和选言推理：在多个可选方案中分析取舍。一步棋既影响自己也影响对手，推敲时从对手应法、结果反推当前落点，触发逆向思维。

【满分作答示范】 B 项正确。一步棋有多种可选走法，先形成多个选言支并比较取舍，体现选言推理；落子还会牵动双方后续局势，可以从对手应法或可能结果反推当前落点，体现逆向思维。

【采分点对照】
- 答案选B
- 一步棋有多种走法，先形成多个可选支项，运用选言推理分析取舍
- 一步棋又同时牵动双方局势，从对手应法或结果倒推当前落点，触发逆向思维
- ②没有必要条件句式支撑，③把不可能穷尽的棋局误说成完全归纳
- 错项分析：A 项诱人，因为①确实抓住了多种走法对应选言推理
- 错在②把走法和结果的一般联系硬说成必要条件
- C 项把②③组合起来，两个都不成立
- D 项诱人，因为④正确
- 错在③把无法穷尽的围棋落子说成完全归纳，并夸大到“才能取得最终胜利”

### 联言判断类型识别

#### 7. 2024海淀一模 第7题（选择题）

【这道题考什么】 考联言判断或联言推理。抓手是：“不是洋货买不起，而是国货更有性价比”包含两个同时成立的判断：否定前一说法，并肯定后一说法。

【题目材料】

```text
7.“不是洋货买不起,而是国货更有性价比。”近来,
“不是XX 买不起,而是XX 更有性价比”这一句
式走红。下列判断中,与上述句式判断类型一致的是
A.一个数是偶数,当且仅当,这个数能被2 整除
B.极力之所举,则无不胜也
C.这个推理的前提真实,并且推理形式有效
D.代书遗嘱无效,除非有两个以上无利害关系的见证人在场见证
```

【设问】 7． “不是洋货买不起，而是国货更有性价比。 ”近来， “不是 XX 买不起，而是 XX 更有性价比”这一句
式走红。下列判断中，与上述句式判断类型一致的是
A.一个数是偶数，当且仅当，这个数能被 2 整除
B.极力之所举，则无不胜也
C.这个推理的前提真实，并且推理形式有效
D.代书遗嘱无效，除非有两个以上无利害关系的见证人在场见证

【怎么想到的】 “不是洋货买不起，而是国货更有性价比”不是一个单纯否定句，而是同时断定两件事：前一说法不成立，后一说法成立。把它翻译成判断结构，就是“并非前一说法，并且后一说法成立”，属于联言判断。

【满分作答示范】 应选 C。原句同时表达两层意思：不是因为洋货买不起，而是因为国货更有性价比。它把一个否定判断和一个肯定判断用“而是”连在一起，结构上就是联言判断；C 项同样由两个判断共同成立构成。

【采分点对照】
- 答案选C
- 题干“不是洋货买不起，而是国货更有性价比”同时断定两件事：前一说法不成立，后一说法成立，结构就是“并非 P，并且 Q”的联言判断
- C 项“前提真实，并且推理形式有效”也由两个判断通过“并且”联结，类型一致
- 错项分析：A 项“当且仅当”是充分必要条件判断
- B 项“极力之所举，则无不胜也”带有条件判断结构
- D 项“除非有两个以上无利害关系的见证人在场见证”也是条件判断

### 联言判断真值条件

#### 8. 2024朝阳二模 第19题第（2）问（主观题）

【这道题考什么】 考联言判断或联言推理。抓手是：“与天地合其德，与日月合其明，与四时合其序”由三个并列联言支共同组成，每一支都被同时肯定，整体判断要求三个支判断共同成立。

【题目材料】

```text
19. （16分）
中华文明拥有五千多年不间断的历史,积淀形成辉煌灿烂的中华优秀传统文化,中
华优秀传统文化的特质赋予中国式现代化深厚底蕴,给予其精神和思想力量。
生生之宇宙观
宇宙处于生生不息的变化之中。“天地之大德曰生”“富有之谓大业,日新之谓盛德,
生生之谓易”。宇宙永久的变易包含永远的革新,是生命的不断充实、成长、更新和展开。
一体之天人观
人类与天地为一体。天地的交合生成了世界,赋予了人的身体和本性,所有人都是
天地生育的子女;不仅如此,万物和人类一样,也是天地所生。因此,他人都是自己的同
胞,万物都是自己的朋友。
法天地之人生观
人应该效法天地之德。“夫大人者,与天地合其德,与日月合其明,与四时合其序。”天
之德在生育万物而不息,地之德在广阔博大,君子应学习天地之德,自强不息、厚德载物。
(1)生生之宇宙观体现了辩证思维的 1 特征。人效法天地之德体现的推理
类型是 2 推理。（4分）
(2)“夫大人者,与天地合其德,与日月合其明,与四时合其序。”是哪种复合判断? 该
复合判断为真的条件是什么? （5分）
(3)“中华优秀传统文化的特质赋予中国式现代化以深厚底蕴”。结合材料,综合运
用所学,谈谈你对这句话的理解。（7分）
```

【设问】 “夫大人者，与天地合其德，与日月合其明，与四时合其序。”是哪种复合判断？该复合判断为真的条件是什么？（5分）

【怎么想到的】 原句连续说“与天地合其德，与日月合其明，与四时合其序”，三个分句并列出现，而且意思上要求共同成立。只要有一个分句不成立，就不能说整个判断为真。

【满分作答示范】 这句话由“合其德、合其明、合其序”三个并列判断组成，是联言判断。只有三个支判断都成立，整体判断才为真；其中任一部分不成立，整个联言判断就不能成立。

【采分点对照】
- “与天地合其德，与日月合其明，与四时合其序”是由三个并列支判断组成的联言判断
- 只有“合其德”“合其明”“合其序”每一个联言支都为真，整个联言判断才为真，只要其中一个联言支为假，整个联言判断就是假的

### 复合判断识别与逻辑规则辨析

#### 9. 2024顺义二模 第6题（选择题）

【这道题考什么】 考选言推理或复合判断。抓手是：刑法第二十条正当防卫条文不是一个单一简单判断，而是把目的、对象、正在进行的不法侵害、制止行为、损害后果、责任结论等多个判断联结起来，共同限定何种行为属于正当防卫、何种情形不负刑事责任。

【题目材料】

```text
6.在生活和工作中，有些听起来似乎有道理，但仔细想起来，又疑窦丛生，这就需要学习形式逻辑，提升逻辑思维能力。下列观点和逻辑分析正确的是
A.法定继承第一顺位继承人中的子女，包括婚生子女、非婚生子女、养子女和有扶养关系的继子女；该观点对概念外延的划分犯了“多出子项”的逻辑错误。
B.若a=b，则ac=bc；该判断中，a=b是ac=bc的充分必要条件。
C.刑法第二十条规定：“为了使国家、公共利益、本人或者他人的人身、财产和其他权利免受正在进行的不法侵害，而采取的制止不法侵害的行为，对不法侵害人造成损害的，属于正当防卫，不负刑事责任。”该判断属于复合判断。
D.“服务员同志，请当心，你的手指浸到我的汤里去了。”“没有关系，汤不烫，我不痛。”该回答违反了排中律。
```

【设问】 6.在生活和工作中，有些听起来似乎有道理，但仔细想起来，又疑窦丛生，这就需要学习形式逻辑，提升逻辑思维能力。下列观点和逻辑分析正确的是
A.法定继承第一顺位继承人中的子女，包括婚生子女、非婚生子女、养子女和有扶养关系的继子女；该观点对概念外延的划分犯了“多出子项”的逻辑错误。
B.若a=b，则ac=bc；该判断中，a=b是ac=bc的充分必要条件。
C.刑法第二十条规定：“为了使国家、公共利益、本人或者他人的人身、财产和其他权利免受正在进行的不法侵害，而采取的制止不法侵害的行为，对不法侵害人造成损害的，属于正当防卫，不负刑事责任。”该判断属于复合判断。
D.“服务员同志，请当心，你的手指浸到我的汤里去了。”“没有关系，汤不烫，我不痛。”该回答违反了排中律。

【怎么想到的】 C 项的刑法条文不是一个简单判断，它同时包含目的、保护对象、正在进行的不法侵害、制止行为、造成损害、责任结论等多个判断，并通过条件关系和结论关系组合在一起，所以属于复合判断。A 项把法定继承中“子女”的具体类型误判为划分错误。

【满分作答示范】 应选 C。刑法条文把防卫目的、保护对象、正在发生的不法侵害、制止行为、损害结果和责任结论放在一个条件结构中，已经不是单一性质判断，而是多个判断组合成的复合判断。A、B、D 分别误判划分、条件关系和逻辑规律。

【采分点对照】
- 答案选C
- 刑法第二十条的正当防卫表述不是单一性质判断，而是把目的、保护对象、正在进行的不法侵害、制止行为、造成损害和责任结论等多个判断按条件关系联结起来，所以属于复合判断
- A、B、D分别误判划分、条件和逻辑规律
- 错项分析：A 项错在婚生子女、非婚生子女、养子女和有扶养关系的继子女本来属于法律列明的子女范围，不是多出子项
- B 项错在只成立充分条件，不成立充分必要条件
- D 项错在把答非所问误判为排中律

## 八、真假关系、逻辑规律与关系判断

【本类怎么做】
- 先锁定同一对象、同一时间、同一方面，再判断是否违反同一律、矛盾律或排中律。
- 真假话题用假设法逐项代入，保留唯一能自洽的组合。
- 关系判断题要看关系是否对称、反对称、传递或非传递。

【本类常见坑】
- 没有同一条件，就不能轻易说自相矛盾。
- 两不可违反排中律，二者都真违反矛盾律。
- 日常亲近、喜欢、相邻等关系，不能想当然推出传递性。

### 矛盾律

#### 1. 2026东城期末 第17题第（2）问（主观题）

【这道题考什么】 考矛盾律。抓手是：主张一方面要求完整保留历史街巷的一砖一瓦，另一方面又主张对无法适应现代需要的部分进行必要拆除和改造。

【题目材料】

```text
17. 人形机器人“入职”汽车生产线，安防机器人智能巡逻，科研机器人在实验室“上岗”……场景作为系统性验证新技术、新产品、新业态的具体情境，赋能新质生产力发展。
材料一 推动场景创新，制度性障碍亟待破解。
障碍1：高价值数据产权界定模糊、缺乏开放机制。政府、央企等掌握核心场景和数据资源，民营企业在特定领域面临较高的市场准入门槛，各地各部门场景建设存在孤岛化问题。
障碍2：场景业主方与技术供给方之间信息不对称、信任成本高、交易效率低。大量场景富集地区“有场景、缺技术”，而科技企业集聚地方“有技术、缺场景”。
障碍3：场景数据价值、利益分配规则不清楚。新技术新产品首试首用的政策保险、容错机制尚未普及，缺乏有效的社会分担机制，抑制企业创新活力。
（1）在上述障碍中任选两个，分别提出政策性建议，并运用《经济与社会》知识，说明理由。
材料二 某市发布老城区“微更新+智慧场景”需求。以下是关于更新方案的一些主张。
主张1：我们既要完整保留历史街巷的一砖一瓦，也要对其中无法适应现代需要的部分进行必要的拆除和改造。
主张2：要提升垃圾分类效率，必须引入智能垃圾箱。因为，智能垃圾箱含有无接触投放和自动积分奖励功能，如果引入智能垃圾箱，垃圾分类效率就能得到提升。
主张3：有些科学民主的更新方案是采用“居民提案—AI智能模拟—多轮投票”模式制定的。“立体花园+口袋公园”复合型公共空间方案是通过此模式制定的。因此，“立体花园+口袋公园”复合型公共空间方案是科学民主的更新方案。
（2）运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）
```

【设问】 运用形式逻辑知识，论证三项主张是否符合逻辑。（6分）

【怎么想到的】 主张1一边说要完整保留历史街巷的一砖一瓦，一边又允许对无法适应现代需要的部分进行必要拆除和改造。判断是否违反矛盾律，要看是不是在同一时间、同一对象、同一方面作出互相否定的判断。

【满分作答示范】 主张1不合逻辑。如果“完整保留”和“必要拆改”指向同一街巷、同一时间、同一方面，就不能同时成立；把两个相互排斥的判断并列肯定，违背矛盾律要求的思维一致性。

【采分点对照】
- 主张1不符合逻辑
- “完整保留历史街巷的一砖一瓦”和“对无法适应现代需要的部分进行必要拆除和改造”如果指向同一对象、同一时间、同一方面，就不能同时为真
- 主张把两个相互排斥的判断并列肯定，违反矛盾律关于同一思维过程中不能自相矛盾的要求

### 矛盾关系与真假判断

#### 2. 2026东城期末 第7题（选择题）

【这道题考什么】 考真假关系与逻辑规律。抓手是：四位老师的判断中，吴老师和王老师的话正好形成一真一假的矛盾关系。

【题目材料】

```text
7. 某高中举办“科技+体育”运动会,设置四大项目:“AI 运动数据挑战赛”“AI 主题闯关”“跨年级智
能接力赛”“人机赛跑”。四位老师对比赛结果作出如下预测:
周老师:“人机赛跑”会达标。
吴老师:如果“AI 运动数据挑战赛”达标,那么“跨年级智能接力赛”就不会达标。
郑老师:如果“人机赛跑”未达标,那么“AI 主题闯关”也未达标。
王老师:“AI 运动数据挑战赛”和“跨年级智能接力赛”都会达标。
上述四人的预测仅有一个符合事实,以下哪项不可能为真( )
A. AI 运动数据挑战赛达标,AI 主题闯关未达标
B. 跨年级智能接力赛达标,AI 运动数据挑战赛达标
C. AI 主题闯关达标,跨年级智能接力赛未达标
D. AI 主题闯关达标,人机赛跑未达标
```

【设问】 7. 某高中举办“科技+体育”运动会，设置四大项目：“AI 运动数据挑战赛”“AI 主题闯关”“跨年级智
能接力赛”“人机赛跑”。四位老师对比赛结果作出如下预测：
周老师：“人机赛跑”会达标。
吴老师：如果“AI 运动数据挑战赛”达标，那么“跨年级智能接力赛”就不会达标。
郑老师：如果“人机赛跑”未达标，那么“AI 主题闯关”也未达标。
王老师：“AI 运动数据挑战赛”和“跨年级智能接力赛”都会达标。
上述四人的预测仅有一个符合事实，以下哪项不可能为真（ ）
A.AI 运动数据挑战赛达标，AI 主题闯关未达标
B.跨年级智能接力赛达标，AI 运动数据挑战赛达标
C.AI 主题闯关达标，跨年级智能接力赛未达标
D.AI 主题闯关达标，人机赛跑未达标

【怎么想到的】 四位老师只有一人说真话，先要找天然互相冲突的一组。吴老师说“若 AI 运动数据挑战赛达标，则跨年级智能接力赛不达标”，王老师却说二者都会达标，二者正好构成一真一假的关系。

【满分作答示范】 A 项正确。吴老师的条件判断和王老师的“两项都达标”互相冲突，二者一真一假；在四人只有一人说真话的限制下，可推出周、郑为假，人机赛跑未达标而 AI 主题闯关达标。

【采分点对照】
- 答案选A
- 吴老师“若数据挑战达标则接力不达标”与王老师“二者都会达标”构成一真一假
- 四人仅一真，进而可推出周老师为假、郑老师也为假，所以人机赛跑未达标且 AI 主题闯关达标
- A 项说 AI 主题闯关未达标，与必然结果冲突，故“不可能为真”
- 错项分析：B 项看似与王老师预测一致，但当王老师为唯一真话时，AI 运动数据挑战赛和跨年级智能接力赛都达标是可能情况
- C 项在吴老师为唯一真话时也可能成立，不能判为“不可能”
- D 项由周老师假、郑老师假可以推出人机赛跑未达标且 AI 主题闯关达标，反而是必然可能的情况
- A 项错在 AI 主题闯关未达标，而由唯一真话关系可推出它应当达标

### 形式逻辑综合选择题

#### 3. 2024朝阳一模 第6题（选择题）

【这道题考什么】 考真假关系与逻辑规律。抓手是：A 项把物权、债权、知识产权同著作权、商标权并列，出现越级划分。

【题目材料】

```text
6.要想准确鲜明地表达思想，思维必须合乎逻辑。下列表达中，符合逻辑规则的是
A.财产权可分为物权、债权、知识产权、著作权、商标权
B.我不赞成所有人都有崇高的理想，也不赞成所有人都没有崇高的理想
C.所有的科技人员都是懂计算机的，并且有些不懂计算机的是科技人员
D.我无法一天读完老舍的作品，«茶馆»是老舍的作品，因此我无法一天读完«茶馆»
```

【设问】 6.要想准确鲜明地表达思想，思维必须合乎逻辑。下列表达中，符合逻辑规则的是
A.财产权可分为物权、债权、知识产权、著作权、商标权。
B.我不赞成所有人都有崇高的理想，也不赞成所有人都没有崇高的理想。
C.所有的科技人员都是懂计算机的，并且有些不懂计算机的是科技人员。
D.我无法一天读完老舍的作品，《茶馆》是老舍的作品，因此我无法一天读完《茶馆》。

【怎么想到的】 这类综合题不能凭语感选“顺耳”的表达，要逐项找每个选项是否真的违反逻辑规则。A 的问题是同一次划分中混入不同层级的子项。

【满分作答示范】 B 项正确。“人人都有崇高理想”和“人人都无崇高理想”这两个全称说法是反对关系，可以一起为假，但不能一起为真；同时反对二者，并不违反逻辑规则。

【采分点对照】
- 答案选B
- B 同时不赞成“所有人都有崇高理想”和“所有人都没有崇高理想”，这两个全称判断是反对关系，可以同假，不能同真
- 同时反对二者并不违反逻辑规则
- A 是越级划分，C 自相矛盾，D 偷换“老舍的作品”的外延
- 错项分析：A 项诱人，因为列出了多个财产权类型
- 错在物权、债权、知识产权可以同层列举，著作权、商标权又属于知识产权内部类型，不能并列划分
- C 项诱人，因为两句话都围绕科技人员
- 错在“所有科技人员都懂计算机”和“有些不懂计算机的是科技人员”不能同真
- D 项诱人，因为它像一个三段论
- 错在“老舍的作品”在前提中指老舍全部作品，在结论中换成单篇《茶馆》，犯四概念错误

### 关系判断与非传递关系

#### 4. 2026朝阳一模 第5题（选择题）

【这道题考什么】 考关系判断。抓手是：足球赛里“1 班赢 2 班、2 班赢 3 班”只是两场具体比赛结果，胜负关系会受对阵、状态和场次影响，不能像大小关系那样必然传递到 1 班与 3 班之间。

【题目材料】

```text
5. “健康第一”既是理念又是责任，更要落到行动上。某校举办
校园足球、篮球和排球三项体育比赛，赛场内外精彩纷呈。下列分析正确的是（ ）
A.1 班同学没参加全部三项比赛——可推出“1 班同学参加了一项或两项比赛”为真
B.“如果说张同学是足球天赋型选手，那么我就是努力养成型选手。”——该说法属于充要条件假言判断
C.本次体育赛事的三项比赛中包含足球比赛、篮球比赛——该表述犯了概念外延“划分不全”的逻辑错误
D.在足球赛中，1 班赢了2 班，2 班赢了3 班——1 班与3 班的胜负关系属于非传递关系
```

【设问】 5. “健康第一”既是理念又是责任，更要落到行动上。某校举办
校园足球、篮球和排球三项体育比赛，赛场内外精彩纷呈。下列分析正确的是（ ）
A.1 班同学没参加全部三项比赛——可推出“1 班同学参加了一项或两项比赛”为真
B.“如果说张同学是足球天赋型选手，那么我就是努力养成型选手。”——该说法属于充要条件假言判断
C.本次体育赛事的三项比赛中包含足球比赛、篮球比赛——该表述犯了概念外延“划分不全”的逻辑错误
D.在足球赛中，1 班赢了2 班，2 班赢了3 班——1 班与3 班的胜负关系属于非传递关系

【怎么想到的】 关系是否传递，要看“甲和乙有这种关系、乙和丙有这种关系”时，能不能必然推出“甲和丙也有这种关系”。足球赛中 1 班赢 2 班、2 班赢 3 班，并不能保证 1 班一定赢 3 班，胜负关系不具有传递性。

【满分作答示范】 D 项正确。胜负关系不传递：1 班胜 2 班、2 班胜 3 班，不能保证 1 班也胜 3 班。

【采分点对照】
- 答案选D
- 判断关系是否传递，要看“甲对乙有此关系、乙对丙有此关系”能否必然推出“甲对丙也有此关系”
- 足球赛中 1 班赢 2 班、2 班赢 3 班，不保证 1 班一定赢 3 班，所以胜负关系属于非传递关系
- 错项分析：A 项错在“没参加全部三项”不能排除一项都没参加
- B 项错在“如果……那么……”表达充分条件，不是充要条件
- C 项错在题干只是说明赛事包含足球、篮球，没有作完整划分

#### 5. 2025丰台二模 第13题（选择题）

【这道题考什么】 考关系判断。抓手是：“同学”关系只说明两个人之间存在同一学习共同体中的关联。

【题目材料】

```text
13. 逻辑思维过程是由概念、判断和推理来承担和表现的。只有做到准确把握概念、正确 运用判断、精确进
行推理,思维才能合乎逻辑的要求。下列说法正确的是
A. 甲是乙的同学,乙是丙的同学,“同学”关系是一种非传递关系
B.“国际关系的基本形式有合作和竞争”,这一判断对母项做出正确划分
C. 从“有的人不是说谎者”这一前提,能够通过换位推理必然得出结论
D. “文学是用文字表达的语言艺术”明确了文学的内涵,揭示了文学的本质属性
```

【设问】 13. 逻辑思维过程是由概念、判断和推理来承担和表现的。只有做到准确把握概念、正确 运用判断、精确进
行推理，思维才能合乎逻辑的要求。下列说法正确的是
A.甲是乙的同学，乙是丙的同学，“同学”关系是一种非传递关系
B.“国际关系的基本形式有合作和竞争”,这一判断对母项做出正确划分
C.从“有的人不是说谎者”这一前提，能够通过换位推理必然得出结论
D.“文学是用文字表达的语言艺术”明确了文学的内涵，揭示了文学的本质属性

【怎么想到的】 “同学”关系不保证传递：甲是乙的同学、乙是丙的同学，甲和丙可能同校不同班，也可能互不相识，不能必然推出甲是丙的同学。B 项只说“合作和竞争”，没有穷尽国际关系基本形式。

【满分作答示范】 应选 A。同学关系不具有必然传递性：甲是乙的同学、乙是丙的同学，只能说明两组关系分别成立，不能推出甲也一定是丙的同学。B、C、D 分别存在划分不全、换位不当和定义过窄的问题。

【采分点对照】
- 答案选A
- 同学关系不保证传递：甲是乙的同学、乙是丙的同学，只说明两组人分别存在同学关系，不能必然推出甲也是丙的同学
- B 划分不全，C 从特称否定判断不能换位推出必然结论，D 的定义范围过窄
- 错项分析：B 项诱人，因为合作和竞争确实是国际关系基本形式中的重要类型
- 错在它没有穷尽全部基本形式，不能说作出了正确划分
- C 项诱人，因为很多性质判断可换位
- 错在特称否定判断不能换位推出必然结论
- D 项诱人，因为它像定义
- 错在“用文字表达的语言艺术”范围过窄，不能完整揭示文学本质属性

### 排中律与两不可错误

#### 6. 2025朝阳期末 第19题（主观题）

【这道题考什么】 考排中律的边界。抓手是：甲既不接受“使用融雪剂”，又不接受“禁止使用融雪剂”，等于同时否定一对互相排斥且不能同时为假的判断，材料要求学生检查是否违背排中律。

【题目材料】

```text
19.（7分）
某小区居民讨论冬季应该如何开展扫雪工作。
甲:我不同意使用融雪剂,但是我也不同意禁止使用融雪剂。
乙:扫雪工作既要快速完成方便居民出行,又要慢慢清扫以免遗漏任何一处积雪。
丙:所有为维护小区美好环境付出辛勤劳动的行为都是值得赞扬的。居民在小区扫雪是为维护小区美
好环境付出辛勤劳动的行为。所以,居民在小区扫雪是值得赞扬的。
结合材料,运用《逻辑与思维》知识,分析上述居民的话是否合乎逻辑,说明理由。
```

【设问】 结合材料，运用《逻辑与思维》知识，分析上述居民的话是否合乎逻辑，说明理由。

【怎么想到的】 甲的问题在于同时否定“使用融雪剂”和“禁止使用融雪剂”。这两个判断在同一讨论中构成相互矛盾的两种选择，不能同时都假，至少有一个为真。

【满分作答示范】 甲违反排中律。使用融雪剂与禁止使用融雪剂在同一场景中构成矛盾选择，不能同时都假；甲把两边都否定，等于拒绝在是与非之间作出明确判断。

【采分点对照】
- 使用融雪剂和禁止使用融雪剂在同一情境、同一对象、同一方面上构成相互矛盾判断，二者不能同假，必有一真
- 甲同时否定两个矛盾判断，等于在“是”与“非”之间拒绝作出明确判断，犯“两不可”错误，违反排中律对明确性的要求

### 矛盾律与自相矛盾错误

#### 7. 2025朝阳期末 第19题（主观题）

【这道题考什么】 考矛盾律的边界。抓手是：乙一方面要求快速完成扫雪，另一方面又要求慢慢清扫积雪，两个要求指向同一清雪过程、同一时间安排，却给出相反速度标准，构成同一方面的冲突。

【题目材料】

```text
19.（7分）
某小区居民讨论冬季应该如何开展扫雪工作。
甲:我不同意使用融雪剂,但是我也不同意禁止使用融雪剂。
乙:扫雪工作既要快速完成方便居民出行,又要慢慢清扫以免遗漏任何一处积雪。
丙:所有为维护小区美好环境付出辛勤劳动的行为都是值得赞扬的。居民在小区扫雪是为维护小区美
好环境付出辛勤劳动的行为。所以,居民在小区扫雪是值得赞扬的。
结合材料,运用《逻辑与思维》知识,分析上述居民的话是否合乎逻辑,说明理由。
```

【设问】 结合材料，运用《逻辑与思维》知识，分析上述居民的话是否合乎逻辑，说明理由。

【怎么想到的】 乙的问题在于同时肯定“快速完成扫雪”和“慢慢清扫积雪”。在同一场扫雪安排中，快速完成与慢慢清扫作为相互冲突的要求，不能同时为真。

【满分作答示范】 乙违反矛盾律。快速完成扫雪和慢慢清扫积雪在同一安排中相互排斥，乙同时肯定二者，等于同一对象同一方面既要快又要慢。

【采分点对照】
- 快速完成扫雪和慢慢清扫积雪在同一情境中提出相互排斥的行动要求，不能同时成立
- 乙同时肯定二者，等于在同一对象、同一时间、同一方面既要求“快”又要求“慢”，作出互相冲突的判断，犯自相矛盾错误，违反矛盾律关于思维一致性的要求

### 逻辑规则综合选择

#### 8. 2024东城一模 第6题（选择题）

【这道题考什么】 考真假关系与逻辑规律。抓手是：题干要求判断多个逻辑分析哪一项正确，D 项抓住“选择必须比较，不加比较作选择”中的内在冲突，指出其中包含逻辑矛盾。

【题目材料】

```text
6. 科学思维要符合认识规律、遵循逻辑规则。下列分析正确的是
A.时尚就是流行的生活方式。犯了“同语反复”的逻辑错误。
B.北京分为东城、西城、海淀等区。犯了“划分不全”的逻辑错误。
C.来到海边，小张尽情地呼吸着空气、阳光和海水。该语句含义不明确，不表达判断。
D.选择，是读者神圣的权利。但如果不加比较作选择，是滥用了此种权利。违背矛盾律。
```

【设问】 6.科学思维要符合认识规律、遵循逻辑规则。下列分析正确的是
A.时尚就是流行的生活方式。犯了“同语反复”的逻辑错误。
B.北京分为东城、西城、海淀等区。犯了“划分不全”的逻辑错误。
C.来到海边，小张尽情地呼吸着空气、阳光和海水。该语句含义不明确，不表达判断。
D.选择，是读者神圣的权利。但如果不加比较作选择，是滥用了此种权利。违背矛盾律。

【怎么想到的】 D 项的关键是“选择”本身就要求比较，不加比较却说自己在作选择，前后要求冲突，违反矛盾律。A 项“时尚就是流行的生活方式”即使有定义范围问题，也不是同语反复。

【满分作答示范】 D 项正确。选择本来就要比较取舍；一边说选择，一边排除比较，两个要求在同一语境中打架，构成自相矛盾。

【采分点对照】
- 答案选D
- “选择”本身要求在不同对象之间作比较和取舍
- “不加比较作选择”却把选择与非比较同时放在一起，前后要求冲突，属于同一时间、同一方面的自相矛盾，违背矛盾律
- A、B、C都是对错误类型的误判
- 错项分析：A 项诱人，因为“时尚”和“流行的生活方式”看起来像在重复
- 错在它并没有把被定义项原样重说一遍，不能判为同语反复
- B 项诱人，因为“东城、西城、海淀等区”列举不完整
- 错在“等”本来就是开放列举，并未声称完成严格划分
- C 项诱人，因为“呼吸阳光和海水”明显不合常理
- 错在它仍表达了一个陈述，只是概念搭配不当，不能说成“不表达判断”

### 枚举概括与同一对象替换

#### 9. 2024西城一模 第11题（选择题）

【这道题考什么】 考真假关系与逻辑规律。抓手是：①在题干已给出三舱段封闭集合的前提下，把问天/梦天/天和分别是舱段概括为三者都是舱段。

【题目材料】

```text
11. “问天”“梦天”“天和”不仅是中国空间站的三个舱段，也是中国航天人走过的路，它们连缀起中华民族求索太空的浩瀚征程。据此，以下推理正确的是
①“问天”是中国空间站的舱段，“梦天”是中国空间站的舱段，“天和”是中国空间站的舱段，所以，“问天”“梦天”“天和”都是中国空间站的舱段。
②“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，中国航天人走过的路，或是“问天”，或是“梦天”，或是“天和”。
③“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程，中国空间站的三个舱段是“问天”“梦天”“天和”，所以，中国空间站的三个舱段连缀起中华民族求索太空的浩瀚征程。
④“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程。
A.①②
B.①③
C.②④
D.③④
```

【设问】 11.“问天”“梦天”“天和”不仅是中国空间站的三个舱段，也是中国航天人走过的路，它们连缀起中华民族求索太空的浩瀚征程。据此，以下推理正确的是
①“问天”是中国空间站的舱段，“梦天”是中国空间站的舱段，“天和”是中国空间站的舱段，所以，“问天”“梦天”“天和”都是中国空间站的舱段。
②“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，中国航天人走过的路，或是“问天”，或是“梦天”，或是“天和”。
③“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程，中国空间站的三个舱段是“问天”“梦天”“天和”，所以，中国空间站的三个舱段连缀起中华民族求索太空的浩瀚征程。
④“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程。
A.①②
B.①③
C.②④
D.③④

【怎么想到的】 四个推理长得很像，差别在“有没有越过题干保证”。①只是在题干给定的三个舱段内部作概括：问天、梦天、天和分别是舱段，所以三者都是舱段，没有扩大范围。

【满分作答示范】 B 项正确。①只在问天、梦天、天和这三个给定舱段内概括，没有扩大范围；③把这三个舱段与“中国空间站的三个舱段”视作同一组对象，谓述可以转移。

【采分点对照】
- 答案选B
- ①只在题干给定的三个舱段这一封闭集合内概括，没有扩大对象范围
- ③把“中国空间站的三个舱段”和“问天、梦天、天和”作为同一组对象替换，谓述可以转移
- ②把三条路扩大成全部道路，④添加了前提没有保证的整体关系
- 错项分析：A项诱人，是因为①确实成立，但②把“问天、梦天、天和是航天人走过的路”误说成“中国航天人走过的路只能是这三种”，由列举跳成穷尽
- C项诱人，是因为④也用了题干的诗意表达，但④缺少“这三者作为一个整体连缀征程”的前提，只凭三个对象分别是路推不出整体关系
- D项诱人，是因为③成立，但④不成立
- 把③的同一对象替换和④的整体关系偷加混在一起，就会误选

### 真假话约束推理

#### 10. 2026丰台二模 第9题（选择题）

【这道题考什么】 考真假关系与逻辑规律。抓手是：四人各喜欢三种茶中的两种且不喜欢一种。

【题目材料】

```text
9.花茶是我国独具特色的茶叶品类,主要有茉莉花茶、白兰花茶和珠兰花茶等。甲、乙、
丙、丁四人对这三种茶的态度只有“喜欢”或“不喜欢”,每人恰好喜欢两种、不喜
欢一种,且四人中只有一人说假话,其余三人说真话。
甲:乙不喜欢茉莉花茶。
乙:我不喜欢的茶与丙相同。
丙:甲喜欢茉莉花茶,且丁不喜欢白兰花茶。
丁:甲、乙、丙三人中恰好有两人喜欢茉莉花茶。
据此,下列推断必然为真的是
1甲不喜欢白兰花茶
2乙喜欢珠兰花茶
3丙不喜欢珠兰花茶
4丁不喜欢白兰花茶
A. 13
B. 14
C. 23
D. 24
```

【设问】 9.花茶是我国独具特色的茶叶品类，主要有茉莉花茶、白兰花茶和珠兰花茶等。甲、乙、丙、丁四人对这三种茶的态度只有“喜欢”或“不喜欢”，每人恰好喜欢两种、不喜欢一种，且四人中只有一人说假话，其余三人说真话。甲说：乙不喜欢茉莉花茶。乙说：我不喜欢的茶与丙相同。丙说：甲喜欢茉莉花茶，且丁不喜欢白兰花茶。丁说：甲、乙、丙三人中恰好有两人喜欢茉莉花茶。据此，下列推断必然为真的是
①甲不喜欢白兰花茶
②乙喜欢珠兰花茶
③丙不喜欢珠兰花茶
④丁不喜欢白兰花茶
A.①③
B.①④
C.②③
D.②④

【怎么想到的】 真假话题不能靠直觉选一个可能情形，要列约束：每人恰好喜欢两种、不喜欢一种；四句话中只有一句假话。

【满分作答示范】 D 项正确。按“每人恰好喜欢两种、不喜欢一种”和“四人中只有一人说假话”枚举可行情形，所有满足条件的安排都保留两点：乙喜欢珠兰花茶，丁不喜欢白兰花茶；而甲是否不喜欢白兰花茶、丙是否不喜欢珠兰花茶会随可行情形变化，不能判为必然。所以必然为真的是②④。

【采分点对照】
- 答案选D
- 题干同时给出两组硬约束：每人恰好喜欢两种、不喜欢一种
- 四人中只有一人说假话
- 把四句话放进这两个约束中检验，所有可成立情形都会保留“乙喜欢珠兰花茶”和“丁不喜欢白兰花茶”，而①③只在部分情形成立，不能算必然
- 错项分析：A 项诱人，因为①③在某些安排中可能出现
- 错在题目问“必然为真”，二者都不能由所有约束稳定推出
- B 项含④这个必然真项，但①不必然
- C 项含②这个必然真项，但③不必然
- 组合题不能停在其中一项成立，必须两项都被约束保真

### 矛盾律与一致性要求

#### 11. 2026顺义二模 第18题第（1）问（主观题）

【这道题考什么】 考矛盾律。抓手是：车企初期判断 A：AI 自动驾驶系统全程正常，事故原因归于外部突发情况。

【题目材料】

```text
18.（14分）坚守人文温度、拥抱智能向善，推动人工智能健康有序发展。
材料一 某车企的 AI 自动驾驶车辆在道路行驶中发生碰撞事故，造成车辆受损。
初期企业回应：“车辆的 AI 自动驾驶系统全程正常工作，事故原因是前方车辆突然变道，属于不可预判的突发情况。”后续交警部门出具事故认定书，指出“AI 自动驾驶系统未及时识别前方车辆变道，未做出有效制动反应，是事故主要原因”。企业辩称：“系统在特定光线条件下存在感知延迟，属于技术待优化点。”
某班同学在对上述案例的分析时产生了分歧，借助 AI 平台进行评析。AI 平台给出以下两个结论。
结论一：企业前后说法自相矛盾。理由是：车企初期声称 AI 系统全程正常工作，事故系不可预判突发情况，将责任完全归于外部；交警认定后又改口说系统存在感知延迟、属于技术待优化点，承认系统存在问题。车企前后两个判断相互冲突，违反思维的确定性要求。
结论二：企业没有坚持实事求是。理由是：交警认定书已明确事故主因是系统未及时识别、未有效制动，属于客观事实；车企初期刻意回避系统缺陷，用外部原因掩盖技术问题，不是基于事实的理性分析，而是主观臆断、回避问题。
（1）结合材料，运用《逻辑与思维》知识，请你对 AI 分析的观点进行点评。（6分）
材料二 2026年一款名为 OpenClaw 的开源 AI 智能体风靡。因其图标是一只鲜红的龙虾，训练这款 AI，被网友戏称为“养龙虾”。
相较传统 AI 聊天机器人，这只“龙虾”能做的事多得多：接管键盘鼠标、自动整理文件、起草邮件、填写表格、分析数据……一句话，不仅能“动嘴”回答，更能“动手”执行。于是，“龙虾”瞬间点燃了全球开发者的热情，成为最受瞩目的开源项目之一。
但就在无数人欢呼“生产力革命”到来时，质疑声也越来越多：有人账户里的钱被悄悄转走，有人电脑被黑客远程控制，还有人积累了多年的工作文件被一键清空……
（2）结合材料，运用法治知识，谈谈该开源智能体可能会侵犯用户的哪些民事权利，并分析如何规避该开源智能体在推广应用过程中的风险。（8分）
```

【设问】 结合材料，运用《逻辑与思维》知识，请你对AI分析的观点进行点评。（6分）

【怎么想到的】 先看两个 AI 结论分别评什么。结论一抓到车企前后说法冲突是对的，但“确定性要求”应改成矛盾律的一致性要求；结论二抓到车企回避系统缺陷、不如实反映客观事实，也符合科学思维追求客观性的要求。

【满分作答示范】 AI 结论一总体成立，但表述要修正：车企先说系统全程正常、事故来自外部突发情况，后又承认系统存在感知延迟和技术问题，二者指向同一事故、同一系统，不能同时为真，违背矛盾律所要求的思维一致性，而不是所谓“确定性要求”。结论二也成立：交警已认定事故主因是系统未及时识别、未有效制动，车企初期回避系统缺陷、把原因推给外部情况，没有如实反映客观对象，不符合科学思维追求认识客观性的要求。

【采分点对照】
- 结论一关于前后说法自相矛盾的判断成立：同一事故、同一系统上既说系统全程正常，又承认系统存在感知延迟和技术问题，两个判断不能同真
- 应表述为违背矛盾律所要求的思维一致性，不能写成违反思维的确定性要求
- 结论二也成立：交警认定系统未及时识别、未有效制动是客观事实，车企初期回避系统缺陷、以外部原因掩盖技术问题，不符合科学思维追求认识客观性的要求

## 考场速查

- **一、充分条件假言推理与判断**：先把条件句写成“P -> Q”，分清前件 P 和后件 Q。 常见坑：后件为真不能推出前件必真。
- **二、必要条件假言推理与判断**：把“只有 P 才 Q”“没有 P 就没有 Q”先翻译成 Q -> P。 常见坑：有了必要条件，不等于结果一定发生。
- **三、三段论、性质判断周延与换质位**：先找大项、小项、中项，再看中项有没有真正把两个前提接起来。 常见坑：同一个词前后换对象，就是四概念错误。
- **四、归纳推理与探求因果联系**：先判断是完全归纳还是不完全归纳，不完全归纳只给或然结论。 常见坑：几个例子反复出现，不等于结论必然成立。
- **五、类比推理**：先找两个对象在哪些方面相同或相似，再看能不能迁移到新的属性。 常见坑：只说“很像”不够，必须写出相似点和迁移点。
- **六、概念、定义、外延关系与划分**：概念题先看内涵是否明确、外延是否清楚。 常见坑：划分标准前后不一，会造成子项混乱。
- **七、选言推理、联言判断与复合判断**：先判断选言是相容还是不相容，再选推理规则。 常见坑：相容选言不能用不相容选言的排除规则。
- **八、真假关系、逻辑规律与关系判断**：先锁定同一对象、同一时间、同一方面，再判断是否违反同一律、矛盾律或排中律。 常见坑：没有同一条件，就不能轻易说自相矛盾。

—  本册完  —

飞哥正志讲堂


