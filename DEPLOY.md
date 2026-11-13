# 部署到服务器

本文说明如何将 SCEX DOCS 文档站整体拷贝到服务器，并用项目自带的 nginx 提供服务（默认监听 `8880` 端口）。

## 项目自带内容

除文档本身外，项目目录内已包含部署所需的全部内容：

- `nginx/`：Windows 版 nginx 二进制与自定义配置（`nginx/conf/nginx.conf`）
- `start-server.bat` / `stop-server.bat`：Windows 启动与停止脚本
- `start-server.sh` / `stop-server.sh`：Linux 启动与停止脚本
- `deploy/nginx.conf.template`：Linux 部署用的配置模板

## Windows

1. 将整个项目文件夹拷贝到服务器任意位置（需连同 `nginx/` 目录一并拷贝）。
2. 运行 `start-server.bat`。
3. 浏览器访问 `http://服务器地址:8880`。
4. 停止服务运行 `stop-server.bat`。

## Linux

1. 安装 nginx：

   ```bash
   sudo apt install nginx
   ```

2. 将整个项目文件夹拷贝到服务器。
3. 运行启动脚本：

   ```bash
   chmod +x start-server.sh stop-server.sh
   ./start-server.sh
   ```

   脚本会优先使用项目内 `nginx-linux/sbin/nginx`（若有），否则回退到系统 nginx，并根据项目实际路径自动生成配置（监听 `8880` 端口）。

4. 停止服务运行 `./stop-server.sh`。

## 端口与配置

- 默认监听 `8880` 端口。
- 更换端口：Windows 下编辑 `nginx/conf/nginx.conf` 中的 `listen`；Linux 下可用环境变量 `PORT` 覆盖，例如 `PORT=9000 ./start-server.sh`。
- 站点根目录为项目根（即 `nginx` 目录的上一级），因此整个项目拷贝到任何位置均可直接运行，无需修改路径。

## 防火墙

请确保服务器防火墙放行对应端口：

```bash
sudo ufw allow 8880/tcp
```

## 注意事项

- 项目中的 `nginx/` 目录为 Windows 版二进制；若部署到 Linux 服务器，请改用系统 nginx 或自行放置 `nginx-linux/` 目录。
- docsify 默认使用 hash 路由（`#/`），无需配置 history 回退。
- `nginx.conf` 已为 `.md` 文件设置 `text/markdown` 类型，确保 docsify 能正常加载各页面。
