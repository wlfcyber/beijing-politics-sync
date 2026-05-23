# ORDER 000: 夜间总管接管令

## 对所有正在跑的线程

用户已睡觉。继续工作，不要等用户确认，除非遇到源边界问题：某套卷是否属于本书、某文件是否能作为评分细则、某外部模型真实调用是否无法完成。

每个线程下一次汇报必须回答：

1. 当前状态词是什么：`RUNNING` / `CANDIDATE_DELIVERY_NEEDS_AUDIT` / `BLOCKED_ADVISOR` / `BLOCKED_SOURCE_BOUNDARY` / `DELIVERED_WITH_GOVERNANCE_GAPS` / `STRICT_FINAL_ACCEPTED`。
2. 已覆盖多少题/套，未覆盖多少题/套，未覆盖原因是什么。
3. GPT Pro 与 Claude 真实调用证据在哪里。
4. Governor 与 Confucius 是否基于最终学生成品而不是工作日志运行。
5. Word/PDF 是否已渲染检查，检查报告在哪里。
6. 下一步具体写哪个文件、修哪个缺口、关闭哪个风险。

## 对选必一

不要停在“术语汇总”或“重建稿可读”。目标是哲学宝典同级：框架优先、每个框架节点挂真实题、每题有材料触发、为什么想到、答案句、易错点、同类题。覆盖全部考题，不得只放代表题。

## 对必修四

以已认可哲学宝典为母版，只补先前没有的题和确有缺口的题，不重建、不改框架、不把旧已认可内容洗掉。重点核 `remaining_old_choice_presence_gaps_after_v7.csv`、新增 9 套、old subjective quality failed 是否已处理。

## 对选必二

继续 GPT Pro + Claude 框架互动，不把 v13_10 候选交付自动当终局。必须验证双轴框架、42题重标、开放容器、治理附录、traceability、Governor、Confucius 和 Word/PDF 是否相互一致。标准是聪明高三学生能直接上手并尽量全对。

