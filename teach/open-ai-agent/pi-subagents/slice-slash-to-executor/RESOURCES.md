# Slash 到 executor 桥接 资源

## 知识

- [pi-subagents README](https://github.com/nicobailon/pi-subagents) — 扩展安装与 slash 命令概览
- [module-slash-workflows 参考](../module-slash-workflows/reference/slash-workflows-overview.html) — 命令清单、bridge 边界与 prompt workflow 接缝
- [slice-single-foreground-run](../slice-single-foreground-run/lessons/0001-flow-map.html) — executor 内 `runSinglePath` 之后的 spawn 八跳
- 源码入口：`open-ai-agent/pi-subagents/src/extension/index.ts`（bridge 注册与 `registerSlashCommands` 调用顺序）

## 智慧（社区）

- [pi 编码 agent 生态](https://github.com/earendil-works/pi-coding-agent) — slash 命令与 extension 事件总线的宿主环境；调试 bridge 时需确认 extension 已加载

## 空白

- 暂无独立的 slash-bridge 设计 RFC；行为以源码事件名与 integration test 为准
