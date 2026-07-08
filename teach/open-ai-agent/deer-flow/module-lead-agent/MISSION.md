# 使命：Agent lead runtime

## 为什么
学习者需要在 deer-flow 中定位、调试和扩展真正的 agent runtime，而不是把 Gateway、LangGraph 配置、工具系统和中间件链混成一团。完成本主题后，学习者应能从一次 run 追到 lead agent 的装配点，并判断新增模型、工具、skill 或中间件应该接在哪个边界。

## 成功的样子
- 能从 `backend/langgraph.json` 和 Gateway run 路径追到 `make_lead_agent`。
- 能说明 lead agent 装配模型、工具、prompt、middleware 与 `ThreadState` 的顺序。
- 能快速查找中间件清单、源码索引和可扩展入口。

## 约束条件
- 本主题是 L1 模块总览，lesson 控制在 15 分钟内完成。
- 课程只覆盖 lead agent 如何被装配成可运行 agent，长表格放入 reference。
- 文档使用简体中文，代码标识符和源码路径保留英文。

## 不在范围内
- 不深入 Gateway HTTP/SSE 生命周期细节。
- 不逐行讲解 subagent executor、tool 实现、memory 存储和数据库持久化。
- 不覆盖前端 workspace 交互细节。
