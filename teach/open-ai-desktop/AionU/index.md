# AionU 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | AionU 架构地图、技术栈与学习路线 |
| Electron 主入口与生命周期 | `./module-main-entry/` | Electron 入口分流、backend 启动和退出收尾总览 |
| Main process 基础设施 | `./module-process-infra/` | initializeProcess、存储、bridge、服务与 backend 前置设施 |
| Preload 与 IPC 安全边界 | `./module-preload-ipc/` | 主 preload、桥接 adapter 与 pet 多窗口通道总览 |
| Renderer 核心与 UI Shell | `./module-renderer-core/` | provider 栈、路由守卫和统一 UI shell 总览 |
| Common adapter 调用适配层 | `./module-common-adapter/` | renderer 能力目录到 IPC、REST、WebSocket 的适配总览 |
| Web 运行时与 CLI | `./module-web-runtime/` | WebHost、静态服务器、Web CLI 与密码重置启动链路 |
| 移动端应用 | `./module-mobile-app/` | Expo 移动端登录、WebSocket 和聊天运行时总览 |
| Conversation runtime | `./module-conversation-runtime/` | 会话页壳层、消息区、workspace 与平台分流总览 |
| Team Mode 多 Agent 协作 | `./module-team-mode/` | 团队页、成员 slot、Team run 事件和发送闸门总览 |
| Cron 自动化 | `./module-cron/` | 定时任务列表、状态 hook、HTTP API 和事件流总览 |
| Assistants、Skills 与 Tools 设置 | `./module-assistants-skills/` | 助手编辑、Skill 导入和 MCP 工具配置总览 |
| 构建、发布与资源准备 | `./module-build-release/` | dist 入口、aioncore 资源、electron-builder 和发布资产总览 |
| 测试体系与质量闸门 | `./module-test-quality/` | Vitest、Playwright、CI coverage 和业务测试证据总览 |
| 文档、示例与资源体系 | `./module-docs-resources/` | docs、examples、.aionui、resources、public 的产品契约总览 |
| 桌面启动到首屏全链路 | `./slice-desktop-startup/` | Electron 入口、main process、renderer bootstrap、Router 首屏与失败边界 |
| WebUI 启动与远程访问全链路 | `./slice-webui-remote/` | `--webui`、web-host、web-cli、远程绑定和密码初始化边界 |
| 发送会话消息全链路 | `./slice-conversation-send/` | SendBox、runtime view、adapter、HTTP/WS 流和错误反馈 |
| 工具调用确认全链路 | `./slice-tool-permission/` | permission 消息、确认 UI、adapter confirm、恢复路径和安全边界 |
| Team 创建并运行全链路 | `./slice-team-run/` | Team 创建、成员 slot、发送 gate、run event 和 E2E 边界 |
| Cron 任务创建与触发全链路 | `./slice-cron-trigger/` | Cron 创建/编辑/启停、run-now、AI 指令和刷新链路 |
| 助手或 Skill 导入全链路 | `./slice-skill-import/` | Skills Hub 手动导入、assistant 默认 skill 绑定与错误文案 |
| Backend 启动失败恢复全链路 | `./slice-backend-recovery/` | backend failure 分类、数据库恢复和安装完整性弹窗 |

| Backend lifecycle 深剖 | `./deep-dive-backend-lifecycle/` | backend 启动、复用、停止与 SQLite 竞争规避 |
| REST/WS adapter 深剖 | `./deep-dive-adapter-rest-ws/` | httpBridge、wsEmitter、错误映射与 E2E helper |
| Team 事件模型深剖 | `./deep-dive-team-event-model/` | Team run、child turn、slot gate 与 reconcile 机制 |
| 发布资源裁剪深剖 | `./deep-dive-release-resource-trim/` | electron-builder 资源裁剪、aioncore 准备与校验 |
| Skills / Assistants / MCP 深剖 | `./deep-dive-skills-assistants-mcp/` | Assistant 默认能力、Skill 绑定和 MCP 快照边界 |
