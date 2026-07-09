# 教学笔记：App-server JSON-RPC 服务

- 本次任务是 L1 模块导览，重点建立地图：职责、位置、接口类别、内部分层、关键依赖和一个最小调用序列。
- 用户要求所有输出为中文，并明确禁止修改源项目、`.agents/`、`_progress.json`、`_progress.md`、`index.md`。
- `codex-rs/app-server/README.md` 的 API Overview 很长，课程只引用生命周期和核心原语，完整方法类别放入 reference。
- 后续 L2 可围绕 `turn/start` 从 JSON-RPC 入站、`TurnRequestProcessor` 到 core 事件流做垂直切片。
