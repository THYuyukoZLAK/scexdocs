#!/usr/bin/env bash
# SCEX DOCS 停止脚本 (Linux)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -x "$SCRIPT_DIR/nginx-linux/sbin/nginx" ]; then
    NGINX_BIN="$SCRIPT_DIR/nginx-linux/sbin/nginx"
else
    NGINX_BIN="$(command -v nginx || true)"
fi

echo "正在停止 SCEX DOCS..."
if [ -n "$NGINX_BIN" ]; then
    "$NGINX_BIN" -g "pid $SCRIPT_DIR/nginx.pid;" -s stop 2>/dev/null || true
fi
rm -f "$SCRIPT_DIR/nginx.pid"

if [ -f "$SCRIPT_DIR/bugreport/server.pid" ]; then
    API_PID="$(cat "$SCRIPT_DIR/bugreport/server.pid")"
    kill "$API_PID" 2>/dev/null || true
    rm -f "$SCRIPT_DIR/bugreport/server.pid"
fi

echo "已停止。"
