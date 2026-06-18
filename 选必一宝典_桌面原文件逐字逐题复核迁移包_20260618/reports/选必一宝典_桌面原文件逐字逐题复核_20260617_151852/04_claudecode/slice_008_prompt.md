你是本项目的真实 ClaudeCode 复核线。使用模型目标 claude-opus-4-8，effort=max。

本次只复核 slice 008: doc_order 36-40。不要声称全书完成，不改写任何源文件。

硬规则摘要：
- 当前桌面文档字段是【材料触发点】【设问】【为什么能想到】【答案落点】【同题组】，缺独立“术语”和“细则位置”通常是结构风险。
- 普通参考答案不能冒充评分细则；没有正式评分细则/评标/阅卷总结/用户确认评分材料时，写 LOW_EVIDENCE 或 BLOCKED。
- 每条检查：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。
- 尤其注意：2026海淀二模Q20(2) 是否为短评7分且“共同利益”只是必要性知识可选项之一；2024西城二模Q19 是否为5分新思路题且共同利益只在总判断/时代背景中；2025延庆一模Q20(2) 是否为四角度8分回应“脱钩断链”；2026朝阳期末Q20 是否为“大国外交为什么更有作为”的多角度8分题，不要把共同利益当成全题唯一答案；2026朝阳二模Q20(2) 是否为人类命运共同体维护和平与发展的6分三角度题。

请完成本项目 ClaudeCode 复核。你可以只基于下方 slice 输入判断，不要改源文件；输出必须保留表格和源证据边界：

# ClaudeCode Slice 008 Findings

- model_used: claude-opus-4-8
- effort: max
- scope: doc_order 36-40 only
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e

## Findings

| doc_order | entry_id | question_ref | status | problem | evidence_pointer | suggested_fix |
|---:|---|---|---|---|---|---|

status 只用 PASS、LOW_EVIDENCE、NEEDS_FIX、BLOCKED。
表格后追加“## 源证据边界”，说明你的判断主要基于 slice 输入可见文本，仍需 Codex 回原卷/细则确认的部分。

下面是 slice 输入：

# ClaudeCode Slice 008 Input

source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
scope: document-order question entries 36-40 only; do not claim full-book completion.

## Q0036 doc_order=36 blocks=442-452
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2026海淀二模Q20(2)
- question_ref: 2026海淀二模Q20
- duplicate_group_id: UQ0058
- duplicate_group_doc_orders: 16;36;292;359
- duplicate_group_core_points: 共商共建共享的全球治理观;和平与发展仍是时代主题;国家间共同利益是国家合作的基础;践行真正的多边主义

<!-- block:442 type:paragraph style:Normal -->
10. 2026海淀二模Q20(2)

<!-- block:443 type:paragraph style:Normal -->
【材料触发点】 全球发展倡议本身就是题目主题，材料要求把中国倡议与国际发展合作实践连接起来。

<!-- block:444 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，围绕“全球发展倡议从合作理念到丰富实践”这一主题，撰写一篇短评。（7分）

<!-- block:445 type:paragraph style:Normal -->
【为什么能想到】 近百个国家、地区和国际组织同中方签署倡议合作文件、携手谋发展，众多主体愿聚到一起是因发展需求彼此契合，正对应国家间共同利益是国家合作的基础。

<!-- block:446 type:paragraph style:Normal -->
【答案落点】 全球发展倡议契合全人类共同利益，共同利益是国家合作的基础，近百个国家同中方签署合作文件、携手共谋发展。

<!-- block:447 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:448 type:paragraph style:Normal -->
· 答题层次：本题7分，按短评答题层次组织

<!-- block:449 type:paragraph style:Normal -->
· 逻辑分层（1分）：分清“背景及原因”和“具体举措及其积极影响”，通过分段呈现

<!-- block:450 type:paragraph style:Normal -->
· 背景及原因/意义（3分）：必要性知识1分，可写时代主题、经济全球化/世界多极化、共同利益等；重要性知识1分，可写推动国际秩序朝更加公正合理方向发展、推动经济全球化朝开放包容普惠平衡共赢方向发展、增强发展中国家话语权和国际地位等任意一点；结合材料论述1分

<!-- block:451 type:paragraph style:Normal -->
· 具体举措（3分）：共商共建共享、完善全球治理、践行多边主义、践行正确义利观、坚持《联合国宪章》宗旨和原则等任意两点给2分；结合材料论述1分

<!-- block:452 type:paragraph style:Normal -->
· 答题提醒：只写“人类命运共同体”且不关联其他发展知识，得1分；罗列知识、缺乏论述，最多3分

## Q0037 doc_order=37 blocks=453-461
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2024西城二模Q19中国答案的国际关系新思路
- question_ref: 2024西城二模Q19
- duplicate_group_id: UQ0027
- duplicate_group_doc_orders: 5;37;260;333;360;378;458
- duplicate_group_core_points: 中国推动构建人类命运共同体;和平与发展仍是时代主题;国家间共同利益是国家合作的基础;推动国际关系民主化;推动构建人类命运共同体;相互尊重、公平正义、合作共赢的新型国际关系;践行真正的多边主义

<!-- block:453 type:paragraph style:Normal -->
11. 2024西城二模Q19中国答案的国际关系新思路

<!-- block:454 type:paragraph style:Normal -->
【材料触发点】 题面把恃强凌弱、零和博弈、结盟对抗作为旧国际关系的问题，需要把中国答案放回当今世界主题之下，说明它顺应而非违背和平与发展的时代潮流。

<!-- block:455 type:paragraph style:Normal -->
【设问】 结合材料，阐述中国答案所体现的处理国际关系的新思路。

<!-- block:456 type:paragraph style:Normal -->
【为什么能想到】 题面批判恃强凌弱、零和博弈，中国答案转向利益交汇和命运交织，所以先抓国家间共同利益。

<!-- block:457 type:paragraph style:Normal -->
【答案落点】 全人类是命运与共的大家庭，国与国之间利益交汇、命运交织、休戚与共，共同利益是处理国际关系合作共赢的基础。

<!-- block:458 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:459 type:paragraph style:Normal -->
· 答题层次：本题5分，1分总判断，4分任取二点

<!-- block:460 type:paragraph style:Normal -->
· 总判断（1分）：全人类是一个命运与共的大家庭，国与国之间利益交汇、命运交织、休戚与共；也可用和平与发展作时代背景替代

<!-- block:461 type:paragraph style:Normal -->
· 新思路层（4分，以下任取二点，每点2分）：人类命运共同体理念超越集团政治的“小圈子”规则；超越实力至上的逻辑；超越少数国家定义“普世价值”的垄断；顺应时代潮流，倡导全球协作，推动国际秩序朝着更加公正合理的方向发展。正面解释可展开为赋予发展中国家更多发言权、推动国际关系民主化、坚持真正的多边主义、完善全球治理等

## Q0038 doc_order=38 blocks=462-473
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2025延庆一模Q20(2)外交部发言人回应"脱钩断链"
- question_ref: 2025延庆一模Q20
- duplicate_group_id: UQ0019
- duplicate_group_doc_orders: 4;38;65;222;330;361;379;530
- duplicate_group_core_points: 和平与发展仍是时代主题;国家间共同利益是国家合作的基础;展现大国责任担当;推动国际关系民主化;推动构建人类命运共同体;维护全球产业链供应链稳定畅通;维护国家利益是主权国家对外活动的出发点和落脚点;践行真正的多边主义

<!-- block:462 type:paragraph style:Normal -->
12. 2025延庆一模Q20(2)外交部发言人回应"脱钩断链"

<!-- block:463 type:paragraph style:Normal -->
【材料触发点】 材料二中个别国家鼓噪"脱钩断链"和供应链"去风险"，与近70个国家和地区企业到链博会寻找"链"通中外方案形成对照；要论证供应链合作的正当性，必须用时代主题判定"合作"才是符合潮流的方向，"脱钩"违背潮流。

<!-- block:464 type:paragraph style:Normal -->
【设问】 假如你是外交部发言人，请结合材料二，运用《当代国际政治与经济》知识，对上述提问做出回应。

<!-- block:465 type:paragraph style:Normal -->
【为什么能想到】 外交部回应“脱钩断链”，材料一方面呈现链博会吸引70个国家参与，另一方面呈现“去风险”实为阻断合作。题目要求回应为什么维护产供链稳定符合各方利益，就要抓共同利益：各国在产供链安全、市场联通、发展机会上的共同需求，是反对脱钩断链、深化合作的基础。

<!-- block:466 type:paragraph style:Normal -->
【答案落点】 维护全球产供链韧性和稳定符合国际社会的共同利益，共同利益是国家合作的基础，各国应深化产供链合作共识。

<!-- block:467 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:468 type:paragraph style:Normal -->
· 答题层次：本题8分，四个角度，每角度2分。

<!-- block:469 type:paragraph style:Normal -->
· 时代主题：维护全球产供链韧性和稳定，是推动世界经济可持续发展的重要保障，符合国际社会共同利益，顺应和平与发展的时代主题。

<!-- block:470 type:paragraph style:Normal -->
· 经济全球化方向：中国坚持高质量发展和高水平对外开放，反对“脱钩断链”，推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展。

<!-- block:471 type:paragraph style:Normal -->
· 世界多极化：世界多极化是当今国际形势的突出特点，“脱钩断链”损人不利己；中国在追求本国利益的同时兼顾他国合理关切，推动各国深化产供链合作、共建“世界共赢链”。

<!-- block:472 type:paragraph style:Normal -->
· 人类命运共同体：中国愿同各国携手维护全球产业链供应链稳定畅通，凝聚合作共识，共筑人类命运共同体。

<!-- block:473 type:paragraph style:Normal -->
· 可替代提醒：国家利益、国际关系、多边主义等角度可替代作答，但与前面角度意思重复时不重复计算。

## Q0039 doc_order=39 blocks=474-485
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2026朝阳期末Q20
- question_ref: 2026朝阳期末Q20
- duplicate_group_id: UQ0008
- duplicate_group_doc_orders: 8;39;58;68;138;246;311;342;389;399;459;540
- duplicate_group_core_points: 世界多极化与全球南方联合自强;世界多极化是当今国际形势的突出特点;中国推动构建人类命运共同体;习近平外交思想指导中国特色大国外交（外交为民、服务中国式现代化）;共享经济全球化成果，促进世界经济共同繁荣;和平与发展仍是时代主题;国家间共同利益是国家合作的基础;建设开放型世界经济，扩大开放合作;推动国际秩序和全球治理体系更加公正合理;推动构建人类命运共同体;维护国家利益是主权国家对外活动的出发点和落脚点;顺应经济全球化趋势，反对贸易保护主义

<!-- block:474 type:paragraph style:Normal -->
13. 2026朝阳期末Q20

<!-- block:475 type:paragraph style:Normal -->
【材料触发点】 题目指向分析中国特色大国外交更有作为的必要性，材料呈现“构建周边命运共同体—妥善管控矛盾分歧—让人民远离冲突和战争—共建安宁家园—培育战略互信”的关系链，要求从时代主题和中国外交的共同体目标说明主动作为的理由。

<!-- block:476 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，分析中国特色大国外交为什么要更有作为。

<!-- block:477 type:paragraph style:Normal -->
【为什么能想到】 材料讲周边命运共同体、管控分歧和战略互信，说明中国作为建立在共同利益和共同安全上。

<!-- block:478 type:paragraph style:Normal -->
【答案落点】 国家间共同利益是国家合作的基础，中国更有作为正是顺应各国共谋发展的共同利益，为世界发展大局贡献力量。

<!-- block:479 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:480 type:paragraph style:Normal -->
· 本题8分，按四个角度组织，每个角度都写成“背景+目标”。

<!-- block:481 type:paragraph style:Normal -->
· 可先总起：中国特色大国外交主动作为，是顺应世界发展大势、服务国家发展大局的必然选择；后面角度不够完整时，这句可帮助兜住1分。

<!-- block:482 type:paragraph style:Normal -->
· 和平发展角度：和平与发展是当今时代主题；再结合材料说明推动人类命运共同体、维护共同利益、推动国际新秩序或完善全球治理。

<!-- block:483 type:paragraph style:Normal -->
· 国际政治角度：可写世界多极化深入发展，也可写单边主义、霸权主义和强权政治仍然存在；再结合材料说明提升发展中国家代表性和话语权、维护发展中国家利益或推动全球南方联合自强。

<!-- block:484 type:paragraph style:Normal -->
· 国际经济角度：可写经济全球化深入发展，也可写贸易保护主义带来挑战；再结合材料说明推动开放型世界经济、世界经济共同繁荣、互利共享、开放合作或共享发展成果。

<!-- block:485 type:paragraph style:Normal -->
· 国家利益角度：可写维护主权、安全、发展利益，或国家利益是国际关系的决定性因素，或维护国家利益是主权国家对外活动的出发点和落脚点；再结合材料说明维护人民利益、服务中国式现代化。

## Q0040 doc_order=40 blocks=488-498
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2026朝阳二模Q20(2)
- question_ref: 2026朝阳二模Q20
- duplicate_group_id: UQ0070
- duplicate_group_doc_orders: 40;274;438
- duplicate_group_core_points: 国家间共同利益是国家合作的基础;在平等互利基础上开展合作，实现互利共赢;贡献中国智慧、中国方案、中国力量

<!-- block:488 type:paragraph style:Normal -->
14. 2026朝阳二模Q20(2)

<!-- block:489 type:paragraph style:Normal -->
【材料触发点】 材料说人类命运共同体理念在民族国家之上强调全人类立场，推动各国在兼顾全人类共同利益的前提下维护自身主权和发展。

<!-- block:490 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，分析人类命运共同体理念为什么能维护世界和平与发展。

<!-- block:491 type:paragraph style:Normal -->
【为什么能想到】 材料说该理念在民族国家之上强调全人类立场、兼顾共同利益再护主权；之所以各国愿同行，是因有共同利益的交汇，故用国家间共同利益是国家合作的基础来解。

<!-- block:492 type:paragraph style:Normal -->
【答案落点】 人类命运共同体理念超越民族国家本位，在尊重国家主权的前提下强调全人类立场，维护全人类共同利益，为协调国家利益与全球共同利益提供价值指引。

<!-- block:493 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:494 type:paragraph style:Normal -->
· 答题层次：本题6分，按三个角度组织；每个角度2分，知识1分、结合材料1分。

<!-- block:495 type:paragraph style:Normal -->
· 角度一：符合共同利益和时代主题（2分）。可写人类命运共同体理念超越民族国家本位，维护全人类共同利益，顺应和平与发展；时代主题可作替代表达。

<!-- block:496 type:paragraph style:Normal -->
· 角度二：倡导合作共赢、坚持多边主义、共商共建共享（2分）。可写摒弃零和博弈，推动各方合作应对全球性问题。

<!-- block:497 type:paragraph style:Normal -->
· 角度三：提供中国方案，推动国际新秩序或新型国际关系（2分）。可写：解决全球性问题提供中国方案，推动国际关系更加公正合理。

<!-- block:498 type:paragraph style:Normal -->
· 答题提醒：每个角度都要把知识和材料对应起来，不能只罗列术语。

