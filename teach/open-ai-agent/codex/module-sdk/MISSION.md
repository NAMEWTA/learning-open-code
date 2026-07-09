# 使命：Python 与 TypeScript SDK

## 为什么
用户需要快速判断 Codex SDK 在项目整体架构中的位置，并能从公开 API 反推到底层运行时、线程、turn 和事件流如何协作。掌握这个主题后，用户可以阅读 SDK 源码、设计 SDK 调用链，或对比 Python / TypeScript 两套封装的边界差异。

## 成功的样子
- 能说明 Python SDK 与 TypeScript SDK 分别通过什么运行时通道驱动 Codex。
- 能列出两套 SDK 的主要公开 API，并知道完整清单在哪里查。
- 能写出最小的创建 thread、发起 run turn、消费流式事件的调用序列。
- 能按推荐顺序继续阅读源码，而不是从生成模型或测试夹缝中迷路。

## 约束条件
- 本主题是 L1 模块导览，短课控制在 15 分钟内完成。
- 只写入 `teach/open-ai-agent/codex/module-sdk/`，不修改源项目和其他主题目录。
- 课程必须链接 L0 总览，并把长清单分流到 reference。

## 不在范围内
- 不讲 Rust core 的执行细节。
- 不逐字段展开生成协议模型。
- 不覆盖 SDK 发布流水线和 npm / PyPI 版本发布策略。
