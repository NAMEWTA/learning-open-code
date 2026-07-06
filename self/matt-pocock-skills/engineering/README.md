# 工程

日常编码工作中使用的技能。

## 用户调用

只能通过手动输入调用（`disable-model-invocation: true`）。

- **[ask-matt](./ask-matt/SKILL.md)** — 询问哪个技能或流程适合你的情况。作为本仓库中用户调用技能的路由器。
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — 在质询会话中同步构建项目的领域模型，精炼术语并实时更新 `CONTEXT.md` 和 ADR。
- **[triage](./triage/SKILL.md)** — 将 issue 按分类角色状态机进行流转。
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)** — 扫描代码库寻找深化机会，以可视化 HTML 报告呈现，然后对你选中的方向进行深入质询。
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)** — 为本仓库配置工程技能（issue 追踪器、分类标签、领域文档布局）。每个仓库只需运行一次。
- **[to-issues](./to-issues/SKILL.md)** — 使用垂直切片将任何计划、spec 或 PRD 拆分为可独立领取的 issue。
- **[to-prd](./to-prd/SKILL.md)** — 将当前对话转化为 PRD 并发布到 issue 追踪器。
- **[prototype](./prototype/SKILL.md)** — 构建一次性原型——用于状态/逻辑问题的可运行终端应用，或多种可切换的 UI 变体。

## 模型调用

模型或用户均可触达（通过丰富的触发短语让模型能主动调用）。

- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)** — 针对疑难 bug 和性能回归的规范化诊断循环：复现 → 最小化 → 假设 → 插桩 → 修复 → 回归测试。
- **[tdd](./tdd/SKILL.md)** — 红-绿-重构循环的测试驱动开发。一次一个垂直切片地构建功能或修复 bug。
- **[domain-modeling](./domain-modeling/SKILL.md)** — 主动构建和精炼项目领域模型——挑战术语、用场景进行压力测试、实时更新 `CONTEXT.md` 和 ADR。
- **[codebase-design](./codebase-design/SKILL.md)** — 设计深层模块的共享规范和词汇：小接口、清晰接缝、通过接口可测试。
