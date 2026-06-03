# Claude Cowork E2 — 全 65 题完善与 codebook 扩展审查报告

baseline: 65 core formal=61 / ref=4 / missing=0；framework_v1 直接闭合 16/65；formal PARTIAL 45；reference_only PARTIAL 4；当前 codebook 7 行。本报告仅做 codebook 扩展候选评估，不输出最终框架、不输出宝典、不动 v1 节点。

## 0. 工作口径

- 不直接造框架节点，只提出 codebook observation；每条候选都附带 question_id + rubric_atom_id + material_atom_id 三角；reference_only 不进核心；不按教材目录补节点；不把必修三话语升级；不把法考构成要件硬塞。
- 不能促成稳定 code 的题，明确写"transfer/open-container"或"reject"，不硬凑。

## 1. 总体口径数字

| 桶 | 题数 | 含义 |
|---|---|---|
| already_closed_by_existing_code | 16 | framework_v1 当前 PASS |
| promote_candidate_new_code | 与 CODE_COWORK_008 联动的 6 道题 (formal) | 见 §3.1 |
| revise_existing_code | 涉及 001/002/004-006/007 的 21 道题 | 见 §3.2 |
| transfer_only_open_container | 11 道单题或宽口径题 | 见 §4 |
| source_check_needed | 5 道 | 见 §5 |
| reference_only_non_core | 4 道 | 见 §6 |

（部分题同时跨多个桶，例如 CC0103/CC0143 同时落入 promote_008 与 revise_002／revise_007；全量见 claude_cowork_all65_completion_table.csv 的 why_not_closed_yet 字段中的 secondary 标注。）

## 2. 任务 A 摘要：全 65 题 completion_status

完整表见 `claude_cowork_all65_completion_table.csv`。字段：question_id / completion_status / current_pass_status / evidence_level / existing_framework_entry_node / why_not_closed_yet / what_evidence_could_close_it / must_not_promote_reason_if_any。

关键观察：
- 16 道 PASS 题分布在七个 v1 节点上，证据落点稳定；本轮不动。
- 45 道 formal PARTIAL 题中，**只有 6 道与 CODE_COWORK_008 联动构成新 code 的稳定证据基**（CC0131 / CC0206 / CC0229 / CC0283 / CC0319 / RECOVER_2026_西城_二模_18_2，并部分含 CC0103、CC0143）。
- 14 道题提供"对 001/002/004-006/007 的 revise"证据；其余多数属单题孤证或宽口径，必须保留 transfer。
- 4 道 reference_only 题（CC0040 / CC0162 / CC0311 / CC0353）按硬规则只能 weak/open observation，不进核心。

## 3. 任务 B+C：扩展候选清单

完整表见 `claude_cowork_codebook_expansion_candidates.csv`，10 条候选；按 status 概括如下。

### 3.1 可新增到 provisional_codebook_v1 的候选观察（promote_to_codebook）

**EXP_008 → CODE_COWORK_008 知识产权/不正当竞争司法保护四步链**

- supporting_question_ids: CC0131_2025_房山_一模_19 | CC0206_2025_西城_期末_19 | CC0229_2026_东城_一模_18 | CC0283_2026_朝阳_一模_18 | CC0319_2026_海淀_期末_19 | CC0103_2025_丰台_一模_19 | CC0143_2025_朝阳_一模_19 | RECOVER_2026_西城_二模_18_2
- minimum judgment：①行为定性（不正当竞争／知识产权侵权／商业诋毁／恶意诉讼）→②援引（《反不正当竞争法》或《民法典》具体规则）→③司法手段（惩罚性赔偿／调解／驳回／制止侵权）→④法治意义（创新生态+营商环境+核心价值观）。
- 全题三角：六道独立年份独立学校题反复同型奖励同一答题链；rubric 与 material atom 链接齐备。
- 风险：
  - empty_value: 高——CC0103 明文扣"维护双方合法权益、优化营商环境"；意义层必须明确受益主体。
  - legal_exam: 高——CC0143 明文"部分写反不正当竞争被扣"；要求精准区分消法/反法/民法典。
  - 模块边界: 低，但需克制不滑入必修三"法治化营商环境"宏观话语。
- 反例与边界：CC0319 同时含"民事主体行使权利不得超出正当界限"提示，意义层不应只停在不正当竞争层。

> 这是本轮唯一推荐**新增**的 code。其他 cluster 在严格三角与"反复同型"标准下，更适合作为对现有 code 的 sub-branch 扩展，避免与已有 7 条 code 重叠或在小样本上虚增 code。

### 3.2 只能修订现有 code 的候选观察（revise_existing_code）

**EXP_001R → 修订 CODE_COWORK_001**：加入"法理依据+事实分析+意义/保障作用"三段式 cell sub-pattern。
- 支撑：CC0189 / CC0213 / CC0214 / CC0137 / RECOVER_2025_海淀_二模_18（5 道题）。
- 反例：CC0084 等"完成下表"型并非全部三段式，不可硬套。

**EXP_002R → 修订 CODE_COWORK_002**：加入"对象=民法基本原则/具体法律制度/典型案例示范"三角分支。
- 支撑：CC0019 / CC0054 / CC0045 / CC0063 / CC0223 / RECOVER_2026_西城_二模_18_3（6 道题；与 CC0251 PASS 题同方向）。
- 反例：评析当事人行为题（CC0238 / CC0373）不进意义层。

**EXP_007R → 修订 CODE_COWORK_007**：加入"识别违法行为 + 法律边界/诉讼请求 + 程序救济 + 实体责任承担"四段扩展。
- 支撑：CC0092 / CC0277 / CC0289 / CC0380 / RECOVER_2024_东城_二模_19_1 / RECOVER_2026_延庆_一模_18_1 / RECOVER_2026_门头沟_一模_18_1 / CC0125（8 道题）。
- 边界：不可越级到行政诉讼或完整民诉法体系（CC0245_03 已明确警示）。

**EXP_046R → 修订 CODE_COWORK_004 + CODE_COWORK_006**：加入"多主体评析"与"无显式以事实为依据锚句但仍存在 1 分法理依据"分支。
- 支撑：CC0238 / CC0364 / RECOVER_2026_西城_二模_18_1（3 道题）。
- 反例：单主体题不可硬套多主体链。

### 3.3 只能保持 transfer / open-container 的题或 cluster（keep_transfer_only）

详见 `claude_cowork_transfer_only_or_open_container.csv`。主要包括：

| question_id | transfer_reason |
|---|---|
| CC0025_2024_朝阳_二模_17 | 平台用工三从属性，单题孤证（候选 EXP_LABOR） |
| CC0181_2025_海淀_期末_21 | 竞业限制单题；法考化风险高 |
| CC0195_2025_西城_一模_20 | 工会集体合同+公平与效率，跨模块单题 |
| CC0200_2025_西城_二模_18 | 未成年人打赏多方过错单题（候选 EXP_MINOR） |
| CC0276_2026_房山_二模_17 | 涉外法治公共政策论证，模块边界高（候选 EXP_FOREIGN → reject） |
| CC0318_2026_海淀_期末_18_2 | 住房租赁条例规范意义，单题 |
| CC0332_2026_石景山_二模_19 | 校园欺凌"惩教并行"，单题 |
| CC0340_2026_西城_一模_17 | 民法典物权编绿色发展，单题 |
| RECOVER_2024_东城_一模_19 | 诉讼时效说明，单题 |
| RECOVER_2024_东城_二模_19_2 | "避免类似问题"2 分小题 |
| RECOVER_2025_丰台_二模_19_2 | "谈对××的理解"宽口径题 |

### 3.4 应明确 reject 的题或 cluster（reject）

- **EXP_FOREIGN (CC0276 涉外法治)**：公共政策论证脱离"反复奖励同一最小判断+材料事实到法律语言"模式；模块边界与必修三化风险高；硬规则 8/10 共同禁止升级。
- **EXP_REF (4 道 reference_only 题)**：硬规则 5/11 明文禁止 reference_only 单独支撑核心 code；只能 weak/open observation。

### 3.5 仍需回源核查的题号（source_check_needed）

详见 `claude_cowork_source_check_questions.csv`。

| question_id | 必须先做的源核动作 |
|---|---|
| CC0011_2024_丰台_二模_17 | rubric atom 单一未切分；8 分整段需拆为独立赋分单元 |
| CC0019_2024_朝阳_一模_19 | rubric atom 单一未切分；7 分整段需拆 |
| CC0061_2024_西城_一模_18 | 三个小问（回避制度/错别字/赡养义务）需独立 atom 化 |
| CC0254_2026_丰台_二模_18 | rubric atom 多为教学反思/学生问题清单，非细则切分 |
| RECOVER_2026_房山_一模_17_1 | rubric atom 三条为抽象奖励标签，需补独立赋分单元 |

源核前不得 promote（硬规则 6）。源核后 CC0011/CC0019/CC0054 大概率收敛到 EXP_002R；CC0254 与 RECOVER_2026_房山_一模_17_1 是否构成"辨析题"新机制，待源核后再评估。

## 4. 任务 B：cluster 源核摘要

完整表见 `claude_cowork_source_check_needed.csv`（30 cluster × 12 字段）。结论分布：

| 处置 | cluster 数量 | 备注 |
|---|---|---|
| PROMOTE 008（独立成 code 部分） | PC09 整体 / PC06 部分 / PC14 部分 / PC19 整体 / PC16 部分 | 见 EXP_008 |
| REVISE 001 | PC02 整体 / PC15 整体 | 见 EXP_001R |
| REVISE 002 | PC01 部分 / PC03 部分 / PC11 部分 / PC12 / PC14 部分 / PC06 部分 | 见 EXP_002R |
| REVISE 007 | PC04 部分 / PC23 / PC24 / PC08 部分 / PC27 / PC07 部分 / PC30 / PC05 部分 | 见 EXP_007R |
| REVISE 004/006 | PC10 部分 / PC11 部分 / PC20 | 见 EXP_046R |
| SOURCE_CHECK | PC03 (CC0011) / PC10 (RECOVER) / PC13 (CC0061) / PC21 (CC0254) | 见 §3.5 |
| TRANSFER / REJECT | PC01 (CC0025) / PC04 (CC0332) / PC05 (RECOVER) / PC07 (CC0200) / PC17 / PC18 / PC22 / PC25 / PC26 / PC28 / PC29 | 见 §3.3-3.4 |

> 任意 cluster 是否构成新 code 的判定只看"反复奖励同一最小判断 + 同型材料事实到法律语言转化 + 同型满分句"，不看主题相似。多数 cluster 是"题型主题"层面的相似，最小判断不同，因此不能促 code。

## 5. v1 → v2 建议

不写 v2，但给出三条结构性建议（不构成框架文本）：

1. **新增 1 个 code（CODE_COWORK_008）** 是本轮唯一稳健的扩展。其加入后，FWV1_N04/N05/N06 都会因为多了一条"知识产权+不正当竞争司法保护"专门通道而减负，预计可把现在分散在 N02+N03+N04 / N02+N04+N05 / N02+N04+N06 三个 PARTIAL 桶里的 6–8 道题升级为 PASS。

2. **对 001 / 002 / 007 各做一次 sub-branch revision**（EXP_001R/002R/007R）。这三处修订不增加新节点，但把当前 21 道 PARTIAL 题中的多数收敛到现有 code，本身在 v1 框架结构上不改变节点数，只动 codebook 内部的 rubric_reward_pattern 与 full_score_sentence_pattern 字段。

3. **保持单题孤证为 transfer**，不要为了"提高 PASS 率"在 v2 增 single-question 节点。65 题语料里"竞业限制 / 涉外法治 / 校园欺凌 / 物权编绿色 / 工会集体合同 / 监护责任 / 诉讼时效 / 集体合同 / 住房租赁条例"都是单题孤证或公共政策论证，硬规则 10 要求保留为 TRANSFER_TEST。

落地次序（不写 v2 内容，仅排序）：
1. 完成 5 道 source_check 题的回源切分（CC0011 / CC0019 / CC0061 / CC0254 / RECOVER_2026_房山_一模_17_1）。
2. 评估 EXP_002R 与 EXP_008 在源核后是否仍互不冲突（CC0011 / CC0054 / CC0143 / CC0103 的归属可能位移）。
3. 在 codebook_v1 上做 5 条变更：1 新增 + 4 修订（001/002/004-006/007）。
4. 再做一次全 65 题压测，再决定是否触发 v2。

## 6. 输出文件

- `claude_cowork_all65_completion_table.csv` — 任务 A 全 65 题分类。
- `claude_cowork_codebook_expansion_candidates.csv` — 任务 C 全部 10 条 expansion_candidate。
- `claude_cowork_source_check_needed.csv` — 任务 B 30 个 cluster 源核结论。
- `claude_cowork_transfer_only_or_open_container.csv` — 必须保留为 transfer 的 11 道题。
- `claude_cowork_source_check_questions.csv` — 必须回源的 5 道题与具体动作。
- `claude_cowork_all_question_completion_report.md` — 本报告。

## 7. 硬规则自检

- ✅ 不输出最终框架/总图/学生口诀/宝典目录。
- ✅ 所有候选 observation 均附 question_id + rubric_atom_id + material_atom_id。
- ✅ reference_only 单列于 reject，不入核心。
- ✅ pending/source_check 5 道题明确标注"需回源后再评估"，未升级。
- ✅ 不按教材目录补节点。
- ✅ 不把必修三话语升级（CC0276 已 reject；CC0289_08 的"答必修3不赋分"已写入 EXP_007R 的 boundary）。
- ✅ 不把法考构成要件硬塞高中题（EXP_008 / EXP_007R 都标注"法考化风险高+具体警戒线"）。
- ✅ 单题孤证均保留为 transfer/open-container 或 reject（CC0025 / CC0181 / CC0195 / CC0200 / CC0276 / CC0318 / CC0332 / CC0340 / RECOVER_2024_东城_一模_19 / RECOVER_2024_东城_二模_19_2 / RECOVER_2025_丰台_二模_19_2）。
- ✅ 全程未生成 v2 框架文本。
