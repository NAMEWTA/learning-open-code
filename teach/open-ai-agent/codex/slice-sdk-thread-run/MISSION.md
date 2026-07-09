# 使命：SDK startThread/run 到 Codex 事件消费链路

## 为什么
用户希望通过 SDK（TypeScript 或 Python）编程式调用 Codex agent，理解从调用 `startThread()`/`run()` 到消费流式事件的全链路机制，以便在自定义应用中集成 Codex 能力，并能自主排查集成问题。

## 成功的样子
- 能画出 TypeScript SDK 和 Python SDK 各自的调用链路时序图
- 能解释 `CodexExec.run()` 如何通过子进程 JSONL 与 Rust 二进制通信
- 能在 SDK 事件流中正确区分 thread.started、turn.completed、turn.failed 等关键事件
- 能识别连接断开、进程异常退出、thread 不存在三类典型故障并给出排查方向

## 约束条件
- 以 TypeScript SDK 为主线，Python SDK 作为对照讲解
- 每节 15 分钟内可完成，控制在 1200 字以内
- 不深入 app-server 协议细节（已在 L1-module-app-server 中覆盖）

## 不在范围内
- app-server JSON-RPC 协议设计与消息路由实现（见 L1-module-app-server）
- Rust exec 模块内部 agent 循环（见 L1-module-core-runtime）
- SDK 的登录、账号管理、模型列表等非 thread/run 路径
