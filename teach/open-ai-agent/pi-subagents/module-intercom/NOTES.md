# 教学笔记：父子进程 intercom 与 supervisor 协调模块

- 角色：teach-goal L1 主题生成 worker，只写 `teach/open-ai-agent/pi-subagents/module-intercom/`。
- 课程范围：核心源码为 `open-ai-agent/pi-subagents/src/intercom/intercom-bridge.ts`、`open-ai-agent/pi-subagents/src/intercom/native-supervisor-channel.ts`、`open-ai-agent/pi-subagents/src/intercom/result-intercom.ts`。
- 讲解策略：短课讲职责边界；reference 承载消息类型、生命周期、调用方矩阵和测试证据。
- 后续 L2 候选：`slice-supervisor-decision-request`、`slice-async-result-intercom-delivery`、`slice-live-resume-follow-up`、`slice-nested-child-control-intercom`。
