# Batch24 Source Transcription - 2025海淀期中

Status: `SOURCE_REVIEWED_BATCH24`

## Source Files

- suite bundle: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2025各区模拟题__2025各区期末__2025海淀期中.md`
- rubric/answer source: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\7bbd92bd3b93e531_2025海淀期中细则.md`
- teacher-version paper: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\b452d8b4e21b94be_2024北京海淀高三_上_期中政治_教师版.md`
- raw rubric: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区期末\2025海淀期中\细则\2025海淀期中细则.docx`
- raw teacher paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区期末\2025海淀期中\试卷\2024北京海淀高三（上）期中政治（教师版）.pdf`

## Source Facts

- Answer key: `1C 2A 3C 4D 5B 6A 7B 8D 9D 10A 11B 12B 13A 14C 15D`.
- The scoring source is a DOCX answer/rubric file with direct text extraction.
- Current DOCX had `0` existing `2025海淀期中` mentions before Batch24 registration, so no inherited philosophy-body entry existed to register.
- Q16(1), Q16(2), Q17, and Q20 are 《经济与社会》 or economic/global-economy questions.
- Q18 and Q19 are 《政治与法治》 questions.
- Q21(1) is a legal/fazhi question; wording about “符合国情和实际、符合社会发展的需求” is a good-law evaluation standard, not a philosophy scoring point.
- Q21(2) is 《当代国际政治与经济》.
- Choice questions Q1-Q15 are economics, politics/law, national-security, international-politics, or public-governance rows; none has a rubric-supported 必修四 philosophy body placement.

## Boundary Rows

- Q1: 经济与社会选择题 -> 国有企业/民营企业/商业航天产业链
- Q2: 经济与社会选择题 -> 市场需求/差异化产品/消费者性价比
- Q3: 经济与社会选择题 -> 二次元经济/消费新空间
- Q4: 经济与社会选择题 -> 市场准入制度/非公有制经济
- Q5: 经济与社会选择题 -> 医保个人账户/社会保障
- Q6: 经济与社会选择题 -> 养老助餐/民营企业/公共服务供给
- Q7: 政治与法治选择题 -> 党建引领/党员先锋模范作用/社会治理
- Q8: 政治与法治选择题 -> 全国人大常委会执法检查/人大监督
- Q9: 政治与法治/民族政策选择题 -> 对口支援西藏/民族团结/生存权发展权
- Q10: 政治与法治/法律规范选择题 -> 网络暴力治理/多方主体/特殊群体权益
- Q11: 政治与法治选择题 -> 基层治理法治化/协商民主
- Q12: 政治与法治选择题 -> 总体国家安全观/国家安全利益
- Q13: 当代国际政治与经济选择题 -> 入境游/公共外交/经济动能
- Q14: 当代国际政治与经济选择题 -> 中国特色大国外交/人类命运共同体/一个中国原则
- Q15: 当代国际政治与经济选择题 -> APEC能源合作/国际能源合作
- Q16(1): 经济与社会主观题 -> 咖啡市场前景/生产技术/产品质量/消费方式/市场需求
- Q16(2): 经济与社会/当代国际经济主观题 -> 企业出海/经营战略/海外市场/经济全球化/全球治理
- Q17: 经济与社会主观题 -> 瞪羚企业/财政补贴/税收优惠/融资支持/人才引进
- Q18: 政治与法治主观题 -> 基层民主/党的领导/基层群众自治/协商共治
- Q19: 政治与法治主观题 -> 党纪处分条例/全面从严治党/党内法规/依法治国
- Q20: 经济与社会主观题 -> 粮食产销区省际横向利益补偿/共同富裕/粮食安全/区域协调发展
- Q21(1): 法律与生活/法治知识主观题 -> 婚姻法/民法典/良法之治/权利义务相对应
- Q21(2): 当代国际政治与经济主观题 -> 新中国外交的变与不变/外交思想/独立自主和平外交政策

## Guardrail

- No DOCX body insertion was made.
- No ordinary reference answer is treated as a philosophy scoring rubric.
- Political, economic, legal, and international-politics concepts are not converted into philosophy nodes merely because words like “实际”, “发展”, “创新”, or “公平正义” appear.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
