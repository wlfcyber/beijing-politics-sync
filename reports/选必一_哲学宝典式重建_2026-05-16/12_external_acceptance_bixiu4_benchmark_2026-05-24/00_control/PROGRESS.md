# 进度记录

## 2026-05-24

- 已定位选必一最新版候选稿与 Word 文件。
- 已定位必修四哲学 v8 标杆 Markdown/PDF 和状态报告。
- 已建立本轮外部验收工作区。
- 已复制原始候选稿、清洁候选稿、哲学标杆和哲学状态说明。
- 已完成本地清洁稿预处理：
  - 删除学生稿末尾工程合入指令与单题来源索引。
  - 移除标题中的“严格终稿补入”工程前缀。
  - 补回一处被工程索引隔开的“细则位置/来源”字段。
- 清洁稿完整性预检：
  - 题例：351 条。
  - `【材料触发点】`：351 条。
  - `【设问】`：351 条。
  - `【答案落点】`：351 条。
  - `【细则位置】`：351 条。
  - `【来源】`：351 条。
  - 工程痕迹 `严格终稿补入` / `Codex 合入指令` / `本补丁` / `补丁` / `审计` / `source_path`：0。

## 下一步

1. 生成 GPT Pro 和 Claude 外审提示。
2. 通过真实网页/客户端提交外审材料。
3. 保存完整反馈。
4. 按 must-fix 修订清洁稿并重建 Word/PDF。
5. 复审通过后同步到最终成品目录和 GitHub。

## 2026-05-24 续跑记录

- GPT Pro 网页端已完成一审，结论为 FAIL_MUST_REVISE，已保存原始反馈。
- Claude 网页端 Opus/Adaptive 已尝试提交，但浏览器控制在长页面中卡死；未计入最终通过。
- ClaudeCode 以 `--model opus` 作为生产/审稿 fallback 多轮处理，先后指出并修正学生版中的模板化 `为什么能想到` 问题。
- 已形成学生精简版 v6：
  - `04_revisions/选必一_当代国际政治与经济_主观题术语宝典_学生精简版_v6.md`
- v6 本地预检结果：
  - 题例：351 条。
  - 核心答题点标题：138 个。
  - `【什么时候写】`：351 条。
  - `【设问】`：351 条。
  - `【为什么能想到】`：351 条。
  - `材料信号/设问意图/答题动作`：各 351 条。
  - `【卷面句】`：351 条。
  - 禁用模板词 `骨干句/承接材料事实/写出对应的卷面句/设问追问/设问要求/重心是/理论入口/机制入口/秩序入口/中国入口/联合国入口/审题入口`：0。
  - 后台词 `评分/细则/参考答案/来源：/Claude/GPT/Codex/PASS/FAIL`：0。
- ClaudeCode Opus v6 一审为 FAIL，指出三类 P0：内部措辞、HTML 标记、重复核心标题。
- 已按“不删 351 题例、不合并不同题”的原则修复 P0：
  - 删除 6 处 `strict-final` HTML 标记。
  - 清除 `用户硬规则/钉死/分列/必须保留` 等编辑口吻。
  - 将联合国桶内两个真重复核心标题合并，核心标题由 140 降为 138，351 个题例保留。
  - 对跨桶或近似点增加学生可读功能限定，防止“重复桶”误解。
- ClaudeCode Opus 二审结论：`VERDICT: PASS`，保存于 `03_claude_opus/CLAUDE_CODE_OPUS_V6_REVIEW2_CAPTURE_20260524.md`。
- v6 仍未完成最终外部验收：需要再次提交 GPT Pro 复审和 Claude Opus 4.7 Adaptive 复审，拿到真实 PASS 或继续按意见改。

## 2026-05-24 外审复跑记录

- 已在新的 ChatGPT Pro 网页会话中上传四个附件：
  - `02_gptpro_web/GPTPRO_V6_FINAL_REVIEW_PROMPT.md`
  - `04_revisions/选必一_当代国际政治与经济_主观题术语宝典_学生精简版_v6.md`
  - `01_review_materials/02_bixiu4_philosophy_benchmark_student.md`
  - `04_revisions/V6_LOCAL_QA_REPORT.md`
- GPT Pro 网页端给出 `VERDICT: PASS`，认为 v6 学生精简版达到必修四哲学宝典学生版同等含金量，可以交付；保存于 `02_gptpro_web/GPTPRO_V6_REVIEW_CAPTURE_20260524.md`。
- GPT Pro 提到的剩余项均为不阻碍交付的小风险：5 个孤立题例缺少 `同题组`、部分跨桶同题组较长、`模型/路径/流程` 是题材语境词而非后台词。
- 因 GPT Pro 已经审核 v6 原文，未按小风险改正文，避免改后使 GPT PASS 失效。
- 已尝试 Claude 网页端 Opus/Adaptive：
  - 自动化 Chrome 配置打开后跳转登录页。
  - 默认 Chrome 配置重新打开后也跳转登录页。
  - 未读取账号、Cookie、local storage 或密码。
  - 结论记录为 `BLOCKED_LOGIN`，保存于 `03_claude_opus/CLAUDE_WEB_BLOCKED_LOGIN_20260524.md`。
- 已用 ClaudeCode `--model opus --effort max` 在 GPT Pro PASS 后做备用全稿审查，结论为 `VERDICT: PASS`，保存于 `03_claude_opus/CLAUDE_CODE_OPUS_AFTER_GPT_PASS_FALLBACK_CAPTURE_20260524.md`。
- 当前最终验收状态：`PENDING_CLAUDE_WEB`。不能诚实宣称四线终审完全闭环；需要用户让 Claude 网页端保持登录后，再送同一 v6 给 Claude Opus/Adaptive。
