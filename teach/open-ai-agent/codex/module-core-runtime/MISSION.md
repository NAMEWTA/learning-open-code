# 使命：Core Thread/Turn 与模型上下文

## 为什么
学习者希望从 0 到 1 掌握 Codex CLI 的 agent 核心架构，能够在阅读 TUI、exec、app-server、tools、skills 等后续模块时，准确判断问题应当进入 core、protocol、core-api 还是周边 crate。这个主题的目标不是背诵所有文件，而是建立可复用的 Thread/Turn 阅读地图，避免被庞大的 `codex-core` 淹没。

## 成功的样子
- 能说明 `codex-core` 在 TUI、exec、app-server 与模型后端之间承担的编排职责。
- 能从 `ThreadManager`、`CodexThread`、`Op`、`EventMsg` 四个对象读懂一次最小 turn 的入口和输出。
- 能把上下文、任务类型、模型客户端、事件映射、MCP/skills/session 持久化分配到正确源码目录。
- 能识别哪些新功能不应该继续塞进 `codex-core`，而应优先考虑 protocol、tools、mcp、skills、config 或独立 crate。

## 约束条件
- 本次 L1 只建立模块地图，lesson 控制在 15 分钟内完成，细节留给后续 L2/L3/L4。
- 只写入 `teach/open-ai-agent/codex/module-core-runtime/`，不修改源项目和全局进度文件。
- 教学输出使用中文；Rust 标识符、crate 名、文件路径保持英文原文。

## 不在范围内
- 不逐行解释 `codex-rs/core/src/session/turn.rs`、工具执行、MCP 生命周期、skills 激活、app-server JSON-RPC 或 TUI 渲染。
- 不新增、重构或测试 `open-ai-agent/codex/` 源码。
- 不把 `codex-core` 当成万能入口；后续课程会专门拆解 tools、sandboxing、app-server、skills 等边界。
