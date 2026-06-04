# Claude Opus 4.8 Skill Gate Review

- channel: cli_or_api_real_call
- tool: claude CLI
- model_usage_reported: claude-opus-4-8
- status: succeeded
- session_id: b000505b-f070-4bbc-82bb-897bed9a14e9

```markdown
## verdict

**CONDITIONAL_PASS** — 本轮增量方向正确且诚实（仍如实报告 `final_user_goal_ready=no` 与浏览器闸口 not ready），防伪与平台隔离等护栏是真实进步。但"源访问真实性"尚未被证明、Claude 评审通道未验活、浏览器闸口存在"可读 = 可访问"的语义混淆。这些必须在下一轮关闭后，才能信任该技能去自主驱动完稿。

## strongest_parts

- **防伪清单**（禁止伪造文献/页码/引文/问卷/访谈/CNKI 记录/导师意见）直击研究生论文最大造假面。
- **Windows 证据在 Mac 上一律作废、Mac 必须重验** → 杜绝跨平台证据串用。
- **`chrome_cdp_probe` 仅取 tab 标题/URL**，不读 cookie/本地存储/表单/正文/凭据 → 最小权限，尊重登录、CAPTCHA、SSO 与机构规则。
- **`run_audit` / `workflow_gate_matrix` 要求每条 lane 各自的外审证据**，而非一行汇总 → 难以用单点谎言蒙混过关。
- **`final_user_goal_ready=yes` 作为唯一终态信号** → 单一可信收口，便于审计。

## remaining_workflow_gaps

1. 浏览器闸口只能证明"URL 是 RUC/CNKI"，**无法证明"已认证 + 拿到全文/导出"**。当前"Chrome path readable"实为"CDP 链路可读"，不等于"源可访问"，二者被混为一谈。
2. 因探针不读正文，**源内容从何而来、如何与防伪规则绑定没有机制**：缺一个把每条引用钉到真实检索事件的"来源溯源台账"。
3. 双评审中只证明了 **GPT-5.5 Pro 在线；Claude Opus 4.8 Max 通道是否在 Mac 验活无证据**。规则要求"两者都通过"，但一条 lane 未证 → 自主完稿在结构上不可能。
4. **缺"真实通过"判据**：没有评审 rubric（逐条核对引用、章节完整性、方法论、语言层级、可机读 verdict + 列明异议），存在橡皮图章风险。
5. **缺顺序依赖**：选题应在"源访问就绪"之后、由真实可检索源支撑；否则先定题再回填易诱发造假。
6. **缺修订台账**（异议→改动→复评）与无进展检测，"迭代直到通过"可能陷入表面微调或死循环。
7. **证据新鲜度/会话绑定未定义**：旧 run 已 `no`（诚实），但需时间戳 + run-id，防止陈旧 ready 被复用。

## must_add_to_skill_or_scripts

- **浏览器闸口分三级并各留证据**：(a) CDP 链路可读；(b) 当前为授权 RUC/CNKI URL；(c) 已认证全文/导出能力。(c) 用隐私友好证明（用户确认成功打开全文 + 导出文件落到已知路径并记 hash），不读正文。
- **新增 `source_provenance_ledger`**：每条源记 `{题名/作者/CNKI或RUC标识/检索URL/时间戳/获取方式/本地文件路径+hash}`；`run_audit` 对论文中任一引用无台账条目即判 fail。
- **新增 `claude_review_readiness` 验活探针**，与 pro-cli 对称，并纳入 gate matrix。
- **评审 schema**：两位评审都须做引用抽查（对台账）、完整性/方法/语言层级检查，输出可机读 verdict + 枚举异议；零未决异议方可 pass。
- **加门禁依赖**：选题 gate 依赖源访问 gate；初稿 gate 依赖最小 N 条台账源；评审 gate 依赖初稿完整性。
- **所有 gate 证据打 run-id + 时间戳**；`run_audit` 拒收跨机或非本 run 证据。

## risk_of_false_completion

- **最大风险**：把"CDP 可读 + URL 命中 RUC/CNKI"误判为"源访问就绪"。当前 `readable` 措辞正是这一漏洞的语言入口。
- 探针不读正文 → 源内容可能从模型自述或人工粘贴混入；**若无溯源台账，造假从后门重新进入**，防伪规则形同口号。
- **Claude lane 未验活** → 可能在该通道缺失/被 mock 时仍声称"双评通过"。
- 若 `final_user_goal_ready` 的计算未强制"所有上游 gate 同时为新鲜绿"，聚合信号可被局部置位伪造。

## recommended_next_step

**先修浏览器闸口语义**：把"CDP 链路可读 / RUC·CNKI URL 命中 / 已认证全文导出"三态彻底分离，并要求 (c) 一份具体的检索取证产物（导出文件 + hash + 时间戳），让"可读"永远无法被当作"可访问"。此步同时解锁真实取源、堵住当前最大的假完成口，并为紧随其后的 `source_provenance_ledger`（由 `run_audit` 强制校验）打下地基——整条"真实源 → 源支撑初稿 → 真实双评"链条都依赖它。
```
