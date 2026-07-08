# TUI 结果渲染与 async widget 模块资源

## 知识

- `open-ai-agent/pi-subagents/src/tui/render.ts`
  核心渲染模块。适用于理解 foreground result 的 compact/expanded 渲染、multi-result 行标签、async widget 行生成、状态 glyph、宽度裁剪和拥挤终端降级。
- `open-ai-agent/pi-subagents/src/tui/render-helpers.ts`
  TUI 辅助格式化函数。适用于理解列表过滤、边框行、居中 header/footer、路径缩写和滚动提示等较通用的终端文本工具。
- `open-ai-agent/pi-subagents/src/shared/status-format.ts`
  状态文案聚合函数。适用于解释 activity age、parallel outcome 和 step status 聚合如何在 result 与 widget 两侧复用。
- `open-ai-agent/pi-subagents/src/shared/types.ts`
  渲染输入类型定义。适用于确认 `Details`、`AgentProgress`、`AsyncJobState`、`AsyncJobStep`、`NestedRunSummary` 的字段含义。
- `open-ai-agent/pi-subagents/src/runs/background/async-job-tracker.ts`
  async widget 数据来源。适用于理解后台 run summary 如何转换成 `AsyncJobState`，再交给 `renderWidget` 刷新 UI。
- `open-ai-agent/pi-subagents/src/extension/index.ts`
  渲染入口接入点。适用于确认 `renderSubagentResult` 如何接到 tool result renderer，以及 `renderWidget` 如何在 tool result 后刷新。
- `open-ai-agent/pi-subagents/test/unit/render-helpers.test.ts`
  行为佐证：行裁剪、多行内容规范化、dynamic fanout span、total cost、静态 sequential/parallel chain 标签。
- `open-ai-agent/pi-subagents/test/integration/render-widget.test.ts`
  行为佐证：async widget 排序、parallel wording、拥挤终端 progressive fallback、expanded live detail、隐藏 job 计数、稳定 glyph 行为。
- `open-ai-agent/pi-subagents/test/integration/render-fork-badge.test.ts`
  行为佐证：fork badge、compact 运行态详情、错误原因、暂停、空输出 warning、parallel/chain 标签。
- `open-ai-agent/pi-subagents/test/unit/status-format.test.ts`
  行为佐证：activity label、step status 聚合和 parallel outcome 文案。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  适用于把 TUI 显示、async widget 拥挤布局或状态文案的设计疑问拿到维护者上下文中验证。

## 空白

- 当前仓库没有单独的 TUI 渲染设计文档；本主题以源码、类型定义和测试断言作为主要依据。
- 当前没有收录 `@earendil-works/pi-tui` 的官方 API 文档副本；本主题只解释本项目实际调用到的组件和宽度函数。
- 本轮不追溯历史 issue 或 PR 讨论；如果后续要解释“为什么改成当前布局”，应补充维护者讨论或提交历史。
