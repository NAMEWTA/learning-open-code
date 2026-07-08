# 使命：共享类型、状态与文件基础设施模块

## 为什么
用户已经从 L0 知道 `artifacts/status outputs` 是 async 可观测性的基础。本主题要把注意力收窄到 `src/shared`：理解它如何把类型契约、路径约定、原子写入、JSONL 事件、chain 行为、status 文案和 session 工具提供给 agent、extension、runs、slash 与 TUI。

## 成功的样子
- 能用一句话说清 `src/shared` 在整体架构中的职责。
- 能区分共享类型层、文件状态层、路径/session 工具层各自解决的问题。
- 能从 `AsyncStatus`、`ArtifactPaths`、`writeAtomicJson`、`createJsonlWriter` 判断后台运行状态如何落盘和被读取。
- 能用单元测试定位共享基础设施的行为证据，而不是只凭字段名推断。

## 约束条件
- 本主题是 L1 模块导览，只讲共享基础设施，不展开完整 executor 垂直链路。
- 课程面向具备 TypeScript/Node 基础的开发者，正文控制为 15 分钟内完成的短课。
- 本轮只写入 `teach/open-ai-agent/pi-subagents/module-shared-infra/`，不更新项目进度文件或其他主题目录。

## 不在范围内
- 不逐行讲解 `subagent-executor.ts`、`async-execution.ts` 或 `run-status.ts` 的执行流程。
- 不覆盖 agent discovery、extension schema、slash 命令解析和 intercom 协议细节。
- 不做字段级百科；长类型表、常量清单和依赖矩阵放入 reference。
