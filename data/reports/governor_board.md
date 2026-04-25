# Governor Board

## 2026-04-25 北京高三政治模拟卷材料升级
- trigger: 用户指出旧版材料“过于简单无聊”，要求学习区级模拟题材料写法。
- organizer: pass. 已抽样学习 2025 海淀一模、2025 西城二模、2026 西城一模、2026 朝阳一模等可读样卷，重点复盘材料的场景、主体、机制、矛盾和任务化写法。
- mapper: pass. 形成材料写法学习笔记，并重写 A/B/C 三套卷为材料升级版；旧“筛题版”保留但不作为主推荐版本。
- validation: pass. 三套升级版均为 15 道选择题 + 6 道主观题，并附答案与评分参考。
- deliverables:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_区卷材料写法学习笔记_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_A卷_材料升级版_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_B卷_材料升级版_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_C卷_材料升级版_2026-04-25.md`
- remaining boundaries:
  - 本轮重点解决材料厚度和区卷感，尚未做最终 Word 排版。
  - 后续整合成正式卷时，还需统一风格、答案细则颗粒度和选择题难度曲线。

## 2026-04-25 北京高三政治模拟卷三套筛题版
- organizer: pass. 已在既有蓝图基础上生成 A/B/C 三套筛题版，每套均为 100 分、90 分钟、15 道选择题 + 6 道主观题。
- mapper: pass. 三套卷均保持主观题六本书结构：必修二、必修三、必修四、选必一、选必二、选必三各一题；必修一只进入选择题。
- source-policy: pass with boundary. 每套卷均附题源链接，来源包含新华社、央视网、最高人民法院、商务部、国家知识产权局、北京市政府网等。
- rubric-policy: pass. 每套卷附选择题答案和主观题评分要点，供后续筛选与整合。
- deliverables:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_A卷_筛题版_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_B卷_筛题版_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_C卷_筛题版_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_三套卷选题对照表_2026-04-25.csv`
- validation:
  - 选题对照表 63 行：A/B/C 各 15 道选择题、6 道主观题。
  - 三套卷均包含答案、评分参考、题源链接。
- remaining boundaries:
  - 当前为筛题版，不是最终排印版。
  - 后续应由用户挑选各板块最佳题后，再做整卷统一风格、难度曲线和版式复核。

## 2026-04-25 北京高三政治模拟卷命题蓝图
- organizer: pass. 已盘点一模/二模缓存条目并将样本池从海淀、西城扩展为全区学习；重点顺序固定为海淀、西城、东城、朝阳、丰台、其他区。
- mapper: pass. 产出 21 题位矩阵，主观题按六本书分配：必修二、必修三、必修四、选必一、选必二、选必三各 1 道；必修一只进入选择题。
- source-policy: pass with boundary. 每题必须绑定最新时政热点与可追溯来源链接；来源优先级为官方发布、官方媒体、大型民间媒体。
- rubric-policy: pass. 新增细则可信度规则：海淀权重最高，西城校准；重复出现在海淀/西城或重点区之间的细则口径可信度上升；普通参考答案不得自动升级为评分细则。
- deliverables:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_命题蓝图_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_题型分值模块矩阵_2026-04-25.csv`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_热点材料来源库_2026-04-25.csv`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_评分细则模板_2026-04-25.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\北京高三政治模拟卷_样卷细则可信度规则_2026-04-25.csv`
- remaining boundaries:
  - 当前仍为蓝图阶段，未生成完整学生卷。
  - 2026 海淀/西城扫描版试卷仍需 OCR 后用于版式精修。
  - 2026 二模资料未进入当前本地样本，后续补入后需修订蓝图。

## 2026-04-25 选必二《法律与生活》深度改稿

- organizer: pass. Corpus cache refreshed; deep revision run created at `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必二法律与生活深度改稿_2026-04-25_1601`.
- mapper: pass with explicit boundary. Coverage matrix upgraded from a simple backfill list into a source-governed matrix with `source_id`, question/subquestion, file path, source type, rubric level, verification status, risk notes, and training value.
- patcher: pass. Main framework replaced with route-first structure: `设问任务 -> 主体关系 -> 权利客体 -> 法律关系 -> 关键事实/证据 -> 法律规则 -> 责任/救济 -> 价值意义`.
- patcher follow-up: pass. Added `30秒总分流图`, macro `教材四域/训练八节点`, node-level `必答点/可加点/禁写点`, one-material-multiple-law trimming rule, and source-risk list.
- governor: pass for current framework revision. `2026海淀一模` corrected to `18(3)`; `2025海淀二模18` split into entity IP and procedure/evidence entries; answer-pending and teacher-version items are not promoted to scoring rubrics.
- deliverables:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必二法律与生活_新版教学框架.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必二法律与生活_三年题源覆盖矩阵.csv`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必二法律与生活_三年题目细则回填框架.md`
- remaining boundaries:
  - `2026顺义一模18` remains answer/rubric pending.
  - `2025西城二模10` remains teacher-version choice material, not a scoring source.
  - Family inheritance and labor/social-security formal scoring coverage still need future source supplementation.

## Current Status

- organizer: pass. Latest skill workspace refresh was run with explicit 2024/2025/2026 source roots; `exam_suite_inventory.csv` has 134 suite views and `cleanup_candidates.csv` has 4 review-only candidates.
- mapper: needs-merge but current stage merged. Active selected-compulsory-one run reused 173 ledgered local files, 152 searchable text items, and 22 included main-question rows.
- patcher: needs-merge/blocker noted. Exact question anchors and one-material-many-point placements were repaired in the new artifact and coverage matrix.
- summarizer: pass for current artifacts:
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必一材料-触发-答题点总框架.md`
  - `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必一答题点回填说明.md`
- governor_decision: blocked for exhaustive completion; usable selected-compulsory-one main-question framework stage draft only.

## Passed This Round

- Latest `feige-politics-garden` skill was used after the user requested a restart.
- Real role agents were spawned and registered for Leader, Organizer, Mapper, Patcher, Governor, and Automation.
- User framework from the attached PDF was preserved in `USER_FRAMEWORK.md`.
- Mixed 必修二 + 选必一 “经济角度” patch was applied: only international-economy chains were merged.
- Main-question scoring chains were merged only from rubric, marking-report, or lecture-scoring evidence.
- Vague question labels from the old run were replaced with exact anchors.
- Pure compulsory-two domestic-economy content was explicitly excluded from the selected-compulsory-one framework.
- Long-term files updated: `book_method_registry.md`, `master_rubric_summary.md`, and this governor board.

## Failures To Rerun

- Full source exhaustion: not complete.
- Choice-question wrong-option line: not processed in this round.
- OCR/protected-source conversion: not complete.
- `国家安全是最高国家利益` still needs a hard selected-compulsory-one main-question scoring source before it can be counted as included.

## Remaining Blockers

- 21 source files in `SOURCE_LEDGER.csv` are `ocr-needed` or protected/scan-only.
- Choice-question objective-key and wrong-option work remains pending.
- Whole-book `TASK_COMPLETE` is not allowed.

## Active Run

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选择性必修一_当代国际政治与经济_2026-04-25_1417`
