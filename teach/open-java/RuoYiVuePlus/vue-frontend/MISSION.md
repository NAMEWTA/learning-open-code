> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `mission.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# Mission: Vue 前端完整架构

## Why
RuoYi-Vue-Plus 的 Vue 前端是一个生产级企业后台管理系统的完整实现，基于 Vue 3 + TypeScript + Element Plus + Vite 技术栈。掌握它意味着你能够：独立搭建一个具备动态路由、按钮级权限控制、多布局切换、国际化、数据加密传输等企业级能力的中后台前端项目；深入理解前后端分离架构中前端如何与后端 Spring Boot 应用通过 Token 鉴权、菜单动态加载、字典数据联动等方式协同工作；获得一套可复用的前端工程化骨架，用于快速启动新的管理后台项目或为现有项目添加标准化模块。

## Success looks like
- 能从零启动项目，理解 `main.ts` -> `App.vue` -> `layout` -> `router` -> `views` 的完整初始化链路，并说出 Pinia store（app、user、permission、settings、tagsView、dict、notice）各自的职责边界
- 能追踪登录流程：从登录表单提交 -> Axios 请求拦截器注入加密和防重放 -> 后端返回 token -> `userStore` 存储角色/权限 -> `permissionStore.generateRoutes()` 拉取后端菜单树并动态注册路由 -> 路由守卫放行 -> 侧边栏渲染的完整闭环
- 能解释权限控制的三层体系：路由级（`filterAsyncRouter` 动态注册 + `dynamicRoutes` 本地过滤）、按钮级（`v-hasPermi` / `v-hasRoles` 指令通过 DOM 移除实现）、函数级（`auth.hasPermi/.hasRole` 插件方法），以及超级管理员 `*:*:*` 和 `admin` 角色的绕过逻辑
- 能利用项目已有的 composables（`useTableSelection`、`useFormDialog`、`useSearchReset` 等）和自定义组件（`Pagination`、`RightToolbar`、`ImageUpload`、`Editor` 等）快速组装一个带搜索、分页、批量操作的标准 CRUD 页面
- 能说出 Axios 实例的请求/响应拦截器链：Token 注入 -> 加密协商（RSA 加密 AES 密钥 + AES 加密请求体）-> 防重复提交 -> 响应解密 -> 统一错误码处理 -> 401 重新登录弹窗，并能基于此模式新增自定义拦截逻辑

## Constraints
- 需要已掌握 Vue 3 Composition API（`ref`、`reactive`、`computed`、`watch`、`onMounted`）和 TypeScript 基础（接口、泛型、枚举）
- 需要理解 SPA 路由基本概念（动态路由、嵌套路由、路由守卫）和 Pinia 状态管理基本用法
- 需要本地 Node.js >= 20.19.0 和 pnpm >= 10.0.0 运行环境
- 需要配套后端服务（RuoYi-Vue-Plus）运行在 `localhost:8080`，前端通过 Vite proxy 代理 API 请求

## Out of scope
- 不覆盖 Vue 3 框架本身的入门教学（响应式原理、模板语法、组件通信等基础概念）
- 不覆盖 CSS/SCSS/UnoCSS 的样式编写教学，仅涉及布局和主题切换机制
- 不覆盖后端 Java/Spring Boot 代码分析，仅涉及前后端 API 契约层面
- 不覆盖代码生成器（gen 模块）的具体实现细节
- 不覆盖 ECharts 图表配置和富文本编辑器（wangEditor）的业务使用教学
- 不覆盖 WebSocket/SSE 推送的底层通信协议细节
