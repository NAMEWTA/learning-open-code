# deer-flow · 架构教学 Wiki

> 📊 整体进度：39/39 goals · 100% · Round 9 收尾完成
> 🕐 最后更新：2026-07-08
> ✅ 审查：27 conditional_pass · 2 passed · 10 L3 skipped · 0 pending
> 📌 源码锚点：`eb5eb9c`（`main`）

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ████████ |
| L1 模块总览 | 12 | 12 | ████████ |
| L2 垂直切片 | 10 | 10 | ████████ |
| L3 微观 API | 12 | 12 | ████████ |
| L4 深度剖析 | 4 | 4 | ████████ |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立 deer-flow 全局地图：Gateway + LangGraph harness + Next.js workspace。
- **[📄 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Python 3.12 / FastAPI / LangGraph + Next.js 16 · 8 大后端子系统 + 前端双通道

---

## 📦 L1 · 模块总览

### module-gateway — Gateway API 外壳
- **[📘 模块导览短课](module-gateway/lessons/0001-gateway-module-tour.html)**
- **[📄 模块总览参考](module-gateway/reference/gateway-overview.html)**
- **[🔬 API 参考 (L3)](module-gateway/reference/gateway-api.html)**
  > 职责：FastAPI 入口、Auth/CSRF 中间件、REST 路由聚合
- **关联垂直切片**：[聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) · [上传与 artifact](slice-upload-sandbox-artifact/lessons/0001-flow-map.html) · [配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html)

### module-lead-agent — Agent lead runtime
- **[📘 模块导览短课](module-lead-agent/lessons/0001-lead-agent-module-tour.html)**
- **[📄 模块总览参考](module-lead-agent/reference/lead-agent-overview.html)**
  > 职责：`make_lead_agent` 装配模型、工具、prompt、middleware 链
- **关联垂直切片**：[聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) · [skill 激活](slice-skill-activation/lessons/0001-flow-map.html) · [subagent 委派](slice-subagent-delegation/lessons/0001-flow-map.html) · [goal 续跑](slice-goal-continuation/lessons/0001-flow-map.html)

### module-runtime-persistence — Runtime 与 persistence
- **[📘 模块导览短课](module-runtime-persistence/lessons/0001-runtime-persistence-module-tour.html)**
- **[📄 模块总览参考](module-runtime-persistence/reference/runtime-persistence-overview.html)**
  > 职责：run 生命周期、SSE stream、checkpointer、数据库持久化
- **关联垂直切片**：[聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) · [定时任务](slice-scheduled-task-run/lessons/0001-flow-map.html) · [IM 入站](slice-im-channel-run/lessons/0001-flow-map.html) · [memory 注入](slice-memory-update-injection/lessons/0001-flow-map.html)

### module-tools-mcp — Tools 与 MCP
- **[📘 模块导览短课](module-tools-mcp/lessons/0001-tools-mcp-module-tour.html)**
- **[📄 模块总览参考](module-tools-mcp/reference/tools-mcp-overview.html)**
  > 职责：内置工具、MCP 加载、deferred tool_search
- **关联垂直切片**：[配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html)

### module-sandbox — Sandbox 与文件系统
- **[📘 模块导览短课](module-sandbox/lessons/0001-sandbox-module-tour.html)**
- **[📄 模块总览参考](module-sandbox/reference/sandbox-overview.html)**
  > 职责：sandbox provider、虚拟路径、文件工具安全边界
- **关联垂直切片**：[上传与 artifact](slice-upload-sandbox-artifact/lessons/0001-flow-map.html)

### module-subagents — Subagent 系统
- **[📘 模块导览短课](module-subagents/lessons/0001-subagents-module-tour.html)**
- **[📄 模块总览参考](module-subagents/reference/subagents-overview.html)**
  > 职责：task tool、executor、状态契约、并发限制
- **关联垂直切片**：[subagent 委派](slice-subagent-delegation/lessons/0001-flow-map.html)

### module-skills — Skills 系统
- **[📘 模块导览短课](module-skills/lessons/0001-skills-module-tour.html)**
- **[📄 模块总览参考](module-skills/reference/skills-overview.html)**
  > 职责：skill 解析、安装、slash 激活、allowed-tools 策略
- **关联垂直切片**：[skill 激活](slice-skill-activation/lessons/0001-flow-map.html)

### module-memory-context — Memory 与 summarization
- **[📘 模块导览短课](module-memory-context/lessons/0001-memory-context-module-tour.html)**
- **[📄 模块总览参考](module-memory-context/reference/memory-context-overview.html)**
  > 职责：Memory / Summarization / DurableContext 三轨上下文管理
- **关联垂直切片**：[memory 注入与异步更新](slice-memory-update-injection/lessons/0001-flow-map.html)

### module-channels — IM channels 与 GitHub webhook
- **[📘 模块导览短课](module-channels/lessons/0001-channels-module-tour.html)**
- **[📄 模块总览参考](module-channels/reference/channels-overview.html)**
  > 职责：MessageBus、ChannelManager、8 平台 adapter、GitHub webhook
- **关联垂直切片**：[IM 入站消息执行](slice-im-channel-run/lessons/0001-flow-map.html)

### module-frontend-workspace — Frontend workspace
- **[📘 模块导览短课](module-frontend-workspace/lessons/0001-frontend-workspace-module-tour.html)**
- **[📄 模块总览参考](module-frontend-workspace/reference/frontend-workspace-overview.html)**
  > 职责：工作区页面、聊天 UI、artifact 面板、sidecar
- **关联垂直切片**：[聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) · [自定义 agent](slice-custom-agent-management/lessons/0001-flow-map.html)

### module-frontend-core — Frontend core 数据层
- **[📘 模块导览短课](module-frontend-core/lessons/0001-frontend-core-module-tour.html)**
- **[📄 模块总览参考](module-frontend-core/reference/frontend-core-overview.html)**
  > 职责：LangGraph SDK + REST 双通道、认证外壳、React Query hooks
- **关联垂直切片**：[聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html)

### module-config-deploy — 配置与部署
- **[📘 模块导览短课](module-config-deploy/lessons/0001-config-deploy-module-tour.html)**
- **[📄 模块总览参考](module-config-deploy/reference/config-deploy-overview.html)**
  > 职责：config.yaml、Makefile、scripts、Docker 整栈编排
- **关联垂直切片**：[配置热加载边界](slice-config-hot-reload/lessons/0001-flow-map.html)

---

## 🔪 L2 · 垂直切片

| 切片 | 主课 | 所属模块 |
|------|------|----------|
| [聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) | ChatPage → SDK → Gateway → worker → lead agent | gateway, lead-agent, runtime, frontend |
| [skill slash 激活](slice-skill-activation/lessons/0001-flow-map.html) | `/skill` 注入 + read_file 递进加载 | skills, lead-agent |
| [subagent 委派](slice-subagent-delegation/lessons/0001-flow-map.html) | task tool → executor → SSE → SubtaskCard | subagents, runtime, workspace |
| [上传与 artifact](slice-upload-sandbox-artifact/lessons/0001-flow-map.html) | 前端上传 → Gateway → sandbox → artifacts API | sandbox, gateway, workspace |
| [memory 注入与更新](slice-memory-update-injection/lessons/0001-flow-map.html) | MemoryMiddleware → queue → updater → 注入 | memory-context, lead-agent |
| [配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html) | 热加载 vs 启动快照边界 | config-deploy, gateway, tools-mcp |
| [定时任务执行](slice-scheduled-task-run/lessons/0001-flow-map.html) | 前端创建 → 调度器 → launch_run | runtime, gateway, workspace |
| [IM 入站消息](slice-im-channel-run/lessons/0001-flow-map.html) | adapter → MessageBus → ChannelManager → run | channels, runtime |
| [自定义 agent 管理](slice-custom-agent-management/lessons/0001-flow-map.html) | bootstrap 向导 + REST CRUD | gateway, lead-agent, workspace |
| [goal 自动续跑](slice-goal-continuation/lessons/0001-flow-map.html) | evaluator 判定 → 隐藏续跑 HumanMessage | runtime, lead-agent |

---

## 🔬 L3 · 微观 API（12 篇）

| 模块 | API 参考 |
|------|----------|
| gateway | [gateway-api.html](module-gateway/reference/gateway-api.html) |
| lead-agent | [lead-agent-api.html](module-lead-agent/reference/lead-agent-api.html) |
| runtime-persistence | [runtime-persistence-api.html](module-runtime-persistence/reference/runtime-persistence-api.html) |
| tools-mcp | [tools-mcp-api.html](module-tools-mcp/reference/tools-mcp-api.html) |
| sandbox | [sandbox-api.html](module-sandbox/reference/sandbox-api.html) |
| subagents | [subagents-api.html](module-subagents/reference/subagents-api.html) |
| skills | [skills-api.html](module-skills/reference/skills-api.html) |
| memory-context | [memory-context-api.html](module-memory-context/reference/memory-context-api.html) |
| channels | [channels-api.html](module-channels/reference/channels-api.html) |
| frontend-workspace | [frontend-workspace-api.html](module-frontend-workspace/reference/frontend-workspace-api.html) |
| frontend-core | [frontend-core-api.html](module-frontend-core/reference/frontend-core-api.html) |
| config-deploy | [config-deploy-api.html](module-config-deploy/reference/config-deploy-api.html) |

---

## 🧠 L4 · 深度剖析

| 主题 | 课程 | 关联 |
|------|------|------|
| [goal 续跑机制](deep-dive-goal-continuation/lessons/0001-problem-frame.html) | [0002 核心机制](deep-dive-goal-continuation/lessons/0002-core-mechanism.html) | [L2 goal 续跑](slice-goal-continuation/lessons/0001-flow-map.html) |
| [deferred tool_search](deep-dive-deferred-tool-search/lessons/0001-problem-frame.html) | [参考笔记](deep-dive-deferred-tool-search/reference/deferred-tool-search-notes.html) | [L2 配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html) |
| [memory 双入队](deep-dive-memory-dual-queue/lessons/0001-problem-frame.html) | [参考笔记](deep-dive-memory-dual-queue/reference/memory-dual-queue-notes.html) | [L2 memory 注入](slice-memory-update-injection/lessons/0001-flow-map.html) |
| [配置热加载边界](deep-dive-config-reload-boundary/lessons/0001-problem-frame.html) | [参考笔记](deep-dive-config-reload-boundary/reference/config-reload-boundary-notes.html) | [L2 配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html) |

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 教学主题 | 27（1 L0 + 12 L1 + 10 L2 + 4 L4） |
| HTML 短课 | 25 |
| HTML 参考页 | 39（含 12 篇 L3 API） |
| 主题审计 | 27/27 通过 |
| Goal 总数 | 39/39 完成 |
| 源码文件总量 | ~1335（含豁免） |
| 已引用讲解 | ~180+ 核心源文件（via SNAPSHOT） |

---

## 🗺️ 推荐学习路径

1. **全局地图** → [L0 项目导览](00-overview/lessons/0001-project-map.html)
2. **后端主干** → gateway → lead-agent → runtime-persistence → tools-mcp
3. **前端双轨** → frontend-core → frontend-workspace
4. **能力扩展** → skills → subagents → sandbox → memory-context → channels
5. **端到端切片** → [聊天流式执行](slice-chat-streaming-run/lessons/0001-flow-map.html) 作为第一条垂直切片
6. **运维部署** → config-deploy → [配置热加载](slice-config-hot-reload/lessons/0001-flow-map.html)
