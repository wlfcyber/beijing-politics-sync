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
Chunk: 3/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: baodian-03
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2026 · 西城 · 一模 · 第17题

- 题目来源：2026 · 西城 · 一模 · 第17题
- 框架归位：A3 物权相邻与共有｜B6 维权路径
- 同题组：本题组仅本分问。

#### 材料
良好生态环境是最公平的公共产品，是最普惠的民生福祉。
【民法典物权编】
第286条：
业主应当遵守法律、法规以及管理规约，相关行为应当符合节约资源、保护生态环境的要求。对于物业服务企业或者其他管理人执行政府依法实施的应急处置措施和其他管理措施，业主应当依法予以配合。
业主大会或者业主委员会，对任意弃置垃圾、排放污染物或者噪声等损害他人合法权益的行为，有权依照法律、法规以及管理规约，请求行为人停止侵害、排除妨碍、消除危险、恢复原状、赔偿损失。
……
第294条：不动产权利人不得违反国家规定弃置固体废物，排放大气污染物、水污染物、土壤污染物、噪声、光辐射、电磁辐射等有害物质。
第326条：用益物权人行使权利，应当遵守法律有关保护和合理开发利用资源、保护生态环境的规定。所有权人不得干涉用益物权人行使权利。

#### 设问
结合材料，运用法律相关知识，说明民法典物权编的上述规定如何推动国家绿色发展。

#### 细则
17.结合材料，运用法律相关知识，说明民法典物权编的上述规定如何推动国家绿色发展。（8分）
【细则】
●法律依据（2分）
贯彻落实民法绿色原则 1分
为绿色发展提供法律依据/法律保障/使生态环境保护有法可依 1分
●作用路径（4分）
合理划定权利界限、强化法定义务、明确法律责任与权利救济（变通：禁止违法排污/明确侵权责任减少环境损害/坚持权利与义务统一/强化权利救济/协调各方利益关系） 3分
结合法条内容，分析合理 1分
●意义价值（2分）
平衡个人利益和生态公共利益/公共利益/社会利益 1分
促进资源开发利用绿色转型/推动可持续发展/节约资源保护环境 1分

#### 答案落点
- 17.结合材料，运用法律相关知识，说明民法典物权编的上述规定如何推动国家绿色发展。
- （8分）【细则】●法律依据（2分）贯彻落实民法绿色原则 1分为绿色发展提供法律依据/法律保障/使生态环境保护有法可依 1分●作用路径（4分）合理划定权利界限、强化法定义务、明确法律责任与权利救济（变通：禁止违法排污/明确侵权责任减少环境损害/坚持权利与义务统一/强化权利救济/协调各方利益关系） 3分结合法条内容，
- 分析合理 1分●意义价值（2分）平衡个人利益和生态公共利益/公共利益/社会利益 1分促进资源开发利用绿色转型/推动可持续发展/节约资源保护环境 1分

### 2026 · 通州 · 期末 · 第19题第1问

- 题目来源：2026 · 通州 · 期末 · 第19题第1问
- 框架归位：A3 物权相邻与共有｜B2 判责/理由
- 同题组：本题组仅本分问。

#### 材料
【案件事实】
某小区3号楼2单元全体业主一致签字同意增设电梯，并于小区主要出入口张贴意见征集单、公示、承诺及图纸等相关材料，公示期间未收到异议。随后，该项目取得了主管部门的审批手续并正式开工。居住于相邻楼的业主范某认为，电梯安装位置影响其采光，侵犯其合法权益，遂多次在现场阻碍施工，导致项目停工。2单元全体业主向人民法院起诉，请求判令范某停止对加装电梯工程的妨害行为。法院经现场勘查，案涉加装电梯采用全玻璃设计，未对相邻楼采光造成影响，遂判决范某停止对电梯加装工程的阻挠行为。同时，法院明确，若电梯投入使用后，确在采光、通风等方面对部分业主造成较大影响，相关权利人可就补偿事宜另行协商或通过法律途径解决。

【法律依据】
《中华人民共和国民法典》（节选）
第二百九十二条：不动产权利人因建造、修缮建筑物以及铺设电线、电缆、水管、暖气和燃气管线等必须利用相邻土地、建筑物的，该土地、建筑物的权利人应当提供必要的便利。
第二百九十六条：不动产权利人因用水、排水、通行、铺设管线等利用相邻不动产的，应当尽量避免对相邻的不动产权利人造成损害。

#### 设问
（1）结合材料，运用《法律与生活》知识，分析判决结果并说明理由。

#### 细则
（1）（8分）
法院判决以事实为根据，以法律为准绳。老旧小区加装电梯属民生工程，已获法定比例业主同意，程序合法。电梯采用玻璃幕墙设计，在提升本楼业主出行便利的同时，能尽量减少对相邻楼业主的影响。依据《中华人民共和国民法典》规定，不动产的相邻权利人应当按照有利生产、方便生活、团结互助、公平合理的原则，正确处理相邻关系。本案判决维护了相邻业主合法权益，有助于促进邻里和谐，践行友善的社会主义核心价值观。

#### 答案落点
- 法院判决以事实为根据、以法律为准绳，支持2单元业主请求，判令范某停止阻碍加装电梯。
- 老旧小区加装电梯属民生工程，已获法定比例业主同意，程序合法，并已取得主管部门审批手续。
- 电梯采用全玻璃设计，法院现场勘查认定未对相邻楼采光造成影响，能尽量减少对相邻楼业主的影响。
- 依据民法典，不动产权利人因建造、修缮建筑物等必须利用相邻土地、建筑物的，相邻权利人应提供必要便利。
- 依据民法典，不动产权利人利用相邻不动产时，应尽量避免对相邻的不动产权利人造成损害。
- 相邻权利人应按照有利生产、方便生活、团结互助、公平合理原则正确处理相邻关系。
- 本案判决维护相邻业主合法权益，有助于促进邻里和谐，践行友善的社会主义核心价值观。

## A4 合同与诚信

本节共 14 个分问。

### 核心答题点和必备知识
- 核心入口：要约、承诺、合同成立、合同效力、履行、违约、格式条款、补充协议、诚实信用。
- 第一判断：先判断合同是否成立有效、内容是否明确，再写全面履行、诚信协商、违约责任。
- 易错边界：不能只喊诚信，要把约定、回复、履行、违约事实压进规则。
- 必背句：先判断合同成立生效和约定内容，再写全面履行、诚信履行和违约责任。

### 2024 · 东城 · 二模 · 第19题第1问

- 题目来源：2024 · 东城 · 二模 · 第19题第1问
- 框架归位：A4 合同与诚信｜B6 维权路径
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
- 框架归位：A4 合同与诚信｜B7 短答识别
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
19（2）（2分）
树立合同意识，合同内容应清晰明确。合同缺少重要条款时，双方当事人应当秉持诚信原则，平等协商，对合同进行补充或解释，补全意思表示。

#### 答案落点
- 树立合同意识，合同内容应清晰明确。
- 合同缺少重要条款时，双方当事人应当秉持诚信原则，平等协商。
- 双方应对合同进行补充或解释，补全意思表示。

### 2024 · 朝阳 · 一模 · 第19题

- 题目来源：2024 · 朝阳 · 一模 · 第19题
- 框架归位：A4 合同与诚信｜B5 意义价值
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

### 2024 · 石景山 · 一模 · 第17题

- 题目来源：2024 · 石景山 · 一模 · 第17题
- 框架归位：A4 合同与诚信｜B2 判责/理由
- 同题组：本题组仅本分问。

#### 材料
2023 年 12 月 28 日，北京市第三中级人民法院终审公开宣判北京甲环保公司与四川乙发电公司合同纠纷一案，该案系北京市首例碳排放权交易纠纷案件。
【基本案情】
2021 年12 月，乙公司就采购碳排放配额发布比选公告，甲公司向其进行报价，内容具体明确，并承诺：如未依约履行，乙公司可另行购买等量的碳排放配额；如有差价， 由甲公司补足。乙公司经过比选确认甲公司中标，并向其送达了中标通知。此后，甲公 司明确表示不再履行合同，在此情况下，乙公司另行与第三方公司签订合同，以高于甲 公司所报交易单价的价格购买了相应碳排放配额，由此产生差价，故乙公司诉至法院， 要求甲公司向其支付差价款 289 万余元及相应利息。
【法院判决】
一审法院经审理，认为甲乙两公司就涉案碳排放配额采购事项成立合同关系，且该合同合法有效。判决甲公司向乙公司支付碳排放配额采购差价款289 万余元及相应利息。一审后，甲公司不服判决，向北京三中院提起上诉。北京三中院经审理后作出终审判决： 驳回上诉，维持原判。

#### 设问
运用法律知识，结合案情，说明甲乙两公司合同成立的理由，并从民法基本原则角 度阐述该司法判决的意义。

#### 细则
甲公司参与比选并向乙公司进行报价，内容具体确定，属于要约。乙公司确认甲公司中标，向其送达了中标通知，属于承诺。中标通知书送达甲公司，故双方合同成立。（3分）
法院判决引导碳排放配额交易的民事主体遵循诚信原则、公平原则、绿色原则。有利于推动企业转型升级，兼顾经济效益和社会效益；有利于维护我国碳排放权交易市场的正常秩序，推动要素市场化改革，落实“碳达峰、碳中和”国家重大决策。（5分）

#### 答案落点
- 甲公司参与比选并向乙公司报价，内容具体确定，属于要约。
- 乙公司确认甲公司中标，并向其送达中标通知，属于承诺。
- 中标通知书送达甲公司，双方合同成立，且合同合法有效。
- 甲公司明确表示不再履行合同，乙公司另行高价购买碳排放配额产生差价，甲公司应按承诺承担相应责任。
- 该判决引导碳排放配额交易主体遵循诚信原则、公平原则和绿色原则。
- 该判决有利于推动企业转型升级，兼顾经济效益和社会效益。
- 该判决有利于维护碳排放权交易市场秩序，推动要素市场化改革，落实碳达峰、碳中和决策。
END_CHUNK_CONTENT
