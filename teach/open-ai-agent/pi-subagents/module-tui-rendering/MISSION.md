# 使命：TUI 结果渲染与 async widget 模块

## 为什么
学习者希望能快速读懂 `pi-subagents` 如何把 subagent 执行状态、输出、错误、并行进度和后台任务压缩成终端可读的 TUI。掌握这一层后，排查“为什么 UI 这样显示”“状态计数从哪里来”“展开与折叠有什么差别”时，可以先定位渲染分支，而不是直接陷入执行器或后台 runner。

## 成功的样子
- 能用一句话说明 `open-ai-agent/pi-subagents/src/tui/render.ts` 的职责边界。
- 能区分 foreground result 渲染入口 `renderSubagentResult` 和 background async widget 渲染入口 `renderWidget`。
- 能解释 compact/expanded、single/multi、running/done/failed/paused/empty-output 的主要分支。
- 能指出 `open-ai-agent/pi-subagents/src/tui/render-helpers.ts` 与 `open-ai-agent/pi-subagents/src/shared/status-format.ts` 各自负责的辅助格式化角色。
- 能根据测试文件找到至少一个行为佐证，而不是只凭源码阅读下结论。

## 约束条件
- 本轮只生成 L1 短课与参考页，lesson 控制在 15 分钟内完成。
- 只聚焦 TUI 渲染与 async widget；运行器、agent discovery、intercom、slash workflow 只在解释输入数据时少量引用。
- 所有源码路径引用使用 `open-ai-agent/pi-subagents/...` 前缀。
- 只写入 `teach/open-ai-agent/pi-subagents/module-tui-rendering/`。

## 不在范围内
- 不深入讲解 foreground single、parallel、chain 的执行算法。
- 不展开后台 run 的完整生命周期、status 文件写入协议或 wait 工具行为。
- 不分析 Pi TUI 库内部组件实现，只讲本项目如何调用 `Container`、`Text`、`Markdown` 等组件。
