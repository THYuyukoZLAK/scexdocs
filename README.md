# SCEX DOCS

SCEX 项目文档与技术资料站，基于 [docsify](https://docsify.js.org/) 的纯静态站点：仓库根目录即站点根目录，页面为 `docs/` 下的 Markdown，浏览器端实时渲染，无需构建。

## 目录结构

```
.
├── index.html            # 站点入口，配置 docsify（basePath: docs/）
├── styles.css            # 站点主题样式
├── _sidebar.md           # 侧边栏（根级）
├── docs/                 # 所有文档页面
│   ├── README.md         # 首页
│   ├── _sidebar.md       # 文档侧边栏
│   ├── _coverpage.md     # 封面页
│   ├── bugreports/       # 工单分类页
│   └── *.md              # 各栏目页面
├── js/                   # docsify 与插件、字体、图片（本地化，不依赖 CDN）
├── bugreport/            # 工单上报服务（Python + 前端页面）
├── deploy/               # 部署配置模板 nginx.conf.template
├── start-server.bat/.sh  # 启动脚本（调用项目内 nginx）
├── stop-server.bat/.sh   # 停止脚本
├── recover.ps1           # Windows 定时健康检查/恢复脚本
├── HANDOVER.md           # 交接说明
├── DEPLOY.md             # 部署说明
└── agents_mem.md         # 环境与运维备忘
```

## 本地预览

docsify 通过 `fetch` 加载 Markdown，**不能**直接用 `file://` 打开 `index.html`，需要任意静态 HTTP 服务：

```bash
# 方式一：Python
python -m http.server 8880 --directory .

# 方式二：Node.js
npx serve -l 8880 .
```

然后访问 <http://127.0.0.1:8880/>。

> 生产环境由项目自带 nginx 提供服务（默认 8880 端口），见 `DEPLOY.md`。

## 版本库说明

以下内容因体积大或含运营数据，**未纳入版本库**（见 `.gitignore`）：

- `nginx/`：Windows 版 nginx 发行包与运行日志；Linux 部署请使用 `deploy/nginx.conf.template`；
- `*.log`：访问日志含真实客户端 IP、会话与 CSRF token；
- `backups/`、`*.bak-*`：历史备份副本。

因此克隆后直接运行 `start-server.bat` / `start-server.sh` 会因缺少 `nginx/` 而失败，需自行准备 nginx 运行时。

## GitHub Pages

仓库根目录含 `.nojekyll`，可直接用 Pages 托管：Settings → Pages → 部署分支选 `main`、目录选 `/ (root)`。

## 许可

[MIT](LICENSE) © 2026 西行寺夜和 / THYuyukoZLAK
