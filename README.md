# California Proxy Mac Kit

This kit makes macOS use a local unauthenticated HTTP proxy:

```text
macOS apps -> 127.0.0.1:18001 -> authenticated upstream proxy -> California IP
```

The upstream proxy credentials live only in `~/.california-proxy.env`, not in this folder.

## Files

- `macos_proxy_bridge.py`: local proxy bridge that injects upstream proxy authentication.
- `run-bridge.sh`: starts the bridge from the env file.
- `install-launchd.sh`: installs a user LaunchAgent so the bridge starts at login and stays alive.
- `start-global-proxy.sh`: starts the bridge and points all enabled macOS network services to `127.0.0.1:18001`.
- `stop-global-proxy.sh`: disables macOS HTTP/HTTPS system proxies.
- `status.sh`: checks bridge, upstream reachability, current IP, and macOS proxy settings.
- `proxy-env.sh`: optional shell env exports for Terminal tools that ignore macOS System Proxy.

## Setup

Copy the template:

```bash
cp proxy.env.example ~/.california-proxy.env
chmod 600 ~/.california-proxy.env
```

Edit `~/.california-proxy.env`:

```bash
nano ~/.california-proxy.env
```

Fill it like this:

```bash
LISTEN_HOST=127.0.0.1
LISTEN_PORT=18001
UPSTREAM_HOST=direct.miyaip.online
UPSTREAM_PORT=8001
UPSTREAM_USERNAME=your_username_here
UPSTREAM_PASSWORD=your_password_here
```

Make scripts executable:

```bash
chmod +x *.sh macos_proxy_bridge.py
```

Start the global proxy:

```bash
./start-global-proxy.sh
```

Check status:

```bash
./status.sh
```

Expected California IP:

```text
165.254.151.116
```

## Terminal And Codex CLI

Many native macOS apps, Chrome, Edge, Safari, and the Codex desktop app usually follow macOS System Proxy.

Some Terminal tools do not. In that case run:

```bash
source ./proxy-env.sh
```

Then test:

```bash
curl https://api.ipify.org
```

## Wi-Fi Notes

macOS proxy settings are attached to network services, such as `Wi-Fi`, `Thunderbolt Bridge`, or USB Ethernet. They are not simply one universal switch.

This kit applies the proxy to all enabled services, so switching from Wi-Fi to Ethernet should usually keep working. But different Wi-Fi networks can still behave differently:

- Some networks block `direct.miyaip.online:8001`.
- Some networks hijack DNS or require captive portal login.
- Some networks block direct proxy traffic but allow it only after another VPN/TUN layer.
- Some apps ignore macOS System Proxy and need shell env vars or true TUN mode.

If `./status.sh` says the upstream is not reachable, that network cannot directly use the California proxy. You then need a bottom-layer VPN/TUN first, or a different upstream endpoint.

## Stop

Disable macOS system proxy:

```bash
./stop-global-proxy.sh
```

Remove the login LaunchAgent:

```bash
./uninstall-launchd.sh
```

## Important

This is a system HTTP/HTTPS proxy setup, not a true packet-level VPN. It covers apps that honor macOS proxy settings. It does not guarantee all UDP traffic, all games, or all apps will use the California IP.
