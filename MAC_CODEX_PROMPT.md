# Prompt For Mac Codex

Paste this into Codex on the Mac after copying or cloning this folder there.

```text
我想把这台 Mac 的普通浏览器和 Codex 尽量全局切到美国加州代理。请在当前目录的 california-proxy-mac-kit 工具包里操作。

目标结构：
macOS apps -> 127.0.0.1:18001 -> direct.miyaip.online:8001 -> California IP

请按这个顺序做：

1. 检查当前目录里是否有这些文件：
   - macos_proxy_bridge.py
   - proxy.env.example
   - run-bridge.sh
   - install-launchd.sh
   - start-global-proxy.sh
   - status.sh

2. 如果 ~/.california-proxy.env 不存在，从 proxy.env.example 复制一份：
   cp proxy.env.example ~/.california-proxy.env
   chmod 600 ~/.california-proxy.env

3. 提醒我填入真实代理配置，或者如果我已经给了你，就帮我写入 ~/.california-proxy.env：
   LISTEN_HOST=127.0.0.1
   LISTEN_PORT=18001
   UPSTREAM_HOST=direct.miyaip.online
   UPSTREAM_PORT=8001
   UPSTREAM_USERNAME=<我的用户名>
   UPSTREAM_PASSWORD=<我的密码>

4. 给脚本加可执行权限：
   chmod +x *.sh macos_proxy_bridge.py

5. 执行：
   ./start-global-proxy.sh

6. 执行：
   ./status.sh

7. 判断结果：
   - 如果 bridge listening on 127.0.0.1:18001，说明本机桥启动成功。
   - 如果 upstream reachable，说明当前 Wi-Fi 可以直连加州代理。
   - 如果 Public IP through California bridge 是 165.254.151.116 / Los Angeles / California，说明加州代理成功。
   - 如果 macOS system proxy 显示 HTTPEnable/HTTPSEnable 为 1，并指向 127.0.0.1:18001，说明普通浏览器会走它。

8. 如果 Terminal 或 Codex CLI 不走系统代理，执行：
   source ./proxy-env.sh
   curl https://api.ipify.org

9. 请不要把真实 ~/.california-proxy.env、用户名或密码提交到 GitHub。

10. 如果加州代理必须先打开 0cloud 才能访问，请解释这是底层网络无法直连 direct.miyaip.online:8001，不是脚本问题。优先建议使用能独立直连的加州上游，或者让 0cloud 只做底层 TUN/VPN，不要让它把系统代理抢回 7897。
```
