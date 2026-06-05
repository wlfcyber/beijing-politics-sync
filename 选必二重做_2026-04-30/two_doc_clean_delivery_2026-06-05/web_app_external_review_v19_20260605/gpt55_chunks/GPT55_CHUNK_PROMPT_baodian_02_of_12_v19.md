BEGIN_REVIEW_INSTRUCTIONS
# External Review Context
You are GPT-5.5 Pro doing one chunk of a formal web/app review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is v19. Local QA reports:
- Empty rubric-marker suspects in both Markdown files: 0.
- DOCX XML scan found 0 occurrences of local paths or image-path traces.
- Rendered successfully: 汇编 86 pages, 宝典 93 pages.
- Student-facing DOCX files embed no whole-page source screenshots; source/rubric images remain backend evidence only.
- Rendered-PDF OCR scan found no `元首外交`, paper footer, backend trace, or prior OCR-pollution terms.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

v19 inherits the v10 fixes for the valid GPT-5.5 Pro web review failure from v9 compilation-01, and additionally fixes the valid GPT-5.5 Pro web review failure from v10 compilation-03:
- 2026 朝阳期末18(1): cleaned material/rubric/answer points for the online consumption contract case.
- 2026 朝阳二模18: restored three legal Q&A blanks and the rights-protection answer points.
- 2026 通州期末19(1): restored Civil Code Article 292 and Article 296 legal basis.
- 2026 通州一模20: cleaned severe OCR damage in parties, court, liability, and public-place text.
- 2026 门头沟一模18(1): removed empty trailing rubric marker.
- 2026 房山二模17: removed duplicated/half scoring language from answer points.
- 2026 西城二模18(1)(2): cleaned AI/court/rubric OCR wording.
- 2026 顺义一模18 and 顺义二模18(2): added shared-value and governance-risk answer angles.
- Render QA also changed the Chinese font to Hiragino Sans GB so E049 `稳步前行` renders without dropped glyphs.

v19 specifically fixes the valid Claude Opus 4.8 Max Safari web/app review failure from v11:
- 2024 朝阳二模17: removed `原答案：`, `辩`, `实社社会` and other OCR/editorial pollution; rewrote answer points as clean student-facing bullets.
- 2026 房山二模18(1): moved the AI legal-risk item from A1 to A5 知识产权与公平竞争, with a note that it also involves 名誉权.

v19 also applies a post-Claude cleanup pass for small nonblocking OCR/text defects:
- 2025 东城二模19: `钱某事限制民事行为能力人` -> `钱某是限制民事行为能力人`.
- 2025 东城期末19(1): `建车栩会占用绿地` -> `建车棚会占用绿地`.
- 2025 丰台二模19(2): `参考答 案` -> `参考答案`.
- 2025 丰台期末19: `法院驳回了尹荣的诉讼请求` -> `法院驳回了尹某的诉讼请求`.
- 2026 丰台一模20: `低头看手机 监控画面` -> `低头看手机。监控画面`.
- 2026 丰台二模18: `予盾化解` -> `矛盾化解`.

v19 additionally fixes the valid GPT-5.5 Pro web/app v13 compilation-01 concerns around screenshot spillover and answer-point residue:
- E002 answer points now expose both the 甲公司 and 乙公司 litigation paths within the visible student-facing answer points.
- Student-facing documents no longer embed full-page `原题图` or `细则图`; this removes whole-page screenshot spillover such as the 2025 东城一模第19题 source image carrying Q20 `元首外交` non-Xuanbier material.
- Backend source-image assets are still retained under QA for local verification, but the two student documents are text-only.

v19 also responds to the GPT-5.5 Pro web/app v16 compilation-01 review:
- Locally verified that the named entries still contain the required `题目来源/材料/设问/细则/答案落点/同题组` fields.
- Rewrote student-facing answer points for 2024 石景山一模17, 2024 西城二模16, 2025 东城期末19(1), 2025 东城二模19, and 2025 房山一模19 so raw `细则/替换/变通` residue does not appear in 答案落点.
- GPT chunks are now smaller to reduce cross-entry conflation in web review.

v19 additionally fixes two issues surfaced while adjudicating the v17 web/app first-chunk result:
- 2024 东城一模19: `李某 郭某出具欠据` -> `李某为郭某出具欠据`, confirmed against the earlier formal accepted source text.
- 2024 东城二模19(1): scoring wording now says `乙公司作出肯定答复（材料表述为“可以”）`, avoiding a visible `可以/好的` mismatch for students.
- The previous v17 first-chunk GPT result is not used for closure because browser input-state evidence showed prompt ordering corruption. This package uses smaller chunks and plain BEGIN/END delimiters instead of Markdown code fences.

v19 also fixes the valid GPT-5.5 Pro web/app v18 compilation-01 review:
- 2024 丰台一模17: restored the full reality-meaning scoring chain, including maintaining social fairness, interpersonal harmony, socialist core values, reducing traffic congestion, and advocating green travel.
- 2024 东城二模19(2): changed the visible rubric score label from whole-question `19.（9分）` to this subquestion `19（2）（2分）`.
- 2024 东城一模19: removed the score label from the student-facing answer points while preserving the formal rubric score line.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
END_REVIEW_INSTRUCTIONS


# Chunk Task
Document: AB双轴学生宝典
Chunk: 2/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: baodian-02
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 核心答题点和必备知识
- 核心入口：所有权、财产权、共有部分、相邻通行、采光、加装电梯、业主共同决定、物业服务、绿色居住。
- 第一判断：先找不动产或财产权边界，再落到有利生产、方便生活、团结互助、公平合理。
- 易错边界：多数人同意不等于少数人合法权益自动消失；物业和相邻关系要分清合同义务与物权边界。
- 必背句：先判权利归属、共有或相邻边界，再处理公平合理和实际影响。

### 2024 · 顺义思政 · 二模 · 第17题

- 题目来源：2024 · 顺义思政 · 二模 · 第17题
- 框架归位：A3 物权相邻与共有｜B6 维权路径
- 同题组：本题组仅本分问。

#### 材料
某校学习小组围绕“财产制度助力经济社会发展”的议题开展探究，搜集整理的资料如下。
我国财产制度改革重要节点：
2002年：党的十六大报告提出完善保护私人财产的法律制度。
2004年：宪法修正案在宪法第十三条增加规定：“公民的合法私有财产不受侵犯。”
2007年：十届全国人大五次会议通过物权法，它是我国规范财产关系的民事基本法律。
2016年：《中共中央、国务院关于完善产权保护制度依法保护产权的意见》发布，这是我国首次以中央名义出台关于产权保护的顶层设计文件。这一文件指出：“改革开放以来，通过大力推进产权制度改革，我国基本形成了归属清晰、权责明确、保护严格、流转顺畅的现代产权制度和产权保护法律框架，全社会产权保护意识不断增强，保护力度不断加大。”
2020年：十三届全国人大三次会议通过民法典，进一步完善物权法律制度和其他财产制度。
2022年：党的二十大报告指出：“加强知识产权法治保障，形成支持全面创新的基础制度。”

#### 设问
结合材料，运用所学知识，说明我国财产制度改革如何助力经济社会发展。

#### 细则
17．（7分）
①财产制度规范民事主体的财产关系，坚持物权平等保护原则，依法有效保护各种所有制经济组织和公民的财产权，确定财产归属，增强人民群众的财产财富安全感，增强社会信心，稳定市场主体投资、交易预期，促进财产的流通使用，促进经济社会持续健康发展和国家长治久安。
②建立财产权保护的长效机制，保护财产权，就是保护劳动、保护发明创造、保护和发展生产力，贯彻创新驱动发展战略，增强各类经济主体创新创业动力，促进经济高质量发展。
③完善产权制度，促进生产关系的调整，激活社会主义市场经济蓬勃发展的内生动力，夯实社会主义市场经济的基石，从而推动经济社会的进步。

#### 答案落点
- 17．（7分）①财产制度规范民事主体的财产关系，坚持物权平等保护原则，依法有效保护各种所有制经济组织和公民的财产权，确定财产归属，增强人民群众的财产财富安全感，增强社会信心，稳定市场主体投资、交易预期，促进财产的流通使用，促进经济社会持续健康发展和国家长治久安。
- ②建立财产权保护的长效机制，保护财产权，就是保护劳动、保护发明创造、保护和发展生产力，贯彻创新驱动发展战略，增强各类经济主体创新创业动力，促进经济高质量发展。
- ③完善产权制度，促进生产关系的调整，激活社会主义市场经济蓬勃发展的内生动力，夯实社会主义市场经济的基石，从而推动经济社会的进步。

### 2025 · 东城 · 期末 · 第19题第1问

- 题目来源：2025 · 东城 · 期末 · 第19题第1问
- 框架归位：A3 物权相邻与共有｜B7 短答识别
- 同题组：本题组仅本分问。

#### 材料
某校开展“我为社区献一策”的社会实践活动。下面是一组同学撰写的调查报告。
一、调查背景
近年来，电动自行车以其经济、便利的特点成为市民重要的交通工具。然而，保有量与充电设施数量不
匹配，让充电成为困扰居民的问题。
二、调查发现
某社区有 446 辆电动自行车，却只有 60 个充电接口，对车主新增充电设施的提议，大家产生了意见分
歧。
甲：我没有电动自行车，建车棚会占用绿地，影响我遛弯了。
乙：既不能飞线充电，小区也没有配套设备能集中充电，让我们怎么办？
丙：消防安全问题谁来管？影响居民通行、采光怎么办？
三、学生建议
为解决这一困扰，让电动自行车在楼下待得住，该组同学为社区设计了“在公共区域设置电池充电柜，
车电分离”的方案。

#### 设问
资料卡
《高层民用建筑消防安全管理规定》
第三十七条……电动自行车存放、充电场所应当配备必要的消防器材，充电设施应当具备充
满自动断电功能。
《中华人民共和国民法典》
第二百七十八条下列事项由业主共同决定：……（八）改变共有部分的用途或者利用共有部
分从事经营活动。
（1）遇到的法律问题： 、 。

#### 细则
19（1）评分细则（两种思路都可以得分，如果在同样的思路中，要求涉及具体问题不同，1个问题1分）
思路1.充电桩方案的具体内容是否符合/违反规定（依法依规）
如：
设置充电柜是否违反消防规定；
改变公有部分用途的法律程序问题；
涉及民法典对公共区域功能改变的规定；
思路2.充电桩方案的具体内容涉及哪些权利？
如：
公共区域设置充电柜是否涉及侵权问题；
可能侵害部分业主对公共部分的合法权利
充电柜建设是否损害相邻权的问题
充电柜安全问题可能侵犯居民的人身安全和财产权
xx问题侵犯了居民的合法权益

#### 答案落点
- 可从方案是否依法依规和涉及哪些权利两个思路回答，写出两个具体法律问题即可。
- 依法依规角度：公共区域设置电池充电柜是否符合消防安全规定，是否具备必要消防器材和充满自动断电功能。
- 依法依规角度：改变共有部分用途，或利用共有部分从事经营活动，是否需要业主共同决定。
- 权利角度：在公共区域设置充电柜是否可能侵害部分业主对共有部分的合法权益。
- 权利角度：充电柜建设是否影响相邻关系，如通行、采光、使用公共绿地等。
- 安全角度：充电柜安全问题可能涉及居民人身安全和财产权保护。
- 不要只写“充电难”“居民有分歧”，要把问题落到消防、共有部分、相邻权或合法权益上。

### 2025 · 朝阳 · 二模 · 第20题第1问

- 题目来源：2025 · 朝阳 · 二模 · 第20题第1问
- 框架归位：A3 物权相邻与共有｜B4 评析认识
- 同题组：2025 · 朝阳 · 二模 · 第20题第1问；2025 · 朝阳 · 二模 · 第20题第2问

#### 材料
(10分)在日常生活中,要把握好权利和义务的关系。
材料一 孙女士和刘先生是同一楼层的邻居,两家入户门相对,相距约 2 米。刘先生在自家入户门安装
了具有“智能人脸识别”“180 度超广角”“自动人体侦测”“云存储”等功能的可视门铃摄像头,可通过
手机远程操控。孙女士认为该摄像头可能拍摄到自己及家人的日常出行规律及其他动态信息,要求刘先生
拆除该摄像头,双方由此产生纠纷。
材料二 《中华人民共和国民法典》(节选)
第二百七十一条 业主对建筑物内的住宅、经营性用房等专有部分享有所有权,对专有部分以外的共
有部分享有共有和共同管理的权利。

#### 设问
(1)结合材料,运用《法律与生活》知识,分析上述案例。(8分)

#### 细则
20（1）（8分）结合材料，运用《法律与生活》知识，分析上述案例。
①定性：刘先生侵犯了孙女士的隐私权（2分）。必须在侵权框架内作答；“隐私权”字样写错不给分。刘先生应当承担侵权责任（1分）。
②确权：根据民法典规定，楼道属于双方各自专有部分以外的共有部分，双方享有共有和共同管理的权利（1分）。
③解释隐私权：摄像头能拍摄到孙女士家的日常进出信息，特别是日常出行规律及其他动态信息，该事实分析1分。只笼统写“拍到家门口”或“拍到信息”不给该事实分。
④分析过错：刘先生主观上具有过错（1分）。可替代表述包括：安装设备范围、功能已超出必要限度；使用摄像头超出合理范围；行使权利损害他人正当权益；安装前未尽到妥善注意义务。
⑤相邻关系：根据民法典关于相邻关系的规定，处理邻里纠纷应遵循有利生产、方便生活、团结互助、公平合理原则（1分）。

#### 答案落点
- 定性：刘先生侵犯了孙女士的隐私权，应当承担侵权责任。
- 确权：楼道属于双方专有部分以外的共有部分，双方享有共有和共同管理的权利。
- 隐私分析：摄像头可能拍摄孙女士及家人的日常出行规律和其他动态信息，与私人生活习惯高度关联，属于隐私利益。
- 过错分析：刘先生为保障财产安全可以采取合理措施，但本案设备功能和拍摄范围超出必要限度，安装前未尽妥善注意义务。
- 相邻关系：相邻权利人应按照有利生产、方便生活、团结互助、公平合理原则正确处理邻里关系。

### 2025 · 朝阳 · 二模 · 第20题第2问

- 题目来源：2025 · 朝阳 · 二模 · 第20题第2问
- 框架归位：A3 物权相邻与共有｜B6 维权路径
- 同题组：2025 · 朝阳 · 二模 · 第20题第1问；2025 · 朝阳 · 二模 · 第20题第2问

#### 材料
(10分)在日常生活中,要把握好权利和义务的关系。
材料一 孙女士和刘先生是同一楼层的邻居,两家入户门相对,相距约 2 米。刘先生在自家入户门安装
了具有“智能人脸识别”“180 度超广角”“自动人体侦测”“云存储”等功能的可视门铃摄像头,可通过
手机远程操控。孙女士认为该摄像头可能拍摄到自己及家人的日常出行规律及其他动态信息,要求刘先生
拆除该摄像头,双方由此产生纠纷。
材料二 《中华人民共和国民法典》(节选)
第二百七十一条 业主对建筑物内的住宅、经营性用房等专有部分享有所有权,对专有部分以外的共
有部分享有共有和共同管理的权利。

#### 设问
(2)假如你是人民调解员,提出解决上述纠纷的建议。(2分)

#### 细则
20.（10分）
（2）（2分）
①拆除设备。建议刘先生及时拆除摄像头， 1分
②清除信息。已拍摄的孙女士及家人的视频信息。1分
或：在双方协商一致情况下，双方可共享摄像头。

只写“更换/拆除设备”，或只写“清除云存储信息”，只给1分。
只建议改用仅具备基础安防功能的设备， 只给1分。
只写出赔礼道歉，未写出具体措施， 只给1分。
只笼统写其他侵权责任承担方式， 都不给分。

#### 答案落点
- 建议刘先生及时拆除摄像头。
- 建议刘先生清除已拍摄的孙女士及其家人的视频信息。
- 也可在双方协商一致的情况下，由双方共享摄像头。
- 只写更换或拆除设备、只写清除云存储信息、只建议改用基础安防设备，均只能按1分处理。
- 只写赔礼道歉或笼统写其他侵权责任承担方式，不能替代具体解决措施。

### 2025 · 顺义 · 一模 · 第19题第1问

- 题目来源：2025 · 顺义 · 一模 · 第19题第1问
- 框架归位：A3 物权相邻与共有｜B6 维权路径
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
- 框架归位：A3 物权相邻与共有｜B5 意义价值
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
END_CHUNK_CONTENT
