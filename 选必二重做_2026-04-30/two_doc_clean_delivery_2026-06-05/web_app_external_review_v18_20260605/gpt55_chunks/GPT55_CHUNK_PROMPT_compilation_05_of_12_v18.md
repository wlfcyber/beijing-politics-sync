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
Chunk: 5/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-05
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2025 · 房山 · 一模 · 第19题

- 题目来源：2025 · 房山 · 一模 · 第19题
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

### 2025 · 昌平 · 二模 · 第20题第2问

- 题目来源：2025 · 昌平 · 二模 · 第20题第2问
- 同题组：2025 · 昌平 · 二模 · 第20题第1问；2025 · 昌平 · 二模 · 第20题第2问

#### 材料
案件情况 | 处理结果 | 裁判理由
李某是一名AI绘图软件爱好者，他使用人工智能软件制作了一张图片，并加上“AI 绘画”等标签，发布在自己的社交平台上。网友刘某看到图片后，感觉非常契合自己的文章，便直接拿来作为配图使用，还抹去了平台署名水印。李某认为刘某的行为侵犯了自己的著作权。遂将刘某诉至北京互联网法院。 | 法院支持李某诉讼请求。 | （1）
小王向银行申请开通信用卡，且宣称已阅览申请材料，明晰信用卡相关信息，愿意遵循领用合约及申请表中所列的所有条款。后来小王使用该卡透支消费，却未依照合同约定履行还款义务。银行屡次向小王催告，然而小王迄今仍未还款。为维护自身的合法权益，银行将其诉至法院，恳请依法判决小王偿还信用卡欠款2万元及利息。 | 法院判决小王偿还信用卡欠款本金2万元，并按合同约定支付利息。 | （2）

#### 设问
（2）阅读材料，运用《法律与生活》知识，完成裁判理由。（6分）

#### 细则
双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合法有效，对双方均具有约束力。小王使用信用卡透支且经催缴仍不还款的行为构成违约，违背了诚信原则和全面履行原则，应承担违约责任。
评分细则：
●双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合同有效，对双方均具有约束力。（二选一，1分。替代：合同体现了权利与义务相统一/公平原则/协商一致，等）
●小王使用信用卡透支且经催缴仍不还款的行为构成违约。（1分，替代：应承担违约责任）
●违背了诚信原则和全面履行原则，应承担违约责任。（二选一，1分。替代：体现了诚信的社会主义核心价值观/传统美德，但必须出诚信；社会信用机制等。）
（其他答案，言之成理即可得分，但不重复给分。）

#### 答案落点
- 双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合法有效，对双方均具有约束力。小王使用信用卡透支且经催缴仍不还款的行为构成违约，违背了诚信原则和全面履行原则，应承担违约责任。
评分细则：
●双方签订的相关手续系双方真实意思表示，内容不违反法律规定，合同有效，对双方均具有约束力。（二选一，1分。替代：合同体现了权利与义务相统一/公平原则/协商一致，等）
●小王使用信用卡透支且经催缴仍不还款的行为构成违约。（1分，替代：应承担违约责任）
●违背了诚信原则和全面履行原则，应承担违约责任。（二选一，1分。替代：体现了诚信的社会主义核心价值观/传统美德，但必须出诚信；社会信用机制等。）
（其他答案，言之成理即可得分，但不重复给分。）

### 2025 · 朝阳 · 一模 · 第19题

- 题目来源：2025 · 朝阳 · 一模 · 第19题
- 同题组：本题组仅本分问。

#### 材料
司法护航，营造在线文旅消费法治环境。
某市互联网法院召开涉在线文化旅游消费案件审理情况新闻发布会，介绍涉在线文化旅游消费案件的
审理情况，发布典型案例。以下为其中一例：
王某通过 A 机票代销平台公司（以下简称“A 公司”）购买青岛至宁波的机票，页面显示总价 350 元
（含基建燃油费70元），优惠40元后实付310元。事后，王某在航空公司官网查验发现，机票实际总价为
300 元。经查，A 公司在向王某销售机票的过程中通过技术手段擅自搭售了 10 元的外卖红包，王某在购买
界面并不能清楚地知悉费用的支出细节，也无法拒绝支付10元的额外费用。
王某遂向该市互联网法院提起诉讼，要求 A 公司退还其支付的票款 310 元，并予以三倍赔偿。该法院
的判决支持了王某的诉讼请求。
《中华人民共和国消费者权益保护法》（节选）
第五十五条 经营者提供商品或者服务有欺诈行为的，应当按照消费者的要求增加赔偿其
受到的损失，增加赔偿的金额为消费者购买商品的价款或者接受服务的费用的三倍；增加赔偿
的金额不足五百元的，为五百元。法律另有规定的，依照其规定。

#### 设问
结合材料，运用《法律与生活》知识，说明人民法院支持王某的诉讼请求的理由。

#### 细则
19.（8分）
结合材料，运用《法律与生活》知识，说明人民法院支持王某的诉讼请求的理由。
阅卷前制定的参考答案：
①原告支付机票款，已经出票，合同成立。（1分）
②合同成立不等于生效。（1分）
③某机票代销平台主观上具备欺诈故意，客观上实施了欺诈行为，以立减优惠的形式诱骗消费者购买了高价机票，使王某在违背意思表示的情况下订立合同，因此，根据民法典规定，王某请求人民法院撤销合同。（2分）
④根据消费者权益保护法，因A公司提供服务有欺诈行为，因此，法院应当支持王某要求三倍赔偿的诉讼请求。（2分）
⑤判决维护了消费者的合法权益，规范了在线文旅行业平台经济企业的行为，持续优化网络消费环境，引导电商主体规范经营，明确权利行使边界和责任范围，促进数字经济持续健康发展。（2分）
评分细则、答案变通说明：
①原告通过A公司平台购买机票，双方有要约、承诺或合同成立。（1分）
②A公司擅自搭售10元外卖红包，王某在购买界面不能清楚地知悉费用支出细节，也无法拒绝支付10元额外费用。（1分）材料3个条件必须写全才得分。
A公司的合同欺诈导致王某在违背真实意思表示的情况下订立合同。（1分）
合同无效或可撤销。（1分）
③根据消费者权益保护法。（1分）必须有“消费者”法律字样，只写“保护法”等不给分。
A公司提供服务时有欺诈行为，或侵犯了消费者知情权、公平交易权、自主选择权。（1分）
法院应支持退还票款310元和三倍赔偿的诉讼请求。
④支持王某的诉讼请求，有助于维护消费者合法权益，引导电商企业规范经营，有利于规范企业诚信经营，规范网络消费市场秩序，持续优化网络消费环境，促进数字经济持续健康发展，也可写维护司法权威、维护社会公平正义、弘扬社会主义核心价值观。（2分）

#### 答案落点
- 合同基础：王某通过A公司平台购买机票，双方有要约、承诺，合同成立；但合同成立不等于当然有效。
- 欺诈事实：A公司擅自搭售10元外卖红包，王某不能清楚知悉费用支出细节，也无法拒绝支付10元额外费用。
- 民法典路径：A公司的欺诈导致王某在违背真实意思表示的情况下订立合同，合同可撤销或相应内容不应被支持。
- 消费者法路径：根据消费者权益保护法，A公司提供服务时有欺诈行为，或侵犯消费者知情权、公平交易权、自主选择权。
- 诉求结论：法院应支持退还票款310元和三倍赔偿的诉讼请求。
- 价值意义：维护消费者合法权益，引导电商企业规范经营，规范网络消费市场秩序。
- 还可写持续优化网络消费环境、促进数字经济健康发展、维护司法权威和社会公平正义。

### 2025 · 朝阳 · 二模 · 第20题第1问

- 题目来源：2025 · 朝阳 · 二模 · 第20题第1问
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
END_CHUNK_CONTENT
