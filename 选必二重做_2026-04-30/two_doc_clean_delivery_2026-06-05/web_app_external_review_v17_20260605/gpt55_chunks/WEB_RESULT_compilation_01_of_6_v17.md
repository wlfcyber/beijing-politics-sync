# GPT-5.5 Pro Web Result - compilation-01

- reviewed_via: Chrome visible ChatGPT web session through CDP browser automation
- model_surface_seen: Pro / 进阶专业
- submitted_at: 2026-06-05T00:18:54.484Z
- prompt: `web_app_external_review_v17_20260605/gpt55_chunks/GPT55_CHUNK_PROMPT_compilation_01_of_6_v17.md`
- screenshot: `web_app_external_review_v17_20260605/gpt55_chunks/WEB_RESULT_compilation_01_of_6_v17.png`

## Extracted Result Tail

```text
compilation-01

verdict: FAIL

BLOCKING defects:

2024 · 丰台 · 二模 · 第17题材料明显串断：民法典引文写成“侵权人应当承担侵甲公司在生产中……”，后文“权责任。案例一……案例二”又被甩到 chunk 末尾，导致材料主体、案例一、案例二结构不完整；答案落点却引用“案例一”“案例二”，材料与答案无法对应。

2024 · 海淀 · 一模 · 第19题细则明显残缺并跨题外溢：细则中“层次1”后直接出现“层次法院依法判决……”，缺少层次2、层次3、层次4的完整结构；相关残片“2：乙公司构成侵权……层次3……层次4……”出现在西城条目之后，属于跨题串入。

chunk 末尾存在裸露代码围栏和无归属残片：在“2024 · 西城 · 一模 · 第18题第1问”答案落点后出现 ``` 以及海淀、丰台条目的游离内容，属于学生端结构噪声，会阻断交付。

NONBLOCKING issues:

2024 · 东城 · 一模 · 第19题材料中“李某 郭某出具欠据”疑似缺字，可能应为“李某向郭某出具欠据”，需按原卷核对。

2024 · 东城 · 二模 · 第19题第1问中，材料写乙公司回复“可以”，细则理由处写“乙公司回复‘好的’”，同一事实表述不一致，建议统一为原卷措辞。

2024 · 海淀 · 一模 · 第19题材料中资料卡插入正文，形成“科技公司”“虚拟数字人”句子被打断的线性化问题，虽不如细则残缺严重，但会影响学生阅读。

Required local verification:

Codex 需核对 v17 的学生端 DOCX/Markdown 是否真实包含末尾裸露代码围栏及游离残片；若存在，删除游离残片并把对应内容归回正确条目。

按原卷或原评分细则重建 2024 丰台二模第17题材料，特别是民法典引文、案例一、案例二的完整边界。

按原评分细则重建 2024 海淀一模第19题细则，恢复侵权、不正当竞争、意义层次，不要凭残片自行补写。

核对东城一模19“李某向郭某出具欠据”及东城二模19(1)“可以/好的”的原文。
```
