# GPT-5.5 Pro 内容审查门复核记录（2026-05-02）

## Codex 发给 GPT 的脱敏问题

用户新增硬要求：以后每次完成学生可见成果，都希望 GPT-5.5 Pro 检查和修正具体内容；用户不缺时间，允许夜间反复跑。Codex 已把整本书工作流升级为：每完成学生可见成果、章节批次、最终 Markdown、Word/PDF 文本抽取，都把生成内容本身分块发给 GPT-5.5 Pro 做内容检查；GPT 输出问题等级；Codex 保存原始审稿、写 correction log、本地证据核验后修正；有 must-fix 问题未清零不得 final PASS。请 GPT 检查这套机制是否足够，并给出还应固化进 skill 的硬规则。

## GPT-5.5 Pro 原始答复（复制自网页）

## 1. GO/NO-GO

**GO。**

这套 **GPT-5.5 Pro 内容审查门** 可以固化进 Codex 的 `/飞哥政治庄园/整本书三线总控` skill。

但最终交付必须执行硬条件：

```text
存在 unresolved mustfixcontent：NO-GO，禁止 final PASS。
存在 unresolved shouldfixtransfer：NO-GO，禁止学生终稿 final PASS。
仅剩 styleorreadability：可以 GO，但必须记录未修原因或确认不影响学生迁移。
```

---

## 2. skill 应固化的规则

建议 Codex 在 skill 中新增这一段：

```text
模块名：
GPT-5.5 Pro Content Review And Correction Gate

触发对象：
1. outline
2. section batch
3. final Markdown
4. Word/PDF

流程：
1. Codex 将脱敏 artifact 发给 GPT-5.5 Pro 做内容审查。
2. GPT-5.5 Pro 只审内容质量、迁移链条、可读性、审计痕迹、Word/PDF交付风险。
3. GPT-5.5 Pro 对问题按 severity 分类：
   a. mustfixcontent
   b. shouldfixtransfer
   c. styleorreadability
4. Codex 保存 GPT 原始审查意见。
5. Codex 将每条问题写入 contentcorrectionlog.md。
6. Codex 对涉及内容事实、知识判断、证据等级的问题回到本地证据复核。
7. Codex 决定采纳、部分采纳、拒绝、延后。
8. Codex patch 学生稿或 Word/PDF。
9. Codex 更新 patchstatus。
10. Governor G11 检查是否允许 final PASS。
```

`contentcorrectionlog.md` 必填字段继续保持：

```text
issueid
artifact
location
severity
gptclaim
proposedcorrection
localevidencecheckneeded
codexdecision
patchstatus
affectsstudentdoc
```

建议补充两个字段：

```text
localcheckresult
verifiedclosed_at
```

这样才能证明 Codex 不是只登记问题，而是真的完成证据复核和关闭。

---

## 3. 必须补的硬规则

### 规则 1：GPT 分类不能代替 Codex 裁决

```text
GPT 的 severity 是初判。
Codex 的 codexdecision 是本地裁决。
Governor G11 看 codexdecision 和 patchstatus，不只看 GPT 原文。
```

### 规则 2：mustfixcontent 必须本地证据复核

凡是 `mustfixcontent`，必须进入：

```text
localevidencecheckneeded = yes
patchstatus = checkinglocal / patched / verifiedclosed / rejected
```

不能直接改学生稿。

### 规则 3：shouldfixtransfer 必须回到学生迁移链

凡是 `shouldfixtransfer`，Codex 必须检查对应位置是否有：

```text
材料触发点
为什么想到
答案落点
可迁移表达
```

缺一项就不能关闭。

### 规则 4：styleorreadability 可以快修，但不得改事实

```text
styleorreadability 可以直接润色、调序、改标题、补过渡。
但只要涉及知识点、题型规律、证据等级、答案落点，就必须升级为 mustfixcontent 或 shouldfixtransfer。
```

### 规则 5：G11 final PASS 条件要写死

```text
G11 PASS 条件：
1. outline 已审查或有 fallback/waiver。
2. section batch 已审查或有 fallback/waiver。
3. final Markdown 已审查。
4. Word/PDF 已审查。
5. GPT raw review 已保存。
6. contentcorrectionlog.md 字段完整。
7. mustfixcontent 无 unresolved。
8. shouldfixtransfer 无 unresolved。
9. 所有采纳项 patchstatus = verifiedclosed。
10. 所有拒绝项有 localcheckresult。
11. 所有延后项进入用户待裁决清单。
```

### 规则 6：final Markdown 和 Word/PDF 要分开 PASS

```text
Markdown PASS：
内容、结构、迁移链条、审计痕迹通过。

Word/PDF PASS：
目录、页码、图片、漫画、表格、选项换行、标题层级、视觉可读性通过。
```

不能用 Markdown 通过替代 Word/PDF 通过。

---

## 4. 最大风险

最大风险仍然是 **登记型闭环**：

```text
GPT 已审查
Codex 已保存 raw review
Codex 已写 correction log
```

这些只能说明流程发生过，不能说明问题已经解决。

真正的闭环必须看：

```text
1. 每条 issue 有没有 codexdecision。
2. 需要本地证据复核的有没有 localcheckresult。
3. 采纳项有没有 patch。
4. patch 后有没有回看 artifact。
5. mustfixcontent 和 shouldfixtransfer 有没有清零。
6. Word/PDF 修补后有没有重新渲染验收。
```

---

## 5. Codex 下一步

Codex 现在应按这个顺序做：

```text
1. 把 GPT-5.5 Pro Content Review And Correction Gate 写入 skill。

2. 新增 Governor G11：
   GPT Content Review And Correction Gate。

3. 建立目录：
   gptcontentreview/
   contentcorrectionlog.md

4. 固化 raw review 命名：
   contentreview01_outline_gpt.md
   contentreview02_section_batch01_gpt.md
   contentreview03_final_markdown_gpt.md
   contentreview04_word_pdf_gpt.md

5. 固化 correction log 字段：
   issueid
   artifact
   location
   severity
   gptclaim
   proposedcorrection
   localevidencecheckneeded
   localcheckresult
   codexdecision
   patchstatus
   affectsstudentdoc
   verifiedclosed_at

6. 做一次小样演练：
   用一个 outline 或 section batch 跑完整链条。

7. 演练必须验证：
   GPT raw review 能保存。
   每条 GPT issue 能进入 correction log。
   mustfixcontent 会触发本地证据复核。
   shouldfixtransfer 会触发迁移链修补。
   styleorreadability 能快修但不改事实。
   unresolved mustfixcontent 会阻断 final PASS。
   unresolved shouldfixtransfer 会阻断学生终稿 PASS。

8. 演练通过后，再进入整本书正式运行。
```

最终判断：**GO，允许固化 skill；final PASS 必须由 G11 控制，且 unresolved mustfixcontent 和 unresolved shouldfixtransfer 必须清零。**

## Codex 消化

已采纳并固化：

- 固定触发对象：`outline`、`section_batch`、`final_markdown`、`word_pdf`。
- 补充 `content_correction_log.md` 字段：`local_check_result`、`verified_closed_at`。
- G11 不再只看 raw review 或登记日志，而是看本地裁决、证据核验、patch 状态、关闭状态。
- `must_fix_content` 未清零阻断 final PASS；transfer-blocking `should_fix_transfer` 未清零阻断学生终稿。
- Markdown PASS 与 Word/PDF PASS 分开记录；Markdown 通过不能替代 Word/PDF 通过。
- Word/PDF 仍必须覆盖目录、页码、图片、漫画、表格、选项换行、标题层级、视觉可读性。
