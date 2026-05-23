# 夜间线程登记表

| 线程 | 目标 | 当前定位 | 总管初判 | 写入范围 |
|---|---|---|---|---|
| 选必一 | 做成哲学宝典同级，覆盖全部考题 | `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23` | `RUNNING`，已有 ClaudeCode/Opus 相关材料，需确认全题覆盖、最终正文、Word/PDF 和治理闭环 | 本总管只写 `night_supervisor_2026-05-23/`，代理可写本目录下 `agents/xuanbiyi_*` |
| 必修四 | 把先前没有的题补进已认可哲学框架 | `reports/bixiu4_philosophy_*_2026-05-23` 与桌面 v7/v8 成品 | `CANDIDATE_DELIVERY_NEEDS_AUDIT`，已见 v7/v8、补题、审查包和剩余缺口文件，必须确认 old choice gaps 是否闭合 | 本总管只写 `night_supervisor_2026-05-23/`，代理可写本目录下 `agents/bixiu4_*` |
| 选必二 | GPT Pro + Claude 互动完善框架，直到聪明高三学生可直接上手 | `reports/选必二法律主观题框架_从题源生长/v12_2_framework_growth_restart/v13_10_final_baodian_integrated` | `CANDIDATE_DELIVERY_NEEDS_AUDIT`，23:06 已产出 v13_10 Markdown/Word/PDF/traceability/render QA，但仍需核真实 GPT/Claude、框架迭代和学生全对验收 | 本总管只写 `night_supervisor_2026-05-23/`，代理可写本目录下 `agents/xuanbier_*` |

## 总管代理登记

| 代理 | agent id | 分工 | 输出 |
|---|---|---|---|
| Confucius | `019e5561-f0b6-7b61-8c0c-84473f5ba74b` | 选必一监督：覆盖、宝典同级、真实 GPT/Claude、交付闭环 | `agents/xuanbiyi_status.md`；`patch_orders/ORDER_010_XUANBIYI_NEXT.md` |
| Bernoulli | `019e5561-f242-7b10-bd88-5ec1bb9b4b32` | 必修四监督：旧缺题、新增题、v7/v8、框架保真、Governor/QA | `agents/bixiu4_status.md`；`patch_orders/ORDER_020_BIXIU4_NEXT.md` |
| Tesla | `019e5561-f29c-70e0-8761-371d6b7a3200` | 选必二监督：v13_10 严格验收、GPT/Claude 框架互动、42题 traceability | `agents/xuanbier_status.md`；`patch_orders/ORDER_030_XUANBIER_NEXT.md` |
