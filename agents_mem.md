# agents_mem - SCEX 文档站 + 工单系统

> 工作区根目录：`f:\.C1_Dev`
> 上级总览：`../agents_mem.md`　|　本文件是 **scexdocs/** 的详细备忘（定位 / 结构 / 构建 / 状态 / 坑）。
> 最后更新：2026-10-04（从根目录 `agents_mem.md` 拆分而来）

> 📝 **术语（2026-10-04 起统一为「工单」）**：索引页标题 `# 工单记录`、页头「本页由工单系统自动维护」、字段 `工单编号`、小节 `#### 工单内容`、侧栏「提交工单 / 工单记录」。⚠️ **QQ 群通知文案是唯一例外，刻意不改**（仍为 `[问题汇报提醒]` / `收到新的反馈报告`）。**路径与 URL 未变**（`bugreport/`、`/bugreport/`、`/api/bugreport`、`docs/bugreports/`），代码内部标识符也仍是 `report_*`。本节以下文字保留早期用词（问题汇报/报告），指的是同一套东西。

### 8.1 定位
**SCEX（Space Creator EX.）Minecraft 模组服务器社群的文档站**：docsify 静态站 + 一个可 iframe 嵌入的**问题汇报**子系统。

- 文档站：`scex.aerohakugyokurou.top:8880`　游戏服：`scex.aerohakugyokurou.top:25566`
- 三个子服（= 汇报分类）：`category-1` 整合包侧「须臾」/ `category-2` 创造养老侧「永远」/ `category-3` 怀旧向子服「旧梦」
- 运营：`THYuyukoZLAK`（web 服务）、`Magellan67`（「旧梦」+ 群 bot）、`atsuirizi`（社群）、`Creepercdn`（技术支持）；QQ 群 `362344872`
- 版权：代码 MIT / 内容 CC-BY-SA 4.0

### 8.2 架构

```text
浏览器 → nginx :8880
  ├─ / , /docs/* , /js/* , /styles.css   → docsify 静态
  ├─ /bugreport/*                        → 汇报前端
  └─ POST /api/bugreport                 → Python API :8881
                                             ├─ 追加到 docs/bugreports/category-*.md（一子服务器一文件）
                                             ├─ 重建 docs/bugreports/README.md 索引
                                             └─ LLBot /send_group_msg 通知 QQ 群
```

无前端构建、无 npm；API **只用 Python 3 标准库**。

### 8.3 关键路径

| 路径 | 说明 |
|---|---|
| `index.html` | docsify 入口；`window.$docsify` 已配 `basePath:'docs/'`、`loadSidebar:true`、`onlyCover:false`、`search`、`copyCode`；本地插件 + 自定义代码行号插件 |
| `styles.css` | 文档站主题（SCEX docsify theme） |
| `_sidebar.md`（根） | ⚠️ **不生效**——`basePath` 指向 `docs/`，真正生效的是 `docs/_sidebar.md` |
| `docs/` | 15 个 `.md` + `bugreports/`（工单公开文档），见 §8.4 |
| `js/` | 本地化 docsify + `search` / `zoom-image` / `copy-code` 插件 + `jetbrains-mono.css` + woff2 |
| `bugreport/` | 工单子系统：`index.html`、`app.js`、`styles.css`、`server.py`、`test_server.py`（工单本体不在此目录，见 `docs/bugreports/`） |
| `nginx/` | Windows nginx（`nginx/docs/CHANGES` 首行 = **1.30.4**）；`conf/nginx.conf` 监听 **8880**、`root ../`（= 项目根） |
| `deploy/nginx.conf.template` | Linux 变体（`root @ROOT@` / `include @MIME@` / `error_log stderr` / `access_log off`），由 `start-server.sh` 用 `sed` 渲染 |
| `recover.ps1` + `recovery.log` | **看门狗，不是数据恢复**：每 5 分钟查 8880/8881，掉了就拉起。日志 12 条，最后一次 2026-09-29 20:55 |
| `backups/` | 8 个时间戳快照（`uplog.md`/`_sidebar.md`/同步脚本/计划任务 XML），集中在 2026-08-31 迁移日 + 09-04 |
| `scexdocs.zip` | 项目打包副本 |
| `.nojekyll` | 阻止静态托管忽略下划线开头的 docsify 文件，**不要删** |

### 8.4 `docs/` 内容（15 个文件）

**真实内容**：`README.md`（首页）、`about-subservers.md`（三子服）、`notice.md`（规则 + 管理组名单）、`prepare.md`（首次准备）、`boot-sync.md`、`askquestion.md`（转载《提问的智慧》≈64 KB）、`updates-legacy.md`（「旧梦」更新日志，到 1.0.37）、`uplog.md`、`adding-pages.md`（维护指南）、`skill-webstyle.md`（**深蓝青色样式规范 —— 已抽成工作区技能 `scex-webstyle`**）、`report.md`（内嵌 `/bugreport/` 的 iframe）。
**脚手架/测试**：`_sidebar.md`、`_coverpage.md`（**coverpage 未启用，不显示**）、`testpage.md`、**空文件** `bugs.md`。
**汇报公开文档（2026-10-04 起）**：`bugreports/` —— `README.md`（索引）+ `category-{1,2,3}.md`（每子服务器一个文件），由 `server.py` 自动维护。

### 8.5 问题汇报 API（`bugreport/server.py`）

- 只接受 `POST /api/bugreport`；`Content-Type` 必须 `application/json`；体积 0 或 > **64 KiB** → 413。
- 请求 `{category, type, title, content, reporter, website}`；`website` 是**蜜罐**（命中返回 `200 {"id":"received"}` 静默丢弃）。
- 校验：标题 1–100 且无换行；内容 1–10000；Minecraft ID `^[A-Za-z0-9_]{3,16}$`；**单 IP 10 分钟最多成功 5 次**（限流状态在内存，重启即清空）。
- 成功 `201 {"id":"<报告编号>","notification":"sent|disabled|failed"}`。
- 落盘（**2026-10-04 起**）：**一个子服务器一个文件** `docs/bugreports/category-{1,2,3}.md`，新报告插到文件**顶部**（文件内时间倒序），内容是 **Markdown 表格 + `> ` 引用正文**（**无** YAML front-matter）；每次提交后自动重建索引页 `docs/bugreports/README.md`（各子服务器报告表 + 链接）。手动重建：`python bugreport/server.py --rebuild-index`。正文由 `quote_body()` 渲染：**每个换行补两个行尾空格**（CommonMark 硬换行，因提交者按纯文本书写），行尾空白归一化，空行保留为 `>`。
- 报告位于 docsify `basePath`（`docs/`）下 → **随文档站公开**，从「服务器运维 → 问题汇报记录」可查阅；因此 nginx **不再**对报告做 403 限制（旧 `location ^~ /bugreport/reports/` 规则已删除）。
- ⚠️ **旧实现（已废弃）**：「一报告一文件」存 `bugreport/reports/category-*/`，被 `.gitignore` 忽略、nginx 返回 403。现已整体迁移，报告**纳入文档站版本管理**。
- ⚠️ **无登录、无验证码、无限流持久化**；`8881` **绝不能**直接暴露公网。
- 当前已有 **12 份报告**（category-1: 2、category-2: 1、category-3: 9），最后一份 2026-09-26。
- `test_server.py` **只覆盖** `send_onebot_notification` 的 2 个用例（**不覆盖**路由 / 校验 / 限流 / 写盘）。

### 8.6 LLBot / OneBot v11 通知（**双群**）

```python
ONEBOT_HTTP_URL        = "http://127.0.0.1:3002"   # 备份文件里是 3456
ONEBOT_ADMIN_GROUP_ID  = "978225175"   # 管理群
ONEBOT_MAIN_GROUP_ID   = "362344872"   # 主群
ONEBOT_ACCESS_TOKEN    = ""                        # 当前为空
ONEBOT_TIMEOUT_SECONDS = 5
DOCS_SITE_BASE_URL     = "http://scex.aerohakugyokurou.top:8880"   # 通知里的报告链接前缀
```

`POST {url}/send_group_msg`，body `{group_id:int, message:"…", auto_escape:true}`；token 非空才带 `Authorization: Bearer`。
两个群**各自独立**发送：群号留空即跳过，其中一个失败不影响另一个；`ONEBOT_HTTP_URL` 留空则整体禁用。

- 管理群（`admin_message()`）：`[问题汇报提醒]` / `时间戳：…` / `标题：…` / `服务器大类：…`
- 主群（`main_group_message()`）：`收到新的反馈报告` / `{时间戳}` / `主题：{标题}` / `所属 {大类}` / `链接：{文档站直达链接}`
- 链接由 `report_link()` 拼成：`{DOCS_SITE_BASE_URL}/#/bugreports/{大类键}?id={锚点}`；锚点用 `docsify_anchor()` 复刻 docsify 5.x 的 `Docsify.slugify()`（去 markdown 链接/HTML/emoji、`[A-Z]+` 转小写、剥 `\u2000-\u206F`/`\u2E00-\u2E7F`/ASCII 标点、空格转 `-`、首位数字前加 `_`）。新报告总在文件顶部 → 无 `-1` 重名后缀。**已用真实页面 12/12 核对 id 一致且全部能被 `querySelector` 命中**；`DOCS_SITE_BASE_URL` 留空则不输出链接行。

**先落盘再通知**；通知失败报告仍保留、**无重试**，日志搜 `[OneBot]`。接口返回 `notification` 为对象（如 `{"admin":"sent","main":"disabled"}`）。

### 8.7 运行

```powershell
cd f:\.C1_Dev\scexdocs
.\start-server.bat      # Windows：查 8880/8881 占用 → 起 API（PID 写 bugreport\server.pid）→ 起 nginx
.\stop-server.bat
# 文档站 http://<host>:8880/ ；汇报页 /bugreport/ ；API POST /api/bugreport
```

Linux：`./start-server.sh` / `./stop-server.sh`（`PORT=9000 ./start-server.sh` 可换端口）。

`HANDOVER.md` §9 的发布前检查：

```powershell
python -B -m unittest bugreport.test_server -v
node --check bugreport/app.js
.\nginx\nginx.exe -p .\nginx\ -c conf\nginx.conf -t
```

### 8.8 状态与坑

- ⚠️ **`start-server.bat` / `stop-server.bat` 必须保持纯 ASCII**（HANDOVER 写明原因：向 `.bat` 加中文或在 `chcp` 前依赖代码页，`cmd.exe` 会错误解析文件）。
- 📌 **docsify 链接解析铁律（本仓 `basePath='docs/'`，实测）**：Markdown 链接一律**相对 `docs/` 解析**，**不是**相对当前页面目录。
  - `docs/bugreports/README.md` 里写 `[x](category-1.md)` 会被解析成 `#/category-1`（**404**）→ 必须写 `bugreports/category-1.md`（由 `server.py::rebuild_index()` 生成）。
  - 指向站外子应用的链接会被改写为 hash 死路由（`/bugreport/` → `#/bugreport/`）→ 必须用**原生锚点** `<a href="/bugreport/" target="_blank" rel="noopener">…</a>`（见 `server.py::report_form_link()`）。
  - 嵌套路由会额外请求 `<页面目录>/_sidebar.md` 并 404（自动回退 `docs/_sidebar.md`），**属正常**；侧栏链接在嵌套路由下仍正确（侧栏按 `docs/` 解析）。
  - 受 `subMaxLevel: 2` 影响，报告标题用 `###`（h3），只有分类文件顶部的 `#` 与索引页的 `##` 会进侧栏。
- ⚠️ 改路由/缓存/访问控制要**同步改两份** nginx 配置（Windows `nginx/conf/nginx.conf` + Linux `deploy/nginx.conf.template`）。
- ⚠️ 改 Web 端口要同步 `start-server.bat` 的 `PORT` 与 `nginx.conf` 的 `listen`；改 API 端口要同步 `server.py --port`、两份 nginx 的 `proxy_pass`、启动脚本的占用检查。
- ⚠️ 改大类/类型要**三处同步**：`bugreport/index.html` 的 `<option>`/单选 `value`、`server.py` 的 `CATEGORY_LABELS`/`TYPE_LABELS`、`bugreport/styles.css` 的选中态。新增第四类还需 `docs/bugreports/category-4.md`（可留空，首次提交自动创建）。
- ⚠️ **源机路径硬编码**：`recover.ps1` 里 `$root = 'E:\Minecarft\.F2_scexdocs'`（更早是 `d:\GHfile\scexdocs`）→ **换机后看门狗不可用，必须改**。配套计划任务 XML（`backups/recovery-20260904-125251/`）里又是**第三个**路径 `.F3_scex-website`，且 `<Enabled>false</Enabled>`。
- ⚠️ 日志时区是 **+0900（JST）**；nginx 最后一次活动 **2026-10-02 18:42**，`error.log` 停在 2026-09-29。
- ⚠️ 日志含大量公网扫描记录与**真实客户端 IP**（CensysInspect、MS17-010 探测、`/+CSCOE+/logon.html` 等），对外分享前应脱敏。

---

## 常用命令

```powershell
cd f:\.C1_Dev\scexdocs
.\start-server.bat     # 查 8880/8881 占用 → 起 API（PID 写 bugreport\server.pid）→ 起 nginx
.\stop-server.bat
# 文档站 http://<host>:8880/ ；工单页 /bugreport/ ；API POST /api/bugreport

# 发布前检查
python -B -m unittest bugreport.test_server -v
node --check bugreport\app.js
.\nginx\nginx.exe -p .\nginx\ -c conf\nginx.conf -t

# 手动重建工单索引
python bugreport\server.py --rebuild-index
```

Linux：`chmod +x start-server.sh stop-server.sh` → `./start-server.sh` / `./stop-server.sh`
（`PORT=9000 ./start-server.sh` 可换端口）。

---

## 敏感信息

| 位置 | 内容 | 处理建议 |
|---|---|---|
| `HooriForum/nginx/logs/access.log`、`scexdocs/nginx/logs/*.log` | 真实客户端 IP、会话/CSRF token（`confirm/…`、`logout?token=…`）、内部域名 | 属运营数据非密钥，但外发前应脱敏 |
| `scexdocs/bugreport/server.py` 的 `ONEBOT_ACCESS_TOKEN` | 交接副本里**已为空**（原那么本也无 token） | 迁移到新环境时重新填入即可，别回写进仓库 |
| 三个跨机项目的配置/脚本/日志 | **原机绝对路径**：`D:\GHfile\...`、`E:\Minecarft\.F1_nginx` / `.F2_scexdocs` / `.F3_scex-website`；主机名 `Monarch`、`DESKTOP-B36FCS0`、`DESKTOP-N7LN93G` | 非密钥，但暴露来源机器；换机后也是**直接失效点** |

> 跨项目的敏感项汇总见 `../agents_mem.md`。

---

## 更新记录

| 日期 | 变更 |
|---|---|
| 2026-10-04 | **`scexdocs/` 问题汇报改为「一个子服务器一个文件」**：存储由 `bugreport/reports/category-*/*.md`（一报告一文件）迁到 `docs/bugreports/category-{1,2,3}.md`，新报告插到文件顶部（时间倒序）；新增索引自动重建 `docs/bugreports/README.md` 与 `server.py --rebuild-index`（启动时也会重建）；两份 nginx 删除已失效的 `^~ /bugreport/reports/` 403 规则；`docs/_sidebar.md` 与 `docs/report.md` 增加「问题汇报记录」入口；`bugreport/.gitignore` 移除失效规则（报告改为随文档站公开/纳入版本管理）；HANDOVER.md、`bugreport/README.md` 同步。已验证：12 份报告迁移合并、单元测试 2 项通过、`nginx -t` 通过、端到端 POST（201/400/蜜罐）+ 静态页 200 `text/markdown` |
| 2026-10-04 | **`scexdocs/` 问题汇报新增「主群」通知**：`server.py` 拆出 `send_group_message()` / `admin_message()` / `main_group_message()` / `onebot_status_line()`；`ONEBOT_GROUP_ID` 拆为 `ONEBOT_ADMIN_GROUP_ID`（978225175 管理群）与 `ONEBOT_MAIN_GROUP_ID`（362344872 主群），两群**各自独立**发送（留空跳过、单群失败不影响另一群）；主群文案为「收到新的反馈报告 / 时间戳 / 主题：xx / 所属 xx」；接口 `notification` 由字符串改为对象 `{"admin":…,"main":…}`，`app.js` 同步。离线 mock 单测 2 → **5 项全过**（**未做真实 OneBot 联调**，本机无 OneBot 服务） |
| 2026-10-04 | **`scexdocs/` 主群通知新增报告直达链接**：新增 `DOCS_SITE_BASE_URL` 常量与 `docsify_anchor()` / `report_link()`（复刻 docsify 5.x `Docsify.slugify()`），主群通知末尾追加 `链接：{base}/#/bugreports/{大类}?id={锚点}`（`DOCS_SITE_BASE_URL` 留空则不输出）；`send_onebot_notification()` 第三参数改为**大类键**（显示名内部查 `CATEGORY_LABELS`）。离线单测 5 → **9 项全过**；锚点用真实 docsify 页面 **12/12 核对一致**、且全部能被 `querySelector('#id')` 命中 |
| 2026-10-04 | **`scexdocs/` 汇报正文强制硬换行**：新增 `quote_body()`——正文每行末尾补两个空格（CommonMark 硬换行）、行尾空白归一化、空行保留为 `>`；`render_report()` 改用它。一次性迁移已有正文（category-1/2/3 共 30 行）。离线单测 9 → **12 项全过**；浏览器实测 7 行正文渲染出 6 个 `<br>`（此前会被合并成一行） |
| 2026-10-04 | **`scexdocs/` 术语统一为「工单」**：`问题汇报系统→工单系统`、`问题汇报记录→工单记录`、`问题报告→提交工单`、`报告编号→工单编号`、`汇报内容→工单内容`、`汇报类型→工单类型`、`提交汇报→提交工单`（**QQ 群通知文案刻意不改**，仍为 `[问题汇报提醒]` 与 `收到新的反馈报告`）。改动：代码 `server.py`/`app.js`/`test_server.py`、表单页 `index.html`、静态页 `docs/report.md`、`docs/_sidebar.md`（→「提交工单/工单记录」）、`start-server.sh`、两份 nginx 注释、`HANDOVER.md`、`bugreport/README.md`；并迁移 12 份已有工单。**路径/URL/内部标识符（`report_*`）均未改**；历史备份 `server.py.bak-*` 保留旧词。离线单测 12/12 通过；浏览器实测索引/表单页/侧栏文案一致 |

