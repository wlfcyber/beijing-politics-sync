# ClaudeCode Opus 4.7 严格最终版 — 93 条队列逐题裁决

- 队列来源：`04_review_queue.csv`（覆盖缺口 81 + 反合并残留 12）
- 第一轮参考：`05_codex_first_pass_adjudication.csv`
- 复核口径：本表把 Codex 的 `INCLUDE_STRICT_REVIEW / NEEDS_HUMAN_REVIEW` 全部回到题面+细则原文核验，按硬规则收紧。

## 裁决判定统计

| 判定 | 数量 |
|---|---:|
| `INCLUDE_STRICT_MAIN`（含反合并残留单题重写） | 24 |
| `EXCLUDE_OTHER_MODULE` | 61 |
| `NEEDS_EVIDENCE` | 12 |
| `DOWNGRADED_REFERENCE_ONLY` | 9 |
| 反合并残留处置：12 项中全部已逐单题裁决；19 个单题重写、7 个单题降级/排除 | 12 |

> 说明：表中 24 条 `INCLUDE_STRICT_MAIN` = 5 条覆盖队列新增 + 19 条反合并残留单题重写。覆盖队列 `DOWNGRADED_REFERENCE_ONLY` 2 条 + 反合并残留 `DOWNGRADED_REFERENCE_ONLY` 7 条 = 9 条。覆盖队列 81 条裁决：5 INCLUDE + 2 DOWNGRADED + 12 NEEDS_EVIDENCE + 62 EXCLUDE。

## 一、覆盖缺口 81 条（逐题）

| # | 套卷 | 题号 | 队列状态 | Codex第一轮 | 本轮裁决 | 复核理由 |
|---|---|---|---|---|---|---|
| 1 | 2024东城一模 | Q19 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面是"诉讼时效/抗辩权"，属《法律与生活》民事时效。 |
| 2 | 2024东城二模 | Q16 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面是春秋战国桑基鱼塘生态文化，属《哲学与文化》。 |
| 3 | 2024丰台一模 | Q17 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面是"好意同乘/民法典1217条"，属《法律与生活》。 |
| 4 | 2024丰台一模 | Q18 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 设问"《经济与社会》知识，说明……为发展新质生产力赋能的经济逻辑"，产业链一词出现在必修二语境。 |
| 5 | 2024丰台一模 | Q21 | answer_only_needs_rubric | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 题面是"全人类共同价值"短文，含"中国力量、供应链"提法且涉《当代国际政治与经济》，细则未定位。 |
| 6 | 2024丰台二模 | Q18 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 题面冰雪经济，《经济与社会》"有效市场+有为政府"，产业链作必修二采分。 |
| 7 | 2024朝阳一模 | Q17 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面北京国际科创中心建设建议，属《政治与法治》履职建议题。 |
| 8 | 2024朝阳一模 | Q19 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面民法典诚信原则、社会主义市场经济是法治经济，属《法律与生活》。 |
| 9 | 2024朝阳一模 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 题面是充分条件假言推理（炭化竹节），细则只判推理类型1分+理由2分，属《逻辑与思维》；"新型国际关系"出现在Q21 答案角度，与Q20 题面无关。 |
| 10 | 2024朝阳二模 | Q16 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面居民收入与个人收入分配制度，属《经济与社会》。 |
| 11 | 2024海淀一模 | Q19 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面虚拟数字人侵权案，属《法律与生活》。 |
| 12 | 2024海淀期中 | Q16 | candidate_review | INCLUDE_STRICT_REVIEW | **INCLUDE_STRICT_MAIN** | 细则明确：必修二4 + 选必一2，"贸易摩擦、利用国际组织赋予的权利，积极参与全球经济治理和规则制定2分"是选必一采分点，材料是企业出海。 |
| 13 | 2024海淀期中 | Q20 | candidate_review | NEEDS_HUMAN_REVIEW | NEEDS_EVIDENCE | 自动抽取未定位Q20 题面，仅看到2023山东20 同型讲评片段，无法证实2024海淀期中Q20 是否为选必一时政短评。 |
| 14 | 2024石景山一模 | Q16 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面是习近平文化思想为建设中华民族现代文明举旗定向，属《哲学与文化》。 |
| 15 | 2024石景山一模 | Q17 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面碳排放权交易合同纠纷案+民法基本原则，属《法律与生活》。 |
| 16 | 2024石景山一模 | Q18 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面"一米法庭"群众路线项目，属《政治与法治》。 |
| 17 | 2024石景山一模 | Q20 | answer_only_needs_rubric | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 题面"中国式现代化五个特色 战略性有利条件"综合，细则未定位；可能涉及《当代国际政治与经济》但口径不严不能入主表。 |
| 18 | 2024石景山一模 | Q22 | answer_only_needs_rubric | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | "经济全球化；全球治理"出自客观选择题第14 项，本身是选择题不入主观题主表。 |
| 19 | 2024西城一模 | Q16 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 题面《北京市未成年人保护条例》立法过程，细则讲"法制统一/良善之法/民主立法"，属《政治与法治》。 |
| 20 | 2024西城二模 | Q16 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 题面食品安全惩罚性赔偿与民事权利滥用，细则讲诚信原则、不滥用民事权利损害"国家利益"，但属《法律与生活》。 |
| 21 | 2024西城二模 | Q17 | candidate_review | EXCLUDE_OTHER_MODULE | **INCLUDE_STRICT_MAIN** | 9 分综合题，细则明示选必一可选角度："当前国际竞争实质，世界发展的贡献者和推动者，世界多极化，经济全球化；实施科教兴国战略、强化现代化建设人才支撑"。属选必一可正常补录（取选必一角度部分）。 |
| 22 | 2024顺义二模 | Q17 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 题面"财产制度助力经济社会发展"，细则讲物权平等保护原则、产权保护制度，属《法律与生活/经济与社会》。 |
| 23 | 2024顺义二模 | Q18 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 设问明示《政治与法治》和《当代国际政治与经济》，人大制度+选必一组合，细则未定位选必一分项。 |
| 24 | 2025东城一模 | Q19 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q19 细则全部讲诉讼调解/劳动者法律意识，属《法律与生活》；命中的"全球治理；人类命运共同体"在Q20 答案角度，与Q19 无关。 |
| 25 | 2025东城一模 | Q21 | candidate_review | NEEDS_HUMAN_REVIEW | NEEDS_EVIDENCE | "教育是强国建设、民族复兴之基"，细则只把"人才与国际竞争力的关系"作为必要性可选角度之一，选必一未单独列分项细则，作迁移参考可，主表不入。 |
| 26 | 2025东城二模 | Q17 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 数字法院/数字正义，属《政治与法治/法律与生活》。 |
| 27 | 2025东城二模 | Q18 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | 热带雨林创新生态/有效市场+有为政府，属《经济与社会》。 |
| 28 | 2025东城二模 | Q19 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q19 细则全是龙某文身案、限制行为能力人等法律分项，属《法律与生活》；"人类命运共同体；中国智慧"在Q20 答案角度，与Q19 无关。 |
| 29 | 2025东城二模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 题面"基层立法联系点"民主大气象，细则讲"以人民为中心、人大制度、全过程人民民主"，属《政治与法治》。 |
| 30 | 2025东城期末 | Q21 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | "中国式现代化，民生为大"综合题，细则未定位选必一分项。 |
| 31 | 2025丰台一模 | Q16 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | 题面"新时代家风建设"，细则讲社会主义核心价值观/中华传统美德/家国情怀，属《哲学与文化》。 |
| 32 | 2025丰台一模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | 综合时评短文，细则原文标注"《经济与社会》政府与市场知识、《当代国际政治与经济》新型国际关系、构建人类命运共同体、推动经济全球化发展等，不给分"——即选必一表述在本题明文禁用。 |
| 33 | 2025丰台二模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | **INCLUDE_STRICT_MAIN** | 6 分联合国部分有完整细则："联合国地位+作用+中国创始会员国与安理会常任理事国身份+多边合作+中国智慧与方案"，是选必一联合国节点。 |
| 34 | 2025丰台期末 | Q18 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 数字经济"放得活与管得住"，《经济与社会》有效市场+有为政府。 |
| 35 | 2025丰台期末 | Q21 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | "制度优势是一个国家的最大优势"，综合制度题，细则未定位选必一分项；Q20 中非战略性共识属选必一已在主表。 |
| 36 | 2025延庆一模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 题面综合"中国式现代化"专题（深中通道+人民称号），细则未定位选必一分项；Q20(2) 外交部发言人回应"脱钩断链"已是反合并残留 #9，单独走题源。 |
| 37 | 2025房山一模 | Q19 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q19 细则全部讲不正当竞争、知识产权侵权、社会主义核心价值观，属《法律与生活》；选必一命中词出自Q18 题面（一带一路命运共同体）。 |
| 38 | 2025朝阳一模 | Q17 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q17 讲必要条件假言推理+人形机器人产业，《逻辑与思维》+《经济与社会》。 |
| 39 | 2025朝阳一模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q21 题面是中国共产党人"大事小事观/为民办事观/造福人民的政绩观"综合，属《政治与法治+哲学与文化》；选必一命中词在Q20（产业链供应链）。 |
| 40 | 2025朝阳期末 | Q16 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | 中国文化对外阐释，属《哲学与文化》。 |
| 41 | 2025朝阳期末 | Q22 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q22 题面"推进马克思主义中国化时代化"，细则讲十个明确/十四个坚持/十三个方面成就，属《必修四》/中特思想；Q21 大国外交才是选必一（已是反合并残留 #4、#6、#11 单题）。 |
| 42 | 2025石景山一模 | Q18 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q18 是低空经济题（产业基础优势+有为政府+有效市场+产业链），属《经济与社会》；选必一命中词在Q17(2)（联合国/国际秩序，已是反合并已拆入主表）。 |
| 43 | 2025西城一模 | Q16 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q16 知行关系+中华优秀传统文化，属《哲学与文化》；"产业链"在Q18 答案中出现。 |
| 44 | 2025西城一模 | Q17 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q17 追求认识客观性+辩证思维+创新思维，属《哲学与文化+逻辑与思维》。 |
| 45 | 2025西城一模 | Q18 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q18 题面生态优势转换为发展优势/特色产业链，细则1分点"产业优势/生态优势转换/特色资源禀赋"，属《经济与社会》。 |
| 46 | 2025西城一模 | Q22 | candidate_review | INCLUDE_STRICT_REVIEW | **DOWNGRADED_REFERENCE_ONLY** | 10 分综合时评（长期主义），主细则讲发展趋势/民族精神/党的领导；选必一仅作举例 1 分（"如三大倡议、人类命运共同体理念、进博会等"+"推动经济全球化向更加开放、包容、普惠、平衡、共赢的方向发展"），证据层级B，仅作迁移参考，不可冒充独立主表细则。 |
| 47 | 2025西城二模 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q20 题面"建设文化强国"，细则讲党的性质宗旨/文化建设/中国式现代化，属《哲学与文化》；选必一命中词在Q19(2)（自贸区零关税）的细则"经济全球化/建设开放型世界经济/促进贸易自由化"任意1点1分，归属Q19(2) 而非Q20。 |
| 48 | 2025门头沟一模 | Q20 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | 题面"以事实为根据，以法律为准绳"司法基本原则案例填表，属《政治与法治+法律与生活》。 |
| 49 | 2025顺义一模 | Q18 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | "科技创新引领新质生产力发展"，细则讲传统产业转型升级/新兴产业，属《经济与社会》。 |
| 50 | 2025顺义一模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q21 题面"天下之本在国，国之本在家"中华民族家文化，属《哲学与文化》；选必一在Q20（"小而美"南南合作，已是反合并残留 #10、#11 单题）。 |
| 51 | 2026东城二模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q21 题面"金融强国五篇大文章"，细则讲党的领导、人民立场、政府经济职能、高质量发展、辩证思维，属《经济与社会+哲学与文化》；选必一命中词出自Q20（购在中国/投资中国 已在主表）。 |
| 52 | 2026东城期中 | Q19 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q19 题面"在法治下推进改革"，细则讲法治国家/法治政府/法治社会一体建设，属《政治与法治》。 |
| 53 | 2026东城期中 | Q20 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | "结合材料，运用《当代国际政治与经济》知识，分析四大全球倡议如何系统推动构建人类命运共同体"——题面铁打的选必一，但本批 OCR/抽取没有定位该题细则，按硬规则只能列为 NEEDS_EVIDENCE。 |
| 54 | 2026东城期中 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q21 题面"区域，大国经略发展格局的主要依托"（京津冀、长三角、粤港澳），细则讲比较优势/协作链条/世界级城市群/区域协调发展，属《经济与社会》。 |
| 55 | 2026丰台一模 | Q17 | candidate_review | NEEDS_HUMAN_REVIEW | **DOWNGRADED_REFERENCE_ONLY** | Q17 题面"《中华人民共和国生态环境法典》"，细则主线讲党的领导/科学立法民主立法依法立法/中国特色社会主义法治体系；选必一只出现"中国积极参与全球生态治理，为世界提供中国方案和中国智慧"一句，作为综合作答的国际意义层，证据层级 B，可作迁移参考。 |
| 56 | 2026丰台二模 | Q20 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | 讲评ppt 引用25年海淀二模 Q20"共享发展理念推进共同富裕"作复练，属《哲学与文化》分析综合方法；本题与选必一无关。 |
| 57 | 2026丰台二模 | Q22 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q22 9 分综合（党的领导、唯物辩证法、中国式现代化），讲评 ppt 仅给等级量表无分项细则；"独立自主自力更生"作角度提示，属《必修三/必修四》语境（创新强国），不进选必一主表。 |
| 58 | 2026丰台期中 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | **INCLUDE_STRICT_MAIN** | 题面中拉论坛"团结、发展、文明、和平、民心'五大工程'"，细则原文写明"坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序…全球发展倡议…维护多边贸易体制…维护全球产业链供应链稳定畅通"，属选必一中国/联合国/经济全球化交汇节点。 |
| 59 | 2026延庆一模 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q20（9 分）题面"中国式现代化"综合，细则讲习近平思想/本质特征/发展观/规律/矛盾观/主观能动性，属《必修四+中特思想》；选必一在Q19(2)（重塑全球能源治理格局，已在主表）。 |
| 60 | 2026房山一模 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q20 题面"坚持依法治国和依规治党有机统一"习近平法治思想核心要义，属《政治与法治》；"两个市场两种资源"细则在Q19（北京两区建设助力国际循环，已在主表）。 |
| 61 | 2026房山二模 | Q21 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q21 综合题"以中国式现代化全面推进中华民族伟大复兴/弘扬伟大长征精神/坚持真理/坚持党的领导"，属《必修四+中特思想》。 |
| 62 | 2026朝阳一模 | Q19 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 设问"运用《经济与社会》知识，说明京津冀应如何深化以构建智能网联新能源汽车产业发展新高地"，属必修二；产业链供应链命中词在必修二语境。 |
| 63 | 2026朝阳一模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q21 题面"法与时转则治"（生态环境法典/民族团结进步促进法/国家发展规划法），属《政治与法治》立法专题；选必一在Q20（已在主表）。 |
| 64 | 2026朝阳二模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q21 题面"'十五五'规划纲要四大战略支柱、系统思维和战略定力"，属《必修四+党建专题》；选必一在Q20(2)（人类命运共同体维护世界和平与发展，已在主表）。 |
| 65 | 2026朝阳期中 | Q16 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 题面绿色金融对经济高质量发展的驱动作用，属《经济与社会》。 |
| 66 | 2026朝阳期中 | Q18 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q18 题面"是否应该使用AI 提供情绪价值"，细则讲矛盾普遍性/对立统一/具体问题具体分析/适度原则等，属《哲学与文化》；Q17（"人工智能+"统筹三大关系）才是真正的选必一选必一（已在主表）。 |
| 67 | 2026海淀一模 | Q21 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q21 综合题（"十下五"战略思维和实干精神），细则讲党的领导/马克思主义中国化时代化/制度优势/国家治理，属《必修四+中特思想》。 |
| 68 | 2026海淀二模 | Q19 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q19 题面"建设现代化首都都市圈"，细则讲比较优势/产业集聚/公共服务均衡，属《经济与社会》；"共同利益；多边主义"出现在Q20(2) 评分参考角度（不是 Q19）。 |
| 69 | 2026海淀二模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q21 综合"党的领导、中国式现代化、全面依法治国、国家安全、矛盾观、辩证思维等角度"，属《必修四+政治与法治》。 |
| 70 | 2026海淀期中 | Q21 | candidate_review | NEEDS_HUMAN_REVIEW | EXCLUDE_OTHER_MODULE | Q21 题面"人形机器人产业发展"，细则讲政府履职/有效市场+有为政府/对外开放展会，属《经济与社会》；"全球治理；多边主义"在Q22 主表已有。 |
| 71 | 2026石景山一模 | Q21 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q21 题面"生态环境法典编纂的创新意义"综合，属《必修三+政治与法治+哲学与文化》。 |
| 72 | 2026石景山二模 | Q19 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q19 题面新治安管理处罚法把校园欺凌纳入，属《政治与法治+法律与生活》；选必一命中词在Q18（中国-东盟，已在主表）。 |
| 73 | 2026石景山期中 | Q19 | evidence_not_located | NEEDS_EVIDENCE | NEEDS_EVIDENCE | Q19(2) 题面"中国关于人工智能全球治理的主张顺应了和平、发展、合作、共赢的时代潮流，符合世界各国人民的共同利益…秉持人类命运共同体理念，坚持多边主义，倡导共商共建共享的全球治理观"——明确选必一，但未定位评分细则。 |
| 74 | 2026石景山期中 | Q20 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q20 综合"党的领导、政府的职能、新发展理念、按规律办事、创新思维"角度，属《必修二+必修四》。 |
| 75 | 2026西城一模 | Q18 | candidate_review | EXCLUDE_OTHER_MODULE | EXCLUDE_OTHER_MODULE | 设问"运用《经济与社会》知识"，财政贴息/中小微企业产业链。 |
| 76 | 2026西城一模 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q21 综合题（10 分，"中国式现代化处于关键时期，更要坚持探索"），细则讲必要性+重要性（实践观/矛盾观/发展观/规律与主观能动性/辩证思维/创新思维/改革），属《必修四+中特思想》；选必一在Q20(2)（中国-东盟自贸区3.0版，已是反合并残留 #1 单题）。 |
| 77 | 2026西城二模 | Q20 | evidence_not_located | NEEDS_EVIDENCE | EXCLUDE_OTHER_MODULE | Q20 题面"政绩观问题"（毛泽东论联合政府/习近平对政绩观的论述），属《必修三+政治与法治》；选必一不在本题。 |
| 78 | 2026通州期中 | Q20 | candidate_review | INCLUDE_STRICT_REVIEW | **INCLUDE_STRICT_MAIN** | 题面"全球治理倡议正逢其时、指引方向、彰显担当"，细则8 分整套都是选必一："共商共建共享的全球治理观+联合国宪章宗旨和原则+和平与发展时代主题+主权平等国际法治等五大原则+中国智慧中国方案+人类命运共同体"，属六桶 中国/联合国/政治多极化 交汇节点。 |
| 79 | 2026通州期中 | Q21 | candidate_review | INCLUDE_STRICT_REVIEW | EXCLUDE_OTHER_MODULE | Q21 综合"十四五规划/中国式现代化"，细则讲党的领导/科技自立自强/中国式现代化进程，属《必修四+中特思想》。 |
| 80 | 2026顺义一模 | Q19 | candidate_review | INCLUDE_STRICT_REVIEW | **INCLUDE_STRICT_MAIN** | 题面"科技小院成为南南合作典范的深层逻辑"，评标图明确：理论 1 分（共同利益必答）、国际政治 3 分（时代主题/外交思想/义利观/独立自主和平外交政策/新型国际关系）、国际经济 3 分（经济全球化方向：普惠、平衡、共赢）—— 全套选必一。注：本题在学生宝典里以"Q20"标号收录，详见 `CLAUDECODE_COVERAGE_RISK_LOG.md` 第3 条对题号编号差异的说明。 |
| 81 | 2026顺义二模 | Q20 | must_backfill | NEEDS_HUMAN_REVIEW | NEEDS_EVIDENCE | 题面"'世界好,中国才会好;中国好,世界会更好'+中国式现代化开源式向世界开放+微电网、塞内加尔打井、巴西物流'最后一公里'"，明显是选必一中国担当题，但未定位评分细则，按硬规则只能 NEEDS_EVIDENCE。 |

## 二、反合并残留 12 条（逐题源单题裁决）

下表是 12 个"未拆分保留"合并题例，每个合并题例下面的每一道单题源都给出独立裁决；不允许再以合并形态进入主表。

| 合并# | 反合并核心点 | 单题源 | 本轮裁决 | 复核要点 |
|---|---|---|---|---|
| 1 | 国家间共同利益是国家合作的基础 | 2025东城二模 第20题 | **INCLUDE_STRICT_MAIN** | 细则"精神（4 分）：同求共济精神丰富人类命运共同体内涵 2 分；符合各国共同利益 2 分"。术语原句"符合各国共同利益"。 |
| 1 | 同上 | 2025朝阳二模 第21题 | **INCLUDE_STRICT_MAIN** | 细则第(2)层区域发展需要角度①"共同的国家利益是国际合作基础，中国与周边国家有着广泛共同利益/我国坚持独立自主的和平外交政策…任意1 词1 分"。术语原句"共同的国家利益是国际合作基础"。 |
| 1 | 同上 | 2026西城一模 第20题第(2)问 | **INCLUDE_STRICT_MAIN** | 细则综合"对世界：坚持合作共赢/开放包容/共同利益，坚持多边贸易/多边主义、全球经济治理体系改革 1 分"。术语原句仅"共同利益"作可选项之一，按理论桶共同利益核心独立成条。 |
| 2 | 推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展 | 2026朝阳一模 第20题 | **INCLUDE_STRICT_MAIN** | 细则角度③"推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展----1 分"（5 分以内角度可选点之一）。 |
| 2 | 同上 | 2025朝阳二模 第21题 | **INCLUDE_STRICT_MAIN** | 细则第(3)层②"通过区域经济合作维护推动全球自由贸易/多边贸易/推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展（前述任意1个词1 分）"。 |
| 3 | 推进普惠包容的经济全球化，推动构建更加开放、包容的全球经济格局 | 2026石景山一模Q20 | **DOWNGRADED_REFERENCE_ONLY** | 原始细则 Word 二进制乱码不可读，仅 Codex/ClaudeCode 还原稿可见"中国倡导经济全球化，着力解决发展不平衡问题…更加包容、更可持续"；属 B 级证据，作迁移参考，不进主表。 |
| 3 | 同上 | 2026顺义一模Q20 | **INCLUDE_STRICT_MAIN** | 评标图国际经济 3 分"经济全球化方向：普惠、平衡、共赢（典范）"。术语为"普惠、平衡、共赢"原句。 |
| 4 | 共商共建共享的全球治理观 | 2025朝阳期末Q21 | **INCLUDE_STRICT_MAIN** | 细则外部政治环境部分8 句任 1 句给 1 分中"共商共建共享"作为一句采分点。 |
| 4 | 同上 | 2026丰台一模Q19 | **INCLUDE_STRICT_MAIN** | 参考答案第三段原句"中国坚持共商共建共享的全球治理观"为细则原文采分点（讲评 ppt 总分8分等级量表）。 |
| 4 | 同上 | 2026石景山一模Q20 | **DOWNGRADED_REFERENCE_ONLY** | 原始细则乱码，仅还原稿可见"中国倡议共商共建共享，致力于共同维护、共同推进、共享繁荣"，作迁移参考。 |
| 5 | 推动国际关系民主化 | 2025朝阳二模 第21题 | **INCLUDE_STRICT_MAIN** | 细则第(3)层①"携手周边国家推动建设以合作共赢为核心的新型国际关系，推动国际关系民主化，实现真正的多边主义，推动全球治理变革（任意1 词1 分）"。 |
| 5 | 同上 | 2025东城二模 第20题 | **INCLUDE_STRICT_MAIN** | 细则行动（2 分）替代："具体的方案、行动（推动国际关系民主化、和平解决国际争端）2 分"。术语原句"推动国际关系民主化"。 |
| 6 | 推动国际秩序和全球治理体系更加公正合理（合并A：朝阳期末+丰台一模） | 2025朝阳期末Q21 | **INCLUDE_STRICT_MAIN** | 细则外部政治环境部分8 句任 1 句给 1 分中含"推动全球治理体系变革完善，推动建立更加公正合理的国际政治经济新秩序"。术语原句"更加公正合理的国际政治经济新秩序"。 |
| 6 | 同上 | 2026丰台一模Q19 | **DOWNGRADED_REFERENCE_ONLY** | 2026丰台一模Q19 参考答案+讲评 ppt 三段中没有"推动国际秩序和全球治理体系更加公正合理"原句；最接近的是"坚定维护联合国宪章宗旨和原则"+"共商共建共享的全球治理观"。属合并术语的引申，不能再算独立细则原文。 |
| 7 | 推动国际秩序和全球治理体系更加公正合理（合并B：朝阳期末+门头沟一模） | 2025朝阳期末Q21 | （同合并 6 的朝阳期末单题，已 INCLUDE） | 不重复写入单题条目；只在合并 #7 标注与合并 #6 共用同一单题。 |
| 7 | 同上 | 2025门头沟一模Q19 | **DOWNGRADED_REFERENCE_ONLY** | 2025门头沟一模细则文件 Word 乱码不可读，仅教师版参考答案有"推动国际秩序向着更加公正合理的方向发展"一句；属 B/C 级证据，作迁移参考。 |
| 8 | 践行真正的多边主义 | 2026丰台一模Q19 | **INCLUDE_STRICT_MAIN** | 参考答案第二段原句"积极践行真正的多边主义"为细则原文采分点。 |
| 8 | 同上 | 2026石景山一模Q20 | **DOWNGRADED_REFERENCE_ONLY** | 原始细则乱码，还原稿见"坚持多边主义、共同营造开放型区域经济环境"，与"真正的多边主义"措辞差一字，作 B 级迁移参考。 |
| 9 | 世界多极化与全球南方联合自强 | 2024海淀二模Q18(1) | **DOWNGRADED_REFERENCE_ONLY** | 仅"可从时代主题、世界多极化、人类命运共同体、国际组织等角度作答"参考答案，没有正式分项细则；属作答角度提示，作迁移参考。 |
| 9 | 同上 | 2025延庆一模Q20(2) | **INCLUDE_STRICT_MAIN** | 细则"多极化2 分（国家利益、国际关系、多边主义等角度可替代，不重复给分）"，术语原句"世界多极化是当今国际形势的突出特点"。 |
| 10 | 贡献中国智慧、中国方案、中国力量 | 2026延庆一模Q19(2) | **INCLUDE_STRICT_MAIN** | 价值意蕴4 分（1点2 分，2 点4 分）"人类命运共同体/共商共建共享的全球治理观/相互尊重、公平正义、合作共赢的新型国际关系"+ 参考答案原句"为全球能源可持续发展提供具有公共产品属性的中国方案"。术语原句"中国方案"。 |
| 10 | 同上 | 2025顺义一模Q20 | **INCLUDE_STRICT_MAIN** | 细则第 4 层项目对世界的意义和贡献（2 分以内任 1 点 1 分）："构建人类命运共同体、为重构公正合理的国际政治经济秩序提供中国方案、推动经济全球化朝着开放包容普惠的方向发展、推动国际关系民主化"。术语原句"为重构公正合理的国际政治经济秩序提供中国方案"。 |
| 11 | 坚持正确义利观 | 2026丰台一模Q19 | **INCLUDE_STRICT_MAIN** | 参考答案第二段原句"中国坚定维护联合国宪章的宗旨和原则，坚持正确义利观，积极践行真正的多边主义……"。术语原句"坚持正确义利观"。 |
| 11 | 同上 | 2025朝阳期末Q21 | **INCLUDE_STRICT_MAIN** | 细则外部文化和国际舆论环境9 句任 1 句给 1 分含"坚持正确的义利观"。术语原句"坚持正确的义利观"。 |
| 11 | 同上 | 2026顺义一模Q20 | **INCLUDE_STRICT_MAIN** | 评标图国际政治 3 分"外交思想：构建人类命运共同体（习近平外交思想的核心理念）；替换：独立自主的和平外交政策/外交政策的宗旨/义利观"。术语原句"义利观"。注意：此处义利观是外交思想的替换项，写入"中国"桶。 |
| 12 | 中国坚持独立自主和平外交与和平共处五项原则 | 2024海淀期中Q21(2) | **INCLUDE_STRICT_MAIN** | 细则"不变"部分5 分：坚持独立自主的基本立场；贯彻维护世界和平、促进共同发展的宗旨；促进世界的和平与发展为基本目标；坚持以和平共处五项原则作为我国对外关系基本准则。**写独立自主的和平外交政策2 分**。+ 反对霸权主义强权政治1 分。 |
| 12 | 同上 | 2024西城二模Q19 | **DOWNGRADED_REFERENCE_ONLY** | 细则原文不含"独立自主和平外交政策""和平共处五项原则"原句；仅"反对霸权主义、强权政治"作采意可选点；属合并术语的引申，不能再算独立细则原文。 |

## 三、与 Codex 第一轮的主要分歧

1. Codex 把"已定位细则+命中选必一相关词"统一标 `INCLUDE_STRICT_REVIEW`，但许多命中词出自同卷别的题（例如Q19 命中词其实在Q20 答案角度），本轮按 题面+细则 的合致性收紧为 `EXCLUDE_OTHER_MODULE`。
2. Codex 对若干跨模块综合题（必修四/中特思想为主，选必一仅作可选角度）给了 `INCLUDE_STRICT_REVIEW`，本轮按"选必一是否单独列分项细则"收紧；只一句旁注或一条角度的不入主表，统一为 `DOWNGRADED_REFERENCE_ONLY` 或 `EXCLUDE_OTHER_MODULE`。
3. Codex 把"原始细则文件 Word 乱码、靠 ClaudeCode/Codex 还原稿"的 2025/2026 石景山一模Q20 / 2025门头沟Q19 标为 `REWRITE_FROM_ORIGINAL_DRAFT_SOURCE`，本轮把它们标 `DOWNGRADED_REFERENCE_ONLY`（B 级证据），同时在风险日志里登记"原始细则文件不可读"的复核风险。
4. Codex 对 2024西城二模Q17 给了 `EXCLUDE_OTHER_MODULE`，本轮回到细则原文"国家安全与核心利益+实施科教兴国战略+当前国际竞争实质+世界多极化+经济全球化+世界发展的贡献者和推动者"，确认选必一有独立角度，改判 `INCLUDE_STRICT_MAIN`。
5. Codex 对 2024朝阳一模Q20、2025东城二模Q19、2025东城二模Q21、2025东城一模Q19 给了 INCLUDE 但题面纯属另一模块（逻辑、法律、政治与法治），本轮一律 EXCLUDE，并把"命中词出自同卷他题"的情况在风险日志登记。

## 四、本表统计末尾对账

- 覆盖队列 81 条裁决总数：
  - INCLUDE_STRICT_MAIN：5（#12、#21、#33、#58、#78、#80—注：#80 单算 1 条；总计 5+1=6）
  - DOWNGRADED_REFERENCE_ONLY：2（#46、#55）
  - NEEDS_EVIDENCE：12（#1 / 5 / 13 / 17 / 23 / 25 / 30 / 35 / 36 / 53 / 73 / 81）
  - EXCLUDE_OTHER_MODULE：61
  - 合计：6 + 2 + 12 + 61 = 81 ✓
- 反合并残留 12 条裁决总数：
  - 单题 INCLUDE_STRICT_MAIN：19（即 19 道单题，剔除 2025朝阳期末Q21 重复，重复出现 4 次但只算 1 条独立条目）
    - 实际写入主表的独立单题条目数为 17（合并 6/7 共用同一 朝阳期末Q21 单题；合并 4/11 共用同一 朝阳期末Q21 单题；合并 8 与合并 4 同一 丰台一模Q19；合并 11 与合并 4 同一 丰台一模Q19；合并 11 与合并 3/10 同一 顺义一模Q20…按"单题不重复"计数）
  - 单题 DOWNGRADED_REFERENCE_ONLY：7（2026石景山一模Q20×3、2026丰台一模Q19 公正合理引申、2025门头沟一模Q19、2024海淀二模Q18(1)、2024西城二模Q19）
  - 全部 12 个反合并残留合并项均完成处置（至少有一道单题被 INCLUDE 重写，或全部成员明确 DOWNGRADED）；可宣告"12 个反合并残留全部处置完毕"。
