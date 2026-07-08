# 课程快照：WebUI 启动与远程访问全链路

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T18:53:55+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/desktop/src/index.ts` | Electron 启动分支、`--webui`、`--remote`、`--resetpass`、backend 复用与无窗口存活链路 | 核心 |
| `packages/desktop/src/process/utils/webuiConfig.ts` | WebUI 端口解析、远程访问判断、用户配置、桌面偏好恢复与桌面管理式 WebUI 生命周期 | 核心 |
| `packages/web-host/src/index.ts` | `startWebHost()` 组合 backend 与静态服务，区分 `ownBackend` 与 `useExistingBackend` | 核心 |
| `packages/web-host/src/static-server.ts` | 静态资源服务、API 代理、登录路径转发、WS/STT TCP splice、监听地址和 `networkUrl` 生成 | 核心 |
| `packages/web-cli/src/index.ts` | 独立 WebCLI 启动、参数解析、路径解析、frontend-only 降级、resetpass 与停止逻辑 | 核心 |
| `packages/web-cli/src/ensureAdminPassword.ts` | WebCLI 首启管理员密码自举、认证状态轮询和失败不阻断边界 | 辅助 |
| `packages/web-cli/src/browser.ts` | 本地/远程模式下自动打开浏览器的策略边界 | 辅助 |
| `docs/guides/webui.md` | 用户指南证据和默认端口、排障端口漂移标注 | 证据 |
| `tests/e2e/specs/webui.e2e.ts` | WebUI 设置页、默认端口、远程开关、启停生命周期的 E2E 证据 | 证据 |

## 关联教学引用

- `teach/open-ai-desktop/AionU/00-overview/reference/00-overview.html` — L0 架构回链，确认 WebUI 在整体架构中的位置
- `teach/open-ai-desktop/AionU/module-web-runtime/reference/web-runtime-overview.html` — L1 WebHost / WebCLI 模块边界回链
- `teach/open-ai-desktop/AionU/module-main-entry/reference/main-entry-overview.html` — L1 Electron main 入口和运行形态分流回链
- `teach/open-ai-desktop/AionU/module-docs-resources/reference/docs-resources-overview.html` — L1 docs/resources 文档漂移判断回链

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-flow-map.html` | WebUI 启动与远程访问主链路短课 |

## 已生成参考文档

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | `reference/webui-remote-flow-map.html` | 入口点、沿途层次、调用时序、边界路径、证据与漂移速查 |

## 已生成学习记录

| 编号 | 学习记录 | 描述 |
|------|---------|------|
| 01 | `learning-records/0001-webui-runtime-boundaries.md` | 确认 Electron headless、桌面设置恢复和独立 WebCLI 三条当前实现路径 |

## 快照摘要
- 课程数：1
- 参考文档数：1
- 引用源文件数：9
- 关联教学文件数：4
- 学习记录数：1
