# 模型建议消化日志

本文件记录 GPT-5.5 Pro、Claude Opus 4.7 Adaptive、ClaudeCode 或 Codex 子智能体给出的建议。任何建议必须经 Codex 本地证据检查后才能影响框架或学生文档。

| advice_id | source_model_or_role | phase | suggestion_summary | decision | local_evidence_to_check | affects_framework | affects_student_doc | status |
|---|---|---|---|---|---|---|---|---|
| B01-GPT55-IND-001 | GPT-5.5 via OpenAI Codex CLI, not ChatGPT web | Batch01 independent blueprint | 五域降为归位容器，主干应转为定关系、找争点、对规则/要件、落结果；价值必须锚定法律关系 | partially_accepted_but_web_visible_gate_pending_if_required | 需更多 formal 主观题跨题域验证；B01-Q2 只能 reference_only | yes | yes | incorporated_as_cli_advice_only |
| B01-CLAUDE-IND-001 | Claude Opus via Claude CLI, not web Adaptive Thinking visible | Batch01 independent blueprint | 学生版应压缩为看题三段、答题四步、价值一规；V0 节点过密，不可直接教学 | partially_accepted_but_adaptive_thinking_gate_pending | 需验证选择题、小题、纯程序题、纯意义题 | yes | yes | incorporated_as_cli_advice_only |
| B01-GPT55-XCR-001 | GPT-5.5 via OpenAI Codex CLI, not ChatGPT web | Cross-critique of Claude | 同意动作链优先，但三问应保留为教师后台验收；开放容器需分级 | accepted_with_modification_but_web_visible_gate_pending_if_required | 检查五域覆盖矩阵是否失衡；检查程序/效力/比较题 | yes | no | incorporated_as_cli_advice_only |
| B01-GPT-CALL-CLARIFY-001 | Codex correction | Call provenance | GPT 输出来自 `codex exec -m gpt-5.5` 的非交互 CLI 会话，不会出现在 ChatGPT 网页版历史 | accepted | 若用户要求网页版可见 GPT-5.5 Pro，则重跑并替换/补充日志 | yes | no | active_correction |
| B01-CLAUDE-XCR-001 | Claude Opus via Claude CLI, not web Adaptive Thinking visible | Cross-critique of GPT | 反对单轴动作链替代五域；要求去法考化措辞，价值作条件触发 | accepted_with_modification_but_adaptive_thinking_gate_pending | 检查北京卷是否存在仅靠题域归位、动作链失灵的题 | yes | yes | incorporated_as_cli_advice_only |
| B01-SESSION-ISO-001 | User boundary | Session isolation | GPT、Claude、ClaudeCode 正在跑其他项目，本轮必须新开独立对话/会话/工作目录 | accepted | 后续每次真实调用均检查输出目录和 prompt 首部 | yes | no | active_rule |
| B01-CLAUDE-CALL-CLARIFY-001 | Codex correction | Call provenance | Claude 输出来自 `claude -p --model opus` 的非交互 CLI 会话，不会出现在 Claude 网页版 Adaptive Thinking 对话历史 | accepted | 若用户要求 Claude Opus 4.7 Adaptive Thinking 网页端，则重跑并替换/补充日志 | yes | no | active_correction |
| B01-WEB-GATE-001 | User correction | Official model gate | 正式 gate 必须使用 user-visible GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive Thinking 模式 | accepted | 已完成网页/桌面端可见会话并归档原文输出 | yes | yes | completed_for_batch01_trial3 |
| B01-COPY-TARGET-ERR-001 | Codex correction | Clipboard/window hygiene | `Web Claude Cross-Critique Prompt` 是应发送给 Claude 的 prompt；曾在复制/校验过程中被误抓到 Codex/本地剪贴板视野，不能作为模型报告或 Codex 输出 | excluded | 已核验正式归档文件头：Claude cross-critique 与 GPT cross-critique 均为模型最终回复；advisor_reports/fusion 中无该 prompt 作为报告残留 | no | no | corrected_excluded |
| B01-GPT55-WEB-IND-001 | GPT-5.5 Pro web-visible ChatGPT | Batch01 independent framework council | 支持 V0.1 证据分层候选；主干为定关系、抓争点、对规则、落结果、价值锚定；五域降为索引；B01-Q2 只进开放容器 | accepted_with_revision | 当前 formal 只有 2 道，所有主干只能 B 候选 / A 待验证；价值不作每题必做第五步 | yes | yes | incorporated_in_web_official_fusion |
| B01-CLAUDE-WEB-IND-001 | Claude Opus 4.7 Adaptive visible app/web | Batch01 independent framework council | 学生端压缩为四步 + 价值一规 + 五域索引；命题路径留教师后台；reference_answer 不推动主干 | accepted_with_revision | 需回原始评分细则核验 B01-Q1 从属性和 B01-Q3 价值层级；纯程序/比较/选择题待样本 | yes | yes | incorporated_in_web_official_fusion |
| B01-GPT55-WEB-XCR-001 | GPT-5.5 Pro web-visible ChatGPT | Cross-critique of Claude | 同意教师/学生分离和四步暂定主干；要求保留零步问法、保留条件/程序要求和开放容器，防止过度压缩漏题 | accepted_with_revision | 题型触发分支须等待 formal_or_scoring_source 样本；五域类型库暂缓 | yes | yes | incorporated_in_web_official_fusion |
| B01-CLAUDE-WEB-XCR-001 | Claude Opus 4.7 Adaptive visible app/web | Cross-critique of GPT | 同意证据闸门和五域索引；反对价值并列第五步、学生六步线性、当前标 A、B01-Q2 优先追踪 | accepted | 所有当前节点最高 B 候选；A 级升格需后续 batch | yes | yes | incorporated_in_web_official_fusion |
| B01-EVIDENCE-CORR-002 | Codex local evidence correction | Batch01 evidence level | B01-Q2 `2024海淀一模第19题` 本地存在细则层次表，预处理表 reference_answer 标记错误 | accepted | 已复核 `2024海淀一模/细则/细则.docx` 抽取文本；支持知识产权/不正当竞争索引，不能单题推新技术高频主干 | yes | yes | corrected_after_user_review |
