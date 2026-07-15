# 使命：Agent 核心引擎

## 为什么
理解 Hermes Agent 最核心的 agent/ 模块——这是整个框架的中枢引擎，所有用户入口（CLI、TUI、Web、20+ 消息平台）的消息最终都通过它驱动完整的对话生命周期。掌握 agent/ 的内部架构后，才能看懂 Hermes Agent 如何实现自进化学习闭环，以及如何在库模式下集成 Hermes Agent 到自己的应用中。

## 成功的样子
- 能画出 agent/ 模块的内部四层架构图（对话循环层 → 工具执行层 → 记忆管理层 → 上下文压缩层）
- 能说出 conversation_loop.py、tool_executor.py、context_compressor.py、memory_manager.py 各文件的职责
- 能写出一个最小化的 AIAgent 库模式调用示例（5 行代码启动一次对话）
- 能解释 run_conversation() 的一次调用如何串联起 agent/ 下的各个子模块

## 约束条件
- 学习方式：阅读教学课程 + 对照源码验证
- 先修要求：已完成 L0 Hermes Agent 项目总览，理解整体分层架构
- 本模块聚焦 agent/ 目录本身，不深入 tools/、providers/ 等下游模块

## 不在范围内
- tools/ 目录下各个工具的内部实现（terminal_tool、browser_tool 等，属于 tools 模块课程）
- providers/ 目录下各模型提供商的适配细节（属于 providers 模块课程）
- gateway/ 消息网关的平台适配逻辑（属于 gateway 模块课程）
- CLI 命令的逐个使用教程（属于用户手册范畴）
