你现在是北京高考政治教研整本书项目的 GPT-5.5 Pro 战略指挥官。

硬规则：
1. 你只提供战略指挥建议，不直接决定本地证据真假，不直接命令 Claude Code。
2. Codex 是本地总控、本地证据裁判，同时自己也跑一条生产线。
3. Claude Code 是独立从0重跑线。
4. 所有事实最终以本地源文件、评分细则/参考答案边界、用户框架为准。
5. 不要要求我粘贴账号、密钥、本地绝对路径、大段试题原文或大段评分文本。
6. 本轮是选择性必修一《当代国际政治与经济》主观题评分术语积累，不是普通答案库。
7. 旧终稿可以作质量参照和遗漏风险提示，但不能继承旧结论，不能当证据。

本阶段报告：

【阶段名称】
Phase 01 Workspace And Initial Source Inventory

【阶段目标】
从0重启选必一整本主观题术语积累：读最新技能和本地小本本，保留旧终稿但不继承旧结论，启动 ClaudeCode 独立复跑线，创建控制文件，生成三年原始题源初始索引。

【已完成】
- 已读最新 router / whole-book orchestrator / xuanbiyi branch skill。
- 已读 whole-book SOP、run protocol、cross-model invocation、control-file rules。
- 已读本地选必一交付要求记事本、current-user-requirements、xuanbiyi-term-protocol。
- 用户确认：从0重开；旧终稿保留但不覆盖；三年原始题源为主，镜像/缓存只补查；GPT 用当前已打开对话；ClaudeCode 完整跑，不设预算 cap。
- 新建 run folder 和 numbered control layout。
- 已写 MASTER_REQUIREMENTS、START_CARD、ZERO_START_DECLARATION、NOTEBOOK_DIGEST、USER_FRAMEWORK、USER_QUESTIONS、DECISION_LOG、task_plan、findings、progress。
- ClaudeCode 独立线已启动；第一轮因 CLI 参数问题退出，已修复并重启，目前在读技能和写 lane 文件。
- Codex 自己从三年原始目录生成第一版文件级 SOURCE_LEDGER。

【未完成】
- Codex 自己的套卷级/题级生产还没开始。
- ClaudeCode 尚未闭合任何套卷。
- GPT phase advice 还未保存/消化。
- GPT content review 固定触发项 outline、section_batch、final_markdown、word_pdf 尚未发生，因为还没有学生版内容。

【产物】
- 控制文件：MASTER_REQUIREMENTS、START_CARD、ZERO_START_DECLARATION、NOTEBOOK_DIGEST、USER_FRAMEWORK、USER_QUESTIONS、DECISION_LOG、task_plan、findings、progress。
- ClaudeCode 启动提示和启动脚本。
- 初始 SOURCE_LEDGER / SOURCE_INVENTORY。

【源材料/覆盖情况】
- 已扫描 2024、2025、2026 三个本地原始题源根目录。
- 文件总数：177。
- P0 候选评分/评标/细则文件：98。
- P1 候选参考答案文件：2。
- P2 候选讲评/教学/课件文件：7。
- P3 候选试卷文件：61。
- unknown：9。
- 2024: 66 文件；2025: 61 文件；2026: 50 文件。

【非文本材料处理情况】
- 已识别 PDF、Word、PPT/PPTX、可能含图表文件。
- 尚未进入逐文件渲染/OCR/视觉读取阶段。
- 不允许因单一工具失败跳过 PDF/PPT/图片/表格/扫描。

【P0/P1/P2/P3/P4 证据统计】
P0_candidate_scoring 98；P1_candidate_reference_answer 2；P2_candidate_teaching_or_lecture 7；P3_candidate_paper 61；P4 仅为工作产物，不作证据。

【遗漏题/遗漏套卷/遗漏文件类型】
尚未确定。当前是文件级索引，还未转换为套卷/题号级矩阵。

【Codex 与 Claude Code 差异】
尚无。ClaudeCode 刚启动，正在生成自己的 lane 文件。

【冲突/阻塞】
- 旧终稿质量可能不错，但不能继承为证据。
- Safari 不能用 Apple Events DOM 注入，GPT 交互将用当前 ChatGPT Pro 对话的可见 UI/剪贴板方式。
- GPT 不能作为本地证据 authority。

【Governor 闸门状态】
G0 小本本已读：pass。
G1 从0声明：pass。
G2 源范围记录：pass。
G10 当前 phase report 已准备，等待 GPT 建议与 Codex digestion。
G11 暂不适用，还没有 outline/section_batch/final_markdown/word_pdf。

【本阶段最不确定的 3 件事】
1. 177 个文件中哪些套卷真正含有选必一主观题和 P0/P2/user-confirmed 评分证据。
2. 必须补入样本是否都能在三年主源中找到当前证据，还是需要镜像补查。
3. 旧终稿中哪些表达质量好但必须重新回源取证。

【最可能遗漏的材料类型】
评标 PPT、图片/表格式细则、扫描 PDF 页、缓存文本丢失的 rubric 层级。

【最可能误判的证据等级】
参考答案误标 P0；普通讲评 PPT 误标评分细则；旧生成稿误当证据。

【最可能误导学生的表达】
“材料中”“细则要求”“采分点”“要落到”“参考答案”“评标”、路径/debug/OCR/status 话术。

【禁止进入学生版清单】
本地路径、source id、模型/审计/状态话术、普通参考答案冒充术语、未重新取证的旧终稿文字。

【Codex拟定下一步】
1. Codex 把文件级 SOURCE_LEDGER 转为套卷/题号级矩阵。
2. Codex 自己开始 suite-by-suite 生产线。
3. ClaudeCode 继续独立复跑，Codex 轮询监督。
4. 第一批学生版 outline 出来后马上触发 GPT content review。

请输出一个“下一阶段指挥包”，只要结构化建议：
1. stop/go 判断；
2. 下一阶段第一优先级；
3. Codex 生产线任务；
4. Claude Code 独立重跑线任务；
5. 需要 Claude/GPT 审稿的点；
6. Governor 必查项；
7. Confucius/学生迁移验证点；
8. 最大风险和具体防错动作；
9. Codex 在采纳你建议前必须做的本地检查。
