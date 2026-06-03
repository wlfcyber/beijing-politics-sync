# DECISION_LOG — ClaudeCode 生产线 C

继承 B 线 D-001 ~ D-009 的全部决策（不在此重复，参见 B 线 DECISION_LOG.md）。本日志只记录 C 线新增决策。

## D-C-001  2026-05-05  C 线独立目录

- **决策**：新建 `claudecode_lane_C_full_rerun_2026-05-05/`，与 B 线、Codex 各线均隔离。
- **原因**：用户 5-5 当面要求"重跑"，且要求做愤怒高三生审阅；为避免污染 B 线已有 PASS 状态、保留对照可能性，分目录跑。
- **后果**：C 线交付独立产出，PASS 后允许做 B↔C 对照报告。

## D-C-002  2026-05-05  复用 B 线 OCR 解析文本，不复用 B 线结论

- **决策**：通过 symlink 接入 B 线 `source_inventory/extracted/`（178 份 .txt）和 `00_control/SOURCE_LEDGER_v2.csv` 作为**定位线索**；其余 B 线产物（QUESTION_PACK / hand_crafted / 框架版.md / 情境版.md / GOVERNOR / CONFUCIUS）一律不读不引用。
- **原因**：OCR 是机械活，重做无 ROI；但结论必须 C 线独立达成才算真正"重跑+进化"。
- **后果**：源文本不重做；其余全部独立 rebuild。SOURCE_LEDGER_v2 的等级判断也需 C 线在使用前抽查复核。

## D-C-003  2026-05-05  外部模型 gate 继续豁免

- **决策**：本轮**不**调用 web 端 GPT-5.5 Pro / Claude Opus 4.7 Adaptive，继承 B 线 D-002。codex CLI 仅作 cli_provisional_advice，不计入 web gate。
- **原因**：用户离场，要求 ClaudeCode 自己跑完。
- **后果**：C 线 FINAL_ACCEPTANCE_REPORT 必须显式声明"无 web 端真实调用"。

## D-C-004  2026-05-05  Confucius 角色升级为"愤怒的聪明但一无所知的高三生"

- **决策**：C 线 Confucius 评级标准比 B 线（PASS_LEARNABLE_v2）严格一档：必须显式抓出至少 9 处具体瑕疵（3 类各 3 处），不能 PASS 才返回修改。
- **原因**：用户 5-5 明确指定愤怒高三生角色，目的就是让审阅更刻薄。
- **后果**：Confucius 报告必须包含具体段落引用，不得只给抽象评语。Governor + Confucius 评级如果有冲突，以 Confucius 优先返工。

## D-C-005  2026-05-05  允许使用 codex CLI 做交叉质询

- **决策**：在框架进化阶段，允许通过 `codex exec` 让 Codex CLI 提供 cli_provisional_advice 作为本地交叉质询；输出文件落 `framework_evolution/codex_cli_provisional/`，仅作思路对冲，不进入证据链。
- **原因**：用户授权"问 codex"。
- **后果**：cli_provisional_advice 不能作为框架定稿依据，但可作为发现盲点的工具。
