# 选必二框架生成任务计划

## Phase 00：启动与锁规则

- [x] 读取选必二分支 skill 与本地小本本。
- [x] 追加 2026-05-03 框架生成放行要求。
- [x] 创建 `framework_bootstrap_2026-05-03` 运行目录。
- [x] 建立角色账本、批次协议、模型提示词。
- [x] 生成当前预处理快照分析。

## Phase 01：原料层复核

- [x] 从 `LEGAL_QUESTION_INDEX.csv`、`SUBJECTIVE_PREPROCESS.csv`、`CHOICE_PREPROCESS.csv` 生成前三道主观题案例卡。
- [x] 标记前三道主观题的 reference_answer-only 证据边界。
- [ ] 优先复核主观题 37 道；选择题先只处理已锁答案题。
- [ ] 把 `MISSING_OR_UNCERTAIN.md` 中的 uncertain 和未锁答案项目纳入缺口，不冒充闭环。

## Phase 02：框架候选 v0 -> v0.1

- [x] 用 v0 脚手架给前三道主观题归位。
- [x] 统计前三题节点命中、证据强度和典型题。
- [x] 记录前三题归位缺口和开放容器。
- [x] 形成 `FRAMEWORK_V0_1_CANDIDATE_TRIAL3_WEB_OFFICIAL.md`。不得称为 V1。

## Phase 03：Framework Council 自我进化

- [x] Round 0：Codex 生成 evidence pack，含案例卡、频次、归位矩阵、缺口、候选修改。
- [x] Round 0 必须补充命题路径反推：命题目标、载体选择、设问路径、细则奖励动作、制度细节与法治价值平衡。
- [x] Round 1A：真实调用 GPT-5.5 Pro，独立研究主干高频、全面覆盖、节点升级/降级。
- [x] Round 1B：真实调用 Claude Opus 4.7 Adaptive，独立研究学生可学性、迁移表达、抽象风险。
- [x] Round 2A：把 GPT 报告交给 Claude Opus 反驳/吸收。
- [x] Round 2B：把 Claude 报告交给 GPT-5.5 Pro 反驳/吸收。
- [x] Round 3：Codex 写 convergence brief。
- [ ] Round 4：Codex 回本地题源和细则逐条裁决。
- [ ] Round 5：只把证据核验通过的修改升级为新框架版本。

## Phase 04：全量归位与迭代

- [ ] 每批新增/复核题进入归位矩阵。
- [ ] 每批结束后按 `SELF_EVOLUTION_PROTOCOL.md` 更新框架版本与缺口清单。
- [ ] ClaudeCode B 独立复跑，输出冲突和遗漏。
- [ ] Codex 逐项裁决。

## Phase 05：框架定稿与学生版

- [ ] 形成证据锁定版框架。
- [ ] Claude Opus 4.7 进行教学文本成品化。
- [ ] GPT-5.5 Pro 内容压力测试。
- [ ] Governor 检查证据边界和覆盖。
- [ ] Confucius 检查零基础学生能否迁移。
- [ ] 输出 Markdown / Word / PDF / 验收报告。
