#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/lib.sh"
load_env

echo "Bridge:"
if bridge_is_listening; then
  echo "  listening on $LISTEN_HOST:$LISTEN_PORT"
else
  echo "  not listening on $LISTEN_HOST:$LISTEN_PORT"
fi

echo
echo "Upstream:"
echo "  $UPSTREAM_HOST:$UPSTREAM_PORT"
if nc -z "$UPSTREAM_HOST" "$UPSTREAM_PORT" >/dev/null 2>&1; then
  echo "  reachable from this network"
else
  echo "  not reachable from this network"
fi

echo
echo "Public IP through California bridge:"
if bridge_is_listening; then
  curl --proxy "http://$LISTEN_HOST:$LISTEN_PORT" --connect-timeout 15 --max-time 30 https://ipinfo.io/json || true
  echo
else
  echo "  skipped because bridge is not listening"
fi

echo
echo "Public IP without proxy:"
curl --noproxy '*' --connect-timeout 15 --max-time 30 https://api.ipify.org || true
echo

echo
echo "macOS system proxy:"
scutil --proxy
