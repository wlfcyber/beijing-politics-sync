BEGIN_REVIEW_INSTRUCTIONS
# External Review Context
You are GPT-5.5 Pro doing one chunk of a formal web/app review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is v23. Local QA reports:
- Empty rubric-marker suspects in both Markdown files: 0.
- DOCX XML scan found 0 occurrences of local paths or image-path traces.
- Rendered successfully: 汇编 85 pages, 宝典 93 pages.
- Student-facing DOCX files embed no whole-page source screenshots; source/rubric images remain backend evidence only.
- Rendered-PDF OCR scan found no `元首外交`, paper footer, backend trace, or prior OCR-pollution terms.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

v23 inherits the v10 fixes for the valid GPT-5.5 Pro web review failure from v9 compilation-01, and additionally fixes the valid GPT-5.5 Pro web review failure from v10 compilation-03:
- 2026 朝阳期末18(1): cleaned material/rubric/answer points for the online consumption contract case.
- 2026 朝阳二模18: restored three legal Q&A blanks and the rights-protection answer points.
- 2026 通州期末19(1): restored Civil Code Article 292 and Article 296 legal basis.
- 2026 通州一模20: cleaned severe OCR damage in parties, court, liability, and public-place text.
- 2026 门头沟一模18(1): removed empty trailing rubric marker.
- 2026 房山二模17: removed duplicated/half scoring language from answer points.
- 2026 西城二模18(1)(2): cleaned AI/court/rubric OCR wording.
- 2026 顺义一模18 and 顺义二模18(2): added shared-value and governance-risk answer angles.
- Render QA also changed the Chinese font to Hiragino Sans GB so E049 `稳步前行` renders without dropped glyphs.

v23 specifically fixes the valid Claude Opus 4.8 Max Safari web/app review failure from v11:
- 2024 朝阳二模17: removed `原答案：`, `辩`, `实社社会` and other OCR/editorial pollution; rewrote answer points as clean student-facing bullets.
- 2026 房山二模18(1): moved the AI legal-risk item from A1 to A5 知识产权与公平竞争, with a note that it also involves 名誉权.

v23 also applies a post-Claude cleanup pass for small nonblocking OCR/text defects:
- 2025 东城二模19: `钱某事限制民事行为能力人` -> `钱某是限制民事行为能力人`.
- 2025 东城期末19(1): `建车栩会占用绿地` -> `建车棚会占用绿地`.
- 2025 丰台二模19(2): `参考答 案` -> `参考答案`.
- 2025 丰台期末19: `法院驳回了尹荣的诉讼请求` -> `法院驳回了尹某的诉讼请求`.
- 2026 丰台一模20: `低头看手机 监控画面` -> `低头看手机。监控画面`.
- 2026 丰台二模18: `予盾化解` -> `矛盾化解`.

v23 additionally fixes the valid GPT-5.5 Pro web/app v13 compilation-01 concerns around screenshot spillover and answer-point residue:
- E002 answer points now expose both the 甲公司 and 乙公司 litigation paths within the visible student-facing answer points.
- Student-facing documents no longer embed full-page `原题图` or `细则图`; this removes whole-page screenshot spillover such as the 2025 东城一模第19题 source image carrying Q20 `元首外交` non-Xuanbier material.
- Backend source-image assets are still retained under QA for local verification, but the two student documents are text-only.

v23 also responds to the GPT-5.5 Pro web/app v16 compilation-01 review:
- Locally verified that the named entries still contain the required `题目来源/材料/设问/细则/答案落点/同题组` fields.
- Rewrote student-facing answer points for 2024 石景山一模17, 2024 西城二模16, 2025 东城期末19(1), 2025 东城二模19, and 2025 房山一模19 so raw `细则/替换/变通` residue does not appear in 答案落点.
- GPT chunks are now smaller to reduce cross-entry conflation in web review.

v23 additionally fixes two issues surfaced while adjudicating the v17 web/app first-chunk result:
- 2024 东城一模19: `李某 郭某出具欠据` -> `李某为郭某出具欠据`, confirmed against the earlier formal accepted source text.
- 2024 东城二模19(1): scoring wording now says `乙公司作出肯定答复（材料表述为“可以”）`, avoiding a visible `可以/好的` mismatch for students.
- The previous v17 first-chunk GPT result is not used for closure because browser input-state evidence showed prompt ordering corruption. This package uses smaller chunks and plain BEGIN/END delimiters instead of Markdown code fences.

v23 also fixes the valid GPT-5.5 Pro web/app v18 compilation-01 review:
- 2024 丰台一模17: restored the full reality-meaning scoring chain, including maintaining social fairness, interpersonal harmony, socialist core values, reducing traffic congestion, and advocating green travel.
- 2024 东城二模19(2): changed the visible rubric score label from whole-question `19.（9分）` to this subquestion `19（2）（2分）`.
- 2024 东城一模19: removed the score label from the student-facing answer points while preserving the formal rubric score line.

v23 additionally repairs issues surfaced while adjudicating the v19 web/app first-chunk result:
- Local source/render/OCR contradicted the v19 GPT blocker about 2024 丰台一模17 material fracture; this is recorded as web-input contamination, not a document defect.
- 2024 朝阳一模19: removed the answer-point score-label residue while preserving the formal rubric score line.
- Applied a global answer-point cleanup layer to remove leading question-number / score shells from student-facing answer-point bullets while preserving formal rubric text.
- 2026 延庆一模18(1): replaced a whole-rubric answer-point dump with seven clean student-facing answer points.
- v23 Markdown and OCR scans found no backend/web prompt traces and no answer-point bullets beginning with score shells.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
END_REVIEW_INSTRUCTIONS


# Chunk Task
Document: 试题和细则汇编
Chunk: 8/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-08
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2025 · 门头沟 · 一模 · 第20题

- 题目来源：2025 · 门头沟 · 一模 · 第20题
- 同题组：本题组仅本分问。

#### 材料
“以事实为根据，以法律为准绳”是我国司法活动的基本原则，核心是通过客观事实认真严格依
照法律规定作出裁判，确保司法公正性与权威性。
案件事实 裁判要点
裁判结果：支持A公司的诉讼请求，B公司、C公
司应停止侵害，删除相关内容并赔偿A公司经济损失。
案例一 A享有“我不是胖虎”系列美
裁判理由：根据《中华人民共和国著作权法》的规
术作品的复制权、改编权、信息网络传播权
定，著作权人对其作品享有广泛的权利。他人未经著作
等著作财产性权利。B公司、C公司未经许
权人许可使用著作权人的作品，就可能构成侵权。B公
可，在其经营的微博账号中发布了与A公司
司、C公司未经许可，擅自将被诉侵权图片作为微博图
“我不是胖虎”类似电脑壁纸“橘猫”。A
片发布，使公众可以在其个人选定的时间和地点获得作
公司向法院起诉B公司、C公司，要求其承
品，均侵害了A公司的著作权。
担侵权责任。
现实意义：该判决充分保障了著作权人的合法权
益，规范了企业行为。
案例二 孙某在2022年4月应聘甲公
司，所投简历写明：2015年7月至2022年3
月期间有4段工作经历。后孙某入职甲公 裁判结果①
司，同日双方签订了劳动合同，并约定了试 裁判理由②
用期。入职后经甲公司查证，孙某在2015年 现实意义③
毕业后的7年时间，曾在17家公司任职，甲
公司以孙某未如实提供工作经历为由，在试
用期将其辞退。孙某向法院起诉，请求法院
判决甲公司支付违法解除劳动关系赔偿金。

#### 设问
请结合以下案例，参照所给出完成下表。

#### 细则
20（1）裁判结果：驳回或不支持孙某诉讼请求（1分），甲公司无需支付赔偿金（1分）。
20（2）裁判理由共4分：
①法律规定1分，写出订立劳动合同应遵循诚实信用原则即可得1分；或根据《劳动合同法》，以欺诈手段订立的劳动合同无效或者部分无效。
②孙某违反诚实信用原则、违反劳动者基本职业道德或侵犯甲公司知情权（1分）。
③甲公司在违背真实意思的情况下与孙某签订合同，或劳动合同无效（1分）。
④甲公司提出解除劳动关系符合法律规定，解除劳动关系并无不妥或行为无过错（1分）。
20（3）现实意义共3分：
①维护用人单位合法权益（1分）。
②约束劳动者行为，有利于劳动者遵守职业道德（1分）。
③有利于和谐劳动关系的构建，有利于弘扬诚信的社会主义核心价值观，或维护社会公平正义（1分）。

#### 答案落点
- 裁判结果：驳回或不支持孙某诉讼请求，甲公司无需支付违法解除劳动关系赔偿金。
- 订立劳动合同应遵循诚实信用原则；或以欺诈手段订立的劳动合同无效或者部分无效。
- 孙某隐瞒多段工作经历，违反诚实信用原则、劳动者基本职业道德或侵犯甲公司知情权。
- 甲公司在违背真实意思的情况下与孙某签订合同，劳动合同可认定无效或部分无效。
- 甲公司在试用期解除劳动关系符合法律规定，解除行为并无不妥或无过错。
- 该裁判有利于维护用人单位合法权益，约束劳动者行为，构建和谐劳动关系，弘扬诚信价值。

### 2025 · 顺义 · 一模 · 第19题第1问

- 题目来源：2025 · 顺义 · 一模 · 第19题第1问
- 同题组：2025 · 顺义 · 一模 · 第19题第1问；2025 · 顺义 · 一模 · 第19题第2问

#### 材料
法者，所以兴功惧暴也；律者，所以定分止争也；令者，所以令人知事也。
材料一
案例1 高某与刘某为邻居。刘某一家经常在门口堆放杂物及生活垃圾。高某跟刘某沟通过多次，要求其清除杂物及垃圾，对方均不予理会，饱受困扰的高某曾找过物业、在微信群反映，刘某依旧我行我素，还在微信群内辱骂高某。高某将刘某诉至法院，经法院调解，刘某向高某表达了歉意，双方握手言和。
案例2 甲公司从事娱乐、游戏、动漫产业几十年，其品牌已经具有较高知名度和显著性。乙公司经营范围为动漫游戏、动漫、游艺用品销售等，其将企业名称变更登记为与甲公司相似的名称。甲公司认为该名称存在侵权，向市场监督管理局（以下简称市监局）提出《请求企业名称争议裁决》申请，市监局确认乙公司的名称侵犯甲公司公司合法权益，应予以纠正。乙公司不服市监局裁决，提起诉讼，法院驳回乙公司诉讼请求。

#### 设问
(1)运用《法律与生活》知识，分析上述案例是如何解决纠纷的。
案例1:
案例2:

#### 细则
（1）评分细则：
案例1：解决纠纷方式：法院坚持诉讼调解，实现邻里和谐、实质化解纠纷。（1分）
理由：通道为公共通行的通道，属于建筑物的共有部分，应当在合理限度内恰当使用；刘某为自家方便堆放垃圾和杂物，不仅影响邻居通行，存在重大安全隐患，而且违反民法典关于相邻权的规定，也有违邻里之间和谐相处的文化传统。（1分）
要求：不动产的相邻各方要按照有利于生产、方便生活、团结互助、公平合理的原则，正确处理通风、采光、通行等相邻关系；给相邻方造成妨碍的，应当主动排除妨碍。（1分，可替换为正确处理相邻关系、遵守民法典相关原则）
案例2：事实分析：甲公司对字号使用在先，该字号在中国市场已经具有较高知名度和显著性；乙公司擅自将该字号登记为企业名称使用，主观上具有攀附他人已经建立的商业信誉的故意，造成公众混淆，损害甲公司的商业信誉，影响其品牌形象和市场份额，同时对消费者构成欺诈，损害社会公共利益。（1分）
性质认定：乙公司行为属于不正当竞争，可替换为“搭便车”或违反公平原则。（1分）
解决纠纷方式：市监局作出的裁决证据确实充分，适用法律法规正确，法院遂判决驳回乙公司诉讼请求。（1分）

#### 答案落点
- 案例1通过法院诉讼调解解决邻里纠纷，实现邻里和谐、实质化解纠纷。
- 公共通道属于建筑物共有部分，刘某堆放垃圾杂物影响通行、存在安全隐患，违反相邻权规则和邻里和谐传统。
- 相邻各方应按照有利生产、方便生活、团结互助、公平合理原则正确处理相邻关系，造成妨碍应主动排除。
- 案例2中，甲公司对字号使用在先并具有较高知名度和显著性。
- 乙公司擅自将相似字号登记为企业名称，具有攀附他人商业信誉的故意，造成公众混淆并损害甲公司商业信誉和公共利益。
- 乙公司行为属于不正当竞争；市监局裁决证据充分、适用法律正确，法院判决驳回乙公司诉讼请求。

### 2025 · 顺义 · 一模 · 第19题第2问

- 题目来源：2025 · 顺义 · 一模 · 第19题第2问
- 同题组：2025 · 顺义 · 一模 · 第19题第1问；2025 · 顺义 · 一模 · 第19题第2问

#### 材料
法者，所以兴功惧暴也；律者，所以定分止争也；令者，所以令人知事也。
材料一
案例1 高某与刘某为邻居。刘某一家经常在门口堆放杂物及生活垃圾。高某跟刘某沟通过多次，要求其清除杂物及垃圾，对方均不予理会，饱受困扰的高某曾找过物业、在微信群反映，刘某依旧我行我素，还在微信群内辱骂高某。高某将刘某诉至法院，经法院调解，刘某向高某表达了歉意，双方握手言和。
案例2 甲公司从事娱乐、游戏、动漫产业几十年，其品牌已经具有较高知名度和显著性。乙公司经营范围为动漫游戏、动漫、游艺用品销售等，其将企业名称变更登记为与甲公司相似的名称。甲公司认为该名称存在侵权，向市场监督管理局（以下简称市监局）提出《请求企业名称争议裁决》申请，市监局确认乙公司的名称侵犯甲公司公司合法权益，应予以纠正。乙公司不服市监局裁决，提起诉讼，法院驳回乙公司诉讼请求。
材料二 定分止争——案结事了人和，让公平正义充分彰显。司法裁判的最高境界，从来不是简单的胜败之争，而是以“和合”之力让公平正义在人与人相互理解的土壤中生根发芽，绽放出绚烂的人性之花。

#### 设问
(2)结合材料一与材料二，运用法治知识，阐释定分止争的价值。

#### 细则
19（2）
参考答案：民事主体行使民事权利不得超过正当界限，不得损害国家、社会、他人合法权益；在解决纠纷中，公民既要有维权意识，又要选择适当途径解决纠纷践行文明、和谐的社会主义核心价值观。坚持多元纠纷解决机制，支持人们理性表达诉求、依法维护权益，社会形成尊法学法守法用法的氛围，增进社会共识，维护社会秩序；通过适当的解决纠纷机制之间协调运行，能更好协调各方利益，有效化解社会矛盾，实现社会和谐，提升社会治理水平。
阅卷细则：
对个人的价值：维护(企业）公民的合法权益/ 增强公众对法律的信任和遵守意识(2分）
对企业的价值：保护企业的合法权益/规范市场主体的行为(促进企业依法、诚信经营）/维护公平的市场竞争秩序（两个合法权益不重复给分）（2分）
对社会的价值：化解社会矛盾/促进社会和谐/维护社会秩序/促进公平正义/提升社会治理水平（2分）
1个角度2分，2个角度4分，3个角度5分，满分不超过5分

#### 答案落点
- 19（2）参考答案：民事主体行使民事权利不得超过正当界限，不得损害国家、社会、他人合法权益；
- 在解决纠纷中，公民既要有维权意识，又要选择适当途径解决纠纷践行文明、和谐的社会主义核心价值观。
- 坚持多元纠纷解决机制，支持人们理性表达诉求、依法维护权益，社会形成尊法学法守法用法的氛围，增进社会共识，维护社会秩序；
- 通过适当的解决纠纷机制之间协调运行，能更好协调各方利益，有效化解社会矛盾，实现社会和谐，提升社会治理水平。
- 阅卷细则：对个人的价值：维护(企业）公民的合法权益/ 增强公众对法律的信任和遵守意识(2分）对企业的价值：保护企业的合法权益/规范市场主体的行为(促进企业依法、诚信经营）/维护公平的市场竞争秩序（两个合法权益不重复给分）（2分）对社会的价值：化解社会矛盾/促进社会和谐/维护社会秩序/促进公平正义/提升社会治理水平（2分）1个角度2分，
- 2个角度4分，3个角度5分，满分不超过5分

### 2026 · 东城 · 一模 · 第18题

- 题目来源：2026 · 东城 · 一模 · 第18题
- 同题组：本题组仅本分问。

#### 材料
人民法院以司法之力守护“向新力”。
案例一 某科技公司三名创始人，因专利权归属纠纷，陷入长期诉讼，公司发展因此停滞。对此，办
案合议庭没有“一判了之”，而是居中斡旋，弥合分歧。当事人最终达成和解，全身心投入创新创业，实
现了多方共赢。
案例二 甲公司系某水稻植物新品种的权利人。乙公司擅自将甲公司享有植物新品种权的稻种更换包
装后对外销售。经人民法院查明，乙公司侵权行为覆盖范围广。人民法院判令乙公司立即停止侵害，并对
其适用惩罚性赔偿，赔偿甲公司经济损失300万元。
案例三 丙公司资金运转困难，又得知丁公司处于上市关键期，遂以丁公司生产的机器狗侵犯其专利
权为由，向人民法院提起诉讼，索赔诉求反复变更。人民法院综合考量丙公司起诉时机、诉讼请求反复无
常、缺乏依据等情形，依法驳回其全部诉讼请求，并明确谴责丙公司的恶意诉讼行为。

#### 设问
结合材料，运用《法律与生活》知识，谈谈法院是如何以司法之力守护“向新力”的。

#### 细则
18.（8分）人民法院以司法之力守护“向新力”。
案例一：诉讼调解（1分，可替代为“调解”）；推动纠纷实质性化解，表达出“解决问题”，或体现以和为贵、法德结合、效率高、节约司法资源（1分）。
案例二：惩罚性赔偿，严惩主观恶性强、社会危害大的知识产权侵权，增加侵权成本（1分）；发挥警示规范作用，保护当事人合法权益，维护市场秩序、诚信原则、公平竞争或公平正义（1分）。注意：不是混淆行为“搭便车”。
案例三：驳回并谴责恶意诉讼、滥用诉讼权利的行为（1分）；贯彻诚信原则，明确权利行使界限、权利义务统一，维护诉讼秩序或司法秩序，节约司法资源（与案例一不重复给，1分）。注意：不是商业诋毁、不正当竞争。
总说：法院公正司法，以事实为依据、以法律为准绳，发挥司法裁判导向作用（1分）；保护知识产权就是保护创新，提升创新活力（1分）。

#### 答案落点
- 案例一：诉讼调解；推动纠纷实质性化解，体现以和为贵、法德结合、效率高或节约司法资源。
- 案例二：适用惩罚性赔偿，严惩主观恶性强、社会危害大的知识产权侵权，增加侵权成本。
- 案例二：发挥警示规范作用，保护当事人合法权益，维护市场秩序、诚信原则、公平竞争或公平正义。
- 案例三：驳回并谴责恶意诉讼、滥用诉讼权利的行为。
- 案例三：贯彻诚信原则，明确权利行使界限和权利义务统一，维护诉讼秩序或司法秩序，节约司法资源。
- 总说：法院公正司法，以事实为依据、以法律为准绳，发挥司法裁判导向作用。
- 总说：保护知识产权就是保护创新，提升创新活力。

### 2026 · 东城 · 二模 · 第19题

- 题目来源：2026 · 东城 · 二模 · 第19题
- 同题组：本题组仅本分问。

#### 材料
法治是最好的营商环境。大健康产业蓬勃发展，需要企业规范深耕。
甲公司开拓新领域，打造“中药＋餐饮＋健康检测”一站式新型养生空间。为加速项目落地，甲公司开启对外招商，锁定乙、丙两家公司作为候选合作伙伴。
乙公司为在竞争中胜出，捏造事实向甲公司项目负责人张某暗示丙公司的管理能力、产品质量低下。张某信以为真，在未经查证的情况下，违规直接与乙公司签订承包合同。后乙公司进场施工，因管理混乱导致项目严重延期。甲公司因此遭受重大经济损失。

#### 设问
结合材料，运用《法律与生活》知识，评析乙公司和张某的行为。

#### 细则
2025-2026 东城高三政治综合练习（二）主观题细则
乙公司：以商业诋毁获取竞争优势（2分）；可替代为构成不正当竞争，或违背诚信原则（1分）。未全面履行合同，构成违约（1分）；应承担赔偿损失等违约责任（1分）。市场主体应坚持依法诚信经营（1分，与诚信原则不重复给）。
张某：未遵守劳动纪律与职业道德（2分）。劳动者权利与义务相统一，劳动者应履行义务（1分，可与乙公司依法诚信经营互替）。
总说：市场经济就是法治经济，应共同营造公平竞争的市场环境（1分）。

#### 答案落点
- 乙公司以商业诋毁获取竞争优势，构成不正当竞争，也违背诚信原则。
- 乙公司未全面履行合同，构成违约，应承担赔偿损失等违约责任。
- 市场主体应坚持依法诚信经营。
- 张某未遵守劳动纪律与职业道德。
- 劳动者权利与义务相统一，劳动者应履行相应义务。
- 市场经济就是法治经济，应共同营造公平竞争的市场环境。
END_CHUNK_CONTENT
