# 使命：模型 profile 与供应商能力探测模块

## 为什么
学习者需要能判断 `pi-subagents` 如何把运行时模型注册表、live probe、成本/质量启发式和 settings 覆盖合成可执行的子 agent 模型配置。掌握后，面对“某个子 agent 为什么用了这个模型、为什么 fallback、为什么被 scope 拦住”这类问题，可以从源码证据定位事实来源，而不是凭经验猜。

## 成功的样子
- 能解释 provider catalog、quota profile、quality profile 三类文件分别提供什么事实。
- 能顺着 `agentOverrides` 说明 profile 如何影响内置 agent 的有效 `model`。
- 能区分 profile 生成、运行时 fallback、`modelScope` 边界检查各自负责的阶段。
- 能用测试文件验证模型分层、live probe、路径安全、scope 约束和 fallback 行为。

## 约束条件
- 本主题是 L1 模块导览，只覆盖 `open-ai-agent/pi-subagents/src/profiles/profiles.ts` 的模块职责和关键调用关系。
- 只少量引用调用方与测试，不展开完整 runs 执行链路、agent discovery 全细节或 provider SDK 实现。
- 输出必须是简体中文，源码路径使用 `open-ai-agent/pi-subagents/...` 前缀。

## 不在范围内
- 不讲 Pi extension 注册、TUI 渲染、async runner 生命周期或 slash 命令解析。
- 不评估现实世界模型供应商价格优劣，只讲本仓库如何从 registry metadata 与探测结果派生 profile。
- 不修改源码、进度台账或其他教学主题目录。
