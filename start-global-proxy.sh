#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/lib.sh"
load_env

if ! bridge_is_listening; then
  "$SCRIPT_DIR/install-launchd.sh"
fi

if ! wait_for_bridge; then
  echo "Bridge is not listening on $LISTEN_HOST:$LISTEN_PORT." >&2
  exit 1
fi

echo "Setting macOS HTTP and HTTPS system proxies to $LISTEN_HOST:$LISTEN_PORT..."

while IFS= read -r service; do
  [[ -z "$service" ]] && continue
  echo "  $service"
  set_proxy_for_service "$service"
done < <(enabled_network_services)

echo
echo "Testing upstream reachability..."
nc -vz "$UPSTREAM_HOST" "$UPSTREAM_PORT" || true

echo
echo "Testing California public IP through the local bridge..."
curl --proxy "http://$LISTEN_HOST:$LISTEN_PORT" --connect-timeout 15 --max-time 30 https://api.ipify.org
echo

echo
echo "System proxy summary:"
scutil --proxy
