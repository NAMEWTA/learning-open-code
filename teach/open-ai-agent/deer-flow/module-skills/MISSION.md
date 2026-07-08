# 使命：Skills 系统

## 为什么
学习者希望在不通读整个 deer-flow 后端的情况下，快速掌握 Skills 如何作为 progressive loading 扩展机制接入 lead agent。掌握这条链路后，他们可以判断一个 skill 为什么会出现在 prompt、为什么 slash 激活失败、以及为什么某些工具会被隐藏。

## 成功的样子
- 能沿着一次 run 说明 skill 从存储发现、启用状态、agent 白名单到 prompt 渲染的主路径。
- 能解释 `/skill-name` 激活如何把 `SKILL.md` 注入隐藏上下文，并说清它和模型自主 `read_file` 的差异。
- 能根据 `allowed-tools`、custom agent `skills` 白名单和测试锚点判断工具暴露边界。
- 能定位后续深挖所需的 API、storage、install、policy、middleware 和内置 public skill 文件。

## 约束条件
- 本 goal 只产出 L1 模块材料，lesson 必须是 15 分钟短课。
- 所有持久化输出只写入 `teach/open-ai-agent/deer-flow/module-skills/`。
- Tools/MCP 模块会并行讲工具加载边界，本主题只讲 skills 对 prompt 与工具集合的影响。

## 不在范围内
- 不逐行讲每个内置 public skill 的业务流程。
- 不深讲 MCP tool discovery、deferred tool promotion 或 sandbox provider 实现。
- 不生成 skill authoring 完整教程；只给出理解 DeerFlow skills runtime 的地图。
