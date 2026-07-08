# 模型 profile 与供应商能力探测模块资源

## 知识

- `open-ai-agent/pi-subagents/src/profiles/profiles.ts`
  本主题的一手来源。覆盖 profile JSON 结构、provider catalog 刷新、live probe、模型分类、支配模型过滤、quota/quality profile 生成、profile 应用和 profile 检查。
- `open-ai-agent/pi-subagents/src/agents/agents.ts`
  settings 消费侧来源。用于理解 `subagents.agentOverrides`、`subagents.defaultModel`、`subagents.modelScope` 如何进入 `AgentConfig`。
- `open-ai-agent/pi-subagents/src/runs/shared/model-fallback.ts`
  运行时模型候选与 fallback 来源。用于区分 profile 写入的 primary model 与 agent `fallbackModels`、retryable failure 之间的关系。
- `open-ai-agent/pi-subagents/src/runs/shared/model-scope.ts`
  模型能力边界来源。用于理解 allow pattern、thinking suffix 剥离、explicit/inherited 两种违规严重度。
- `open-ai-agent/pi-subagents/src/agents/agent-management.ts`
  管理面证据。用于理解 `models` 管理动作如何展示有效模型来源，以及 create/update 如何提示 model 和 fallbackModels 是否在 registry 中。
- `open-ai-agent/pi-subagents/src/extension/schemas.ts`
  对外参数 schema 证据。用于确认 subagent 调用暴露的是任务级 `model` override，而 profile 落点是 settings 与 agent discovery。
- `open-ai-agent/pi-subagents/test/unit/profiles.test.ts`
  profile 模块行为测试。覆盖目录创建、路径安全、catalog 缓存、probe、启发式 fallback、quota/quality 选择、profile check、thinking suffix。
- `open-ai-agent/pi-subagents/test/unit/agent-overrides.test.ts`
  settings 覆盖测试。用于确认 profile 写入的 `agentOverrides` 如何影响 builtin/custom agent，及 project/user 优先级。
- `open-ai-agent/pi-subagents/test/unit/model-fallback.test.ts`
  fallback 与模型解析测试。用于验证 provider/id 规范化、模糊匹配、candidate 去重、retryable failure、scope 配合。
- `open-ai-agent/pi-subagents/test/unit/model-scope.test.ts` 与 `open-ai-agent/pi-subagents/test/unit/model-scope-settings.test.ts`
  scope 规则测试。用于验证 allow pattern、explicit error、inherited warn、settings discovery 优先级。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  上游问题讨论入口，适用于核对模型选择、provider registry 差异、profile 生成失败或 scope 策略的真实使用反馈。
- [pi-subagents GitHub 仓库](https://github.com/nicobailon/pi-subagents)
  上游源码和 README 入口，适用于对照当前子模块版本与主线实现是否已经变更。

## 空白

- 缺少真实 provider catalog 样本与历史价格快照；本主题只依据源码、测试构造数据和运行时 registry 字段解释算法。
- 缺少生产环境 probe 失败统计；`auth`、`unavailable`、`timeout`、`error` 的影响只按源码规则与单元测试说明。
