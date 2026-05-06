# 外部提交清单

time: 2026-05-04 11:05 CST
status: claude_captured_patched__gpt_blocked_wrong_thread

## 作废说明

2026-05-04 09:50 左右的网页尝试因误投/焦点混乱/误点语音按钮作废，不计入 GPT/Claude 有效证据。

2026-05-04 10:05-10:14 的二次尝试也未形成有效提交：Safari 可导航到选必一 ChatGPT 记录 URL 并短暂显示 `XBY1-RG-*` 行，但上传/输入焦点随后漂移到无关 ChatGPT 线程；ChatGPT 桌面 App 被 Computer Use 安全策略禁止控制；Claude 桌面端打开记录 URL 后仍显示选必二对话。上述均不计入有效外审。

2026-05-04 10:50-10:52 继续尝试：Claude 桌面端侧边栏成功切回 `学生文档审稿意见`，URL 为 `claude.ai/chat/97d32a69-e05b-4b69-a5f9-3c3a0cf09ce6`，正文可见选必一全书最终回归审稿记录和 `Opus 4.7 Adaptive` 模型标识。附件上传按钮曾导致窗口漂移回选必二线程，因此停止附件上传；随后在正确 Claude 选必一对话中发送补跑版深度教学成品化复核 prompt，要求若上下文不足则回复 `NEED_ARTIFACT_UPLOAD`。该 Claude 补跑已提交，等待响应捕获。

2026-05-04 10:56 左右的 GPT-5.5 Pro 再尝试作废：Safari 曾短暂回到记录中的选必一 ChatGPT URL `69f7099a...`，但输入/发送过程中再次漂移到选必二/法律线程 `69f7793c...`。已点击停止生成。该 GPT 尝试不计入本任务证据，也不得作为 PASS。

2026-05-04 10:52-11:05 Claude Opus 4.7 Adaptive 有效闭合：Claude 在同一个 `学生文档审稿意见` 对话中回复“我具备做这轮复核所需的上下文,不需要再上传文件”，给出 `PASS_AFTER_FIX` 和 D-01 至 D-10。回复已保存为 `claude_opus_deep_teaching_response_20260504.md`，并已进入本地裁决与返修。

2026-05-04 11:07：`artifact_for_external_review_选必一学生讲义_20260504.md` 已刷新为 Claude 返修后的最新 Markdown，供未来 GPT 手动/稳定窗口补跑使用。

## GPT-5.5 Pro 提交前检查

- [ ] 当前通道不是已暂停的 Safari 漂移状态；如使用 Safari，必须由用户先确认窗口稳定停在选必一旧对话。
- [ ] 用户确认当前窗口是正确的同一个 ChatGPT Pro 对话，不是 Codex 另一个线程，不是选必二/法律线程。
- [ ] 输入框为空，没有残留文字。
- [ ] 没有语音/麦克风模式；不点击语音按钮。
- [ ] 上传附件：`artifact_for_external_review_选必一学生讲义_20260504.md`。
- [ ] 粘贴 prompt：`gpt55_deep_external_review_prompt_20260504.md`。
- [ ] 发送后截图或保存可见回复。
- [ ] 回复保存到本目录，文件名：`gpt55_deep_external_review_response_20260504.md`。

2026-05-04 11:18-11:28 补充尝试：Codex 在 Safari 中切回 `Opus4.6 vs 4.7`，确认 URL 为 `https://chatgpt.com/c/69f7099a-36e0-839a-b579-db4d592f1848`，并提交带唯一标记 `XBY1-GPT-DEEP-FINAL-20260504-1118` 的补跑 prompt。提交后页面显示 GPT/Pro 正在思考。随后 Safari 被另一 Codex 线程/另一个 ChatGPT 会话争用，多次回到法律线程或其他会话；用户确认两个线程容易冲突，要求等待另一个线程的 GPT 思考/空窗期使用，避免互相干扰。因此本次只记录为“正确线程已提交但回复捕获被跨线程冲突中断”，不得计为 PASS。

当前状态：submitted_correct_thread__capture_blocked_by_cross_thread_safari_conflict。Safari 不再主动操作，直到另一个线程处于 GPT 思考/空窗期或用户确认窗口可用；补跑 GPT 深度审稿尚无有效回复；不能把任何 GPT 深度补跑计为 PASS。

## Claude Opus 4.7 Adaptive 提交前检查

- [x] 当前 Claude 窗口已确认切到选必一记录对话；不能使用仍显示选必二《法律与生活》的窗口。
- [x] 当前窗口是正确的同一个 Claude Opus 4.7 Adaptive 对话，不是其他 Claude/项目线程。
- [x] 输入框为空，没有残留文字。
- [ ] 上传附件：`artifact_for_external_review_选必一学生讲义_20260504.md`。注：附件按钮会造成线程漂移，已暂停附件上传。
- [x] 粘贴 prompt：补跑版深度教学成品化复核 prompt，沿用同一 Claude 对话上下文。
- [x] 发送后截图或保存可见回复。
- [x] 回复保存到本目录，文件名：`claude_opus_deep_teaching_response_20260504.md`。

## 回流本地后的必做

- [x] 把 Claude issue 合并进 `local_decision_and_patch_log_20260504.md`。
- [x] 每条 substantive issue 标注本地裁决：accept / partial / reject / defer。
- [x] 接受的正文修改先改 Markdown，再重新生成 DOCX/PDF。
- [x] 重跑 Governor。
- [x] 重跑 Confucius artifact-only。
- [x] 更新 `FINAL_ACCEPTANCE_REPORT.md` 和 `reports/督工验收状态.md`。
- [ ] GPT 深度补跑有效回复捕获。当前 blocked，不得伪造。
