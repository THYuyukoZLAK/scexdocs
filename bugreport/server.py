#!/usr/bin/env python3
"""Minimal local API that stores validated bug reports as Markdown files."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import unicodedata
import urllib.request
import uuid
from collections import defaultdict, deque
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import quote

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
# 工单按子服务器合并保存：每个大类对应一个 docs/bugreports/category-*.md 文件，
# 新工单追加到该文件顶部；索引页 docs/bugreports/README.md 由 rebuild_index() 重建。
# 由于位于 docsify 的 basePath (docs/) 下，文档站可直接查阅工单内容。
REPORTS_DIR = PROJECT_DIR / "docs" / "bugreports"
INDEX_FILE = REPORTS_DIR / "README.md"
REPORTS_MARKER = "<!-- reports -->"
MAX_BODY_BYTES = 64 * 1024
CATEGORY_LABELS = {
    "category-1": "整合包侧「须臾」",
    "category-2": "创造养老侧「永远」",
    "category-3": "怀旧向子服「旧梦」",
}
CATEGORIES = set(CATEGORY_LABELS)
TYPE_LABELS = {"bug": "BUG/错误", "request": "Request/新功能申请", "other": "其他"}
MINECRAFT_ID = re.compile(r"^[A-Za-z0-9_]{3,16}$")
RATE_LIMIT_COUNT = 5
RATE_LIMIT_WINDOW = 10 * 60
REQUESTS: dict[str, deque[float]] = defaultdict(deque)
REQUESTS_LOCK = Lock()
# LLBot / OneBot v11 configuration.
# 管理群（内部处理用）与主群（面向玩家公示）会各收到一条格式不同的通知。
# ONEBOT_HTTP_URL 留空则整体禁用；某个群号留空则跳过该目标。
# token 必须与 LLBot 中设置的一致，留空则不发送 Authorization 头。
ONEBOT_HTTP_URL = "http://127.0.0.1:3002"  # Example: "http://127.0.0.1:3000"
ONEBOT_ADMIN_GROUP_ID = "978225175"  # 管理群
ONEBOT_MAIN_GROUP_ID = "362344872"  # 主群
ONEBOT_ACCESS_TOKEN = ""
ONEBOT_TIMEOUT_SECONDS = 5

# 文档站根地址，用于在群通知里附上工单的直达链接（末尾不要带斜杠）。
# 留空则通知中不附链接；换域名/端口后需同步修改。
DOCS_SITE_BASE_URL = "http://scex.aerohakugyokurou.top:8880"


def markdown_cell(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def report_file(category: str) -> Path:
    """返回某个子服务器对应的工单文件（一个子服务器一个文件）。"""
    return REPORTS_DIR / f"{category}.md"


def report_form_link() -> str:
    """指向工单提交页的原生链接。

    docsify 会把 Markdown 链接 /bugreport/ 改写成 hash 路由 #/bugreport/（死路由），
    因此这里用带 target 的原始 HTML 锚点，让浏览器直接请求独立提交应用。
    """
    return '<a href="/bugreport/" target="_blank" rel="noopener">工单提交页</a>'


def category_header(category: str) -> str:
    """生成工单文件顶部的固定说明，末尾的标记用于插入新工单。"""
    return (
        f"# {CATEGORY_LABELS[category]}\n\n"
        "> 本页由工单系统自动维护，新提交的工单会自动出现在最前面。\n"
        f"> 提交新工单请前往 {report_form_link()}。\n\n"
        f"{REPORTS_MARKER}\n"
    )


def quote_body(content: str) -> str:
    """把工单正文渲染成引用块，并为每个换行补两个空格。

    提交者通常按纯文本习惯书写，单个换行在 Markdown 里会被合并成空格；
    补两个行尾空格（CommonMark 硬换行）可让正文保持原本的分行。
    空行保留为 `>`，仍作为段落分隔。
    """
    lines = []
    for line in content.splitlines():
        if not line.strip():
            lines.append(">")
        else:
            lines.append("> " + line.rstrip() + "  ")
    return "\n".join(lines)


def render_report(
    *,
    title: str,
    category_label: str,
    type_label: str,
    reporter: str,
    timestamp: str,
    report_id: str,
    content: str,
) -> str:
    """把一条工单渲染成可追加到子服务器文件的 Markdown 片段。"""
    quoted = quote_body(content)
    return (
        "---\n\n"
        f"### {title}\n\n"
        "| 字段 | 内容 |\n| --- | --- |\n"
        f"| 工单编号 | {report_id} |\n"
        f"| 大类 | {markdown_cell(category_label)} |\n"
        f"| 类型 | {markdown_cell(type_label)} |\n"
        f"| 提交者 Minecraft ID | {markdown_cell(reporter)} |\n"
        f"| 提交时间 | {timestamp} |\n\n"
        f"#### 工单内容\n\n{quoted}"
    )


def append_report(category: str, block: str) -> None:
    """把新工单插入到对应子服务器文件的最前面（紧随标记之后）。"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = report_file(category)
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    anchor = f"{REPORTS_MARKER}\n"
    if anchor not in text:
        text = category_header(category)
    text = text.replace(anchor, f"{anchor}\n{block}\n", 1)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_records(text: str) -> list[dict[str, str]]:
    """从子服务器文件中解析出每条工单的元信息，用于重建索引。"""
    records: list[dict[str, str]] = []
    for chunk in re.split(r"(?m)^### ", text)[1:]:
        lines = chunk.splitlines()
        record = {"title": lines[0].strip(), "id": "", "type": "", "reporter": "", "time": ""}
        for line in lines[1:]:
            if line.startswith("#### "):
                break
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 2:
                continue
            key, value = cells
            if key in {"字段", "---"} or set(key) <= {"-"}:
                continue
            if key == "工单编号":
                record["id"] = value
            elif key == "类型":
                record["type"] = value
            elif key == "提交者 Minecraft ID":
                record["reporter"] = value
            elif key == "提交时间":
                record["time"] = value
        records.append(record)
    return records


def rebuild_index() -> None:
    """根据各子服务器文件重建 docs/bugreports/README.md 索引页。"""
    sections: list[str] = []
    total = 0
    for category, label in CATEGORY_LABELS.items():
        path = report_file(category)
        records = parse_records(path.read_text(encoding="utf-8")) if path.exists() else []
        if not records:
            continue
        total += len(records)
        # docsify 将 Markdown 链接解析为相对 basePath（docs/）的路径，
        # 因此这里的链接必须带 bugreports/ 前缀，否则会退化成 /category-N 而 404。
        rows = "\n".join(
            f"| {record['id']} | {markdown_cell(record['type'])} | {markdown_cell(record['reporter'])} "
            f"| {record['time']} | [{markdown_cell(record['title'])}](bugreports/{path.name}) |"
            for record in records
        )
        sections.append(
            f"## {label}\n\n"
            "| 工单编号 | 类型 | 提交者 | 提交时间 | 标题 |\n"
            "| --- | --- | --- | --- | --- |\n"
            f"{rows}\n"
        )
    document = (
        "# 工单记录\n\n"
        "> 本页由工单系统自动维护，每次提交工单后自动重建。\n"
        f"> 提交新工单请前往 {report_form_link()}。\n\n"
        f"当前共 **{total}** 份工单。\n\n"
        + "\n".join(sections)
    )
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(document, encoding="utf-8", newline="\n")


def client_address(handler: BaseHTTPRequestHandler) -> str:
    if handler.client_address[0] in {"127.0.0.1", "::1"}:
        forwarded = handler.headers.get("X-Real-IP", "").strip()
        if forwarded:
            return forwarded[:64]
    return handler.client_address[0]


def rate_limited(address: str) -> bool:
    now = time.monotonic()
    with REQUESTS_LOCK:
        attempts = REQUESTS[address]
        while attempts and now - attempts[0] > RATE_LIMIT_WINDOW:
            attempts.popleft()
        if len(attempts) >= RATE_LIMIT_COUNT:
            return True
        attempts.append(now)
        return False


# docsify 5.x 的 Docsify.slugify()：标题在页面上生成元素 id 时使用的规则。
_DOCSIFY_PUNCTUATION = re.compile(
    r"[\u2000-\u206f\u2e00-\u2e7f\\'!\"#$%&()*+,./:;<=>?@\[\]^`{|}~]"
)
_DOCSIFY_MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_DOCSIFY_HTML_TAG = re.compile(r"<[^>]+>")
_DOCSIFY_UPPERCASE = re.compile(r"[A-Z]+")
_DOCSIFY_LEADING_DIGIT = re.compile(r"^(\d)")
# Python 的 re 不支持 \p{Emoji_Presentation}，这里近似覆盖主要 emoji 区段；
# 若标题含罕见 emoji，锚点可能对不上，但链接仍会正常打开对应子服务器页面。
_DOCSIFY_EMOJI = re.compile("[\U0001f000-\U0001faff]")


def docsify_anchor(title: str) -> str:
    """复刻 docsify 的 Docsify.slugify()，得到标题在页面上生成的元素 id。"""
    anchor = unicodedata.normalize("NFC", title.strip())
    anchor = _DOCSIFY_MARKDOWN_LINK.sub(r"\1", anchor)
    anchor = anchor.replace("\ufe0f", "")
    anchor = _DOCSIFY_EMOJI.sub("", anchor)
    anchor = _DOCSIFY_UPPERCASE.sub(lambda match: match.group(0).lower(), anchor)
    anchor = _DOCSIFY_HTML_TAG.sub("", anchor)
    anchor = _DOCSIFY_PUNCTUATION.sub("", anchor)
    anchor = re.sub(r"\s", "-", anchor)
    return _DOCSIFY_LEADING_DIGIT.sub(r"_\1", anchor)


def report_link(category: str, title: str) -> str:
    """工单在文档站的直达链接（docsify hash 路由 + 标题锚点）。

    新工单总是插在子服务器文件最前面，因此它就是该页第一个同名标题，
    docsify 不会给它加 -1 之类的去重后缀，锚点即 slugify(title)。
    """
    base = DOCS_SITE_BASE_URL.strip().rstrip("/")
    if not base:
        return ""
    anchor = docsify_anchor(title)
    if not anchor:
        return f"{base}/#/bugreports/{category}"
    return f"{base}/#/bugreports/{category}?id={quote(anchor, safe='')}"


# 群通知文案与站内术语刻意不同步：站内统一用「工单」，通知仍沿用
# 「[问题汇报提醒]」/「收到新的反馈报告」。修改前请先与运营确认。
def admin_message(timestamp: str, title: str, category_label: str) -> str:
    """管理群通知：便于内部定位与处理。"""
    return (
        "[问题汇报提醒]\n"
        f"时间戳：{timestamp}\n"
        f"标题：{title}\n"
        f"服务器大类：{category_label}"
    )


def main_group_message(timestamp: str, title: str, category_label: str, category: str) -> str:
    """主群通知：面向玩家的公示版，并附上该工单在文档站的直达链接。"""
    lines = [
        "收到新的反馈报告",
        timestamp,
        f"主题：{title}",
        f"所属 {category_label}",
    ]
    link = report_link(category, title)
    if link:
        lines.append(f"链接：{link}")
    return "\n".join(lines)


def onebot_status_line() -> str:
    """启动时打印 OneBot 通知配置概要。"""
    labels = (("管理群", ONEBOT_ADMIN_GROUP_ID), ("主群", ONEBOT_MAIN_GROUP_ID))
    url = ONEBOT_HTTP_URL.strip()
    if not url:
        return "[OneBot] 未配置 ONEBOT_HTTP_URL，群通知已禁用"
    active = [f"{label} {group.strip()}" for label, group in labels if group.strip()]
    if not active:
        return "[OneBot] 未配置群号，群通知已禁用"
    base = DOCS_SITE_BASE_URL.strip().rstrip("/")
    suffix = f"；工单链接前缀 {base}" if base else "；未配置 DOCS_SITE_BASE_URL，通知不带链接"
    return "[OneBot] 群通知已启用：" + "、".join(active) + f"（{url}）" + suffix


def send_group_message(group_config: str, message: str) -> str:
    """向单个群发送纯文本消息。

    返回 "sent"（已发送）或 "disabled"（未配置该群）；发送失败则抛异常。
    """
    api_url = ONEBOT_HTTP_URL.strip().rstrip("/")
    group_text = group_config.strip()
    if not api_url or not group_text:
        return "disabled"
    try:
        group_id = int(group_text)
    except ValueError as error:
        raise ValueError("群号必须是数字") from error

    endpoint = api_url
    if not endpoint.endswith("/send_group_msg"):
        endpoint += "/send_group_msg"
    if not endpoint.startswith(("http://", "https://")):
        raise ValueError("ONEBOT_HTTP_URL 必须使用 http:// 或 https://")

    body = json.dumps(
        {"group_id": group_id, "message": message, "auto_escape": True},
        ensure_ascii=False,
    ).encode("utf-8")
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if ONEBOT_ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ONEBOT_ACCESS_TOKEN}"

    request = urllib.request.Request(endpoint, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=ONEBOT_TIMEOUT_SECONDS) as response:
        result = json.loads(response.read(MAX_BODY_BYTES).decode("utf-8"))
    if not isinstance(result, dict) or result.get("status") not in {"ok", "async"}:
        raise RuntimeError(f"OneBot 返回失败：{result!r}")
    if result.get("retcode") not in {0, 1}:
        raise RuntimeError(f"OneBot 返回异常状态：{result!r}")
    return "sent"


def send_onebot_notification(timestamp: str, title: str, category: str) -> dict[str, str]:
    """向管理群与主群推送工单通知，返回每个群的状态。

    `category` 是大类键（如 category-1），显示名从 CATEGORY_LABELS 取。
    两个目标互相独立：留空即跳过，其中一个失败不影响另一个。
    """
    category_label = CATEGORY_LABELS.get(category, category)
    targets = (
        ("admin", ONEBOT_ADMIN_GROUP_ID, admin_message(timestamp, title, category_label)),
        ("main", ONEBOT_MAIN_GROUP_ID, main_group_message(timestamp, title, category_label, category)),
    )
    states: dict[str, str] = {}
    for name, group_config, message in targets:
        try:
            states[name] = send_group_message(group_config, message)
        except Exception as error:
            # 工单已经落盘，通知失败只记录状态，绝不影响提交结果。
            states[name] = "failed"
            print(f"[OneBot] {name} 群通知发送失败：{error}", flush=True)
    return states


class ReportHandler(BaseHTTPRequestHandler):
    server_version = "SCEXReportAPI/1.0"

    def log_message(self, format: str, *args: object) -> None:
        print(f"[{self.log_date_time_string()}] {client_address(self)} {format % args}")

    def send_json(self, status: int, payload: dict[str, object]) -> None:
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(encoded)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/bugreport":
            self.send_json(404, {"error": "接口不存在。"})
            return

        content_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        if content_type != "application/json":
            self.send_json(415, {"error": "仅接受 JSON 请求。"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY_BYTES:
            self.send_json(413, {"error": "提交内容为空或过大。"})
            return

        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "请求内容不是有效的 JSON。"})
            return
        if not isinstance(payload, dict):
            self.send_json(400, {"error": "请求格式无效。"})
            return

        if str(payload.get("website", "")).strip():
            self.send_json(200, {"id": "received"})
            return

        category = str(payload.get("category", "")).strip()
        report_type = str(payload.get("type", "")).strip()
        title = str(payload.get("title", "")).strip()
        content = str(payload.get("content", "")).strip()
        reporter = str(payload.get("reporter", "")).strip()

        if category not in CATEGORIES:
            self.send_json(400, {"error": "请选择有效的大类。"})
            return
        category_label = CATEGORY_LABELS[category]
        if report_type not in TYPE_LABELS:
            self.send_json(400, {"error": "请选择有效的工单类型。"})
            return
        if not 1 <= len(title) <= 100 or "\n" in title or "\r" in title:
            self.send_json(400, {"error": "标题须为 1 至 100 个字符，且不能换行。"})
            return
        if not 1 <= len(content) <= 10000:
            self.send_json(400, {"error": "工单内容须为 1 至 10000 个字符。"})
            return
        if not MINECRAFT_ID.fullmatch(reporter):
            self.send_json(400, {"error": "Minecraft ID 须为 3 至 16 位字母、数字或下划线。"})
            return
        if rate_limited(client_address(self)):
            self.send_json(429, {"error": "提交过于频繁，请十分钟后再试。"})
            return

        now = datetime.now().astimezone()
        timestamp = now.isoformat(timespec="seconds")
        report_id = f"{now:%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:8]}"
        block = render_report(
            title=title,
            category_label=category_label,
            type_label=TYPE_LABELS[report_type],
            reporter=reporter,
            timestamp=timestamp,
            report_id=report_id,
            content=content,
        )
        try:
            append_report(category, block)
        except OSError:
            self.send_json(500, {"error": "服务器无法写入工单文件。"})
            return
        try:
            rebuild_index()
        except OSError as error:
            # 工单已成功写入，索引重建失败不应让提交失败。
            print(f"[report] 索引重建失败：{error}", flush=True)

        # The report is already durable; an external notification failure must
        # never turn the submission into an apparent failure and cause retries.
        try:
            notification = send_onebot_notification(timestamp, title, category)
        except Exception as error:  # 兜底：通知层异常不能影响已落盘的提交
            notification = {"admin": "failed", "main": "failed"}
            print(f"[OneBot] 工单 {report_id} 通知发送失败：{error}", flush=True)
        if any(state == "failed" for state in notification.values()):
            print(f"[OneBot] 工单 {report_id} 通知结果：{notification}", flush=True)

        self.send_json(201, {"id": report_id, "notification": notification})


def main() -> None:
    parser = argparse.ArgumentParser(description="SCEX bug report Markdown API")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8881)
    parser.add_argument("--pid-file", type=Path)
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="重建 docs/bugreports/README.md 索引后退出",
    )
    args = parser.parse_args()

    if args.rebuild_index:
        rebuild_index()
        print(f"索引已重建：{INDEX_FILE}", flush=True)
        return

    try:
        rebuild_index()
    except OSError as error:
        print(f"[report] 启动时重建索引失败：{error}", flush=True)

    server = ThreadingHTTPServer((args.host, args.port), ReportHandler)
    if args.pid_file:
        args.pid_file.write_text(str(os.getpid()), encoding="ascii")
    try:
        print(f"Bug report API listening on http://{args.host}:{args.port}", flush=True)
        print(onebot_status_line(), flush=True)
        server.serve_forever()
    finally:
        if args.pid_file:
            args.pid_file.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
