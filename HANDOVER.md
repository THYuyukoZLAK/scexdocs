# SCEX DOCS 项目交接文档

本文面向后续开发者和运维人员，说明 SCEX DOCS 的组成、运行方式、常用配置、工单系统及维护注意事项。

## 1. 项目概述

SCEX DOCS 包含两个部分：

1. 基于 docsify 的静态 Markdown 文档站。
2. 可通过 iframe 嵌入文章的工单提交页，以及负责写入 Markdown 和发送 QQ 群提醒的 Python API。

整体请求流如下：

```text
浏览器
  |
  v
nginx :8880
  |-- /、/docs/*、/js/*、/styles.css  -> 静态文件 / docsify
  |-- /bugreport/*                    -> 工单前端
  |-- POST /api/bugreport             -> Python API :8881
                                              |-- 追加到 docs/bugreports/category-*.md
                                              |-- 重建 docs/bugreports/README.md 索引
                                              `-- 调用 LLBot /send_group_msg
```

项目没有前端构建步骤，也不依赖 npm。工单 API 只使用 Python 3 标准库。

## 2. 运行环境

### Windows

- Windows 10/11 或 Windows Server。
- Python 3，并能通过 `py -3` 或 `python` 调用。
- 项目已在 `nginx/` 内附带 Windows 版 nginx。
- PowerShell，用于停止 Python API 进程。

### Linux

- Python 3。
- 系统 nginx，或放置在 `nginx-linux/sbin/nginx` 的项目内 nginx。
- `bash`、`sed`、`ss` 等常用系统工具。
- nginx 运行用户必须能读取项目文件；启动 API 的用户必须能写入 `docs/bugreports/`。

默认端口：

| 服务 | 监听地址 | 默认端口 | 说明 |
| --- | --- | --- | --- |
| nginx | 所有网卡 | `8880` | 文档站及统一入口 |
| 工单 API | `127.0.0.1` | `8881` | 仅供本机 nginx 反向代理 |
| LLBot | 由 LLBot 决定 | 当前配置见 `server.py` | OneBot v11 正向 HTTP 服务 |

## 3. 目录结构

```text
scexdocs/
├── index.html                    # docsify 入口与插件配置
├── styles.css                   # 文档站全局主题
├── _sidebar.md                  # 历史/根侧栏；当前站点主要使用 docs/_sidebar.md
├── HANDOVER.md                  # 本交接文档
├── DEPLOY.md                    # 基础部署说明
├── start-server.bat             # Windows 启动脚本，必须保持纯 ASCII
├── stop-server.bat              # Windows 停止脚本，必须保持纯 ASCII
├── start-server.sh              # Linux 启动脚本
├── stop-server.sh               # Linux 停止脚本
├── docs/
│   ├── README.md                # 文档站首页
│   ├── _sidebar.md              # 当前 docsify 实际使用的侧栏
│   ├── _coverpage.md            # 封面内容；需在 docsify 中启用 coverpage 才会显示
│   ├── skill-webstyle.md        # 页面配色与组件规范
│   ├── bugreports/              # 工单公开文档（由 server.py 自动维护）
│   │   ├── README.md            # 工单索引，每次提交后自动重建
│   │   ├── category-1.md        # 整合包侧「须臾」全部工单
│   │   ├── category-2.md        # 创造养老侧「永远」全部工单
│   │   └── category-3.md        # 怀旧向子服「旧梦」全部工单
│   └── *.md                     # 普通文章
├── js/
│   ├── docsify.min.js           # 本地化 docsify
│   ├── search.min.js            # 搜索插件
│   ├── zoom-image.min.js        # 图片缩放插件
│   ├── docsify-copy-code.min.js # 复制代码插件
│   ├── jetbrains-mono.css       # 字体声明
│   └── *.woff2 / 图片           # 字体和图片资源
├── bugreport/
│   ├── index.html               # 工单提交表单
│   ├── styles.css               # 工单提交页样式
│   ├── app.js                   # 前端校验和提交逻辑
│   ├── server.py                # Markdown API 与 OneBot 通知
│   ├── test_server.py           # OneBot 通知单元测试
│   └── README.md                # 工单子系统说明
├── nginx/
│   ├── nginx.exe               # Windows nginx
│   ├── conf/nginx.conf         # Windows 实际配置
│   └── logs/                   # Windows 访问日志和错误日志
└── deploy/
    └── nginx.conf.template     # Linux 动态配置模板
```

`.nojekyll` 用于阻止静态托管平台忽略下划线开头的 docsify 文件，不应删除。

## 4. 启动和停止

### Windows

在项目根目录双击或执行：

```bat
start-server.bat
```

脚本会：

1. 检查 `8880` 和 `8881` 是否被占用。
2. 查找并验证 Python 3。
3. 启动 `bugreport/server.py`，将 PID 写入 `bugreport/server.pid`。
4. 启动项目内 nginx。

停止服务：

```bat
stop-server.bat
```

Windows 批处理脚本刻意只使用 ASCII 字符。不要向 `.bat` 文件加入中文输出或将其转换为依赖代码页的编码，否则 `cmd.exe` 可能在执行 `chcp` 之前错误解析文件。

### Linux

首次使用确保脚本可执行：

```bash
chmod +x start-server.sh stop-server.sh
./start-server.sh
```

停止服务：

```bash
./stop-server.sh
```

Linux API 标准输出和错误会追加到 `bugreport/server.log`。Windows 启动时则直接显示在启动控制台。

### 访问地址

- 文档站：`http://服务器地址:8880/`
- 工单提交页：`http://服务器地址:8880/bugreport/`
- 工单 API：`POST http://服务器地址:8880/api/bugreport`

不要直接向公网开放 `8881`。生产环境如需 HTTPS，应在本项目 nginx 之前使用已有 HTTPS 反向代理，或自行补充证书配置。

## 5. 文档站配置

### docsify 入口

`index.html` 内的 `window.$docsify` 是主配置。当前关键项：

| 配置 | 当前作用 |
| --- | --- |
| `basePath: 'docs/'` | 所有文章默认从 `docs/` 加载 |
| `loadSidebar: true` | 加载 `docs/_sidebar.md` |
| `auto2top: true` | 切换文章后回到顶部 |
| `subMaxLevel: 2` | 侧栏生成到二级标题 |
| `maxLevel: 4` | Markdown 标题最大解析层级 |
| `search` | 本地全文搜索配置 |
| `copyCode` | 代码复制按钮文字 |

项目资源已本地化，不需要外部 CDN。修改 JS/CSS 后如浏览器仍使用旧文件，可提升 `index.html` 资源 URL 后的版本号，例如将 `?v=2` 改为 `?v=3`。

### 新增或修改文章

1. 在 `docs/` 下创建小写英文文件名的 `.md` 文件。
2. 使用一个一级标题，以二级标题组织主要章节。
3. 在 `docs/_sidebar.md` 中加入相对链接。
4. 使用启动脚本预览，不要直接双击 `index.html`。
5. 检查桌面端、窄屏、站内链接和图片路径。

示例：

```markdown
- 文档维护

  - [服务器使用指南](server-guide.md)
```

由于 `basePath` 指向 `docs/`，当前真正生效的是 `docs/_sidebar.md`，不是根目录 `_sidebar.md`。如果保留两份侧栏，修改导航时建议同步更新，避免以后调整 `basePath` 时出现旧菜单。

### 样式修改

- 文档站样式：修改根目录 `styles.css`。
- 工单提交页样式：修改 `bugreport/styles.css`。
- 设计规范：参考 `docs/skill-webstyle.md`。
- 字体入口：`js/jetbrains-mono.css`。

主配色约定：

| 用途 | 色值 |
| --- | --- |
| 页面背景 | `#022335` |
| 面板背景 | `#093750` |
| 表单强调色 | `#1985a1` |
| 标题文字 | `#d2f7fd` |
| 正文文字 | `#abc0ca` |
| 边框 | `#0f5377` |

通用样式应写入对应 CSS 文件，不要在单篇文章内复制整套样式。

## 6. 工单系统

### 前端

工单提交页可直接访问，也可以嵌入文章：

```html
<iframe
  src="/bugreport/"
  title="工单提交"
  width="100%"
  height="620"
  loading="lazy">
</iframe>
```

表单字段包括：

- 服务器大类。
- 类型：BUG、新功能申请、其他，三者互斥。
- 标题。
- 详细内容。
- 提交者 Minecraft ID。

`app.js` 会向 `/api/bugreport` 发送 JSON。浏览器校验只是用户体验措施，真正的安全校验在 `server.py` 中完成。

### API 与工单文件

`server.py` 默认只监听 `127.0.0.1:8881`，nginx 将外部的 `/api/bugreport` 转发到该服务。

服务端限制包括：

- 请求正文最大 `64 KiB`。
- 标题为 1 至 100 个字符且不能换行。
- 内容为 1 至 10000 个字符。
- Minecraft ID 为 3 至 16 位字母、数字或下划线。
- 单个来源地址十分钟最多成功进入保存流程 5 次。
- 隐藏蜜罐字段用于过滤简单机器人。

工单编号格式：

```text
YYYYMMDD-HHMMSS-随机八位十六进制
```

工单按子服务器合并保存：同一大类的所有工单都追加到 `docs/bugreports/category-*.md`（**一个子服务器一个文件**），新工单插入文件顶部，因此文件内按时间倒序排列。每次写入后还会重建索引页 `docs/bugreports/README.md`。

正文按纯文本处理：`quote_body()` 会给每个换行补两个行尾空格（CommonMark 硬换行），因为提交者通常不熟悉 Markdown，单个换行在 Markdown 中会被合并成空格；空行仍作为段落分隔。调整正文渲染格式时改 `quote_body()` 即可（已落盘的历史正文不会自动重排，必要时一次性批量改写）。

由于 `docs/bugreports/` 位于 docsify 的 `basePath`（`docs/`）下，工单内容会随文档站公开，可通过「服务器运维 → 工单记录」直接查阅，因此 nginx 不再对工单做访问限制。如需手动重建索引，可执行 `python bugreport/server.py --rebuild-index`。

工单文件属于文档站内容；如需保留历史快照，迁移或重装服务器前仍建议单独备份整个 `docs/bugreports/`。

限流状态保存在内存中，重启 API 后会清空。当前没有登录、验证码或持久化队列，若接口公开在互联网上，应结合上游防火墙或反向代理继续限制访问频率。

### 修改服务器大类

服务器大类必须同时修改两处：

1. `bugreport/index.html` 中 `<option>` 的显示文字。
2. `bugreport/server.py` 中 `CATEGORY_LABELS` 的可信映射。

建议保留稳定的 `category-1`、`category-2`、`category-3` 值和目录名，只修改显示名称。服务端不会信任浏览器提交的显示名称，QQ 群提醒也使用 `CATEGORY_LABELS`。

如果确实要新增第四类，还需：

1. 在前端增加 `<option value="category-4">`。
2. 在 `CATEGORY_LABELS` 增加 `category-4`。
3. 为 `category-4` 准备 `docs/bugreports/category-4.md`（可留空，首次提交时会自动创建）。
4. 确认新大类的工单文件与索引能被正常重建。

### 修改工单类型

同步修改：

- `bugreport/index.html` 中单选按钮的 `value` 和显示文字。
- `bugreport/server.py` 中 `TYPE_LABELS`。
- 如需新颜色，修改 `bugreport/styles.css` 对应的选中状态。

## 7. LLBot / OneBot v11 群提醒

在 LLBot 中启用 OneBot v11 正向 HTTP 服务。然后修改 `bugreport/server.py` 顶部的配置：

```python
ONEBOT_HTTP_URL = "http://127.0.0.1:3002"
ONEBOT_ADMIN_GROUP_ID = "978225175"
ONEBOT_MAIN_GROUP_ID = "362344872"
ONEBOT_ACCESS_TOKEN = "your-secret-token"
ONEBOT_TIMEOUT_SECONDS = 5
DOCS_SITE_BASE_URL = "http://scex.aerohakugyokurou.top:8880"
```

配置说明：

| 变量 | 说明 |
| --- | --- |
| `ONEBOT_HTTP_URL` | LLBot HTTP 根地址，也可填写以 `/send_group_msg` 结尾的完整地址；留空则整体禁用 |
| `ONEBOT_ADMIN_GROUP_ID` | 管理群群号（内部处理用），使用字符串填写；留空则跳过该目标 |
| `ONEBOT_MAIN_GROUP_ID` | 主群群号（面向玩家公示），使用字符串填写；留空则跳过该目标 |
| `ONEBOT_ACCESS_TOKEN` | 与 LLBot 一致的 token；为空时不发送 Authorization 头 |
| `ONEBOT_TIMEOUT_SECONDS` | 通知请求超时秒数 |
| `DOCS_SITE_BASE_URL` | 文档站根地址；主群通知会附上工单直达链接，留空则不带链接 |

两个群各收到一条独立通知：群号留空即跳过，其中一个发送失败也不影响另一个。全部留空时禁用提醒。

通知内容格式：

```text
# 管理群
[问题汇报提醒]
时间戳：2026-08-31T16:25:31+08:00
标题：区块加载异常
服务器大类：怀旧向子服「旧梦」

# 主群
收到新的反馈报告
2026-08-31T16:25:31+08:00
主题：区块加载异常
所属 怀旧向子服「旧梦」
链接：http://scex.aerohakugyokurou.top:8880/#/bugreports/category-3?id=%E5%8C%BA%E5%9D%97%E5%8A%A0%E8%BD%BD%E5%BC%82%E5%B8%B8
```

消息通过 OneBot v11 `/send_group_msg` 发送，并设置 `auto_escape=true`，因此标题中的 CQ 码不会被解析。

注：群通知的**固定文案不随站内术语变化**（站内统一用「工单」），仍为 `[问题汇报提醒]` 与 `收到新的反馈报告`。

主群那条末尾的 `链接` 是工单在文档站的直达地址：`{DOCS_SITE_BASE_URL}/#/bugreports/{大类键}?id={锚点}`。锚点由 `docsify_anchor()` 复刻 docsify 5.x 的 `Docsify.slugify()` 得出；因为新工单总是插在子服务器文件最前面，它不会带上 `-1` 之类的重名后缀。修改标题清洗规则时需同步参考 docsify 版本。

工单会先写入磁盘，再调用 LLBot。即使 LLBot 离线、token 错误或请求超时，工单仍会保留；接口返回的 `notification` 为对象（如 `{"admin": "sent", "main": "disabled"}`），任一目标失败时页面会提示「群聊提醒发送失败」。当前没有自动重试机制，应在日志中搜索 `[OneBot]` 排查。

`ONEBOT_ACCESS_TOKEN` 是明文源码配置。不要把包含真实 token 的 `server.py` 推送到公开仓库或发送给无关人员；交接副本应先清空 token。

修改配置后必须重启服务才能生效。

## 8. nginx 配置

项目有两份 nginx 配置源：

| 平台 | 文件 | 使用方式 |
| --- | --- | --- |
| Windows | `nginx/conf/nginx.conf` | nginx 直接读取 |
| Linux | `deploy/nginx.conf.template` | `start-server.sh` 替换根目录、MIME 路径和端口后生成临时配置 |

修改 API 路由、缓存规则或访问控制时必须同步修改这两份文件。

重要路由：

| location | 作用 |
| --- | --- |
| `= /api/bugreport` | 仅允许 POST，转发到 `127.0.0.1:8881` |
| `~* \.md$` | 设置 `text/markdown` 并禁用强缓存（含 `docs/bugreports/*.md`） |
| `~* \.(html?|css|js)$` | 禁止强缓存频繁修改的前端文件 |
| 图片和字体规则 | 缓存一天 |
| `/` | 仅返回存在的文件或目录 |

### 修改 Web 端口

- Windows：同时修改 `start-server.bat` 的 `PORT` 和 `nginx/conf/nginx.conf` 的 `listen`。
- Linux：执行 `PORT=9000 ./start-server.sh`，脚本会替换模板中的 `8880`。
- 同时更新防火墙和上游反向代理。

### 修改 API 端口

当前 API 端口固定为 `8881`。修改时需要同步：

1. `server.py` 的 `--port` 默认值，或启动脚本传入 `--port`。
2. 两份 nginx 配置中的 `proxy_pass`。
3. Windows/Linux 启动脚本的端口占用检查。

## 9. 测试与发布前检查

### 自动检查

在项目根目录执行：

```powershell
python -B -m unittest bugreport.test_server -v
```

该测试会模拟 OneBot 响应，不会真的向 QQ 群发消息。

如果安装了 Node.js，可检查前端脚本语法：

```powershell
node --check bugreport/app.js
```

Windows nginx 配置检查：

```powershell
.\nginx\nginx.exe -p .\nginx\ -c conf\nginx.conf -t
```

### 手工检查

1. 运行启动脚本。
2. 打开 `/`，确认首页、侧栏、搜索和文章切换正常。
3. 打开 `/bugreport/`，确认三种类型按钮互斥。
4. 提交测试工单，确认页面显示工单编号。
5. 检查对应子服务器页面（`docs/bugreports/category-*.md`）是否新增了工单，且索引页已刷新。
6. 启用 LLBot 时确认管理群与主群分别收到对应格式的提醒。
7. 打开「工单记录」页面，确认能从索引跳转到各子服务器页面。
8. 删除测试工单。
9. 运行停止脚本，并确认 `8880`、`8881` 已释放。

### 发布前清单

- [ ] `server.py` 中的 LLBot 地址、群号和 token 适用于目标服务器。
- [ ] 未向公开仓库提交真实 token。
- [ ] `docs/bugreports/` 已备份且目标用户有写权限。
- [ ] Windows 两个 `.bat` 仍为纯 ASCII。
- [ ] Windows 与 Linux nginx 路由保持一致。
- [ ] 新文章已加入 `docs/_sidebar.md`。
- [ ] 防火墙仅开放需要的 Web 端口，没有开放 `8881`。
- [ ] 自动检查和手工提交流程通过。

## 10. 日志、备份与恢复

| 内容 | Windows | Linux |
| --- | --- | --- |
| nginx 访问日志 | `nginx/logs/access.log` | 当前模板关闭访问日志 |
| nginx 错误日志 | `nginx/logs/error.log` | nginx 启动终端/系统日志 |
| API 日志 | Windows 启动控制台 | `bugreport/server.log` |
| API PID | `bugreport/server.pid` | `bugreport/server.pid` |
| 工单数据 | `docs/bugreports/` | `docs/bugreports/` |

备份至少应包含：

- 整个 Git 项目或代码发布包。
- `docs/bugreports/` 中的工单文件与索引。
- 当前部署使用的 `server.py` OneBot 配置，或单独记录配置值。
- 外层 HTTPS 反向代理和防火墙配置（若有）。

恢复时先放回代码和工单，确认目录权限，再启动服务并完成一次测试提交。

## 11. 常见故障

### Windows 批处理提示语法错误或乱码

- 确认 `start-server.bat`、`stop-server.bat` 只含 ASCII。
- 不要向文件中加入中文注释或中文 `echo`。
- 从 `cmd.exe` 运行脚本以查看完整错误，不要只观察一闪而过的窗口。

### 提示端口已占用

Windows：

```powershell
netstat -ano | findstr ":8880"
netstat -ano | findstr ":8881"
```

Linux：

```bash
ss -ltnp | grep -E ':8880|:8881'
```

先确认进程归属，不要直接终止未知进程。

### 文档首页正常，但文章无法加载

- 确认文章位于 `docs/`。
- 检查 `docs/_sidebar.md` 路径和大小写。
- 检查 nginx 对 `.md` 返回 `text/markdown`。
- 查看浏览器开发者工具中的 404 请求。

### 表单显示，但提交失败

- 确认 Python API 正在监听 `127.0.0.1:8881`。
- 查看 nginx 错误日志是否出现 `connect() failed`。
- 确认 `docs/bugreports/` 可写。
- 检查请求是否超过 `64 KiB` 或字段校验限制。

### 工单已保存，但 QQ 群没有提醒

- 确认 LLBot 已登录且启用了 OneBot v11 正向 HTTP。
- 检查 `ONEBOT_HTTP_URL` 端口和 `/send_group_msg` 路径。
- 检查群号、机器人群成员状态和 access token。
- 查看 API 日志中的 `[OneBot]` 错误。
- 从部署机器直接调用 LLBot HTTP 地址，确认没有防火墙阻断。

### 修改 CSS/JS 后页面没有变化

- 强制刷新浏览器。
- 提升 `index.html` 中对应资源的 `?v=` 版本。
- 确认修改的是文档站 `styles.css` 还是 `bugreport/styles.css`。

## 12. 当前设计限制

- 工单使用 Markdown 文件而非数据库，不适合高并发或复杂检索。
- 限流只保存在内存中，重启即清空。
- 表单没有账号认证和验证码。
- OneBot 通知失败不会自动重试。
- Windows nginx 是开发/轻量部署方案；长期生产运行建议使用 Linux nginx 或统一的服务管理器。
- LLBot token 当前保存在 Python 源码中，需要严格控制仓库和服务器文件权限。

交接前，原维护者应说明目标服务器地址、外层反向代理、LLBot 运行位置、工单备份位置，以及真实凭据由谁保管；敏感值不要写入本文。
