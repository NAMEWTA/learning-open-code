# 使命：Skills / Assistants / MCP 映射设计

## 为什么
学习者需要能维护 AionU 中 Assistant 默认能力、Skill 导入绑定、MCP 工具配置之间的边界。掌握后，他们可以判断一个能力到底应该改 Assistant 定义、Skills Hub、Tools/MCP 设置页，还是会话创建时的快照逻辑。

## 成功的样子
- 能解释 Assistant、Skill、MCP 三者分别持久化什么、不持久化什么。
- 能从 Assistant 设置页的状态追到 `/api/assistants`、`/api/skills`、`/api/mcp` 和 `/api/conversations`。
- 能基于 E2E 与源码事实判断当前测试覆盖的强弱，并提出可执行补测方向。

## 约束条件
- 本主题是 L4 深度剖析，优先读源码事实、设计取舍、可靠性与局限。
- 每节短课控制在 10-15 分钟内，长表格和证据矩阵分流到 reference。
- 只写入当前主题目录，不修改源项目、不提交 git、不更新主 Agent 管理的索引和进度文件。

## 不在范围内
- 不展开 AionU 后端 Rust 实现细节。
- 不讲完整扩展系统、ACP adapter 生命周期或 Team Mode。
- 不把 Skills Hub 的所有 UI 交互拆成独立教程，只覆盖与 Assistant 绑定相关的导入和默认能力链路。
