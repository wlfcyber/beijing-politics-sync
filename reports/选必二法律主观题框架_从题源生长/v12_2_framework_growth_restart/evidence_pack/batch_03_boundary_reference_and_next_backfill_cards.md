# Batch 03 Boundary Reference And Next-Backfill Cards

用途：让 GPT/Claude 判断开放容器、参考题、下一版候选是否暴露框架缺口；不得把它们直接硬塞进核心。

## 5 OPEN_OR_REFERENCE

- CC0040_2024_海淀_一模_19 | 问对判决的认识 | 仅参考，不支撑核心
- CC0162_2025_海淀_一模_18 | 问对判决的认识 | 仅参考，不支撑核心
- CC0311_2026_海淀_二模_18 | 问制度作用 | 仅参考，不支撑核心
- CC0353_2026_西城_期中_17 | 问判决是否正确 | 仅参考，不支撑核心
- CC0380_2026_顺义_二模_18_2 | 问法律风险与治理 | 仅参考，不支撑核心

## 6 next-backfill candidates

### CC0251_2026_丰台_一模_20
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/试卷/试卷.pdf 第9页图像|/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx 第51页
- question_found：结合材料，运用《法律与生活》知识，阐明人民法院作出该判决的法理依据和现实意义。
- material_found：郭某餐后离开，在餐厅外台阶区域低头看手机、不慎踩空摔倒并受伤；监控未见下雨、下雪、积雪、积水、冰冻等客观危险因素；郭某起诉餐饮公司和物业公司要求赔偿。
- rubric_found：细则PPT第51页：经营者安全保障义务应在合理限度内；证据表明事发现场不存在影响通行的客观因素；原告自身未尽安全注意义务；经营者无过错，不承担赔偿；判决平衡权利义务、明确安全保障义务边界。

### CC0276_2026_房山_二模_17
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL_WITH_BOUNDARY_REVIEW
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/试卷/2026北京房山高三二模政治（教师版）.pdf 第6页、第10页|/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/细则/26房山评标(2).docx
- question_found：中国走向世界，以负责任大国参与国际事务，必须善于运用法治。结合材料，运用法治知识，谈谈中国是如何加强涉外法治建设的。
- material_found：外国巨轮“尊重”案：青岛海事法院对船舶实施“活扣押”促成和解；出台外商投资法及实施条例保护内外资企业；线上多元纠纷解决平台；涉外海事纠纷调解机制。
- rubric_found：评标/答案页：完善涉外法律法规体系；创新涉外司法实践；多元纠纷解决平台；创新诉讼调解；以法治方式践行大国责任。

### CC0277_2026_房山_二模_18
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/试卷/2026北京房山高三二模政治（教师版）.pdf 第7页、第10页|/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026房山二模/细则/26房山评标(2).docx
- question_found：（1）结合材料一，运用《法律与生活》知识，分析上述场景可能涉及的法律边界，并提出应对措施。
- material_found：OPC“数字员工”场景：撰写行业文章生成某公司虚假负面数据；把公司核心代码、独家运营策略上传公共AI平台；设计国潮风手机壳图案并直接商业销售。
- rubric_found：评标/答案页：商业诋毁/名誉权、商业秘密泄露、著作权或外观设计侵权；应履行审核义务、完善保密措施、签订保密合同。

### CC0317_2026_海淀_期中_18
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL_WITH_ID_STAGE_REVIEW
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末/试卷/试卷.pdf 第6页、第9-10页
- question_found：（1）运用《法律与生活》知识，判断这一条款是否有效，并说明理由。
- material_found：住房租赁企业合同样本约定：合同期满后，承租人不得在企业不知情情况下与房屋产权人私下建立租赁关系，否则视为违约并支付一个月租金作为违约金；承租人不同意，企业称条款不能更改。
- rubric_found：答案页：该条款属于格式条款；提供格式条款一方应遵循公平原则；条款限制承租人自由订立合同的权利，应认定无效。

### CC0318_2026_海淀_期中_18_2
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL_WITH_ID_STAGE_REVIEW
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末/试卷/试卷.pdf 第6页、第9-10页
- question_found：（2）运用法治知识，分析《住房租赁条例》上述规定的现实意义。
- material_found：《住房租赁条例》规定国务院住房城乡建设主管部门会同市场监管部门制定并公布住房租赁合同、住房租赁经纪服务合同示范文本；县级以上政府部门加强行业诚信建设、信用评价、信用记录和分类监管。
- rubric_found：答案页：合同示范文本规范合同内容、防止格式条款滥用、保护租赁双方权益、减少纠纷；引导市场主体依法诚信；明确政府职责，推动市场监管和良法善治。

### CC0319_2026_海淀_期中_19
- source_hunt_result：FOUND_FOR_NEXT_BACKFILL_WITH_ID_STAGE_REVIEW
- next_action：进入下一版回填候选，不纳入v12.1正文
- checked_sources：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末/试卷/试卷.pdf 第7页、第10页
- question_found：运用《法律与生活》知识，谈谈对本案判决的认识。
- material_found：甲公司运营综合性票务平台；郑某通过网络店铺销售针对该售票应用程序的抢票软件；甲公司认为该软件规避平台购票规则、妨碍售票业务正常开展，起诉请求停止侵权、赔偿损失；法院认定构成不正当竞争并判赔。
- rubric_found：答案页：郑某利用技术手段提供不正当抢票优势，破坏平台购票规则，干扰售票业务，损害甲公司信誉和合法权益，构成不正当竞争并承担侵权责任。

