# 使命：Renderer Shell 模块

## 为什么
用户要系统学习 Orca 桌面应用，需要先看懂 renderer 侧如何从 React 入口变成可恢复、可持久化、可同步 runtime graph 的应用外壳。这个主题把 UI shell、全局 store、session 水合和 runtime 同步的边界讲清楚，为后续 worktree 创建链路和移动端同步链路做铺垫。

## 成功的样子
- 能从 renderer 启动入口追到 `App` 的 shell 装配，并解释错误边界、i18n、主题和 crash diagnostics 的作用。
- 能说明 `useAppStore` 如何组合多个 Zustand slice，以及为什么 App 只编排启动、水合、持久化和 runtime 同步。
- 能识别统一 tab/group/layout 模型、workspace session 写回和 runtime graph publish 各自在哪些文件维护。

## 约束条件
- 短课控制在 15 分钟内，只讲代表性文件，不展开所有 React 组件和视觉细节。
- 教学内容以仓库真实源码和测试为准，不臆测未实现的 UI 行为。
- L1 主题必须通过快照、审计和独立审查后才能标记完成。

## 不在范围内
- 不逐个讲解所有页面组件、modal、sidebar 面板和具体样式。
- 不深入 PTY provider、main IPC handler、移动端 runtime RPC server 的内部实现；这些属于其他主题。
