#!/usr/bin/env bash
# SCEX DOCS 启动脚本 (Linux)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="${PORT:-8880}"

if [ -x "$SCRIPT_DIR/nginx-linux/sbin/nginx" ]; then
    NGINX_BIN="$SCRIPT_DIR/nginx-linux/sbin/nginx"
    MIME_INCLUDE="$SCRIPT_DIR/nginx-linux/conf/mime.types"
else
    NGINX_BIN="$(command -v nginx || true)"
    MIME_INCLUDE="/etc/nginx/mime.types"
fi

if [ -z "$NGINX_BIN" ]; then
    echo "[错误] 未找到 nginx。请先安装：sudo apt install nginx" >&2
    exit 1
fi
if [ ! -f "$MIME_INCLUDE" ]; then
    echo "[错误] 未找到 mime.types：$MIME_INCLUDE" >&2
    exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
    echo "[错误] 未找到 Python 3，工单功能无法启动。" >&2
    exit 1
fi
if ss -ltn 2>/dev/null | grep -q ":$PORT "; then
    echo "[错误] 端口 $PORT 已被占用。" >&2
    exit 1
fi
if ss -ltn 2>/dev/null | grep -q ":8881 "; then
    echo "[错误] 工单 API 端口 8881 已被占用。" >&2
    exit 1
fi

echo "============================================"
echo "  SCEX DOCS 启动脚本 (Linux / nginx)"
echo "============================================"
echo "  项目目录 : $SCRIPT_DIR"
echo "  端口     : $PORT"
echo "  nginx    : $NGINX_BIN"
echo

python3 "$SCRIPT_DIR/bugreport/server.py" \
    --pid-file "$SCRIPT_DIR/bugreport/server.pid" \
    >> "$SCRIPT_DIR/bugreport/server.log" 2>&1 &
API_PID=$!

CONF="$(mktemp /tmp/scex-nginx.conf.XXXXXX)"
trap 'rm -f "$CONF"; kill "$API_PID" 2>/dev/null || true' ERR
sed -e "s|@ROOT@|$SCRIPT_DIR|g" \
    -e "s|@MIME@|$MIME_INCLUDE|g" \
    -e "s|listen       8880;|listen       $PORT;|g" \
    "$SCRIPT_DIR/deploy/nginx.conf.template" > "$CONF"

"$NGINX_BIN" -c "$CONF" -g "pid $SCRIPT_DIR/nginx.pid;"
rm -f "$CONF"
trap - ERR

echo "已启动，请访问 http://localhost:$PORT"
echo "工单提交页：http://localhost:$PORT/bugreport/"
echo "停止服务请运行 ./stop-server.sh"
