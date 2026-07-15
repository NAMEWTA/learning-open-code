# CLI 入口与模式选择 资源

## 知识

- [cli.ts - CLI 入口源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/cli.ts) — 11 行入口：shebang、全局配置、调用 main()
- [main.ts - 主流程编排源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/main.ts) — 855 行核心管线：9 阶段启动流程与三模式分发
- [args.ts - 参数解析源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/cli/args.ts) — 50+ 参数定义、解析循环、printHelp()
- [startup-ui.ts - 首次启动配置源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/cli/startup-ui.ts) — 首次设置检测、TUI 弹窗、主题选择
- [session-picker.ts - 会话选择器源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/cli/session-picker.ts) — --resume 的 TUI 会话列表
- [rpc-entry.ts - RPC 模式入口源码](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/rpc-entry.ts) — orchestrator 子进程的备选入口
- [modes/index.ts - 模式导出](https://github.com/anthropics/pi/blob/main/packages/coding-agent/src/modes/index.ts) — InteractiveMode / runPrintMode / runRpcMode 的公共接口
- [Node.js process.argv 文档](https://nodejs.org/api/process.html#processargv) — 理解 args.slice(2) 的含义
- [Node.js shebang 文档](https://nodejs.org/api/cli.html#-e---eval-script) — 理解 `#!/usr/bin/env node` 的工作原理

## 智慧（社区）

- [Pi GitHub Discussions](https://github.com/anthropics/pi/discussions) — 讨论 Pi 使用技巧和 CLI 参数配置
- [Pi Discord](https://discord.gg/anthropic) — 实时交流 Pi 开发与使用问题

## 空白

- 当前未找到专门讲解 Pi CLI 启动链路的社区博客或视频教程。本课程覆盖的内容主要来自源码直接阅读。
- `node:readline` 在 `promptConfirm()` 中的使用细节（TUI 之外的回退路径）在官方文档中无专门说明。
