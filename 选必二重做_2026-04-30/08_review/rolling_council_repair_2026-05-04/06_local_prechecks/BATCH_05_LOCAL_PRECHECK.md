# Batch 05 本地预扫：纠纷解决生态公益与新业态

生成时间：2026-05-04

角色边界：Codex A 内部“劳动者 + 补丁者”本地预扫。本文件不是最终框架定稿，不替代 GPT-5.5 Pro / Claude Opus 4.7 Adaptive，也不替主线程做最终五域裁决。

## 0. 读取与裁决依据

已读本地规则：

- `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
- `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbier/SKILL.md`
- `/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/00_飞哥选必二法律与生活要求小本本.md`

已读本地证据：

- `01_batch_packs/batch_05_纠纷解决生态公益与新业态.md`
- `05_codex_local_decisions/BATCH_01_CODEX_LOCAL_DECISION.md`
- `05_codex_local_decisions/BATCH_02_CODEX_LOCAL_DECISION.md`
- v2 预处理核对表：`preprocess_v2_2026-05-03/LEGAL_QUESTION_INDEX_V2.csv`、`curated/*LEGAL_QUESTION_INDEX_V2.csv`、`curated/*SUBJECTIVE_SOURCE_PACKS_V2.csv`

沿用 B01/B02 的硬规则：

- reference answer 不推动主干。
- `formal_or_scoring_source` 可以支持候选主干，但遇到混合模块、摘录串题、OCR 污染时必须先抽法律小问或回源核验。
- `official_answer_key` 只锁选择题答案，不等于主观题采分细则；若 Batch05 包与 v2 预处理答案锁定状态冲突，先标 `需本地核验`。
- 程序救济暂保留“双身份”：横切动作 + 归位容器；不在 Batch05 直接定为独立第五实体域。
- 公共法律服务、生态公益、新业态不能靠关键词升主域；需要看设问是否要求《法律与生活》的具体法律关系、程序、效力、责任或救济。

## 1. 本批总判

`纠纷解决生态公益与新业态` 不建议作为未经拆分的第五域直接 accept。

更稳的本地候选结构是：

1. `程序救济 / 纠纷解决`：candidate，作为横切动作强成立，同时可保留低频归位容器。强证据来自诉讼时效、多元解纷、调解/仲裁/诉讼、举证责任、和解/司法确认等题。
2. `生态公益`：defer，不宜升为实体主域。它多是绿色原则、公共利益、公益诉讼或司法保护的价值出口，需要挂回物权/侵权/IP/程序。
3. `新业态`：reject 独立主域；candidate 场景标签。平台打赏、AI/新质生产力、线上纠纷平台等应挂回民事行为效力、平台责任、知识产权或程序救济。
4. `公共法律服务 / 社会治理服务`：defer 边界题。若主落点是政府公共服务、基层治理、公共服务水平，不能进入法律主干频次；若设问奖励具体调解、诉讼、司法确认、举证责任，才抽法律小问。

## 2. 逐题本地预扫

### 1. 2024 东城一模 Q19

- 本地判断：真程序救济，但应作为“诉讼时效 + 家庭赡养例外”的横切规则，不是第五域实体样本。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=未见独立推动；疑似污染=未见。
- 本地依据：Batch05 pack 标 `formal_scoring_matched`；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源锁定到 2024 东城一模答案/细则 PDF。
- 命题路径：目标是让学生理解诉讼时效的制度功能和不适用例外；载体选择赡养费请求与法院诉讼；设问从“原因”切入；评分奖励“督促主张权利、解决纠纷、节约司法资源”以及“保护老人基本生存权利、公序良俗、人文关怀”。
- 建议：accept 为程序横切卡；revise 归位为“程序规则 + 家庭赡养价值”，不计为第五域独立频次。

### 2. 2024 丰台二模 Q17

- 本地判断：生态公益真题，但更像“绿色原则/生态公共利益价值出口 + 知识产权技术支撑 + 环境侵权责任”，不是单独第五域主干。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=有“参考答案/拓展答案”字样，不能推动主干；疑似污染=有，Batch05 摘录后半混入 18(1)、18(2) 逻辑/科学思维内容。
- 本地依据：Batch05 pack 标 `formal_scoring_matched`；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为丰台二模细则 docx。
- 命题路径：目标是考民法典绿色原则如何服务生态环境保护；载体是环境污染、知识产权保护、公益诉讼/法院判决；设问问“作用”；评分奖励绿色原则、技术创新支撑、污染侵权责任、权利义务和个人/公共利益平衡。
- 建议：revise。只取 Q17 的评分标准说明部分；参考答案与拓展答案只能作表达线索；混入 Q18 的逻辑/科学思维内容必须隔离。

### 3. 2024 朝阳二模 Q12

- 本地判断：真程序识别选择题，考民事诉讼、刑事自诉、二审/审监边界；但 Batch05 与 v2 答案锁定状态冲突。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 C，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack 标 `official_answer_key / objective_answer_locked`；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标 `defer_answer_missing`、`missing_exact_rubric_block`。
- 命题路径：目标是区分平等主体民事纠纷与刑事/审监程序；载体是羽毛球受伤索赔诉讼；设问通过四个题肢嵌入程序错位；评分奖励识别民事诉讼性质，排除辩护人、自诉刑责、二审后上诉等错位。
- 建议：defer。先回源核验可靠客观答案表；若 C 锁定，可 accept 为“程序选择题微卡”。

### 4. 2024 海淀一模 Q11

- 本地判断：混合题。实体主干是体育活动侵权/公平原则，程序题肢涉及庭审调解与审监期限；不宜整题归第五域。
- 证据标记：formal_or_scoring_source=Batch05 标是，v2 选择题索引为 `missing_exact_rubric_block`；official_answer_key=答案 C 已在 Batch05 与 v2 accepted 中出现；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv` 为 `accept_high`，答案 C。
- 命题路径：目标是考活动风险责任与民事诉讼程序边界；载体是足球受伤索赔；设问用组合选项；评分奖励“公平原则/合理确定权利义务”和“庭审调解程序”，同时排除不可抗力、审监期限错位。
- 建议：revise。进入人格权/侵权或一般侵权主域，程序调解作为题肢级横切标签。

### 5. 2024 石景山一模 Q18

- 本地判断：有法律小问，但 Batch05 证据状态疑似被抬高；必须只抽（2）物业服务合同、不可抗力、人民调解/司法确认小问。
- 证据标记：formal_or_scoring_source=Batch05 标是，v2 标 `missing`；official_answer_key=否；reference_answer=无可靠推动；疑似污染=有，Batch05 评分摘录开头混入“碳排放配额交易/碳达峰碳中和”价值段。
- 本地依据：v2 `DEFERRED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 标 `defer_mixed_module`、`需回原细则/OCR 复核`；Batch05 pack 中摘录明显串入其他内容。
- 命题路径：目标是让学生给基层调解员提供专业法治指导；载体是暴雨漏房、物业服务合同、一米法庭；设问要求“假如你是法官”；评分应奖励不可抗力条件、物业违约责任、非诉调解优先、司法确认强制执行效力。
- 建议：defer / revise。先回原细则/OCR；确认后只入“合同违约 + 程序救济横切”，不能用污染摘录推动第五域。

### 6. 2024 西城一模 Q18

- 本地判断：混合题段。Q18(1)(2) 是诉讼程序术语，Q18(3) 主体是赡养义务和法治德治价值；不能整题放入程序救济。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=否；疑似污染=非串题污染，但 v2 标混合模块。
- 本地依据：Batch05 pack；v2 `DEFERRED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 标 `defer_mixed_module`，细则源为西城一模细则 docx。
- 命题路径：目标是通过模拟庭审和告知书考诉讼角色、回避制度、赡养义务及法律促进道德；载体是二审赡养纠纷；设问分三问；评分奖励回避理由、辩护人/诉讼代理人纠错、赡养义务和孝老敬亲价值。
- 建议：revise / defer。抽小问：程序术语小卡可入程序横切；Q18(3) 应归家庭赡养与法德价值出口，不算第五域主样本。

### 7. 2024 西城二模 Q11

- 本地判断：公益诉讼/行政监管程序边界题，具有程序开放容器价值；但民事诉讼、行政诉讼、公益诉讼关系需核验。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 B，v2 为 `defer_mixed_module` 且 `missing_exact_rubric_block`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标混合模块。
- 命题路径：目标是区分公益诉讼中行政机关举证、审理程序和上诉期限；载体是文物旧址监管职责案；设问用四个程序判断；评分奖励行政行为合法性举证与上诉期限，排除民事诉讼程序错位。
- 建议：defer。可作为“公益诉讼/行政程序边界”开放容器候选，不进入民事程序主干频次。

### 8. 2024 西城二模 Q13

- 本地判断：人民调解/枫桥经验是真纠纷解决，但更偏基层治理与人民调解制度，不是具体民事法律关系题。
- 证据标记：formal_or_scoring_source=Batch05 标是；official_answer_key=答案 C；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv` 为 `accept_high`、答案 C。
- 命题路径：目标是考人民调解与新时代枫桥经验的制度定位；载体是“小事不出村”等治理经验；设问问“因为”；评分奖励“党领导下基层社会治理机制和方法”“依靠人民群众正确处理人民内部矛盾”，排除收费和法院主持调解错位。
- 建议：revise。保留为“纠纷解决低频开放容器/公共法律服务边界”，不推动程序主干细化。

### 9. 2024 顺义二模 Q11

- 本地判断：错归 Batch05。主干是网络差评、新闻报道、公共利益抗辩、人格/名誉侵权边界，诉讼只是材料载体。
- 证据标记：formal_or_scoring_source=否；official_answer_key=答案 A；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `ACCEPTED_LEGAL_QUESTION_INDEX_V2.csv` 为 `accept_high`、答案 A。
- 命题路径：目标是考批评监督、新闻媒体如实报道与侵权责任边界；载体是网络匿名评价和媒体报道；设问要求判断认识；评分奖励公共利益如实报道不承担民事责任，排除终审/举证责任倒置等程序错项。
- 建议：reject from Batch05 / revise to Batch03 人格权侵权。程序题肢不推动程序域。

### 10. 2025 东城一模 Q19

- 本地判断：真程序救济核心题，但内部案例跨劳动、继承等实体关系；应作横切程序表格题。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为 2025 东城一模细则 PDF。
- 命题路径：目标是比较调解/仲裁/诉讼解决纠纷的机制与意义；载体是三个案件表格；设问是阅读材料完成表格；评分奖励机制识别、对劳动者/医院/家庭继承等主体的具体意义、以和为贵与定分止争。
- 建议：accept 为程序横切主证据；不要把其中劳动、继承案例反向并入第五域实体频次。

### 11. 2025 东城二模 Q10

- 本地判断：实体主干更像景区安全保障/侵权责任，调解和旅游环保法庭是情境；若答案为 D，程序不是主考点。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 D，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标答案未锁。
- 命题路径：目标可能是考安全保障义务与调解方式边界；载体是游客被猴抓伤后热线调解；设问用选择题排错；评分若落 D，奖励“景区未尽安全保障义务须赔偿”，排除人民调解、无须举证、只要游客未注意即可免责。
- 建议：defer / revise。先核验答案；若 D 锁定，应归侵权/安全保障，程序只作材料场景。

### 12. 2025 东城期末 Q17

- 本地判断：生态司法价值题候选，但正式细则未锁，且 Batch05 摘录串入其他题。
- 证据标记：formal_or_scoring_source=Batch05 标是，v2 标 `missing`；official_answer_key=否；reference_answer=否；疑似污染=有，摘录混入“创新思维”“充电桩方案”等非本题内容。
- 本地依据：v2 `DEFERRED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 标 `defer_needs_rubric`、`需回原细则/OCR 复核`。
- 命题路径：目标是考法院如何通过惩处、执行修复、公开道歉提升生态治理；载体是污染环境罪、劳务代偿修复、公益诉讼/生态修复；设问问“如何提升生态颜值”；评分应奖励审判权/惩处、创新执行、生态修复价值。
- 建议：defer。只可列为生态公益价值出口待核验；不能用当前摘录推动第五域。

### 13. 2025 丰台二模 Q9

- 本地判断：公共法律服务/劳动调解边界题，主落点是劳动关系和社会治理服务，不是独立第五域。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 B，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标答案未锁；旧 choice preprocess 也提示答案未自动锁定。
- 命题路径：目标是考一站式调解中心的功能定位；载体是街道劳动人事争议调解中心；设问评析该中心；评分奖励促进劳动关系和谐、提升社会治理水平，排除“创新劳动人事改革”“居民自治权利”。
- 建议：defer / revise。若答案锁定，可挂“劳动与职业 + 纠纷解决服务”双标签；不计为第五域实体频次。

### 14. 2025 丰台二模 Q10

- 本地判断：真诉讼调解/多元解纷价值题，但选择题答案锁定需复核。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 D，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标答案未锁。
- 命题路径：目标是考诉讼调解对金融纠纷的实质化解；载体是债务纠纷、法官调解、企业融资风险；设问用四个判断；评分奖励“成功调解共赢/激发市场主体活力”“司法为民/司法温度”，排除诉讼唯一有效和举证责任错位。
- 建议：defer 后 candidate。答案核验后可入程序横切/诉讼调解价值卡。

### 15. 2025 海淀期末 Q14

- 本地判断：错归 Batch05。主干是著作权侵权与举证，调解只是一个可选题肢。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 C，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标答案未锁。
- 命题路径：目标是考著作权保护、登记误区、被告举证与法院调解；载体是食品包装使用画作图案；设问选择正确判断；评分奖励举证责任和法院主持调解，排除著作权登记决定权利、发表权保护期等错误。
- 建议：reject from Batch05 / revise to Batch04 知识产权；程序只作题肢标签。

### 16. 2025 西城二模 Q18

- 本地判断：真“新业态场景”题，但法律主干是限制民事行为能力人大额打赏、民事法律行为效力、平台过错、监护责任和公平责任分担。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=有答案示例但同时有细则；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为 2025 西城二模细则 docx。
- 命题路径：目标是考平台经济场景中未成年人交易效力和多方过错；载体是网络主播打赏平台；设问分析法院判决结果；评分奖励限制民事行为能力、行为无效、平台/父母/小刘各方过错、民法典 157 条、公平原则和平台/监护人价值引导。
- 建议：revise。新业态只能作场景标签；主归“民事行为效力 + 平台责任/监护责任”，不支持新业态独立主域。

### 17. 2025 顺义一模 Q19

- 本地判断：题面是真纠纷解决/定分止争，但现有评分摘录严重污染，不能进入主干证据。
- 证据标记：formal_or_scoring_source=Batch05 标是，v2 为 `missing_exact_rubric_block`；official_answer_key=否；reference_answer=不可用；疑似污染=有，Batch05 摘录混入文化、逻辑、政府职能等非本题内容。
- 本地依据：v2 `ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 标 `accept_high` 但 `evidence_type=missing`、`需回原细则/OCR 复核`；Batch05 pack 中评分摘录明显与 Q19 不匹配。
- 命题路径：目标应是比较案例一调解、案例二行政裁决/诉讼，并阐释定分止争价值；载体是邻里纠纷和企业名称争议；设问为“如何解决纠纷”“定分止争价值”；评分应奖励调解、行政裁决/诉讼、案结事了人和、公平正义。
- 建议：defer。题面可保留候选；评分细则必须回源后才可推动程序横切。

### 18. 2026 东城一模 Q18

- 本地判断：混合 IP + 程序救济题。主域应是知识产权/创新保护，程序是“调、惩、辨”中的横切动作。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=否；疑似污染=有 OCR 噪声和扫描残留，但 v2 细则源锁定。
- 本地依据：Batch05 pack；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为 2026 东城一模细则 PDF。
- 命题路径：目标是考法院如何通过司法保护创新；载体是专利权归属调解、植物新品种权惩罚性赔偿、恶意诉讼驳回；设问问“如何守护向新力”；评分奖励诉讼调解、惩罚性赔偿、规制恶意诉讼、公正司法和保护创新。
- 建议：revise。主归 Batch04 知识产权不正当竞争；程序救济只作横切动作。需清理 OCR 污染后再引用采分点。

### 19. 2026 朝阳一模 Q11

- 本地判断：多元纠纷一体化平台是真纠纷解决/公共法律服务边界题，但不是具体民事责任题。
- 证据标记：formal_or_scoring_source=否；official_answer_key=Batch05 标 B，v2 标 `defer_answer_missing`；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `DEFERRED_LEGAL_QUESTION_INDEX_V2.csv` 标答案未锁。
- 命题路径：目标是考多元力量融合与诉前调解效率；载体是道交纠纷线上处理平台；设问选择正确说法；评分奖励创新矛盾化解渠道、提升效率，排除法院审判职能、法律援助、行政裁决错位。
- 建议：defer / candidate。答案核验后可入“公共法律服务/纠纷解决开放容器”，不升第五域主干。

### 20. 2026 朝阳一模 Q18

- 本地判断：主干是知识产权护航新质生产力，程序救济是法院做法之一；不应留在 Batch05。
- 证据标记：formal_or_scoring_source=是，但 Batch05 只露出“措施类”提示，采分细则需核验；official_answer_key=否；reference_answer=否；疑似污染=未见明显串题，但评分体不完整。
- 本地依据：v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为 2026 朝阳一模细则 docx。
- 命题路径：目标是考人民法院依法保护知识产权；载体是调解专利权归属、惩罚性赔偿、规制恶意诉讼；设问问“如何依法保护知识产权”；评分应奖励法院“调、惩、辨”的具体措施及其创新保护效果。
- 建议：revise to Batch04。程序横切保留，但不推动第五域。

### 21. 2026 石景山一模 Q18

- 本地判断：真程序救济核心题，尤其是举证责任分配；可支持“程序横切卡”。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=否；疑似污染=未见。
- 本地依据：Batch05 pack；v2 `FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 为 `accept_high`，细则源为 2026 石景山一模细则 doc。
- 命题路径：目标是考刑事、行政、民事诉讼中举证责任分配；载体是公诉、行政诉讼、建筑物坠落损害；设问要求参考示例完成表格；评分奖励行政机关举证、原告损害/因果举证、建筑物使用人过错倒置、谁主张谁举证和公平合理。
- 建议：accept。进入程序横切主证据，但不据此把第五域定成实体域。

### 22. 2026 门头沟一模 Q18

- 本地判断：Q18(1) 是真“环境民事公益诉讼 + 和解/司法调解/司法确认效力”题；Q18(2) 是逻辑与思维，必须切开。
- 证据标记：formal_or_scoring_source=是；official_answer_key=否；reference_answer=有“示例”但同时有细则；疑似污染=混合模块，Batch05 摘录含 Q18(2) 逻辑与思维细则。
- 本地依据：Batch05 pack；v2 `DEFERRED_SUBJECTIVE_SOURCE_PACKS_V2.csv` 标 `defer_mixed_module`，原因是同一题段含《法律与生活》和其他模块显性设问；细则源为 2026 门头沟一模细则 docx。
- 命题路径：目标是考公益诉讼主体、纠纷解决方式、司法确认效力如何维护生态环境公共利益；载体是赤泥库环境民事公益诉讼；设问 Q18(1) 问“如何消除损害风险、维护生态环境公共利益”；评分奖励公益组织起诉、和解/司法调解/诉讼、多元纠纷解决、法院审查确认、强制执行效力。
- 建议：revise / defer。抽 Q18(1) 后可作为“程序救济 + 生态公益价值出口”强候选；Q18(2) 逻辑与思维全部隔离。

## 3. 疑似污染与需核验清单

高优先级污染隔离：

1. 2024 丰台二模 Q17：Batch05 摘录后半混入 Q18(1) 逻辑规则和 Q18(2) 科学思维，不能用后半推动法律框架。
2. 2024 石景山一模 Q18：Batch05 标 formal，但 v2 标 `missing/defer_mixed_module`；摘录混入碳排放配额交易价值段，必须回源。
3. 2025 东城期末 Q17：Batch05 摘录混入创新思维和充电桩权利内容；v2 标 `defer_needs_rubric`。
4. 2025 顺义一模 Q19：Batch05 评分摘录与定分止争题不匹配，混入文化、逻辑、政府职能；只能保留题面候选。
5. 2026 东城一模 Q18：v2 有 formal 源，但 OCR 噪声严重，引用采分点前要回 PDF/渲染页清理。
6. 2026 朝阳一模 Q18：v2 有 formal 源，但 Batch05 只露出“措施类”提示，细则体不完整，需回细则 docx。
7. 2026 门头沟一模 Q18：Q18(1) 法律与生活可用，Q18(2) 逻辑与思维必须隔离。

选择题答案锁定冲突：

- Batch05 标 `official_answer_key`，但 v2 仍 `defer_answer_missing` 的题：2024 朝阳二模 Q12、2025 东城二模 Q10、2025 丰台二模 Q9、2025 丰台二模 Q10、2025 海淀期末 Q14、2026 朝阳一模 Q11。
- 处理建议：这些题可以用于“候选题型/命题路径观察”，但不得生成正式错项句或推动频次，除非回源确认可靠答案表。

## 4. 给主线程的 accept / revise / defer / reject

### accept

- 接受“程序救济/纠纷解决”作为强横切动作：诉讼时效、调解/仲裁/诉讼、司法确认、举证责任、多元解纷均有本地题面支撑。
- 接受 Q1、Q10、Q21 作为程序横切的较稳主证据；Q22(1) 可在小问拆分后作为强候选。
- 接受“价值后置”规则：生态公益、新业态、司法温度、以和为贵、社会责任等只能在本案法律关系/程序/处理结果之后收束。

### revise

- 把当前第五域拆为后台标签：`程序救济`、`公益/生态价值出口`、`新业态场景`、`公共法律服务边界`。
- 把 Q9、Q15、Q18、Q20 从 Batch05 主体中移出或改为横切标签：它们的主域分别更接近人格权侵权、知识产权、知识产权、知识产权。
- 把 Q16 “平台打赏”从“新业态域”改为“民事行为效力 + 平台/监护过错责任”，新业态只作场景标签。
- 把 Q4、Q11 这类实体责任题中的程序题肢拆成“题肢级程序标签”，不整题推动程序域。

### defer

- 第五域最终是否保留原名、重命名，或改为“程序横切 + 低频开放容器”，必须等 Batch03/B04/B05 全部本地裁决和主线程融合后定。
- 公共法律服务/社会治理边界题是否纳入法律合集，需统一核验 B02 提到的 2026 海淀一模 Q9 与本批 Q8、Q13、Q19。
- 生态公益是否需要单独追踪标签，可以保留；但是否成为第五域前台入口，当前证据不足。
- 所有 `defer_answer_missing` 选择题不得推动客观错项库或主干频次。
- 所有摘录污染题必须回源核验后再进入主线程融合。

### reject

- 拒绝把 `纠纷解决生态公益与新业态` 作为一个不拆分的第五域直接定稿。
- 拒绝把 reference answer、拓展答案、污染摘录推动主干。
- 拒绝把“出现法院/诉讼/调解/平台/生态环境”作为归域充分条件。
- 拒绝把“新业态”独立成学生前台主域；它目前只支持场景标签。
- 拒绝把生态公益单独升成实体主域；更稳的是“法律规则入口 + 生态公共利益价值出口”。

## 5. 覆盖增量与缺口

本地预扫新增的可用判断：

- Batch05 的真实核心不是一个第五实体域，而是“程序横切”与三个低频容器的混合。
- 程序题里有稳定可教动作：谁能主张、走什么程序、谁举证、协议/调解有什么法律效力、法院如何促成实质解纷。
- 生态公益题的稳定表达是价值出口，不是入口；必须先有民法绿色原则、侵权责任、公益诉讼主体或司法确认效力。
- 新业态题目前没有独立法理主干，只能挂回民事行为效力、平台责任、IP 保护、纠纷解决平台等实体/程序节点。
- 公共法律服务题是最大边界风险：一旦主落点是公共服务或治理水平，就不能计入法律主干频次。

仍未关闭：

- Batch05 真实 GPT/Claude 双向审议与主线程 Codex 本地裁决尚未由本文件替代。
- 选择题答案锁定冲突尚未回源解决。
- 污染摘录尚未逐一回原 Word/PDF/PPT 渲染核验。
- 最终五域命名和学生前台结构仍应由主线程在五批闭合后裁决。
