我必须先停下来汇报一个阻塞性问题：**你贴进来的三个 batch 的正文内容全部是乱码（?? 占位符），我读不到任何一条 entry 的实质中文文本**。

## 现状

三批材料的结构性字段（编号、题目标签如 `2026????`、字段名如 `???????` `????` `????????` `??????`）都还能看出位置，但每一条的 **题干摘录 / 来源 / 期望要点 / 当前内容** 的中文正文都已被替换成 `?` 字符。Summary、Governor 备注、ClaudeCode B 报告同样全部乱码。

这是典型的 Windows 控制台 / PowerShell 把 UTF-8 文本以 GBK 或 cp437 读取后再回写的编码事故，不是 prompt injection，但它让"语义 → 来源 → 形式"三段审查无法进行——我连一条条目在讲哪个考点都看不到，更不可能判定 DELETE / REWRITE / NEED_EVIDENCE / PASS。

## 我不会做的事

- **不会**凭结构（节点名、来源年份、字段位置）猜测条目含义并产出虚假裁决。按你过去的硬约束，弱证据/无证据的内容必须 NEED_EVIDENCE 或 REWRITE，而我现在面对的是 100% 无证据——任何"裁决"都等同于编造。
- **不会**只对极少数能从英文 token 还原的内容（例如 `OPC` `OvernightPolicyChange` `MBTI`）单点开火，因为这会让你误以为剩余 40 条已经过审。

## 需要你这边做一次的事

请用以下任一种方式把同样的三批材料重发一次，确保 UTF-8：

1. **最稳**：把三个 batch 各自存成 `.md` 文件（UTF-8 with BOM 或纯 UTF-8）后告诉我路径，我用 Read 工具直接读，绝不会经过终端编码层。建议路径：
   - `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/05_final_review_input/batch_01_all_inserted_entries.md`
   - `.../batch_02_high_risk_render_pages.md`
   - `.../batch_03_summary_and_gate.md`
2. 若坚持要贴进对话，请先在源端执行 `chcp 65001` 或在 PowerShell 里用 `Get-Content -Encoding UTF8 path | Set-Clipboard`，再粘贴；粘贴后请先目测确认中文不再是 `?`。
3. 你也可以直接告诉我"读 `05_delivery/student_patch_entries.accepted.jsonl` 与 `student_patch_entries.blocked.jsonl`，按 41 + 74 的口径出三段审"，我会从仓库内文件读，绕开任何终端编码层。

## 一个先行 sanity check（不依赖正文）

仅凭你给的 summary 数字，已经能看出两处需要你确认是否是预期口径：

- batch_03 顶部写 **accepted 41 / blocked 74**，但同文件 `???????` 段又写 **接受 26 条**，且 `???????` 节点合计是 **26 节点配额**而非 41。请确认 41 是不是已经把"prompt_gate_resolution 后从 blocked 升回 accepted 的 9 条 + Tongzhou 修复 2 条 + weak_gate 修复若干"全部并入；如果 26 才是当前 ledger 的真值，那 batch_01 里多出的条目本身就是越权插入，需要先解决口径再审条目。
- `COVERAGE_CLOSURE_MATRIX_V2` 说 35/35 全部 `COVERED_OR_PATCHED`、open gate=0，但同文件下方又自承"some closure rows still retain blocked_weak_evidence counts while also having accepted_insertions"。这两句在同一份 governor 文档里直接相互削弱——外审（GPTPro / Claude 网页）大概率会以此为切口质疑"本地 PASS"成色。建议你在重发材料前，自己先决定这份矛盾要保留还是合并。

请告诉我你倾向哪种重发方式，我等到能真正读到中文正文后再开始三段审，不会先开工垫话。
