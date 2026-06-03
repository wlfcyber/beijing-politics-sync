# ClaudeCode Prompt For Claude Zero Run

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Code 独立执行者。

本轮不是修旧稿，不是润色 v8/v9/v10/v11/v12，也不是做 GPT/Claude 会议纪要。你要从 0 重新跑一遍：以题源、设问、材料、答案、评分细则、评标、讲评明确给分口径为唯一养料，独立生成一份“前面框架穷尽，后面全题穷尽”的飞哥课堂版框架。

【最高目标】
产出一份真正像用户旧框架的《选必二法律主观题穷尽框架与全题宝典》：
1. 前面：穷尽框架。
2. 后面：所有已锁源法律主观题逐题题链。
3. 学生能背，老师能讲，考场能启动。
4. 短句、箭头、正向触发、反向筛查、飞哥想说。
5. 不像工程报告，不像 AI 教学法，不像法考，不像必修三。

【输入】
优先自动查找：
/Users/wanglifei/Desktop/北京高考政治/
/Users/wanglifei/Desktop/北京高考政治/2024各区模拟题
/Users/wanglifei/Desktop/北京高考政治/2025各区模拟题
/Users/wanglifei/Desktop/北京高考政治/2026各区一模
/Users/wanglifei/Desktop/北京高考政治/2026各区期末和期中

若当前工作区有这些文件，也一并使用：
2025各区模拟题.zip
2026各区一模.zip
2026各区期末和期中.zip
哲学与文化  2026班课.pdf
经济与社会-应如何类考题-主体积累页_极简版(1).pdf

旧框架文件只用于学习风格，不作为选必二证据来源。
先前 v8/v9/v10/v11/v12 输出如果存在，只能作为反面检查和对照，不得直接继承题链、分类或结论。

【硬规则】
1. 只研究主观题，选择题全部忽略。
2. 不得扩大到旧 65/70 口径。
3. 不得纳入 pending 三题，除非本轮重新找到原题、设问、材料和正式给分口径。
4. OPEN_OR_REFERENCE 只能放参考容器，不能支撑核心框架。
5. 不得先想框架再找题证明。
6. 不得按教材目录搭框架。
7. 不得使用“金样板题”“10 道极简演练”作为产品结构。
8. 不得写 DOCX/PDF/TASK_COMPLETE/FINAL_PASS。
9. 学生正文不得出现 corpus、atom、evidence、rubric、PASS、reference_only、评分细则、参考答案、page、slide、R_、M_。
10. 不得把参考答案、讲评分析、设问要素、评分说明当材料。
11. 宁可降级/待补，也不许硬写假题链。
12. 每道题必须 source lock：真实设问、真实材料核心、真实答案/细则口径。

【风格学习】
先读取用户旧框架，提取风格 DNA：
1. 先导：这类题到底在考什么。
2. 正向触发：看到什么 → 写什么。
3. 反向筛查：A ≠ B，哪些方向不能写。
4. 高频答题语言：可背、可换材料、可上考场。
5. 飞哥想说：有裁断感，告诉学生哪个更通用、哪个别乱写。
输出：
claude_zero_run/00_飞哥旧框架风格DNA.md

【执行步骤】

STEP 1：全量盘点文件
自动解压 zip，抽取 PDF/Word/PPT/图片文本。扫描件、无文本层 PDF 要 OCR 或记录失败。
输出：
claude_zero_run/01_source_manifest.csv
claude_zero_run/01_processing_log.md
claude_zero_run/01_failed_files.csv

STEP 2：抽取选必二法律主观题候选
只收主观题。
每题字段：
question_id
年份区阶段题号
原题文件和页码
真实设问
真实材料
答案/细则/评标/讲评给分口径
evidence_level：formal / lecture_explicit_scoring / reference_only / missing
为什么是选必二法律主观题
为什么可能不是
模块边界风险
输出：
claude_zero_run/02_candidate_subjective_law_questions.csv
claude_zero_run/02_uncertain_or_boundary_cases.md

STEP 3：逐题 source lock
每题生成一张卡：
题源：
原始文件：
页码/题号：
真实设问：
真实材料核心：
对应答案/细则：
正式证据等级：
是否进入核心题链：
若不进入，原因：
输出：
claude_zero_run/source_lock_cards/{question_id}.md
claude_zero_run/03_source_lock_index.csv

STEP 4：证据清理
把题分成三类：
A 核心题：有真实设问、真实材料、正式或明确给分口径。
B 参考题：证据弱、OPEN_OR_REFERENCE、讲评参考、设问或材料不完整。
C 待补/剔除：无法锁源、疑似必修三/经济/逻辑、缺正式证据。
输出：
claude_zero_run/04_corpus_status_report.md
claude_zero_run/04_core_questions.csv
claude_zero_run/04_reference_questions.csv
claude_zero_run/04_pending_or_excluded.csv

STEP 5：从题源生长框架，不许先写正文
先生成“框架穷尽清单”，但必须是强分诊，不是万能篮子。
每个框架点必须有：
看到什么
触发什么
怎么写
别写什么
支撑题号
证据等级
是否核心
是否参考
输出：
claude_zero_run/05_framework_exhaustion_map.csv
claude_zero_run/05_framework_exhaustion_map.md

必须覆盖：
一、设问入口
- 问理由/诉求/判决结果
- 问裁判理由/补表
- 问评析
- 问意义/价值
- 问调解/维权/路径

二、材料触发
- 合同成立/履约/违约
- 平台用工/三从属性
- 消费者欺诈/知情权/惩罚性赔偿
- 人格权/隐私/名誉/个人信息
- 知识产权/不正当竞争
- 多主体过错/未成年人/公平分责
- 好意同乘/侵权减责
- 相邻关系/物权边界/绿色原则
- 竞业限制/商业秘密/劳动权利
- 纠纷解决/调解/仲裁/诉讼/举证
- 家庭继承/赡养监护，如核心题有支撑
- 法律制度意义/规则保护谁规范谁

三、反向筛查
- 法院 ≠ 公正司法
- 法治 ≠ 全面依法治国
- 企业 ≠ 经济生活
- 平台 ≠ 劳动关系，除非有三从属性事实
- 消费者 ≠ 三倍赔偿，除非有欺诈
- 创新 ≠ 只写保护创新
- 意义 ≠ 裸价值
- 多主体 ≠ 一锅炖
- 案例 ≠ 法考

STEP 6：写上篇穷尽框架
输出：
claude_zero_run/06_上篇_选必二法律主观题穷尽框架_飞哥版.md

结构：
# 上篇：选必二法律主观题穷尽框架

1. 先导：这类题到底考什么
写清：不是背法条，不是法考，不是必修三，是把生活纠纷翻译成法律得分点。

2. 总法门
定题型 → 翻材料 → 写法律 → 收价值
每步都写：
看到什么：
要干什么：
别写什么：
飞哥想说：

3. 设问分诊穷尽
每类格式：
看到：
第一步：
答案骨架：
反向筛：
来源题：
飞哥想说：

4. 材料触发穷尽
每类格式：
看到：
翻成法律话：
高频句：
别写：
来源题：
飞哥想说：

5. 反向筛查穷尽
必须写成 A≠B。

6. 高频得分语言
分块：
诉求支持类
裁判理由类
评析行为类
合同类
劳动类
消费者类
人格权类
知识产权/不正当竞争类
纠纷解决类
意义价值类
每块：
最推荐背：
什么时候用：
什么时候别用：
飞哥想说：

7. 最短记忆版
最多 15 行。

STEP 7：写下篇全题题链
输出：
claude_zero_run/07_下篇_全题题链_飞哥版.md
claude_zero_run/07_下篇_全题题链_飞哥版.csv

只写核心锁源题。参考题、待补题单列，不得混入正文。
每题最多半页，格式：
题源：
证据等级：
设问入口：
命中框架：
材料触发：
1. 材料信息 → 法律翻译 → 细则喜欢的话
2. 材料信息 → 法律翻译 → 细则喜欢的话
3. 材料信息 → 法律翻译 → 细则喜欢的话
答案骨架：
1.
2.
3.
反向筛：
飞哥想说：

硬要求：
- 每题必须有真实设问。
- 每题必须有真实材料核心。
- 每题必须有材料事实 → 法律翻译 → 细则喜欢的话。
- 每题必须能看出如何用上篇框架。
- 不能粘贴评分细则或参考答案。
- 不能出现待回源占位。

STEP 8：开放容器与待补题
输出：
claude_zero_run/08_开放容器与待补题.md
分两块：
A. OPEN_OR_REFERENCE：仅参考，不支撑核心。
B. 缺源/边界题：列需要什么原始文件，不写题链。

STEP 9：覆盖矩阵
输出：
claude_zero_run/09_框架_题目_覆盖矩阵.csv
要求：
1. 核心矩阵只统计核心锁源题。
2. OPEN_OR_REFERENCE 单列。
3. 缺源题单列。
4. 不许再出现 v10 那种虚高统计。
5. 每个核心框架点必须有正式题支撑。

STEP 10：QA 验收
输出：
claude_zero_run/10_QA_acceptance.md

只能写：
CLAUDE_ZERO_CONDITIONAL_PASS
或 FAIL

逐项检查：
1. 是否从 0 跑完题源。
2. 是否只研究主观题。
3. 是否 source lock 每道题。
4. 是否前面框架穷尽。
5. 是否后面全核心题穷尽。
6. 是否参考题和待补题单列。
7. 是否没有工程语言进入学生正文。
8. 是否没有参考答案/评分说明混入材料。
9. 是否没有万能合同、万能程序、万能意义。
10. 是否像飞哥课堂框架。
11. 是否不法考化、不必修三化、不经济化。
12. 是否不写 FINAL_PASS/TASK_COMPLETE/DOCX/PDF。

【最终提醒】
你不是来证明自己跑了流程。
你是来生成一份能上课的框架。

旧版本最大问题：
- 有证据，但不像课。
- 有题链，但像工程。
- 有框架，但学生不会背。

这次必须做到：
- 框架前面穷尽。
- 题目后面穷尽。
- 每个触发点都能回到题。
- 每道题都能回到框架。
- 全文像飞哥课堂板书，不像 AI 报告。

现在开始执行。

## Supervisor Addendum

Before content work, pass the project three-layer SOP. Read the control files in `claude_zero_run/`, the master governor files, the xuanbier skill, and the hard-rule notebook. Save all generated artifacts under `claude_zero_run/`. If you use ClaudeCode CLI rather than VS Code ClaudeCode, write that status honestly as `ClaudeCode CLI/provisional` in the run evidence.

