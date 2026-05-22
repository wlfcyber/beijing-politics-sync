# GPT-5.5 Pro 与 Claude Opus 开放观察交叉验证

## 输入状态

- GPT official v3 output: `06_open_observations/gpt55pro_open_observations.md`，解析 32 条 observation。
- Claude official v3 output: `06_open_observations/claude_opus_open_observations.md`，解析 29 条 observation。
- 共同输入包: `reasoner_packet_v3_corrected_missing17_20260519.zip`，70 题，65 formal，5 reference_only，0 missing。
- 本表仍不是代码本；只决定观察层面的 keep / merge / split / discard / pending。

## 统计

- match_type `claude_only`: 11
- match_type `gpt_only`: 10
- match_type `same`: 8
- match_type `similar`: 22
- decision `discard`: 14
- decision `keep`: 4
- decision `merge`: 13
- decision `pending`: 18
- decision `split`: 2
- strong_shared_observations: 17
- observations_needing_source_check: 18

## 强共享观察

- `CV001` GPT `S01` × Claude `OBS_S10`: merge。GPT聚焦好意同乘单题，Claude抽象为法理依据与现实意义分层。 共同题号: 无直接交集，按语义与证据簇合并。
- `CV002` GPT `S01` × Claude `OBS_S06`: merge。GPT强调现实意义必须由规则推出，Claude抽象为个案权益、秩序、价值三层。 共同题号: 无直接交集，按语义与证据簇合并。
- `CV004` GPT `S03` × Claude `OBS_S13`: merge。双方均发现劳动合同解除题要先判劳动者义务与用人单位合法解除。 共同题号: CC0119_2025_丰台_期末_19 ; CC0213_2025_门头沟_一模_20 ; CC0214_2025_门头沟_一模_20_2。
- `CV006` GPT `S05` × Claude `OBS_S03`: merge。GPT合同成立/效力/履行层次，与Claude法律定性入口相近。 共同题号: CC0244_2026_东城_期中_18。
- `CV007` GPT `S05` × Claude `OBS_S15`: merge。GPT强调合同层次不能混，Claude强调复合问题先拆多个法律问题。 共同题号: CC0143_2025_朝阳_一模_19。
- `CV008` GPT `S06` × Claude `OBS_S12`: merge。GPT消费者欺诈/惩罚性赔偿与Claude知识产权/消费欺诈/惩罚性赔偿题源簇重合。 共同题号: CC0063_2024_西城_二模_16 ; CC0143_2025_朝阳_一模_19 ; CC0305_2026_海淀_一模_18。
- `CV009` GPT `S07` × Claude `OBS_S01`: keep。双方都把法律名称、权利名称、主体能力术语精度视为显性得分线。 共同题号: CC0084_2025_东城_二模_19。
- `CV010` GPT `S07` × Claude `OBS_S04`: merge。GPT人格权/未成年人术语敏感，Claude抽象为主体身份精度独立计分。 共同题号: CC0084_2025_东城_二模_19。
- `CV011` GPT `S08` × Claude `OBS_S03`: merge。双方都强调违约、侵权、无过错/过错推定等路径定性不能混。 共同题号: CC0084_2025_东城_二模_19 ; CC0244_2026_东城_期中_18 ; CC0254_2026_丰台_二模_18。
- `CV012` GPT `S08` × Claude `OBS_S07`: merge。GPT程序路径不可泛维权，Claude具体化为救济方式/责任方式必须具体。 共同题号: 无直接交集，按语义与证据簇合并。
- `CV013` GPT `S08` × Claude `OBS_S15`: merge。GPT区分违约侵权/程序路径，Claude指出复合题先分诉讼请求和法律问题。 共同题号: CC0084_2025_东城_二模_19。
- `CV014` GPT `S09` × Claude `OBS_S12`: merge。双方均发现知识产权/创新题须先写权利类型、侵权/保护，再接创新价值。 共同题号: CC0103_2025_丰台_一模_19 ; CC0131_2025_房山_一模_19 ; CC0283_2026_朝阳_一模_18。
- `CV015` GPT `S10` × Claude `OBS_S12`: merge。GPT不正当竞争最小判断与Claude商业诋毁/技术秘密/市场秩序簇重合。 共同题号: CC0131_2025_房山_一模_19 ; CC0238_2026_东城_二模_19。
- `CV016` GPT `S11` × Claude `OBS_S07`: keep。双方都反对泛列协商调解仲裁诉讼，要求按材料写具体救济/程序行为。 共同题号: CC0245_2026_东城_期中_18_2。
- `CV018` GPT `S12` × Claude `OBS_S14`: keep。双方均发现相邻关系/权利边界题必须回到民法典相邻关系原则和具体边界。 共同题号: CC0223_2025_顺义_一模_19 ; CC0364_2026_通州_期中_19_1。
- `CV019` GPT `S12` × Claude `OBS_S05`: merge。GPT绿色/相邻关系后接价值，Claude指出民法基本原则是知识-价值桥。 共同题号: CC0011_2024_丰台_二模_17 ; CC0223_2025_顺义_一模_19 ; CC0364_2026_通州_期中_19_1。
- `CV020` GPT `S13` × Claude `OBS_S09`: keep。双方均发现材料原文必须转译为法律语言；抄材料或堆教材被限分。 共同题号: CC0084_2025_东城_二模_19 ; CC0143_2025_朝阳_一模_19。

## 需回源或暂存

- `CV017` S11 × OBS_S11: pending。Claude自标需更多题验证，保留但不作核心。
- `CV021` S14 × OBS_S10: pending。设问类型观察过宽，需要在代码本中拆成题型小代码。
- `CV022` C01 × OBS_C01: pending。必须回源核查；核查前不得作强证据。
- `CV023` C03 × OBS_W04: pending。跨模块题需题号/小问拆分后再用。
- `CV024` C04 × OBS_F05: pending。需要模块归属复核。
- `CV028` V02 × OBS_S04: pending。可作为代码本候选，但需避免把所有身份差异合并得过宽。
- `CV029` V03 × OBS_S07: pending。程序路径可候选，具体触发边界需再压测。
- `CV030` V03 × OBS_S11: pending。任选其一型仍需更多题验证。
- `CV039` V01 × —: pending。GPT-only weak/validation/do-not-promote observation; cannot support core code alone.
- `CV040` V04 × —: pending。GPT-only weak/validation/do-not-promote observation; cannot support core code alone.
- `CV041` — × OBS_S02: pending。Claude-only strong observation with formal evidence; store for next validation but do not enter core codebook alone.
- `CV042` — × OBS_S08: pending。Claude-only strong observation with formal evidence; store for next validation but do not enter core codebook alone.
- `CV043` — × OBS_W01: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.
- `CV044` — × OBS_W02: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.
- `CV045` — × OBS_W03: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.
- `CV046` — × OBS_W05: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.
- `CV047` — × OBS_C02: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.
- `CV048` — × OBS_C03: pending。Claude-only weak/conflict observation; keep for source check or next validation, not core codebook.

## 禁止事项

- `reference_only` 观察不能单独支撑核心 code。
- 冲突题号 CC0001、CC0094、CC0363/CC0364、CC0373、CC0305 等必须先回源或小问拆分。
- 本轮交叉验证仍不输出框架。
