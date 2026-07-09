# 使命：CLI 与 npm 包装层

## 为什么
用户希望从 0 到 1 掌握 Codex CLI 的入口架构，能够解释一次 `codex` 命令如何从 npm 包装层进入 Rust CLI，并进一步分流到 exec、TUI、MCP、app-server 等运行模块。掌握这条边界后，后续阅读具体功能时可以先判断该从包装、分发还是业务 crate 入手。

## 成功的样子
- 能画出 `@openai/codex` npm 包、平台原生二进制、`codex-rs/cli` 之间的调用链。
- 能根据一个用户命令判断它会进入 TUI、exec、MCP、plugin、app-server、remote-control 或其他子模块。
- 能说清 `codex-rs/cli` 作为薄分发层依赖哪些关键 crate，以及哪些细节应该下钻到后续 L2/L3 课程。

## 约束条件
- 本课是 L1 模块导览，单节 lesson 控制在 15 分钟内完成。
- 只写入 `teach/open-ai-agent/codex/module-cli-packaging/`，不修改源项目和项目级进度文件。
- 以当前本地源码快照为事实来源，避免脱离源码扩写产品叙述。

## 不在范围内
- 不展开 TUI 渲染、core agent turn、app-server JSON-RPC 协议的内部实现。
- 不讲 release workflow 如何构建和发布各平台 npm optional package。
- 不分析认证、沙箱、模型请求、MCP OAuth、plugin marketplace 的完整业务逻辑。
