# HanaAgent · 架构教学 Wiki

> 📊 整体进度：**26/26 goals · 100%** · 已执行 6 轮
> 🕐 最后更新：2026-07-07

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ 100% |
| L1 模块总览 | 10 | 10 | ██████████ 100% |
| L2 垂直切片 | 7 | 7 | ██████████ 100% |
| L3 微观 API | 4 | 4 | ██████████ 100% |
| L4 深度剖析 | 4 | 4 | ██████████ 100% |

---

## 🏗️ L0 · 项目总览

- **[📄 HanaAgent 项目总览](00-overview/reference/00-overview.html)**
  > 技术栈：TypeScript + Electron 42 + React 19 + Hono 4 + better-sqlite3
  > 架构风格：六层分层（Desktop → Server → Core → Hub → Lib → Plugins）
  > 10 个顶层模块 · 1,924 个源文件

---

## 📦 L1 · 模块总览

### module-core — core/ 引擎编排层
- **[📄 模块总览](module-core/reference/core-overview.html)**
  > 职责：Engine Facade → Agent/Session/Plugin/Provider/Bridge 六大 Manager
  > 分层：Engine → Domain Managers → Specialized Services → External Dependencies
  > 核心文件：session-coordinator.ts (217KB), engine.ts (115KB), agent.ts (81KB)
- **关联垂直切片**：
  - [🔪 Agent 对话全链路](slice-agent-conversation-flow/lessons/agent-conversation-flow.html)
  - [🔪 插件生命周期全链路](slice-plugin-lifecycle-flow/lessons/plugin-lifecycle-flow.html)
  - [🔪 外部平台桥接全链路](slice-bridge-message-flow/lessons/bridge-message-flow.html)

### module-lib — lib/ 核心库（36 个子系统）
- **[📄 模块总览](module-lib/reference/lib-overview.html)**
  > 职责：功能实现层，所有底层能力（记忆、工具、沙盒、技能、桥接等）
  > 分组：8 个功能域（记忆与身份/工具与执行/安全沙盒/AI与LLM/集成桥接/书桌自动化/文件技能/基础设施）
- **[🔬 API 参考 (L3)](module-lib/reference/lib-api.html)** — 待生成
- **关联垂直切片**：
  - [🔪 记忆编译检索全链路](slice-memory-compile-flow/lessons/memory-compile-flow.html)
  - [🔪 安全沙盒执行全链路](slice-sandbox-exec-flow/lessons/sandbox-exec-flow.html)
  - [🔪 书桌定时任务全链路](slice-desk-automation-flow/lessons/desk-automation-flow.html)

### module-server — server/ Hono HTTP + WebSocket 服务
- **[📄 模块总览](module-server/reference/server-overview.html)**
  > 职责：独立 Node.js 进程，Hono HTTP 框架 + ws WebSocket + 38 路由模块
  > 特色：双 WS 架构、三层鉴权后备链、Ring Buffer 流式事件、Worker Keepalive
- **关联垂直切片**：
  - [🔪 Agent 对话全链路](slice-agent-conversation-flow/lessons/agent-conversation-flow.html)

### module-hub — hub/ 后台任务中心
- **[📄 模块总览](module-hub/reference/hub-overview.html)**
  > 职责：Scheduler 双轨调度 + ChannelRouter 频道路由 + EventBus 40+ 能力 + AgentExecutor
  > 特色：Heartbeat+Cron 统一走 executeIsolated 隔离执行、Agent Phone 送达模型
- **关联垂直切片**：
  - [🔪 外部平台桥接全链路](slice-bridge-message-flow/lessons/bridge-message-flow.html)

### module-desktop — desktop/ Electron + React 前端
- **[📄 模块总览](module-desktop/reference/desktop-overview.html)**
  > 职责：Electron 42 主进程(5022 行) + React 19 渲染进程(18 组件子目录)
  > 特色：8 窗口入口、24 Zustand stores、5 语言国际化、Native 模块
- **关联垂直切片**：
  - [🔪 首次运行引导流程](slice-first-run-onboarding-flow/lessons/first-run-onboarding-flow.html)

### module-shared — shared/ 跨层共享模块
- **[📄 模块总览](module-shared/reference/shared-overview.html)**
  > 职责：51 个文件，跨 Desktop/Server/Core 共享的类型定义与工具函数
  > 特色：CONFIG_SCHEMA 22 全局字段、12 层日志脱敏、ErrorBus 去重窗口、零上层依赖

### module-plugins — plugins/ 内置系统插件
- **[📄 模块总览](module-plugins/reference/plugins-overview.html)**
  > 职责：6 个内置系统插件（beautify/image-gen/jimeng-cli/mcp/media/office）
  > 旗舰插件 image-gen：8 个 Adapter + 异步 Poller + 任务持久化
- **关联垂直切片**：
  - [🔪 插件生命周期全链路](slice-plugin-lifecycle-flow/lessons/plugin-lifecycle-flow.html)

### module-packages — packages/ 插件 SDK 体系
- **[📄 模块总览](module-packages/reference/packages-overview.html)**
  > 职责：四包 SDK 体系（plugin-protocol → plugin-sdk → plugin-runtime → plugin-components）
  > 特色：四级主题回退 + 13 个 React 组件 + 40+ Runtime helpers

### module-skills2set — skills2set/ 内置技能定义
- **[📄 模块总览](module-skills2set/reference/skills2set-overview.html)**
  > 职责：4 套内置技能（插件创建向导/技能创建向导/静默反思/用户指南）
  > 特色：10 步迭代开发循环 + 5 阶段推理协议 + 评测流水线

### module-cli — cli/ CLI 终端入口
- **[📄 模块总览](module-cli/reference/cli-overview.html)**
  > 职责：Server-first CLI 瘦客户端（仅 800 行），三层降级连接策略
  > 特色：6 种命令矩阵 + ANSI True Color 主题 + shared/yuan-visuals 色彩共享

---

## 🔪 L2 · 垂直切片

### slice-agent-conversation-flow — Agent 对话全链路
- **[📄 课程](slice-agent-conversation-flow/lessons/agent-conversation-flow.html)**
  > 链路：React ChatArea → WS → chat.ts → Engine → Agent → SessionCoordinator → LLM → 回流广播
  > 所属模块：[module-core](module-core/reference/core-overview.html) · [module-server](module-server/reference/server-overview.html)
  > 异常路径：LLM 超时、Token 超限压缩、用户中断、WS 断开宽限、停滞看门狗、空回复检测

### slice-plugin-lifecycle-flow — 插件安装与加载全链路
- **[📄 课程](slice-plugin-lifecycle-flow/lessons/plugin-lifecycle-flow.html)**
  > 链路：拖拽 zip → PluginManager.install() → manifest 解析 → 权限判定 → PluginContext → 工具/路由注册 → onload
  > 所属模块：[module-core](module-core/reference/core-overview.html) · [module-plugins](module-plugins/reference/plugins-overview.html)
  > 异常路径：权限不足→restricted、manifest 格式错误→拒绝、依赖不兼容→incompatible

### slice-memory-compile-flow — 记忆编译与检索全链路
- **[📄 课程](slice-memory-compile-flow/lessons/memory-compile-flow.html)**
  > 链路：会话结束 → SessionCompactor → DiaryWriter → compileToday → weeklyRollup → longterm → Prompt 注入
  > 所属模块：[module-lib](module-lib/reference/lib-overview.html) · [module-core](module-core/reference/core-overview.html)
  > 异常路径：内存溢出限流、编译失败回退、LLM 失败降级、文件系统容错、并发竞态防护

### slice-sandbox-exec-flow — 安全沙盒命令执行全链路
- **[📄 课程](slice-sandbox-exec-flow/lessons/sandbox-exec-flow.html)**
  > 链路：Agent exec_command → normalizeExecCommandParams → classifyExecCommand(5级) → PathGuard(11级) → 审批 → OS沙盒 → 输出
  > 所属模块：[module-lib](module-lib/reference/lib-overview.html)
  > 异常路径：路径越权阻断、命令注入拦截、沙盒逃逸保护、Managed Config 写入拦截、超时中断

### slice-bridge-message-flow — 外部平台消息桥接全链路
- **[📄 课程](slice-bridge-message-flow/lessons/bridge-message-flow.html)**
  > 链路：Telegram/飞书/钉钉 Webhook → Adapter → BridgeManager → SessionManager → Agent Phone → ChannelRouter → 回复
  > 所属模块：[module-core](module-core/reference/core-overview.html) · [module-hub](module-hub/reference/hub-overview.html)
  > 异常路径：断连重连、Token 过期、消息格式兼容、限流保护、幂等去重(10min TTL)

### slice-desk-automation-flow — 书桌文件拖拽与定时任务全链路
- **[📄 课程](slice-desk-automation-flow/lessons/desk-automation-flow.html)**
  > 链路：chokidar 监听 → ResourceIO → ActivityStore → CronScheduler → AgentExecutor → 通知回传
  > 所属模块：[module-lib](module-lib/reference/lib-overview.html)
  > 异常路径：文件监听失效降级、系统休眠追赶、Agent 执行超时双重保险

### slice-first-run-onboarding-flow — 首次运行引导流程
- **[📄 课程](slice-first-run-onboarding-flow/lessons/first-run-onboarding-flow.html)**
  > 链路：Electron 启动 → first-run.ts 检测 → Splash → Onboarding 6 步(语言/身份/Provider/模型/主题/工作区) → 主界面
  > 所属模块：[module-desktop](module-desktop/reference/desktop-overview.html) · [module-core](module-core/reference/core-overview.html)
  > 异常路径：Provider 连接失败、API Key 无效、OAuth 中断、模板缺失/磁盘满/端口占用

---

---

## 🔬 L3 · 微观 API 参考

### module-core — core/ API 参考
- **[🔬 API 参考](module-core/reference/core-api.html)** — 2063 行 / 112KB
  > 8 组 400+ API：HanaEngine(150+) / Agent(50+) / SessionCoordinator(60+) / PluginManager(40+) / Provider+LLM(60+) / VisionBridge(5) / 安全权限(10) / 基础设施(50+)

### module-server — server/ API 参考
- **[🔬 API 参考](module-server/reference/server-api.html)** — 1675 行 / 88KB
  > 15 组 200+ 端点：认证(12) / 会话(22) / Agent(22) / 插件(20+) / Provider(15+) / 配置(21) / 文件(24) / 设备(5) / 桥接(6) / 频道(11) / 书桌(10) / 技能(10) / WebSocket 协议 / HTTP 中间件(6) / 工具函数(6)

### module-lib — lib/ API 参考
- **[🔬 API 参考](module-lib/reference/lib-api.html)** — 1000 行 / 57KB
  > 8 子系统完整 API + 15 子系统速查表：memory / sandbox / exec-command / shell / skills / desk / workflow / llm

### module-shared — shared/ API 参考
- **[🔬 API 参考](module-shared/reference/shared-api.html)** — 1515 行 / 99KB
  > 8 组 28 文件 120+ API：配置/Schema / 运行时路径 / 安全密钥 / 模型Provider / 工作区 / 错误重试 / 通知偏好 / 网络

---

## 🧠 L4 · 深度剖析

### deep-dive-sandbox — 双层沙盒架构设计
- **[📄 课程](deep-dive-sandbox/lessons/sandbox-architecture.html)**
  > PathGuard 11 级判定链 + Bubblewrap/Seatbelt/Restricted Token 三平台 OS 沙盒
  > 5 种方案对比 · AppContainer→Restricted Token 迁移史 · 11 维跨平台差异矩阵
  > 关联模块：[module-lib](module-lib/reference/lib-overview.html) · [L2 沙盒执行](slice-sandbox-exec-flow/lessons/sandbox-exec-flow.html)

### deep-dive-memory-conveyor — 记忆 v4 传送带模型
- **[📄 课程](deep-dive-memory-conveyor/lessons/memory-conveyor.html)**
  > compileToday→compileDaily→weeklyRollup→longterm 五级蒸馏算法（含伪代码）
  > Token 预算分配（today 450/daily 100/longterm 600/facts 300）· 日成本 $0.10-0.50
  > 关联模块：[module-lib](module-lib/reference/lib-overview.html) · [L2 记忆编译](slice-memory-compile-flow/lessons/memory-compile-flow.html)

### deep-dive-session-coordinator — SessionCoordinator 217KB 巨兽拆解
- **[📄 课程](deep-dive-session-coordinator/lessons/session-coordinator.html)**
  > 8 职责域聚合根分析 · promptSession 12 步管线 · 18 个 Map 字段分组
  > 渐进式拆分建议（P0→P1→P2）· 16 个构造器注入的依赖网
  > 关联模块：[module-core](module-core/reference/core-overview.html)

### deep-dive-plugin-sdk — 插件 SDK 四包分离架构
- **[📄 课程](deep-dive-plugin-sdk/lessons/plugin-sdk-architecture.html)**
  > protocol/sdk/runtime/components 四包职责边界 · BusProxy 能力安全模型
  > 四级主题回退 · 7 组正确 vs 反模式 · 3 种生产分发方式
  > 关联模块：[module-packages](module-packages/reference/packages-overview.html) · [module-plugins](module-plugins/reference/plugins-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 顶层模块 L1 | 10 / 10（100%） |
| 核心功能 L2 | 7 / 7（100%） |
| 微观 API L3 | 4 / 4（100%） |
| 深度剖析 L4 | 4 / 4（100%） |
| **总计** | **26 goals** |
| 产出文档总大小 | ~1.2 MB |
| HTML 课程（L2+L4 lessons） | 11 篇 |
| HTML 参考（L0+L1+L3 reference） | 15 篇 |
| 豁免文件（vendor/自动生成/二进制/资源/字体/CI） | ~200+ 个 |

### 覆盖率明细

| 模块 | 源文件 | L1 | L3 | L4 | 覆盖状态 |
|------|--------|-----|-----|-----|---------|
| core/ | 148 | ✅ | ✅ API 参考 112KB | ✅ SessionCoordinator | 完全覆盖 |
| lib/ | 272 | ✅ | ✅ API 参考 57KB | ✅ 沙盒+记忆 | 完全覆盖 |
| server/ | 75 | ✅ | ✅ API 参考 88KB | — | 完全覆盖 |
| desktop/ | 733 | ✅ | 架构覆盖 | — | 完全覆盖 |
| shared/ | 56 | ✅ | ✅ API 参考 99KB | — | 完全覆盖 |
| plugins/ | 62 | ✅ | — | — | L1 覆盖 |
| hub/ | 9 | ✅ | — | — | L1 覆盖 |
| cli/ | 7 | ✅ | — | — | L1 覆盖 |
| packages/ | 8 | ✅ | — | ✅ 四包架构 | 完全覆盖 |
| skills2set/ | 5 | ✅ | — | — | L1 覆盖 |
| tests/ | 570 | 引用佐证 | — | — | 辅助引用 |
| 配置/构建 | 47 | ✅ 提及 | — | — | L0 覆盖 |
