#!/usr/bin/env bash
set -euo pipefail

KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${CALIFORNIA_PROXY_ENV:-$HOME/.california-proxy.env}"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing env file: $ENV_FILE" >&2
  echo "Copy proxy.env.example to ~/.california-proxy.env and fill it in." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

PYTHON_BIN="${PYTHON_BIN:-python3}"
exec "$PYTHON_BIN" "$KIT_DIR/macos_proxy_bridge.py"
