# 使命：Frontend workspace

## 为什么
用户希望在具备 React/Next.js 基础的前提下，快速看懂 DeerFlow 的用户可见工作台：聊天、Agents、scheduled tasks、artifact、sidecar 等入口如何被页面组织起来，以及这些体验如何通过前端 core 层接到 Gateway 和 LangGraph API。掌握后，用户应能在修改工作台体验时先定位正确层级，而不是从庞大的组件树里盲搜。

## 成功的样子
- 能画出 `workspace` 路由壳、功能页面、workspace 组件族、core API 层之间的关系。
- 能从一个聊天提交动作追到 `useThreadStream`、LangGraph SDK、Gateway 代理接口。
- 能区分普通 REST 调用、LangGraph SDK 调用、React Query 缓存、纯 UI 状态各自负责什么。
- 能说出 Agents、scheduled tasks、workspace changes、artifact、sidecar 在前端模块中的入口文件。

## 约束条件
- 本主题是 L1 模块导览，只覆盖 15 分钟内能建立方向感的结构知识。
- 读者有 React/Next.js 基础，但不默认熟悉 DeerFlow 业务命名。
- 教学内容基于源码快照，不深入后端 Gateway 实现和 LangGraph 内部协议。
- 长组件/API 清单放入 reference，lesson 只保留一条主线。

## 不在范围内
- 后端 Gateway 路由、认证中间件、LangGraph graph 执行器的内部实现。
- UI 视觉系统、Tailwind 细节、组件库样式规范的逐项讲解。
- 每个 workspace 子功能的完整源码深挖；后续可拆成聊天流、scheduled tasks、sidecar、artifacts 等 L2 课程。
