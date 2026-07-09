# 使命：追踪 app-server JSON-RPC 的 thread/start 到 turn/start 完整链路

## 为什么
理解富客户端（IDE、桌面应用、SDK）如何通过 Codex 的 JSON-RPC 协议创建对话线程并启动模型回合。我需要能够在新客户端接入、调试协议不匹配、或定制 app-server 行为时，从源码层面追踪整个调用链，而非停留在 API 文档层面。

## 成功的样子
- 能画出 thread/start 和 turn/start 从 JSON-RPC 请求到 core 执行再回到通知的完整时序图
- 能在源码中定位每一层的入口函数和关键数据结构
- 能判断一个线上错误（如 "Not initialized"、"thread not found"）应该在哪一层排查
- 能识别至少一条异常路径（如 thread 不存在、turn 被取消）的处理逻辑

## 约束条件
- 教学语言为简体中文，代码标识符保留英文原名
- 每节课 15 分钟内可完成，正文不超过 1500 字
- 源码引用以 codex-rs/ 下的 Rust 源文件为主

## 不在范围内
- app-server 的 transport 层实现细节（HTTP/WebSocket/stdio 帧处理）
- core 内部的 LLM 调用、工具执行、sandbox 策略细节
- SDK 端的具体语言绑定实现
- MCP、Plugin、Skill 等扩展机制的调用链路
