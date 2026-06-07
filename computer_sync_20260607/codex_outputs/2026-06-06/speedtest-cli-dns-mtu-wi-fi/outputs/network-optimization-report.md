# 网络加速诊断与处理报告

日期：2026-06-06（北京时间）

## 已确认的 3 个主要问题

1. CLI/测速流量被 Windows 用户代理和环境变量导向 `127.0.0.1:18001` California 代理。
   - 代理出口显示为 `165.254.151.116 / NTT-LTD / US`，speedtest-cli 因此选择洛杉矶/蒂华纳等远端测速站。
   - Cloudflare 25MB 下载：走代理约 1,846,853 B/s（约 14.8 Mbps）；加入直连例外后约 10,012,411 B/s（约 80.1 Mbps）。

2. MTU 不匹配。
   - Wi-Fi 接口当前 MTU 为 1500。
   - 实测 1500 路径会收到“需要分片”，1492 可通过。
   - 调整 MTU 需要管理员权限，当前窗口无法写入。

3. 后台/配置负担。
   - 存在非当前自动连接 Wi-Fi 配置 `zjy`，当前高速 5GHz 配置是 `zjy_5G`。
   - Steam/steamwebhelper 后台进程存在网络连接。
   - Delivery Optimization 有大量缓存/历史下载记录，但当前性能快照没有实时下载速率；限速需要管理员或设置页权限。

## 已执行的改动

- 安装并运行了 `speedtest-cli`。
- 删除非当前 Wi-Fi 配置 `zjy`，只保留当前 `zjy_5G`。
- 关闭后台 Steam/steamwebhelper 进程。
- 刷新 DNS 缓存。
- 未改 DNS 服务器：路由器 DNS `192.168.1.1` 实测约 30-45 ms，比直接访问 1.1.1.1/8.8.8.8 的约 600 ms 更快。
- 优化本地/mDNS 与测速绕行：
  - 用户 `NO_PROXY` 从 `localhost,127.0.0.1,::1` 更新为 `localhost,127.0.0.1,::1,.local,speed.cloudflare.com`。
  - Windows 代理例外新增 `speed.cloudflare.com`。
  - 保留 California 代理，没有全局关闭，避免影响需要代理的应用。

## 前后测试摘要

- speedtest-cli（走系统代理）：
  - 前：下载约 15.7 Mbps，上传约 15.6 Mbps，延迟约 199 ms，洛杉矶服务器。
  - 后：下载约 15.7 Mbps，上传约 15.5 Mbps，延迟约 177 ms，洛杉矶服务器。

- Cloudflare 下载能力：
  - 走代理：约 14.8 Mbps。
  - 直连 IPv6/代理例外后：约 80.1 Mbps。

- 延迟/丢包：
  - 到路由器：0% 丢包，平均约 5-7 ms。
  - 到 GitHub：0% 丢包，约 112-115 ms。
  - 到 OpenAI：0% 丢包，前约 229 ms，后约 192 ms。
  - 到 8.8.8.8：前一次出现 12% 丢包，复测 0% 丢包，约 233 ms。

- Wi-Fi：
  - `zjy_5G`，5GHz，802.11ax，信号 76%，协商速率 2402 Mbps，信道利用率约 3%。
  - 结论：室内 Wi-Fi 不是主要瓶颈。

## 仍需管理员权限的推荐项

1. 把 WLAN MTU 调为 1492：
   `netsh interface ipv4 set subinterface "WLAN" mtu=1492 store=persistent`

2. 在 Windows 设置中限制 Delivery Optimization 后台下载：
   - 后台下载建议 5%。
   - 前台下载建议 25%。

## 结论

本次真正有效的提速来自代理绕行：对可直连的 Cloudflare 测试下载，速度从约 14.8 Mbps 提升到约 80.1 Mbps。Wi-Fi 链路本身状态良好；剩余主要瓶颈是系统代理路径、跨境/运营商链路，以及需要管理员权限才能修复的 MTU/后台更新限速。
