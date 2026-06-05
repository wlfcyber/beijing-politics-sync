BEGIN_REVIEW_INSTRUCTIONS
# External Review Context
You are GPT-5.5 Pro doing one chunk of a formal web/app review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is v18. Local QA reports:
- Empty rubric-marker suspects in both Markdown files: 0.
- DOCX XML scan found 0 occurrences of local paths or image-path traces.
- Rendered successfully: 汇编 86 pages, 宝典 93 pages.
- Student-facing DOCX files embed no whole-page source screenshots; source/rubric images remain backend evidence only.
- Rendered-PDF OCR scan found no `元首外交`, paper footer, backend trace, or prior OCR-pollution terms.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

v18 inherits the v10 fixes for the valid GPT-5.5 Pro web review failure from v9 compilation-01, and additionally fixes the valid GPT-5.5 Pro web review failure from v10 compilation-03:
- 2026 朝阳期末18(1): cleaned material/rubric/answer points for the online consumption contract case.
- 2026 朝阳二模18: restored three legal Q&A blanks and the rights-protection answer points.
- 2026 通州期末19(1): restored Civil Code Article 292 and Article 296 legal basis.
- 2026 通州一模20: cleaned severe OCR damage in parties, court, liability, and public-place text.
- 2026 门头沟一模18(1): removed empty trailing rubric marker.
- 2026 房山二模17: removed duplicated/half scoring language from answer points.
- 2026 西城二模18(1)(2): cleaned AI/court/rubric OCR wording.
- 2026 顺义一模18 and 顺义二模18(2): added shared-value and governance-risk answer angles.
- Render QA also changed the Chinese font to Hiragino Sans GB so E049 `稳步前行` renders without dropped glyphs.

v18 specifically fixes the valid Claude Opus 4.8 Max Safari web/app review failure from v11:
- 2024 朝阳二模17: removed `原答案：`, `辩`, `实社社会` and other OCR/editorial pollution; rewrote answer points as clean student-facing bullets.
- 2026 房山二模18(1): moved the AI legal-risk item from A1 to A5 知识产权与公平竞争, with a note that it also involves 名誉权.

v18 also applies a post-Claude cleanup pass for small nonblocking OCR/text defects:
- 2025 东城二模19: `钱某事限制民事行为能力人` -> `钱某是限制民事行为能力人`.
- 2025 东城期末19(1): `建车栩会占用绿地` -> `建车棚会占用绿地`.
- 2025 丰台二模19(2): `参考答 案` -> `参考答案`.
- 2025 丰台期末19: `法院驳回了尹荣的诉讼请求` -> `法院驳回了尹某的诉讼请求`.
- 2026 丰台一模20: `低头看手机 监控画面` -> `低头看手机。监控画面`.
- 2026 丰台二模18: `予盾化解` -> `矛盾化解`.

v18 additionally fixes the valid GPT-5.5 Pro web/app v13 compilation-01 concerns around screenshot spillover and answer-point residue:
- E002 answer points now expose both the 甲公司 and 乙公司 litigation paths within the visible student-facing answer points.
- Student-facing documents no longer embed full-page `原题图` or `细则图`; this removes whole-page screenshot spillover such as the 2025 东城一模第19题 source image carrying Q20 `元首外交` non-Xuanbier material.
- Backend source-image assets are still retained under QA for local verification, but the two student documents are text-only.

v18 also responds to the GPT-5.5 Pro web/app v16 compilation-01 review:
- Locally verified that the named entries still contain the required `题目来源/材料/设问/细则/答案落点/同题组` fields.
- Rewrote student-facing answer points for 2024 石景山一模17, 2024 西城二模16, 2025 东城期末19(1), 2025 东城二模19, and 2025 房山一模19 so raw `细则/替换/变通` residue does not appear in 答案落点.
- GPT chunks are now smaller to reduce cross-entry conflation in web review.

v18 additionally fixes two issues surfaced while adjudicating the v17 web/app first-chunk result:
- 2024 东城一模19: `李某 郭某出具欠据` -> `李某为郭某出具欠据`, confirmed against the earlier formal accepted source text.
- 2024 东城二模19(1): scoring wording now says `乙公司作出肯定答复（材料表述为“可以”）`, avoiding a visible `可以/好的` mismatch for students.
- The previous v17 first-chunk GPT result is not used for closure because browser input-state evidence showed prompt ordering corruption. This v18 package uses smaller chunks and plain BEGIN/END delimiters instead of Markdown code fences.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
END_REVIEW_INSTRUCTIONS


# Chunk Task
Document: 试题和细则汇编
Chunk: 9/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-09
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2026 · 东城 · 期末 · 第18题第1问

- 题目来源：2026 · 东城 · 期末 · 第18题第1问
- 同题组：2026 · 东城 · 期末 · 第18题第1问；2026 · 东城 · 期末 · 第18题第2问

#### 材料
无人机起飞如何系好“安全带”?
陈某向店主刘某发送邮件：“急需购买A型号无人机一台。用于重要商业拍摄。”刘某回复：“全新
原装，15000元。”陈某立即转账。刘某误将一台内部结构轻微损伤（外观无明显痕迹）的同型号展示机
寄出。
陈某收货后在首次使用中，该无人机因上述损伤失控坠毁，砸伤陈某手臂。陈某花费医疗费8000
元，并因错过商业拍摄损失收入5000元。陈某要求刘某赔偿，双方协商未果。

#### 设问
（1）运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。

#### 细则
18.（11分）无人机起飞如何系好"安全带"?
 陈某向店主刘某发送邮件：“急需购买A型号无人机一台，用于重要商业拍摄。”刘某回复：“全新原装，15000元。”陈某立即转账。刘某误将一台内部结构轻微损伤（外观无明显痕迹）的同型号展示机寄出。
 陈某收货后在首次使用中，该无人机因上述损伤失控坠毁，砸伤陈某手臂。陈某花费医疗费8000元，并因错过商业拍摄损失收入5000元。
 陈某要求刘某赔偿，双方协商未果。
 （1）运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。(7分)
 （2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作?（4分）
要约
实质性变更，新要约
承诺
主体适格+意思表示真实+形式内容合法→合同有效
【违约逻辑：合同成立+合同有效+存在违约行为 → 承担违约责任 4分】
【侵权逻辑：权利受保护+侵权要件齐备 → 承担侵权责任 3分】
违反全面履行/诚信履行/民法诚信/公平原则
要件/侵犯XX权利 → 侵权责任
要约+承诺→合同成立

第一层：违约
【违约角度：合同成立+合同有效+存在违约行为 → 承担违约责任 共4分】

 陈某与刘某之间通过要约与承诺达成一致意思表示，合同成立/订立，双方主体适格、意思表示真实，合同形式与内容合法，合同有效（分析清楚2分，只说成立且有效1分）
 1.只说合同成立/合同有效，没说合同成立且有效，也可给1分
 2.成立（要约+承诺）/有效（主体适格，意思表示真实，形式内容合法）能分析清楚一个，就可给分析的1分

 因刘某未能全面履行合同义务/违反全面履行原则/诚信履行原则/民法诚信原则/民法公平原则（1分）
 注意：这道题不构成“欺诈”（意思表示不真实）

 其行为构成违约，应承担赔偿损失等违约责任（1分）

第二层：侵权
【侵权角度：侵权要件 → 承担侵权责任 共3分】
 情况一：对刘某（销售者）主张侵权（一般过错侵权）
 分析：事实（行为+损害后果）、因果关系、过错，完整分析要件2分，不完整1分。未分析要件，写侵犯了身体权、健康权 或 消费者知情权、安全消费的权利可得1分。要件分析不完整+侵犯了什么权利 可得2分。结论-构成侵权，应当依法承担侵权责任（1分）。
 情况二：对生产者（不排除刘某是生产者的可能）主张产品责任（无过错侵权）
 分析：事实（行为+损害后果），因果关系（2分）完整分析要件2分，不完整1分。
未分析要件，写侵犯了身体权、健康权 或 消费者知情权、安全消费的权利可得1分。要件分析不完整+侵犯了什么权利 可得2分。结论-构成侵权，应当依法承担侵权责任（1分）。

 注：这道题不涉及过错推定责任，举证责任倒置 ||“无过错推定”是错误表述
 说生产者适用一般过错侵权责任，或销售者适用无过错侵权责任 都是错误

#### 答案落点
- 违约角度：陈某与刘某通过要约与承诺达成一致意思表示，合同成立；双方主体适格、意思表示真实，合同形式与内容合法，合同有效。
- 刘某交付内部结构轻微损伤的展示机，未全面履行合同义务，违反全面履行原则、诚信履行原则或民法诚信原则。
- 刘某行为构成违约，应承担赔偿损失等违约责任。
- 侵权角度：陈某手臂受伤、医疗费8000元和商业拍摄损失等属于损害事实，无人机问题与损害后果之间存在因果关系。
- 若对销售者刘某主张一般过错侵权，应分析行为、损害后果、因果关系和过错；构成侵权的，应依法承担侵权责任。
- 若对生产者主张产品责任，应分析产品缺陷、损害后果和因果关系；产品责任适用无过错侵权责任。
- 本题不构成欺诈，也不涉及过错推定责任或举证责任倒置。

### 2026 · 东城 · 期末 · 第18题第2问

- 题目来源：2026 · 东城 · 期末 · 第18题第2问
- 同题组：2026 · 东城 · 期末 · 第18题第1问；2026 · 东城 · 期末 · 第18题第2问

#### 材料
无人机起飞如何系好“安全带”?
陈某向店主刘某发送邮件：“急需购买A型号无人机一台。用于重要商业拍摄。”刘某回复：“全新
原装，15000元。”陈某立即转账。刘某误将一台内部结构轻微损伤（外观无明显痕迹）的同型号展示机
寄出。
陈某收货后在首次使用中，该无人机因上述损伤失控坠毁，砸伤陈某手臂。陈某花费医疗费8000
元，并因错过商业拍摄损失收入5000元。陈某要求刘某赔偿，双方协商未果。

#### 设问
（2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作?

#### 细则
18（2）（4分）维权成功需要做好充分准备和策略选择。陈某需要做好以下工作。
评分口径提示：本小问卷面标注为4分；原细则列出三类准备工作，每类按具体性给到2分，实际按有效采点择优累计，总分不超过4分，不理解为6分小问。
①选择具体维权途径（2分）：可选择调解、仲裁或诉讼。调解可包括第三方人民调解、行政调解、诉讼调解；仲裁需要双方达成有效仲裁协议；若不愿调解或调解不成，可考虑诉讼。若决定向人民法院提起诉讼，需准备起诉状、原被告身份信息，熟悉诉讼流程，注意三年诉讼时效等。无解释、不具体只给1分。
②依法收集证据及类型（2分）：固定并提交交易存在的合同、订单证据，如邮件记录、转账记录等电子证据；收集证明无人机问题故障、手臂受伤损害事实、相关经济损失以及因果关系的物证、诊疗材料、费用凭证等。无解释、不具体只给1分。
③明确权利义务，诉求合理（2分）：主动明确相关法律依据，可通过查询法律法规、咨询专业法律人士或利用法律援助等方式，厘清自身权利义务；可主张违约责任或侵权责任，提出退还无人机购置费、赔偿医疗费、误工费、损失费等经济损失的合理诉求；注意不告不理原则。无解释、不具体只给1分。

#### 答案落点
- 评分口径：本小问4分，三类工作均是采分方向，按具体性择优累计，总分不超过4分。
- 选择维权途径：可选择调解、仲裁或诉讼；调解不成可诉讼，仲裁须有有效仲裁协议；若诉讼要准备起诉状、身份信息并注意三年诉讼时效。
- 收集交易证据：邮件、订单、转账记录等能证明合同或交易存在的电子证据。
- 收集损害和因果关系证据：无人机故障、手臂受伤、医疗费、商业拍摄损失及因果关系的相关材料。
- 明确法律依据和权利义务：可查询法律法规、咨询专业人士或申请法律援助。
- 诉求要合理：可主张违约责任或侵权责任，要求退还无人机购置费，赔偿医疗费、误工费、损失费等合理经济损失。
- 注意不告不理原则，诉讼请求要写清楚、能对应事实和证据。

### 2026 · 丰台 · 一模 · 第20题

- 题目来源：2026 · 丰台 · 一模 · 第20题
- 同题组：本题组仅本分问。

#### 材料
以案释法，明理释义。
《中华人民共和国民法典》
第一千一百九十八条 宾馆、商场、银行、车站、机场、体育场馆、娱乐场所
等经营场所、公共场所的经营者、管理者或者群众性活动的组织者，未尽到安全保
障义务，造成他人损害的，应当承担侵权责任。
【基本案情】
郭某在某餐厅用餐结束后步行离开，在餐厅外的台阶区域不慎踩空摔倒。餐厅外
的监控视频显示，郭某从出现在画面中开始，就一直在低头看手机。监控画面中未见
下雨、下雪，台阶处也未见积雪、积水、冰冻。事发十天后，郭某自行到医院就诊，
诊断腰椎右侧横突骨折。郭某向人民法院起诉餐厅经营者某餐饮公司和餐厅所在楼
宇的物业管理企业某商业管理公司，要求某餐饮公司、某商业管理公司承担侵权责
任，支付赔偿金。
【裁判结果】
人民法院审理认为，原告郭某摔倒是其自身未尽安全注意义务所致，被告某餐饮
公司和某商业管理公司对此并无过错，不应承担赔偿责任。故判决驳回郭某全部诉讼
请求。

#### 设问
结合材料，运用《法律与生活》知识，阐明人民法院作出该判决的法理依据和现
实意义。

#### 细则
20.（8 分）
人民法院以事实为根据、以法律为准绳，作出了上述判决。根据民法典规定，宾馆、商场等公共场所经营者、管理者因过错造成他人损害的，应当承担侵权责任。被告对原告的安全保障义务应保持在合理限度内，且相关证据表明事发现场不存在影响原告通行的客观因素。原告是完全民事行为能力人，摔倒是其自身未尽安全注意义务所致。因此，某餐饮公司和某商业管理公司对此并无过错，不应承担赔偿责任。
该判决有利于平衡原被告双方的权利与义务，倡导安全文明出行和自我负责的安全责任意识，明确经营场所、公共场所的经营者、管理者安全保障义务的边界，弘扬社会主义核心价值观。

#### 答案落点
- 20.（8 分）人民法院以事实为根据、以法律为准绳，作出了上述判决。
- 根据民法典规定，宾馆、商场等公共场所经营者、管理者因过错造成他人损害的，应当承担侵权责任。
- 被告对原告的安全保障义务应保持在合理限度内，且相关证据表明事发现场不存在影响原告通行的客观因素。
- 原告是完全民事行为能力人，摔倒是其自身未尽安全注意义务所致。
- 因此，某餐饮公司和某商业管理公司对此并无过错，不应承担赔偿责任。
- 该判决有利于平衡原被告双方的权利与义务，倡导安全文明出行和自我负责的安全责任意识，明确经营场所、公共场所的经营者、管理者安全保障义务的边界，弘扬社会主义核心价值观。

### 2026 · 丰台 · 二模 · 第18题

- 题目来源：2026 · 丰台 · 二模 · 第18题
- 同题组：本题组仅本分问。

#### 材料
法安天下，德润人心。

【基本案情】张某承包果园多年，果园渐成规模。自2025年春季起，李某饲养的牛群多次闯入其果园，不仅撞断树枝、损坏树体，更将正值花期的果树花苞啃食殆尽，导致大幅减产。张某虽在果园周围悬挂“果园重地，禁止放牧”的警示横幅，但2026年3月，李某家的19头牛再次闯入果园，造成果树严重受损。张某报警后，经民警现场协调，李某仅同意赔偿1000元，与张某主张的35000元实际损失差距较大，张某遂向法院提起诉讼。

《中华人民共和国民法典》第一千二百四十五条：饲养的动物造成他人损害的，动物饲养人或者管理人应当承担侵权责任；但是，能够证明损害是因被侵权人故意或者重大过失造成的，可以不承担或者减轻责任。

【调解过程及结果】案件受理后，承办法官考虑到果园既关乎当事人的财产权益，也与区域生态环境质量密切相关，矛盾化解应与生态修复同步推进。因此，法官并未急于启动庭审程序，而是第一时间赴果园开展现场勘验，全面了解案件背景。在此基础上，法官多次组织双方开展调解工作。一方面，向李某释明《中华人民共和国民法典》关于饲养动物损害责任的有关规定，指出其依法应承担的赔偿责任；另一方面，结合《中华人民共和国生态环境法典》“系统治理、生态优先、绿色发展”的核心原则及“损害担责”的立法理念，引导双方充分认识果园保护的生态价值。

针对李某一次性赔偿确有困难、张某更关注果园后续保护的实际状况，法官提出了“分期赔偿+行为约束+生态修复”的调解方案，由李某分期支付赔偿款，采取围栏加固、专人看管等有效措施，同时协助张某对被损坏的果树进行补种、养护，修复果园生态。经过承办法官的耐心调解，双方当事人最终达成调解协议，李某当庭向张某支付赔偿款2600元并致歉，两家人握手言和。

#### 设问
司法给予我们的不仅仅是定分止争，也是一份融通情理的温暖力量。结合材料，综合运用法治知识，阐明你对这一观点的认识。

#### 细则
18.（8分）
该案的成功调解坚持了法治与德治相结合的原则。（1分）该案以法理定分止争，依据《民法典》，确定李某应承担无过错侵权责任，依法维护张某的合法权益。（3分）
同时，引入《生态环境法典》的核心原则和立法理念，将矛盾化解与生态修复同步推进，彰显法律的刚性；充分考虑双方当事人的实际情况，以“分期赔偿+生态修复”的方案促成当事人互谅互让，传递司法的温暖力量，有利于弘扬社会主义核心价值观。（3+1分）
细则：法治与德治相结合1分；依据《民法典》定分止争、饲养动物侵权适用无过错责任、依法维护合法财产权益、结合生态环境法典推进生态修复共4分；结合双方实际提出柔性调解方案、促成互谅互让、弘扬社会主义核心价值观共3分。

#### 答案落点
- 18.（8分）该案的成功调解坚持了法治与德治相结合的原则。
- （1分）该案以法理定分止争，依据《民法典》，确定李某应承担无过错侵权责任，依法维护张某的合法权益。
- （3分）同时，引入《生态环境法典》的核心原则和立法理念，将矛盾化解与生态修复同步推进，彰显法律的刚性；
- 充分考虑双方当事人的实际情况，以“分期赔偿+生态修复”的方案促成当事人互谅互让，传递司法的温暖力量，有利于弘扬社会主义核心价值观。
- （3+1分）细则：法治与德治相结合1分；
- 依据《民法典》定分止争、饲养动物侵权适用无过错责任、依法维护合法财产权益、结合生态环境法典推进生态修复共4分；
- 结合双方实际提出柔性调解方案、促成互谅互让、弘扬社会主义核心价值观共3分。

### 2026 · 丰台 · 期末 · 第18题

- 题目来源：2026 · 丰台 · 期末 · 第18题
- 同题组：本题组仅本分问。

#### 材料
《中华人民共和国未成年人保护法》第四十四条：爱国主义教育基地、图书馆、青少年宫、儿童活动中心、儿童之家应当对未成年人免费开放。博物馆、纪念馆、科技馆、展览馆、美术馆、文化馆、社区公益性互联网上网服务场所以及影剧院、体育场馆、动物园、植物园、公园等场所，应当按照有关规定对未成年人免费或者优惠开放。

某区人民检察院调查发现，有部分影院在网络票务平台和现场购票场所均未对未成年人免票或优惠购票政策作出明确提示，部分影院现场购票场所处将优惠观影的未成年人群体限定于身高1.3米或1.2米以下的未成年人，缩小了应享受观影优惠的未成年人范围，违反了《中华人民共和国未成年人保护法》第四十四条的规定。

该区人民检察院在全面梳理相关法律及规范性文件的基础上，依法对该区文化和旅游局以行政公益诉讼立案并制发检察建议。要求主管部门监督影院依法对未成年人免费或者优惠开放，对未成年人观影优惠政策在网络票务平台和现场购票场所作出明确提示。

收到检察建议后，该区文化和旅游局通过沟通督促、加强监管和宣传教育等方式整改落实，确保未成年人优惠观影政策落实。

#### 设问
结合材料，运用法治知识，阐述该检察公益诉讼案例的积极意义。

#### 细则
知识板块：政治与法治、法律与生活。能力板块：解释与论证。
检察权（法律监督）+公共利益2分：该案为各地检察机关办理类似案件提供了有效示范，推动检察机关依法行使检察权，有效维护社会公共利益。
政府积极履职+维护市场秩序2分：通过检察建议督促政府有关部门履行法定职责，切实维护良好市场秩序/文化市场健康发展。
市场主体（部分影院的法定义务+未成年人的合法权益）2分：纠正部分影院的侵权违法行为，引导电影院等市场主体自觉履行法律规定的义务，保障未成年人的合法权益。
全社会（法治意识、法治环境+弘扬社会主义核心价值观）2分：增强全社会成员的法治意识，营造全社会保护未成年人健康成长的法治环境。

#### 答案落点
- 知识板块：政治与法治、法律与生活。
- 能力板块：解释与论证。
- 检察权（法律监督）+公共利益2分：该案为各地检察机关办理类似案件提供了有效示范，推动检察机关依法行使检察权，有效维护社会公共利益。
- 政府积极履职+维护市场秩序2分：通过检察建议督促政府有关部门履行法定职责，切实维护良好市场秩序/文化市场健康发展。
- 市场主体（部分影院的法定义务+未成年人的合法权益）2分：纠正部分影院的侵权违法行为，引导电影院等市场主体自觉履行法律规定的义务，保障未成年人的合法权益。
- 全社会（法治意识、法治环境+弘扬社会主义核心价值观）2分：增强全社会成员的法治意识，营造全社会保护未成年人健康成长的法治环境。
END_CHUNK_CONTENT
