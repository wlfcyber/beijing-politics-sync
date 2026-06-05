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
Chunk: 7/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-07
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2025 · 海淀 · 期末 · 第21题

- 题目来源：2025 · 海淀 · 期末 · 第21题
- 同题组：本题组仅本分问。

#### 材料
阅读材料，完成问题。
“竞业限制”是指用人单位与劳动者之间约定，劳动者在离职后不得到生产同类产品或经营同类产业且有竞争关系的其他用人单位任职，也不得自己生产与原单位有竞争关系的同类产品或经营同类业务。
案例一：李某是A公司自主培养的高级管理人员。在职期间，李某与该公司签订了保密协议和竞业限制协议。两年后，李某离职，次日即入职相同经营范围和业务的B公司，任职相同岗位，负责相同产品生产。该产品生产技术属A公司“不为公众所知悉的技术信息”，A公司将李某诉至法院。法院经审理认为，李某违反了竞业限制义务，判决其向A公司支付赔偿金。
案例二：厨师刘某在某餐饮公司从事拌黄瓜等冷菜制作。公司认为刘某在制作过程中会掌握一些菜品秘方，双方签署了保密及竞业限制协议。刘某从该公司离职后，到其他餐馆从事冷菜制作。原公司以违反竞业限制协议为由起诉刘某，要求赔偿违约金及损失。法院经审理认为，餐饮公司与刘某签订的竞业限制协议应属无效。

#### 设问
结合材料，运用《法律与生活》知识，说明法律规定“竞业限制”并对其加以限制的原因。

#### 细则
释义
法条
案例
角度 | 答案要点
规范
“竞业限制” | 【意义】
有利于企业商业秘密保护 / 保护知识产权 / 推动社会创新
| 【案例一分析】
李某作为负有保密义务的劳动者，泄露公司商业秘密/ 违反协
议约定，应当承担违约责任。
对“竞业限制”的限制 | 【意义】
若不对“竞业限制”加以限制则可能侵犯劳动者的基本劳动权利
/阻碍人才资源合理配置
| 【案例二分析】
刘某作为公司普通员工，并非负有保密义务的人员，餐饮公司与
其签订的竞业限制协议违反了相关法律规定，协议无效。
综合 | 平衡劳动者合法权益与企业商业秘密保护
分
析
角度 | 评分细则
意义
（6分） | 【规范“竞业限制”】
有利于企业商业秘密保护 / 保护知识产权 / 推动社会创新
（以上出现任意两条给2分)
【对“竞业限制”的限制】
保护劳动者的基本劳动权利 / 有利于人才资源合理配置
（以上出现任意一条给2分)
【总结】：
平衡劳动者合法权益与企业商业秘密保护（2分）
（替代答案：维护市场公平竞争 / 遵循公平原则 /权利和义务相统一，给1分）
案例分析
（2分） | 【案例一分析1分】
李某作为负有保密义务的劳动者，泄露公司商业秘密，违反协议约
定，应当承担违约责任。 （以上出现任意一条给1分)
【案例二分析1分】
刘某作为公司普通员工，并非负有保密义务的人员，餐饮公司与其签订的竞业限制协议违反了相关法律规定，协议无效。
（以上出现任意一条给1分)

#### 答案落点
- 规范竞业限制有利于企业商业秘密保护、保护知识产权、推动社会创新。
- 对竞业限制加以限制，可以保护劳动者的基本劳动权利，促进人才资源合理配置。
- 案例一：李某作为负有保密义务的劳动者，泄露公司商业秘密或违反协议约定，应当承担违约责任。
- 案例二：刘某作为公司普通员工，并非负有保密义务的人员，餐饮公司与其签订的竞业限制协议违反法律规定，协议无效。
- 综合：在劳动者合法权益与企业商业秘密保护之间实现平衡。

### 2025 · 石景山 · 一模 · 第20题

- 题目来源：2025 · 石景山 · 一模 · 第20题
- 同题组：本题组仅本分问。

#### 材料
(8分)
新质生产力鼓励新业态拓展创新。人民法院能动履职、保护创新，为发展新质生产力提供重要保障。下列
是石景山法院以司法护航新质生产力发展的两个案例。
案例一
集成电路产业是信息产业的核心，为新质生产力发展提供重要支撑。原告科技公司与被告电路公司就某集
成电路技术研发项目签订委托合同，约定由被告按相关技术标准在规定时间内完成产品研发交付，原告分
期付酬 16万元。研发过程中，原告支付了两期研发费共 9.6万元，经检验，阶段性产品未达合同要求且研
发进度超期。被告延期交付最终成果后，原告主张被告未能依约提交达标成果，错过上市时机，致原告经
济损失严重，故要求被告返还研发费用并支付违约金。法院经审理，判令被告返还原告服务费、违约金共
计11万余元。
案例二
软件是信息技术关键载体，是新质生产力的代表和数字经济发展的基础。“好省”APP是原告某网络科技公
司旗下的一款电商导购应用，用户可在其中领取主流商城的商品优惠券，故该软件上线后下载量巨大。被
告周某是被诉软件“超好省-省钱助手”APP的开发运营者，该软件晚于原告软件三年上线。原告主张“好
省”软件经其长期宣传已具有影响力，被告软件与原告软件名称和图标相近、内容业务相同，已造成公众
混淆，请求法院判令被告停止不当行为并赔偿损失。法院经审理，判令被告停止侵权并赔偿原告损失共计
3.6万元。

#### 设问
参考示例，完成下表。
案例一：裁判理由为①；对发展新质生产力的保障作用为“维护守约方合法权益，激励从业者秉持契约精神和敬业态度，着力提升创新研发能力，促进集成电路产业扩容提质，为新质生产力发展提供重要支撑。”
案例二：裁判理由为“根据反不正当竞争法规定，禁止经营者实施不正当竞争行为。原被告两款软件功能相似，存在竞争关系。被告擅自使用与原告名称、图标相似的软件，容易使消费者发生混淆误认，构成不正当竞争，应当承担停止侵害、赔偿损失的侵权责任”；对发展新质生产力的保障作用为②。

#### 细则
20.（8分）任务类型：解释与论证（法理依据+事实依据+对发展新质生产力的保障作用）。
法理依据：①根据民法典规定，当事人不履行合同义务或者履行合同义务不符合约定的，守约方可以要求违约方承担违约责任。
采点赋分：对应案例一，学生能够从民法典角度说明，准确分析其中一方面得2分；准确分析两方面得4分。
事实依据：①被告开发时间超过履行期限，阶段性产品未达合同约定标准，构成违约，应当承担违约责任。
案例二：根据反不正当竞争法，被告构成不正当竞争，应当承担停止侵害、赔偿损失的侵权责任。准确回答一点得2分；准确回答两点得4分。答非所问或没有应答得0分。
保障作用：②依法打击不正当竞争行为，维护消费者知情权和选择权，保护知识产权，保护经营者的合法权益，维护公平竞争的市场秩序，营造良好营商环境，为数字经济发展提供法治保障。

#### 答案落点
- 案例一：当事人不履行合同义务或者履行合同义务不符合约定的，守约方可以要求违约方承担违约责任。
- 被告开发时间超过履行期限，阶段性产品未达合同约定标准，构成违约，应当承担违约责任。
- 案例二：根据反不正当竞争法，被告构成不正当竞争，应当承担停止侵害、赔偿损失的侵权责任。
- 依法打击不正当竞争行为，维护消费者知情权和选择权，保护知识产权，保护经营者的合法权益。
- 维护公平竞争的市场秩序，营造良好营商环境，为数字经济发展提供法治保障。

### 2025 · 西城 · 一模 · 第20题

- 题目来源：2025 · 西城 · 一模 · 第20题
- 同题组：本题组仅本分问。

#### 材料
全国总工会、人力资源社会保障部、中国企业联合会、全国工商联联合启动2025年度集体协商“集中要约行动”，指导工会与企业开展集体协商、签订集体合同。按照行动部署，各级工会把工资调整幅度、加班工资基数、劳动定额标准、工资支付办法等作为协商的核心议题。

#### 设问
结合材料，综合运用经济和法律的知识，说明上述做法能促进社会公平与经济效率的平衡。

#### 细则
20．（8分）劳动法的首要原则是保护劳动者权益，工会搭建协商平台，劳动者以集体力量与用人单位签订集体合同，可以确保双方协商一致，更加公平、平等自愿。更好地保护劳动者合法权益，促进广大劳动者特别是低薪劳动者群体实现体面劳动，实现社会公平。促进企业依法规范用工，构建和谐劳动关系，激发劳动者积极性，推动生产效率的提高，培育良好商誉，实现社会公平与经济效率的平衡。
【细则】
公平角度：4分
发挥工会的作用/集体的力量1分；可以确保双方协商一致、平等自愿，公平签订劳动合同（或结合订立劳动合同基本原则说明）1分；更好地保护劳动者合法权益（或获得劳动报酬的权利）1分；促进体面劳动（尊重劳动/保护苦脏险累且工资水平不高的劳动者等/分配公平）1分。
效率角度：4分
促进企业依法规范用工（合理用工）1分；激发劳动者积极性/保障收入1分；建立和谐劳动关系1分；推动生产效率的提高/培育良好商誉/企业信誉形象1分。

#### 答案落点
- 劳动法的首要原则是保护劳动者权益，工会搭建协商平台，劳动者以集体力量与用人单位签订集体合同，可以确保双方协商一致，更加公平、平等自愿。
- 更好地保护劳动者合法权益，促进广大劳动者特别是低薪劳动者群体实现体面劳动，实现社会公平。
- 促进企业依法规范用工，构建和谐劳动关系，激发劳动者积极性，推动生产效率的提高，培育良好商誉，实现社会公平与经济效率的平衡。
- 【细则】公平角度：4分发挥工会的作用/集体的力量1分；
- 可以确保双方协商一致、平等自愿，公平签订劳动合同（或结合订立劳动合同基本原则说明）1分；
- 更好地保护劳动者合法权益（或获得劳动报酬的权利）1分；
- 促进体面劳动（尊重劳动/保护苦脏险累且工资水平不高的劳动者等/分配公平）1分。

### 2025 · 西城 · 二模 · 第18题

- 题目来源：2025 · 西城 · 二模 · 第18题
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
- 小刘为限制民事行为能力人，其大额打赏行为，家长事先不知情、事后也不同意追认，交易行为无效。
- 平台的审核措施不完善，未能尽到合理审查的义务，存在过错。
- 小刘父母疏于监管，未能履行好监护职责，行为存在过错。
- 小刘沉迷打赏，并通过欺骗手段规避监管，自身行为也有过错。
- 综合各方过错程度，根据民法典157条规定，法院判定平台和小刘父母都应承担相应责任，符合公平原则。
- 本案判决警示，平台应健全审核机制、担当社会责任，监护人应履行监护义务，教育引导未成年人树立正确消费观。
- 【细则】小刘为限制民事行为能力人（1分），其大额打赏行为，家长事先不知情、事后也不同意追认，交易行为（民事法律行为）无效。

### 2025 · 西城 · 期末 · 第19题

- 题目来源：2025 · 西城 · 期末 · 第19题
- 同题组：本题组仅本分问。

#### 材料
【案情回放】
“小爱同学，今天天气怎么样？”“小爱同学，讲个故事”……随着M公司2017年7月推出的“小爱同学”智能语音设备后，“小爱同学”越来越多地参与到我们的生活中。截至2020年12月，其月活跃用户数达到8670万人，累计唤醒约495亿次。
陈某于2017年8月至2020年6月间，在不同商品类别上抢先大量申请注册相关商标，并向M科技关联企业发函，要求停止使用“小爱同学”商标。同时与深圳市Y公司合作，在运动手表、闹钟等商品上使用“小爱同学”商标，并发布相关宣传文章。M公司因此提起诉讼，指控陈某及深圳市Y公司构成不正当竞争。
【判决结果】
经人民法院审理，“小爱同学”作为有一定影响力的唤醒词、人工智能引擎的名称以及搭载人工智能引擎的智能音箱等商品的名称，受到反不正当竞争法的保护。判决陈某、深圳市Y智能科技有限公司立即停止侵权，陈某赔偿M科技经济损失及合理支出120万元，深圳市Y公司对其中25万元承担连带责任。一审判决后，当事人均未上诉。

#### 设问
“唤醒词”亦受法律保护，请运用法律知识分析法院的判决。

#### 细则
19.（8分）
根据反不正当竞争法，陈某在明知他人已经使用“小爱同学”唤醒词并有一定影响的情况下，抢先注册，并发布引人误解的商业宣传信息，构成混淆及虚假宣传，属于不正当竞争，违背了诚实信用原则。
该案判决合理确定各方利益，规制了滥用权利的行为，保护了科技创新型企业的品牌商誉，有利于促进新业态的发展，为数字经济发展营造良好的法治化营商环境。
解析要点：结合材料描述侵权事实；写出引人误解、混淆或虚假宣传；写出属于不正当竞争或违反反不正当竞争法；写出违背诚实信用原则或商业道德；说明该案判决保护了合法权益或规范了市场行为，有利于新业态、新经济、数字经济发展、创新、维护市场秩序或优化营商环境。

#### 答案落点
- “小爱同学”唤醒词和相关商品名称已经具有一定影响，受反不正当竞争法保护。
- 陈某明知他人已经使用该唤醒词并有一定影响，仍抢先注册相关商标。
- 陈某及深圳市Y公司在相关商品上使用“小爱同学”并发布宣传，容易造成混淆或误认，构成混淆及虚假宣传。
- 上述行为属于不正当竞争，违背诚实信用原则和商业道德。
- 法院判令停止侵权并赔偿损失，合理确定各方利益，规制滥用权利行为。
- 该判决保护科技创新型企业的品牌商誉，有利于促进新业态和数字经济发展，营造良好法治化营商环境。
END_CHUNK_CONTENT
