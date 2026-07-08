# Native supervisor 与 intercom 协调全链路资源

## 知识

- 本地源码：`open-ai-agent/pi-subagents/src/intercom/intercom-bridge.ts`
  讲解 bridge mode 归一、`orchestratorTarget` 解析、`applyIntercomBridgeToAgent` 如何追加 `contact_supervisor` 与系统提示。适用于理解子 agent 启动前协调能力从哪来。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/shared/pi-args.ts`
  讲解子进程环境变量注入：`PI_SUBAGENT_SUPERVISOR_CHANNEL_DIR`、orchestrator session id、run metadata。适用于排查子端报 native supervisor channel 不可用。
- 本地源码：`open-ai-agent/pi-subagents/src/intercom/native-supervisor-channel.ts`
  讲解 request/reply 文件协议、子端 `contact_supervisor`、父端轮询与 `subagent_supervisor` reply。适用于运行中阻塞决策全链路。
- 本地源码：`open-ai-agent/pi-subagents/src/intercom/result-intercom.ts`
  讲解 grouped payload 构建、delivery acknowledgement、compact receipt 与 heavy output 剥离。适用于理解完成后的结果回传。
- 本地源码：`open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts`
  讲解 `resolveIntercomBridge`、`emitForegroundResultIntercom`、`maybeBuildForegroundIntercomReceipt` 与 single/parallel/chain 出口。适用于把 intercom 模块接回前台执行主路径。
- 本地接线：`open-ai-agent/pi-subagents/src/extension/index.ts`
  创建并启动 `createNativeSupervisorChannel`，在 session 生命周期中 poll pending request。适用于理解父端轮询从哪启动。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/intercom-bridge.test.ts`
  验证 mode 默认、fork-only 条件、工具注入幂等与 allowlist 不阻塞 native 工具。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/native-supervisor-channel.test.ts`
  验证 session 过滤、reply path、resolved/expired/inactive 清理、child ask 取消时 request 移除。
- 本地测试：`open-ai-agent/pi-subagents/test/unit/result-intercom.test.ts`
  验证 grouped payload、receipt 格式、details 剥离 heavy output、嵌套结果脱敏。
- 本地测试：`open-ai-agent/pi-subagents/test/integration/intercom-result-delivery.test.ts`
  验证 foreground single/parallel/chain 只发一个 grouped event；bridge inactive 或 delivery 超时回退 legacy output。
- 上游 L1 参考：`teach/open-ai-agent/pi-subagents/module-intercom/reference/intercom-overview.html`
  intercom 模块消息类型、调用方矩阵与边界判断；本切片是其 foreground 协调深化。

## 智慧（社区）

- [nicobailon/pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  上游问题讨论入口。适用于把 supervisor channel 与 result delivery 行为差异对照到真实 bug 或回归报告。

## 空白

- 未找到 pi-subagents 官方独立文档专门描述 native supervisor 文件通道协议；当前课程以源码类型定义、默认 bridge 模板与单元/集成测试为可信来源。
