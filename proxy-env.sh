#!/usr/bin/env bash

# Source this file in Terminal sessions whose tools do not read macOS System Proxy:
#   source ./proxy-env.sh

export http_proxy="http://127.0.0.1:18001"
export https_proxy="http://127.0.0.1:18001"
export HTTP_PROXY="$http_proxy"
export HTTPS_PROXY="$https_proxy"
export no_proxy="localhost,127.0.0.1,::1"
export NO_PROXY="$no_proxy"

echo "Shell proxy environment set to $http_proxy"
