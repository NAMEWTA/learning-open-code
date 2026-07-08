# HanaAgent 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | HanaAgent 架构全景：技术栈、目录结构、核心设计哲学 |
| core/ 引擎编排层 | `./module-core/` | Engine→Agent→Session→Plugin→Provider 五层编排 |
| lib/ 核心库 | `./module-lib/` | 36 个子系统：记忆编译、双层沙盒、技能市场、工作流引擎 |
| server/ Hono 服务 | `./module-server/` | 38 路由模块 + 双 WS 架构 + 三层鉴权后备链 |
| hub/ 后台任务中心 | `./module-hub/` | Scheduler+Heartbeat 双轨 + Agent Phone 模型 + EventBus |
| desktop/ Electron 前端 | `./module-desktop/` | 8 窗口入口 + 24 Zustand stores + 5 语言国际化 |
| shared/ 跨层共享 | `./module-shared/` | 51 文件 8 组：配置 Schema、密钥保管、日志脱敏、ErrorBus |
| plugins/ 内置插件 | `./module-plugins/` | 6 个系统插件：beautify/image-gen/mcp/media/office/jimeng-cli |
| packages/ 插件 SDK | `./module-packages/` | 四包 SDK 体系：protocol→sdk→runtime→components |
| skills2set/ 技能定义 | `./module-skills2set/` | 4 套内置技能：插件创建/技能创建/静默反思/用户指南 |
| cli/ CLI 终端 | `./module-cli/` | Server-first CLI + 三层降级连接 + 终端主题 |
| Agent 对话全链路 | `./slice-agent-conversation-flow/` | 用户输入→LLM 响应 8 层穿透 + 6 异常路径 |
| 插件生命周期全链路 | `./slice-plugin-lifecycle-flow/` | 拖拽安装→工具注册 8 层穿透 + 3 级门禁 |
| 记忆编译检索全链路 | `./slice-memory-compile-flow/` | 会话摘要→长期记忆 7 层传送带 + 断点续跑 |
| 安全沙盒执行全链路 | `./slice-sandbox-exec-flow/` | 命令执行→双层沙盒 8 层穿透 + 7 异常路径 |
| 外部平台桥接全链路 | `./slice-bridge-message-flow/` | 5 平台 Webhook→Agent 响应 10 层穿透 |
| 书桌定时任务全链路 | `./slice-desk-automation-flow/` | 文件监听→Cron→Agent 执行 11 步链路 |
| 首次运行引导流程 | `./slice-first-run-onboarding-flow/` | Electron 启动→Provider 配置 7 层引导 |
