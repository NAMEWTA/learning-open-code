# 工具定义与执行抽象资源

## 知识

- 源码：`open-ai-agent/codex/codex-rs/tools/src/lib.rs`
  `codex-tools` 的对外 re-export 清单。适用于判断哪些类型属于共享工具协议层。
- 源码：`open-ai-agent/codex/codex-rs/tools/src/tool_executor.rs`
  `ToolExecutor`、`ToolExposure` 的定义。适用于理解“规格与执行绑定”的核心接口。
- 源码：`open-ai-agent/codex/codex-rs/tools/src/tool_spec.rs`
  Responses API 工具规格枚举与 JSON 生成入口。适用于理解模型看到的工具形态。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/spec_plan.rs`
  工具来源规划、模型可见工具清单、registry 构建入口。适用于找新增工具应该挂在哪一层。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/router.rs`
  模型响应项到 `ToolCall`/`ToolInvocation` 的转换和分发入口。适用于调试工具调用未进入 handler 的问题。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/registry.rs`
  handler 查找、hook、telemetry、生命周期事件和输出转换。适用于理解执行抽象的包裹层。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/handlers/shell.rs`
  shell 类工具共享执行入口 `run_exec_like`。适用于追踪权限、审批、apply_patch 拦截和 runtime 调用。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/handlers/apply_patch.rs`
  freeform `apply_patch` handler、流式 diff consumer、权限计算。适用于追踪补丁工具执行。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/runtimes/shell.rs`
  shell runtime 的审批、网络审批、沙箱命令构造和进程执行。适用于定位真实命令执行点。
- 源码：`open-ai-agent/codex/codex-rs/core/src/tools/runtimes/apply_patch.rs`
  已验证 patch 在环境文件系统中的执行 runtime。适用于理解文件写入如何受沙箱约束。
- 源码：`open-ai-agent/codex/codex-rs/core/src/exec.rs`
  子进程执行、超时、取消、输出聚合和输出上限。适用于理解 shell 输出为何被截断或超时。
- 源码：`open-ai-agent/codex/codex-rs/exec-server/README.md`
  exec-server 的进程/文件系统 RPC 和远端环境生命周期。适用于理解远端执行环境。

## 智慧（社区）

- 本仓库后续 L2/L3 源码教学主题
  适用于把本 L1 导览拆成更细的 handler、runtime、审批、沙箱专题。
- Codex 项目 issue/PR 讨论区
  适用于验证工具抽象变更背后的设计取舍；本次未联网检索，后续可按具体问题补充链接。

## 空白

- 尚未收录官方架构文档中专门解释 Codex tool runtime 的章节；当前主题以源码和 crate README 为一手材料。
