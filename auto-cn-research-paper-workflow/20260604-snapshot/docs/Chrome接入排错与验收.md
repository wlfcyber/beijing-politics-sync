# Chrome 接入排错与验收

## 当前结论

当前自动科研流的本地 workflow 已就绪，Chrome 插件接管已恢复。知网检索和详情页链路已经通过；全文下载链路已触发到 `CNKI-Login`，需要用户本人完成登录/机构认证后继续。

## 当前证据

| 项目 | 当前证据 | 结论 |
| --- | --- | --- |
| Chrome 当前配置 | `LastUsedProfile=Profile 1`，`LastActiveProfiles=Profile 1` | 当前 Chrome 使用 `Profile 1` |
| 扩展文件 | `Profile 1\Extensions\hehggadaopoacecdllhhajmbjkdcmajg` 存在 | Codex 扩展文件存在 |
| 扩展启用记录 | `Profile 1\Preferences` 中 `HasCodexSetting=False` | 当前配置没有注册/启用 Codex 扩展 |
| Native Host | `C:\Users\Administrator\AppData\Local\OpenAI\extension\com.openai.codexextension.json` 存在 | 本机消息桥接 manifest 存在 |
| Native Host 允许来源 | `chrome-extension://hehggadaopoacecdllhhajmbjkdcmajg/` | Host 允许正确扩展 ID |
| 插件通道测试 | 返回 `Browser is not available: extension` | Codex Chrome Extension 未连通 |
| Computer Use 浏览器接管 | 被系统停止，原因是无法可靠识别浏览器 URL | 不能用它绕过 Chrome 插件通道 |
| Chrome 扩展详情页 | Chrome 进程标题出现 `扩展程序 - Codex - Google Chrome` | 用户已打开 Codex 扩展页 |
| Chrome 扩展进程 | Chrome 启动参数中出现 `--extension-process` | Chrome 中存在扩展进程 |
| Native Host 可执行文件 | `extension-host.exe` 存在 | Host 可执行文件存在 |
| 复测结果 | 打开扩展页后再次返回 `Browser is not available: extension` | 仍未连通 |
| 重新添加扩展后复测 | Chrome 插件通道能列出标签页，metadata 显示 `profileName=Lifei`，`extensionId=hehggadaopoacecdllhhajmbjkdcmajg` | 已恢复 |
| CNKI 检索 | `https://cnki.net/index/` 可用，检索 `数字治理` 后进入 `Search-CNKI` 结果页 | 已通过 |
| 详情页 | 可打开第一条结果详情页并读取摘要、关键词、DOI 等元数据 | 已通过 |
| 下载入口 | `PDF Download` 可触发，但跳转到 `CNKI-Login` | 需要用户登录 |

## 你需要检查的设置

在当前 Chrome 中打开：

```text
chrome://extensions
```

检查是否有名为 `Codex` 的扩展。

### 如果能看到 Codex 扩展

1. 确认右下角开关是开启状态。
2. 点击“详情”。
3. 确认扩展没有被 Chrome 标记为错误、损坏或需要修复。
4. 回到人大图书馆/知网页面，保持该标签页打开。

### 如果看不到 Codex 扩展

说明扩展文件虽在本地目录里，但没有被当前 Chrome 配置注册。需要从 Codex 插件 UI 重新安装或修复 Chrome 插件，然后回到当前 Chrome 配置 `Profile 1`。

### 如果 Codex 扩展显示损坏或错误

不要手动改 Chrome 配置文件。优先在 Codex 插件 UI 中重新安装/修复 Chrome 插件。

## 我不能自行执行的修复

我不能手工编辑 Chrome `Preferences`、强制写入扩展启用状态、绕过 Chrome 扩展注册流程，或用前台键鼠方式绕过浏览器 URL 安全校验。当前需要通过 Chrome 扩展页面或 Codex 插件 UI 完成修复。

## 我这边的验收动作

当前验收进度：

1. Chrome 插件通道能列出打开标签页：已通过。
2. 能读取当前知网页面标题和 URL：已通过。
3. 能接管人大图书馆/知网标签页：CNKI Overseas 已通过；`www.cnki.net` 被 `ERR_BLOCKED_BY_CLIENT` 阻断。
4. 能执行一次测试检索：已通过。
5. 能打开一条文献详情页：已通过。
6. 能触发允许的下载，或明确记录“需用户导出/PDF 不可得”：已触发下载入口，但被 `CNKI-Login` 阻断。
7. 能把检索日志和文献状态写入工作区：已写入 `知网接入验收记录.md`。

只有上述 1-7 都完成，才能声明“真实知网检索与下载链路可用”。

## 安全边界

- 我不会读取、保存或分析密码、Cookie、local storage、浏览器密码、会话文件。
- 登录、验证码、统一身份认证和身份确认由你本人完成。
- 我不会绕过知网、人大图书馆或学校库的访问控制和下载限制。
- 只处理当前论文任务需要的文献，不做批量下载或镜像。
