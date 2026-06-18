你是本项目的真实 ClaudeCode 复核线。使用模型目标 claude-opus-4-8，effort=max。

本次只复核 slice 009: doc_order 41-45。不要声称全书完成，不改写任何源文件。

硬规则摘要：
- 当前桌面文档字段是【材料触发点】【设问】【为什么能想到】【答案落点】【同题组】，缺独立“术语”和“细则位置”通常是结构风险。
- 普通参考答案不能冒充评分细则；没有正式评分细则/评标/阅卷总结/用户确认评分材料时，写 LOW_EVIDENCE 或 BLOCKED。
- 每条检查：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。
- 尤其注意：2024海淀二模Q18(1) 是否为8分时政述评等级题且“共同利益”不是固定得分层；2026西城期末Q20 是否有“是什么2/为什么3/效果3”的正式细则且共同利益只在为什么层一类中；2026通州一模Q19 是否是措施或知识4分+材料作用4分，不能把共同利益写成全题唯一答案；2025朝阳二模Q21 是否为中国发展需要3+区域发展需要3+世界发展需要2，且共同利益在区域发展需要层；2026房山二模Q20 是否为六个方向各1分+材料结合2分，且共同利益/共同发展只是其中一方向。

请直接输出下面 markdown，不要调用工具，不要写额外解释：

# ClaudeCode Slice 009 Findings

- model_used: claude-opus-4-8
- effort: max
- scope: doc_order 41-45 only
- source_docx_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e

## Findings

| doc_order | entry_id | question_ref | status | problem | evidence_pointer | suggested_fix |
|---:|---|---|---|---|---|---|

status 只用 PASS、LOW_EVIDENCE、NEEDS_FIX、BLOCKED。
表格后追加“## 源证据边界”，说明你的判断主要基于 slice 输入可见文本，仍需 Codex 回原卷/细则确认的部分。

下面是 slice 输入：

# ClaudeCode Slice 009 Input

source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
scope: document-order question entries 41-45 only; do not claim full-book completion.

## Q0041 doc_order=41 blocks=503-512
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2024海淀二模Q18(1)多极化世界中的民主与全球治理
- question_ref: 2024海淀二模Q18
- duplicate_group_id: UQ0025
- duplicate_group_doc_orders: 3;23;41;300;329;383;397
- duplicate_group_core_points: 世界多极化是当今国际形势的突出特点;共商共建共享的全球治理观;和平与发展仍是时代主题;国家间共同利益是国家合作的基础;推动国际关系民主化;推动构建人类命运共同体;霸权主义和强权政治、单边主义是和平与发展的现实挑战

<!-- block:503 type:paragraph style:Normal -->
15. 2024海淀二模Q18(1)多极化世界中的民主与全球治理

<!-- block:504 type:paragraph style:Normal -->
【材料触发点】 资料包呈现全球南方国家崛起、金砖国家等机制作用增强，以及人工智能、大数据带来的共同治理难题；各国之所以需要围绕民主与全球治理展开互鉴和协作，是因为在提升全球治理代表性、弥合技术治理缺口上存在共同利益。

<!-- block:505 type:paragraph style:Normal -->
【设问】 任选一个议题，参考资料包中的内容，运用《当代国际政治与经济》知识，围绕所选的议题写一篇时政述评。（8分）要求：观点明确；知识运用准确；论述合乎逻辑，条理清晰。

<!-- block:506 type:paragraph style:Normal -->
【为什么能想到】 题目要求围绕“多极化世界中的民主与全球治理”写时政述评，资料包把全球南方发声、国际组织作用增强和人工智能治理缺口放在一起，说明全球治理不是单个国家能独自完成的事务。回答各国为什么能够通过论坛和国际机制共同推动治理改革时，应先写国家间共同利益是国家合作的基础，再接到各方围绕共同挑战推动全球治理民主化。

<!-- block:507 type:paragraph style:Normal -->
【答案落点】 国家间共同利益是国家合作的基础，人工智能治理缺口、全球南方代表性不足等共同挑战，使各国需要依托国际组织和合作机制推动全球治理更加民主、有效。

<!-- block:508 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:509 type:paragraph style:Normal -->
· 答题层次：本题8分，时政述评等级题；原题没有把共同利益单列为固定得分层。

<!-- block:510 type:paragraph style:Normal -->
· 可用角度：可从时代主题、世界多极化、人类命运共同体、国际组织等角度作答。

<!-- block:511 type:paragraph style:Normal -->
· 定档要求：观点明确；知识运用准确；论述合乎逻辑、条理清晰。高档要紧扣所选议题综合展开；低档多为观点不明、罗列知识、知识错误、重复题干或无效作答。

<!-- block:512 type:paragraph style:Normal -->
· 迁移提醒：共同利益可以作为解释合作必要性的迁移语言，但不能替代原题明确列出的角度，也不能冒充单独固定分值。

## Q0042 doc_order=42 blocks=515-524
- bucket: 理论
- sub_bucket: 合作
- core_point: 国家间共同利益是国家合作的基础
- question_title: 2026西城期末Q20参与全球气候治理中的中国实践
- question_ref: 2026西城期末Q20
- duplicate_group_id: UQ0042
- duplicate_group_doc_orders: 22;42;348;368;494;556
- duplicate_group_core_points: 和平与发展仍是时代主题;国家间共同利益是国家合作的基础;坚定维护以联合国为核心的国际体系和以国际法为基础的国际秩序;坚持正确义利观;推动构建人类命运共同体;践行真正的多边主义

<!-- block:515 type:paragraph style:Normal -->
16. 2026西城期末Q20参与全球气候治理中的中国实践

<!-- block:516 type:paragraph style:Normal -->
【材料触发点】 答题要求角度2将“共同利益”单列为1分，材料中全球气候治理、可持续发展、清洁世界都指向各国共同利益。

<!-- block:517 type:paragraph style:Normal -->
【设问】 结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。

<!-- block:518 type:paragraph style:Normal -->
【为什么能想到】 看到答题要求把共同利益单列，就不能只用大国担当或中国方案概括。气候变化影响所有国家，中国参与全球气候治理的合作基础正在于各国维护生态安全和可持续发展的共同利益。

<!-- block:519 type:paragraph style:Normal -->
【答案落点】 国家间共同利益是国家合作的基础。应对气候变化、促进全球可持续发展符合各国共同利益，中国参与全球气候治理有利于推动国际合作。

<!-- block:520 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:521 type:paragraph style:Normal -->
· 本题8分，按“是什么—为什么—效果”三层写。

<!-- block:522 type:paragraph style:Normal -->
· 是什么2分：先说中国在全球气候治理中是建设者、引领者或负责任大国；再结合材料概括具体做法，如坚持绿色发展、新发展理念，发挥有为政府和有效市场作用。

<!-- block:523 type:paragraph style:Normal -->
· 为什么3分：从四类中写满三类即可：全球气候治理挑战或完善全球治理体系；世界各国共同利益；中国理念，如人类命运共同体、全人类共同价值、正确义利观、共商共建共享、真正的多边主义、互利共赢；自觉履行国际义务、遵循国际法、承担国际责任。

<!-- block:524 type:paragraph style:Normal -->
· 效果3分：对世界写两层，一是促进全球可持续发展或建设清洁世界，二是维护联合国核心作用或完善全球治理体系；对中国写一层，即贡献中国智慧或中国力量。

## Q0043 doc_order=43 blocks=526-534
- bucket: 理论
- sub_bucket: 合作
- core_point: 共同利益是合作的基础
- question_title: 2026通州一模Q19
- question_ref: 2026通州一模Q19
- duplicate_group_id: UQ0043
- duplicate_group_doc_orders: 21;43;265;387;422;558
- duplicate_group_core_points: 中国特色大国外交与人类命运共同体;共同利益是合作的基础;和平与发展仍是时代主题;国际关系民主化与国际政治经济新秩序;相互尊重、公平正义、合作共赢的新型国际关系;遵循联合国宪章宗旨和原则

<!-- block:526 type:paragraph style:Normal -->
1. 2026通州一模Q19

<!-- block:527 type:paragraph style:Normal -->
【材料触发点】 材料既有中俄关系稳定定位，也有中美关系穿越风浪、周边睦邻友好和全球南方合作，说明不同国家之间存在可以通过合作实现的共同利益。

<!-- block:528 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，分析中国元首外交如何为世界注入稳定性与正能量。（8分）

<!-- block:529 type:paragraph style:Normal -->
【为什么能想到】 题目问“如何注入稳定性与正能量”，不能只写中国单方面努力；多组双边和多边镜头共同出现，提示答案要抓国家间共同利益，通过扩大合作基础来解释稳定来源。

<!-- block:530 type:paragraph style:Normal -->
【答案落点】 中国元首外交立足各方共同利益，推动大国关系平稳前行、周边关系睦邻友好、全球南方团结合作，从而为国际关系稳定提供合作基础。

<!-- block:531 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:532 type:paragraph style:Normal -->
· 答题层次：本题8分，措施或知识4分，材料分析且必须答作用4分，落点指向为世界注入稳定性与正能量

<!-- block:533 type:paragraph style:Normal -->
· 可采知识：和平与发展时代主题、共同利益是合作的基础、兼顾他国合理关切、维护多边贸易体制、推动经济全球化朝开放包容普惠平衡共赢方向发展、坚持正确义利观、推动国际关系民主化和国际政治经济新秩序、共商共建共享全球治理观、推动构建人类命运共同体、中国特色大国外交

<!-- block:534 type:paragraph style:Normal -->
· 作答提醒：不能只罗列知识；每个知识点都要接材料中元首外交的合作、治理、开放或和平作用，说明如何形成稳定性和正能量

## Q0044 doc_order=44 blocks=537-547
- bucket: 理论
- sub_bucket: 合作
- core_point: 共同利益是合作的基础
- question_title: 2025朝阳二模Q21（周边工作新局面）
- question_ref: 2025朝阳二模Q21
- duplicate_group_id: UQ0103
- duplicate_group_doc_orders: 44
- duplicate_group_core_points: 共同利益是合作的基础

<!-- block:537 type:paragraph style:Normal -->
2. 2025朝阳二模Q21（周边工作新局面）

<!-- block:538 type:paragraph style:Normal -->
【材料触发点】 题目要求说明我国为什么要努力开创周边工作新局面，材料呈现中国与周边国家在发展、安全、互联互通等方面互相需要，必须先点明共同利益是合作基础。

<!-- block:539 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。

<!-- block:540 type:paragraph style:Normal -->
【为什么能想到】 材料写周边国家合作、互联互通、安全发展和区域联动，不是单边施惠，而是共同利益驱动的区域合作。题目问“为什么要努力开创”，需要解释中国开展周边工作的现实依据，而不是只写中国外交口号。先说明中国与周边国家存在广泛共同利益，再接到和平发展、经济融合、国际关系民主化和人类命运共同体。

<!-- block:541 type:paragraph style:Normal -->
【答案落点】 共同的国家利益是国际合作的基础，中国与周边国家在发展、安全、互联互通等领域有广泛共同利益，这是我国努力开创周边工作新局面的客观依据。

<!-- block:542 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:543 type:paragraph style:Normal -->
· 答题层次：本题8分，按“中国的发展需要—区域的发展需要—世界的发展需要”三层组织；同一关键词不重复，语言要有层次、无知识错误

<!-- block:544 type:paragraph style:Normal -->
· 从中国的发展需要角度看（3分）：必要性1分，可写周边国家众多、符合我国与周边国家地理环境和文化发展状况、国际形势出现深刻变化；重要性任意两点2分，可写实现发展繁荣的重要基础、提高开放型经济水平、维护国家安全、为国家发展创造良好外部环境、运筹外交全局、推动构建人类命运共同体

<!-- block:545 type:paragraph style:Normal -->
· 从区域的发展需要角度看（3分）：共同的国家利益是国际合作基础，中国与周边国家有广泛共同利益，或写我国坚持独立自主的和平外交政策、维护世界和平、促进共同发展，任意一点1分；与周边国家开展贸易，促进经济融合和共同发展、促进区域经济一体化、促进区域贸易和投资自由化便利化，任意一点1分；创新区域合作机制、搭建合作平台，维护地区和平稳定或区域安全，推动构建周边国家命运共同体，任意一点1分

<!-- block:546 type:paragraph style:Normal -->
· 从世界的发展需要角度看（2分）：携手周边国家推动建设以合作共赢为核心的新型国际关系、推动国际关系民主化、实现真正的多边主义、推动全球治理变革，任意一点1分；通过区域经济合作维护和推动全球自由贸易、多边贸易，或推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展，任意一点1分

<!-- block:547 type:paragraph style:Normal -->
· 答题提醒：同一个关键词不重复计分；整体语言要有层次、有问题意识，不能把知识点机械堆在一起

## Q0045 doc_order=45 blocks=550-563
- bucket: 理论
- sub_bucket: 合作
- core_point: 共同利益是合作的基础
- question_title: 2026房山二模Q20
- question_ref: 2026房山二模Q20
- duplicate_group_id: UQ0050
- duplicate_group_doc_orders: 45;122;240;297;493
- duplicate_group_core_points: 共同利益是合作的基础;共商共建共享的全球治理观;坚持正确义利观;推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展;数据要素在全球范围内流动

<!-- block:550 type:paragraph style:Normal -->
3. 2026房山二模Q20

<!-- block:551 type:paragraph style:Normal -->
【材料触发点】 技术联合研发、标准对接互认和弥合数据鸿沟，体现多方围绕数字发展需求形成合作基础。

<!-- block:552 type:paragraph style:Normal -->
【设问】 结合材料，运用《当代国际政治与经济》知识，分析世界数据组织完善全球数据治理，服务全球数字经济发展的智慧。

<!-- block:553 type:paragraph style:Normal -->
【为什么能想到】 材料把技术联合研发、标准对接互认、弥合数据鸿沟并列，都指向各方在数字发展上的共同需求；要答“智慧”，先点共同利益是合作的基础，安排才接得上共同发展。

<!-- block:554 type:paragraph style:Normal -->
【答案落点】 各方在数据发展和数字经济繁荣上存在共同利益，世界数据组织推动技术联合研发、标准对接互认和数据鸿沟弥合，有利于实现共同发展。

<!-- block:555 type:paragraph style:Normal -->
【同题组】 （按原题答题层次）

<!-- block:556 type:paragraph style:Normal -->
· 答题层次：本题8分，围绕世界数据组织完善全球数据治理、服务全球数字经济发展的中国智慧展开；六个方向各1分，材料结合2分。

<!-- block:557 type:paragraph style:Normal -->
· 治理方向一：普惠包容的经济全球化（1分）。

<!-- block:558 type:paragraph style:Normal -->
· 治理方向二：平等有序的世界多极化（1分）。

<!-- block:559 type:paragraph style:Normal -->
· 利益基础：共同利益或共同发展（1分）。

<!-- block:560 type:paragraph style:Normal -->
· 合作关系：合作共赢或互利共赢（1分）。

<!-- block:561 type:paragraph style:Normal -->
· 治理方式：共商共建共享、全球治理观或真正的多边主义（1分）。

<!-- block:562 type:paragraph style:Normal -->
· 数据流动：推动数据要素在全球范围内流动（1分）。

<!-- block:563 type:paragraph style:Normal -->
· 材料落点（2分）：结合世界数据组织弥合数据鸿沟、释放数据价值、繁荣数字经济展开；论述充分2分，论述一般1分。

