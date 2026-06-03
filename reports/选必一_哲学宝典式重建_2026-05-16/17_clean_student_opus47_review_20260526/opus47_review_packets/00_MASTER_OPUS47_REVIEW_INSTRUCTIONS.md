# Claude Opus 4.7 总审核指令

请作为真实 Claude Opus 4.7 Adaptive 外审，审核本目录中的选必一纯净学生版送审稿。

## 读取顺序

1. 先读 `PACKET_INDEX.md`。
2. 再按编号逐个读取 `*_CLAUDE_OPUS47_REVIEW_PACKET.md`。
3. 必要时对照 `../选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_纯净送审稿_20260526.md`，但不要重写整本。

## 审核边界

- 只判断这份纯净学生版是否已经去掉提醒、提示、边界、后台审核、模型名、本地路径、SHA、TODO/debug 等学生版污染。
- 同时检查是否误删核心内容：六大要素、核心答题点、题例、卷面句、同题组和末尾极简速记版是否仍可用。
- 不做个人审美重写，不要求恢复被删除的提示性包装。
- 对每个分块给出独立 verdict。

## 输出格式

OVERALL_VERDICT: ACCEPT / PATCH_REQUIRED / REJECT

PER_PACKET_VERDICTS:

- `01_时代背景_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `02_理论_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `03_经济全球化_part01_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `04_经济全球化_part02_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `05_政治多极化_part01_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `06_政治多极化_part02_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `07_中国_part01_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `08_中国_part02_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `09_联合国_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT
- `10_六大要素术语极简速记版_CLAUDE_OPUS47_REVIEW_PACKET.md`: ACCEPT / PATCH_REQUIRED / REJECT

P0:
- 若无，写“无”。

P1:
- 若无，写“无”。

P2:
- 若无，写“无”。

必须改的原句 => 建议句:
- 若无，写“无”。

最终一句话结论:
- 说明能否作为选必一纯净学生版继续进入最终 Word/PDF 生成。
