# 使命：CLI 框架 -- Fire 命令注册、子命令系统、配置管理、REPL 交互

## 为什么
理解 hermes_cli/ 目录中 199 个 Python 文件构成的 CLI 命令体系——包括 40+ 子命令的注册机制、argparse 解析树构建、配置文件的读取与热加载、终端交互式控制台引擎。这些是开发者理解"hermes <命令>"如何被路由到具体逻辑的关键知识，也是后续扩展新子命令的基础。

## 成功的样子
- 能准确说出 main.py、_parser.py、completion.py 三个入口级文件的职责边界
- 能画出从 `hermes gateway start` 到 cmd_gateway() 的完整 argparse 分发链路
- 能独立写出一个新的子命令插件（build_xxx_parser + cmd_xxx handler）
- 理解 config.py 中 374KB 配置管理的分层结构：默认值、YAML 覆盖、环境变量融合

## 约束条件
- 不深入 Agent 核心运行逻辑（属于 L1-agent-core 课程）
- 不覆盖 gateway/ 网关层内部消息路由（属于 L1-gateway 课程）
- 不涉及 tools/、skills/、providers/ 等垂直模块的内部实现

## 不在范围内
- cli.py 顶层的 Fire 框架用法（已在 L1-agent-entry 中介绍）
- run_agent.py 的 AIAgent 类定义与对话循环
- TUI 终端界面渲染（ui-tui/）或 Web Dashboard（web/）前端实现
