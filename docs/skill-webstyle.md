---
name: webstyle
description: 深蓝-青色「航空仪表/科学仪表」系网页样式风格指南。适用于 THYuyukoZLAK 的 SCEX 服务器生态系页面（aerohakugyokurou.top 主站、forum.hoorimanor.top/vote 投票系统、本地 voteproj 等）。用于快速为新页面套用统一配色、字体与组件样式。
---

# WebStyle Skill — 深蓝青色科技风（JetBrains Mono 仪表风）

本技能总结自以下已观测页面（2026-08-11）：

| 页面 | 说明 |
| --- | --- |
| `https://aerohakugyokurou.top/2023/06/17/mdguide.html` | 主站 markdown 备忘（Jekyll + Bootstrap 5.3.3 暗色） |
| `https://aerohakugyokurou.top/2022/08/19/guide.html` | 主站入服指南（同上） |
| `https://forum.hoorimanor.top/vote/` | 投票系统线上版（Bootstrap 3） |
| `http://127.0.0.1:8889/result.html` | 投票系统本地版（`voteproj/` 源） |

四个页面共享**同一套设计语言**：深蓝黑底色 + 青色高亮 + 等宽字体，整体呈「飞行仪表 / 科学设备 / 终端的冷色调」风格。

---

## 1. 核心设计语言

- **基调**：深色、低饱和、蓝黑背景上以青色作为唯一强调色。
- **气质**：冷静、科技感、控制台/仪表盘感。像 MC 服务器「周目记录 / 服务器状态」页面。
- **圆角**：整体偏好 **直角/极小圆角**（`border-radius: 0`），呈硬朗工业感；主站默认按钮为 Bootstrap 默认圆角。
- **图标**：尽量不要使用图标。
- **文字**：全站统一 `JetBrains Mono` 等宽字体；中文回退「思源黑体 CN / Sarasa Gothic SC」。
- **装饰细节**：主站链接 hover 有**青色自左向右填充背景**动画；表格行 hover 变青；代码块为**纯黑 + 白字 + 行号**。

---

## 2. 调色板（关键色值）

> 主站（Bootstrap 5 dark theme 变量）与投票系统（手写 CSS）共用同一色系，但强调色略有差异：主站 `#03a4fb`，投票系统 `#1985a1`。取两者可互换，按页面用途选用。

| 角色 | 色值 | 用途 |
| --- | --- | --- |
| 页面背景 | `#022335` | `body` / Bootstrap `--bs-body-bg` |
| 面板/导航背景 | `#093750` | 导航栏、卡片背景（`--bs-tertiary-bg` 附近） |
| 强调色（主站） | `#03a4fb` | 链接、激活项、填充按钮（`--bs-primary`） |
| 强调色（投票/表单） | `#1985a1` | 卡片左竖条、边框、选中态 |
| 强调色 hover | `#1a9bbe` / `#29b2fc` | 主按钮 hover |
| 标题/亮文本 | `#d2f7fd` | `h1~h6`、卡片标题、`--bs-heading-color` |
| 正文文本 | `#abc0ca` | 主体文字（`--bs-body-color`） |
| 弱化标签 | `#828282` | 表头、元信息、次级说明 |
| 分隔线/边框 | `#0f5377` | 输入框边框、标题下划线、表格分隔 |
| 行分隔线 | `#063145` | 表格行间细线 |
| 行 hover 背景 | `#0a3f5c` | 表格/列表行 hover |
| 成功/进行中 | `#00d68a`（投票徽章）/ `#198754`（主站 success） | 「进行中」状态 |
| 警示 | `#ffc107`（主站）/ `#a85a00`（div） | 警示 |
| 危险/错误 | `#dc3545`（主站）/ `#a80000`（投票错误/div） | 危险 |
| 信息 | `#0dcaf0` / `#008fa8` | 信息提示 |
| 代码块 | 黑 `#000` 底 + 白 `#fff` 字 | `pre` / `code` |
| 链接默认 | `#68c8fd`（暗色主题链接） | 正文链接 |

主站暗色主题等价变量：

```css
--bs-body-bg: #022335;
--bs-body-color: #abc0ca;
--bs-heading-color: #d2f7fd;
--bs-link-color: #68c8fd;
--bs-link-hover-color: #86d3fd;
--bs-primary: #03a4fb;
--bs-secondary: #abc0ca;
--bs-code-color: #e685b5;
--bs-border-color: #495057;
```

---

## 3. 字体与排版

**字体栈（两个站点一致）：**

```css
font-family: fontjmono, "JetBrains Mono", "思源黑体 CN", "Sarasa Gothic SC",
             "Source Han Sans SC", "Helvetica Neue", Helvetica, Arial, sans-serif;
```

- 正文大小：投票系统 `15px`；主站 Bootstrap `1rem`（根 16px）。
- JetBrains Mono 需加载 Regular/Bold/Italic/BoldItalic 四种 woff2（主站 `/font/` 自托管，或 Google Fonts）。

**标题规范（主站）：**

```css
h1, h2, h3, h4, h5, h6 {
  border-bottom: 1px solid;   /* 每个标题都有下划线 */
  margin-top: 2rem;
  color: #d2f7fd;
}
h1, .h1 { border-bottom-color: #c4c4c4; }
h2, .h2 { border-bottom-color: #828282; }
h3, .h3, h4, .h4, h5, h6 { border-bottom-color: #0f5377; }
```

**写作排版约定**（主站 markdown 备忘中的规范，同样适用于文档类页面）：

- 中文字符与半角英文/数字间用半角空格隔开；中文句内使用全角标点、直角引号「」。
- 尽量少用三级以上标题；以二级标题作为顶级标题可行。

---

## 4. 组件样式

### 4.1 导航栏（navbar）

主站：高 `50px`、背景 `#093750`（`.top-bg`），链接色 `#abc0ca`，hover `#03a4fb`，激活项底部有 4px 青色条。

投票系统 `.navbar-audio`：

```css
.navbar-audio {
  background: #093750 !important;
  border: none !important;
  border-bottom: 2px solid #1985a1;
  box-shadow: 0 1px 10px rgba(0,0,0,.15);
  border-radius: 0 !important;
  min-height: 50px;
}
.navbar-audio .navbar-brand { color: #d2f7fd; font-size: 20px; letter-spacing: 1px; }
```

导航右侧主按钮 `.nav-create-btn`：填充 `#1985a1`、文字 `#022335`、加粗、无圆角；hover 变 `#1a9bbe`。次级按钮 `.ghost`：背景 `#022335`、边框 `#0f5377`，hover 边框 `#1985a1`、文字 `#d2f7fd`。

### 4.2 卡片（.card）

投票系统卡片（**左侧 4px 青色竖条**是标志性特征）：

```css
.card {
  background-color: #093750;
  border-left: 4px solid #1985a1;
  padding: 18px 24px;
  margin-bottom: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,.2);
}
.card-title { color: #d2f7fd; font-size: 16px; padding-bottom: 8px;
              border-bottom: 1px solid #0f5377; }
```

### 4.3 表格（table）

投票系统表格规范：

```css
.poll-table thead th {
  color: #828282; font-size: 13px; text-transform: uppercase; letter-spacing: .5px;
  padding: 10px 8px; border-bottom: 1px solid #0f5377; text-align: left;
  font-weight: normal; background: #093750; position: sticky; top: 0;
}
.poll-table tbody td { padding: 10px 8px; border-bottom: 1px solid #063145; vertical-align: middle; }
.poll-table tbody tr:hover { background: #0a3f5c; }
/* 表内标题：白青；说明：灰 */
.col-title .pt-title { color: #d2f7fd; font-size: 14px; }
.col-title .pt-desc { color: #828282; font-size: 12px; }
```

主站 `.logchart`（服务器日志/统计表）：

```css
.logchart thead tr { background-color: #008fa8; color: #fff; }
.logchart tbody tr:nth-child(odd)  { background-color: #474747; }
.logchart tbody tr:nth-child(even) { background-color: #2e2e2e; }
.logchart tbody tr:hover { background-color: #03a4fb; color: #022335; }
.logchart th, .logchart td { border: 1px solid #000; text-align: center; padding: 5px; }
```

### 4.4 按钮

- 主按钮：填充 `#1985a1` / `#03a4fb`，深色文字，hover 提亮。
- 幽灵按钮：深底 `#022335` + 边框 `#0f5377`，hover 边框青色 `#1985a1`。
- 表格行内小按钮 `.act-btn`：`padding: 4px 12px; border-radius: 0; border: 1px solid #0f5377; background: #022335; color: #abc0ca;` hover 边框变 `#1985a1` 文字变 `#d2f7fd`；`.primary` 变青色填充。

### 4.5 表单输入

```css
.form-field input, .form-field textarea, .form-field select {
  width: 100%;
  background: #022335;
  border: 1px solid #0f5377;
  border-radius: 0;
  color: #abc0ca;
  font-size: 14px;
  padding: 7px 10px;
  outline: none;
  font-family: inherit;
  transition: border-color .2s;
}
.form-field input:focus { border-color: #1985a1; }
.form-field label { color: #828282; font-size: 13px; }
```

选项列表项（单选/多选）：背景 `#022335` + 边框 `#0f5377`，hover 边框变 `#1985a1`，选中态 `.selected` 边框 `#1985a1` + 背景 `rgba(25,133,161,.15)`，输入框 `accent-color: #1985a1`。

### 4.6 状态徽章（.status-badge）

```css
.status-badge { display: inline-block; padding: 1px 8px; font-size: 12px;
                border-radius: 0; border: 1px solid; letter-spacing: 1px; }
.status-badge.ongoing { color: #00d68a; border-color: #00d68a; background: rgba(0,214,138,.08); }
.status-badge.ended   { color: #828282; border-color: #0f5377; background: rgba(15,83,119,.15); }
```

### 4.7 结果条/进度条

```css
.result-summary { display: flex; gap: 24px; align-items: center; padding: 14px 16px;
                  background: #022335; border-left: 3px solid #1985a1; }
.result-summary .rs-num   { color: #d2f7fd; font-size: 26px; font-weight: bold; }
.result-summary .rs-label { color: #828282; font-size: 12px; }

.rr-bar  { width: 100%; height: 10px; background: #022335; border: 1px solid #0f5377;
           border-radius: 0; overflow: hidden; }
.rr-fill { height: 100%; background: #1985a1; width: 0; transition: width .6s ease; }
```

### 4.8 引用块 / 提示框（主站 markdown 扩展）

普通 blockquote：文字 `#828282`、左边框 5px `#828282`。

**高亮引用块**（`.uuz-markdown blockquote.block-*`，Bootstrap 暗色变量的派生）：

```css
.block-info    { border-color:#0dcaf0; background:#032830; color:#6edff6; }
.block-warning { border-color:#ffc107; background:#332701; color:#ffda6a; }
.block-danger  { border-color:#dc3545; background:#2c0b0e; color:#ea868f; }
.block-success { border-color:#198754; background:#051b11; color:#75b798; }
/* 块前 ::before 标签：尽量不要使用图标，用文字 Info / Warning / Danger / Success 区分 */
```

**高亮 div 元素**（`.warning/.caution/.approved/.tips`，带左下角裁切 + 左竖条，尽量不要使用图标）：

```css
.warning, .caution, .approved, .tips {
  background-color:#380000; color:#a80000; border-left:5px solid #a80000;
  padding:5px 12px; font-size:15px; margin-bottom:10px;
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - 15px), calc(100% - 15px) 100%, 0 100%);
}
.caution  { background-color:#382200; color:#a85a00; border-left-color:#a85a00; }
.approved { background-color:#003800; color:#00a800; border-left-color:#00a800; }
.tips     { background-color:#00272e; color:#008fa8; border-left-color:#008fa8; }
```

### 4.9 代码块

```css
pre, code {
  background-color: #000 !important;
  color: #fff !important;
  border: none !important;
  border-radius: 0 !important;
  font-size: 14px !important;
}
/* 主站 pre 带行号（::before 计数器） */
```

### 4.10 链接（主站特色 hover 动画）

```css
a { text-decoration: none !important; transition: color .15s; }
a::before {
  content: ""; position: absolute; left: 0; bottom: 0;
  width: 0; height: 100%; background: #03a4fb; z-index: -1;
  transition: width .15s cubic-bezier(0.42, 0, 0.14, 1);
}
a:hover::before { width: 100%; }
```

### 4.11 滚动条 & 选中

```css
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background-color: #093750; }
::-webkit-scrollbar-thumb { background-color: rgba(255,255,255,.18); }
::-webkit-scrollbar-thumb:hover { background-color: rgba(255,255,255,.63); }
::selection { background-color: rgba(3,164,251,.28); }
```

---

## 5. 页面骨架示例（投票系统风格）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>页面标题</title>
  <link rel="stylesheet" href="bootstrap.min.css">
  <!-- 尽量不要使用图标，无需引入 font-awesome -->
  <style>
    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body {
      background-color: #022335 !important;
      font-family: fontjmono, "JetBrains Mono", "思源黑体 CN", "Sarasa Gothic SC",
                   "Source Han Sans SC", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
      color: #abc0ca !important;
      font-size: 15px !important;
    }
    .page-container { max-width: 820px; margin: 0 auto; padding: 20px; }
    .card { background: #093750; border-left: 4px solid #1985a1;
            padding: 20px 24px; box-shadow: 0 2px 12px rgba(0,0,0,.2); }
    /* ... 按上述组件样式填充 ... */
  </style>
</head>
<body> ... </body>
</html>
```

---

## 6. 速查（How to reuse）

1. **新做普通信息/文档页** → 采用主站样式：Bootstrap 5 暗色 + 上面 4.8/4.9/4.10 的 markdown 扩展样式。
2. **新做工具/数据页（投票、统计、管理后台）** → 采用投票系统样式：Bootstrap 3/4 + 4.1~4.7 组件。
3. **配色纪律**：背景 `#022335`，面板 `#093750`，强调色 `#1985a1`（表单/工具）或 `#03a4fb`（站点/链接），亮文本 `#d2f7fd`，正文 `#abc0ca`，弱化 `#828282`，边框 `#0f5377`。不要引入其他高饱和色。
4. **字体纪律**：始终以 `JetBrains Mono` 开头的中文等宽回退栈，正文 14–15px。
5. **形态纪律**：优先直角（`border-radius: 0`）；卡片左侧 4px 竖条；表格行 hover 提亮；成功态绿色、警告黄色、危险红色。
6. **图标纪律**：尽量不要使用图标；确需强调时以文字或配色表达。

---

## 7. 来源页面清单（验证用）

- 主站样式文件：`https://aerohakugyokurou.top/css/main.css`（Bootstrap 5.3.3 + `[data-bs-theme="dark"]` 定制 + `.uuz-markdown` 扩展）
- 投票系统源文件：`voteproj/index.html`、`voteproj/vote.html`、`voteproj/create.html`、`voteproj/result.html`（本地工作区）
- 投票系统线上：`https://forum.hoorimanor.top/vote/`
