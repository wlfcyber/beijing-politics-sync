#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/lib.sh"
load_env

echo "Disabling macOS HTTP and HTTPS system proxies..."

while IFS= read -r service; do
  [[ -z "$service" ]] && continue
  echo "  $service"
  disable_proxy_for_service "$service"
done < <(enabled_network_services)

echo
echo "System proxy summary:"
scutil --proxy
