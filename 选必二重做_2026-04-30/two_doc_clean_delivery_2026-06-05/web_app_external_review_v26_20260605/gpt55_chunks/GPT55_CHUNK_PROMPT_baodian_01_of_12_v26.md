BEGIN_REVIEW_INSTRUCTIONS
# External Review Context
You are GPT-5.5 Pro doing one chunk of a formal web/app review. Do not invent exam evidence, rubric facts, scoring rules, or legal facts. This is a partial chunk review; do not issue the final project verdict unless asked in a final synthesis prompt.

User requires exactly two student-facing DOCX documents for 选必二《法律与生活》:
1. 试题和细则汇编: all 2024-2026 选必二 subjective questions; each entry has 题目来源、材料、设问、细则、答案落点、同题组.
2. AB双轴学生宝典: A-axis legal relation framework + B-axis answer-shape framework; under each A-axis core point, core answer points/knowledge, then all related subjective questions with the same required fields.

Forbidden student-facing noise: 三十秒速记, engineering/production traces, internal E0xx IDs, source_id/SRC_, absolute local paths, TODO/BLOCKED, backend verification chatter, 制作记录, 命题人路径, 判题四步.

Current candidate is v26. Local QA reports:
- Empty rubric-marker suspects in both Markdown files: 0.
- DOCX XML scan found 0 occurrences of local paths or image-path traces.
- Rendered successfully: 汇编 84 pages, 宝典 93 pages.
- Student-facing DOCX files embed no whole-page source screenshots; source/rubric images remain backend evidence only.
- Rendered-PDF OCR scan found no `元首外交`, paper footer, backend trace, or prior OCR-pollution terms.

Important process constraint: any prior CLI-based Claude/GPT result is invalid for this project and must not be counted. This prompt is for a new valid web/app review pass only.

v26 inherits the v10 fixes for the valid GPT-5.5 Pro web review failure from v9 compilation-01, and additionally fixes the valid GPT-5.5 Pro web review failure from v10 compilation-03:
- 2026 朝阳期末18(1): cleaned material/rubric/answer points for the online consumption contract case.
- 2026 朝阳二模18: restored three legal Q&A blanks and the rights-protection answer points.
- 2026 通州期末19(1): restored Civil Code Article 292 and Article 296 legal basis.
- 2026 通州一模20: cleaned severe OCR damage in parties, court, liability, and public-place text.
- 2026 门头沟一模18(1): removed empty trailing rubric marker.
- 2026 房山二模17: removed duplicated/half scoring language from answer points.
- 2026 西城二模18(1)(2): cleaned AI/court/rubric OCR wording.
- 2026 顺义一模18 and 顺义二模18(2): added shared-value and governance-risk answer angles.
- Render QA also changed the Chinese font to Hiragino Sans GB so E049 `稳步前行` renders without dropped glyphs.

v26 specifically fixes the valid Claude Opus 4.8 Max Safari web/app review failure from v11:
- 2024 朝阳二模17: removed `原答案：`, `辩`, `实社社会` and other OCR/editorial pollution; rewrote answer points as clean student-facing bullets.
- 2026 房山二模18(1): moved the AI legal-risk item from A1 to A5 知识产权与公平竞争, with a note that it also involves 名誉权.

v26 also applies a post-Claude cleanup pass for small nonblocking OCR/text defects:
- 2025 东城二模19: `钱某事限制民事行为能力人` -> `钱某是限制民事行为能力人`.
- 2025 东城期末19(1): `建车栩会占用绿地` -> `建车棚会占用绿地`.
- 2025 丰台二模19(2): `参考答 案` -> `参考答案`.
- 2025 丰台期末19: `法院驳回了尹荣的诉讼请求` -> `法院驳回了尹某的诉讼请求`.
- 2026 丰台一模20: `低头看手机 监控画面` -> `低头看手机。监控画面`.
- 2026 丰台二模18: `予盾化解` -> `矛盾化解`.

v26 additionally fixes the valid GPT-5.5 Pro web/app v13 compilation-01 concerns around screenshot spillover and answer-point residue:
- E002 answer points now expose both the 甲公司 and 乙公司 litigation paths within the visible student-facing answer points.
- Student-facing documents no longer embed full-page `原题图` or `细则图`; this removes whole-page screenshot spillover such as the 2025 东城一模第19题 source image carrying Q20 `元首外交` non-Xuanbier material.
- Backend source-image assets are still retained under QA for local verification, but the two student documents are text-only.

v26 also responds to the GPT-5.5 Pro web/app v16 compilation-01 review:
- Locally verified that the named entries still contain the required `题目来源/材料/设问/细则/答案落点/同题组` fields.
- Rewrote student-facing answer points for 2024 石景山一模17, 2024 西城二模16, 2025 东城期末19(1), 2025 东城二模19, and 2025 房山一模19 so raw `细则/替换/变通` residue does not appear in 答案落点.
- GPT chunks are now smaller to reduce cross-entry conflation in web review.

v26 additionally fixes two issues surfaced while adjudicating the v17 web/app first-chunk result:
- 2024 东城一模19: `李某 郭某出具欠据` -> `李某为郭某出具欠据`, confirmed against the earlier formal accepted source text.
- 2024 东城二模19(1): scoring wording now says `乙公司作出肯定答复（材料表述为“可以”）`, avoiding a visible `可以/好的` mismatch for students.
- The previous v17 first-chunk GPT result is not used for closure because browser input-state evidence showed prompt ordering corruption. This package uses smaller chunks and plain BEGIN/END delimiters instead of Markdown code fences.

v26 also fixes the valid GPT-5.5 Pro web/app v18 compilation-01 review:
- 2024 丰台一模17: restored the full reality-meaning scoring chain, including maintaining social fairness, interpersonal harmony, socialist core values, reducing traffic congestion, and advocating green travel.
- 2024 东城二模19(2): changed the visible rubric score label from whole-question `19.（9分）` to this subquestion `19（2）（2分）`.
- 2024 东城一模19: removed the score label from the student-facing answer points while preserving the formal rubric score line.

v26 additionally repairs issues surfaced while adjudicating the v19 web/app first-chunk result:
- Local source/render/OCR contradicted the v19 GPT blocker about 2024 丰台一模17 material fracture; this is recorded as web-input contamination, not a document defect.
- 2024 朝阳一模19: removed the answer-point score-label residue while preserving the formal rubric score line.
- Applied a global answer-point cleanup layer to remove leading question-number / score shells from student-facing answer-point bullets while preserving formal rubric text.
- 2026 延庆一模18(1): replaced a whole-rubric answer-point dump with seven clean student-facing answer points.
- v26 Markdown and OCR scans found no backend/web prompt traces and no answer-point bullets beginning with score shells.

v26 also fixes the valid GPT-5.5 Pro web/app v23 compilation-06 review:
- 2025 海淀期末20: restored the original table/example/blank-column structure from the source DOCX and removed the editor residue `表格条款补充`; render QA then changed the visible student text to a clear `表格转写` format.
- 2025 海淀一模18: rewrote answer points as clean student-facing bullets while preserving the formal scoring-rule text in `细则`.
- Broader answer-point residue scan then cleaned E010, E035, E048, E050, E053, E054, E057, E062, E063, E066, E067, and E069 so `答案落点` no longer begins with raw score shells, `【细则】`, `评分细则`, or prompt-like headings.

For this chunk, identify only BLOCKING defects or significant NONBLOCKING issues visible in the chunk. If something depends on original exam images not present in this chunk, say what Codex must locally verify; do not invent corrected wording.
END_REVIEW_INSTRUCTIONS


# Chunk Task
Document: AB双轴学生宝典
Chunk: 1/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: baodian-01
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
# 选必二《法律与生活》AB双轴学生宝典

本稿沿用 AB 双轴：A 轴定法律关系，B 轴定答案形状。每个 A 轴核心要点下，穷尽列入当前三年题源中归入该点的主观题。

## AB 双轴总规则

- A 轴：先判断生活冲突属于哪类法律关系，防止整题跑偏。
- B 轴：再判断设问要表格、判责、诉求、评析、意义、维权路径还是短答识别，防止答案形状跑偏。
- 写法：材料事实必须进入法律规则，法律规则必须落到结论。

## A1 民事行为与时效

本节共 3 个分问。

### 核心答题点和必备知识
- 核心入口：未成年人、意思表示、代理、追认、合同效力、限制民事行为能力、诉讼时效、不适用时效。
- 第一判断：先判断行为是否有效、权利是否还能主张，再落到交易安全或特殊身份利益保护。
- 易错边界：诉讼时效不是权利消灭；未成年人案件不能只写同情，要写行为能力、追认和责任分配。
- 必背句：先判断行为能力、意思表示、追认、时效或行为效力，再落请求能否支持。

### 2024 · 东城 · 一模 · 第19题

- 题目来源：2024 · 东城 · 一模 · 第19题
- 框架归位：A1 民事行为与时效｜B5 意义价值
- 同题组：本题组仅本分问。

#### 材料
案件1 2018年，郭某为李某制作电表箱，李某为郭某出具欠据，约定2019年2月1日前还
清。期间，郭某从未催要钱款。2024年3月，郭某
向李某催讨钱款，李某拒绝还款。郭某无奈将李
某告上法庭，最终因李某主张诉讼时效届满而
败诉。
案件2 冯某与其母程某约定，自2018年3
月起，冯某每月向程某支付赡养费。2019年1月
资料卡
诉讼时效是指权利主体
在法定期间内不行使权利，
义务人便享有抗辩权（权利
人行使其请求权时，义务人
享有的拒绝其请求的权利），
从而导致权利人无法胜诉的
法律制度。
起，冯某再未支付上述费用，程某从未催讨。2024
年2月，程某将冯某诉至法庭，要求其支付5年来未支付的相关费用。冯某以诉讼
时效届满为由进行抗辩。法院依据《中华人民共和国民法典》第一百九十六条，以
请求支付赡养费不适用诉讼时效为由，对冯某的主张不予支持，判令冯某如数支付
相关费用。

#### 设问
针对上述案件，运用《法律与生活》知识，谈谈法律规定诉讼时效并对其不适用
的情形加以规定的原因。

#### 细则
19.（6分）
法律规定诉讼时效有助于督促当事人积极主张权利，推动纠纷解决，节约司法资源。赡
养问题事关老年人的基本生存权利，成年子女对父母有赡养的义务。请求支付赡养费不
适用诉讼时效的规定有助于保护老年人的合法权益，彰显公序良俗，体现人文关怀，构建
和谐家庭。

#### 答案落点
- 法律规定诉讼时效，有助于督促当事人积极主张权利，推动纠纷解决，节约司法资源。
- 赡养问题事关老年人的基本生存权利，成年子女对父母有赡养义务。
- 请求支付赡养费不适用诉讼时效，有助于保护老年人的合法权益。
- 该规定彰显公序良俗，体现人文关怀，有利于构建和谐家庭。

### 2025 · 东城 · 二模 · 第19题

- 题目来源：2025 · 东城 · 二模 · 第19题
- 框架归位：A1 民事行为与时效｜B1 补表/补链
- 同题组：本题组仅本分问。

#### 材料
(8分)法律以清晰的边界和公正的尺度守护社会秩序，营造美好生活。
案件一 龙某为 13 周岁的钱某在所经营的美容工作室进行了大面积文身并收取费用。钱某母亲发现后，为
避免对钱某求学及就业造成影响，要求龙某为钱某清洗文身并赔偿。因协商未果，钱某诉至法院，最终法
院判决龙某退还文身费用并赔偿精神损失。
案件二 杨某在其运营的自媒体账号发布文章，在没有事实依据的情况下，评价某公司“搅乱市场”“打劫同
行”“无赖”“强盗”，引发社会关注，造成严重负面影响。该公司诉至法院，最终法院判决杨某公开道歉并赔
偿损失。
案件三 邬某通过某公司的 App预定境外客房，支付方式为“到店支付”，下单后即被从银行卡中扣除房款，
邬某不知情也未入住。邬某发现扣款后要求退还，而公司认为其服务条款中已注明“部分酒店住宿可能会
对您的银行卡预先收取全额预订费用”，拒绝退款。邬某诉至法院，最终法院判决该公司退还房款。

#### 设问
阅读材料，完成下表。
案件 | 体现的民法原则 | 以案说法 | 典型意义
案件一 | 守法和公序良俗原则 | ① | 对规范商家经营，保障未成年人合法权益、呵护未成年人健康成长具有重要意义。
案件二 | 诚信原则 | ② | 引导自媒体经营者树立法治意识，规范其行为，有利于提升媒体公信力，同时有利于维护良性市场竞争秩序。
案件三 | ③ | 本案所涉“服务条款”属于格式条款，公司负有向用户提示、说明的义务，只在内容复杂繁多的服务条款中约定，不足以起到提示作用，故认定公司违约。 | ④

#### 细则
19.阅读材料，完成表格。
（一）本题标准和变通
①龙某为钱某文身案例（2分）：该情境有两个问题，即合同效力问题和侵权问题：
学生可以通过把一个问题说清楚得2分，也可以通过呈现2个准确的知识点得2分
合同效力问题：限制民事行为能力人/法定代理人未追认（1分）+ 合同无效（1分）
侵权问题：龙某没有尽到核实义务/存在过错（1分）+ 侵犯身体权/健康权（1分）
呈现了两个知识点，如：钱某是限制民事行为能力人（1分）+龙某侵犯了身体权/健康
权（1分）
②杨某自媒体案例（2分）
杨某利用自媒体，故意侮辱/诽谤某公司，造成其社会评价降低（任意一个要件1分）+ 侵
害名誉权（不可替换，1分）
构成要件替换：诬陷、捏造、造谣、诋毁、抹黑、不实信息；损害形象、损害该公司声誉；
邬某服务条款案例：
③体现的民法原则（1分）：
公平原则（1分）
可替换：诚信原则（1分）
④典型意义：意义一条2分，两条3分：
第一条：维护消费者合法权益
第二条：规范格式条款的使用
如本题消费者权益和格式条款都没提到，提到规范商家经营给1分。

#### 答案落点
- 案件一可从合同效力作答：钱某是限制民事行为能力人，文身合同未经法定代理人追认，可认定无效。
- 案件一也可从侵权作答：龙某未尽核实义务或存在过错，侵犯钱某身体权、健康权。
- 案件二中，杨某利用自媒体侮辱、诽谤或发布不实信息，造成某公司社会评价降低。
- 案件二应落到侵害名誉权，不能只笼统写“不当言论”。
- 案件三中，平台服务条款属于格式条款，公司负有提示、说明义务。
- 案件三体现公平原则，也可替换为诚信原则。
- 案件三典型意义可写维护消费者合法权益、规范格式条款使用；两条都写更稳。

### 2025 · 西城 · 二模 · 第18题

- 题目来源：2025 · 西城 · 二模 · 第18题
- 框架归位：A1 民事行为与时效｜B2 判责/理由
- 同题组：本题组仅本分问。

#### 材料
17岁的小刘背着家长、绕过平台监管打赏多名网络主播，金额高达45万余元。
家长：我们发现之后，先跟主播沟通，有几位主播退了一部分钱，总计5万余元。后与平台客服沟通，想要回其余40万余元的打赏款，遭到拒绝。所以，我们现在将平台告上人民法院，要求返还充值款项。
平台：注意到小刘账号的异常消费后，采取了消费限制措施，停止了该账户的充值和打赏权限。但随后，小刘冒充监护人的身份与平台客服电话沟通，平台才解除了涉案账号的全部限制措施，平台不应承担责任。
人民法院一审判定，由被告平台退还未成年人充值款24万元。平台不服提出上诉，二审法院维持了一审判决。
【资料卡】《中华人民共和国民法典》第一百五十七条规定：民事法律行为无效、被撤销或者确定不发生效力后，行为人因该行为取得的财产应当予以返还；不能返还或者没有必要返还的应当折价补偿。有过错的一方应当赔偿对方由此所受到的损失；各方都有过错的，应当各自承担相应的责任。

#### 设问
结合材料，运用《法律与生活》的知识，分析人民法院的判决结果。

#### 细则
18．（8分）小刘为限制民事行为能力人，其大额打赏行为，家长事先不知情、事后也不同意追认，交易行为无效。平台的审核措施不完善，未能尽到合理审查的义务，存在过错。小刘父母疏于监管，未能履行好监护职责，行为存在过错。小刘沉迷打赏，并通过欺骗手段规避监管，自身行为也有过错。综合各方过错程度，根据民法典157条规定，法院判定平台和小刘父母都应承担相应责任，符合公平原则。本案判决警示，平台应健全审核机制、担当社会责任，监护人应履行监护义务，教育引导未成年人树立正确消费观。
【细则】
小刘为限制民事行为能力人（1分），其大额打赏行为，家长事先不知情、事后也不同意追认，交易行为（民事法律行为）无效。（1分）
平台的审核措施不完善，未能尽到合理审查的义务，存在过错。小刘父母疏于监管，未能履行好监护职责，行为存在过错。小刘沉迷打赏，并通过欺骗手段规避监管，自身行为也有过错。（过错分析，共3分）
综合各方过错程度，根据民法典157条规定，法院判定平台和小刘父母都应承担相应责任，符合公平原则（1分）。
判决意义：2分。引导平台健全审核机制、担当社会责任（或促进平台经济健康发展）（1分），警示监护人依法履行监护义务，或教育引导未成年人树立正确消费观。（1分）
（即规范引导平台…1分，规范引导监护人或未成年人…）

#### 答案落点
- 小刘为限制民事行为能力人，其大额打赏行为家长事先不知情、事后不同意追认，交易行为无效。
- 平台审核措施不完善，未尽到合理审查义务，存在过错。
- 小刘父母疏于监管，未能履行好监护职责，行为存在过错。
- 小刘沉迷打赏，并通过欺骗手段规避监管，自身行为也有过错。
- 综合各方过错程度，根据民法典第一百五十七条，法院判定平台和小刘父母承担相应责任，符合公平原则。
- 本案警示平台健全审核机制、担当社会责任，也警示监护人履行监护义务，教育引导未成年人树立正确消费观。

## A2 人格权与个人信息

本节共 3 个分问。

### 核心答题点和必备知识
- 核心入口：名誉、隐私、肖像、姓名、生命健康、个人信息、未成年人身心权益、平台数据使用。
- 第一判断：先锁定被保护的人格利益，再写侵害方式、损害后果、责任承担和必要的治理边界。
- 易错边界：网络、AI、平台背景不能替代具体人格权；必须写清侵犯的是哪项权利。
- 必背句：先叫准人格利益或个人信息权益，再写侵害行为、损害后果和责任。

### 2026 · 延庆 · 一模 · 第18题第1问

- 题目来源：2026 · 延庆 · 一模 · 第18题第1问
- 框架归位：A2 人格权与个人信息｜B3 诉求支持
- 同题组：本题组仅本分问。

#### 材料
技术创新犹如一把双刃剑，在带来发展机遇的同时，也伴随着诸多挑战。
材料一 近年来，在AI技术驱动下，虚拟数字人实现了由静态向动态、拟人化向真人化、单向功能向
交互功能的跨越式发展，并在新闻报道、影视制作等多个领域大放异彩。然而，随之出现的AI仿冒乱象也
对社会伦理秩序与法律规制体系提出了严峻挑战。
名词解释 案 例
利用 AI 仿冒公众人物直播营销，是指借助深度 2025 年，北京 M 公司在未经授权的情况下，
伪造、语音合成、形象模拟等 AI 技术，在未经授权 利用AI技术合成著名主持人李某的形象，在粉丝
的情况下，擅自对公众人物的外貌、声音、行为等 量88万的网络账号直播间内，将普通糖果类鱼油
特征进行高精度模拟，生成与该公众人物高度仿真 包装成具有治疗头晕、改善记忆功效的“神药”，
的虚拟数字人，进而开展直播营销活动，其目的是 售价 59.9 元/3 瓶，累计售出 17.7 万单，还伪造
利用公众人物的社会声誉、粉丝信任关系实现商业 用户评价。
流量的不当攫取。

#### 设问
（1）结合材料一，运用《法律与生活》知识，分析 M 公司涉嫌哪些违法行为，若主持人李某诉至法
院，可提出哪些诉讼请求并说明理由。（8分）

#### 细则
18.（15分）
（1）（8分）
M公司涉嫌侵犯李某的肖像权、名誉权；侵犯消费者的知情权；进行虚假和引人误解的商业宣传，构成不正当竞争。
诉讼请求：停止侵害、赔偿损失、承担诉讼费用、赔礼道歉。
事实与理由：M公司未经李某允许，利用AI技术合成李某形象用于虚假直播营销活动，不当攫取流量。M公司的行为侵犯了李某的肖像权，虚假宣传也在一定程度上影响了李某的社会评价，侵犯了李某的名誉权。被告的行为，违背了诚实信用原则，损害了原告的合法权益。
评分细则：
①违法行为3分，每个角度1分（人格权角度、消费者权益角度、不正当竞争）
②诉讼请求1分可替代
③事实1分；侵权行为1分；违背诚信原则1分；
④事实与侵权分析恰当1分（形象-肖像；虚假宣传-名誉）

#### 答案落点
- M公司涉嫌侵犯李某的肖像权、名誉权。
- M公司利用AI技术合成李某形象进行虚假直播营销，不当攫取流量，损害李某合法权益。
- M公司将普通糖果类鱼油包装成具有治疗功效的“神药”并伪造用户评价，侵犯消费者知情权。
- M公司进行虚假和引人误解的商业宣传，构成不正当竞争。
- 李某可提出停止侵害、赔偿损失、承担诉讼费用、赔礼道歉等诉讼请求。
- 事实与理由要对应：未经允许合成李某形象用于直播营销，侵犯肖像权；虚假宣传影响社会评价，侵犯名誉权。
- 被告行为违背诚实信用原则，损害原告合法权益；作答要把违法行为、诉讼请求、事实与侵权分析分别写清。

### 2026 · 石景山 · 二模 · 第19题

- 题目来源：2026 · 石景山 · 二模 · 第19题
- 框架归位：A2 人格权与个人信息｜B4 评析认识
- 同题组：本题组仅本分问。

#### 材料
2026年1月1日，新修订的《中华人民共和国治安管理处罚法》正式施行，首次将校园欺凌纳入治安管理处罚范畴，明确以殴打、侮辱、恐吓等方式实施学生欺凌的，公安机关可直接介入，对违反治安管理的欺凌行为依法处罚，同时采取矫治教育等措施。“他还是个孩子”，不再是校园欺凌的挡箭牌。
本次修订打破了“未成年人违法不拘留”的惯例，规定已满14周岁不满16周岁的未成年人，一年内两次以上违反治安管理的，依法执行行政拘留；已满14周岁不满18周岁，初次违反治安管理但情节严重、影响恶劣的，依法执行行政拘留。实践中，涉事未成年人往往存在“失管失教”或“失学辍学”等问题，处罚同步通知学校和家长，并启动后续帮教，形成“惩教闭环”。本次修订在遵循“教育为主、惩罚为辅”原则的同时，传递出“法不能向不法让步”的鲜明导向，对“教育与惩罚”的关系作出精准再平衡。

#### 设问
结合材料，运用《法律与生活》知识，谈谈对未成年人校园欺凌违法行为“惩”“教”并行的认识。

#### 细则
19．（8分）从“惩”“教”两个维度出发，正确表述1条法律依据+1点实践意义，得4分；2点得8分。
依据民法典，自然人享有生命权、身体权、健康权等人格权以及财产权，本次修订通过明确处罚标准，强化了对未成年人校园欺凌违法行为的惩罚，/为保护学生合法权益提供了更有力的法律支持，/有利于营造尊法学法守法用法的良好氛围、切实维护校园和谐稳定。（4分）民法典规定父母有对未成年子女的行为进行必要的约束和引导以及批评教育、合理惩戒的义务。本次修订倡导“惩教闭环”，强化执法机关、家庭、学校等机构形成协同治理合力，/既让未成年人认识到法律威严，又通过系统化矫治教育帮助未成年人树立法治观念，/真正帮助涉事未成年人回归正途。（4分）

#### 答案落点
- 认识“惩”“教”并行，要分别写出法律依据和实践意义。
- 惩的依据：自然人享有生命权、身体权、健康权等人格权以及财产权，修订处罚标准强化对校园欺凌违法行为的惩罚。
- 惩的意义：为保护学生合法权益提供更有力法律支持，也有利于营造尊法学法守法用法的氛围、维护校园和谐稳定。
- 教的依据：民法典规定父母有对未成年子女进行必要约束、引导、批评教育和合理惩戒的义务。
- 教的意义：倡导“惩教闭环”，推动执法机关、家庭、学校等形成协同治理合力。
- 惩教并行既让未成年人认识法律威严，也通过系统化矫治教育帮助其树立法治观念、回归正途。

### 2026 · 顺义 · 二模 · 第18题第2问

- 题目来源：2026 · 顺义 · 二模 · 第18题第2问
- 框架归位：A2 人格权与个人信息｜B6 维权路径
- 同题组：本题组仅本分问。

#### 材料
材料二：2026年一款名为OpenClaw的开源AI智能体风靡。它能接管键盘鼠标，自动整理文件、起草邮件、填写表格、分析数据，图标是一只鲜红龙虾。开源智能体能力不断扩展的同时，也出现了新的风险：有人账户里的钱被悄悄转走，有人电脑被黑客远程控制，还有人积累多年的工作文件被一键清空。

#### 设问
结合材料，运用法治知识，谈谈该开源智能体可能会侵犯用户的哪些民事权利，并分析如何规避该开源智能体在推广应用过程中的风险。（8分）

#### 细则
18（2）（8分）该开源智能体可能侵犯用户的财产权、隐私权、个人信息利益等。
必修3《政治与法治》角度：立法机关科学立法，针对人工智能等新兴技术领域，及时制定和完善相关法律法规，充分保护用户的合法权益；推进严格执法，全面履行政府职能，加强市场监管和网络安全监管职能；推进公正司法，维护人民权益；推进全民守法，增强权利意识和义务观念，了解开源智能体相关法律知识，提升风险识别能力。
选必2《法律与生活》角度：民法典明确规定保护用户人身权益和财产权益。任何组织或者个人不得侵害他人的财产权、隐私权，处理个人信息应遵循合法、正当、必要原则。当用户人格权益和财产权益受到侵害时，权利人可通过协商、调解、仲裁、诉讼等途径维护自身权益，可依法请求行为人停止侵害、排除妨碍、消除危险、赔礼道歉等；造成损害的，还可依法请求损害赔偿。

#### 答案落点
- 该开源智能体可能侵犯用户财产权、隐私权、个人信息利益等民事权益。
- 选必二角度：民法典保护用户人身权益和财产权益，任何组织或个人不得侵害他人财产权、隐私权。
- 处理个人信息应遵循合法、正当、必要原则，不能借开源智能体推广非法收集、滥用或泄露个人信息。
- 权利受到侵害时，用户可通过协商、调解、仲裁、诉讼等途径维权，请求停止侵害、排除妨碍、消除危险、赔礼道歉、损害赔偿。
- 必修三角度：应针对人工智能等新兴技术领域及时制定和完善法律法规，充分保护用户合法权益。
- 政府应严格执法，加强市场监管和网络安全监管；司法机关应公正司法，依法维护人民权益。
- 用户和开发者应推进全民守法，增强权利意识和义务观念，了解开源智能体相关法律知识，提升风险识别能力。

## A3 物权相邻与共有

本节共 8 个分问。

### 核心答题点和必备知识
- 核心入口：所有权、财产权、共有部分、相邻通行、采光、加装电梯、业主共同决定、物业服务、绿色居住。
- 第一判断：先找不动产或财产权边界，再落到有利生产、方便生活、团结互助、公平合理。
- 易错边界：多数人同意不等于少数人合法权益自动消失；物业和相邻关系要分清合同义务与物权边界。
- 必背句：先判权利归属、共有或相邻边界，再处理公平合理和实际影响。
END_CHUNK_CONTENT
