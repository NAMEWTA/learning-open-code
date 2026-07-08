# 使命：Slash 命令与 prompt workflow 模块

## 为什么
学习者需要在阅读 pi-subagents 时快速判断一条用户输入的 slash 命令，尤其是 prompt workflow 模板命令，最终如何变成结构化的 subagent 执行请求。掌握这条链路后，后续排查命令解析、模板扩展、进度显示和 executor 衔接时不会迷失在事件桥与 UI 状态之间。

## 成功的样子
- 能从 `open-ai-agent/pi-subagents/src/extension/index.ts` 定位 slash bridge、prompt template bridge 和 `registerSlashCommands` 的注册位置。
- 能解释 `open-ai-agent/pi-subagents/prompts/*.md` 如何被 `prompt-workflows.ts` 发现、解析 frontmatter，并转换为 `SubagentParamsLike`。
- 能区分 `/run`、`/chain`、`/parallel` 等原生 slash 命令与 `/prompt-workflow`、`/chain-prompts` 两类模板命令的共同执行出口。
- 能用相关测试判断上下文选择、取消、进度更新、最终快照和 prompt 覆盖优先级是否被保护。

## 约束条件
- 本主题是 L1 模块总览，短课只聚焦“注册/模板进入执行链路”，长清单放入参考页。
- 源码范围以 `open-ai-agent/pi-subagents/src/slash/*.ts` 与 `open-ai-agent/pi-subagents/prompts/*.md` 为主，只少量引用 extension 入口、runs 执行衔接和测试证据。
- 所有课程引用的源码路径都必须带 `open-ai-agent/pi-subagents/...` 前缀。

## 不在范围内
- 不深入讲解 executor 内部的 single、parallel、chain 执行算法。
- 不展开 profiles、model catalog、doctor 等命令背后的业务实现。
- 不讲 TUI renderer 的具体绘制细节，只说明 live-state 给渲染层提供稳定快照。
