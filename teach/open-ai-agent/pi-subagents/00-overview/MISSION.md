# 使命：pi-subagents 项目整体架构与学习地图

## 为什么
学习者希望系统理解 `pi-subagents` 如何把一个 Pi 父会话扩展成可委派、可观测、可恢复的 subagent 运行时。掌握这张地图后，后续阅读入口、执行器、后台状态、slash/RPC/intercom 等模块时，可以知道每个文件处在什么职责边界内。

## 成功的样子
- 能用一句话说明 `pi-subagents` 的项目定位和主要使用场景。
- 能画出 parent Pi session、`subagent` tool、agent discovery、foreground executor、async tracker、slash/RPC/intercom、artifacts/status 输出之间的关系。
- 能根据顶层目录判断后续源码阅读应该从哪个 L1/L2 主题切入。
- 能说明哪些文件本轮只作为背景或发布资产豁免，不纳入核心架构教学。

## 约束条件
- 本主题是 L0 导览，只建立全局地图，不展开每条执行链路的异常分支。
- 每节 lesson 保持 15 分钟内完成；接口清单、候选方向和豁免清单分流到 reference。
- 教学产物只写入 `teach/open-ai-agent/pi-subagents/00-overview/`。

## 不在范围内
- 不深入重写 agent discovery、chain execution、async runner、intercom bridge 的完整实现。
- 不创建后续 L1/L2 主题目录。
- 不运行或修改 `open-ai-agent/pi-subagents` 源码。
