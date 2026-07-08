# 单次前台 subagent run 资源

## 知识

- [pi-subagents README](https://github.com/nicobailon/pi-subagents) — 项目定位、安装与 subagent tool 基本用法。
- [pi-subagents extension/index.ts](open-ai-agent/pi-subagents/src/extension/index.ts) — Pi extension 入口，注册 `subagent` tool 并创建 executor。
- [subagent-executor.ts](open-ai-agent/pi-subagents/src/runs/foreground/subagent-executor.ts) — 执行门卫：`action` 分流、`effectiveAsync`、spawn 限额、`runSinglePath`。
- [execution.ts runSync](open-ai-agent/pi-subagents/src/runs/foreground/execution.ts) — 单 child 前台执行：spawn、JSONL 解析、progress、model fallback。
- [pi-spawn.ts](open-ai-agent/pi-subagents/src/runs/shared/pi-spawn.ts) — 解析 `pi` 可执行路径（含 Windows 与 `PI_SUBAGENT_PI_BINARY`）。
- [single-execution.test.ts](open-ai-agent/pi-subagents/test/integration/single-execution.test.ts) — mock Pi CLI 下的 spawn→parse→result 集成佐证。

## 智慧（社区）

- [pi-subagents GitHub Issues](https://github.com/nicobailon/pi-subagents/issues) — 上报前台 run 超时、spawn 失败、model fallback 等真实环境问题。
- [Pi coding agent 生态](https://github.com/nicobailon) — 理解父/子 Pi 进程关系与 extension 加载方式。

## 空白

- 官方文档尚未单独拆出「single foreground run」章节；本主题以源码与集成测试为首要依据。
- child Pi 的 JSONL 事件协议细节分散在 `execution.ts` 与 pi-agent-core，需结合上游包阅读。
