# 使命：MCP 延迟工具发现（deferred tool search）

## 为什么
接入多个 MCP server 后，每个工具的 JSON schema 会迅速占满模型上下文。我想理解 DeerFlow 在 `tool_search.enabled` 下如何把 MCP 工具「只露名字、按需拉 schema」，以及 fail-closed 与 catalog hash 如何防止静默泄漏或陈旧 promotion。

## 成功的样子
- 能说明「全量 bind_tools」与「延迟发现 + promote」的 token 与可发现性权衡
- 画出 assemble → middleware 过滤 → tool_search promote → 下一轮 bind 的闭环
- 遇到 MCP schema 意外暴露或 promote 失效时，知道查哪三个文件与哪几条测试

## 约束条件
- 以 monorepo 子模块 `open-ai-agent/deer-flow` 当前 harness 源码为准
- 先读过 `module-tools-mcp` 导览更佳；本主题为 L4 深度剖析，单节 15 分钟

## 不在范围内
- MCP client 传输层（stdio/SSE/HTTP）与 cache 失效细节（见 module-tools-mcp）
- skills 侧的 `deferred_discovery` / `describe_skill` 平行机制（见 module-skills）
