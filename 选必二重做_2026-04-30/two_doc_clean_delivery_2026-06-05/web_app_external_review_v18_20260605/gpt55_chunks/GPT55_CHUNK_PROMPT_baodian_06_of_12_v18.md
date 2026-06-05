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
Chunk: 6/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: baodian-06
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2025 · 丰台 · 二模 · 第19题第2问

- 题目来源：2025 · 丰台 · 二模 · 第19题第2问
- 框架归位：A5 知识产权与公平竞争｜B6 维权路径
- 同题组：本题组仅本分问。

#### 材料
(13 分)数智时代，司法“把脉开方”解保护与创新之困。
案例
某互联网企业开发了一款AI产品，用户输入“我要看某某热播剧”后，AI 生成的链
接中多数指向盗版资源网站。版权方 H 公司在检测数据时发现其热播剧日均被盗版链
接点击超万次，遂向法院提起诉讼，请求开发这款 AI 产品的互联网企业承担侵权责
任。
调研
法院在深入调研后，发现 AI 产品拥有千亿级参数规模的通用大模型，生成的具体内
容具有高度的不可预测性。该互联网企业已经从语料输入、模型运行到内容输出等各
个环节进行了定期跟踪和核查，尽到了相应的义务。
建议
法院遂开出具有前瞻性、可操作性的司法建议：给 AI 装上“版权雷达”,提前扫描
问题指令；在输出端部署“数字巡警”,实时扫描可疑链接；定期开展“安全体
检”,关注 AI 健康。

#### 设问
(2)一纸司法建议，既为当下划定了红线，防止技术滥用，又为未来创新发展预留了空间。 运用《法律
与生活》知识，谈谈你对这句话的理解。(8 分)

#### 细则
参考答案： 19.（2）（8分）
答案示例：
这句话体现了法律在技术创新与社会秩序之间的平衡作用。司法建议通过明确 AI技术应用的法律边界，既规范了当前的技术行为，防止技术滥用，又为技术的未来创新发展提供了合法的空间。通过划定“红线”，如要求企业安装“版权雷达”和“数字巡警”，对侵权行为进行实时监测，保护了创作者的合法权益，维护了社会公共利益;通过“安全体检”等措施，为技术创新提供了合法路径，体现了对公平原则、诚信原则、守法和公序良俗原则的贯彻。司法建议不仅解决了当前的侵权问题，还为未来创新发展预留空间，展现了法律在规范与保护之间的智慧平衡。
评分标准说明：
标准：
1、这句话体现了法律在技术创新与社会秩序之间的平衡作用。（2分）
2、司法建议通过明确 AI技术应用的法律边界，既规范了当前的技术行为，防止技术滥用，又为技术的未来创新发展提供了合法的空间。（2分）
3、通过划定“红线”，如要求企业安装“版权雷达”和“数字巡警”，对侵权行为进行实时监测，保护了创作者的合法权益，维护了社会公共利益;（2分）通过“安全体检”等措施，为技术创新提供了合法路径，体现了对公平原则、诚信原则、守法和公序良俗原则的贯彻。（2分）司法建议不仅解决了当前的侵权问题，还为未来创新发展预留空间，展现了法律在规范与保护之间的智慧平衡。
说明：
1、这句话体现了法律在技术创新与社会秩序之间（1分，说清平衡主体，言之成理即可得分）的平衡作用。（1分，可变通“相一致、相统一等”）
2、司法建议通过明确AI技术应用的法律边界，既规范了当前的技术行为，防止技术滥用，
通过划定“红线”，如要求企业安装“版权雷达”和“数字巡警”，对侵权行为进行实时监测，（1分，出现一个与“限制”相关即可，可采意）保护了创作者的合法权益，维护了社会公共利益；（2分，出现一个相关即可，可采意）（总，要明确通过“划红线、各种监管”等限制手段规范AI行为，维护著作权人等合法权利，从而促进AI的健康、长远发展）
3、又为技术的未来创新发展提供了合法的空间。通过“安全体检”等措施，为技术创新提供了合法路径，（1分，出现与“促进创新”相关即可，可采意）体现了对公平原则、诚信原则、守法和公序良俗原则的贯彻。（2分，出现1个即可。如果有其他关于促进创新的意义例如：促进企业创新积极性等也可变通最多1分，不能重复得分。）（总，要明确通过“提供、预留合法空间、安全体检”等保护手段促进创新，体现民法原则。）

#### 答案落点
- 这句话体现法律在技术创新与社会秩序之间的平衡作用。
- 司法建议通过明确 AI 技术应用的法律边界，规范当前技术行为，防止技术滥用。
- “版权雷达”“数字巡警”等措施针对侵权风险划定红线，有利于保护创作者合法权益、维护社会公共利益。
- “安全体检”等措施不是否定创新，而是为技术创新提供合法路径和安全边界。
- 该司法建议体现公平原则、诚信原则、守法和公序良俗原则等民法基本原则。
- 作答要同时写出“限制滥用”和“保护创新”两面，落到法律规范与创新保护的统一。

### 2025 · 房山 · 一模 · 第19题

- 题目来源：2025 · 房山 · 一模 · 第19题
- 框架归位：A5 知识产权与公平竞争｜B5 意义价值
- 同题组：本题组仅本分问。

#### 材料
阅读材料，回答问题。
“真创新”受到“真保护”，我国知识产权侵权诉讼判赔数额创历史新高。
案情回放 A集团近40名高级管理人员及技术人员，先后离职赴B集团工作，其中30人于当年离职
后即入职。两年后，A集团发现B集团以上述部分离职人员作为发明人或共同发明人，利用在原单位接触、
掌握的有关新能源汽车底盘应用技术以及其中的12套底盘零部件图纸及数模承载的技术信息（下称技术秘
密）申请了12件实用新型专利，且B集团在没有任何技术积累或合法技术来源的情况下，在短期内即推出
某系列型号电动汽车，涉嫌侵害A集团技术秘密。A集团决定向法院提起诉讼。
判决结果 法院经审理认为，B 集团以不正当手段侵害 A 集团技术秘密，适用 2 倍惩罚性赔偿，判决
赔偿共计6.4亿余元。

#### 设问
结合材料，谈谈“真创新”受到“真保护”的法治价值。

#### 细则
19.（8分）
①B集团通过挖走A集团核心技术人员并窃取技术秘密属于典型的不正当竞争行为，法院的判决打击
了违法行为，促使企业依法诚信经营，维护了公平的竞争环境，促进市场经济健康发展。
②法院对B集团适用的高额赔偿提高了侵权成本，强化知识产权保护，使企业更愿意投入研发，激发
创新活力和科技进步。
③法院公正司法，维护了社会公平正义，弘扬了社会主义核心价值观。
细则：
1.不正当竞争
B集团通过挖走A集团核心技术人员并窃取技术秘密（材料1分）属于典型的不正当竞争行为（定性
分析1分），法院的判决打击了违法行为，促使企业依法诚信经营，维护了公平的竞争环境，促进市
场经济健康发展。（法治价值2分）
2.惩罚性赔偿
法院对B集团适用的高额赔偿提高了侵权成本（材料1分），强化知识产权保护，使企业更愿意投入
研发，激发创新活力和科技进步。（创新2分）
3.道德意义
法院公正司法，维护了社会公平正义，弘扬了社会主义核心价值观。（1 分，给出社会主义核心价值
观的具体词语也可以）
4.劳动者
劳动者有保守秘密的义务，在就业过程中要做到权利和义务相统一，严守职业道德。（2分）
5.民法的基本原则（1分）
6.必修三法治
公正司法、全民守法、法治社会、法治国家等角度。（2分）
从以上角度答题，总分不超过8分，单纯写知识，没有材料，比如每一点的开头都是有利于，总分不
超过6分。

#### 答案落点
- B集团挖走A集团核心技术人员并窃取技术秘密，属于典型的不正当竞争行为。
- 法院判决打击违法行为，促使企业依法诚信经营，维护公平竞争环境，促进市场经济健康发展。
- 法院适用高额赔偿或惩罚性赔偿，提高侵权成本，强化知识产权保护。
- 高额赔偿有利于让企业更愿意投入研发，激发创新活力和科技进步。
- 法院公正司法，维护社会公平正义，弘扬社会主义核心价值观。
- 劳动者有保守秘密的义务，在就业过程中应坚持权利和义务相统一，严守职业道德。
- 还可从民法基本原则、公正司法、全民守法、法治社会等角度补充，但不能只罗列知识，必须结合材料。

### 2025 · 昌平 · 二模 · 第20题第1问

- 题目来源：2025 · 昌平 · 二模 · 第20题第1问
- 框架归位：A5 知识产权与公平竞争｜B2 判责/理由
- 同题组：2025 · 昌平 · 二模 · 第20题第1问；2025 · 昌平 · 二模 · 第20题第2问

#### 材料
案件情况 | 处理结果 | 裁判理由
李某是一名AI绘图软件爱好者，他使用人工智能软件制作了一张图片，并加上“AI 绘画”等标签，发布在自己的社交平台上。网友刘某看到图片后，感觉非常契合自己的文章，便直接拿来作为配图使用，还抹去了平台署名水印。李某认为刘某的行为侵犯了自己的著作权。遂将刘某诉至北京互联网法院。 | 法院支持李某诉讼请求。 | （1）
小王向银行申请开通信用卡，且宣称已阅览申请材料，明晰信用卡相关信息，愿意遵循领用合约及申请表中所列的所有条款。后来小王使用该卡透支消费，却未依照合同约定履行还款义务。银行屡次向小王催告，然而小王迄今仍未还款。为维护自身的合法权益，银行将其诉至法院，恳请依法判决小王偿还信用卡欠款2万元及利息。 | 法院判决小王偿还信用卡欠款本金2万元，并按合同约定支付利息。 | （2）

#### 设问
（1）阅读材料，运用《法律与生活》知识，完成裁判理由。（6分）

#### 细则
20.阅读材料，运用《法律与生活》知识，完成裁判理由。（6分）
案件一：
案件情况：李某是一名AI绘图软件爱好者，他使用人工智能软件制作了一张图片，并加上“AI绘画”等标签，发布在自己的社交平台上。网友刘某看到图片后，感觉非常契合自己的文章，便直接拿来作为配图使用，还抹去了平台署名水印。李某认为刘某的行为侵犯了自己的著作权，遂将刘某诉至北京互联网法院。
处理结果：法院支持李某诉讼请求。
裁判理由：关于AI作品权利归属问题，著作权法规定著作权人限于自然人、法人或非法人组织，AI不能成为著作权主体。李某使用人工智能软件制作的图片，具备“智力成果”和“独创性”要件，受到著作权法保护，享有著作权。刘某未经许可将其作为配图使用且抹去水印，侵害了李某的信息网络传播权和署名权，属于侵权行为，应承担侵权责任。
评分细则：①著作权法规定著作权人限于自然人、法人或非法人组织，李某使用人工智能软件制作的图片，具备“智力成果”和“独创性”要件，受到著作权法保护。（法律保护著作权角度，1分；可替代为著作权法规定著作权人对其作品享有广泛的权利）②刘某未经许可将其作为配图使用且抹去水印，侵害了李某的信息网络传播权和署名权（二选一，1分）。③能够结合材料说出李某虽然使用了AI，但具备“智力成果”和“独创性”要件，受到著作权法保护，享有著作权；或从鼓励创新角度阐述意义（1分，言之成理即可得分，但不重复给分）。
案件二：
案件情况：小王向银行申请开通信用卡，且宣称已阅览申请材料，明晰信用卡相关信息，愿意遵循领用合约及申请表中所列的所有条款。后来小王使用该卡透支消费，却未依照合同约定履行还款义务。银行屡次向小王催告，然而小王迄今仍未还款。为维护自身合法权益，银行将其诉至法院，恳请依法判决小王偿还信用卡欠款2万元及利息。
处理结果：法院判决小王偿还信用卡欠款本金2万元，并按合同约定支付利息。
裁判理由：双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合法有效，对双方均具有约束力。小王使用信用卡透支且经催缴仍不还款的行为构成违约，违背了诚信原则和全面履行原则，应承担违约责任。
评分细则：①双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合同有效，对双方均具有约束力。（二选一，1分；可替代为合同体现权利与义务相统一、公平原则、协商一致等）②小王使用信用卡透支且经催缴仍不还款的行为构成违约。（1分；可替代为应承担违约责任）③违背了诚信原则和全面履行原则，应承担违约责任。（二选一，1分；可替代为体现诚信的社会主义核心价值观、传统美德，但必须出现诚信；或社会信用机制等）其他答案言之成理即可得分，但不重复给分。

#### 答案落点
- 案件一：著作权法规定著作权人限于自然人、法人或非法人组织，AI不能成为著作权主体。
- 李某使用人工智能软件制作的图片，具备智力成果和独创性要件，受到著作权法保护，李某享有著作权。
- 刘某未经许可将图片作为配图使用并抹去水印，侵害李某的信息网络传播权或署名权，属于侵权行为，应承担侵权责任。
- 案件一还可从鼓励创新、保护创作成果角度说明法院支持李某的意义。
- 案件二：小王申请信用卡并确认领用合约及申请表条款，相关手续系双方真实意思表示，内容不违反法律规定，合同有效，对双方具有约束力。
- 小王使用信用卡透支且经银行催缴仍不还款，构成违约，应承担违约责任。
- 小王的行为违背诚信原则和全面履行原则；作答必须出现诚信，才能稳定拿到该层分。

### 2025 · 朝阳 · 期末 · 第20题

- 题目来源：2025 · 朝阳 · 期末 · 第20题
- 框架归位：A5 知识产权与公平竞争｜B1 补表/补链
- 同题组：本题组仅本分问。

#### 材料
人民法院审理案件，必须坚持以事实为根据、以法律为准绳，做到公正司法。了解案件，分析事实，印证法理。
案件事实 | 拟写裁判要点
示例：案件一 甲公司在2016年与乙公司终止合作后，继续在甲公司运营的相关地图软件、应用和第三方服务中使用乙公司数据。乙公司以甲公司侵犯署名权、修改权、复制权、信息网络传播权等理由向人民法院提起诉讼。 | 裁判理由：根据著作权法，甲公司在应用软件中使用被诉侵权电子地图，侵害了乙公司对涉案导航电子地图的署名权、修改权、复制权、信息网络传播权。裁判结果：被告停止侵害、赔礼道歉、消除影响并赔偿损失。
案件二 丙公司依托电子地图收集的电子地图数据、用户出行数据和实时交通信息等原始数据，通过特定算法并经分析处理形成数据产品“拥堵延时指数”。被告丁公司采用变换IP地址和伪造浏览器标识等不正当手段抓取“拥堵延时指数”数据，并在其经营的某金融终端付费软件上以商业化为目的使用了上述数据。丙公司就此诉至人民法院。 | 裁判理由：① 裁判结果：②
案件三 甲向乙旅游公司购买门票，并于当日参加“摇摆桥”项目。在该项目进行过程中，乙旅游公司工作人员过度摇晃桥面，甲从摆桥上摔落、受伤。经医院诊断，甲左肱骨髁上髁间粉碎性骨折，共住院13天。经鉴定，甲的损伤及目前后遗症评定为九级伤残。甲向人民法院起诉，请求判令乙旅游公司赔偿医疗费等经济损失。 | 裁判理由：③ 裁判结果：④

#### 设问
参考示例，完成下表。

#### 细则
20.（10分）参考示例，完成下表。
案件二：
裁判理由：①根据反不正当竞争法；②被告行为损害了原告“拥堵延时指数”数据的合法权益和消费者利益，构成不正当竞争；③破坏市场竞争秩序，违背商业道德和诚实信用原则。
裁判结果：①被告停止侵权、消除影响；停止侵害可替换为停止数据使用等相关表述。②被告赔偿原告经济损失及维权合理开支。简写“赔损”不给分，写成“补偿”不给分。
案件三：
裁判理由：①根据民法典或消费者权益保护法；②旅游公司工作人员过度摇晃桥面与甲摔落、受伤之间有因果关系，写出因果关系事实可得分；③旅游公司有过错；④旅游公司应承担侵权责任（主要责任），或写旅游公司侵犯了甲的身体权、健康权；⑤旅游公司与甲构成合同关系；⑥旅游公司未对参与者提供充分有效的安全保障，应承担违约责任。
裁判结果：支持甲的合理诉讼请求，乙旅游公司对甲承担相应责任，赔偿医疗费等合理经济损失。

#### 答案落点
- 案件二裁判理由：依据反不正当竞争法，丁公司的抓取和商业化使用行为损害数据合法权益和消费者利益，构成不正当竞争。
- 案件二还要写：该行为破坏市场竞争秩序，违背商业道德和诚实信用原则。
- 案件二裁判结果：被告停止侵权、消除影响，赔偿原告经济损失及维权合理开支。
- 案件三裁判理由：依据民法典或消费者权益保护法，旅游公司工作人员过度摇晃桥面与甲摔落受伤之间有因果关系。
- 案件三还要写：旅游公司有过错，应承担主要侵权责任；也可写侵犯甲的身体权、健康权。
- 案件三也可从合同关系作答：旅游公司未对参与者提供充分有效的安全保障，应承担违约责任。
- 案件三裁判结果：支持甲的合理诉讼请求，乙旅游公司赔偿医疗费等合理经济损失。
END_CHUNK_CONTENT
