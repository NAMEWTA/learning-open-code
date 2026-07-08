# 课程快照：module-web-runtime

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:23:53+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/packages/web-host/src/index.ts` | `startWebHost()` 组合入口与公共导出 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/web-host/src/types.ts` | `WebHostOptions`、`WebHostHandle`、`AppMetadata` 契约 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-host/src/backend-launcher.ts` | backend 生命周期、端口选择、spawn 与诊断 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/web-host/src/static-server.ts` | 静态资源宿主、API 代理与 TCP splice | 🔴 核心 |
| `open-ai-desktop/AionU/packages/web-host/src/agent-process-registry.ts` | 停止阶段的 agent 进程清理 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-host/src/backend-launcher.test.ts` | backend 生命周期的单元测试证据 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-host/src/static-server.unit.test.ts` | 静态服务、代理与 WebSocket 升级行为测试 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-host/src/agent-process-registry.test.ts` | agent 进程清理行为测试 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-host/tests/start-web-host.test.ts` | 组合器职责边界测试 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-cli/src/index.ts` | CLI 参数解析、启动链、frontend-only 与 resetpass | 🔴 核心 |
| `open-ai-desktop/AionU/packages/web-cli/src/browser.ts` | 自动开浏览器与平台 opener 规则 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/web-cli/src/ensureAdminPassword.ts` | 首启管理员密码探测与生成 | 🔴 核心 |
| `open-ai-desktop/AionU/tests/unit/web-cli/browser.test.ts` | 浏览器打开策略测试 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/web-cli/ensureAdminPassword.test.ts` | 首启密码轮询、回退与警告分支测试 | 🟡 辅助 |
| `open-ai-desktop/AionU/docs/guides/webui.md` | 用户视角的 WebUI 启动与远程访问说明 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-web-runtime-module-tour | `lessons/0001-web-runtime-module-tour.html` | WebHost 与 WebCLI 运行时导览短课 |

## 参考资料

- `reference/web-runtime-overview.html` — WebHost 与 WebCLI 运行时参考

## 目录背景说明

- `packages/web-host/src/` 是本主题的运行时核心目录；快照中只保留实际被课程和参考文档分析到的文件，不再记录接口 URL 片段。
- `docs/guides/webui.md` 属于用户文档，不参与运行时实现，但为 CLI 行为提供外部可见的操作语义。

## 快照摘要
- 课程数：1
- 引用源文件数：15
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
