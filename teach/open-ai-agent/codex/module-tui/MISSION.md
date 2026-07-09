# 使命：TUI 交互式终端界面

## 为什么
学习者希望从 0 到 1 掌握 Codex CLI 的交互式终端架构，能够读懂无子命令启动后如何进入 TUI、如何把用户输入转成 core 可执行的请求，以及 UI 状态如何反映 agent 运行进度。

## 成功的样子
- 能指出 `codex-tui` crate 在 CLI、app-server、core 协议与终端渲染之间的边界。
- 能沿着一次交互输入说明 `run_main`、`App`、`ChatWidget`、`BottomPane` 的职责分工。
- 能为后续 L2 垂直切片学习定位应阅读的源码文件，而不是在 TUI 大模块中迷路。

## 约束条件
- 本主题服务于批量生成的 Codex 架构课程，每节 lesson 控制在 15 分钟内完成。
- 本次 L1 只建立模块地图，复杂事件路径、渲染细节、测试策略留给 L2/L3/L4。
- 教学材料必须基于当前子模块源码快照，并通过 teach 审计脚本。

## 不在范围内
- 不讲 ratatui 的完整渲染 API 教程。
- 不展开 app-server/core 的内部执行循环。
- 不覆盖所有 slash command、插件、协作 agent、历史回放和终端图片功能。
