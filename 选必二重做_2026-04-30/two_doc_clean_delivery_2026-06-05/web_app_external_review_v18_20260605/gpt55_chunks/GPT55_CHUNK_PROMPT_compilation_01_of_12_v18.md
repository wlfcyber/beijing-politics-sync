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
Chunk: 1/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-01
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
# 选必二《法律与生活》试题和细则汇编

本汇编只保留题目来源、材料、设问、细则、答案落点、同题组，供学生按真题材料和评分口径复盘。

## 覆盖总览

- 分问总数：74
- 同题组数量：64

### 2024 · 东城 · 一模 · 第19题

- 题目来源：2024 · 东城 · 一模 · 第19题
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
- 19.（6分）法律规定诉讼时效有助于督促当事人积极主张权利，推动纠纷解决，节约司法资源。
- 赡养问题事关老年人的基本生存权利，成年子女对父母有赡养的义务。
- 请求支付赡养费不适用诉讼时效的规定有助于保护老年人的合法权益，彰显公序良俗，体现人文关怀，构建和谐家庭。

### 2024 · 东城 · 二模 · 第19题第1问

- 题目来源：2024 · 东城 · 二模 · 第19题第1问
- 同题组：2024 · 东城 · 二模 · 第19题第1问；2024 · 东城 · 二模 · 第19题第2问

#### 材料
甲公司从乙公司购入一批电视，约定2024年3月10日发货。乙公司如约发
货后，甲公司不便收货，双方约定货物由快递仓库代为储存至3月20日，仓储费用
由乙公司承担。3月19日，甲公司表示依然不便收货，需要延长仓储时间至3月
30日，乙公司回复“可以”。双方无其他磋商内容。
3月30日，甲公司收货并垫付全部仓储费用后，向乙公司要求“尾款扣除仓储
费用后支付”，乙公司表示拒绝承担3月21日及以后的仓储费用，甲公司因此拒绝
支付尾款。双方协商未果，欲通过诉讼解决争议。

#### 设问
（1）请你选择其中一方进行代理，并撰写起诉状。（7分）
民事起诉状
原告：
被告：
诉讼请求：
事实与理由：
望法院判如所请。

#### 细则
题号与设问：19（1）请你选择其中一方进行代理，并撰写起诉状（7分）。
参考答案示例一：
原告：甲公司；被告：乙公司。
诉讼请求：1.请求判令被告承担全部仓储费用；2.请求判令被告承担本案诉讼费用。
事实与理由：
事实：我司于2024年3月10日自乙公司购买一批电视，因收货不便，该批货物由快递代为储存，且约定3月20日及以前的仓储费用由卖方承担。3月19日，我司与被告协商再延长10天，获得肯定答复。3月30日，我司收货并垫付全部仓储费用，但乙公司拒绝承担3月21日及以后产生的仓储费用。
理由：3月19日，我司“再延长10天”的真实意思为“时间延长10天，且期间仓储费用由卖方承担”。我方属于以默示方式，延续此前仓储费用全部由卖方承担的交易习惯，续签协议。因此，本案所涉全部仓储费用及诉讼费应由卖方承担。
阅卷细则：
原告被告不给分。
示例一：原告甲公司、被告乙公司。
诉讼请求：判令被告承担全部仓储费用或继续履行，被告承担本案诉讼费用（2分）。
事实与理由中的事实：我公司于2024年3月10日自乙公司购买一批电视，因收货不便，该批货物由快递代为储存，且约定3月20日及以前的仓储费用由卖方承担。3月19日，我公司与被告协商再延长10天，获得肯定答复。3月30日，我公司收货并垫付全部仓储费用，但乙公司拒绝承担3月21日及以后产生的仓储费用。（踩意2分）
理由：①我公司提出延长仓储时间，乙公司作出肯定答复（材料表述为“可以”），应按原合同内容全面履行，乙公司的行为违背诚信原则。②乙公司拒绝承担3月21日以后产生的仓储费用，并未与我公司协商一致，属于单方变更合同行为；其行为构成违约，应当承担违约责任。（1个理由2分，2个理由3分）
示例二：原告乙公司、被告甲公司。
诉讼请求：判令被告支付尾款或继续履行，被告承担本案诉讼费用（2分）。
事实：甲公司于2024年3月10日自我公司购买一批电视，因收货不便，该批货物由快递代为储存，且约定3月20日及以前的仓储费用由我公司承担。3月19日，被告与我司协商再延长10天，我公司同意。3月30日，甲公司收货后，我公司不同意支付3月21日及以后产生的仓储费用，甲公司拒不支付合同尾款。（踩意2分）
理由：①3月19日提出新合同，合同只对延期进行约定，并未协商延长仓储时间的费用承担问题，但由于费用产生由甲公司原因导致，该笔费用理应由甲公司承担，若逾期产生的费用仍由我方承担，有违公平原则。（只谈要约承诺构成新合同给1分，有公平原则给2分）②买卖合同有效，甲公司不支付尾款违反全面履行原则；其行为构成违约，应承担违约责任。（1个理由2分，2个理由3分）

#### 答案落点
- 可选择原告甲公司或原告乙公司，但要始终站在同一方立场写起诉状。
- 若代理甲公司：写明原告甲公司、被告乙公司，并提出判令乙公司承担全部仓储费用或继续履行、承担本案诉讼费用。
- 事实部分要交代3月10日购买电视、因收货不便由快递代为储存、3月20日及以前仓储费由卖方承担、3月19日协商再延长10天、3月30日收货并垫付全部仓储费用、乙公司拒绝承担3月21日以后费用。
- 理由部分要说明“再延长10天”的真实意思是时间延长10天且期间仓储费用仍由卖方承担。
- 应写出以默示方式延续此前仓储费用由卖方承担的交易习惯，或续签、补充协议的判断。
- 乙公司拒绝承担3月21日以后仓储费用，未与甲公司协商一致，属于单方变更合同行为，违背诚信原则和全面履行原则。
- 若代理乙公司：可提出甲公司支付合同尾款或继续履行，并说明3月19日只约定延期、未约定后续仓储费用由乙公司承担；甲公司拒付尾款违反全面履行原则，也可从公平原则说明逾期费用应由甲公司承担。

### 2024 · 东城 · 二模 · 第19题第2问

- 题目来源：2024 · 东城 · 二模 · 第19题第2问
- 同题组：2024 · 东城 · 二模 · 第19题第1问；2024 · 东城 · 二模 · 第19题第2问

#### 材料
甲公司从乙公司购入一批电视，约定2024年3月10日发货。乙公司如约发
货后，甲公司不便收货，双方约定货物由快递仓库代为储存至3月20日，仓储费用
由乙公司承担。3月19日，甲公司表示依然不便收货，需要延长仓储时间至3月
30日，乙公司回复“可以”。双方无其他磋商内容。
3月30日，甲公司收货并垫付全部仓储费用后，向乙公司要求“尾款扣除仓储
费用后支付”，乙公司表示拒绝承担3月21日及以后的仓储费用，甲公司因此拒绝
支付尾款。双方协商未果，欲通过诉讼解决争议。

#### 设问
（2）为避免类似问题产生，我们应该________。（2分）

#### 细则
19.（9分）
（2）树立合同意识，合同内容应清晰明确。合同缺少重要条款时，双方当事人应当秉持诚
信原则，平等协商，对合同进行补充或解释，补全意思表示。

#### 答案落点
- 19.（9分）（2）树立合同意识，合同内容应清晰明确。
- 合同缺少重要条款时，双方当事人应当秉持诚信原则，平等协商，对合同进行补充或解释，补全意思表示。

### 2024 · 丰台 · 一模 · 第17题

- 题目来源：2024 · 丰台 · 一模 · 第17题
- 同题组：本题组仅本分问。

#### 材料
《中华人民共和国民法典》第一千二百一十七条：非营运机动车发生交通事故造成无偿搭乘人损害，属于该机动车一方责任的，应当减轻其赔偿责任，但是机动车使用人有故意或重大过失的除外。

资料卡：好意同乘，指驾驶人基于善意互助或友情帮助，无偿搭载他人或允许他人无偿搭乘的情谊行为。

甲某搭乙某的车出行，上车后未听乙某提醒系好安全带。乙某在驾驶过程中因雨天路滑，撞到灯杆，造成甲某受伤住院。为此，乙某主动垫付了部分医疗费用。甲某认为，本次交通事故对自己造成严重人身财产损害，乙某应承担全部责任，向其赔付医疗费、误工费和护理费等损失。乙某认为自己好意让甲某免费搭乘，由于客观原因发生意外，并无过错，不应该承担全部责任。两人为此诉至法院。

法院综合考虑本案好意同乘时的具体情况、事故事实以及被告乙某主动承担部分责任的行为等，酌情减轻乙某赔偿责任。

#### 设问
结合材料，运用《法律与生活》知识，谈谈法院酌情减轻被告赔偿责任的法理依据和现实意义。

#### 细则
参考答案：法院判决应以事实为依据，以法律为准绳。本案中，驾驶人乙某和搭乘人甲某之间形成好意同乘关系。驾驶人对搭乘人的生命财产安全负有保障义务，被告乙某发生交通事故，造成原告甲某受伤，侵犯了其生命权、健康权，需要承担相应责任。被告乙某在原告甲某受伤一事上，固然存在过错，但并非故意或重大过失，原告甲某诉请其承担全部赔偿责任，有违民事活动的公平原则，根据民法典和好意同乘相关规定，应当减轻被告乙某的赔偿责任。法院判决有利于维护双方合法权益，促进社会公平，对维持人际关系和谐，弘扬社会主义核心价值观及减少交通拥堵、倡导绿色出行具有积极意义。
评分标准说明：本题8分，法理依据5分，现实意义3分。法理依据方面，“法院判决应以事实为依据，以法律为准绳”为必踩点1分；双方形成好意同乘并明确权利义务、侵权责任2分；结合好意同乘减轻赔偿责任条件和案件实际2分。现实意义可从个人、国家司法、社会发展角度作答，涉及维护双方合法权益、保障公正司法、弘扬社会主义核心价值观等，每点1分，共3分。

#### 答案落点
- 法院判决应以事实为依据、以法律为准绳。
- 甲某与乙某之间形成好意同乘关系，驾驶人对搭乘人的生命、健康和财产安全负有合理保障义务。
- 乙某发生交通事故造成甲某受伤，侵犯甲某生命权、健康权，应承担相应侵权责任。
- 乙某并非故意或重大过失，且甲某未按提醒系好安全带；甲某要求乙某承担全部赔偿责任有违公平原则。
- 根据民法典好意同乘相关规定，法院可以酌情减轻乙某赔偿责任。
- 该判决有利于维护双方合法权益、促进社会公平，也有利于维持人际关系和谐、弘扬社会主义核心价值观。

### 2024 · 丰台 · 二模 · 第17题

- 题目来源：2024 · 丰台 · 二模 · 第17题
- 同题组：本题组仅本分问。

#### 材料
民法典守护碧水蓝天，保护生态环境。
《中华人民共和国民法典》规定：“民事主体从事民事活动，应当有利于节约资
源、保护生态环境。”“民事主体依法享有知识产权。”“因污染环境、破坏生态造成他
人损害的，侵权人应当承担侵权责任。”
案例一
某公司发明专利技术从源头上解决长期污水
污泥分离不彻底、处理工序复杂化等关键技
术问题，首次提出了通过操控屏控制移动杆，
实现过滤速度可控的农村污水分离技术重大
突破，方法简单、易于操作，降低污水净化
成本的同时，显著提高污水净化效率，延长
装置的使用寿命，已在多地村庄生活污水治
理项目中成功应用并推广。
案例二
甲公司在生产中，长期存在超标排放废
水、废气等污染物损害环境公共利益的
行为，周边居民的日常生活受到严重影
响。乙环境研究所以甲公司存在长期连
续超标排放污染物、构成环境民事侵权
为由，提起环境民事公益诉讼。法院审
理后判决甲公司立即停止侵权、消除危
险、赔偿环境损失等。

#### 设问
运用《法律与生活》知识，结合上述案例分析民法典的相关规定对保护生态环境
的作用。

#### 细则
17.运用《法律与生活》知识，结合上述案例分析民法典的相关规定对保护生态环境的作用。（8分）
参考答案：民法典规定的绿色原则为生态环境保护提供了基本遵循。在上述案例中，民法典强调对知识产权的保护，能够鼓励技术创新，为生态环境保护提供技术支撑。依据民法典规定，甲公司污染、破坏环境应承担相应的侵权责任。民法典上述条款合理地确定了民事主体的权利义务，既能保护合法权益，又能惩罚违法行为，有助于平衡个人利益和公共利益，合理预防损害，维护良好的生态环境。
【拓展答案】：
增强环保意识、维护社会公平正义。
评分标准说明：
民法典规定的绿色原则为生态环境保护提供了基本遵循。（1分）在上述案例中，民法典强调对知识产权的保护，能够鼓励技术创新，为生态环境保护提供技术支撑。（2分）依据民法典规定，甲公司污染、破坏环境应承担相应的侵权责任。（1分）民法典上述条款合理地确定了民事主体的权利义务，既能保护合法权益，又能惩罚违法行为，有助于平衡个人利益和公共利益，合理预防损害，维护良好的生态环境。（4分）（权利义务、个人利益和公共利益、维护良好的生态环境三个点都写到就给4分。）

#### 答案落点
- 民法典绿色原则为生态环境保护提供基本遵循。
- 民法典保护知识产权，能够鼓励案例一中的环保技术创新，为生态环境保护提供技术支撑。
- 依据民法典，案例二中甲公司污染、破坏环境造成损害，应承担相应侵权责任。
- 相关规定合理确定民事主体的权利与义务，既保护合法权益，又惩罚违法行为。
- 这些规定有助于平衡个人利益与公共利益，合理预防损害，维护良好生态环境。
- 也可从增强环保意识、维护社会公平正义角度补充说明意义。

### 2024 · 朝阳 · 一模 · 第19题

- 题目来源：2024 · 朝阳 · 一模 · 第19题
- 同题组：本题组仅本分问。

#### 材料
诚信是法治精神的重要伦理基础。民法典第七条规定：“民事主体从事民事活动，应当遵循诚信原则，秉持诚实，恪守承诺。”

镜头一：2022年12月，A公司与B公司签订购销合同约定：A公司向B公司提供产品，货款于发货后的60日内付清。2023年1月，A公司依约向B公司提供货物，但截至2023年7月，B公司欠A公司货款590万元未支付。2023年8月，A公司起诉B公司，要求其支付货款及违约金。人民法院最终判决B公司尽快付清全部欠款并支付逾期违约金。

镜头二：某购物中心为200余家商户建立了“码上诚信”二维码，消费者扫描二维码，即可查询此商户相关的行政许可、行政处罚、主动承诺、自愿注册等信用信息。有市民说：“我经常来这个商场消费，一是因为‘码上诚信’让我感觉在这里购物很放心，二是因为这里的商品质量和售后服务态度都很好。”

#### 设问
结合材料，运用《法律与生活》知识，分析诚信原则对促进社会主义市场经济健康发展的积极作用。

#### 细则
19.（7分）
社会主义市场经济本质上是法治经济。民法典将诚信原则确立为基本原则之一，凸显了社会主义核心价值观对社会主义市场经济建设的引导和规范。
诚信原则要求合同当事人按照约定全面履行义务，有利于规范民事主体行为，尊重和维护民事主体合法权利；司法机关可根据诚信原则定分止争，维护公平正义，维护诚信、健康的市场秩序。
诚信原则要求经营者依法、诚信经营，保护消费者的合法权益。这不仅有利于平衡经营者与消费者之间的关系，而且有助于守法诚信的经营者扩大市场，并最终增进社会整体福祉。

#### 答案落点
- 19.（7分）社会主义市场经济本质上是法治经济。
- 民法典将诚信原则确立为基本原则之一，凸显了社会主义核心价值观对社会主义市场经济建设的引导和规范。
- 诚信原则要求合同当事人按照约定全面履行义务，有利于规范民事主体行为，尊重和维护民事主体合法权利；
- 司法机关可根据诚信原则定分止争，维护公平正义，维护诚信、健康的市场秩序。
- 诚信原则要求经营者依法、诚信经营，保护消费者的合法权益。
- 这不仅有利于平衡经营者与消费者之间的关系，而且有助于守法诚信的经营者扩大市场，并最终增进社会整体福祉。
END_CHUNK_CONTENT
