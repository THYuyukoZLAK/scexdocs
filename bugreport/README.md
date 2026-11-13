# 工单提交页

iframe 地址为 `/bugreport/`，例如：

```html
<iframe src="/bugreport/" title="工单提交" width="100%" height="620" loading="lazy"></iframe>
```

三个服务器选项的 `value` 请保留为
`category-1`、`category-2`、`category-3`。工单按子服务器合并写入
`docs/bugreports/category-1.md`、`docs/bugreports/category-2.md`、
`docs/bugreports/category-3.md`（**一个子服务器一个文件**），索引页
`docs/bugreports/README.md` 会随每次提交自动重建。
如需修改服务器显示名称，请同步修改 `index.html` 中的选项文本和 `server.py` 中的
`CATEGORY_LABELS`，服务端映射也是群提醒使用的可信名称。

页面需配合 `server.py` 使用。项目启动脚本会自动在本机 `8881` 端口启动该服务，
nginx 将 `/api/bugreport` 转发到它。接收端只依赖 Python 3 标准库。

工单文件位于文档站的 `docs/bugreports/` 下，已作为公开文档随站点提供，可在「工单记录」页面直接查阅。

如需手动重建索引，可执行：

```bash
python bugreport/server.py --rebuild-index
```

## LLBot / OneBot v11 群通知

在 LLBot 中启用 OneBot v11 正向 HTTP 服务，然后修改 `bugreport/server.py` 顶部的常量：

| 常量 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- |
| `ONEBOT_HTTP_URL` | 是 | `http://127.0.0.1:3002` | LLBot HTTP 服务根地址；也可填写以 `/send_group_msg` 结尾的完整地址；留空则整体禁用 |
| `ONEBOT_ADMIN_GROUP_ID` | 否 | `978225175` | 管理群群号（内部处理用） |
| `ONEBOT_MAIN_GROUP_ID` | 否 | `362344872` | 主群群号（面向玩家公示） |
| `ONEBOT_ACCESS_TOKEN` | 否 | `your-secret-token` | 与 LLBot 配置一致的访问令牌，建议启用 |
| `DOCS_SITE_BASE_URL` | 否 | `http://scex.aerohakugyokurou.top:8880` | 文档站根地址；主群通知会附上工单直达链接，留空则不带链接 |

两个群各收到一条格式不同的通知，且互不影响（群号留空即跳过，一个失败不阻断另一个）：

管理群：

```text
[问题汇报提醒]
时间戳：2026-09-07T19:16:15+08:00
标题：xx模组导致的客户端偶发崩溃问题
服务器大类：创造养老侧「永远」
```

主群：

```text
收到新的反馈报告
2026-09-07T19:16:15+08:00
主题：xx模组导致的客户端偶发崩溃问题
所属 创造养老侧「永远」
链接：http://scex.aerohakugyokurou.top:8880/#/bugreports/category-2?id=xx%E6%A8%A1%E7%BB%84%E5%AF%BC%E8%87%B4%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E5%81%B6%E5%8F%91%E5%B4%A9%E6%BA%83%E9%97%AE%E9%A2%98
```

末尾的 `链接` 行是工单在文档站的直达地址（docsify 的 `#/bugreports/<大类>?id=<标题锚点>`），由 `DOCS_SITE_BASE_URL` 与标题锚点拼成；`DOCS_SITE_BASE_URL` 留空时不输出该行。

注：群通知的**固定文案不随站内术语变化**（站内统一用「工单」），仍为 `[问题汇报提醒]` 与 `收到新的反馈报告`。

新工单保存成功后才会调用 LLBot。通知请求超时或 LLBot 返回失败时，工单仍会保留，
接口返回的 `notification` 会标明各群状态（如 `{"admin": "sent", "main": "failed"}`），
错误会写入 `bugreport/server.log`。
