# 新电脑接管提示：必修四哲学 v4 / ClaudeCode OCR-needed 回收监督

更新时间：2026-04-28  
当前操作者：Codex 监督者  
当前目标：把 ClaudeCode 拉回“cache-first + 一手来源复核”的轨道，继续补完三年模拟 55 套中 OCR-needed / needs_followup / source-missing 的真实边界。

## 0. 当前结论

- 当前 Mac 上没有 ClaudeCode CLI 后台任务在运行；S001 尚未重新启动。
- 已停止一轮错误倾向的 S001 运行：那轮把“不能吃旧结论”误扩大成“不能吃已转换的一手来源缓存”，这是不对的。
- 正确口径：旧分析结论、旧框架条目、旧 CSV 推断不能当证据；但从原始试卷、答案、细则转换出来的 txt、suite bundle、render 图片，属于一手来源缓存，必须优先使用。
- 项目根目录 `CLAUDE.md` 已在本机修正为 2026-04-28 cache-first 接管规则。旧版“禁止读缓存/同步仓库”的表述只保留为“禁止引用旧结论”的安全提醒。
- S001 的 cache-first 指令已经写好：
  `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/CLAUDE_OCR_RERUN_S001_CACHE_FIRST_PROMPT.md`
- 同一份完整 prompt 已同步进 Git 仓库：
  `reports/claude_ocr_rerun_s001_cache_first_prompt_2026-04-28.md`

## 1. 当前项目路径

主工作目录：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27`

主要输出目录：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4`

最终 v4 产物：

- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/必修四哲学材料-知识触发框架_原框架节点版_v4.md`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/必修四哲学材料-知识触发框架_原框架节点版_v4_审计证据版.md`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/PHILOSOPHY_FRAMEWORK_ENTRIES_CANONICAL.csv`

OCR 重跑目录：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun`

控制清单：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/codex_claude_compare/08_OCR-needed重跑控制清单.md`

## 2. 已知 OCR-needed / source 边界

必须重跑 OCR / 读图回收：

- S001 `2024东城一模`
- S009 `2024丰台二模`
- S038 `2026丰台一模`
- S040 `2026房山一模`
- S042 `2026海淀一模`
- S048 `2026丰台期末`
- S050 `2026朝阳期末`
- S052 `2026海淀期末`

文件未真缺失、ClaudeCode 曾误判：

- S046 `2026顺义一模`：试卷 PDF 可读；细则 PPTX 第2页有 Q16；PPTX 第1页有 1-15 答案键。

真 source/key 缺口：

- S044 `2026西城一模`：有试卷和主观题细则，缺 Q1-15 客观答案键。
- S053 `2026西城期末`：本地 `试卷/` 无试卷；有参考答案、评标 PPTX、细则 PDF。
- S055 `2026石景山期末`：本地只有 `其他材料/答案及评分参考.pdf`，无试卷。

本地 OCR/图片 followup：

- S007、S008、S015、S019、S029、S033

模块边界排除，不是漏：

- S006、S034、S051

## 3. S042 特别注意：不是个例风险

S042 `2026海淀一模` 已由 ClaudeCode 跑出：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/S042_2026海淀一模.md`

但需要重新审计它的结论。

当前 Codex 核验到的本地 `细则.pdf` 文字是：第16题“可从发展的观点、社会存在与社会意识、价值观、文化的功能等角度作答”。没有查到字面“物质决定意识”。  
ClaudeCode 的问题是：它把“不是字面物质决定意识”扩大成“应清出这个唯物论相关入口”，这太粗。至少必须进入 `社会存在与社会意识` 节点；如果用户教学框架把“社会存在决定社会意识”归入广义“物质决定意识”讲法，还应做关联提示，而不是删除。

新电脑接管后要做一轮“细则关键词 -> 框架节点”反向审计，防止 S042 这种不是个例。

## 4. S001 下一步：不要从头乱 OCR，必须 cache-first

S001 已确认的一手来源缓存：

- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/suite_bundles/S001_2024东城一模.txt`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/suite_focus_bundles/S001_2024东城一模.txt`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/extracted_texts/S001_2024东城一模_scoring_rubric_4b2073bcc9e2_细则.pptx.txt`
- `/Users/wanglifei/Desktop/政治模拟题_故事化返工_20260427_Codex重做_v2/00_benchmark_15/texts/2024东城一模_rubric.txt`
- `/Users/wanglifei/Desktop/政治模拟题_故事化返工_20260427_Codex重做_v2/00_benchmark_15/texts/2024东城一模_paper.txt`

注意：`2024东城一模_paper.txt` 经查是 0 字节。要在审计里记录“paper txt cache empty”，然后使用已渲染图片补试卷正文。

已有渲染图片：

- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模/page_*.png`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模_split/page*_strip*.png`
- `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模_ans/page_01.png`

## 5. 新电脑启动 ClaudeCode 的命令

如果新电脑也是 Mac 且路径一致，在主工作目录运行：

```zsh
cd /Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27
/Users/wanglifei/.local/bin/claude -p --verbose --model opus --effort max \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --output-format stream-json \
  --include-partial-messages \
  --debug-file outputs_v4/visible_runs/claude_ocr_rerun_S001_cache_first_debug.log \
  "$(< outputs_v4/CLAUDE_OCR_RERUN_S001_CACHE_FIRST_PROMPT.md)" \
  | tee outputs_v4/visible_runs/claude_ocr_rerun_S001_cache_first_stream.jsonl
```

如果新电脑路径不同，把 prompt 里的路径先整体改成新电脑实际路径；但不能改变工作原则。

如果新电脑没有本机 `outputs_v4/CLAUDE_OCR_RERUN_S001_CACHE_FIRST_PROMPT.md`，可直接使用本仓库里的：

`reports/claude_ocr_rerun_s001_cache_first_prompt_2026-04-28.md`

## 5A. ClaudeCode 记忆迁移包

已在本机桌面生成一个不含账号登录态/token 的 ClaudeCode 记忆迁移包：

`/Users/wanglifei/Desktop/claudecode_memory_transfer_2026-04-28.tar.gz`

SHA256：

`39a859bfb23a5dd5a044e05b9b6f1323641746c1dd971867e99e8f9373a7f0fa`

包内含：

- 本项目 `~/.claude/projects/.../*.jsonl` raw session；
- S042/S001 的 stream-json、debug log、visible run；
- Claude prompts、S001 cache-first prompt、final Word prompt；
- Codex/Claude 双版本比对材料；
- OCR-needed 控制清单和已渲染页面；
- 最新 skill 规则与项目级 `CLAUDE.md`。

包内不含：

- `~/.claude.json`
- `~/.claude/backups`
- `~/.claude/cache`
- Claude 登录态、token、auth

新电脑若要恢复 raw ClaudeCode 会话历史，可解压后执行：

```zsh
mkdir -p ~/.claude/projects/-Users-wanglifei-Desktop-claude-bixiu4-independent-rerun-2026-04-27
rsync -a claudecode_memory_transfer_2026-04-28/claude_raw_project_sessions/ \
  ~/.claude/projects/-Users-wanglifei-Desktop-claude-bixiu4-independent-rerun-2026-04-27/
```

这一步是 best-effort：ClaudeCode 是否在界面里直接显示旧会话，取决于新电脑 ClaudeCode 版本和项目路径识别；即使不显示，jsonl 也能作为完整历史查证。真正无缝继续仍以本 handoff、S001 prompt、skill 规则和输出产物为准。

## 6. 监督标准

ClaudeCode 运行时要看这些信号：

- `ps` 里必须有 `claude -p` 或对应 CLI 进程。
- stream jsonl 必须持续出现 tool_use、assistant message、file edit、write 等实际动作。
- debug log 如果长时间只显示网络重试，要先确认 auth / 网络 / 代理，而不是让它继续空等。
- 判断“卡住”要看数据：进程状态、elapsed time、stream-json 增量、debug log 增量、输出文件 mtime、tool call、网络/auth 报错。不能因为可见正文停顿就直接杀掉。
- 若确实需要重启，不要改成“只给它核心句让它拼答案”。优先重发同一套完整任务，或让它写 checkpoint 后继续同一套；不得绕过当前套卷跳下一套。
- 模型优先级：能用 Opus 4.7 adaptive/max 就用；CLI 只能表达为 `--model opus --effort max` 时，启动后必须从 stream 里确认真实模型是 Opus 系列。
- S001 之后继续 S009、S038、S040、S048、S050、S052；S042 则做纠偏审计。
- 如果后续为了加速开多条线，可以从队首、队中、队尾倒推三段并行，但每条线必须分配不重叠的套卷范围，最终由监督者统一合并到原理方法论框架，而不是按题号/套卷顺序堆。

## 7. 最终文档硬标准

- 按用户原有“原理方法论”框架组织，不按题号堆题。
- 最终 Word 标题固定为 `2026北京高考政治哲学宝典---三年模拟全触发全链条`。
- 首页只保留标题和大署名 `飞哥正志讲堂`，要大气好看；标题下面不要副标题、过程说明、来源说明或工作日志。
- 第二页留“前言”部分给用户自己写，不要把过程说明塞进去。
- ClaudeCode 可以按自己的审美设计最终 Word，但内容不能改，不能在最终版后面附工作日志。
- 设问必须抄全。
- 材料只摘触发关键句，但要足够学生看懂。
- 触发逻辑必须解释“材料里的哪句话/哪种关系为什么能想到这个原理”，不能写“因为细则写了所以能放”。
- 回应设问必须写成具体答案链：因为什么原理，所以材料中的主体应/能够/需要怎么做，最终回答题目问的什么。
- 学生最终版不能出现 source path、F04、slide、L24、OCR log、debug 语句。
- 来源、路径、页码、缓存说明只能进审计文件。
- 不得无中生有题号、题面、细则或答案键。

## 8. 双版本比对与融合要求

- 后续要对比 ClaudeCode 版和 Codex 版：两边都放在同一原理方法论下、且题号/设问/材料/细则一致的，可视为双模型复核后的高置信条目。
- 两边不一致的，不能直接删；必须回到原题、材料和细则判断谁对，并把剩余分歧列给用户人工审。
- Codex 有而 ClaudeCode 漏掉的条目要单列：先判断是 ClaudeCode 漏源、框架节点判断不同，还是 Codex 自己过度扩张。
- 对 ClaudeCode 已写的“从题目到原理方法论解释链”，要审查学生是否看得懂；必要时 Codex 重新写一遍，再融合出最终版。

## 9. 给新电脑 Codex 的直接提示

你现在接管的是“飞哥正志讲堂：2026北京高考政治哲学宝典---三年模拟全触发全链条”的 v4/OCR-needed 复核监督。先不要自己改最终稿，先检查 ClaudeCode 是否可用，并从 `S001 / 2024东城一模` 的 cache-first prompt 启动 ClaudeCode。严格区分“旧结论不能吃”和“一手来源缓存必须优先吃”。当前无 ClaudeCode 后台进程，S001 尚未重启。请按本文件第 5 节命令启动，监督它跑完 S001；跑完后审核它是否补全完整设问、材料触发、知识触发逻辑、具体回应设问、细则边界。然后继续 OCR-needed 队列，不得把未跑完的卷子称为完成。
