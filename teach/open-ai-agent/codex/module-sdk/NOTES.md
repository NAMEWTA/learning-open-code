# 教学笔记：Python 与 TypeScript SDK

- 用户要求本主题作为 teach-goal 的 L1 worker 产物生成，必须使用简体中文。
- lesson 只讲 SDK 模块导览和最小调用序列；完整 API、依赖和源码阅读顺序放在 `reference/sdk-overview.html`。
- Python SDK 和 TypeScript SDK 的最大差异：Python 通过 `codex app-server --listen stdio://` 使用 JSON-RPC 长连接；TypeScript 通过 `codex exec --experimental-json` 使用每次 turn 的 JSONL 子进程流。
- 不要修改项目级 `index.md`、进度文件、源项目或其他主题目录。
