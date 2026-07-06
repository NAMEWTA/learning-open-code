# Mission: React 企业级前端开发 — 以 ruoyi-react 为实例从零到精通

## Why
用户是 React 零基础，但在后端 Java（RuoYi-Vue-Plus）有经验。他需要能读懂、修改并扩展 ruoyi-react 前端项目，最终具备独立搭建企业级 React 前端项目的能力。ruoyi-react 是一个真实的生产级项目（UmiJS Max + Zustand + Ant Design v6 + Axios），覆盖了动态路由、状态管理、API 加密、多标签页、实时推送等企业级核心场景，是理想的学习范本。

## Success looks like
- 能打开 ruoyi-react 任意页面文件（如 `pages/system/user/index.tsx`），讲清楚每一行代码的作用和完整数据流向（组件→hook→store→API→后端）
- 能仿照现有页面（如用户管理），在 30 分钟内独立新增一个完整的 CRUD 页面，包括：路由配置、API 定义、Zustand store（如需要）、页面组件（表格+搜索+弹窗表单）
- 能修改动态路由逻辑：理解 `DynamicPage` 的匹配机制、`migratedPages` 映射表、后端返回的路由树结构，能添加新的页面映射
- 能调试前端问题：追踪 token 存储→请求拦截器附加→401 处理→重新登录的完整链路；追踪 Zustand store 的状态更新→组件重渲染流程
- 能解释 UmiJS 的约定式路由、运行时配置（app.tsx）、ProLayout 布局机制
- 能独立从零搭建一个基于 UmiJS Max + Ant Design + Zustand 的项目骨架

## Constraints
- 用户 React 零基础，需要从 JSX、组件、state/props 等基础概念讲起
- 所有讲解必须指向 ruoyi-react 真实源码路径，用实际代码做例子
- 每节课程聚焦一个可落地的知识点，给用户一个具体的小胜利
- 重点覆盖用户指定的四个主题：**动态路由、Hook、页面组成、持久化**
- 课程约 12-15 节，每节 5-10 分钟可读完

## Out of scope
- Node.js/npm/pnpm 等工具链的安装配置（假设已有基础环境）
- CSS 布局和样式细节（除非与组件库使用直接相关）
- 后端 Java 代码的讲解
- Vue 版本的 RuoYi 前端（仅关注 React 版本）
- Warm-Flow 工作流引擎的内部实现
