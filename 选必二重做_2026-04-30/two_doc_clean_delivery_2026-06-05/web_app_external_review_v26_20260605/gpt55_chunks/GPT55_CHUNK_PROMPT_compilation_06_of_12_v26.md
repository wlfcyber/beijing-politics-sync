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
Document: 试题和细则汇编
Chunk: 6/12

Review this chunk for:
1. Any student-facing noise or backend trace.
2. Missing required fields in entries contained in this chunk.
3. Obvious answer/rubric/material incoherence visible from the text.
4. Any wording or structure issue that should block final delivery.
5. For AB handbook chunks, check whether 框架归位 and A-axis placement are visibly incoherent.

# Required Output
Return Chinese, compact:
- chunk_id: compilation-06
- verdict: PASS / CONDITIONAL_PASS / FAIL for this chunk only
- BLOCKING defects: 无 if none
- NONBLOCKING issues: 无 if none
- Required local verification: 无 if none

# Chunk Content
BEGIN_CHUNK_CONTENT
### 2025 · 朝阳 · 二模 · 第20题第2问

- 题目来源：2025 · 朝阳 · 二模 · 第20题第2问
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

### 2025 · 朝阳 · 期末 · 第20题

- 题目来源：2025 · 朝阳 · 期末 · 第20题
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

### 2025 · 海淀 · 一模 · 第18题

- 题目来源：2025 · 海淀 · 一模 · 第18题
- 同题组：本题组仅本分问。

#### 材料
随着居民消费水平的提高，主题乐园越来越受到游客的青睐。某主题乐园推出了年卡服务，游客只需
支付一定费用办理年卡，即可享受主题乐园酒店的折扣优惠，并通过优先通道快速入园游玩项目。游客在
办理时需与该主题乐园签订有关年卡的《条款及细则》格式合同，其中明确规定：“主题乐园年卡不可转
让，年卡及其相应福利仅限持卡人本人使用。若游客违反上述约定，主题乐园有权解除合同。”
小黄在购买年卡后，发现主题乐园酒店对登记入住人员与实际入住人员是否一致的审查存在漏洞，于
是他利用年卡以七折优惠价格订购酒店房间并在网络交易平台公开售卖给他人，通过传递房卡的方式交由
其他游客持卡实际入住，从中多次赚取差价。主题乐园发现后，短信通知小黄，因其违反双方合同约定，
即刻撤销其年卡全部权益。
小黄对此表示不满，向法院提起诉讼，认为格式条款无效，要求解封年卡，恢复相关权益，并要求主
题乐园赔偿其禁卡期间的损失。最终，法院判决驳回小黄的诉讼请求。

#### 设问
运用《法律与生活》知识，谈谈对本案判决的认识。

#### 细则
18．（7分）
小黄与主题乐园签订的格式合同意思表示真实，条款符合公平原则，合同有效。小黄利用审查漏洞不当获利的行为违反合同约定，违背诚信原则。主题乐园可以根据合同约定，采取撤销年卡的方式解除合同。法院判决保护了主题乐园合法权益，有利于营造公平公正市场环境。
【细则】
合同有效（2分）
2分：条款符合公平原则/权利义务相统一，合同有效
1分：格式合同意思表示真实，合同有效
0分：意思表示真实/合同有效

案情分析（3分）
小黄的行为违反合同约定/违约，（1分）违背诚信原则（1分）
主题乐园可以根据合同约定，采取撤销年卡的方式解除合同。（1分）

判决意义（2分）
法院判决保护了主题乐园合法权益
有利于平衡经营者和消费者的关系
有利于营造公平公正市场环境/维护良好的市场秩序
有利于维护社会公平正义
有利于践行诚信的社会主义核心价值观/诚信的道德风尚
（以上任意出现2条，给2分）

#### 答案落点
- 小黄与主题乐园签订的格式合同意思表示真实。
- 年卡条款符合公平原则，体现权利义务相统一，合同有效。
- 小黄利用审查漏洞，以年卡优惠订购酒店房间并转售牟利，违反合同约定，构成违约。
- 小黄的行为违背诚信原则。
- 主题乐园可以根据合同约定撤销年卡权益或解除合同。
- 法院判决保护了主题乐园合法权益，有利于平衡经营者和消费者之间的关系。
- 该判决有利于营造公平公正的市场环境、维护良好市场秩序，也有利于维护社会公平正义和诚信价值。

### 2025 · 海淀 · 二模 · 第18题

- 题目来源：2025 · 海淀 · 二模 · 第18题
- 同题组：本题组仅本分问。

#### 材料
小海旁听了学校的“模拟法庭”活动，以下是旁听笔记。
【法条参考】
《中华人民共和国商标法》第三十二条 申请商标注册不得损害他人现有的在先权利，也不得以不正当手段抢先注册他人已经使用并有一定影响的商标。
【庭审记录】
1. 开庭准备
书记员查明当事人和其他诉讼参与人是否到庭，宣布法庭纪律。
审判长核对当事人基本情况，告知当事人有关诉讼权利和义务，询问当事人是否提出 ① 。
2. 法庭调查
原告诉称其于2025年2月成功注册“吃滴美”商标，依法享有商标专用权。被告没有注册“吃滴美”商标，且在经营过程中使用该商标进行糕点生产，并在包装上使用该商标字样，属于未经许可的使用行为。原告请求法院判令被告停止使用“吃滴美”商标，并赔偿损失。
被告辩称其多年来一直在使用“吃滴美”商标进行糕点生产，在当地具有知名度，且被告“吃滴美”企业创办于清乾隆四年（1739年），以制作酥糖、糕点著称，系老字号企业，原告行为是恶意抢注，不应保护。
原告出示商标注册证明文件用以证明原告享有“吃滴美”商标专用权，出示 ② 用以证明 ③ 。
被告出示 ④ 用以证明 ⑤ 。
……
3. 法庭辩论
原被告就本案争议焦点展开辩论。
4. 合议庭评议
审判长宣布休庭，在休庭后依法评议。
5. 宣告判决
本院查明，……被告“吃滴美”企业创办于清乾隆四年（1739年），以制作酥糖、糕点著称，系老字号企业，其产品多次荣获国家轻工产品奖项。原告作为当地企业，应知道这一事实……
本院认为，根据《中华人民共和国商标法》第三十二条的规定，原告 ⑥ 的做法，违背了 ⑦ 这一民法基本原则，不利于 ⑧ ，本院予以谴责。
综上所述，被告在商品包装上使用“吃滴美”标识，系正常经营行为，原告诉讼请求不应获得支持。依照《中华人民共和国商标法》第三十二条、第五十六条、第五十七条第一项、第二项和《中华人民共和国民事诉讼法》第十三条、第一百四十二条的规定，判决如下：
驳回原告的诉讼请求。
案件受理费1000元，由原告承担。
如不服本判决，可以在判决书送达之日起十五日内，向本院递交上诉状。
【旁听收获】
⑨

#### 设问
运用法治知识，将笔记中划线处补充完整。

#### 细则
18题
1. 回避，1分。
2. 被告在包装上使用“吃滴美”商标，1分。
3. 未经许可使用商标权/侵犯商标权，需与②对应，1分。
4. 能证明被告老字号、知名度、无侵权或被告拥有在先权利的材料，或合理的书证、物证、证言类例子，1分。
5. 老字号/知名度/无侵权/被告拥有在先权利，需与④对应，1分。
6. 抢注/抢先注册/恶意注册/损害在先权利/符合商标法第三十二条规定，1分。
7. 诚信/公平/守法和公序良俗/公序良俗，1分。
8. 市场秩序/营商环境/社会主义核心价值观/中华传统美德/公平竞争，1分。
9. 旁听收获按层次给分：第一层，获得新知，如学习了相关法律知识、了解“行使权利有边界”、了解证据对诉讼的价值或了解法庭审理内容和流程；第二层，感受公正，如程序公正、结果公正、以事实为依据以法律为准绳、体现公正司法；第三层，体会价值，如维护老字号企业合法权益、传承中华优秀传统美德、弘扬社会主义核心价值观、维护良好市场秩序。三个层次4分，两个层次3分，一个层次2分。

#### 答案落点
- ①填写“回避”。
- ②③应对应原告举证：例如被告在包装上使用“吃滴美”商标，用以证明未经许可使用商标或侵犯商标权。
- ④⑤应对应被告举证：例如老字号、知名度、在先使用或无侵权的材料，用以证明被告拥有在先权利或不构成侵权。
- ⑥填写抢注、抢先注册、恶意注册或损害在先权利。
- ⑦填写诚信、公平、守法和公序良俗等民法基本原则。
- ⑧可填写市场秩序、营商环境、社会主义核心价值观、中华传统美德或公平竞争。
- ⑨旁听收获从获得法律新知、感受司法公正、体会老字号保护和市场秩序价值等层次作答。

### 2025 · 海淀 · 期中 · 第21题第1问

- 题目来源：2025 · 海淀 · 期中 · 第21题第1问
- 同题组：本题组仅本分问。

#### 材料
21. 75年，大国自信而坚定的脚步。
1950 年 5 月 1 日，《中华人民共和国婚姻法》开始施行。这是新中国成立后颁布的第一部具有基本法
律性质的法律，彻底废除了封建主义家庭制度，确立了以婚姻自由、一夫一妻、保护妇女儿童权益为原则
的社会主义婚姻家庭制度。2021年1月1日，《中华人民共和国民法典》正式实施。民法典专门设置了“婚
姻家庭编”，包括婚姻法在内的多部法律同时废止。
中华人民共和国婚姻法（1950） 中华人民共和国民法典
第二十四条 离婚时，原为夫妻共同生活所 第一千零八十九条 离婚时，
负担的债务，以共同生活时所得财产偿还；如无 夫妻共同债务应当共同偿还。共同
共同生活时所得财产或共同生活时所得财产不足 财产不足清偿或者财产归各自所有
清偿时，由男方清偿。男女一方单独所负的债 的，由双方协议清偿；协议不成
务，由本人偿还。 的，由人民法院判决。
思政课上，大家围绕老师出示的两则法条展开了讨论。小海认为，1950 年婚姻法中“由男方清偿”的
规定并不合理，民法典的规定才符合良法的要求。

#### 设问
（1）运用法治知识，对小海的观点进行评析。

#### 细则
21（1）（6分）
参考答案：小海的观点片面。新中国成立初期尚未完全建立夫妻共同财产制度，在家庭生活中男方经济地位更强，根据权利与义务相对应原则，由男方清偿具有合理性，有利于保护当事各方的利益。随着时代的发展，夫妻双方的经济状况发生变化，具备了“共同偿还”“协议清偿”的条件。良法应当符合国情和实际，符合社会发展的需求。婚姻法与民法典的规定都符合良法的要求。
评分细则：
观点（1分）：可写片面、错误、正确、认同或同意等，但须能体现对小海观点的评价。
分析（5分）：
角度一：时代背景。
知识：从中国实际出发，或科学立法符合国情和实际。（2分）
变通表述：科学立法、由社会实际情况决定、立足国情、符合实际。（可给1分）
材料分析：分析1950年和2021年具体社会情况。（1分）
材料分析：对比1950年男女经济地位。（1分）
角度二：男女个体。
知识：合理设定权利与义务，或法律面前人人平等，或公平，或尊重保障人权。（1分）

#### 答案落点
- 先表态：小海的观点片面。
- 1950年背景：新中国成立初期尚未完全建立夫妻共同财产制度，家庭生活中男方经济地位更强。
- 权利义务分析：根据权利与义务相对应原则，由男方清偿在当时具有合理性，有利于保护当事各方利益。
- 时代发展分析：随着时代发展，夫妻双方经济状况发生变化，具备了“共同偿还”“协议清偿”的条件。
- 良法标准：良法应当符合国情和实际，符合社会发展的需求。
- 综合结论：婚姻法与民法典的规定都符合良法要求，不能只肯定民法典而否定1950年婚姻法。
- 评分提醒：分析要覆盖时代背景、男女个体、科学立法或从中国实际出发，不能只罗列结论。
END_CHUNK_CONTENT
