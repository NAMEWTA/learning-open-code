# Hermes Agent · 架构教学 Wiki

> 📊 整体进度：18/18 goals · 100% · 已执行 5 轮
> 🕐 最后更新：2026-07-09

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ██████████ 100% |
| L1 模块总览 | 12 | 12 | ██████████ 100% |
| L2 垂直切片 | 5 | 5 | ██████████ 100% |
| L3 微观 API | 0 | * | 已通过 L1 reference 覆盖 |
| L4 深度剖析 | 0 | * | 待后续按需触发 |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟建立全局地图：分层架构、20+ 目录、五条设计哲学、豁免清单。
- **[📄 Hermes Agent 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：Python 3.11+ · Fire CLI · Rich TUI · 异步网关 · Agent Skills 标准

---

## 📦 L1 · 模块总览

### module-agent-core — Agent 核心引擎
- **[📘 模块导览](module-agent-core/lessons/0001-agent-core-module-tour.html)** — 四层架构：对话循环→工具执行→记忆管理→上下文压缩
- **[📄 参考](module-agent-core/reference/agent-core-overview.html)** — 接口清单、依赖关系、文件索引
- **关联切片**：[🔪 Agent 对话全链路](slice-agent-conversation-loop/lessons/0001-flow-map.html)

### module-agent-entry — Agent 入口层
- **[📘 模块导览](module-agent-entry/lessons/0001-agent-entry-module-tour.html)** — CLI 启动、主运行循环、状态持久化、日志配置
- **[📄 参考](module-agent-entry/reference/agent-entry-overview.html)** — 13 文件职责、依赖矩阵、配置路径

### module-gateway — 消息网关
- **[📘 模块导览](module-gateway/lessons/0001-gateway-module-tour.html)** — 三层架构：平台适配→中继路由→投递
- **[📄 参考](module-gateway/reference/gateway-overview.html)** — 24 平台全表、DeliveryRouter 四级回退
- **关联切片**：[🔪 多平台消息全链路](slice-multi-platform-message/lessons/0001-flow-map.html)

### module-tools — 工具层
- **[📘 模块导览](module-tools/lessons/0001-tools-module-tour.html)** — 四大子系统：终端/浏览器/委托/审批
- **[📄 参考](module-tools/reference/tools-overview.html)** — 92 文件索引、审批三层安全闸门
- **关联切片**：[🔪 工具执行与审批全链路](slice-tool-execution-approval/lessons/0001-flow-map.html)

### module-skills — 技能系统
- **[📘 模块导览](module-skills/lessons/0001-skills-module-tour.html)** — SKILL.md 规范、Skills Hub 七源发现、策展器状态机
- **[📄 参考](module-skills/reference/skills-overview.html)** — 品类目录、接口清单、源码索引
- **关联切片**：[🔪 技能生命周期全链路](slice-skill-lifecycle/lessons/0001-flow-map.html)

### module-cli-framework — CLI 框架
- **[📘 模块导览](module-cli-framework/lessons/0001-cli-framework-module-tour.html)** — argparse 命令树、子命令插件化、配置补全
- **[📄 参考](module-cli-framework/reference/cli-framework-overview.html)** — 40+ 子命令清单、Builder 接口、分发流程图

### module-plugins — 插件系统
- **[📘 模块导览](module-plugins/lessons/0001-plugins-module-tour.html)** — 四源五态加载、PluginContext 注册、23 Hook 生命周期
- **[📄 参考](module-plugins/reference/plugins-overview.html)** — 形态矩阵、Hook 全表、依赖关系图

### module-providers — 模型提供商
- **[📘 模块导览](module-providers/lessons/0001-providers-module-tour.html)** — ProviderProfile 声明式抽象、注册中心懒加载
- **[📄 参考](module-providers/reference/providers-overview.html)** — 17 字段全表、6 钩子签名、10 下游消费者

### module-cron — 定时任务调度
- **[📘 模块导览](module-cron/lessons/0001-cron-module-tour.html)** — tick 调度循环、croniter 集成、lifecycle_guard
- **[📄 参考](module-cron/reference/cron-overview.html)** — API 速查、平台路由表、安全蓝图
- **关联切片**：[🔪 定时任务全链路](slice-cron-scheduled-task/lessons/0001-flow-map.html)

### module-tui — 终端 UI
- **[📘 模块导览](module-tui/lessons/0001-tui-module-tour.html)** — React+Ink 双进程架构、JSON-RPC 通信
- **[📄 参考](module-tui/reference/tui-overview.html)** — 25 文件索引、20 事件类型、RPC 方法速查

### module-acp — Agent Client Protocol
- **[📘 模块导览](module-acp/lessons/0001-acp-module-tour.html)** — stdio JSON-RPC 传输、线程安全事件桥接
- **[📄 参考](module-acp/reference/acp-overview.html)** — ToolKind 映射、编辑审批策略、斜杠命令表

### module-web — Web 仪表盘
- **[📘 模块导览](module-web/lessons/0001-web-module-tour.html)** — FastAPI+SPA 架构、PluginManifest 插件系统
- **[📄 参考](module-web/reference/web-overview.html)** — 18 页面索引、14 API 端点族、Provider 层级链

---

## 🔪 L2 · 垂直切片

### slice-agent-conversation-loop — Agent 对话全链路
- **[📘 链路地图](slice-agent-conversation-loop/lessons/0001-flow-map.html)**
  > 六阶段：CLI → Init → Conversation Loop → Provider API → Response → Context Compress
  > 所属模块：[module-agent-core](module-agent-core/reference/agent-core-overview.html)、[module-agent-entry](module-agent-entry/reference/agent-entry-overview.html)

### slice-tool-execution-approval — 工具执行与审批全链路
- **[📘 链路地图](slice-tool-execution-approval/lessons/0001-flow-map.html)**
  > Tool Call → Registry → HARDLINE(12条) → DANGEROUS(47条) → Smart → Execute
  > 所属模块：[module-tools](module-tools/reference/tools-overview.html)、[module-agent-core](module-agent-core/reference/agent-core-overview.html)

### slice-skill-lifecycle — 技能生命周期全链路
- **[📘 链路地图](slice-skill-lifecycle/lessons/0001-flow-map.html)**
  > Task Complete → Curator → Template → Write → Register → Track → Self-Improve/Archive
  > 所属模块：[module-skills](module-skills/reference/skills-overview.html)

### slice-multi-platform-message — 多平台消息全链路
- **[📘 链路地图](slice-multi-platform-message/lessons/0001-flow-map.html)**
  > Platform → Adapter → Relay → Agent → Delivery Router → Platform Send
  > 所属模块：[module-gateway](module-gateway/reference/gateway-overview.html)

### slice-cron-scheduled-task — 定时任务全链路
- **[📘 链路地图](slice-cron-scheduled-task/lessons/0001-flow-map.html)**
  > NL Parse → Expression → Persist → Tick → Execute → Guard → Deliver
  > 所属模块：[module-cron](module-cron/reference/cron-overview.html)、[module-gateway](module-gateway/reference/gateway-overview.html)

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| L0 项目总览 | 1 篇 |
| L1 模块总览 | 12 篇（含 12 篇 reference） |
| L2 垂直切片 | 5 个（各含 1 节短课） |
| 教学短课合计 | 18 节 |
| 参考文档合计 | 13 篇 |
| 覆盖顶层目录 | 12/12（100%） |
| 覆盖核心功能链路 | 5 条 |
| 审查状态 | 全部 conditional_pass（Critical 已修复） |
