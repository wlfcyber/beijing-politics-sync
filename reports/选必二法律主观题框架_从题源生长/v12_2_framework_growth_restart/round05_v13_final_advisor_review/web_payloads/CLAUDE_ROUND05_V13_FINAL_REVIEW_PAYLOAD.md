# Round05 External Final Review Payload: Xuanbier v13.0 Double-Axis Legal Baodian

Date: 2026-05-23

You are Claude Opus 4.7 Adaptive, final teaching reviewer focused on student learnability, transfer language, and over-abstract-node risk.

You are reviewing a Beijing Gaokao Politics 选择性必修二《法律与生活》 legal-question framework and baodian. This is NOT a request to invent a framework from scratch now. Earlier real GPT Pro and Claude Opus 4.7 Adaptive web outputs both said v12.2 must be upgraded to a double-axis framework. Codex implemented that as v13.0.

Important gate rules:
- Do not praise generally. Find structural defects if any.
- Do not treat v12.2 E1-E6 as the main legal framework; in v13.0 they are B-axis question-action labels.
- Check whether A-axis legal relationship/content labels are genuinely correct for all 42 rows.
- Open-container/reference-only rows must stay outside the core. Do not ask to promote them unless you identify a concrete evidence need.
- Give a final verdict exactly one of:
  - ACCEPT_FINAL_WITH_CAVEAT
  - ACCEPT_AFTER_MINOR_PATCHES
  - REVISE_MAJOR
  - FAIL_FRAMEWORK

## v13.0 Structure Under Review

A-axis is the legal relationship/content axis:
A1 民事法律关系总论 (foundation layer, not counted as independent trunk); A2 人身权与人格权; A3 物权与相邻关系; A4 合同; A5 知识产权与市场竞争接口; A6 侵权责任; A7 婚姻家庭与继承; A8 劳动关系; A9 消费者权益与经营秩序; A10 多元纠纷解决与诉讼程序.

B-axis preserves v12.2 E1-E6 as question-action axis:
B1 表格/裁判要点/补链; B2 判决/裁判/责任理由; B3 诉求/请求能否支持; B4 评析/认识/观点; B5 意义/价值/保护/推动; B6 调解/维权/纠纷解决路径.

Operating formula:
First locate A = legal relationship/content, then locate B = question action/proposition path, then answer by fact trigger -> rule/element -> responsibility/effect/procedure conclusion -> conditional meaning/value output.

## A-axis Support Counts

```csv
a_axis,status,primary_row_count,governance_note
A1_民事法律关系总论,基础层，不作为独立主干计数,0,基础层，不要求 primary 支持数
A2_人身权与人格权,启用主干,4,enabled_supported
A3_物权与相邻关系,启用主干,3,enabled_supported
A4_合同,启用主干,5,enabled_supported
A5_知识产权与市场竞争接口,启用主干,8,enabled_supported
A6_侵权责任,启用主干,5,enabled_supported
A7_婚姻家庭与继承,启用主干,3,enabled_supported
A8_劳动关系,启用主干,6,enabled_supported
A9_消费者权益与经营秩序,启用主干,5,enabled_supported
A10_多元纠纷解决与诉讼程序,启用主干,3,enabled_supported
```

## B-axis Support Counts

```csv
b_axis,old_v12_2_entry,row_count
B1_表格/裁判要点/补链,E1,9
B2_判决/裁判/责任理由,E2,8
B3_诉求/请求能否支持,E3,3
B4_评析/认识/观点,E4,7
B5_意义/价值/保护/推动,E5,11
B6_调解/维权/纠纷解决路径,E6,4
```

## A x B Nonzero Cross Counts

```csv
a_axis,b_axis,row_count
A2_人身权与人格权,B1_表格/裁判要点/补链,1
A2_人身权与人格权,B3_诉求/请求能否支持,1
A2_人身权与人格权,B4_评析/认识/观点,2
A3_物权与相邻关系,B2_判决/裁判/责任理由,1
A3_物权与相邻关系,B5_意义/价值/保护/推动,1
A3_物权与相邻关系,B6_调解/维权/纠纷解决路径,1
A4_合同,B1_表格/裁判要点/补链,1
A4_合同,B2_判决/裁判/责任理由,1
A4_合同,B4_评析/认识/观点,1
A4_合同,B5_意义/价值/保护/推动,1
A4_合同,B6_调解/维权/纠纷解决路径,1
A5_知识产权与市场竞争接口,B1_表格/裁判要点/补链,3
A5_知识产权与市场竞争接口,B2_判决/裁判/责任理由,1
A5_知识产权与市场竞争接口,B5_意义/价值/保护/推动,4
A6_侵权责任,B1_表格/裁判要点/补链,1
A6_侵权责任,B2_判决/裁判/责任理由,1
A6_侵权责任,B4_评析/认识/观点,1
A6_侵权责任,B5_意义/价值/保护/推动,2
A7_婚姻家庭与继承,B4_评析/认识/观点,2
A7_婚姻家庭与继承,B5_意义/价值/保护/推动,1
A8_劳动关系,B1_表格/裁判要点/补链,1
A8_劳动关系,B2_判决/裁判/责任理由,3
A8_劳动关系,B3_诉求/请求能否支持,1
A8_劳动关系,B5_意义/价值/保护/推动,1
A9_消费者权益与经营秩序,B2_判决/裁判/责任理由,1
A9_消费者权益与经营秩序,B3_诉求/请求能否支持,1
A9_消费者权益与经营秩序,B4_评析/认识/观点,1
A9_消费者权益与经营秩序,B5_意义/价值/保护/推动,1
A9_消费者权益与经营秩序,B6_调解/维权/纠纷解决路径,1
A10_多元纠纷解决与诉讼程序,B1_表格/裁判要点/补链,2
A10_多元纠纷解决与诉讼程序,B6_调解/维权/纠纷解决路径,1
```

## 42 Locked Core Rows Compact Evidence

### CC0084_2025_东城_二模_19
- District/year: 2025 东城 二模 Q19
- Prompt/action: 阅读材料，完成下表。
- A primary: A2_人身权与人格权
- A secondary/boundary: 有：A9_消费者权益与经营秩序;A5_知识产权与市场竞争接口;A4_合同
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 三个案例：13周岁未成年人被经营者大面积文身，法院判退费并赔偿；自媒体无事实依据贬损某公司并造成负面影响，法院判道歉赔偿；平台预订境外客房后预扣房款，消费者不知情且未入住，法院判退还房款。
- Rubric/scoring anchor: 案件一写未成年人保护和公序良俗。 / 案件二写无事实依据贬损造成商誉损害，承担道歉赔偿责任。 / 案件三写格式条款和消费者知情、公平交易，平台不能用提示不清条款强扣款。
- Codex placement note: 未成年人纹身和商誉名誉先落人格权益，消费者平台扣款作为副轴。
- Guardrail: none

### CC0305_2026_海淀_一模_18_3
- District/year: 2026 海淀 一模 Q18
- Prompt/action: 围绕消费者诉求能否支持，分别判断隐私权侵害与消费者欺诈责任。
- A primary: A2_人身权与人格权
- A secondary/boundary: 有：A9_消费者权益与经营秩序
- B axis: B3_诉求/请求能否支持
- Old v12.2 entry: E3_诉求请求能否支持
- Material core: 服务消费纠纷：消费者在经营者提供的包间内活动具有私密性，商家公开包厢内监控录像片段、网络聊天信息；赵某虚假宣传具有治疗糖尿病并发症等功效、夸大功效诱导消费。
- Rubric/scoring anchor: 先分两条链：隐私权侵害链和消费者欺诈链。 / 隐私链写监控、公开信息和侵权责任。 / 消费链写虚假宣传、知情权和惩罚性赔偿条件。
- Codex placement note: 包间监控和传播聊天视频先侵害隐私，虚假功效宣传进入消费者副轴。
- Guardrail: none

### CC0150_2025_朝阳_二模_20
- District/year: 2025 朝阳 二模 Q20
- Prompt/action: 结合材料,运用《法律与生活》知识,分析上述案例。
- A primary: A2_人身权与人格权
- A secondary/boundary: 有：A3_物权与相邻关系
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 20.(10 分)在日常生活中,要把握好权利和义务的关系。 材料一 孙女士和刘先生是同一楼层的邻居,两家入户门相对,相距约2 米。刘先生在自家入户门安装 了具有“智能人脸识别”“180 度超广角”“自动人体侦测”“云存储”等功能的可视门铃摄像头,可通过 手机远程操控。孙女士认为该摄像头可能拍摄到自己及家人的日常出行规律及其他动态信息,要求刘先生 拆除该摄像头,双方由此产生纠纷。 材料二 《中华人民共和国民法典》(节选) 第二百七十一条 业主对建筑物内的住宅、经营性用房等专有部…
- Rubric/scoring anchor: 先根据案情锁定具体权利。 / 再把侵害行为和损害结果对应起来。 / 最后写责任方式和依法保护权利的意义。
- Codex placement note: 可视门铃、人脸识别和云存储先落隐私/个人信息，相邻关系解释边界。
- Guardrail: none

### CC0332_2026_石景山_二模_19
- District/year: 2026 石景山 二模 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，谈谈对未成年人校园欺凌违法行为“惩”“教”并行的认识。
- A primary: A2_人身权与人格权
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 19．（8分） 2026年1月1日，新修订的《中华人民共和国治安管理处罚法》正式施行，首次将校园欺凌纳入治安管理处罚范畴，明确以殴打、侮辱、恐吓等方式实施学生欺凌的，公安机关可直接介入，对违反治安管理的欺凌行为依法处罚，同时采取矫治教育等措施。“他还是个孩子”，不再是校园欺凌的挡箭牌。 本次修订打破了“未成年人违法不拘留”的惯例，规定已满14周岁不满16周岁的未成年人，一年内两次以上违反治安管理的，依法执行行政拘留；已满14周岁不满18周岁，初次违反治安管理但情节严重、影响恶…
- Rubric/scoring anchor: 先写校园欺凌是违法行为，需要依法惩戒。 / 再写未成年人保护要求教育矫治并重，不能只罚不教。 / 最后写惩教并行既保护受害人，也帮助未成年人回归正轨。
- Codex placement note: 校园欺凌惩教并行主要保护未成年人人身人格利益，但属公法边界题，保留边界标记。
- Guardrail: none

### CC0364_2026_通州_期中_19_1
- District/year: 2026 通州 期中 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，分析判决结果并说明理由。
- A primary: A3_物权与相邻关系
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 某小区3号楼2单元全体业主一致同意增设电梯，已公示、承诺、提交图纸，公示期未收到异议并取得审批手续。相邻楼业主范某认为影响采光，多次阻碍施工。法院现场勘查认为全玻璃设计未对采光造成影响，判令范某停止阻碍；若投入使用后确有较大影响，可另行协商或依法解决。
- Rubric/scoring anchor: 先写加装电梯已获同意、公示和审批，程序合法。 / 再写现场勘查显示未影响采光，范某阻碍没有事实依据。 / 最后写相邻关系应方便生活、公平合理，判令停止妨害，同时保留后续补偿或法律途径。
- Codex placement note: 加装电梯与相邻妨碍是内容主轴，程序合法性为裁判支撑。
- Guardrail: Procedure legality is rewarded in this case because the original answer includes legal proportion consent/procedure and the source card says procedure was locked. It is not a universal first sentence for all E2 questions. Do not import the separate 逻辑与思维 subquestion atoms R02..08 into the law framework.

### CC0340_2026_西城_一模_17
- District/year: 2026 西城 一模 Q17
- Prompt/action: 结合材料，运用法律相关知识，说明民法典物权编的上述规定如何推动国家绿色发展。
- A primary: A3_物权与相邻关系
- A secondary/boundary: 有：A6_侵权责任
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 17．（8分）良好生态环境是最公平的公共产品，是最普惠的民生福祉。 【民法典物权编】 第286条： 业主应当遵守法律、法规以及管理规约，相关行为应当符合节约资源、保护生态环境的要求。对于物业服务企业或者其他管理人执行政府依法实施的应急处置措施和其他管理措施，业主应当依法予以配合。 业主大会或者业主委员会，对任意弃置垃圾、排放污染物或者噪声等损害他人合法权益的行为，有权依照法律、法规以及管理规约，请求行为人停止侵害、排除妨碍、消除危险、恢复原状、赔偿损失。 …… 第294条：不…
- Rubric/scoring anchor: 先写物权编规定民事主体行使物权应兼顾绿色原则和公共利益。 / 再结合业主规约、停止侵害、恢复原状说明规则如何约束行为。 / 最后写这些规定把绿色发展落实到日常民事生活。
- Codex placement note: 小区共有和物业规则推动绿色发展，以物权/物业秩序为主，环境侵权责任为副轴。
- Guardrail: none

### CC0092_2025_东城_期末_19_1
- District/year: 2025 东城 期末 Q19
- Prompt/action: 遇到的法律问题：____、____。
- A primary: A3_物权与相邻关系
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B6_调解/维权/纠纷解决路径
- Old v12.2 entry: E6_调解维权纠纷解决证据路径
- Material core: 社区有446辆电动自行车但只有60个充电接口，居民围绕公共区域设置电池充电柜产生分歧：占用绿地、无集中充电设备、消防安全、通行和采光等。学生提出在公共区域设置“车电分离”的电池充电柜方案，资料卡给出消防规定和民法典共有部分用途改变规定。
- Rubric/scoring anchor: 先写本题要找法律问题，不是直接出治理口号。 / 再从共有部分用途、消防安全、人身财产安全和相邻权中选具体问题。 / 最后说明解决分歧要在合法程序和权利边界内协商。
- Codex placement note: 共有区域充电柜、消防安全和相邻权利以物权/物业关系为主，程序解决为副轴。
- Guardrail: none

### CC0189_2025_石景山_一模_20
- District/year: 2025 石景山 一模 Q20
- Prompt/action: 阅读材料，参考示例，完成下表。
- A primary: A4_合同
- A secondary/boundary: 有：A5_知识产权与市场竞争接口
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 案例一：科技公司与电路公司签订集成电路研发委托合同，约定按标准按期交付；被告阶段性产品不达标且进度超期，最终仍未提交达标成果，法院判返还服务费并支付违约金。案例二：“好省”APP上线三年后，被告开发“超好省-省钱助手”，名称图标相近、业务内容相同，造成公众混淆，法院判停止侵权并赔偿。
- Rubric/scoring anchor: 案例一按合同违约写：有约定、未达标、超期、担责。 / 案例二按不正当竞争写：近似标识、业务相同、混淆、担责。 / 最后把规则作用落到守约研发、公平竞争和新质生产力。
- Codex placement note: 研发委托合同违约和软件混淆竞争并列，第一格合同链承担主入口。
- Guardrail: none

### CC0054_2024_石景山_一模_17
- District/year: 2024 石景山 一模 Q17
- Prompt/action: 运用法律知识，结合案情，说明甲乙两公司合同成立的理由，并从民法基本原则角 度阐述该司法判决的意义。
- A primary: A4_合同
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 乙公司发布碳排放配额采购比选公告；甲公司报价内容具体明确并承诺违约补差；乙公司确认中标并送达通知，之后甲公司拒不履行导致乙公司高价另购。
- Rubric/scoring anchor: 先写报价具体明确构成要约，中标通知到达构成承诺，合同成立。 / 再写合同成立后双方应全面履行、遵循诚信原则，拒不履行应担责。 / 最后从碳排放配额交易看，判决维护交易安全，也服务绿色发展。
- Codex placement note: 要约承诺与合同成立是主轴。
- Guardrail: none

### CC0244_2026_东城_期中_18
- District/year: 2026 东城 期中 Q18
- Prompt/action: 运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。
- A primary: A4_合同
- A secondary/boundary: 有：A6_侵权责任
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 18. 无人机起飞如何系好“安全带”? 陈某向店主刘某发送邮件：“急需购买A 型号无人机一台。用于重要商业拍摄。”刘某回复：“全新 原装，15000 元。”陈某立即转账。刘某误将一台内部结构轻微损伤（外观无明显痕迹）的同型号展示机 寄出。 陈某收货后在首次使用中，该无人机因上述损伤失控坠毁，砸伤陈某手臂。陈某花费医疗费8000 元，并因错过商业拍摄损失收入5000 元。陈某要求刘某赔偿，双方协商未果。 （1） （2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工…
- Rubric/scoring anchor: 先确定双方是什么法律关系。 / 再看行为违反了什么义务、侵害了什么权利。 / 最后写应承担的法律责任和依据。
- Codex placement note: 无人机买卖的要约承诺、错发瑕疵品和合同责任为主轴，坠机损害作侵权副轴。
- Guardrail: none

### CC0019_2024_朝阳_一模_19
- District/year: 2024 朝阳 一模 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，分析诚信原则对促进社会主义市场经济健康发展的积极作用。
- A primary: A4_合同
- A secondary/boundary: 有：A9_消费者权益与经营秩序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 民法典第七条确立诚信原则。镜头一：A公司依约供货，B公司长期拖欠货款，法院判令B公司付清欠款并支付逾期违约金。镜头二：购物中心用“码上诚信”公开商户信用信息，消费者因商家信用、商品质量和售后服务而放心消费。
- Rubric/scoring anchor: 先写民法典诚信原则是社会主义市场经济中民事活动的重要规则。 / 再用合同拖欠货款说明诚信原则约束合同履行、保护守约方。 / 最后用码上诚信说明经营者诚信经营能保护消费者权益、维护健康市场秩序。
- Codex placement note: 合同欠款和诚信履行是主轴，商户信用与消费信心为副轴。
- Guardrail: none

### CC0245_2026_东城_期中_18_2
- District/year: 2026 东城 期中 Q18
- Prompt/action: 维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
- A primary: A4_合同
- A secondary/boundary: 有：A6_侵权责任;A10_多元纠纷解决与诉讼程序
- B axis: B6_调解/维权/纠纷解决路径
- Old v12.2 entry: E6_调解维权纠纷解决证据路径
- Material core: 陈某邮件表示急需购买A型号无人机，刘某回复全新原装15000元，陈某转账；刘某误寄内部结构受损的展示机。陈某首次使用时无人机因损伤失控坠毁，砸伤手臂并造成医疗费和误工损失；双方协商未果。
- Rubric/scoring anchor: 先选路径：调解、仲裁或诉讼，协商未果后路径要升级。 / 再备证据：合同订单、邮件转账、无人机故障、伤害和损失、因果关系。 / 最后明诉求：可主张违约责任或侵权责任，提出退费、医疗费、误工损失等合理请求。
- Codex placement note: 无人机瑕疵买卖可走违约或侵权，合同请求权是主轴。
- Guardrail: none

### CC0137_2025_昌平_二模_20
- District/year: 2025 昌平 二模 Q20
- Prompt/action: 阅读材料，运用《法律与生活》知识，完成裁判理由。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A4_合同
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: （1）李某使用 AI 绘图软件制作图片，加“AI 绘画”等标签发布；刘某未经许可拿来配图并抹去水印；法院支持李某诉讼请求。（2）小王申请开通信用卡，声明已阅览申请材料并愿意遵守领用合约；使用信用卡透支消费后未按约还款；银行诉至法院；法院判决小王偿还本金和利息。
- Rubric/scoring anchor: AI 格：AI 不是著作权主体，但李某使用 AI 形成的独创性智力成果受保护；刘某未经许可使用并抹水印，侵犯著作权，应担责。 / 信用卡格：双方信用卡领用合约合法有效，小王透支后未按约还款，违反诚信和全面履行原则，应承担违约责任。 / 裁判理由题是一格一链，不能把两个格子糊成一个创新题。
- Codex placement note: AI 图片著作权是第一内容轴，信用卡领用合同作第二格。
- Guardrail: CC0137 only supports one-grid-one-chain table reasoning: AI copyright grid and credit-card contract grid. Do not expand into a general AI innovation trunk.

### CC0157_2025_朝阳_期末_20
- District/year: 2025 朝阳 期末 Q20
- Prompt/action: 了解案件，分析事实，印证法理，参考示例，完成下表。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A6_侵权责任;A9_消费者权益与经营秩序
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 案例二：丙公司通过电子地图数据、用户出行数据和实时交通信息，经算法形成“拥堵延时指数”；丁公司用变换IP、伪造浏览器标识等手段抓取数据，并在付费软件中商业化使用。案例三：甲购买旅游门票参加“摇摆桥”，工作人员过度摇晃桥面致甲摔伤住院并构成伤残，甲起诉旅游公司赔偿。
- Rubric/scoring anchor: 案件二按“不正当手段抓取数据—不正当竞争—停止侵害赔偿”写。 / 案件三按“安全保障义务—过错和因果—侵权/违约责任”写。 / 如果写责任范围，要记得游客自身注意义务可能影响分担。
- Codex placement note: 数据抓取不正当竞争是主要法益，旅游安全保障以侵权责任承接。
- Guardrail: none

### CC0213_2025_门头沟_一模_20
- District/year: 2025 门头沟 一模 Q20
- Prompt/action: 结合以下案例，参照所给出完成下表。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A8_劳动关系
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 案例一给出“我不是胖虎”美术作品著作权侵权示例。案例二：孙某应聘甲公司时简历只写4段工作经历，入职后查明其7年间曾在17家公司任职；甲公司以未如实提供工作经历为由，在试用期内解除劳动关系。
- Rubric/scoring anchor: 先照案例一的格式：裁判结果、裁判理由、现实意义。 / 案例二结果写驳回孙某请求，甲公司无需赔偿。 / 理由写诚实信用、知情权、劳动合同无效或解除合法；意义写维护用人单位权益和诚信劳动关系。
- Codex placement note: 著作权示例与劳动诚信并列，但题面先以知识产权示例组织表格。
- Guardrail: none

### CC0206_2025_西城_期末_19
- District/year: 2025 西城 期末 Q19
- Prompt/action: “唤醒词”亦受法律保护，请运用法律知识分析法院的判决。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A9_消费者权益与经营秩序
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: M公司推出“小爱同学”智能语音设备后，“小爱同学”作为唤醒词和商品名称已有较高影响。陈某抢先在不同商品类别申请相关商标，并与Y公司在手表、闹钟等商品上使用“小爱同学”商标、发布宣传文章。M公司起诉，法院认定受反不正当竞争法保护，判停止侵权并赔偿。
- Rubric/scoring anchor: 先说明“小爱同学”已经形成一定影响，应受反不正当竞争法保护。 / 再结合抢注、使用、宣传说明混淆和虚假宣传。 / 最后写判决制止不正当竞争，保护创新企业商誉，维护数字经济秩序。
- Codex placement note: 标识混淆、商标抢注和虚假宣传指向知识产权与竞争秩序。
- Guardrail: none

### CC0103_2025_丰台_一模_19
- District/year: 2025 丰台 一模 Q19
- Prompt/action: 结合材料，运用法治相关知识，分析本案作为人民法院保护科技创新典型案例的意义。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A8_劳动关系
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 19. 2024 年6 月，最高人民法院知识产权法庭对一起因技术秘密侵权纠纷上诉案作出判决。原告方下 属公司的近40 名高级管理人员及技术人员离职后加入被告方，并利用在原单位接触的技术信息申请了12 件实用新型专利。 根据《中华人民共和国反不正当竞争法》，最高人民法院知识产权法庭依法适用2 倍惩罚性赔偿，判 决被告方赔偿原告方经济损失及维权合理开支合计6.4 亿余元，创下我国知识产权侵权诉讼判赔数额新 高。 该案在停止侵害民事责任承担的具体方式、内容、范围，以及拒绝履行、停止…
- Rubric/scoring anchor: 先写技术秘密属于知识产权保护对象，任何主体不得以不正当手段获取和使用。 / 再结合离职人员、专利申请和竞争行为说明侵权及不正当竞争。 / 最后写惩罚性赔偿提高违法成本，有利于保护科技创新和公平竞争。
- Codex placement note: 技术秘密、实用新型和惩罚性赔偿构成知识产权/竞争主轴，前员工身份为副轴。
- Guardrail: none

### CC0131_2025_房山_一模_19
- District/year: 2025 房山 一模 Q19
- Prompt/action: 结合材料，谈谈“真创新”受到“真保护”的法治价值。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A8_劳动关系
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: A集团近40名高管及技术人员离职赴B集团工作；B集团利用离职人员在原单位接触掌握的新能源汽车底盘技术信息申请12件实用新型专利，并在无合法技术来源情况下短期推出相关车型；法院认定B集团以不正当手段侵害A集团技术秘密，适用2倍惩罚性赔偿，判赔6.4亿余元。
- Rubric/scoring anchor: 先写技术秘密和知识产权应受法律保护。 / 再结合离职人员、技术信息、无合法来源说明B集团构成不正当竞争。 / 最后写惩罚性赔偿提高侵权成本，维护公平竞争，激励真创新。
- Codex placement note: 新能源底盘技术秘密和不正当竞争主轴。
- Guardrail: none

### CC0229_2026_东城_一模_18
- District/year: 2026 东城 一模 Q18
- Prompt/action: 结合材料，运用《法律与生活》知识，谈谈法院是如何以司法之力守护“向新力”的。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 18．（8 分）人民法院以司法之力守护“向新力”。 案例一 某科技公司三名创始人，因专利权归属纠纷，陷入长期诉讼，公司发展因此停滞。对此，办 案合议庭没有“一判了之”，而是居中斡旋，弥合分歧。当事人最终达成和解，全身心投入创新创业，实 现了多方共赢。 案例二 甲公司系某水稻植物新品种的权利人。乙公司擅自将甲公司享有植物新品种权的稻种更换包 装后对外销售。经人民法院查明，乙公司侵权行为覆盖范围广。人民法院判令乙公司立即停止侵害，并对 其适用惩罚性赔偿，赔偿甲公司经济损失300 …
- Rubric/scoring anchor: 法院通过解决知识产权权属纠纷，稳定创新主体预期。 / 通过惩罚性赔偿提高侵权成本，保护创新成果。 / 通过规制恶意诉讼和权利滥用，维护公平竞争和创新环境。
- Codex placement note: 司法保护创新以知识产权主轴组织，调解和惩罚性赔偿为程序工具。
- Guardrail: none

### CC0283_2026_朝阳_一模_18
- District/year: 2026 朝阳 一模 Q18
- Prompt/action: 结合材料，运用《法律与生活》知识，谈谈人民法院是如何依法保护知识产权以护航新质生产力发展的。
- A primary: A5_知识产权与市场竞争接口
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 人民法院以“调、惩、辩”三维实践护航创新：通过第三方调解高效化解生物医药领域专利权归属纠纷；对故意侵害植物新品种权、商业秘密等行为适用惩罚性赔偿；对假借维权实施恶意诉讼、权利滥用的行为快速审结并否定。
- Rubric/scoring anchor: 按“调、惩、辩”三段写。 / 每段先写法院做了什么，再写保护了什么。 / 最后总收束：保护知识产权、兼顾公共利益，为新质生产力提供稳定法治环境。
- Codex placement note: 知识产权保护为主，调解、惩罚性赔偿和反恶意诉讼为程序副轴。
- Guardrail: none

### CC0289_2026_朝阳_二模_18
- District/year: 2026 朝阳 二模 Q18
- Prompt/action: 结合材料，运用《法律与生活》知识，将以上回答补充完整。从以上三个问答中任选其一，谈谈如何依法保护问答中所涉及到的权利。
- A primary: A6_侵权责任
- A secondary/boundary: 有：A2_人身权与人格权;A3_物权与相邻关系;A10_多元纠纷解决与诉讼程序
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 三个问答分别涉及：高空抛物、坠物危害人身权益且适用举证责任倒置；安装摄像头可能影响邻居隐私，需要沟通协商、调整拍摄范围或拆除设备；违法构筑物影响通行、通风、采光，涉及相邻不动产权利人合法权益，原告需举证影响。
- Rubric/scoring anchor: 先把三个问答分别补成具体权利和规则。 / 任选一个时，按权利名、侵害事实、保护路径写。 / 最后说明依法保护权利要既有实体权利也有证据和程序意识。
- Codex placement note: 高空抛物/物件损害带出侵权主轴，隐私、相邻和救济路径为副轴。
- Guardrail: Primary delivery is completion of three Q&A blanks; the '任选其一' part then asks rights-protection by basis + action + remedy. Choosing question 1/2/3 itself is not scored; personal information and 必修三 slogans are not scored.

### CC0002_2024_丰台_一模_17
- District/year: 2024 丰台 一模 Q17
- Prompt/action: 结合材料，运用《法律与生活》知识，谈谈法院酌情减轻被告赔偿责任的法理依据和现实意义。
- A primary: A6_侵权责任
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 甲某无偿搭乘乙某车辆且未系安全带；乙某雨天驾驶发生交通事故致甲某受伤；民法典好意同乘规则要求对非故意、非重大过失的驾驶人减轻赔偿责任。
- Rubric/scoring anchor: 先说明本案是好意同乘交通损害，不是合同纠纷。 / 再写驾驶人无故意或重大过失，无偿搭乘关系下可酌情减轻赔偿责任。 / 最后写这样既保护受害人合法权益，也鼓励互助善意并守住安全责任边界。
- Codex placement note: 好意同乘交通损害是侵权减责，A1 只提示民事关系底盘。
- Guardrail: none

### CC0254_2026_丰台_二模_18
- District/year: 2026 丰台 二模 Q18
- Prompt/action: 司法给予我们的不仅是定分止争，也是一份融通情理的温暖力量。结合材料，综合运用法治知识，阐明你对这一观点的认识。
- A primary: A6_侵权责任
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 张某承包果园，李某饲养的牛群多次闯入果园造成果树受损、减产；民法典规定饲养动物造成他人损害，动物饲养人或管理人应承担侵权责任。法院受理后现场勘验，释明民法典饲养动物损害责任，并结合生态环境法典理念提出“分期赔偿+行为约束+生态修复”调解方案，促成和解。
- Rubric/scoring anchor: 先写饲养动物造成他人损害，饲养人或管理人依法承担侵权责任。 / 再写法院通过现场勘验和释明规则厘清责任。 / 最后写调解方案兼顾赔偿、行为约束和生态修复，体现法律温度。
- Codex placement note: 牛入果园致损是动物/侵权责任，调解方案为 B6 副动作。
- Guardrail: none

### CC0011_2024_丰台_二模_17
- District/year: 2024 丰台 二模 Q17
- Prompt/action: 运用《法律与生活》知识，结合上述案例分析民法典的相关规定对保护生态环境的作用。
- A primary: A6_侵权责任
- A secondary/boundary: 有：A5_知识产权与市场竞争接口
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 民法典守护碧水蓝天。案例一：某公司发明污水污泥分离技术，解决长期污水污泥分离难题，并在农村污水净化处理项目中应用推广。案例二：甲公司长期超标排放废水、废气等污染物损害环境公共利益，乙环境研究所提起环境民事公益诉讼，法院判令甲公司立即停止侵权、消除危险、赔偿环境损失。
- Rubric/scoring anchor: 先写民法典绿色原则要求民事活动有利于节约资源、保护生态环境。 / 再结合两个案例写知识产权保护促进绿色技术应用，侵权责任追究约束污染行为。 / 最后落到民法典以权利保护、义务约束和责任承担推动生态环境保护。
- Codex placement note: 生态环境公益诉讼以侵权责任和停止损害为主，专利技术保护为副轴。
- Guardrail: none

### CC0180_2025_海淀_期末_20
- District/year: 2025 海淀 期末 Q20
- Prompt/action: 下表列出了《最高人民法院关于适用〈中华人民共和国民法典〉侵权责任编的解释（一）》部分条款。参考示例，完成下表。
- A primary: A6_侵权责任
- A secondary/boundary: 有：A9_消费者权益与经营秩序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 最高人民法院围绕民法典侵权责任编重大争议制定解释。题表要求解释两类规则：缺陷产品造成产品自身损害是否纳入产品责任赔偿范围；禁止饲养的烈性犬等危险动物造成损害时，动物饲养人或管理人如何承担责任。
- Rubric/scoring anchor: 第一格写缺陷产品责任：无过错责任，保护消费者。 / 第二格写禁养危险动物致害：最严格无过错责任，强化饲养人责任。 / 最后收束到司法解释明确责任边界、保障生命财产安全。
- Codex placement note: 产品责任、危险动物和无过错责任是侵权主轴，消费者保护为副轴。
- Guardrail: none

### CC0051_2024_海淀_期中_21_1
- District/year: 2024 海淀 期中 Q21
- Prompt/action: 运用法治知识，对小海的观点进行评析。
- A primary: A7_婚姻家庭与继承
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 1950年婚姻法确立婚姻自由、一夫一妻、保护妇女儿童权益；其中离婚共同债务不足时规定“由男方清偿”。民法典婚姻家庭编规定离婚时夫妻共同债务应共同偿还，共同财产不足或财产归各自所有的，由双方协议清偿，协议不成由人民法院判决。小海认为1950年规定不合理，民法典规定才符合良法要求。
- Rubric/scoring anchor: 先表态：小海观点有合理之处，但不能脱离历史条件全盘否定1950年婚姻法。 / 再比较：1950年规定符合当时废除封建婚姻制度的需要，民法典规定更体现平等保护和权利义务统一。 / 最后落点：良法要从实际出发并随时代发展完善，维护婚姻家庭关系中的公平正义。
- Codex placement note: 夫妻共同债务和法律变迁属于婚姻家庭财产规则。
- Guardrail: Use as recovered evidence for evaluation of a view under marriage-family law and good-law standards. Do not create a broad legal-change trunk, and do not turn it into 必修三 scientific legislation slogans.

### CC0061_2024_西城_一模_18
- District/year: 2024 西城 一模 Q18
- Prompt/action: 运用法治知识，谈谈对二审法院向郭某的三个儿子发出《督促履行义务告知书》的认识。
- A primary: A7_婚姻家庭与继承
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 九十岁郭某起诉三子支付赡养费，一审未支持；二审虽未支持抚养费请求，但基于老人精神陪伴需求向三个儿子发出督促履行义务告知书。
- Rubric/scoring anchor: 先写成年子女对父母负有赡养义务。 / 再说明赡养包括经济供养、生活照料和精神慰藉，不能只给钱。 / 最后写法院告知书以柔性方式督促履行，有助于保护老人权益和家庭和谐。
- Codex placement note: 成年子女赡养父母是家庭法义务。
- Guardrail: none

### CC0045_2024_海淀_二模_19
- District/year: 2024 海淀 二模 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，分析本案判决的社会价值。
- A primary: A7_婚姻家庭与继承
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 19．（6 分）遗赠扶养协议纠纷案宣判。 【案情简介】某社区居委会与曹某签订协议，约定由某居委会定时定员结对子照看关心曹某， 每月给予曹某基本生活费，免费看病诊治，逢年过节给予曹某各类生活补助及慰问生活用品等， 养老至寿终；曹某现有的动产和不动产在曹某寿终后，产权移交某居委会。此后，某居委会按照 约定履行扶养义务。曹某去世后，曹某的四个子女要求继承遗产，与该居委会产生争议。该居委 会遂将曹某的四个子女等人诉至法院，请求判令：（1）确认某居委会与曹某签订的协议有效；（2） 曹某…
- Rubric/scoring anchor: 先写遗赠扶养协议依法有效，扶养人履行义务应受保护。 / 再结合居委会照料老人和子女争议说明判决维护诚信和老人权益。 / 最后写判决有助于鼓励多元养老、弘扬家庭和社会责任。
- Codex placement note: 遗赠扶养协议、老人权益和多元养老属于婚姻家庭继承主轴。
- Guardrail: none

### CC0214_2025_门头沟_一模_20_2
- District/year: 2025 门头沟 一模 Q20
- Prompt/action: 参照案例一，完成案例二的裁判理由。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 孙某入职甲公司时隐瞒真实工作经历，甲公司在违背真实意思情况下与其签订劳动合同；试用期内查证后解除劳动关系，孙某请求赔偿。
- Rubric/scoring anchor: 先写劳动合同订立要遵循诚实信用。 / 再写孙某隐瞒经历使甲公司违背真实意思签约。 / 最后写甲公司解除劳动关系合法，不承担赔偿责任。
- Codex placement note: 劳动合同诚信题；A1 只作为真实意思表示和行为效力底层。
- Guardrail: none

### CC0025_2024_朝阳_二模_17
- District/year: 2024 朝阳 二模 Q17
- Prompt/action: 结合材料,说明仲裁委员会作出上述裁决的理由,并分析该典型案例的意义。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 平台企业与劳动者签合作协议，但平台派单、签到、奖惩、结算并把运输服务纳入自身业务组成；仲裁支持劳动者确认事实劳动关系。
- Rubric/scoring anchor: 先写不能只看合作协议名称，要看实际用工关系。 / 再从派单、签到、奖惩、结算和业务组成说明三从属性。 / 最后写仲裁认定劳动关系有利于保护新就业形态劳动者合法权益，规范平台用工。
- Codex placement note: 平台用工事实劳动关系，仲裁裁决只是 B 轴动作。
- Guardrail: none

### CC0119_2025_丰台_期末_19
- District/year: 2025 丰台 期末 Q19
- Prompt/action: 请运用《法律与生活》相关知识阐释法院的裁判理由。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 尹某在购物中心任主管期间违反管理规章，单位结合经营需要调整其岗位。尹某消极怠工、经常无故旷工，经多次提醒仍未改变。购物中心解除劳动合同，尹某诉请支付违法赔偿金，法院驳回其诉讼请求。
- Rubric/scoring anchor: 先写劳动者既有权利也有义务。 / 再结合尹某旷工和违反规章说明解除有法律依据。 / 最后写法院驳回赔偿请求，维护合理用工秩序和健康劳动关系。
- Codex placement note: 劳动纪律与解除劳动合同。
- Guardrail: none

### CC0181_2025_海淀_期末_21
- District/year: 2025 海淀 期末 Q21
- Prompt/action: 结合材料，运用《法律与生活》知识，说明法律规定“竞业限制”并对其加以限制的原因。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A5_知识产权与市场竞争接口
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 21. 阅读材料，完成问题。 “竞业限制”是指用人单位与劳动者之间约定，劳动者在离职后不得到生产同类产品或经营同类产业且有竞争关系的其他用人单位任职，也不得自己生产与原单位有竞争关系的同类产品或经营同类业务。 案例一：李某是A公司自主培养的高级管理人员。在职期间，李某与该公司签订了保密协议和竞业限制协议。两年后，李某离职，次日即入职相同经营范围和业务的B公司，任职相同岗位，负责相同产品生产。该产品生产技术属A公司“不为公众所知悉的技术信息”，A公司将李某诉至法院。法院经审理认…
- Rubric/scoring anchor: 先写竞业限制是为了保护用人单位商业秘密和竞争利益。 / 再写竞业限制会影响劳动者就业权，因此必须依法、合理、适度。 / 最后写法律既保护企业创新，也保障劳动者自主择业和人才合理流动。
- Codex placement note: 竞业限制在劳动关系内平衡商业秘密和就业权。
- Guardrail: none

### CC0373_2026_顺义_一模_18
- District/year: 2026 顺义 一模 Q18
- Prompt/action: 结合材料，运用《法律与生活》知识，闫某和张某的诉求能否得到法院的支持，并说明理由。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A5_知识产权与市场竞争接口;A1_民事法律关系总论
- B axis: B3_诉求/请求能否支持
- Old v12.2 entry: E3_诉求请求能否支持
- Material core: 闫某求职遭公司以仅招男性为由拒绝面试；张某原系A公司总经理并签订竞业限制协议，离职后其妻成为B公司投资人，B公司业务与A公司竞争，且B公司关联公司为张某缴纳社保。
- Rubric/scoring anchor: 先分判两个诉求：就业歧视和竞业限制。 / 就业歧视链写平等就业权；竞业限制链写保护商业秘密与劳动者就业权平衡。 / 最后说明法院应在企业利益和劳动者权益之间依法平衡。
- Codex placement note: 就业平等和竞业限制均属劳动关系，商业竞争利益和主体关系为副轴。
- Guardrail: none

### CC0195_2025_西城_一模_20
- District/year: 2025 西城 一模 Q20
- Prompt/action: 结合材料，综合运用经济和法律的知识，说明上述做法能促进社会公平与经济效率的平衡。
- A primary: A8_劳动关系
- A secondary/boundary: 有：A10_多元纠纷解决与诉讼程序
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 全国总工会、人社部等启动集体协商“集中要约行动”，指导工会与企业开展集体协商、签订集体合同；各级工会把工资调整幅度、加班工资基数、劳动定额标准、工资支付办法等作为协商核心议题。
- Rubric/scoring anchor: 先写集体协商是劳动者依法表达利益诉求的机制。 / 再写工资、加班、劳动定额等议题关系劳动者权益和企业管理。 / 最后落到公平保护劳动者、效率稳定企业生产，两者通过协商机制实现平衡。
- Codex placement note: 工会平台、集体协商、工资工时和劳动定额属于劳动关系主轴。
- Guardrail: Keep as law-supported labor-rights fairness/efficiency evidence: union platform + collective contract + labor-rights protection + enterprise lawful employment + efficiency. Do not classify as non-legal economics by default.

### CC0200_2025_西城_二模_18
- District/year: 2025 西城 二模 Q18
- Prompt/action: 结合材料，运用《法律与生活》的知识，分析人民法院的判决结果。
- A primary: A9_消费者权益与经营秩序
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B2_判决/裁判/责任理由
- Old v12.2 entry: E2_判决裁判责任理由
- Material core: 17 岁小刘背着家长、绕过平台监管打赏多名网络主播，金额高达 45 万余元；家长事先不知情、事后不追认；平台发现异常后采取限制措施，但小刘冒充监护人与平台客服沟通，绕过限制；家长诉请返还打赏款。
- Rubric/scoring anchor: 先写小刘是限制民事行为能力人，大额打赏未经监护人追认，交易效力有问题。 / 再写平台、监护人、小刘本人均有过错。 / 最后写法院综合各方过错程度，依据公平原则分担责任，既保护未成年人，也规范平台和监护责任。
- Codex placement note: 直播打赏发生在消费者/平台交易场景，未成年人行为能力作为关键副轴。
- Guardrail: none

### CC0143_2025_朝阳_一模_19
- District/year: 2025 朝阳 一模 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，说明人民法院支持王某的诉讼请求的理由。
- A primary: A9_消费者权益与经营秩序
- A secondary/boundary: 有：A4_合同
- B axis: B3_诉求/请求能否支持
- Old v12.2 entry: E3_诉求请求能否支持
- Material core: 机票代销平台在交易中隐蔽搭售/诱导消费者购买增值服务，消费者无法清楚知悉或有效拒绝；争点是合同成立后是否可撤销及三倍赔偿。
- Rubric/scoring anchor: 先写平台作为经营者应真实、全面告知服务信息，保障消费者知情权和自主选择权。 / 再写隐蔽搭售使消费者难以清楚知悉和有效拒绝，构成欺诈。 / 最后写消费者请求退赔和惩罚性赔偿有法律依据，法院应予支持。
- Codex placement note: 平台捆绑购票和诱导购买以消费者知情选择为主轴，合同撤销/格式安排为副轴。
- Guardrail: none

### CC0238_2026_东城_二模_19
- District/year: 2026 东城 二模 Q19
- Prompt/action: 结合材料，运用《法律与生活》知识，评析乙公司和张某的行为。
- A primary: A9_消费者权益与经营秩序
- A secondary/boundary: 有：A5_知识产权与市场竞争接口;A8_劳动关系
- B axis: B4_评析/认识/观点
- Old v12.2 entry: E4_评析认识谈看法
- Material core: 19．（8分）法治是最好的营商环境。大健康产业蓬勃发展，需要企业规范深耕。 甲公司开拓新领域，打造“中药＋餐饮＋健康检测”一站式新型养生空间。为加速项目落地，甲公司开启对外招商，锁定乙、丙两家公司作为候选合作伙伴。 乙公司为在竞争中胜出，捏造事实向甲公司项目负责人张某暗示丙公司的管理能力、产品质量低下。张某信以为真，在未经查证的情况下，违规直接与乙公司签订承包合同。后乙公司进场施工，因管理混乱导致项目严重延期。甲公司因此遭受重大经济损失。
- Rubric/scoring anchor: 对乙公司：行为定性 + 法律后果 + 规范经营/公平竞争。 / 对张某：行为定性 + 劳动纪律/职业道德/诚信义务 + 应然要求。 / 价值：法律规制不正当行为，维护公平竞争和营商环境。
- Codex placement note: 经营秩序和商业诋毁为主，劳动纪律/职业诚信为第二场景。
- Guardrail: none

### CC0063_2024_西城_二模_16
- District/year: 2024 西城 二模 Q16
- Prompt/action: 结合材料，运用《法律与生活》的知识，分析人民法院判决的意义。
- A primary: A9_消费者权益与经营秩序
- A secondary/boundary: 有：A1_民事法律关系总论
- B axis: B5_意义/价值/保护/推动
- Old v12.2 entry: E5_意义价值作用保护推动
- Material core: 16．（8分） 市民甲在某食品科技有限公司开设的网店中购买了30盒“黄芪薏米饼干”，付款516元。签收后，甲发现这些饼干不符合食品安全标准，随后又在两个月内三次购买同样的饼干，总数达200盒。四次总计付款4176元。甲以产品中添加有黄芪粉，违反了有关规定为由，起诉请求经营者退还价款4176元，支付相当于价款十倍的赔偿金41760元。 审理法院认为，某食品科技有限公司违反我国关于食品安全的相关规定，属于生产经营不符合食品安全标准食品的行为，应依法承担责任。市民甲首单购买的30盒…
- Rubric/scoring anchor: 先写经营者销售不合格食品损害消费者权益，首单维权应获支持。 / 再写后续知假大量购买带有牟利性，不能机械支持全部惩罚性赔偿。 / 最后写判决兼顾食品安全保护与诚信行使权利。
- Codex placement note: 食品安全、惩罚性赔偿和消费者身份边界。
- Guardrail: none

### CC0125_2025_延庆_一模_19
- District/year: 2025 延庆 一模 Q19
- Prompt/action: 运用《法律与生活》知识，说明你会如何进行调解并说 明理由。
- A primary: A9_消费者权益与经营秩序
- A secondary/boundary: 有：A4_合同;A10_多元纠纷解决与诉讼程序
- B axis: B6_调解/维权/纠纷解决路径
- Old v12.2 entry: E6_调解维权纠纷解决证据路径
- Material core: 19. 网络经济持续健康发展，需要法治护航。 案情：杨某在贾某经营的网店下单DIY 模具类商品4 件，售价78 元，杨某签收后对商品不满意，在 未与贾某协商一致的情况下，直接点击了“仅退款”并退款成功。贾某要求杨某退回商品，杨某表示已经 将商品扔掉，无法退回。 贾某认为双方应当先确定货物是否存在质量问题，是否符合“仅退款”标准。杨某退款后应当退还货 物，虽然商品实际售价仅78 元，但杨某恶意“仅退款”的做法让自己遭受了商品损失和邮费损失。杨某 则认为商品质量不合格，达不到预期…
- Rubric/scoring anchor: 先表明调解应围绕诚信原则和公平原则。 / 再说明消费者不能退款后占有商品，商家也要举证商品质量和损失。 / 最后提出退货、补偿或协商方案，兼顾双方利益。
- Codex placement note: 网购退款不退货以消费者/经营者公平交易为主，买卖合同和调解为副轴。
- Guardrail: none

### CC0077_2025_东城_一模_19
- District/year: 2025 东城 一模 Q19
- Prompt/action: 阅读材料，完成下表。
- A primary: A10_多元纠纷解决与诉讼程序
- A secondary/boundary: 有：A4_合同;A8_劳动关系;A7_婚姻家庭与继承
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 三个案例：家装合同逾期后诉讼调解解决；医院与柳某培训协议、服务期未满辞职后申请返还违约金被仲裁驳回；顾氏三兄弟照顾孤寡老人并申请指定遗产管理人，最终获得部分遗产分配。
- Rubric/scoring anchor: 案件一填诉讼调解，写低标的争议通过调解化解。 / 案件二写培训协议有效，劳动者应守约，权利义务要统一。 / 案件三写遗产管理制度和事实扶养，落到财产保护与友善孝老。
- Codex placement note: 三案同表，程序/调解是形式主线，合同、劳动、继承作为内容副轴。
- Guardrail: none

### CC0325_2026_石景山_一模_18
- District/year: 2026 石景山 一模 Q18
- Prompt/action: 阅读材料，参考示例，分析案件中举证责任的分配方式及理由，完成下表。
- A primary: A10_多元纠纷解决与诉讼程序
- A secondary/boundary: 有：A5_知识产权与市场竞争接口;A8_劳动关系;A6_侵权责任
- B axis: B1_表格/裁判要点/补链
- Old v12.2 entry: E1_表格裁判要点补链
- Material core: 案例一：公安机关移送后，人民检察院以侵犯著作权罪、销售侵权复制品罪提起公诉。案例二：某公司不服区人社局工伤认定及区政府行政复议决定，提起行政诉讼。案例三：业主卢某开窗时窗户脱落砸坏张某车辆，张某诉请赔偿。
- Rubric/scoring anchor: 案例一写公诉案件由检察院举证。 / 案例二写行政诉讼由行政机关举证行政行为合法。 / 案例三写民事诉讼中原告证明损害和因果，建筑物使用人证明无过错。
- Codex placement note: 举证责任表以程序为主轴，三案分别牵出知识产权、劳动、侵权。
- Guardrail: none

### CC0223_2025_顺义_一模_19
- District/year: 2025 顺义 一模 Q19
- Prompt/action: （1）运用《法律与生活》知识，分析上述案例是如何解决纠纷的。
- A primary: A10_多元纠纷解决与诉讼程序
- A secondary/boundary: 有：A3_物权与相邻关系;A5_知识产权与市场竞争接口;A9_消费者权益与经营秩序
- B axis: B6_调解/维权/纠纷解决路径
- Old v12.2 entry: E6_调解维权纠纷解决证据路径
- Material core: 案例1：邻居刘某长期在门口堆放杂物垃圾，高某多次沟通、找物业、微信群反映无效，刘某还辱骂高某；高某诉至法院，经法院调解双方握手言和。案例2：乙公司将企业名称登记为与甲公司相似名称，甲公司申请企业名称争议裁决，市监局确认侵权应纠正，乙公司不服起诉，法院驳回。
- Rubric/scoring anchor: 案例1写诉讼调解+相邻关系。 / 案例2写市监裁决+行政诉讼维持，核心是不正当竞争和名称混淆。 / 最后可以落到合法权益、市场秩序和社会和谐，但必须由两个案例推出。
- Codex placement note: 两案都问纠纷如何解决，程序路径为主，分别牵出相邻和竞争秩序。
- Guardrail: Rewarded action is how disputes are solved: case 1 litigation mediation + common-area reasonable use + neighboring relation; case 2 market-regulator adjudication / administrative lawsuit / unfair competition. Value language must be derived from the two cases, not written as free-standing meaning extraction.


## Render / Delivery QA Boundary

# 07 Render QA Report

Status: `v13_0_final_baodian_pdf_rendered_docx_generated_with_docx_render_caveat`

Date: 2026-05-23

## Produced Files

- Markdown framework and 42-card handbook: `01_双轴法律主观题框架章.md` through `06_GOVERNOR_V13_0_CANDIDATE_CHECK.md`
- DOCX candidate: `选必二法律与生活_法律宝典_v13_0_双轴版.docx`
- HTML print source: `选必二法律与生活_法律宝典_v13_0_双轴版.html`
- PDF delivery: `选必二法律与生活_法律宝典_v13_0_双轴版.pdf`
- PDF page renders: `rendered_pdf_pages/page-001.png` through `page-030.png`

## Verification

| check | result | evidence |
|---|---|---|
| traceability row count | pass | `TRACEABILITY_MATRIX_v13_0_double_axis.csv` has 42 rows |
| Markdown card count | pass | `02_42题双轴重标与解析宝典.md` has 42 `###` cards |
| PDF generated | pass | `选必二法律与生活_法律宝典_v13_0_双轴版.pdf` exists, 967580 bytes |
| PDF text coverage | pass | PDF text contains 42 distinct `CC...` question IDs and `UPGRADE_TO_DOUBLE_AXIS` |
| PDF pages rendered | pass | 30 PDF pages -> 30 PNG pages |
| blank-page check | pass | rendered PNG signal check found no blank-like pages |
| visual sample | pass | inspected page 001 cover, page 015 middle question cards, page 030 governance appendix |
| DOCX generated | pass | `选必二法律与生活_法律宝典_v13_0_双轴版.docx` exists, 70165 bytes |
| DOCX Word open check | pass | Word COM opened the DOCX read-only and computed 45 pages / 759 paragraphs |
| DOCX direct render via `render_docx.py` | not passed | local LibreOffice/`soffice` executable is unavailable (`WinError 2`), so DOCX visual render QA is not claimed |

## Governor Note

The PDF delivery is rendered and checked from the HTML print source built from the same v13.0 double-axis traceability data. The DOCX exists and is openable in Word, but it must not be described as DOCX-render-QA-passed unless a future LibreOffice or Word export render path completes.


## Required Output Format

1. Verdict: one of ACCEPT_FINAL_WITH_CAVEAT / ACCEPT_AFTER_MINOR_PATCHES / REVISE_MAJOR / FAIL_FRAMEWORK.
2. Framework-level judgment: is A x B now a genuinely better legal baodian framework than v12.2 single-axis? Why?
3. Row-level audit: list any rows whose A primary, A secondary, or B label should be changed. Use exact question_id and proposed label.
4. Missing trunk or over-split risk: should any A node be merged, renamed, downgraded, or split? Use evidence from the 42 rows only.
5. Student usability: will a zero-baseline student use this better than the old six entrances? Where would they still misfire?
6. Governance: state what must be patched before final claim, if anything.
