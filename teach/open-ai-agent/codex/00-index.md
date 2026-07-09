# codex · 架构教学 Wiki

> 📊 整体进度：21/21 goals · 100% · 已执行 10 轮
> 🕐 最后更新：2026-07-09
> 🔗 源码版本：`cca16a10878202cb2f6e9666b6b4330329ea7e65` (main)

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ████████ |
| L1 模块总览 | 10 | 10 | ████████ |
| L2 垂直切片 | 10 | 10 | ████████ |
| L3 微观 API | 3 | 3 | ████████ |
| L4 深度剖析 | 2 | 2 | ████████ |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立全局地图，判断一个 Codex 问题应该从哪个顶层模块开始读。
- **[📄 codex 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Rust + TypeScript + Python · 架构风格：双语言 CLI（npm → Rust）· 10 个顶层模块

---

## 📦 L1 · 模块总览

### module-cli-packaging — CLI 与 npm 包装层
- **[📘 模块导览短课](module-cli-packaging/lessons/0001-cli-packaging-module-tour.html)**
  > 15 分钟说清 Codex 从 npm bin 到 Rust CLI 子命令分发的启动路径
- **[📄 模块总览参考](module-cli-packaging/reference/cli-packaging-overview.html)**
  > 职责：npm 包装、平台检测、Rust 二进制调用、子命令分发
- **关联垂直切片**：
  - [🔪 npm 到 Rust exec 启动链路](slice-npm-to-rust-exec/lessons/0001-flow-map.html)

### module-tui — TUI 交互式终端界面
- **[📘 模块导览短课](module-tui/lessons/0001-tui-module-tour.html)**
  > 15 分钟内定位 TUI 输入从 run_main 到 App/ChatWidget/BottomPane 的职责边界
- **[📄 模块总览参考](module-tui/reference/tui-overview.html)**
  > 职责：终端交互、消息渲染、输入区与运行状态指示
- **关联垂直切片**：
  - [🔪 交互 TUI 中一次用户 turn 的执行链路](slice-interactive-turn/lessons/0001-flow-map.html)

### module-core-runtime — Core Thread/Turn 与模型上下文
- **[📘 模块导览短课](module-core-runtime/lessons/0001-core-runtime-module-tour.html)**
  > 15 分钟内区分 core-api、codex-core、codex-protocol 在 Thread/Turn 运行时中的职责
- **[📄 模块总览参考](module-core-runtime/reference/core-runtime-overview.html)**
  > 职责：会话管理、回合生命周期、上下文组装、模型流处理、任务调度
- **关联垂直切片**：
  - [🔪 交互 TUI turn 链路](slice-interactive-turn/lessons/0001-flow-map.html)
  - [🔪 App-server JSON-RPC turn 链路](slice-app-server-turn/lessons/0001-flow-map.html)
  - [🔪 工具调用执行闭环](slice-tool-call-execution/lessons/0001-flow-map.html)
  - [🔪 Skill 上下文注入链路](slice-skill-activation/lessons/0001-flow-map.html)
  - [🔪 会话 Resume/Fork 持久化](slice-session-resume-fork/lessons/0001-flow-map.html)

### module-app-server — App-server JSON-RPC 服务
- **[📘 模块导览短课](module-app-server/lessons/0001-app-server-module-tour.html)**
  > 15 分钟内把 app-server JSON-RPC 方法定位到 transport、processor 和 core 边界
- **[📄 模块总览参考](module-app-server/reference/app-server-overview.html)**
  > 职责：JSON-RPC 2.0 协议、Thread/Turn/Item 方法族、传输抽象（HTTP/stdio）
- **[🔬 API 参考 (L3)](module-app-server/reference/app-server-api.html)** — 4 个辅助 crate（client/daemon/transport/test-client）
- **关联垂直切片**：
  - [🔪 App-server thread/start 到 turn/start 链路](slice-app-server-turn/lessons/0001-flow-map.html)
  - [🔪 SDK Thread/Run 事件消费链路](slice-sdk-thread-run/lessons/0001-flow-map.html)

### module-tools-execution — 工具定义与执行抽象
- **[📘 模块导览短课](module-tools-execution/lessons/0001-tools-execution-module-tour.html)**
  > 15 分钟内从一次模型工具调用追到 handler、registry、runtime 与受策略约束的副作用执行
- **[📄 模块总览参考](module-tools-execution/reference/tools-execution-overview.html)**
  > 职责：FunctionTool trait、ToolRegistry、exec policy、shell/patch 工具实现
- **关联垂直切片**：
  - [🔪 工具调用执行闭环](slice-tool-call-execution/lessons/0001-flow-map.html)

### module-sandbox-config — Sandbox、权限与配置系统
- **[📘 模块导览短课](module-sandbox-config/lessons/0001-sandbox-config-module-tour.html)**
  > 15 分钟内讲清配置、权限 profile、审批策略与平台 sandbox 执行之间的最小链路
- **[📄 模块总览参考](module-sandbox-config/reference/sandbox-config-overview.html)**
  > 职责：SandboxType 枚举、权限 profile 继承、execpolicy 引擎、平台沙箱实现
- **关联垂直切片**：
  - [🔪 Sandbox 权限决策链路](slice-sandbox-permission-decision/lessons/0001-flow-map.html)

### module-extensions-skills-mcp — Skills、Plugins、MCP 与 Hooks 扩展系统
- **[📘 模块导览短课](module-extensions-skills-mcp/lessons/0001-extensions-skills-mcp-module-tour.html)**
  > 15 分钟内区分 Skills、Plugins、MCP、Hooks，并复述发现扩展到调用/触发的最小序列
- **[📄 模块总览参考](module-extensions-skills-mcp/reference/extensions-skills-mcp-overview.html)**
  > 职责：Skill 发现/加载、Plugin 清单、MCP 连接管理、Hook 拦截点
- **[🔬 API 参考 (L3)](module-extensions-skills-mcp/reference/extensions-skills-mcp-api.html)** — 5 个子系统（hooks/plugin/connectors/file-search/context-fragments）
- **关联垂直切片**：
  - [🔪 Skill 上下文注入链路](slice-skill-activation/lessons/0001-flow-map.html)
  - [🔪 MCP Server 配置与连接管理](slice-mcp-server-management/lessons/0001-flow-map.html)

### module-sdk — Python 与 TypeScript SDK
- **[📘 模块导览短课](module-sdk/lessons/0001-sdk-module-tour.html)**
  > 15 分钟内区分 Python app-server JSON-RPC 长连接与 TypeScript exec JSONL 子进程流两条 SDK 路径
- **[📄 模块总览参考](module-sdk/reference/sdk-overview.html)**
  > 职责：Codex/Thread API 客户端、流式事件消费、子进程管理
- **关联垂直切片**：
  - [🔪 SDK Thread/Run 事件消费链路](slice-sdk-thread-run/lessons/0001-flow-map.html)

### module-build-release — Bazel、CI 与发布链路
- **[📘 模块导览短课](module-build-release/lessons/0001-build-release-module-tour.html)**
  > 15 分钟内画出 Codex 从 Bazel/Cargo/pnpm 三套构建系统到 npm/Homebrew 发布的最小链路
- **[📄 模块总览参考](module-build-release/reference/build-release-overview.html)**
  > 职责：Bazel 模块化构建、CI 多平台矩阵、发布流水线
- **关联垂直切片**：
  - [🔪 Rust 多平台二进制发布链路](slice-release-package-binary/lessons/0001-flow-map.html)

### module-state-model-backend — 状态、模型提供商与后端通信
- **[📘 模块导览短课](module-state-model-backend/lessons/0001-state-model-backend-module-tour.html)**
  > 定位认证令牌从平台密钥链到 HTTP 请求头的完整路径，区分 10 个 crate 的职责边界
- **[📄 模块总览参考](module-state-model-backend/reference/state-model-backend-overview.html)**
  > 职责：状态持久化(SQLite)、Thread 存储、认证(OAuth/API Key)、模型路由、云端配置
- **[🔬 API 参考 (L3)](module-state-model-backend/reference/state-model-backend-api.html)** — 4 个辅助 crate（analytics/otel/rollout-trace/feedback）
- **关联垂直切片**：
  - [🔪 会话 Resume/Fork 持久化](slice-session-resume-fork/lessons/0001-flow-map.html)

---

## 🔪 L2 · 垂直切片

### slice-npm-to-rust-exec — npm 到 Rust exec 启动链路
- **[📘 课程：链路地图](slice-npm-to-rust-exec/lessons/0001-flow-map.html)**
  > 链路：npm bin → codex.js 平台检测 → 二进制发现 → spawn → Rust CLI 分发 → exec 子进程
  > 所属模块：[module-cli-packaging](module-cli-packaging/reference/cli-packaging-overview.html)

### slice-interactive-turn — 交互 TUI turn 执行链路
- **[📘 课程 1：链路地图](slice-interactive-turn/lessons/0001-flow-map.html)**
  > 11 层架构全景 + mermaid 时序图 + API 错误异常路径
- **[📘 课程 2：主路径详解](slice-interactive-turn/lessons/0002-main-path.html)**
  > ChatWidget 提交 → run_turn 循环 → SSE 事件流转 → Turn 中断异常
  > 所属模块：[module-tui](module-tui/reference/tui-overview.html) · [module-core-runtime](module-core-runtime/reference/core-runtime-overview.html)

### slice-app-server-turn — App-server JSON-RPC turn 链路
- **[📘 课程 1：链路地图](slice-app-server-turn/lessons/0001-flow-map.html)**
  > 7 层架构图 + Mermaid 时序图 + thread 不存在异常路径
- **[📘 课程 2：主路径详解](slice-app-server-turn/lessons/0002-main-path.html)**
  > thread_start_inner 5 阶段 + turn_start_inner 6 阶段
  > 所属模块：[module-app-server](module-app-server/reference/app-server-overview.html) · [module-core-runtime](module-core-runtime/reference/core-runtime-overview.html)

### slice-tool-call-execution — 工具调用执行闭环
- **[📘 课程 1：链路地图](slice-tool-call-execution/lessons/0001-flow-map.html)**
  > 7 步闭环总览 + 三层调度器职责边界 + mermaid 时序图
- **[📘 课程 2：主路径详解](slice-tool-call-execution/lessons/0002-main-path.html)**
  > ToolInvocation → ShellCommandHandler → Orchestrator 审批与沙箱选择 → exec-server 执行
- **[📘 课程 3：异常路径](slice-tool-call-execution/lessons/0003-error-path.html)**
  > 权限拒绝、沙箱降级重试、命令超时与非零退出
  > 所属模块：[module-tools-execution](module-tools-execution/reference/tools-execution-overview.html) · [module-core-runtime](module-core-runtime/reference/core-runtime-overview.html)

### slice-sandbox-permission-decision — Sandbox 权限决策链路
- **[📘 课程 1：链路地图](slice-sandbox-permission-decision/lessons/0001-flow-map.html)**
  > 5 阶段决策管道 + Mermaid 时序图 + 异常路径概览
- **[📘 课程 2：主路径详解](slice-sandbox-permission-decision/lessons/0002-main-path.html)**
  > execpolicy 三态决策 → permissions 编译 → select_initial 决策树
  > 所属模块：[module-sandbox-config](module-sandbox-config/reference/sandbox-config-overview.html)

### slice-skill-activation — Skill 上下文注入链路
- **[📘 课程 1：链路地图](slice-skill-activation/lessons/0001-flow-map.html)**
  > 7 阶段 Mermaid 时序图 + 5 种 root 来源 + 异常路径
- **[📘 课程 2：主路径详解](slice-skill-activation/lessons/0002-main-path.html)**
  > loader BFS 扫描/容错解析、injection 显式提及/全文注入、render 预算模型/三级降级
  > 所属模块：[module-extensions-skills-mcp](module-extensions-skills-mcp/reference/extensions-skills-mcp-overview.html) · [module-core-runtime](module-core-runtime/reference/core-runtime-overview.html)

### slice-mcp-server-management — MCP Server 配置与连接管理
- **[📘 课程 1：链路地图](slice-mcp-server-management/lessons/0001-flow-map.html)**
  > 6 层链路全景 + mermaid 时序图 + stdio/streamable_http transport 对比
- **[📘 课程 2：主路径详解](slice-mcp-server-management/lessons/0002-main-path.html)**
  > CLI 参数解析 → TOML 序列化 → Transport 创建 → Initialize 握手
  > 所属模块：[module-extensions-skills-mcp](module-extensions-skills-mcp/reference/extensions-skills-mcp-overview.html) · [module-cli-packaging](module-cli-packaging/reference/cli-packaging-overview.html)

### slice-sdk-thread-run — SDK Thread/Run 事件消费链路
- **[📘 课程 1：链路地图](slice-sdk-thread-run/lessons/0001-flow-map.html)**
  > 5 层调用链 + mermaid 时序图 + TypeScript/Python SDK 对比
- **[📘 课程 2：主路径详解](slice-sdk-thread-run/lessons/0002-main-path.html)**
  > Codex 构造 → startThread 延迟绑定 → Thread.run() 事件循环 → exec 子进程 JSONL 通信
  > 所属模块：[module-sdk](module-sdk/reference/sdk-overview.html) · [module-app-server](module-app-server/reference/app-server-overview.html)

### slice-release-package-binary — Rust 多平台二进制发布链路
- **[📘 课程 1：链路地图](slice-release-package-binary/lessons/0001-flow-map.html)**
  > 8 路构建矩阵 + macOS 签名串行链 + mermaid 关键路径时序图
- **[📘 课程 2：主路径详解](slice-release-package-binary/lessons/0002-main-path.html)**
  > tag-check → build → sign-macos → release → publish-npm/publish-dotslash
  > 所属模块：[module-build-release](module-build-release/reference/build-release-overview.html) · [module-cli-packaging](module-cli-packaging/reference/cli-packaging-overview.html)

### slice-session-resume-fork — 会话 Resume/Fork/Archive 持久化
- **[📘 课程 1：链路地图](slice-session-resume-fork/lessons/0001-flow-map.html)**
  > 5 阶段全景（create→persist→resume→fork→archive）+ mermaid 时序图
- **[📘 课程 2：主路径详解](slice-session-resume-fork/lessons/0002-main-path.html)**
  > 冷 Resume：ThreadStore trait → load_history → reconstruct_history_from_rollout 反向扫描 → SQLite backfill
- **[📘 课程 3：异常路径](slice-session-resume-fork/lessons/0003-error-path.html)**
  > session 不存在、fork 冲突、archive 失败与子树回滚
  > 所属模块：[module-state-model-backend](module-state-model-backend/reference/state-model-backend-overview.html) · [module-cli-packaging](module-cli-packaging/reference/cli-packaging-overview.html) · [module-core-runtime](module-core-runtime/reference/core-runtime-overview.html)

---

## 🧠 L4 · 深度剖析

### deep-dive-rollout-reconstruction — Rollout JSONL 反向扫描重建 Session 算法
- **[📘 课程 1：问题背景](deep-dive-rollout-reconstruction/lessons/0001-problem-frame.html)**
  > 为什么需要反向扫描？JSONL append-only vs SQLite 查询的架构权衡
- **[📘 课程 2：核心机制](deep-dive-rollout-reconstruction/lessons/0002-core-mechanism.html)**
  > enumerate().rev() 反向扫描 + 窗口链追踪 + 三条件提前终止
  > 关联模块：[module-state-model-backend](module-state-model-backend/reference/state-model-backend-overview.html)
  > 关联切片：[🔪 会话 Resume/Fork 持久化](slice-session-resume-fork/lessons/0001-flow-map.html)

### deep-dive-skill-budget-model — Skill 上下文预算模型与三级降级策略
- **[📘 课程 1：问题背景](deep-dive-skill-budget-model/lessons/0001-problem-frame.html)**
  > 上下文窗口稀缺性 → 为什么选择预算模型而非硬性数量上限
- **[📘 课程 2：核心机制](deep-dive-skill-budget-model/lessons/0002-core-mechanism.html)**
  > 三级降级决策树（完整注入→描述截断→仅名称）+ 逐字符轮转分配 + 别名压缩
  > 关联模块：[module-extensions-skills-mcp](module-extensions-skills-mcp/reference/extensions-skills-mcp-overview.html)
  > 关联切片：[🔪 Skill 上下文注入链路](slice-skill-activation/lessons/0001-flow-map.html)

---

## 📊 产出统计

| 指标 | 数值 |
|------|------|
| L0 项目总览 | 1 主题（1 课 + 1 参考） |
| L1 模块总览 | 10 主题（各 1 课 + 1 参考） |
| L2 垂直切片 | 10 主题（共 21 课 + 10 参考） |
| L3 微观 API | 3 篇参考文档 |
| L4 深度剖析 | 2 主题（共 4 课 + 2 参考） |
| **合计** | **23 主题 · 38 课 · 27 参考** |
| 覆盖顶层模块 | 10/10（100%） |
| 覆盖核心功能 | 10/10 垂直切片 |
| 源码文件引用 | 390+ 处跨 23 个主题 |

---

## 🔮 待覆盖区域（后续规划）

以下 crate 在当前教学中尚未系统化覆盖：

| 优先级 | Crate 组 | 关键 crate |
|--------|---------|-----------|
| 高 | IDE 集成 (code-mode) | code-mode, code-mode-host, code-mode-protocol |
| 高 | 云端基础设施 | cloud-tasks, codex-api, codex-client, responses-api-proxy |
| 中 | 文件与系统工具 | file-system, file-watcher, git-utils, terminal-detection |
| 中 | 连接器生态 | external-agent-sessions, external-agent-migration |
| 低 | 工具链辅助 | ansi-escape, arg0, async-utils, http-client, utils |
| 低 | 第三方集成 | chatgpt, lmstudio, ollama, aws-auth |

建议 L4 深度剖析：
- Sandbox 平台抽象层设计模式（None/MacosSeatbelt/LinuxSeccomp/WindowsRestrictedToken）
- code-mode IDE 集成协议（code-mode ↔ code-mode-host ↔ code-mode-protocol 三方通信）
