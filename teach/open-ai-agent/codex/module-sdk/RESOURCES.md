# Python 与 TypeScript SDK 资源

## 知识

- [Python SDK README](../../../../open-ai-agent/codex/sdk/python/README.md)
  Python SDK 的安装、认证、quickstart 和官方文档入口。适用于确认用户可见的同步调用方式。
- [Python SDK pyproject](../../../../open-ai-agent/codex/sdk/python/pyproject.toml)
  包名、运行时依赖、Python 版本、测试和格式化配置。适用于判断 SDK 如何绑定 pinned CLI runtime。
- [Python SDK public API](../../../../open-ai-agent/codex/sdk/python/src/openai_codex/api.py)
  `Codex`、`AsyncCodex`、`Thread`、`TurnHandle` 等公开封装。适用于阅读 Python 对外 API 和调用链。
- [Python SDK low-level client](../../../../open-ai-agent/codex/sdk/python/src/openai_codex/client.py)
  app-server stdio 子进程、JSON-RPC 请求、通知路由和 turn stream。适用于追踪 Python SDK 内部分层。
- [Python runtime package](../../../../open-ai-agent/codex/sdk/python-runtime/README.md)
  `openai-codex-cli-bin` 的 wheel-only runtime 包说明。适用于理解 Python SDK 为什么能固定 Codex CLI。
- [TypeScript SDK README](../../../../open-ai-agent/codex/sdk/typescript/README.md)
  TypeScript SDK 的 quickstart、streaming、结构化输出、图片输入、恢复 thread 和配置覆盖。适用于确认 Node 侧用户体验。
- [TypeScript SDK package.json](../../../../open-ai-agent/codex/sdk/typescript/package.json)
  npm 包名、Node 版本、构建测试脚本和依赖。适用于判断 TypeScript SDK 的发布形态。
- [TypeScript SDK source](../../../../open-ai-agent/codex/sdk/typescript/src/index.ts)
  导出面、`Codex`、`Thread`、事件和 item 类型。适用于阅读 TypeScript 对外 API 清单。
- [Python SDK tests](../../../../open-ai-agent/codex/sdk/python/tests/)
  public API、JSON-RPC routing、streaming、app-server 集成测试。适用于验证公开 API 和内部协议行为。
- [TypeScript SDK tests](../../../../open-ai-agent/codex/sdk/typescript/tests/)
  run、runStreamed、exec 参数、AbortSignal 和 binary resolution 测试。适用于验证 CLI JSONL 调用链。

## 智慧（社区）

- [Codex GitHub Issues](https://github.com/openai/codex/issues)
  真实用户会在这里暴露 SDK 使用、安装、运行时路径和事件兼容问题。适用于后续验证学习结论是否贴近实践。

## 空白

- 当前主题只基于仓库内 SDK 源码和官方 README；没有引入第三方教程，因为 SDK API 仍处于 beta/dev 形态，第三方材料更容易滞后。
