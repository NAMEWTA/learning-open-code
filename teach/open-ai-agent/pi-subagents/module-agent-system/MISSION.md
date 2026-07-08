# 使命：Agent 发现、配置与内置角色模块

## 为什么
学习者希望在阅读 `pi-subagents` 时能判断一次 subagent 调用最终会使用哪个角色配置。掌握这一点后，后续分析 executor、chain、async run 时就不会把执行层问题误判为 agent discovery 或 settings override 问题。

## 成功的样子
- 能用一句话说明 agents 模块在整体架构中的职责。
- 能根据 scope、source、frontmatter 和 settings 判断最终生效的 `AgentConfig`。
- 能查到 `list/get/create/update/delete/eject/disable/enable/reset` 等管理动作的边界。
- 能用相关单元测试验证一个优先级或覆盖规则是否真实存在。

## 约束条件
- 本主题输出中文教学文档，短课控制在 15 分钟内完成。
- 短课只讲一个学习目标；长接口清单、字段表和内置角色列表放入 reference。
- 本轮只写入 `teach/open-ai-agent/pi-subagents/module-agent-system/`。

## 不在范围内
- 不讲 executor 如何 spawn 子进程或执行 chain。
- 不讲 async status、wait、intercom 的完整生命周期。
- 不修改项目源码、进度文件、项目索引或其他主题目录。
