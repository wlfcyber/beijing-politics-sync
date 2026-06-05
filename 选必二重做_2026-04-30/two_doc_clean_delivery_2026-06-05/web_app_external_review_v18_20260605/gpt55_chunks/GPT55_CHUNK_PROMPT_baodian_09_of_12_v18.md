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
Document: AB双轴学生宝典
Chunk: 9/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: baodian-09
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2026 · 丰台 · 二模 · 第18题

- 题目来源：2026 · 丰台 · 二模 · 第18题
- 框架归位：A6 侵权责任｜B4 评析认识
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

### 2026 · 房山 · 一模 · 第17题第2问

- 题目来源：2026 · 房山 · 一模 · 第17题第2问
- 框架归位：A6 侵权责任｜B5 意义价值
- 同题组：2026 · 房山 · 一模 · 第17题第1问；2026 · 房山 · 一模 · 第17题第2问

#### 材料
AI 幻觉造成损失谁买单？
梁某查询高校报考的相关信息时，某 AI 模型（系 A 公司研发）为其提供了不准确信息（俗称“AI 幻觉”）。梁某指出错误时，AI 模型不仅坚称信息正确，并主动生成“内容有误赔偿 10 万元”的承诺。梁某认为 AI 模型生成的不准确信息对其构成误导受到侵害，AI 模型也承诺对其进行赔偿，遂起诉要求 A 公司赔偿损失。A 公司声称对话内容由 AI 模型生成，已在界面提醒“AI 生成内容仅供参考”。法院经查原告权益未受到实际损害，参照《生成式人工智能服务管理暂行办法》认定不构成侵权。
生成式人工智能服务管理暂行办法
第四条（一）坚持社会主义核心价值观，不得生成煽动颠覆国家政权、危害国家安全和利益、宣扬恐怖主义以及虚假有害信息等法律、行政法规禁止的内容；
第四条（五）基于服务类型特点，采取有效措施，提升生成式人工智能服务的透明度，提高生成内容的准确性和可靠性。
该案例写入 2026 年最高人民法院工作报告。

#### 设问
（2）结合材料，运用法治知识，分析该案例写入最高人民法院工作报告的意义。（6分）

#### 细则
17（2）答案示例
该案例中，AI 模型生成的内容不是《生成式人工智能服务管理暂行办法》规定的有毒有害等法律、行政法规禁止的内容；鉴于科技发展现状，第四条（五）提出要提高生成内容的准确性和可靠性，法院认定不构成侵权。
该案例写入最高人民法院工作报告，有利于平衡技术创新发展与民事权益保护的关系，引导公众理性使用 AI，增强全民法治观念；有利于规范 AI 行业发展，促进技术创新；有利于彰显公平，促进公正司法。
17（2）细则变通：
2分：平衡民事主体合法权益保护与社会公共利益，或平衡技术创新发展与民事权益保护，或从公平角度展开。
1分：公民角度，引导公众理性使用 AI，增强全民法治观念、普法宣传或促进全民守法。
1分：AI 行业角度，规范 AI 行业发展、促进技术创新、积极承担社会责任、实现经济效益与社会效益统一，或为 AI 行业发展营造良好法治环境。
1分：司法角度，促进公正司法，或为同类案件审理提供司法借鉴、依据。
1分：法治社会、法治中国、国家治理体系和治理能力现代化角度。
可替换：弘扬践行社会主义核心价值观、中华优秀传统美德，或依法治国和以德治国相结合。

#### 答案落点
- 该案例写入最高人民法院工作报告，有利于平衡技术创新发展与民事权益保护的关系。
- 有利于引导公众理性使用 AI，增强全民法治观念。
- 有利于规范 AI 行业发展，促进技术创新，并推动企业承担社会责任。
- 有利于为 AI 行业发展营造良好法治环境。
- 有利于彰显公平，促进公正司法，为同类案件审理提供司法借鉴。
- 有利于推进法治社会、法治中国建设，提升国家治理体系和治理能力现代化水平。

### 2026 · 朝阳 · 二模 · 第18题

- 题目来源：2026 · 朝阳 · 二模 · 第18题
- 框架归位：A6 侵权责任｜B1 补表/补链
- 同题组：本题组仅本分问。

#### 材料
有问必答，有惑必解，在法治生活里稳步前行。

在某社区开展的专题普法宣传活动互动环节，居民踊跃提问，法官耐心解答并给出专业的法律建议。

问题一：楼上墙砖脱落、花盆坠落，对我产生困扰，怎么办？
答：以上行为可能涉及 ① 等人身权利。高空抛物、坠物危害极大，这类情形适用“ ② ”原则，即当事人提出诉讼主张时，由对方负责举证。

问题二：出于安全目的，我能在我家房屋门口装一个摄像头吗？
答：以上行为可能涉及隐私权。慎重！安装摄像头看似是“家务事”，实则涉及他人隐私权益，安装前应充分考虑对邻居的影响，必要时与邻里沟通说明；若邻居提出异议，应积极协商解决，调整拍摄范围或拆除设备。

问题三：邻居的自建房影响我家的通风、采光，还导致我家墙体潮湿，我能起诉拆除吗？
答：以上行为可能涉及 ③ 权利人的合法权益。可以。原告应当举证可能违法构筑物确实影响其通行、通风、采光等，从而要求判令拆除构筑物。

#### 设问
结合材料，运用《法律与生活》知识，将以上回答补充完整。从以上三个问答中任选其一，谈谈如何依法保护问答中所涉及到的权利。

#### 细则
18.（8分）
结合材料，运用《法律与生活》知识，将以上回答补充完整。从以上三个问答中任选其一，谈谈如何依法保护问答中所涉及到的权利。
【设问要素】结合材料，《法律与生活》，补充完整。任选其一，谈谈如何，保护权利，8分
【阅卷细则】
第一问：（3分=1+1+1）要求：法律术语准确，变通较少
生命权/身体权/健康权 任选其一——1分
举证责任倒置——1分
相邻的不动产/相邻/相邻关系——1分
第二问：（5分=2+2+1）结构：依据+做法+救济
●民法典依据——共2分
民法典（1分）明确规定并保护上述人格权益（1分）。
【变通】（采意）
民法典--1分 人格权益/人格权益下位展开--1分
依据平等、公平、守法和公序良俗等民法原则（至少1个原则+民法典）--2分
民事领域/民事关系/民事法律关系+权利与义务相对等／权利行使要有边界--2分
生命权、身体权、健康权是人最基础的权利—1分
隐私是自然人的私人生活安宁和不愿为他人知晓的私密空间、私密活动、私密信息--1分
保护隐私权，是对宪法规定的通信秘密受法律保护、住宅不受侵犯等公民权利的落实--1分
民法典规定了不动产相邻关系的处理规则--2分
民法典规定不动产权利人应当为相邻权利人提供必要的便利，尽量避免对相邻的不动产权利人造成损害--2分
相邻关系是对不动产所有权的限制或延伸—1分
●民事主体如何做：不得/应当——共2分
任何组织或个人不得侵害他人的生命权、身体权、健康权和隐私权等。
【变通】3选1（生命权、身体权、健康权/隐私权/相邻不动产权利，任选其中一项权利法理阐释--2分）
不得侵害他人的生命权、身体权、健康权/不得刺探、侵扰、泄露、公开他人的隐私—2分
按照有利生产、方便生活、团结互助、公平合理的原则正确处理相邻关系--2分
自己便利行使权利时，应当照顾到相邻方的利益--2分
权利义务相统一—1分（与第一层不重复赋分）
要保护民事权利/合法权利--1分
●民事权利如何救济——共1分
上述人格权益和权利受到侵害的，权利人可依法请求行为人停止侵害、排除妨碍、消除危险、赔礼道歉等；造成权利人有所损失和损害的，还可依法请求损害赔偿。
【变通】
通过和解/调解/仲裁/诉讼等途径维权--1分
承担停止侵害/排除妨碍/赔礼道歉/赔偿损失/损害赔偿等侵权责任--1分
（在前两层没赋满分时，该层答出两点可赋2分）
【注意】选择问题一/二/三--不赋分
个人信息--不赋分
错别字--不赋分
答必修3/全面依法治国的基本要求--不赋分
回应问题二，但仅用相邻关系知识，没答隐私权--扣1分

#### 答案落点
- 第一问补空：①可填生命权、身体权、健康权中任意一个；②填举证责任倒置；③填相邻的不动产、相邻或相邻关系。
- 第二问任选其一作答时，先写依据：民法典明确规定并保护上述人格权益，或规定了不动产相邻关系处理规则。
- 若选问题一，可写任何组织或个人不得侵害他人的生命权、身体权、健康权；高空抛物、坠物涉及人格权益保护和举证责任倒置。
- 若选问题二，必须写隐私权，不要只写相邻关系；可写不得刺探、侵扰、泄露、公开他人隐私。
- 若选问题三，可写民法典规定不动产权利人应为相邻权利人提供必要便利，并尽量避免对相邻权利人造成损害。
- 做法层面要写权利行使有边界，处理相邻关系应坚持有利生产、方便生活、团结互助、公平合理原则。
- 救济层面可写权利受侵害时，可请求停止侵害、排除妨碍、消除危险、赔礼道歉、损害赔偿，也可通过和解、调解、仲裁、诉讼维权。

### 2026 · 西城 · 二模 · 第18题第2问

- 题目来源：2026 · 西城 · 二模 · 第18题第2问
- 框架归位：A6 侵权责任｜B5 意义价值
- 同题组：2026 · 西城 · 二模 · 第18题第1问；2026 · 西城 · 二模 · 第18题第2问；2026 · 西城 · 二模 · 第18题第3问

#### 材料
18．（23分）法治护航AI时代创新发展。
材料一
2025年3月，梁某因计划报考某高校，使用某科技公司（以下简称“被告公司”）开发的生成式AI应用查询招生信息，该应用生成了关于该校某校区的虚假内容（即AI幻觉）。梁某发现后立即纠正，并提供官方佐证，但AI仍坚持错误信息，并生成“若内容有误，自愿赔偿10万元”的承诺。梁某认为因信赖AI信息而花费大量时间整理报考资料，权益受损，遂向法院起诉，要求被告公司承担侵权责任，赔偿经济损失及精神损害。
庭审中，被告公司抗辩称：一、AI生成内容系模型自主运算结果；二、公司已在应用登录界面、对话首页显著位置提示“AI生成内容仅供参考，相关信息请以官方渠道为准”，并已投入技术力量提升内容准确性，尽到合理注意义务；三、梁某未提供充分证据证明自己确实因AI生成的不准确信息遭受了实际损失。
最终，法院驳回了原告的诉讼请求。原、被告均未上诉。
材料二 该案因涉及生成式AI的法律地位、责任边界、监管规范等新型法律与治理问题，被最高人民法院列为典型案例。该案判决坚持“平衡AI产业创新与用户合法权益保护”，为全国法院审理同类案件提供了统一裁判标准，也为AI企业规范经营、行政机关强化监管、公众理性使用AI提供了明确指引。

#### 设问
（2）结合该案判决对生成式AI权责边界的认定，分析其对促进AI产业发展的影响。（6分）

#### 细则
18（2）结合该案判决对生成式AI权责边界的认定，分析其对促进AI产业发展的影响。（6分）
法治是最好的营商环境。该判决通过明确责任边界，避免过度追责，为企业研发与运营提供稳定法律预期，释放产业创新活力。（2分）
通过统一裁判标准，规范行业行为，推动行业规范有序发展。（2分）
平衡用户权益保障与技术创新需求，引导用户理性使用，减少矛盾隐患，助力AI行业长期健康发展。（2分）
细则：①明确权责边界，避免过度追责，稳定企业发展预期，激发创新活力。②统一裁判标准，规范行业行为，引导产业合规有序发展。③坚持权利义务相统一原则，既要求企业履行注意义务，又明确用户负有审慎义务，平衡AI技术创新与用户权益保障，减少矛盾隐患，助力产业长期健康发展。以上任意两个角度，观点+结合材料分析，一个3分，两个6分。

#### 答案落点
- 法治是最好的营商环境，生成式AI产业发展需要清晰可预期的责任边界。
- 判决明确责任边界，避免对企业过度追责，为研发与运营提供稳定法律预期，释放产业创新活力。
- 判决统一裁判标准，规范行业行为，引导生成式AI企业合规有序发展。
- 判决坚持权利义务相统一，既要求企业履行注意义务，也提醒用户对AI生成内容负有审慎使用义务。
- 判决平衡用户权益保障与技术创新需求，减少矛盾隐患，助力AI行业长期健康发展。

### 2026 · 通州 · 一模 · 第20题

- 题目来源：2026 · 通州 · 一模 · 第20题
- 框架归位：A6 侵权责任｜B1 补表/补链
- 同题组：本题组仅本分问。

#### 材料
20.（8分）
阅读材料，完成下表。

基本案情
李某系社区广场舞义务组织者，长期无偿提供音响、安排场地、组织活动，并时常提醒参与者量力而行、注意安全。张某有轻微心脏不适史但未告知李某，自愿参加活动。某日张某跳舞时突然倒地，李某立即拨打120并实施心肺复苏，张某最终因“心源性猝死”抢救无效死亡。张某家属以李某未尽安全保障义务为由诉至法院，要求赔偿60万元。

裁判结果
人民法院驳回张某家属诉讼请求，判定李某无需承担责任。

裁判理由及意义
《中华人民共和国民法典》
第一千一百七十六条 自愿参加具有一定风险的文体活动，因其他参加者的行为受到损害的，受害人不得请求其他参加者承担侵权责任；但是，其他参加者对损害的发生有故意或者重大过失的除外。
第一千一百九十八条 宾馆、商场、银行、车站、机场、体育场馆、娱乐场所等经营场所、公共场所的经营者、管理者或者群众性活动的组织者，未尽到安全保障义务，造成他人损害的，应当承担侵权责任。（节选）

#### 设问
阅读材料，完成表格中“裁判理由及意义”部分。

#### 细则
20.（8分）
理由：根据《中华人民共和国民法典》规定，参与者不存在故意或重大过失，组织者尽到安全保障义务，则无需承担责任。（2分）本案中张某自愿参加活动，因自身原因突发意外，并非他人行为造成。（1分）李某虽为广场舞义务组织者，但已尽到合理的安全保障义务，事前提醒参与者注意安全，事后及时救助，且不存在故意或重大过失，与张某死亡不存在因果关系，不承担侵权责任。（2分）
意义：引导参与者增强风险意识，对自己的行为负责；合理界定义务组织者的责任范围，体现公平原则；鼓励社会成员在互帮互助中传递社会主义核心价值观，维护和谐有序的社区生活秩序。（3分）

#### 答案落点
- 理由：根据民法典，参与者不存在故意或重大过失，组织者已尽到安全保障义务的，无需承担责任。
- 张某自愿参加广场舞活动，因自身原因突发意外，并非其他参加者行为造成。
- 李某虽为广场舞义务组织者，但已尽到合理安全保障义务，事前提醒参与者量力而行、注意安全。
- 李某事后及时拨打120并实施心肺复苏，不存在故意或重大过失，与张某死亡不存在因果关系，不承担侵权责任。
- 意义：引导参与者增强风险意识，对自己的行为负责。
- 意义：合理界定义务组织者的责任范围，体现公平原则。
- 意义：鼓励社会成员在互帮互助中传递社会主义核心价值观，维护和谐有序的社区生活秩序。

## A7 婚姻家庭与继承

本节共 3 个分问。

### 核心答题点和必备知识
- 核心入口：夫妻关系、赡养、抚养、继承、遗赠扶养协议、家庭义务、老年人权益。
- 第一判断：先写法定义务或协议效力，再写保护弱者、弘扬家庭美德和公序良俗。
- 易错边界：亲情价值必须落到谁对谁承担什么法律义务。
- 必背句：身份关系优先，写清赡养、扶养、继承或家庭义务。
END_CHUNK_CONTENT
