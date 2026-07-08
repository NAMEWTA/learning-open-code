# pi-subagents · 架构教学 Wiki

> 📊 整体进度：19/19 goals · 100% · 已执行 4 轮
> 🕐 最后更新：2026-07-08

---

## 📋 进度面板

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ████████ |
| L1 模块总览 | 10 | 10 | ████████ |
| L2 垂直切片 | 7 | 7 | ████████ |
| L3 微观 API | 1 | 1 | ████████ |
| L4 深度剖析 | 0 | 0 | — |

---

## 🏗️ L0 · 项目总览

- **[📘 项目导览短课](00-overview/lessons/0001-project-map.html)**
  > 15 分钟说清 pi-subagents 的定位、运行边界和后续阅读路线。
- **[📄 项目总览参考](00-overview/reference/00-overview.html)**
  > 技术栈：TypeScript + Pi extension · 架构：extension / runs / agents / slash 分层 · 10 个顶层模块

---

## 📦 L1 · 模块总览

### module-extension-runtime — 扩展入口与 Pi runtime 注册
- **[📘 模块导览短课](module-extension-runtime/lessons/0001-extension-runtime-module-tour.html)**
- **[📄 模块总览参考](module-extension-runtime/reference/extension-runtime-overview.html)**
- **关联切片**：[单次前台 run](slice-single-foreground-run/lessons/0001-flow-map.html) · [Slash→executor](slice-slash-to-executor/lessons/0001-flow-map.html) · [Agent 管理配置](slice-agent-management-config/lessons/0001-flow-map.html)

### module-agent-system — Agent 发现、配置与内置角色
- **[📘 模块导览短课](module-agent-system/lessons/0001-agent-system-module-tour.html)**
- **[📄 模块总览参考](module-agent-system/reference/agent-system-overview.html)**
- **关联切片**：[Agent 管理配置全链路](slice-agent-management-config/lessons/0001-flow-map.html) · [parallel/chain](slice-parallel-chain-execution/lessons/0001-flow-map.html)

### module-runs-execution — 前台、后台与链式运行核心
- **[📘 模块导览短课](module-runs-execution/lessons/0001-runs-execution-module-tour.html)**
- **[📄 模块总览参考](module-runs-execution/reference/runs-execution-overview.html)**
- **[🔬 API 参考 (L3)](module-runs-execution/reference/runs-execution-api.html)** — 16 个辅助 runs 模块文件
- **关联切片**：[单次前台 run](slice-single-foreground-run/lessons/0001-flow-map.html) · [async lifecycle](slice-async-lifecycle-status-wait/lessons/0001-flow-map.html) · [模型预算边界](slice-model-scope-budget-guardrails/lessons/0001-flow-map.html)

### module-shared-infra — 共享类型、状态与文件基础设施
- **[📘 模块导览短课](module-shared-infra/lessons/0001-shared-infra-module-tour.html)**
- **[📄 模块总览参考](module-shared-infra/reference/shared-infra-overview.html)**
- **关联切片**：[parallel/chain](slice-parallel-chain-execution/lessons/0001-flow-map.html) · [async lifecycle](slice-async-lifecycle-status-wait/lessons/0001-flow-map.html)

### module-slash-workflows — Slash 命令与 prompt workflow
- **[📘 模块导览短课](module-slash-workflows/lessons/0001-slash-workflows-module-tour.html)**
- **[📄 模块总览参考](module-slash-workflows/reference/slash-workflows-overview.html)**
- **关联切片**：[Slash→executor](slice-slash-to-executor/lessons/0001-flow-map.html)

### module-intercom — 父子进程 intercom 与 supervisor 协调
- **[📘 模块导览短课](module-intercom/lessons/0001-intercom-module-tour.html)**
- **[📄 模块总览参考](module-intercom/reference/intercom-overview.html)**
- **关联切片**：[Native supervisor 全链路](slice-native-supervisor-intercom/lessons/0001-flow-map.html)

### module-tui-rendering — TUI 结果渲染与 async widget
- **[📘 模块导览短课](module-tui-rendering/lessons/0001-tui-rendering-module-tour.html)**
- **[📄 模块总览参考](module-tui-rendering/reference/tui-rendering-overview.html)**

### module-profiles — 模型 profile 与供应商能力探测
- **[📘 模块导览短课](module-profiles/lessons/0001-profiles-module-tour.html)**
- **[📄 模块总览参考](module-profiles/reference/profiles-overview.html)**
- **关联切片**：[模型预算边界](slice-model-scope-budget-guardrails/lessons/0001-flow-map.html)

### module-packaging-assets — 安装、发布资产与内置 skills/prompts
- **[📘 模块导览短课](module-packaging-assets/lessons/0001-packaging-assets-module-tour.html)**
- **[📄 模块总览参考](module-packaging-assets/reference/packaging-assets-overview.html)**

### module-test-suite — 测试体系与行为佐证
- **[📘 模块导览短课](module-test-suite/lessons/0001-test-suite-module-tour.html)**
- **[📄 模块总览参考](module-test-suite/reference/test-suite-overview.html)**

---

## 🔪 L2 · 垂直切片

### slice-single-foreground-run — 单次前台 subagent run
- **[📘 链路地图](slice-single-foreground-run/lessons/0001-flow-map.html)** · [📄 速查](slice-single-foreground-run/reference/single-foreground-run-flow-map.html)
  > 八跳：注册 → 门卫 → 准备 → runSync → spawn → JSONL → 收尾 → 包装
  > 所属模块：[module-runs-execution](module-runs-execution/reference/runs-execution-overview.html)

### slice-parallel-chain-execution — parallel 与 chain execution
- **[📘 链路地图](slice-parallel-chain-execution/lessons/0001-flow-map.html)** · [📄 速查](slice-parallel-chain-execution/reference/parallel-chain-overview.html)
  > sequential / static parallel / dynamic fanout 三分支
  > 所属模块：[module-runs-execution](module-runs-execution/reference/runs-execution-overview.html)

### slice-async-lifecycle-status-wait — async lifecycle、status 与 wait
- **[📘 课程 1：链路地图](slice-async-lifecycle-status-wait/lessons/0001-flow-map.html)**
- **[📘 课程 2：status/wait](slice-async-lifecycle-status-wait/lessons/0002-status-wait-complete.html)** · [📄 速查](slice-async-lifecycle-status-wait/reference/async-lifecycle-flow-map.html)
  > 五段：点火 → 写盘 → 内存投影 → status/wait → 完成通知

### slice-agent-management-config — Agent 管理、覆盖与配置解析
- **[📘 课程 1：双路径地图](slice-agent-management-config/lessons/0001-flow-map.html)**
- **[📘 课程 2–4：frontmatter / settings / 边界](slice-agent-management-config/lessons/0002-frontmatter-parse.html)** · [📄 速查](slice-agent-management-config/reference/agent-management-config-flow-map.html)

### slice-slash-to-executor — Slash 命令到 executor 桥接
- **[📘 链路地图](slice-slash-to-executor/lessons/0001-flow-map.html)** · [📄 速查](slice-slash-to-executor/reference/slash-to-executor-flow-map.html)
  > 八跳：解析 → live card → request → bridge → executor → 分流 → update → finalize

### slice-native-supervisor-intercom — Native supervisor 与 intercom 协调
- **[📘 课程 1–3](slice-native-supervisor-intercom/lessons/0001-flow-map.html)** · [📄 速查](slice-native-supervisor-intercom/reference/native-supervisor-intercom-flow-map.html)
  > bridge 注入 → 环境写入 → 运行中协调 → 执行完成 → 结果回传

### slice-model-scope-budget-guardrails — 模型范围、预算与安全边界
- **[📘 链路地图](slice-model-scope-budget-guardrails/lessons/0001-flow-map.html)** · [📄 速查](slice-model-scope-budget-guardrails/reference/model-scope-budget-guardrails-flow-map.html)
  > 九跳：配置 → 发现 → 预处理 → modelScope → spawn → 子 runtime → prompt 安全 → tool/turn budget

---

## 📊 源码覆盖统计

| 指标 | 数值 |
|------|------|
| 生产源码 `.ts` 文件 | 92 / 92（100%） |
| teach 主题目录 | 18 |
| HTML 短课 | 24 节 |
| HTML 参考文档 | 19 份 |
| 源 commit | `3ccb564`（main） |
| 豁免文件 | `node_modules/`、二进制资源、测试 fixture 数据 |

---

## 建议后续深化（非阻塞）

- L4：`dynamic-fanout` 空结果策略、`completion-batcher` 去重设计
- L3：其他模块独立 API 参考页（agents、shared-infra 等）可按需追加
- 修订：L1-slash-workflows / packaging-assets 审查中的 Important 项（L0 回链、依赖表、prompt description 补全）
