import json
import unittest
from unittest.mock import MagicMock, patch
from urllib.parse import quote, unquote

from bugreport import server

OK_RESPONSE = b'{"status":"ok","retcode":0,"data":{"message_id":1}}'
TIMESTAMP = "2026-08-31T16:00:00+08:00"
TITLE = "测试标题[CQ:at,qq=all]"
CATEGORY = "category-1"
CATEGORY_LABEL = "整合包侧「须臾」"
DOCS_BASE = "https://docs.example.test"


def _urlopen_ok():
    response = MagicMock()
    response.__enter__.return_value.read.return_value = OK_RESPONSE
    return response


class ConfigTestCase(unittest.TestCase):
    """统一保存/恢复 server 模块级的可变配置。"""

    CONFIG_NAMES = (
        "ONEBOT_HTTP_URL",
        "ONEBOT_ADMIN_GROUP_ID",
        "ONEBOT_MAIN_GROUP_ID",
        "ONEBOT_ACCESS_TOKEN",
        "DOCS_SITE_BASE_URL",
    )

    def setUp(self):
        self.originals = {name: getattr(server, name) for name in self.CONFIG_NAMES}
        self.addCleanup(self.restore_config)

    def restore_config(self):
        for name, value in self.originals.items():
            setattr(server, name, value)


class OneBotNotificationTests(ConfigTestCase):
    def configure(self, url="http://127.0.0.1:3000", admin="111111", main="222222", token="test-token", docs=DOCS_BASE):
        server.ONEBOT_HTTP_URL = url
        server.ONEBOT_ADMIN_GROUP_ID = admin
        server.ONEBOT_MAIN_GROUP_ID = main
        server.ONEBOT_ACCESS_TOKEN = token
        server.DOCS_SITE_BASE_URL = docs

    @patch.object(server.urllib.request, "urlopen")
    def test_sends_distinct_messages_to_admin_and_main_groups(self, urlopen):
        self.configure()
        urlopen.side_effect = [_urlopen_ok(), _urlopen_ok()]

        states = server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY)

        self.assertEqual(states, {"admin": "sent", "main": "sent"})
        self.assertEqual(urlopen.call_count, 2)

        admin_request = urlopen.call_args_list[0].args[0]
        main_request = urlopen.call_args_list[1].args[0]
        admin_payload = json.loads(admin_request.data.decode("utf-8"))
        main_payload = json.loads(main_request.data.decode("utf-8"))

        self.assertEqual(admin_request.full_url, "http://127.0.0.1:3000/send_group_msg")
        self.assertEqual(admin_request.get_header("Authorization"), "Bearer test-token")
        self.assertEqual(admin_payload["group_id"], 111111)
        self.assertTrue(admin_payload["auto_escape"])
        self.assertEqual(
            admin_payload["message"],
            "[问题汇报提醒]\n"
            f"时间戳：{TIMESTAMP}\n"
            f"标题：{TITLE}\n"
            f"服务器大类：{CATEGORY_LABEL}",
        )

        self.assertEqual(main_request.full_url, "http://127.0.0.1:3000/send_group_msg")
        self.assertEqual(main_request.get_header("Authorization"), "Bearer test-token")
        self.assertEqual(main_payload["group_id"], 222222)
        self.assertTrue(main_payload["auto_escape"])
        self.assertEqual(
            main_payload["message"],
            "收到新的反馈报告\n"
            f"{TIMESTAMP}\n"
            f"主题：{TITLE}\n"
            f"所属 {CATEGORY_LABEL}\n"
            f"链接：{DOCS_BASE}/#/bugreports/{CATEGORY}?id={quote(server.docsify_anchor(TITLE), safe='')}",
        )

    @patch.object(server.urllib.request, "urlopen")
    def test_skips_group_without_configured_id(self, urlopen):
        self.configure(main="")
        urlopen.side_effect = [_urlopen_ok()]

        states = server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY)

        self.assertEqual(states, {"admin": "sent", "main": "disabled"})
        self.assertEqual(urlopen.call_count, 1)
        payload = json.loads(urlopen.call_args_list[0].args[0].data.decode("utf-8"))
        self.assertEqual(payload["group_id"], 111111)

    def test_is_disabled_when_no_onebot_config_is_present(self):
        self.configure(url="", admin="", main="")
        self.assertEqual(
            server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY),
            {"admin": "disabled", "main": "disabled"},
        )

    @patch("builtins.print")
    @patch.object(server.urllib.request, "urlopen")
    def test_one_group_failure_does_not_block_the_other(self, urlopen, _print):
        self.configure()
        urlopen.side_effect = [OSError("connection refused"), _urlopen_ok()]

        states = server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY)

        self.assertEqual(states, {"admin": "failed", "main": "sent"})
        self.assertEqual(urlopen.call_count, 2)

    @patch("builtins.print")
    @patch.object(server.urllib.request, "urlopen")
    def test_reports_failure_when_onebot_rejects_the_message(self, urlopen, _print):
        self.configure(main="")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"status":"failed","retcode":100}'
        urlopen.return_value = response

        self.assertEqual(
            server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY),
            {"admin": "failed", "main": "disabled"},
        )

    @patch.object(server.urllib.request, "urlopen")
    def test_main_message_omits_link_when_docs_base_is_empty(self, urlopen):
        self.configure(admin="", main="222222", docs="")
        urlopen.side_effect = [_urlopen_ok()]

        server.send_onebot_notification(TIMESTAMP, TITLE, CATEGORY)

        payload = json.loads(urlopen.call_args_list[0].args[0].data.decode("utf-8"))
        self.assertEqual(payload["message"].splitlines()[-1], f"所属 {CATEGORY_LABEL}")


class DocsifyAnchorTests(ConfigTestCase):
    """锚点规则需与 docsify 5.x 的 Docsify.slugify() 一致（已用真实页面核对过）。"""

    CASES = {
        "webTEST": "webtest",
        "TEST": "test",
        "测试": "测试",
        "截止9.26上午10：40发现的问题": "截止926上午10：40发现的问题",
        "多个AE破坏面板放入神秘工匠渗透附魔台只会放入一个，其余消失": "多个ae破坏面板放入神秘工匠渗透附魔台只会放入一个，其余消失",
        "水晶科技 末影发信器": "水晶科技-末影发信器",
        "神秘基础学·神秘自然研究内容缺失": "神秘基础学·神秘自然研究内容缺失",
        "9月的问题": "_9月的问题",
    }

    def test_matches_docsify_slugify(self):
        for title, expected in self.CASES.items():
            with self.subTest(title=title):
                self.assertEqual(server.docsify_anchor(title), expected)

    def test_report_link_points_at_category_page_and_anchor(self):
        server.DOCS_SITE_BASE_URL = DOCS_BASE + "/"
        link = server.report_link(CATEGORY, TITLE)
        self.assertTrue(link.startswith(f"{DOCS_BASE}/#/bugreports/{CATEGORY}?id="))
        self.assertEqual(unquote(link.split("?id=", 1)[1]), server.docsify_anchor(TITLE))

    def test_report_link_is_empty_without_docs_base(self):
        server.DOCS_SITE_BASE_URL = ""
        self.assertEqual(server.report_link(CATEGORY, TITLE), "")


class ReportBodyTests(unittest.TestCase):
    """提交者按纯文本书写，正文换行需补两个空格才会在 Markdown 中真正换行。"""

    def test_quote_body_adds_hard_break_spaces(self):
        self.assertEqual(
            server.quote_body("第一行\n第二行\n\n第四行"),
            "> 第一行  \n> 第二行  \n>\n> 第四行  ",
        )

    def test_quote_body_normalizes_existing_trailing_spaces(self):
        self.assertEqual(server.quote_body("a   \nb\t\n  \nc"), "> a  \n> b  \n>\n> c  ")

    def test_render_report_body_keeps_line_breaks(self):
        block = server.render_report(
            title="多行正文",
            category_label=CATEGORY_LABEL,
            type_label=server.TYPE_LABELS["bug"],
            reporter="Tester",
            timestamp=TIMESTAMP,
            report_id="20260831-160000-abcdef01",
            content="第一行\n第二行",
        )
        body = block.split("#### 工单内容\n\n", 1)[1]
        self.assertEqual(body, "> 第一行  \n> 第二行  ")


if __name__ == "__main__":
    unittest.main()
