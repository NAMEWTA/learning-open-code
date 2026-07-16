# pi-tui 嵌入使用 资源

## 知识

- [pi-tui 源码：`open-ai-agent/pi/packages/tui/src/`](../../../open-ai-agent/pi/packages/tui/src/)
  核心源码目录，包含 TUI 主类、Terminal 接口、13+ 组件、工具函数。适用于：理解 Component 接口契约、render() 缓存策略、差分渲染算法。

- [pi-tui README：`open-ai-agent/pi/packages/tui/README.md`](../../../open-ai-agent/pi/packages/tui/README.md)
  官方入门文档，包含 Quick Start 示例和 Core API 说明。适用于：快速了解 API 表面和基本用法。

- [pi-tui 测试用例：`open-ai-agent/pi/packages/tui/test/`](../../../open-ai-agent/pi/packages/tui/test/)
  41 个测试文件，覆盖组件渲染、输入处理、ANSI 序列生成等场景。适用于：验证组件行为、理解边界条件。

- [Node.js TTY 文档](https://nodejs.org/api/tty.html)
  Node.js 官方 TTY 模块文档，涵盖 raw mode、resize 事件等。适用于：理解 ProcessTerminal 对 stdin/stdout 的封装原理。

- [Kitty Keyboard Protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/)
  Kitty 终端键盘协议的官方规范。适用于：理解 keybindings.ts 和 keys.ts 中的按键解析逻辑。

- [ECMA-48 / ANSI X3.64 控制序列](https://www.ecma-international.org/publications-and-standards/standards/ecma-48/)
  ANSI 转义序列的国际标准。适用于：理解差分渲染中光标移动、清屏、清行的底层序列。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  Pi 项目的官方 Issue 追踪。适用于：了解已知问题、设计决策讨论、社区使用经验。

## 空白

- 目前未发现 pi-tui 作为独立库被第三方项目使用的公开案例
- 缺少 pi-tui 的独立 API 参考文档（README 仅覆盖基本用法）
