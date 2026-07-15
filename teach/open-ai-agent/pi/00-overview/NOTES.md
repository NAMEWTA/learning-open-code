# 教学笔记：Pi Agent Harness 项目总览

## 批量生成模式
- 本课程为 teach-goal 编排器批量生成，MISSION.md 使用自动生成的默认使命。
- 用户可在后续会话中修改使命以反映真实学习目标。

## 教学注意事项
- Pi 是 monorepo 项目，5 个核心包按依赖层次组织，教学时应自底向上（tui → ai → agent → coding-agent）讲解。
- 项目使用 npm workspaces 管理，包间依赖通过 workspace 协议（`^0.80.3`）声明。
- TypeScript 配置分两层：`tsconfig.base.json`（公共编译选项）+ `tsconfig.json`（路径别名）。
- 项目对依赖安全极度重视，有精确版本锁定、lockfile 审查、shrinkwrap 等多重机制，应在后续课程中展开。
