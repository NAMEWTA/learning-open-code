# 使命：AI 对话全链路 — 三条通道（API + CLI + MCP）的实现与切换

## 为什么
学习者在 L1-backend 中已了解 chat.py 的 OpenAI 兼容 function-calling 架构、cli_runtime.py 的多 CLI 支持、mcp_server.py 的 JSON-RPC over stdio 设计。现在需要将这些分散的模块串联成一条完整的端到端链路——从用户在 Settings 页面选择接入方式开始，经过 /api/chat 分发，到最终模型返回流式答案。理解这三条通道的差异和适用场景后，学习者才能在自己的投研工具中用对 AI 能力：知道什么时候该填 API key、什么时候该调本机 CLI、什么时候该暴露 MCP 工具给 agent。

## 成功的样子
- 能画出三条通道的完整数据流向：Settings 配置 → 前端 llm.ts 请求 → 后端 /api/chat 分发 → API/CLI 处理 → NDJSON 流回前端。
- 能说清 API 通道（function-calling 循环）与 CLI 通道（context-only）的本质差异，以及各自适合什么场景。
- 能解释 cli_runtime.py 如何用「system-file/stdin/arg」三种投递方式适配四种 CLI。
- 能理解 MCP server 如何复用 chat.TOOLS，将数据工具暴露为 JSON-RPC 标准接口。

## 约束条件
- 本主题是 L2 垂直切片，聚焦一条完整的业务链路，不展开 astock/gstock 数据源实现。
- 每节 lesson 保持 15 分钟内完成；源码索引和速查表分流到 reference。
- 教学产物只写入 `teach/open-trading/Vibe-Research/slice-ai-chat/`。
- 批量生成模式，MISSION 使用自动生成的默认使命，不交互等待用户输入。

## 不在范围内
- 不深入分析的 astock.py 腾讯/东财的 HTTP 请求构造。
- 不展开 SSRF 防护的逐行代码审计。
- 不分析前端 Settings.tsx 以外的其他页面组件。
- 不展开 VC/PE 估值模型的金融数学。
