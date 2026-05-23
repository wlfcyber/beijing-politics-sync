# ORDER 011: 选必一即时补丁令

## 当前状态

状态词：`RUNNING`

依据：

- `03_coverage_diff.md` 显示对照题目行 368。
- 状态统计：`strict_exclude_or_other_module=158`、`evidence_not_located=84`、`already_in_main=57`、`candidate_review=50`、`answer_only_needs_rubric=13`、`needs_manual_key_review=5`、`must_backfill=1`。
- `04_review_queue.md` 显示覆盖缺口候选 81、反合并残留 12、队列总数 93。
- `05_claudecode_opus47/` 已有 ClaudeCode adjudication、patch entries、coverage risk log，但当前严格重建目录未见最终 Word/PDF 交付闭环。

## 禁止声称

不得称“选必一宝典已经完成”。当前只能称“严格重建进行中，覆盖与反合并审查已形成队列”。

## 下一步硬任务

1. 先处理 84 个 `evidence_not_located`：
   - 按海淀、西城、东城、朝阳优先，其次丰台、通州、房山、顺义等。
   - 每题必须回到原卷/评分细则/讲评，定位不到正式细则则降级，不得用参考答案冒充。
2. 再处理 50 个 `candidate_review`：
   - 有细则且命中选必一关键词的，必须判定进入主表、降级参考、还是排除其他模块。
   - 每条判定写明题号、设问、细则位置、框架挂点。
3. 处理 13 个 `answer_only_needs_rubric`：
   - 找不到正式评分细则时只能作为参考，不得进“评分术语”主干。
4. 处理 12 个反合并残留：
   - 同核可以合并，但每个真实题源必须在宝典中保留独立触发点或同类题挂载，不能被一个抽象术语吞掉。
5. 生成下一版学生宝典候选时必须满足哲学宝典同级结构：
   - 框架节点 -> 全部对应真题；
   - 每题有完整设问、材料触发、为什么想到、答案句、易错点、同类题；
   - 不得只列术语，不得只放代表题。
6. 完成候选后再进入 GPT Pro / Claude 真实内容审查、Governor、Confucius、Word/PDF QA。

## 下一次汇报必须给出

- 已关闭的 `evidence_not_located` 数量。
- `candidate_review` 的 INCLUDE / DOWNGRADED / EXCLUDE 数量。
- 仍不能处理的 source-boundary 问题。
- 新学生正文路径和 Word/PDF 路径，如果尚未生成要明确写 pending。

