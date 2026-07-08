# 使命：扩展入口与 Pi runtime 注册模块

## 为什么
学习者希望能在不迷失于执行层细节的前提下，判断 `pi-subagents` 如何把 subagent 能力挂进 Pi runtime。掌握这一层后，后续阅读 executor、async、slash、intercom 时能先分清“注册入口”和“实际执行”的边界。

## 成功的样子
- 能用一句话说明 `src/extension` 模块职责。
- 能列出 `index.ts` 注册到 Pi 的主要工具、渲染器、事件桥和 session 生命周期钩子。
- 能解释 `schemas.ts`、`rpc.ts`、`config.ts`、`doctor.ts`、`tool-description.ts`、`control-notices.ts`、`fanout-child.ts` 在入口层的分工。
- 能根据测试文件找到至少一个行为佐证，而不是只凭源码阅读下结论。

## 约束条件
- 本轮只生成 L1 短课与参考资料，lesson 控制在 15 分钟内完成。
- 不重复 L0 的全局项目地图；只聚焦 `src/extension` 的模块边界。
- 只写入 `teach/open-ai-agent/pi-subagents/module-extension-runtime/`。

## 不在范围内
- 不深入讲解 foreground executor 的 single、parallel、chain 执行细节。
- 不展开 async runner、run status、wait 的完整生命周期。
- 不分析 slash 命令解析、agent discovery 覆盖规则或 intercom 协议的内部实现。
