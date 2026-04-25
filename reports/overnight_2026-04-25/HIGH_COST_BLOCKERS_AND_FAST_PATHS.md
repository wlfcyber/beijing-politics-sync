# 高算力卡点与下次快路径

## 1. Word 表格渲染卡点

卡点：三份 Word 第一次用 Markdown 表格转 DOCX，artifact-tool 渲染后出现竖排窄列。之后又尝试固定表格宽度，仍然失败。

真正简单的解法：不用宽表，改成“标题 + 字段标签 + 条目块”。中文密集资料更适合块状排版。

下次规则：第一版就默认块状排版。只有很短的 2-3 列数据才用表格；一旦渲染出现竖列，立刻放弃表格，不做第二轮表格调参。

## 2. PowerShell here-doc 卡点

卡点：按 Linux 习惯用了 `python - <<'PY'`，PowerShell 直接报语法错。

真正简单的解法：PowerShell 使用 here-string 管道：

```powershell
@'
print("hello")
'@ | python -
```

下次规则：Windows/PowerShell 下不使用 Bash here-doc。

## 3. Unicode 路径和反斜杠卡点

卡点：Python 里硬写中文长路径和 `.replace("\\", "\")` 造成语法错误或 mojibake。

真正简单的解法：用 `Path.home() / "Desktop"`、`glob()`、文件大小或模式发现路径，避免手工拼长中文路径。

下次规则：处理中文路径先设 `$env:PYTHONUTF8='1'`，Python 内使用 `pathlib`，必要时用 `glob` 找目录。

## 4. PDF 下载卡点

卡点：`Invoke-WebRequest` 下载门头沟 PDF 超时，留下一个不完整文件；PyMuPDF 打开后 `pages 0`，容易误判为解析问题。

真正简单的解法：用 `curl.exe -L --fail --connect-timeout 30 --max-time 600 -o file url` 重新下载，再检查文件大小和页数。

下次规则：大 PDF/中文 CDN 链接默认用 `curl.exe`；页数为 0 时先重下，不调解析代码。

## 5. 本地搜索导致假 blocker

卡点：选择题劳动者只查本地目录，认为三套 2026 客观答案源缺失；主线程后来通过公开 PDF 很快补证。

真正简单的解法：blocker 进入最终前做升级搜索：本地、重复目录、zip、OCR、外部补源。

下次规则：任何“找不到答案源/细则源”的结论都必须先走 blocker-escalation ladder，不能只凭本地 `rg` 或目录扫描定案。

## 6. 参考答案边界卡点

卡点：门头沟一模外部 PDF 既有选择题答案，也有主观参考答案。它能关闭客观答案源，却不能关闭主观细则缺口。

真正简单的解法：一开始就把源拆成 `objective-answer-key` 和 `reference-answer` 两种用途。

下次规则：参考答案可以补客观答案和题源存在性；主观框架只能用细则、评标、阅卷报告、讲评评分口径或用户确认材料。

## 7. 角色协作卡点

卡点：子线程给出 findings，但主线程还要再发现、整合、验证，缺少统一的发现处置表。

真正简单的解法：每个角色输出固定 schema；主线程维护 `ROLE_FINDING_DISPOSITION.md`，逐条标记 merged/rejected/blocked/superseded。

下次规则：没有发现处置表，不能进入最终验收。

## 8. 独立线程可视化不足

卡点：这次虽然 spawn 了角色，但用户侧不一定能按“项目”查看所有线程；自动化角色因线程上限没有单独线程。

真正简单的解法：新任务创建 `<书名>的政治庄园` 项目文件夹，里面有 `THREAD_REGISTRY.md` 和 `ROLE_THREAD_PROMPTS.md`。能 spawn 就登记 agent id；不能 spawn 就把角色报告写入 `threads/`。

下次规则：启动任务先建项目，再建角色线程，再登记线程，而不是边做边补。
