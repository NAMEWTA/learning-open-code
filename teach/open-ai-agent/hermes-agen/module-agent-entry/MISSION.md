# 使命：Agent 入口层 -- CLI 启动、主运行循环、状态管理、日志与配置系统

## 为什么
理解 Hermes Agent 从用户输入到核心引擎的完整启动链路，掌握入口文件的职责划分与数据流向，为后续阅读 Agent 核心引擎和 CLI 框架层建立第一手代码锚点。

## 成功的样子
- 能准确说出 cli.py、run_agent.py、hermes_state.py 三个文件的职责边界和调用关系
- 能画出从 `python cli.py --query "hello"` 到 Agent 核心对话循环的完整调用链
- 能独立找到 HERMES_HOME、config.yaml 等关键配置项的代码位置

## 约束条件
- 不深入 Agent 核心引擎内部逻辑（属于 L1-agent-core 课程）
- 不覆盖 hermes_cli/ 框架层子命令实现（属于 L1-cli-framework 课程）
- 不涉及 gateway/ 消息网关层（属于 L1-gateway 课程）

## 不在范围内
- 终端 TUI 组件（ui-tui/）、Web Dashboard（web/）、桌面应用（apps/desktop/）的用户界面实现
- 批量训练数据生成流程（batch_runner.py 的详细参数配置）
- MCP 协议服务端内部实现细节（mcp_serve.py 的工具注册机制）
