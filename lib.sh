#!/usr/bin/env bash
set -euo pipefail

KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${CALIFORNIA_PROXY_ENV:-$HOME/.california-proxy.env}"
PLIST_PATH="$HOME/Library/LaunchAgents/com.user.california-proxy-bridge.plist"
LABEL="com.user.california-proxy-bridge"

load_env() {
  if [[ ! -f "$ENV_FILE" ]]; then
    echo "Missing env file: $ENV_FILE" >&2
    echo "Copy proxy.env.example to ~/.california-proxy.env and fill it in." >&2
    exit 1
  fi

  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a

  LISTEN_HOST="${LISTEN_HOST:-127.0.0.1}"
  LISTEN_PORT="${LISTEN_PORT:-18001}"
}

enabled_network_services() {
  networksetup -listallnetworkservices |
    sed '1d' |
    grep -v '^\*' |
    sed '/^[[:space:]]*$/d'
}

bridge_is_listening() {
  nc -z "${LISTEN_HOST:-127.0.0.1}" "${LISTEN_PORT:-18001}" >/dev/null 2>&1
}

wait_for_bridge() {
  local deadline
  deadline=$((SECONDS + 15))
  while (( SECONDS < deadline )); do
    if bridge_is_listening; then
      return 0
    fi
    sleep 0.5
  done
  return 1
}

set_proxy_for_service() {
  local service="$1"
  networksetup -setwebproxy "$service" "$LISTEN_HOST" "$LISTEN_PORT" off
  networksetup -setsecurewebproxy "$service" "$LISTEN_HOST" "$LISTEN_PORT" off
  networksetup -setwebproxystate "$service" on
  networksetup -setsecurewebproxystate "$service" on
  networksetup -setproxybypassdomains "$service" localhost 127.0.0.1 ::1
}

disable_proxy_for_service() {
  local service="$1"
  networksetup -setwebproxystate "$service" off
  networksetup -setsecurewebproxystate "$service" off
}
