# 使命：测试体系与行为佐证模块

## 为什么
学习者在读完 L0 架构和各 L1 模块边界后，需要一套可复现的「行为地图」：当源码注释与实现不一致时，能立刻判断该去 unit、integration 还是 e2e 找断言，并用 `npm run test:*` 验证自己的理解，而不是凭印象猜运行时行为。

## 成功的样子
- 能用一句话说明 `test/` 目录在 `pi-subagents` 中的职责：佐证而非定义产品行为。
- 能区分 unit（纯函数）、integration（mock Pi CLI 管道）、e2e（真实 AgentSession + faux provider）三层的边界与运行命令。
- 能根据功能模块（runs、agents、slash、intercom 等）快速定位对应的 `*.test.ts` 文件。
- 能解释 `test/support/` 中 mock-pi、loader 与 real-session-runner 各自解决什么问题。

## 约束条件
- 本次只建立 L1 模块边界与测试索引，不逐用例讲解每个断言。
- lesson 控制在 15 分钟内；完整测试文件清单与模块映射表放入 reference。
- 只写入 `teach/open-ai-agent/pi-subagents/module-test-suite/`，不修改其他主题目录。

## 不在范围内
- 不展开如何为新功能编写测试用例或设计 mock 响应队列。
- 不讲解 CI 流水线、覆盖率阈值或发布前检查脚本。
- 不在本课覆盖 `test/support/` 每个 helper 函数的实现细节。
