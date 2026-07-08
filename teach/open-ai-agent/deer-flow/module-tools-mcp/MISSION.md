# 使命：Tools 与 MCP

## 为什么
学习者希望把 DeerFlow 的扩展能力从“配置里写了工具”落实到运行时链路：一个工具如何被加载、过滤、延迟暴露，并最终成为 agent 可调用集合。掌握这条链路后，能定位工具未出现、MCP schema 占用上下文、工具名冲突和权限泄漏这类真实问题。

## 成功的样子
- 能沿着 `get_available_tools()` 说明配置工具、内置工具、MCP 工具、ACP 工具进入同一工具集合的顺序。
- 能解释 `tool_search.enabled` 开启后，MCP 工具为什么先只出现在 prompt 名单中，直到 promote 后才暴露 schema。
- 能根据 Gateway MCP API、MCP cache、session pool 和测试锚点判断一个 MCP 配置问题应从哪里排查。

## 约束条件
- 本主题是 L1 模块课，只建立工具系统地图，不逐行讲完每个 built-in tool。
- lesson 必须保持 15 分钟内完成；长表格和测试索引放入 `reference/`。
- 输出只写入 `teach/open-ai-agent/deer-flow/module-tools-mcp/`。

## 不在范围内
- 不讲完整 MCP 协议规范或第三方 MCP server 开发。
- 不深入 Gateway 设置页的前端交互。
- 不展开 sandbox 文件工具、subagent executor、skills policy 的完整实现；这些保留给相邻模块或垂直切片。
