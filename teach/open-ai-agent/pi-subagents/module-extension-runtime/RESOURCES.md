# 扩展入口与 Pi runtime 注册模块资源

## 知识

- `open-ai-agent/pi-subagents/src/extension/index.ts`
  Pi extension 主入口。适用于确认 tool、renderer、slash/RPC、async tracker、supervisor channel 和 session 生命周期注册点。
- `open-ai-agent/pi-subagents/src/extension/schemas.ts`
  TypeBox 参数契约。适用于理解 `subagent`、`wait` 工具对外参数，以及为什么要裁剪嵌套 description。
- `open-ai-agent/pi-subagents/src/extension/rpc.ts`
  in-process RPC bridge。适用于理解事件总线协议、`ping/status/spawn/interrupt/stop` 方法和 async-only spawn 约束。
- `open-ai-agent/pi-subagents/src/extension/config.ts`
  extension 配置读写入口。适用于确认 `~/.pi/agent/extensions/subagent/config.json` 的加载失败降级语义。
- `open-ai-agent/pi-subagents/src/extension/doctor.ts`
  doctor 报告生成器。适用于理解诊断报告如何汇总 runtime、filesystem、discovery、permission system 和 intercom 状态。
- `open-ai-agent/pi-subagents/src/extension/tool-description.ts`
  subagent tool 描述生成器。适用于理解 full、compact、custom 描述模式和强制安全提示。
- `open-ai-agent/pi-subagents/src/extension/control-notices.ts`
  控制通知处理。适用于理解 `needs_attention` 等控制事件如何去重、延迟并投递到父会话。
- `open-ai-agent/pi-subagents/src/extension/fanout-child.ts`
  fanout child 专用入口。适用于理解普通 child 不注册主入口、fanout child 只暴露 child-safe `subagent` 的边界。
- `open-ai-agent/pi-subagents/test/unit/index-child-registration.test.ts`
  行为佐证：父入口注册工具、普通 child 早退、fanout child 避免双注册、child-safe 模式阻止变更类管理动作。
- `open-ai-agent/pi-subagents/test/unit/rpc.test.ts`
  行为佐证：RPC ready/ping、status/interrupt 委托、spawn 强制 async、stop 复用 async timeout 控制路径。
- `open-ai-agent/pi-subagents/test/unit/schemas.test.ts`
  行为佐证：schema 保留顶层参数描述并移除嵌套 description，避免 provider payload 过大或形状被拒。
- `open-ai-agent/pi-subagents/test/unit/doctor.test.ts`
  行为佐证：doctor 报告在成功和失败环境下都能输出有边界的诊断摘要。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues)
  适用于把源码阅读中发现的 runtime 注册、RPC、async 或 child-safe 行为疑问拿到项目维护上下文中验证。

## 空白

- 当前仓库中没有 Pi extension API 的完整官方参考文档副本；本主题先以 `@earendil-works/pi-coding-agent` 类型导入、源码用法和单元测试作为依据。
- 本主题不访问外部社区讨论记录；如后续需要解释历史设计动机，应补充 issue、release note 或 maintainer discussion。
