# 父子进程 intercom 与 supervisor 协调模块资源

## 知识

- 本地源码：`open-ai-agent/pi-subagents/src/intercom/intercom-bridge.ts`
  讲解 intercom bridge 的配置解析、目标命名、默认提示模板和 agent 工具注入。适用于判断“子 agent 为什么拥有或没有 `contact_supervisor` / `intercom` 工具”。
- 本地源码：`open-ai-agent/pi-subagents/src/intercom/native-supervisor-channel.ts`
  讲解子端 `contact_supervisor` 写请求、父端轮询请求、按 session 过滤、回复写回和生命周期清理。适用于排查阻塞问答、进度更新和 native fallback。
- 本地源码：`open-ai-agent/pi-subagents/src/intercom/result-intercom.ts`
  讲解完成结果如何压缩成 grouped payload、如何等待 delivery acknowledgement，以及 compact receipt 如何避免把完整输出塞回普通结果。适用于排查结果回传和恢复提示。
- 本地调用方：`open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts`
  foreground 路径解析 bridge、注入 agent 配置，并在 grouped delivery 成功时返回 compact receipt。适用于理解 intercom 模块被执行器消费的位置。
- 本地调用方：`open-ai-agent/pi-subagents/src/runs/background/result-watcher.ts`
  async 结果文件落盘后，读取 `intercomTarget` 并发送 grouped result。适用于理解异步完成结果为什么不一定走 foreground receipt。
- 本地调用方：`open-ai-agent/pi-subagents/src/runs/shared/pi-args.ts`
  子进程启动参数中注入 supervisor channel 环境变量和临时目录。适用于理解子端 metadata 从哪里来。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/intercom-bridge.test.ts`
  验证 bridge 模式、目标命名、默认提示和幂等工具注入。适用于确认配置边界。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/native-supervisor-channel.test.ts`
  验证父端 session 过滤、stale channel 清理、已有 intercom 工具共存、过期/已解决请求清理和取消行为。适用于确认 supervisor channel 生命周期。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/result-intercom.test.ts`
  验证 grouped payload、async revive 指引、嵌套结果脱敏、receipt 压缩和状态归类。适用于确认结果回传格式。
- 本地集成测试：`open-ai-agent/pi-subagents/test/integration/intercom-result-delivery.test.ts`
  验证 foreground 单子 agent、parallel、chain 的 grouped event 发送，以及 bridge 关闭或 delivery 未确认时的 legacy fallback。适用于确认端到端行为。

## 智慧（社区）

- [nicobailon/pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  上游问题讨论入口。适用于把本主题中的边界判断应用到真实 bug 报告、设计争议或回归复现中。
- 本仓库 teach-goal 评审会话
  适用于把本主题产出的 L2 候选交给后续 worker 继续验证，尤其是阻塞问答、async result、resume follow-up 和嵌套控制切片。

## 空白

- 未找到针对 pi-subagents intercom 子系统的独立外部设计文档；当前课程以源码、测试和上游 issue 入口作为可信来源。
